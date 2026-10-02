# 词嵌入：从零实现 Word2Vec

> 一个词的含义，取决于与它相伴的词。用这个想法训练一个浅层网络，几何结构就会自然浮现。

**Type:** Build
**Languages:** Python
**Prerequisites:** 阶段 5 · 02（BoW + TF-IDF），阶段 3 · 03（从零实现反向传播）
**Time:** ~75 分钟

## 要解决的问题

TF-IDF（词频-逆文档频率）知道 `dog` 和 `puppy` 是不同的词，却不知道它们的含义几乎相同。用 `dog` 训练的分类器，无法泛化到一条谈论 `puppy` 的评论。你可以通过列举同义词来勉强弥补，但遇到罕见词、领域术语，以及任何你未曾考虑过的语言，这种办法就会失效。

你希望有一种表示，让 `dog` 和 `puppy` 在空间中彼此接近，让 `king - man + woman` 落在 `queen` 附近，也让用 `dog` 训练的模型无需额外处理，就能把一部分信号迁移到 `puppy`。

Word2Vec 给了我们这样的空间。两层神经网络、万亿 token（词元）规模的训练，于 2013 年发表。它的架构简单得几乎让人不好意思，但成果重塑了随后十年的自然语言处理（NLP）。

## 核心概念

**分布假设（distributional hypothesis）**（Firth，1957）：“要理解一个词，就看与它相伴的词。”如果两个词出现在相似的上下文中，它们的含义很可能也相近。

Word2Vec 有两种形式，都利用了这个想法。

- **Skip-gram。** 给定中心词，预测周围的词。窗口大小为 2 时，`cat -> (the, sat, on)`。
- **连续词袋（CBOW，continuous bag of words）。** 给定周围的词，预测中心词。`(the, sat, on) -> cat`。

Skip-gram 训练更慢，但对罕见词的处理更好。它成了默认选择。

这个网络只有一个隐藏层，而且没有非线性变换。输入是覆盖整个词表的 one-hot（独热）向量，输出是覆盖整个词表的 softmax。训练结束后，丢弃输出层，隐藏层的权重就是词嵌入（word embedding）。

```text
one-hot(center) ── W ──▶ hidden (d-dim) ── W' ──▶ softmax(vocab)
                          ^
                          this is the embedding
```

关键技巧在于：对 100k（k 表示千）个词计算 softmax，代价高得难以承受。Word2Vec 用**负采样（negative sampling）** 把它转为二分类任务，预测“这个上下文词是否出现在这个中心词附近”。每个训练词对只抽取少量负词（没有共同出现的词），而不对整个词表计算 softmax。

```figure
word-vector-arithmetic
```

## 动手实现

### 步骤 1：从语料库生成训练词对

```python
def skipgram_pairs(docs, window=2):
    pairs = []
    for doc in docs:
        for i, center in enumerate(doc):
            for j in range(max(0, i - window), min(len(doc), i + window + 1)):
                if i == j:
                    continue
                pairs.append((center, doc[j]))
    return pairs
```

```python
>>> skipgram_pairs([["the", "cat", "sat", "on", "mat"]], window=2)
[('the', 'cat'), ('the', 'sat'),
 ('cat', 'the'), ('cat', 'sat'), ('cat', 'on'),
 ('sat', 'the'), ('sat', 'cat'), ('sat', 'on'), ('sat', 'mat'),
 ...]
```

窗口中的每一对（中心词，上下文词）都是一个正训练样本。

### 步骤 2：嵌入表

使用两个矩阵。`W` 是中心词嵌入表，也就是你要保留的那一张；`W'` 是上下文词嵌入表，通常会被丢弃，有时也会与 `W` 取平均。

```python
import numpy as np


def init_embeddings(vocab_size, dim, seed=0):
    rng = np.random.default_rng(seed)
    W = rng.normal(0, 0.1, size=(vocab_size, dim))
    W_prime = rng.normal(0, 0.1, size=(vocab_size, dim))
    return W, W_prime
```

用较小的随机值初始化。词表大小为 10k、维数为 100，是实际可用的规模；用于教学时，50 个词 x 16 维就足以看出几何结构。

### 步骤 3：负采样目标

对于每个正词对 `(center, context)`，从词表中随机抽取 `k` 个词作为负样本。训练模型，使点积 `W[center] · W'[context]` 对正样本较高、对负样本较低。

```python
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -20, 20)))


def train_pair(W, W_prime, center_idx, context_idx, negative_indices, lr):
    v_c = W[center_idx]
    u_pos = W_prime[context_idx]
    u_negs = W_prime[negative_indices]

    pos_score = sigmoid(v_c @ u_pos)
    neg_scores = sigmoid(u_negs @ v_c)

    grad_center = (pos_score - 1) * u_pos
    for i, u in enumerate(u_negs):
        grad_center += neg_scores[i] * u

    W[context_idx] = W[context_idx]
    W_prime[context_idx] -= lr * (pos_score - 1) * v_c
    for i, neg_idx in enumerate(negative_indices):
        W_prime[neg_idx] -= lr * neg_scores[i] * v_c
    W[center_idx] -= lr * grad_center
```

关键公式是：正词对的逻辑损失（logistic loss，希望 sigmoid 接近 1），加上负词对的逻辑损失（希望 sigmoid 接近 0）。梯度流向两张表。完整推导见原论文；如果想真正记住它，不妨用纸笔推一遍。

### 步骤 4：在小型示例语料库上训练

```python
def train(docs, dim=16, window=2, k_neg=5, epochs=100, lr=0.05, seed=0):
    vocab = build_vocab(docs)
    vocab_size = len(vocab)
    rng = np.random.default_rng(seed)
    W, W_prime = init_embeddings(vocab_size, dim, seed=seed)
    pairs = skipgram_pairs(docs, window=window)

    for epoch in range(epochs):
        rng.shuffle(pairs)
        for center, context in pairs:
            c_idx = vocab[center]
            ctx_idx = vocab[context]
            negs = rng.integers(0, vocab_size, size=k_neg)
            negs = [n for n in negs if n != ctx_idx and n != c_idx]
            train_pair(W, W_prime, c_idx, ctx_idx, negs, lr)
    return vocab, W
```

在大型语料库上训练足够多轮（epoch）后，共享上下文的词会得到相似的中心词嵌入。在小型示例语料库上，这个效果还不明显；用数十亿 token 训练时，效果就非常显著。

### 步骤 5：类比技巧

```python
def nearest(vocab, W, target_vec, topk=5, exclude=None):
    exclude = exclude or set()
    inv_vocab = {i: w for w, i in vocab.items()}
    norms = np.linalg.norm(W, axis=1, keepdims=True) + 1e-9
    W_norm = W / norms
    target = target_vec / (np.linalg.norm(target_vec) + 1e-9)
    sims = W_norm @ target
    order = np.argsort(-sims)
    out = []
    for i in order:
        if i in exclude:
            continue
        out.append((inv_vocab[i], float(sims[i])))
        if len(out) == topk:
            break
    return out


def analogy(vocab, W, a, b, c, topk=5):
    v = W[vocab[b]] - W[vocab[a]] + W[vocab[c]]
    return nearest(vocab, W, v, topk=topk, exclude={vocab[a], vocab[b], vocab[c]})
```

使用预训练的 300d（d 表示向量维数）Google News 向量：

```python
>>> analogy(vocab, W, "man", "king", "woman")
[('queen', 0.71), ('monarch', 0.62), ('princess', 0.59), ...]
```

`king - man + woman = queen`。这并不是因为模型知道什么是王室，而是因为向量 `(king - man)` 捕捉到了类似“王室”的含义，把它加到 `woman` 上，就会落在王室女性所处的区域附近。

## 实际使用

从零编写 Word2Vec 是为了教学。生产环境中的 NLP 使用 `gensim`。

```python
from gensim.models import Word2Vec

sentences = [
    ["the", "cat", "sat", "on", "the", "mat"],
    ["the", "dog", "ran", "across", "the", "room"],
]

model = Word2Vec(
    sentences,
    vector_size=100,
    window=5,
    min_count=1,
    sg=1,
    negative=5,
    workers=4,
    epochs=30,
)

print(model.wv["cat"])
print(model.wv.most_similar("cat", topn=3))
```

在实际工作中，你几乎从不自己训练 Word2Vec，而是下载预训练向量。

- **GloVe**：Stanford 提出的共现矩阵分解方法。有 50d、100d、200d、300d 的检查点，通用覆盖面良好。第 04 课专门介绍 GloVe。
- **fastText**：Facebook 对 Word2Vec 的扩展，对字符连续 n 元片段（n-gram）进行嵌入。通过组合子词来处理词表外（OOV，out of vocabulary）词。见第 04 课。
- **在 Google News 上预训练的 Word2Vec**：300d，词表包含 3M（M 表示百万）个词，发表于 2013 年。至今每天仍有人下载。

### 到了 2026 年，Word2Vec 在哪些场景下仍有优势

- 轻量的领域专用检索。在笔记本电脑上，用医学摘要训练一小时，就能得到通用模型都无法捕捉的专用向量。
- 基于类比的特征工程。`gender_vector = mean(man - woman pairs)`。从其他词中减去这个向量，得到一个性别中立的轴。公平性研究至今仍在使用这种方法。
- 可解释性。100d 足够小，可以通过主成分分析（PCA）或 t-SNE（t 分布随机邻域嵌入）绘图，实际看到簇的形成。
- 任何需要在没有 GPU 的设备上运行推理的场景。Word2Vec 查找只需读取一行。

### Word2Vec 在哪些地方会失效

多义性（polysemy）是它绕不过去的限制。`bank` 只有一个向量，`river bank` 和 `financial bank` 共用它。`table` 表示电子表格或家具时，也共用一个向量。下游分类器无法仅从这个向量区分这些词义。

上下文嵌入（contextual embedding，例如 ELMo、BERT 及之后的所有 Transformer）解决了这个问题：根据周围的上下文，为词的每次出现生成不同的向量。这就是从 Word2Vec 到 BERT 的跨越：从静态变为上下文相关。阶段 7 介绍 Transformer 部分。

词表外问题是另一个缺陷。如果 `Zoomer-approved` 没有出现在训练数据中，Word2Vec 就从未见过它，也没有回退办法。fastText 用子词组合解决这个问题，见第 04 课。

## 交付成果

保存为 `outputs/skill-embedding-probe.md`：

```markdown
---
name: embedding-probe
description: Inspect a word2vec model. Run analogies, find neighbors, diagnose quality.
version: 1.0.0
phase: 5
lesson: 03
tags: [nlp, embeddings, debugging]
---

You probe trained word embeddings to verify they are working. Given a `gensim.models.KeyedVectors` object and a vocabulary, you run:

1. Three canonical analogy tests. `king : man :: queen : woman`. `paris : france :: tokyo : japan`. `walking : walked :: swimming : ?`. Report the top-1 result and its cosine.
2. Five nearest-neighbor tests on domain-specific words the user supplies. Print top-5 neighbors with cosines.
3. One symmetry check. `similarity(a, b) == similarity(b, a)` to within float precision.
4. One degenerate check. If any embedding has a norm below 0.01 or above 100, the model has a training bug. Flag it.

Refuse to declare a model good on analogy accuracy alone. Analogy benchmarks are gameable and do not transfer to downstream tasks. Recommend intrinsic + downstream evaluation together.
```

## 练习

1. **简单。** 在一个极小的语料库上运行训练循环，其中包含 20 个关于猫狗的句子。训练 200 轮后，验证 `nearest(vocab, W, W[vocab["cat"]])` 返回的前 3 个结果中包含 `dog`。如果没有，就增加训练轮数或扩大词表。
2. **中等。** 加入针对高频词的子采样（subsampling）。频率高于 `10^-5` 的词，会以与其频率成正比的概率从训练词对中删除。衡量这对罕见词相似度的影响。
3. **困难。** 在 20 Newsgroups 语料库上训练一个模型。计算两个偏见轴：`he - she` 和 `doctor - nurse`。将职业词投影到两个轴上，报告哪些职业的偏见差距最大。这就是公平性研究者使用的一类探查方法。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|-----------------|-----------------------|
| 词嵌入 | 用向量表示词 | 从上下文中学习到的稠密、低维表示，通常为 100-300 维。 |
| Skip-gram | Word2Vec 的技巧 | 根据中心词预测上下文词。比 CBOW 慢，但对罕见词效果更好。 |
| 负采样 | 训练捷径 | 用针对 `k` 个随机词的二分类，替代覆盖整个词表的 softmax。 |
| 静态嵌入 | 每个词对应一个向量 | 无论上下文如何都使用同一个向量，无法处理多义性。 |
| 上下文嵌入 | 对上下文敏感的向量 | 根据周围的词，为每次出现生成不同的向量。这正是 Transformer 产生的表示。 |
| OOV | 词表外 | 训练时未见过的词。Word2Vec 无法为这些词生成向量。 |

## 延伸阅读

- [Mikolov et al. (2013). Distributed Representations of Words and Phrases and their Compositionality](https://arxiv.org/abs/1310.4546)：介绍负采样的论文，篇幅短，易于阅读。
- [Rong, X. (2014). word2vec Parameter Learning Explained](https://arxiv.org/abs/1411.2738)：如果觉得原论文的数学内容晦涩，这篇给出了最清晰的梯度推导。
- [gensim Word2Vec tutorial](https://radimrehurek.com/gensim/models/word2vec.html)：在生产环境中真正有效的训练设置。
