# 词袋、TF-IDF 与文本表示

> 先计数，再思考。到了 2026 年，在定义清晰的任务上，TF-IDF（词频-逆文档频率）仍能胜过嵌入（embedding）。

**Type:** Build
**Languages:** Python
**Prerequisites:** 第 5 阶段 · 01（文本处理），第 2 阶段 · 02（从零实现线性回归）
**Time:** ~75 分钟

## 要解决的问题

模型需要数字，而你手里是字符串。

每条自然语言处理（NLP）流水线都必须回答同一个问题：如何把长度可变的 token（词元）流变成分类器能接收的固定大小向量？这个领域最早采用的答案，是最朴素却管用的办法：数一数词，做成向量。

这种向量支撑过的生产 NLP 应用，比任何嵌入模型都多：垃圾邮件过滤、主题分类、日志异常检测、搜索排序（在 BM25 之前）、第一批情感分析，以及学术 NLP 基准的最初十年。2026 年，面对范围明确的分类任务，实践者仍会优先选择它。它速度快、可解释；在只需关心词是否出现的任务上，其表现往往与拥有 400M（M 表示百万）参数的嵌入模型不相上下。

本课先从零构建词袋（Bag of Words，BoW），再构建 TF-IDF。接着展示如何用三行 scikit-learn 代码完成同样的工作，最后指出什么失效模式会让你转而采用嵌入。

## 核心概念

**词袋（Bag of Words，BoW）** 丢弃词序。对每篇文档，统计词表中每个词出现的次数。向量长度等于词表大小。位置 `i` 存放词 `i` 的计数。

**TF-IDF** 对 BoW 重新赋权。每篇文档里都出现的词没有信息量，因此降低其权重；在整个语料库中少见、却在某篇文档中频繁出现的词是有效信号，因此提高其权重。

```text
TF-IDF(w, d) = TF(w, d) * IDF(w)
             = count(w in d) / |d| * log(N / df(w))
```

其中，`TF` 是词在文档中的词频（term frequency），`df` 是文档频率（document frequency，即有多少篇文档包含该词），`N` 是文档总数。`log` 让那些普遍出现的词的权重保持在有界范围内。

关键性质：两种方法都会生成稀疏向量（sparse vector），各坐标轴的含义可解释。查看训练好的分类器权重，就能知道哪些词会把文档推向各个类别。对于 768 维的 BERT 嵌入，你无法这样做。

```figure
bow-tfidf
```

## 动手实现

### 步骤 1：构建词表

```python
def build_vocab(docs):
    vocab = {}
    for doc in docs:
        for token in doc:
            if token not in vocab:
                vocab[token] = len(vocab)
    return vocab
```

输入：已分词文档的列表（任何词级分词器都可以；本课的 `code/main.py` 使用一个转为小写的简化版本）。输出：`{word: index}` 字典。稳定的插入顺序意味着，索引 0 对应第一篇文档中最先遇到的词。不同实现的约定不同；scikit-learn 按字母顺序排序。

### 步骤 2：词袋

```python
def bag_of_words(docs, vocab):
    matrix = [[0] * len(vocab) for _ in docs]
    for i, doc in enumerate(docs):
        for token in doc:
            if token in vocab:
                matrix[i][vocab[token]] += 1
    return matrix
```

```python
>>> docs = [["cat", "sat", "on", "mat"], ["cat", "cat", "ran"]]
>>> vocab = build_vocab(docs)
>>> bag_of_words(docs, vocab)
[[1, 1, 1, 1, 0], [2, 0, 0, 0, 1]]
```

行对应文档，列对应词表索引。元素 `[i][j]` 表示“词 `j` 在文档 `i` 中出现了多少次”。文档 1 中的 `cat` 计数是两次，因为它确实出现了两次。文档 0 中的 `ran` 计数是零，因为它没有出现。

### 步骤 3：词频与文档频率

```python
import math


def term_frequency(doc_bow, doc_length):
    return [c / doc_length if doc_length else 0 for c in doc_bow]


def document_frequency(bow_matrix):
    df = [0] * len(bow_matrix[0])
    for row in bow_matrix:
        for j, count in enumerate(row):
            if count > 0:
                df[j] += 1
    return df


def inverse_document_frequency(df, n_docs):
    return [math.log((n_docs + 1) / (d + 1)) + 1 for d in df]
```

这里有两个值得说明的平滑技巧。`(n+1)/(d+1)` 避免了 `log(x/0)`。末尾的 `+1` 确保每篇文档里都出现的词，其逆文档频率（IDF）仍为 1（而不是 0），与 scikit-learn 的默认值一致。其他实现会直接使用 `log(N/df)`。两种方式都可行，平滑版本更易用。

### 步骤 4：TF-IDF

```python
def tfidf(bow_matrix):
    n_docs = len(bow_matrix)
    df = document_frequency(bow_matrix)
    idf = inverse_document_frequency(df, n_docs)
    out = []
    for row in bow_matrix:
        length = sum(row)
        tf = term_frequency(row, length)
        out.append([tf_j * idf_j for tf_j, idf_j in zip(tf, idf)])
    return out
```

```python
>>> docs = [
...     ["the", "cat", "sat"],
...     ["the", "dog", "sat"],
...     ["the", "cat", "ran"],
... ]
>>> vocab = build_vocab(docs)
>>> bow = bag_of_words(docs, vocab)
>>> tfidf(bow)
```

三篇文档，五个词表词项（`the`、`cat`、`sat`、`dog`、`ran`）。`the` 在三篇文档中都出现，因此 IDF 较低；`dog` 只出现在一篇中，因此 IDF 较高。向量是稀疏的（大多数元素很小），有区分力的词会凸显出来。

### 步骤 5：对每行做 L2 归一化

```python
def l2_normalize(matrix):
    out = []
    for row in matrix:
        norm = math.sqrt(sum(x * x for x in row))
        out.append([x / norm if norm else 0 for x in row])
    return out
```

不做归一化（normalization）时，较长文档会得到更大的向量，并主导相似度分数。L2 归一化将每篇文档都放到单位超球面上。此时，行之间的余弦相似度（cosine similarity）就是点积。

## 实际使用

scikit-learn 提供可用于生产的版本。

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

docs = ["the cat sat on the mat", "the dog sat on the mat", "the cat ran"]

bow_vectorizer = CountVectorizer()
bow = bow_vectorizer.fit_transform(docs)
print(bow_vectorizer.get_feature_names_out())
print(bow.toarray())

tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(docs)
print(tfidf.toarray().round(3))
```

`CountVectorizer` 一次调用就能完成分词、词表构建和 BoW。`TfidfVectorizer` 在此基础上增加 IDF 加权和 L2 归一化。两者都返回稀疏矩阵。对于 100k（k 表示千）篇文档，稠密版本无法装入内存；在分类器要求稠密表示之前，都应保持稀疏表示。

这些参数会显著改变结果：

| 参数 | 作用 |
|-----|--------|
| `ngram_range=(1, 2)` | 包含二元片段（bigrams）。通常能改善分类效果。 |
| `min_df=2` | 丢弃出现在少于 2 篇文档中的词。在含噪数据上缩减词表。 |
| `max_df=0.95` | 丢弃出现在超过 95% 文档中的词。无须硬编码列表，即可近似实现停用词去除。 |
| `stop_words="english"` | scikit-learn 内置的停用词列表。是否使用取决于任务；情感分析*不应*去掉否定词。 |
| `sublinear_tf=True` | 使用 `1 + log(tf)`，而非原始 `tf`。当一个词在同一篇文档中重复多次时会有帮助。 |

### TF-IDF 仍然占优的场景（截至 2026 年）

- 垃圾邮件检测、主题标注、日志异常标记。重要的是词是否出现，而非语义上的细微差别。
- 数据量较少的情况（数百个已标注样例）。TF-IDF 加逻辑回归没有预训练成本。
- 任何看重延迟的场景。TF-IDF 加线性模型可在微秒级给出结果；通过 Transformer 为一篇文档生成嵌入需要 10-100ms。
- 必须解释预测的系统。查看分类器的系数，正系数最大的词就是原因。

### TF-IDF 失效的场景

一种失效模式是对语义视而不见。看看这两篇文档：

- "The movie was not good at all."（这部电影一点也不好。）
- "The movie was excellent."（这部电影非常出色。）

一篇是负面评论，另一篇是正面评论。它们的 TF-IDF 重叠词项恰好是 `{the, movie, was}`。词袋分类器必须记住：`not` 出现在 `good` 附近时，会使标签翻转。有足够的数据时它能学到这一点，但始终不如理解句法的模型那样自然。

另一种失效模式是推理时遇到词表外（out-of-vocabulary）词。如果 `Zoomer-approved` 这个 token 从未在训练中出现过，基于 IMDb 评论训练的 BoW 模型就不知道该如何处理它。子词嵌入（第 04 课）能处理这种情况，TF-IDF 则不能。

### 混合方案：TF-IDF 加权嵌入

2026 年，中等数据量分类任务的务实默认方案是：把 TF-IDF 权重用作词嵌入上的注意力。

```python
def tfidf_weighted_embedding(doc, tfidf_scores, embedding_table, dim):
    vec = [0.0] * dim
    total_weight = 0.0
    for token in doc:
        if token not in embedding_table or token not in tfidf_scores:
            continue
        weight = tfidf_scores[token]
        emb = embedding_table[token]
        for i in range(dim):
            vec[i] += weight * emb[i]
        total_weight += weight
    if total_weight == 0:
        return vec
    return [v / total_weight for v in vec]
```

嵌入提供语义表示能力，TF-IDF 则突出稀有词。分类器在汇聚后的向量上训练。当已标注样例少于约 50k 时，在情感、主题和意图分类上，这种方法优于单独使用其中任何一种。

## 交付成果

保存为 `outputs/prompt-vectorization-picker.md`：

```markdown
---
name: vectorization-picker
description: Given a text-classification task, recommend BoW, TF-IDF, embeddings, or a hybrid.
phase: 5
lesson: 02
---

You recommend a text-vectorization strategy. Given a task description, output:

1. Representation (BoW, TF-IDF, transformer embeddings, or a hybrid). Explain why in one sentence.
2. Specific vectorizer configuration. Name the library. Quote the arguments (`ngram_range`, `min_df`, `max_df`, `sublinear_tf`, `stop_words`).
3. One failure mode to test before shipping.

Refuse to recommend embeddings when the user has under 500 labeled examples unless they show evidence of semantic failure in a TF-IDF baseline. Refuse to remove stopwords for sentiment analysis (negations carry signal). Flag class imbalance as needing more than a vectorizer change.

Example input: "Classifying 30k customer support tickets into 12 categories. Most tickets are 2-3 sentences. English only. Need explainability for audit logs."

Example output:

- Representation: TF-IDF. 30k examples is not small; explainability requirement rules out dense embeddings.
- Config: `TfidfVectorizer(ngram_range=(1, 2), min_df=3, max_df=0.95, sublinear_tf=True, stop_words=None)`. Keep stopwords because category keywords sometimes are stopwords ("not working" vs "working").
- Failure to test: verify `min_df=3` does not drop rare category keywords. Run `get_feature_names_out` filtered by class and eyeball.
```

## 练习

1. **简单。** 在经过 L2 归一化的 TF-IDF 输出上实现 `cosine_similarity(doc_vec_a, doc_vec_b)`。验证相同文档得分为 1.0，词表没有交集的文档得分为 0.0。
2. **中等。** 为 `bag_of_words` 添加 `n-gram`（连续 n 元片段）支持。参数 `n` 用于统计 `n` 元片段。测试：当 `n=2` 时，对 `["the", "cat", "sat"]` 应产生 `["the cat", "cat sat"]` 的二元片段计数。
3. **困难。** 使用 GloVe 100d 向量（下载一次后缓存）构建上述 TF-IDF 加权嵌入混合方案。在 20 Newsgroups 数据集上，对比它与单独使用 TF-IDF、单独使用均值汇聚嵌入的分类准确率。报告各自在哪些场景下占优。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|-----------------|-----------------------|
| BoW | 词频向量 | 一篇文档中各词表词项的计数。丢弃词序。 |
| TF | 词频 | 一个词在文档中的计数，可选择按文档长度归一化。 |
| DF | 文档频率 | 至少包含该词一次的文档数。 |
| IDF | 逆文档频率 | 经过平滑的 `log(N / df)`。降低到处都出现的词的权重。 |
| 稀疏向量 | 大部分为零 | 词表通常包含 10k-100k 个词；其中大多数不会出现在某一篇给定文档中。 |
| 余弦相似度 | 向量夹角 | L2 归一化向量的点积。1 表示相同，0 表示正交。 |

## 延伸阅读

- [scikit-learn — feature extraction from text](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)：权威 API 参考，附带每个参数的说明。
- [Salton, G., & Buckley, C. (1988). Term-weighting approaches in automatic text retrieval](https://www.sciencedirect.com/science/article/pii/0306457388900210)：让 TF-IDF 成为十年间默认方法的论文。
- ["Why TF-IDF Still Beats Embeddings" — Ashfaque Thonikkadavan (Medium)](https://medium.com/@cmtwskb/why-tf-idf-still-beats-embeddings-ad85c123e1b2)：2026 年对传统方法何时胜出、为何胜出的看法。
