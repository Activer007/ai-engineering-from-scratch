# 从零构建分词器

> 第 01 课给了你一个玩具，这一课给你一件利器。

**Type:** Build
**Languages:** Python
**Prerequisites:** 阶段 10，课程 01（分词器：BPE、WordPiece、SentencePiece）
**Time:** ~90 分钟

## 学习目标

- 构建一个生产级 BPE（字节对编码）分词器（tokenizer），处理 Unicode、空白字符规范化以及特殊 token（词元）
- 实现字节级回退（byte-level fallback），让分词器无需未知 token 就能编码任意输入，包括 emoji、中日韩文字（CJK）和代码
- 添加预分词（pre-tokenization）正则表达式，在应用 BPE 合并前，先按词边界切分文本
- 在语料库上训练自定义分词器，并在多语言文本上与 tiktoken 比较，评估其压缩率

## 要解决的问题

你在第 01 课构建的 BPE 分词器可以处理英文文本。现在把日语丢给它试试，或者 emoji，又或者混用了制表符和空格的 Python 代码。

它就出问题了。

问题不在 BPE，而在于实现不完整。生产用的分词器要处理任意编码的原始字节，在切分前对 Unicode 做规范化，管理永不参与合并的特殊 token，将预分词与子词切分衔接起来，而且完成这一切的速度必须足够快，不能成为处理 15 trillion（万亿）个 token 的训练流程的瓶颈。

GPT-2 的分词器有 50,257 个 token，Llama 3 有 128,256 个，GPT-4 则大约有 100,000 个。这些可不是玩具级的规模。这些词表背后的合并表（merge table）是在数百 gigabytes（十亿字节）文本上训练出来的，而围绕它们构建的整套机制，包括规范化、预分词、特殊 token 注入以及聊天模板（chat template）格式化，正是只能处理 "hello world" 的分词器与能够处理整个互联网的分词器之间的区别。

接下来，你就要构建这套机制。

## 核心概念

### 完整流程

生产用的分词器并不是单一算法，而是由五个阶段组成的流程，每个阶段解决一种问题。

```mermaid
graph LR
    A[Raw Text] --> B[Normalize]
    B --> C[Pre-Tokenize]
    C --> D[BPE Merge]
    D --> E[Special Tokens]
    E --> F[Token IDs]

    style A fill:#1a1a2e,stroke:#e94560,color:#fff
    style B fill:#1a1a2e,stroke:#e94560,color:#fff
    style C fill:#1a1a2e,stroke:#e94560,color:#fff
    style D fill:#1a1a2e,stroke:#e94560,color:#fff
    style E fill:#1a1a2e,stroke:#e94560,color:#fff
    style F fill:#1a1a2e,stroke:#e94560,color:#fff
```

每个阶段各有职责：

| 阶段 | 做什么 | 为什么重要 |
|-------|-------------|----------------|
| 规范化 | Unicode NFKC 规范化，可选转小写、去除重音符号 | "fi" 连字（U+FB01）变成 "fi"（两个字符）。否则，同一个词会得到不同的 token。 |
| 预分词 | 在 BPE 之前将文本切分成片段 | 防止 BPE 跨词边界合并。"the cat" 绝不应该产生 "e c" 这样的 token。 |
| BPE 合并 | 将学到的合并规则应用到字节序列 | 压缩的核心，将原始字节变成子词 token。 |
| 特殊 token | 插入 [BOS]、[EOS]、[PAD] 和聊天模板标记 | 这些 token 的 ID 固定，永远不参与 BPE 合并。模型需要它们来表达结构。 |
| ID 映射 | 将 token 字符串转换为整数 ID | 模型看到的是整数，而不是字符串。 |

### 字节级 BPE

第 01 课的分词器处理的是 UTF-8 字节，这个选择是正确的。但我们略过了一个重要问题：如果这些字节不是有效的 UTF-8，会发生什么？

字节级 BPE 将所有可能的字节值（0-255）都视为有效 token，从而解决这个问题。基础词表恰好包含 256 个条目。任何文件，无论是文本、二进制文件还是损坏的文件，都可以在不产生未知 token 的情况下完成分词。

GPT-2 加了一个技巧：将每个字节映射为可打印的 Unicode 字符，让词表保持可读。在它的映射中，字节 0x20（空格）会变成字符 "G"。这只是显示层面的处理，算法并不在意。

真正强大之处在于：字节级 BPE 能处理地球上的每一种语言。汉字每个占 3 个 UTF-8 字节，日文字符可能占 3-4 个字节。阿拉伯文字、天城文、emoji，全都是字节序列。BPE 算法在这些字节序列中寻找模式的方式，与它在英文 ASCII 字节中寻找模式的方式完全相同。

### 预分词

在 BPE 处理文本之前，你需要先将文本切分成片段。这样可以防止合并算法创建跨词边界的 token。

GPT-2 使用一个正则表达式来切分文本：

```text
'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+
```

这个表达式会切分缩约词（"don't" 变为 "don" + "'t"）、可带前导空格的单词、数字、标点和空白字符。前导空格会与单词保留在一起，因此 "the cat" 会变成 [" the", " cat"]，而不是 ["the", " ", "cat"]。

Llama 使用 SentencePiece（分词库），完全跳过正则表达式。它把原始字节流当作一条长序列，让 BPE 算法自行确定边界。这样更简单，但也让 BPE 有更大的自由度来创建跨词 token。

这种选择很重要。GPT-2 的正则表达式会阻止分词器学到这样的合并：把一个词末尾的 "the" 与下一个词开头的 "the" 合在一起。SentencePiece 则允许这样做，有时能带来更高效的压缩，但 token 也会更难解释。

### 特殊 token

每个生产用的分词器都会为结构标记预留 token ID：

| token | 用途 | 使用者 |
|-------|---------|---------|
| `[BOS]` / `<s>` | 序列起始 | Llama 3、GPT |
| `[EOS]` / `</s>` | 序列结束 | 所有模型 |
| `[PAD]` | 用于批次对齐的填充 | BERT、T5 |
| `[UNK]` | 未知 token（字节级 BPE 无需使用它） | BERT、WordPiece |
| `<\|im_start\|>` | 聊天消息边界的起始 | ChatGPT、Qwen |
| `<\|im_end\|>` | 聊天消息边界的结束 | ChatGPT、Qwen |
| `<\|user\|>` | 用户回合标记 | Llama 3 |
| `<\|assistant\|>` | 助手回合标记 | Llama 3 |

特殊 token 永远不会被 BPE 拆分。合并算法运行之前，会先精确匹配它们，将其替换为固定 ID，再对周围的文本正常分词。

### 聊天模板

这是大多数人感到困惑、也是大多数实现出错的地方。

向聊天模型发送消息时，API（应用程序编程接口）接收的是一个消息列表：

```text
[
  {"role": "system", "content": "You are helpful."},
  {"role": "user", "content": "Hello"},
  {"role": "assistant", "content": "Hi there!"}
]
```

模型看到的不是 JSON，而是一条平铺的 token 序列。聊天模板借助特殊 token，将消息转换成这样的序列。每个模型的做法都不一样：

```text
Llama 3:
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You are helpful.<|eot_id|><|start_header_id|>user<|end_header_id|>

Hello<|eot_id|><|start_header_id|>assistant<|end_header_id|>

Hi there!<|eot_id|>

ChatGPT:
<|im_start|>system
You are helpful.<|im_end|>
<|im_start|>user
Hello<|im_end|>
<|im_start|>assistant
Hi there!<|im_end|>
```

模板弄错了，模型就会输出糟糕的结果。它训练时使用的是一个精确的格式。任何偏差，无论是少了一个换行、调换了一个 token，还是多了一个空格，都会让输入偏离训练分布。

### 速度

对于生产环境中的分词，Python 太慢了。

tiktoken（OpenAI）用 Rust 编写，并提供 Python 绑定。HuggingFace tokenizers 也用 Rust 编写，SentencePiece 则使用 C++。它们相对纯 Python 实现可获得 10-100 倍的加速。

举个规模上的例子：为 Llama 3 预训练对 15 trillion（万亿）个 token 做分词，若每秒处理 1 million（百万）个 token（较快的 Python 实现），需要 174 天；若每秒处理 100 million（百万）个 token（Rust 实现），则需要 1.7 天。

你用 Python 构建分词器，是为了理解算法。在生产环境中，你会使用编译型实现，只通过它的 Python 封装层操作。

```figure
weight-tying
```

## 动手实现

### 步骤 1：字节级编码

先打好基础：将任意字符串转换为字节序列，将每个字节映射为可打印字符以供显示，再反向还原。

```python
def bytes_to_tokens(text):
    return list(text.encode("utf-8"))

def tokens_to_text(token_bytes):
    return bytes(token_bytes).decode("utf-8", errors="replace")
```

用多语言文本测试，观察字节数量：

```python
texts = [
    ("English", "hello"),
    ("Chinese", "你好"),
    ("Emoji", "🔥"),
    ("Mixed", "hello你好🔥"),
]

for label, text in texts:
    b = bytes_to_tokens(text)
    print(f"{label}: {len(text)} chars -> {len(b)} bytes -> {b}")
```

"hello" 是 5 个字节，"你好" 是 6 个字节（每个字符 3 个），火焰 emoji 是 4 个字节。字节级分词器并不关心文本属于哪种语言，字节就是字节。

### 步骤 2：用正则表达式构建预分词器

使用 GPT-2 的正则表达式将文本切分成片段，再由 BPE 独立处理每个片段。

```python
import re

try:
    import regex
    GPT2_PATTERN = regex.compile(
        r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
    )
except ImportError:
    GPT2_PATTERN = re.compile(
        r"""'(?:[sdmt]|ll|ve|re)| ?[a-zA-Z]+| ?[0-9]+| ?[^\s\w]+|\s+(?!\S)|\s+"""
    )

def pre_tokenize(text):
    return [match.group() for match in GPT2_PATTERN.finditer(text)]
```

`regex` 模块支持 Unicode 属性转义（`\p{L}` 表示字母，`\p{N}` 表示数字）。标准库的 `re` 模块不支持，因此这里回退到 ASCII 字符类。对于生产环境中的多语言分词器，请安装 `regex`。

试一试：

```python
print(pre_tokenize("Hello, world! Don't stop."))
# [' Hello', ',', ' world', '!', " Don", "'t", ' stop', '.']
```

前导空格仍与单词保留在一起，缩约词在撇号处切开，标点则成为单独的片段。BPE 永远不会跨越这些边界合并 token。

### 步骤 3：对字节序列执行 BPE

核心算法与第 01 课相同，但现在会独立处理预分词得到的各个片段。

```python
from collections import Counter

def get_byte_pairs(chunks):
    pairs = Counter()
    for chunk in chunks:
        byte_seq = list(chunk.encode("utf-8"))
        for i in range(len(byte_seq) - 1):
            pairs[(byte_seq[i], byte_seq[i + 1])] += 1
    return pairs

def apply_merge(byte_seq, pair, new_id):
    merged = []
    i = 0
    while i < len(byte_seq):
        if i < len(byte_seq) - 1 and byte_seq[i] == pair[0] and byte_seq[i + 1] == pair[1]:
            merged.append(new_id)
            i += 2
        else:
            merged.append(byte_seq[i])
            i += 1
    return merged
```

### 步骤 4：处理特殊 token

特殊 token 需要精确匹配和固定 ID。它们完全绕过 BPE。

```python
class SpecialTokenHandler:
    def __init__(self):
        self.special_tokens = {}
        self.pattern = None

    def add_token(self, token_str, token_id):
        self.special_tokens[token_str] = token_id
        escaped = [re.escape(t) for t in sorted(self.special_tokens.keys(), key=len, reverse=True)]
        self.pattern = re.compile("|".join(escaped))

    def split_with_specials(self, text):
        if not self.pattern:
            return [(text, False)]
        parts = []
        last_end = 0
        for match in self.pattern.finditer(text):
            if match.start() > last_end:
                parts.append((text[last_end:match.start()], False))
            parts.append((match.group(), True))
            last_end = match.end()
        if last_end < len(text):
            parts.append((text[last_end:], False))
        return parts
```

### 步骤 5：完整的分词器类

将各部分衔接起来：规范化、按特殊 token 切分、预分词、BPE 合并，再映射为 ID。

```python
import unicodedata

class ProductionTokenizer:
    def __init__(self):
        self.merges = {}
        self.vocab = {i: bytes([i]) for i in range(256)}
        self.special_handler = SpecialTokenHandler()
        self.next_id = 256

    def normalize(self, text):
        return unicodedata.normalize("NFKC", text)

    def train(self, text, num_merges):
        text = self.normalize(text)
        chunks = pre_tokenize(text)
        chunk_bytes = [list(chunk.encode("utf-8")) for chunk in chunks]

        for i in range(num_merges):
            pairs = Counter()
            for seq in chunk_bytes:
                for j in range(len(seq) - 1):
                    pairs[(seq[j], seq[j + 1])] += 1
            if not pairs:
                break
            best = max(pairs, key=pairs.get)
            new_id = self.next_id
            self.next_id += 1
            self.merges[best] = new_id
            self.vocab[new_id] = self.vocab[best[0]] + self.vocab[best[1]]
            chunk_bytes = [apply_merge(seq, best, new_id) for seq in chunk_bytes]

    def add_special_token(self, token_str):
        token_id = self.next_id
        self.next_id += 1
        self.special_handler.add_token(token_str, token_id)
        self.vocab[token_id] = token_str.encode("utf-8")
        return token_id

    def encode(self, text):
        text = self.normalize(text)
        parts = self.special_handler.split_with_specials(text)
        all_ids = []
        for part_text, is_special in parts:
            if is_special:
                all_ids.append(self.special_handler.special_tokens[part_text])
            else:
                for chunk in pre_tokenize(part_text):
                    byte_seq = list(chunk.encode("utf-8"))
                    for pair, new_id in self.merges.items():
                        byte_seq = apply_merge(byte_seq, pair, new_id)
                    all_ids.extend(byte_seq)
        return all_ids

    def decode(self, ids):
        byte_parts = []
        for token_id in ids:
            if token_id in self.vocab:
                byte_parts.append(self.vocab[token_id])
        return b"".join(byte_parts).decode("utf-8", errors="replace")

    def vocab_size(self):
        return len(self.vocab)
```

### 步骤 6：多语言测试

真正的考验来了：把英文、中文、emoji 和代码都交给它。

```python
corpus = (
    "The quick brown fox jumps over the lazy dog. "
    "The quick brown fox runs through the forest. "
    "Machine learning models process natural language. "
    "Deep learning transforms how we build software. "
    "def train(model, data): return model.fit(data) "
    "def predict(model, x): return model(x) "
)

tok = ProductionTokenizer()
tok.train(corpus, num_merges=50)

bos = tok.add_special_token("<|begin|>")
eos = tok.add_special_token("<|end|>")

test_texts = [
    "The quick brown fox.",
    "你好世界",
    "Hello 🌍 World",
    "def foo(x): return x + 1",
    f"<|begin|>Hello<|end|>",
]

for text in test_texts:
    ids = tok.encode(text)
    decoded = tok.decode(ids)
    print(f"Input:   {text}")
    print(f"Tokens:  {len(ids)} ids")
    print(f"Decoded: {decoded}")
    print()
```

每个汉字会产生 3 个字节，这个 emoji 会产生 4 个字节。它们都不会让分词器崩溃，也都不会产生未知 token。这就是字节级 BPE 的力量。

## 实际使用

### 比较真实的分词器

加载 Llama 3、GPT-4 和 Mistral 实际使用的分词器，看看它们各自如何处理同一段多语言文本。

```python
import tiktoken

gpt4_enc = tiktoken.get_encoding("cl100k_base")

test_paragraph = "Machine learning is powerful. 机器学习很强大。 L'apprentissage automatique est puissant. 🤖💪"

tokens = gpt4_enc.encode(test_paragraph)
pieces = [gpt4_enc.decode([t]) for t in tokens]
print(f"GPT-4 ({len(tokens)} tokens): {pieces}")
```

```python
from transformers import AutoTokenizer

llama_tok = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")
mistral_tok = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")

for name, tok in [("Llama 3", llama_tok), ("Mistral", mistral_tok)]:
    tokens = tok.encode(test_paragraph)
    pieces = tok.convert_ids_to_tokens(tokens)
    print(f"{name} ({len(tokens)} tokens): {pieces[:20]}...")
```

同一段文本会得到不同的 token 数。Llama 3 的词表规模为 128K，会更积极地合并常见模式；GPT-4 的词表规模为 100K，处于中间；Mistral 的词表规模为 32K，产生的 token 更多，但嵌入层也更小。

取舍始终相同：词表越大，序列越短，但参数也越多。

## 交付成果

本课产出一份用于构建和调试生产用分词器的提示词（prompt）。参见 `outputs/prompt-tokenizer-builder.md`。

## 练习

1. **简单：** 添加一个 `get_token_bytes(id)` 方法，显示任意 token ID 对应的原始字节。用它检查最常见的合并 token 实际表示什么。
2. **中等：** 实现一个 Llama 风格的预分词器，按空白字符和数字切分，但保留前导空格。在同一份语料库上，将其词表与 GPT-2 正则表达式方案的词表进行比较。
3. **困难：** 添加一个聊天模板方法，接收 `{"role": ..., "content": ...}` 消息列表，生成符合 Llama 3 聊天格式的正确 token 序列。将结果与 HuggingFace 实现进行对照测试。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|----------------------|
| 字节级 BPE | “处理字节的分词器” | 基础词表包含 256 个字节值的 BPE，无需未知 token 就能处理任意输入 |
| 预分词 | “在 BPE 之前切分” | 基于正则表达式或规则的切分，防止 BPE 跨词边界合并 |
| NFKC 规范化 | “清理 Unicode” | 先做规范分解，再做兼容组合；"fi" 连字变为 "fi"，全角 "A" 变为 "A" |
| 聊天模板 | “消息如何变成 token” | 将 role/content 消息列表转换为平铺 token 序列的精确格式；每个模型各不相同，必须与训练格式一致 |
| 特殊 token | “控制 token” | 绕过 BPE 的预留 token ID，包括 [BOS]、[EOS]、[PAD] 和聊天标记；在合并前精确匹配 |
| 平均每词 token 数（fertility） | “每个词有多少 token” | 输出 token 数与输入词数之比；GPT-4 的英文为 1.3，韩文为 2-3，越高意味着越浪费上下文 |
| tiktoken | “OpenAI 分词器” | 提供 Python 绑定的 Rust BPE 实现，比纯 Python 快 10-100 倍 |
| 合并表 | “词表” | 训练过程中学到的有序字节对合并列表，这就是分词器学到的知识 |

## 延伸阅读

- [OpenAI tiktoken source](https://github.com/openai/tiktoken) -- GPT-3.5/4 使用的 Rust BPE 实现
- [HuggingFace tokenizers](https://github.com/huggingface/tokenizers) -- 支持 BPE、WordPiece（子词分词算法）和 Unigram（基于概率的子词分词算法）的 Rust 分词库
- [Llama 3 paper (Meta, 2024)](https://arxiv.org/abs/2407.21783) -- 关于 128K 词表及分词器训练的详细介绍
- [SentencePiece (Kudo & Richardson, 2018)](https://arxiv.org/abs/1808.06226) -- 不依赖特定语言的分词
- [GPT-2 tokenizer source](https://github.com/openai/gpt-2/blob/master/src/encoder.py) -- 原始的字节到 Unicode 映射
