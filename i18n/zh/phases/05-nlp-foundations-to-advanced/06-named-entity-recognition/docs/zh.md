# 命名实体识别

> 把名称提取出来。听上去很简单，直到你遇到模糊的边界、嵌套实体（nested entity）和领域术语。

**Type:** Build
**Languages:** Python
**Prerequisites:** 阶段 5 · 02（词袋 BoW + TF-IDF），阶段 5 · 03（词嵌入）
**Time:** ~75 分钟

## 要解决的问题

“Apple sued Google over its iPhone search deal in the US.” 五个实体：Apple（ORG）、Google（ORG）、iPhone（PRODUCT）、search deal（也许算）、US（GPE）。好的命名实体识别（NER）系统会把它们全部提取出来，并正确标注类型。差的系统会漏掉 iPhone，把水果 Apple 和公司 Apple 混为一谈，还会把“US”标成 PERSON。

NER 是每条结构化抽取流水线背后的主力：简历解析、合规日志扫描、病历匿名化、搜索查询理解、为聊天机器人回复提供依据，以及法律合同信息抽取。你很少直接看到它，却一直在依赖它。

本课沿着经典方法（基于规则、HMM、CRF）一路走到现代方法（BiLSTM-CRF，再到 Transformer）。每一步都解决前一种方法的某个局限。理解这条演进规律，就是本课的重点。

## 核心概念

**BIO 标注（BIO tagging）** （或 BILOU）把实体抽取转化为序列标注（sequence labeling）问题。为每个 token（词元）标注 `B-TYPE`（实体开头）、`I-TYPE`（实体内部）或 `O`（不属于任何实体）。

```text
Apple    B-ORG
sued     O
Google   B-ORG
over     O
its      O
iPhone   B-PRODUCT
search   O
deal     O
in       O
the      O
US       B-GPE
.        O
```

包含多个 token 的实体可以串联起来：`New B-GPE`、`York I-GPE`、`City I-GPE`。理解 BIO 的模型能够提取任意文本跨度（span）。

架构的演进顺序如下：

- **基于规则。** 正则表达式 + 专名词表（gazetteer）查询。对已知实体的精确率很高，对新实体的覆盖率为零。
- **HMM。** 隐 Markov 模型（Hidden Markov Model）。建模给定标记时 token 的发射概率，以及标记之间的转移概率。使用 Viterbi 解码，以带标注的数据训练。
- **CRF。** 条件随机场（Conditional Random Field）。与 HMM 类似，但属于判别式模型，因此可以混合使用任意特征（词形模式（word shape）、大小写、相邻词）。在 2026 年，它仍是资源有限的生产部署中经典的主力方法。
- **BiLSTM-CRF。** 双向长短期记忆网络与 CRF 的组合。使用神经网络特征代替手工设计的特征。LSTM 从两个方向读取句子，上层 CRF 保证标记序列一致。
- **基于 Transformer。** 用 token 分类头微调（fine-tune）BERT。准确率最高，计算量也最大。

```figure
ner-bio-tagging
```

## 动手实现

### 步骤 1：BIO 标注辅助函数

```python
def spans_to_bio(tokens, spans):
    labels = ["O"] * len(tokens)
    for start, end, label in spans:
        labels[start] = f"B-{label}"
        for i in range(start + 1, end):
            labels[i] = f"I-{label}"
    return labels


def bio_to_spans(tokens, labels):
    spans = []
    current = None
    for i, label in enumerate(labels):
        if label.startswith("B-"):
            if current:
                spans.append(current)
            current = (i, i + 1, label[2:])
        elif label.startswith("I-") and current and current[2] == label[2:]:
            current = (current[0], i + 1, current[2])
        else:
            if current:
                spans.append(current)
                current = None
    if current:
        spans.append(current)
    return spans
```

```python
>>> tokens = ["Apple", "sued", "Google", "over", "iPhone", "sales", "."]
>>> labels = ["B-ORG", "O", "B-ORG", "O", "B-PRODUCT", "O", "O"]
>>> bio_to_spans(tokens, labels)
[(0, 1, 'ORG'), (2, 3, 'ORG'), (4, 5, 'PRODUCT')]
```

### 步骤 2：手工设计的特征

对于经典的非神经网络 NER，特征是关键。下面是一些有用的特征：

```python
def token_features(token, prev_token, next_token):
    return {
        "lower": token.lower(),
        "is_upper": token.isupper(),
        "is_title": token.istitle(),
        "has_digit": any(c.isdigit() for c in token),
        "suffix_3": token[-3:].lower(),
        "shape": word_shape(token),
        "prev_lower": prev_token.lower() if prev_token else "<BOS>",
        "next_lower": next_token.lower() if next_token else "<EOS>",
    }


def word_shape(word):
    out = []
    for c in word:
        if c.isupper():
            out.append("X")
        elif c.islower():
            out.append("x")
        elif c.isdigit():
            out.append("d")
        else:
            out.append(c)
    return "".join(out)
```

`word_shape("iPhone")` 返回 `xXxxxx`。`word_shape("USA-2024")` 返回 `XXX-dddd`。大小写模式是识别专名的强信号。

### 步骤 3：简单的规则与词典基线

```python
ORG_GAZETTEER = {"Apple", "Google", "Microsoft", "OpenAI", "Meta", "Amazon", "Netflix"}
GPE_GAZETTEER = {"US", "USA", "UK", "India", "Germany", "France"}
PRODUCT_GAZETTEER = {"iPhone", "Android", "Windows", "ChatGPT", "Claude"}


def rule_based_ner(tokens):
    labels = []
    for token in tokens:
        if token in ORG_GAZETTEER:
            labels.append("B-ORG")
        elif token in GPE_GAZETTEER:
            labels.append("B-GPE")
        elif token in PRODUCT_GAZETTEER:
            labels.append("B-PRODUCT")
        else:
            labels.append("O")
    return labels
```

生产环境的专名词表包含从 Wikipedia 和 DBpedia 抓取的数百万个条目。覆盖情况不错，消歧能力却很差：例如区分公司 `Apple` 和水果。这就是统计模型胜出的原因。

### 步骤 4：加入 CRF（示意，非完整实现）

如果没有概率论基础，用 50 行代码从零实现完整 CRF 并不能帮助你理解它。这里使用 `sklearn-crfsuite`：

```python
import sklearn_crfsuite

def to_features(tokens):
    out = []
    for i, tok in enumerate(tokens):
        prev = tokens[i - 1] if i > 0 else ""
        nxt = tokens[i + 1] if i + 1 < len(tokens) else ""
        out.append({
            "word.lower()": tok.lower(),
            "word.isupper()": tok.isupper(),
            "word.istitle()": tok.istitle(),
            "word.isdigit()": tok.isdigit(),
            "word.suffix3": tok[-3:].lower(),
            "word.shape": word_shape(tok),
            "prev.word.lower()": prev.lower(),
            "next.word.lower()": nxt.lower(),
            "BOS": i == 0,
            "EOS": i == len(tokens) - 1,
        })
    return out


crf = sklearn_crfsuite.CRF(algorithm="lbfgs", c1=0.1, c2=0.1, max_iterations=100, all_possible_transitions=True)
X_train = [to_features(s) for s in sentences_tokenized]
crf.fit(X_train, bio_labels_train)
```

`c1` 和 `c2` 分别对应 L1 和 L2 正则化。`all_possible_transitions=True` 让模型学到非法序列（例如在 `O` 后面接 `I-ORG`）不太可能出现。CRF 就是这样在你不手写约束的情况下保证 BIO 一致性的。

### 步骤 5：BiLSTM-CRF 增加了什么

特征改由模型学习。输入是 token 嵌入（embedding，例如 GloVe 或 fastText）。LSTM 分别从左到右、从右到左读取文本，拼接后的隐藏状态进入 CRF 输出层。CRF 仍然保证标记序列一致；LSTM 则用学到的特征取代手工设计的特征。

```python
import torch
import torch.nn as nn


class BiLSTM_CRF_Head(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, n_labels):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, bidirectional=True, batch_first=True)
        self.fc = nn.Linear(hidden_dim * 2, n_labels)

    def forward(self, token_ids):
        e = self.embed(token_ids)
        h, _ = self.lstm(e)
        emissions = self.fc(h)
        return emissions
```

CRF 层使用 `torchcrf.CRF`（pip install pytorch-crf）。相比使用手工特征的 CRF，它的提升可以测量出来，但通常比你预期的小，除非你有数万条带标注的句子。

## 实际使用

spaCy 自带可直接使用的生产级 NER。

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple sued Google over its iPhone search deal in the US.")
for ent in doc.ents:
    print(f"{ent.text:20s} {ent.label_}")
```

```text
Apple                ORG
Google               ORG
iPhone               ORG
US                   GPE
```

注意，`iPhone` 被标成了 `ORG`，而不是 `PRODUCT`。spaCy 小模型对产品实体的覆盖较弱。大模型（`en_core_web_lg`）表现更好，Transformer 模型（`en_core_web_trf`）还要更好。

使用 Hugging Face 进行基于 BERT 的 NER：

```python
from transformers import pipeline

ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
print(ner("Apple sued Google over its iPhone in the US."))
```

```text
[{'entity_group': 'ORG', 'word': 'Apple', ...},
 {'entity_group': 'ORG', 'word': 'Google', ...},
 {'entity_group': 'MISC', 'word': 'iPhone', ...},
 {'entity_group': 'LOC', 'word': 'US', ...}]
```

`aggregation_strategy="simple"` 会把连续的 B-X、I-X token 合并成一个文本跨度。不使用它时，你得到的是 token 级标签，需要自行合并。

### 基于大语言模型（LLM）的 NER（2026 年的选择）

零样本（zero-shot）和少样本（few-shot）LLM NER 如今在许多领域已经能与微调模型竞争；当带标注的数据稀缺时，其表现还明显更好。

- **零样本提示。** 给 LLM 一份实体类型列表和一个 schema（结构定义）示例，要求输出 JSON。无需额外训练即可使用；在新领域中的准确率一般。
- **ZeroTuneBio 风格的提示。** 将任务分解为候选抽取 → 含义解释 → 判断 → 复查。多阶段提示词（而非单次提示）能显著提高生物医学 NER 的准确率。同样的模式也适用于法律、金融和科学领域。
- **结合检索增强生成（RAG）的动态提示。** 每次推理调用时，都从小规模已标注的种子集中检索最相似的带标注示例，动态构建少样本提示词。在 2026 年的基准测试中，相比静态提示，这种方法让 GPT-4 在生物医学 NER 上的 F1 提高了 11-12%。
- **按实体类型分解。** 对长文档而言，如果一次调用同时提取所有实体类型，召回率会随文档变长而下降。可以为每种实体类型各做一遍抽取。推理成本更高，但准确率也明显更高。这是处理临床记录和法律合同的标准模式。

截至 2026 年的生产建议：收集训练数据之前，先建立 LLM 零样本基线。F1 往往已经足够好，让你根本不必再微调。

### 经典 NER 仍然占优的场景

即使可以使用 LLM，经典 NER 在以下情况下仍然占优：

- 延迟预算低于 50ms。
- 你有数千个带标注的示例，并且需要 98%+ 的 F1。
- 领域具有稳定的本体（ontology），预训练的 CRF 或 BiLSTM 能很好地迁移。
- 监管约束要求使用本地部署的非生成式模型。

### 容易失效的情况

- **领域偏移（domain shift）。** 用 CoNLL 训练的 NER 处理法律合同时，表现比专名词表还差。应在自己的领域上进行微调。
- **嵌套实体。** “Bank of America Tower”同时是 ORG 和 FACILITY。标准 BIO 无法表示重叠的文本跨度。你需要嵌套 NER，即多遍处理或基于跨度的模型。
- **长实体。** “United States Federal Deposit Insurance Corporation.” token 级模型有时会把它拆开。使用 `aggregation_strategy` 或进行后处理。
- **样本稀少的类型。** 例如医疗 NER 中的 DRUG_BRAND、ADVERSE_EVENT、DOSE 标签，通用模型对此一无所知。Scispacy 和 BioBERT 是这类任务的起点。

## 交付成果

保存为 `outputs/skill-ner-picker.md`：

```markdown
---
name: ner-picker
description: Pick the right NER approach for a given extraction task.
version: 1.0.0
phase: 5
lesson: 06
tags: [nlp, ner, extraction]
---

Given a task description (domain, label set, language, latency, data volume), output:

1. Approach. Rule-based + gazetteer, CRF, BiLSTM-CRF, or transformer fine-tune.
2. Starting model. Name it (spaCy model ID, Hugging Face checkpoint ID, or "custom, trained from scratch").
3. Labeling strategy. BIO, BILOU, or span-based. Justify in one sentence.
4. Evaluation. Use `seqeval`. Always report entity-level F1 (not token-level).

Refuse to recommend fine-tuning a transformer for under 500 labeled examples unless the user already has a pretrained domain model. Flag nested entities as needing span-based or multi-pass models. Require a gazetteer audit if the user mentions "production scale" and labels are unchanged from CoNLL-2003.
```

## 练习

1. **简单。** 实现 `bio_to_spans`（`spans_to_bio` 的逆操作），并在 10 个句子上验证往返转换的一致性。
2. **中等。** 在 CoNLL-2003 英文 NER 数据集上训练上面的 sklearn-crfsuite CRF，使用 `seqeval` 报告各实体类型的 F1。典型结果约为 84 F1。
3. **困难。** 在特定领域（医疗、法律或金融）的 NER 数据集上微调 `distilbert-base-cased`，与 spaCy 小模型比较。记录数据泄漏检查，并写下让你意外的发现。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|-----------------|-----------------------|
| NER | 提取名称 | 为 token 跨度标注类型（PERSON、ORG、GPE、DATE 等）。 |
| BIO | 标注方案 | `B-X` 表示开始，`I-X` 表示延续，`O` 表示实体之外。 |
| BILOU | 更好的 BIO | 增加 `L-X`（最后一个）和 `U-X`（单个），让边界更清晰。 |
| CRF | 结构化分类器 | 对标签之间的转移建模，而不只是对发射建模。保证序列合法。 |
| 嵌套 NER | 重叠实体 | 某个跨度与其内部的子跨度分别是不同的实体。BIO 无法表达这种情况。 |
| 实体级（Entity-level）F1 | 合适的 NER 指标 | 预测跨度必须与真实跨度完全匹配。token 级 F1 会高估准确性。 |

## 延伸阅读

- [Lample et al. (2016). Neural Architectures for Named Entity Recognition](https://arxiv.org/abs/1603.01360) — BiLSTM-CRF 的经典论文。
- [Devlin et al. (2018). BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805) — 介绍后来成为标准的 token 分类模式。
- [spaCy linguistic features — named entities](https://spacy.io/usage/linguistic-features#named-entities) — `Doc.ents` 和 `Span` 各项属性的实用参考。
- [seqeval](https://github.com/chakki-works/seqeval) — 正确的指标计算库，始终使用它。
