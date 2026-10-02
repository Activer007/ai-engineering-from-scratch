# 文本处理：分词、词干提取与词形还原

> 语言是连续的，模型是离散的。预处理是两者之间的桥梁。

**Type:** Build
**Languages:** Python
**Prerequisites:** 第 2 阶段 · 14（朴素 Bayes）
**Time:** ~45 分钟

## 要解决的问题

模型读不懂“The cats were running.”，它读取的是整数。

每个自然语言处理（NLP）系统都从同样的三个问题出发：一个词从哪里开始？这个词的词根是什么？如何在有帮助时把“run”、“running”、“ran”视为同一个东西，而在没有帮助时把它们区分开来？

分词出了错，模型学到的就是垃圾。如果分词器（tokenizer）把 `don't` 当作一个 token（词元），却把 `do n't` 当作两个，训练分布就会分裂。如果词干提取器（stemmer）把 `organization` 和 `organ` 合并成同一个词干，主题建模就会失效。如果词形还原器（lemmatizer）需要词性上下文，而你没有提供，动词就会被当作名词处理。

本课从零构建这三个预处理步骤，再展示 NLTK 和 spaCy 如何完成同样的工作，让你看清其中的取舍。

## 核心概念

三种操作，各有职责，也各有失效模式。

**分词（Tokenization）** 将字符串拆成 token。“token”刻意保持宽泛，因为合适的粒度取决于任务：经典 NLP 按词，Transformer 按子词，不使用空白分隔的语言按字符。

**词干提取（Stemming）** 用规则截去后缀。速度快、处理激进，但不够智能。`running -> run`。`organization -> organ`。第二个例子就是它的失效模式。

**词形还原（Lemmatization）** 利用语法知识，将词还原为词典原形（lemma）。速度较慢，但准确，需要查找表或词形分析器。`ran -> run`（需要知道“ran”是“run”的过去式）。`better -> good`（需要了解比较级形式）。

经验法则：速度重要且能容忍噪声时，使用词干提取（搜索索引、粗略分类）；语义重要时，使用词形还原（问答、语义搜索，以及任何用户会阅读的内容）。

```figure
edit-distance
```

## 动手实现

### 步骤 1：基于正则表达式的词级分词器

最简单而实用的分词器会在非字母数字字符处拆分，同时将标点保留为单独的 token。它不完美，也不是最终版本，但一行代码就能运行。

```python
import re

def tokenize(text):
    return re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?|[0-9]+|[^\sA-Za-z0-9]", text)
```

按优先顺序有三种模式：内部可带撇号的词（`don't`、`it's`）；纯数字；任何单个非空白、非字母数字字符，作为独立 token（标点）。

```python
>>> tokenize("The cats weren't running at 3pm.")
['The', 'cats', "weren't", 'running', 'at', '3', 'pm', '.']
```

需要注意的失效模式：`3pm` 会被拆成 `['3', 'pm']`，因为正则表达式在连续字母和连续数字之间使用了分支选择。对大多数任务来说，这已经够用。URL、电子邮件地址、话题标签都会被拆散。用于生产时，应把专门的模式放在通用模式之前。

### 步骤 2：Porter 词干提取器（仅步骤 1a）

完整的 Porter 算法包含五个阶段的规则。仅步骤 1a 就覆盖了最常见的英语后缀，也足以展示这种处理模式。

```python
def stem_step_1a(word):
    if word.endswith("sses"):
        return word[:-2]
    if word.endswith("ies"):
        return word[:-2]
    if word.endswith("ss"):
        return word
    if word.endswith("s") and len(word) > 1:
        return word[:-1]
    return word
```

```python
>>> [stem_step_1a(w) for w in ["caresses", "ponies", "caress", "cats"]]
['caress', 'poni', 'caress', 'cat']
```

从上往下读这些规则。`ies -> i` 规则解释了为什么 `ponies -> poni`，而不是 `pony`。真正的 Porter 算法还有步骤 1b，会修正这个问题。规则之间会竞争，靠前的规则优先。规则的顺序比任何单条规则都重要。

### 步骤 3：基于查表的词形还原器

真正的词形还原需要词形学（morphology）知识。便于教学实现的版本使用一个小型词典原形表，再加上一套回退规则。

```python
LEMMA_TABLE = {
    ("running", "VERB"): "run",
    ("ran", "VERB"): "run",
    ("runs", "VERB"): "run",
    ("better", "ADJ"): "good",
    ("best", "ADJ"): "good",
    ("cats", "NOUN"): "cat",
    ("cat", "NOUN"): "cat",
    ("were", "VERB"): "be",
    ("was", "VERB"): "be",
    ("is", "VERB"): "be",
}

def lemmatize(word, pos):
    key = (word.lower(), pos)
    if key in LEMMA_TABLE:
        return LEMMA_TABLE[key]
    if pos == "VERB" and word.endswith("ing"):
        return word[:-3]
    if pos == "NOUN" and word.endswith("s"):
        return word[:-1]
    return word.lower()
```

```python
>>> lemmatize("running", "VERB")
'run'
>>> lemmatize("cats", "NOUN")
'cat'
>>> lemmatize("better", "ADJ")
'good'
>>> lemmatize("watched", "VERB")
'watched'
```

最后一个例子是教学重点。`watched` 不在我们的表中，而回退规则只处理 `ing`。真正的词形还原涵盖 `ed`、不规则动词、形容词比较级，以及伴随语音变化的复数（`children -> child`）。因此，生产系统会使用 WordNet、spaCy 的 morphologizer（词形标注组件），或完整的词形分析器。

### 步骤 4：把它们接成流水线

```python
def preprocess(text, pos_tagger=None):
    tokens = tokenize(text)
    stems = [stem_step_1a(t.lower()) for t in tokens]
    tags = pos_tagger(tokens) if pos_tagger else [(t, "NOUN") for t in tokens]
    lemmas = [lemmatize(word, pos) for word, pos in tags]
    return {"tokens": tokens, "stems": stems, "lemmas": lemmas}
```

缺少的部分是词性标注器（POS tagger）。第 5 阶段 · 07（词性标注）会构建一个。现在，先默认把所有内容标成 `NOUN`，并明确这一局限。

## 实际使用

NLTK 和 spaCy 提供可用于生产的版本，各用几行代码即可。

### NLTK

```python
import nltk
nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger_eng")

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag

text = "The cats were running."
tokens = word_tokenize(text)
stems = [PorterStemmer().stem(t) for t in tokens]
lemmatizer = WordNetLemmatizer()
tagged = pos_tag(tokens)


def nltk_pos_to_wordnet(tag):
    if tag.startswith("V"):
        return "v"
    if tag.startswith("J"):
        return "a"
    if tag.startswith("R"):
        return "r"
    return "n"


lemmas = [lemmatizer.lemmatize(t, nltk_pos_to_wordnet(tag)) for t, tag in tagged]
```

`word_tokenize` 能处理缩约形式（contractions）、Unicode，以及你的正则表达式漏掉的边界情况。`PorterStemmer` 执行全部五个阶段。`WordNetLemmatizer` 需要把词性标记（POS tag）从 NLTK 的 Penn Treebank 标记体系转换成 WordNet 的缩写集合。上面的标记转换代码，正是大多数教程会跳过的部分。

### spaCy

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("The cats were running.")

for token in doc:
    print(token.text, token.lemma_, token.pos_)
```

```text
The      the     DET
cats     cat     NOUN
were     be      AUX
running  run     VERB
.        .       PUNCT
```

spaCy 将整条流水线封装在 `nlp(text)` 背后，分词、词性标注和词形还原都会执行。大规模处理时，它比 NLTK 更快，开箱即用的准确性也更高。代价是你不容易单独替换其中的组件。

### 何时选择哪一种

| 场景 | 选择 |
|-----------|------|
| 教学、研究、替换组件 | NLTK |
| 生产、多语言、速度重要 | spaCy |
| Transformer 流水线（反正都要用模型自带的分词器） | 使用 `tokenizers` / `transformers`，跳过经典预处理 |

### 两个没人提醒你的失效模式

大多数教程讲完算法就结束了。有两件事会让实际的预处理流水线栽跟头，却几乎从不被提及。

**可复现性漂移（Reproducibility drift）。** NLTK 和 spaCy 的分词及词形还原行为会随版本变化。在 spaCy 2.x 中得到 `['do', "n't"]` 的输入，在 3.x 中可能得到 `["don't"]`。模型训练时面对的是一种分布，推理时却变成了另一种。准确率悄悄下降，却没人知道原因。在 `requirements.txt` 中固定库版本。编写预处理回归测试，固定 20 个示例句子的预期分词结果，每次升级都运行。

**训练与推理不一致（Training / inference mismatch）。** 训练时进行激进的预处理（转小写、去除停用词、词干提取），部署时却使用用户的原始输入，性能就会大幅下滑。这是生产 NLP 中最常见的失效原因。如果训练时做了预处理，推理时就必须运行完全相同的函数。应把预处理函数随模型包一起交付，而不是留在 notebook 单元格中，让模型服务团队重新编写。

## 交付成果

一个可复用的提示词（prompt），帮助工程师选择预处理策略，无须读完三本教材。

保存为 `outputs/prompt-preprocessing-advisor.md`：

```markdown
---
name: preprocessing-advisor
description: Recommends a tokenization, stemming, and lemmatization setup for an NLP task.
phase: 5
lesson: 01
---

You advise on classical NLP preprocessing. Given a task description, you output:

1. Tokenization choice (regex, NLTK word_tokenize, spaCy, or transformer tokenizer). Explain why.
2. Whether to stem, lemmatize, both, or neither. Explain why.
3. Specific library calls. Name the functions. Quote the POS-tag translation if NLTK is involved.
4. One failure mode the user should test for.

Refuse to recommend stemming for user-visible text. Refuse to recommend lemmatization without POS tags. Flag non-English input as needing a different pipeline.
```

## 练习

1. **简单。** 扩展 `tokenize`，将 URL 保留为单个 token。测试：`tokenize("Visit https://example.com today.")` 应产生一个 URL token。
2. **中等。** 实现 Porter 步骤 1b。如果词中包含元音，且以 `ed` 或 `ing` 结尾，就去掉该后缀。处理双辅音规则（`hopping -> hop`，而不是 `hopp`）。
3. **困难。** 构建一个使用 WordNet 查表的词形还原器；当 WordNet 没有对应条目时，回退到你的 Porter 词干提取器。在带标注的语料上测量准确率，并与单独使用 WordNet、单独使用 Porter 比较。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|-----------------|-----------------------|
| token（词元） | 一个词 | 模型使用的任何单位，可以是词、子词、字符或字节。 |
| 词干（Stem） | 词的根 | 根据规则剥离后缀后的结果，不一定是真实存在的词。 |
| 词典原形（Lemma） | 词典形式 | 查词典时使用的形式，需要语法上下文才能正确求得。 |
| 词性标记（POS tag） | 词性 | NOUN、VERB、ADJ 等类别，是准确进行词形还原所需的信息。 |
| 词形学（Morphology） | 词形变化规则 | 词如何随时态、数、格而改变形式，词形还原依赖这些知识。 |

## 延伸阅读

- [Porter, M. F. (1980). An algorithm for suffix stripping](https://tartarus.org/martin/PorterStemmer/def.txt)：原始论文，只有五页，至今仍是最清楚的解释。
- [spaCy 101 — linguistic features](https://spacy.io/usage/linguistic-features)：实际流水线如何连接。
- [NLTK book, chapter 3](https://www.nltk.org/book/ch03.html)：你还没想到过的分词边界情况。
