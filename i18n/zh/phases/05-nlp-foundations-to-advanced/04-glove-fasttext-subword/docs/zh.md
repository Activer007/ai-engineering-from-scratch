# GloVe、FastText 与子词嵌入

> Word2Vec 为每个词训练一个词嵌入（word embedding）。GloVe 对共现矩阵进行分解。FastText 为词的片段学习嵌入。BPE（字节对编码）则搭起了通向 Transformer 的桥梁。

**Type:** Build
**Languages:** Python
**Prerequisites:** 阶段 5 · 03（从零实现 Word2Vec）
**Time:** ~45 分钟

## 要解决的问题

Word2Vec 留下了两个未解决的问题。

首先，当时还有一条并行的研究路线，直接分解共现矩阵（LSA、HAL），而不是进行在线 Skip-gram 更新。Word2Vec 的迭代方法是从根本上更好，还是差异仅仅源于两种方法处理计数的方式？**GloVe** 回答了这个问题：为矩阵分解精心选择损失函数，就能达到或超过 Word2Vec 的效果，而且训练成本更低。

其次，这两种方法都无法处理从未见过的词，例如 `Zoomer-approved`、`dogecoin`、上周刚造出的任何专有名词，以及罕见词根的每一种屈折形式。**FastText** 通过为字符连续 n 元片段（character n-gram）学习嵌入解决了这个问题：一个词是其各个组成部分的总和，其中包括语素（morpheme），因此即使是词表外（OOV，out-of-vocabulary）的词，也能得到合理的向量。

第三，Transformer 出现后，问题又发生了变化。词级词表的上限大约是一百万个条目，而真实语言的开放程度远不止于此。**字节对编码（BPE）** 及其相关方法通过学习一个由常见子词单元组成、能够覆盖一切的词表，解决了这个问题。每一种现代大语言模型（LLM）的每一种现代分词器，都是子词分词器。

本课将逐一介绍这三种方法，再说明何时该选哪一种。

## 核心概念

**GloVe（Global Vectors，全局向量）。** 构建词与词的共现矩阵 `X`，其中 `X[i][j]` 表示词 `j` 在词 `i` 的上下文中出现的次数。训练向量，使其满足 `v_i · v_j + b_i + b_j ≈ log(X[i][j])`。对损失加权，避免高频词对占据主导。就这么简单。

**FastText。** 一个词是其字符连续 n 元片段与该词本身之和。`where` 变成 `<wh, whe, her, ere, re>, <where>`。词向量就是这些组成部分向量的总和。按 Word2Vec 的方式训练。好处是：未见过的词（`whereupon`）可以由已知的连续 n 元片段组合而成。

**BPE（Byte-Pair Encoding，字节对编码）。** 从由单个字节（或字符）组成的词表开始。统计语料中每一对相邻符号的次数。把出现最频繁的一对合并为一个新的 token（词元）。重复 `k` 轮迭代。结果是一个包含 `k + 256` 个 token 的词表，其中常见序列（`ing`、`tion`、`the`）各自成为单个 token，罕见词则被拆成已知的片段。每个句子都能分出相应的 token。

```figure
n5-subword-merge
```

## 动手实现

### GloVe：分解共现矩阵

```python
import numpy as np
from collections import Counter


def build_cooccurrence(docs, window=5):
    pair_counts = Counter()
    vocab = {}
    for doc in docs:
        for token in doc:
            if token not in vocab:
                vocab[token] = len(vocab)
    for doc in docs:
        indexed = [vocab[t] for t in doc]
        for i, center in enumerate(indexed):
            for j in range(max(0, i - window), min(len(indexed), i + window + 1)):
                if i != j:
                    distance = abs(i - j)
                    pair_counts[(center, indexed[j])] += 1.0 / distance
    return vocab, pair_counts


def glove_train(vocab, pair_counts, dim=16, epochs=100, lr=0.05, x_max=100, alpha=0.75, seed=0):
    n = len(vocab)
    rng = np.random.default_rng(seed)
    W = rng.normal(0, 0.1, size=(n, dim))
    W_tilde = rng.normal(0, 0.1, size=(n, dim))
    b = np.zeros(n)
    b_tilde = np.zeros(n)

    for epoch in range(epochs):
        for (i, j), x_ij in pair_counts.items():
            weight = (x_ij / x_max) ** alpha if x_ij < x_max else 1.0
            diff = W[i] @ W_tilde[j] + b[i] + b_tilde[j] - np.log(x_ij)
            coef = weight * diff

            grad_W_i = coef * W_tilde[j]
            grad_W_tilde_j = coef * W[i]
            W[i] -= lr * grad_W_i
            W_tilde[j] -= lr * grad_W_tilde_j
            b[i] -= lr * coef
            b_tilde[j] -= lr * coef

    return W + W_tilde
```

有两个组成部分值得明确说明。加权函数 `f(x) = (x/x_max)^alpha` 会降低极高频词对（例如 `(the, and)`）的权重，避免它们主导损失。最终嵌入是 `W`（中心词）与 `W_tilde`（上下文词）两张表之和。将两者相加是一种已发表的技巧，通常比只使用其中一张表效果更好。

### FastText：感知子词的嵌入

```python
def char_ngrams(word, n_min=3, n_max=6):
    wrapped = f"<{word}>"
    grams = {wrapped}
    for n in range(n_min, n_max + 1):
        for i in range(len(wrapped) - n + 1):
            grams.add(wrapped[i:i + n])
    return grams
```

```python
>>> char_ngrams("where")
{'<where>', '<wh', 'whe', 'her', 'ere', 're>', '<whe', 'wher', 'here', 'ere>', '<wher', 'where', 'here>'}
```

每个词都由它的连续 n 元片段集合表示（通常每个片段有 3 到 6 个字符）。词嵌入就是其连续 n 元片段嵌入的总和。进行 Skip-gram 训练时，把这种表示放到 Word2Vec 原先使用单个向量的位置即可。

```python
def fasttext_vector(word, ngram_table):
    grams = char_ngrams(word)
    vecs = [ngram_table[g] for g in grams if g in ngram_table]
    if not vecs:
        return None
    return np.sum(vecs, axis=0)
```

对于一个未见过的词，只要它的某些连续 n 元片段已知，仍然可以得到一个向量。`whereupon` 与 `where` 共享 `<wh`、`her`、`ere` 和 `<where`，因此两者在向量空间中的位置接近。

### BPE：学习得到的子词词表

```python
def learn_bpe(corpus, k_merges):
    vocab = Counter()
    for word, freq in corpus.items():
        tokens = tuple(word) + ("</w>",)
        vocab[tokens] = freq

    merges = []
    for _ in range(k_merges):
        pair_freq = Counter()
        for tokens, freq in vocab.items():
            for a, b in zip(tokens, tokens[1:]):
                pair_freq[(a, b)] += freq
        if not pair_freq:
            break
        best = pair_freq.most_common(1)[0][0]
        merges.append(best)

        new_vocab = Counter()
        for tokens, freq in vocab.items():
            new_tokens = []
            i = 0
            while i < len(tokens):
                if i + 1 < len(tokens) and (tokens[i], tokens[i + 1]) == best:
                    new_tokens.append(tokens[i] + tokens[i + 1])
                    i += 2
                else:
                    new_tokens.append(tokens[i])
                    i += 1
            new_vocab[tuple(new_tokens)] = freq
        vocab = new_vocab
    return merges


def apply_bpe(word, merges):
    tokens = list(word) + ["</w>"]
    for a, b in merges:
        new_tokens = []
        i = 0
        while i < len(tokens):
            if i + 1 < len(tokens) and tokens[i] == a and tokens[i + 1] == b:
                new_tokens.append(a + b)
                i += 2
            else:
                new_tokens.append(tokens[i])
                i += 1
        tokens = new_tokens
    return tokens
```

```python
>>> corpus = Counter({"low": 5, "lower": 2, "newest": 6, "widest": 3})
>>> merges = learn_bpe(corpus, k_merges=10)
>>> apply_bpe("lowest", merges)
['low', 'est</w>']
```

第一轮迭代会合并最常见的相邻符号对。经过足够多轮迭代后，常见子串（`low`、`est`、`tion`）会成为单个 token，罕见词则能被清晰地拆分。

实际的 GPT / BERT / T5 分词器会学习 30k-100k（k 表示千）次合并。结果是：任何文本都能分成长度有界、由已知 ID 构成的序列，永远不会出现 OOV。

## 实际使用

在实际工作中，你很少会自己训练这些方法，而是加载预训练检查点。

```python
import fasttext.util
fasttext.util.download_model("en", if_exists="ignore")
ft = fasttext.load_model("cc.en.300.bin")
print(ft.get_word_vector("whereupon").shape)
print(ft.get_word_vector("zoomerapproved").shape)
```

在 Transformer 时代，要进行 BPE 风格的子词分词：

```python
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("gpt2")
print(tok.tokenize("unbelievably tokenized"))
```

```text
['un', 'bel', 'iev', 'ably', 'Ġtoken', 'ized']
```

前缀 `Ġ` 标记词边界（这是 GPT-2 的约定）。每一种现代分词器都属于 BPE 的变体、WordPiece（子词分词算法，用于 BERT）或 SentencePiece（分词库，用于 T5、LLaMA）。

### 何时选择哪一种

| 使用场景 | 选择 |
|-----------|------|
| 需要预训练的通用词向量，不要求容忍 OOV | GloVe 300d（d 表示维数） |
| 需要预训练的通用词向量，必须处理拼写错误 / 新造词 / 词形变化丰富的语言 | FastText |
| 任何要输入 Transformer 的内容（训练或推理） | 使用模型随附的分词器。绝不更换。 |
| 从零训练自己的语言模型 | 先在自己的语料上训练一个 BPE 或 SentencePiece 分词器 |
| 用线性模型进行生产环境中的文本分类 | 仍然选择 TF-IDF（词频-逆文档频率）。参见第 02 课。 |

## 交付成果

保存为 `outputs/skill-embeddings-picker.md`：

```markdown
---
name: tokenizer-picker
description: Pick a tokenization approach for a new language model or text pipeline.
version: 1.0.0
phase: 5
lesson: 04
tags: [nlp, tokenization, embeddings]
---

Given a task and dataset description, you output:

1. Tokenization strategy (word-level, BPE, WordPiece, SentencePiece, byte-level). One-sentence reason.
2. Vocabulary size target (e.g., 32k for an English-only LM, 64k-100k for multilingual).
3. Library call with the exact training command. Name the library. Quote the arguments.
4. One reproducibility pitfall. Tokenizer-model mismatch is the single most common silent production bug; call out which pair must be used together.

Refuse to recommend training a custom tokenizer when the user is fine-tuning a pretrained LLM. Refuse to recommend word-level tokenization for any model targeting production inference. Flag non-English / multi-script corpora as needing SentencePiece with byte fallback.
```

## 练习

1. **简单。** 运行 `char_ngrams("playing")` 和 `char_ngrams("played")`。计算两个连续 n 元片段集合的 Jaccard 重叠度。你应该能看到大量共享片段（`pla`、`lay`、`play`），这就是 FastText 能在不同词形变体之间良好迁移的原因。
2. **中等。** 扩展 `learn_bpe`，跟踪词表增长。绘制每个语料字符对应的 token 数随合并次数变化的曲线。你应该看到最初压缩很快，随后渐近于每个 token 约 ~2-3 个字符。
3. **困难。** 在 Shakespeare 全集上训练一个执行 1k 次合并的 BPE。比较常见词与罕见专有名词的分词结果。测量前后平均每词 token 数。写下让你意外的发现。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|-----------------|-----------------------|
| 共现矩阵 | 词与词的频次表 | `X[i][j]` = 词 `j` 在词 `i` 周围的窗口中出现的次数。 |
| 子词 | 词的一部分 | 字符连续 n 元片段（FastText）或学习得到的 token（BPE/WordPiece/SentencePiece）。 |
| BPE | 字节对编码 | 迭代合并出现最频繁的相邻符号对，直到词表达到目标大小。 |
| OOV | 词表外 | 模型从未见过的词。Word2Vec/GloVe 无法处理，FastText 和 BPE 可以处理。 |
| 字节级 BPE | 对原始字节执行 BPE | GPT-2 的方案。词表从 256 个字节开始，因此任何内容都不会成为 OOV。 |

## 延伸阅读

- [Pennington, Socher, Manning (2014). GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf) — GloVe 论文，共七页，至今仍给出了最好的损失函数推导。
- [Bojanowski et al. (2017). Enriching Word Vectors with Subword Information](https://arxiv.org/abs/1607.04606) — FastText。
- [Sennrich, Haddow, Birch (2016). Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909) — 将 BPE 引入现代 NLP 的论文。
- [Hugging Face tokenizer summary](https://huggingface.co/docs/transformers/tokenizer_summary) — BPE、WordPiece 与 SentencePiece 在实际使用中的区别。
