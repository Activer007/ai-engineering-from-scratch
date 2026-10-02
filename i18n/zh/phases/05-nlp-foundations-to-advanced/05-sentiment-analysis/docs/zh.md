# 情感分析

> 自然语言处理（NLP）的经典任务。关于传统文本分类，你需要掌握的大部分知识都会在这里出现。

**Type:** Build
**Languages:** Python
**Prerequisites:** 阶段 5 · 02（词袋与 TF-IDF），阶段 2 · 14（朴素 Bayes）
**Time:** ~75 分钟

## 要解决的问题

“The food was not great.” 是正向还是负向？

情感判断听起来很简单。评论者说自己喜欢或不喜欢某样东西，给这句话标上标签就行了。它之所以成为经典的 NLP 任务，是因为每个看似简单的情形背后都藏着难题。否定会翻转含义，讽刺也会将含义颠倒。“Not bad at all” 虽然包含两个带有负面意味的词，表达的却是正向情感。表情符号携带的信号比周围的文字还多。领域词汇也很重要，例如音乐评论中的 `tight` 与时尚评论中的 `tight`。

情感分析（sentiment analysis）是传统 NLP 的实践试验场。如果你理解每个朴素基线为何会出现特定的失效模式，就能理解人们为何发明了更复杂的模型。本课从零构建朴素 Bayes（Naive Bayes）基线，再加入逻辑回归（logistic regression），并指出那些让生产环境中的情感分析成为需要以合规标准对待的问题的陷阱。

## 核心概念

传统情感分析分为两步。

1. **表示。** 将文本转换为特征向量：词袋（BoW）、TF-IDF（词频-逆文档频率），或连续 n 元片段（n-gram）。
2. **分类。** 用带标签的样本拟合线性模型，例如朴素 Bayes、逻辑回归或支持向量机（SVM）。

朴素 Bayes 是最简单粗糙、却能奏效的模型。它假设：给定标签后，各个特征彼此独立。根据计数估计 `P(word | positive)` 和 `P(word | negative)`，推理时再将概率相乘。这个“朴素”的独立性假设错得令人发笑，效果却好得令人惊讶。原因在于：当文本特征稀疏、数据量适中时，分类器更在意每个词倾向于哪一类，而不是倾向有多强。

逻辑回归解决了独立性假设的问题。它为每个特征学习一个权重，其中也可以有负权重。作为二元片段（bigram）特征的 `not good` 会得到负权重。对于从未标注过的二元片段，朴素 Bayes 做不到这一点。

```figure
sentiment-logits
```

## 动手实现

### 步骤 1：真实的小型数据集

```python
POSITIVE = [
    "absolutely loved this movie",
    "beautiful cinematography and a great story",
    "one of the best films of the year",
    "brilliant acting from the lead",
    "heartwarming and funny",
]

NEGATIVE = [
    "boring and far too long",
    "not worth your time",
    "the plot made no sense",
    "terrible acting, awful script",
    "i want my two hours back",
]
```

数据集刻意保持很小。实际工作会使用数万条样本，例如 IMDb、SST-2 和 Yelp polarity。数学原理完全相同。

### 步骤 2：从零实现多项式朴素 Bayes

```python
import math
from collections import Counter


def train_nb(docs_by_class, vocab, alpha=1.0):
    class_priors = {}
    class_word_probs = {}
    total_docs = sum(len(d) for d in docs_by_class.values())

    for cls, docs in docs_by_class.items():
        class_priors[cls] = len(docs) / total_docs
        counts = Counter()
        for doc in docs:
            for token in doc:
                counts[token] += 1
        total = sum(counts.values()) + alpha * len(vocab)
        class_word_probs[cls] = {
            w: (counts[w] + alpha) / total for w in vocab
        }
    return class_priors, class_word_probs


def predict_nb(doc, class_priors, class_word_probs):
    scores = {}
    for cls in class_priors:
        s = math.log(class_priors[cls])
        for token in doc:
            if token in class_word_probs[cls]:
                s += math.log(class_word_probs[cls][token])
        scores[cls] = s
    return max(scores, key=scores.get)
```

加性平滑（alpha=1.0）就是 Laplace 平滑（拉普拉斯平滑）。没有平滑，一个词若未在某一类中出现，其概率就会是零，对数值也就会发散。实践中常用 `alpha=0.01`，而教学默认使用 `alpha=1.0`。

### 步骤 3：从零实现逻辑回归

```python
import numpy as np


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -20, 20)))


def train_lr(X, y, epochs=500, lr=0.05, l2=0.01):
    n_features = X.shape[1]
    w = np.zeros(n_features)
    b = 0.0
    for _ in range(epochs):
        logits = X @ w + b
        preds = sigmoid(logits)
        err = preds - y
        grad_w = X.T @ err / len(y) + l2 * w
        grad_b = err.mean()
        w -= lr * grad_w
        b -= lr * grad_b
    return w, b


def predict_lr(X, w, b):
    return (sigmoid(X @ w + b) >= 0.5).astype(int)
```

L2 正则化（regularization）在这里很重要。文本特征是稀疏的；没有 L2，模型就会记住训练样本。从 `0.01` 开始调参。

### 步骤 4：处理否定这一失效模式

看看“not good”和“not bad”。词袋分类器看到的是 `{not, good}` 和 `{not, bad}`，会根据训练中哪一种出现得更多来学习。二元片段分类器看到的则是 `not_good` 和 `not_bad`，会把它们作为不同的特征来学习。这通常就够用了。

没有二元片段时，还有一种更粗略但有效的办法：**否定范围标记（negation scoping）**。给否定词之后的 token（词元）加上 `NOT_` 前缀，直到下一个标点为止。

```python
NEGATION_WORDS = {"not", "no", "never", "nor", "none", "nothing", "neither"}
NEGATION_TERMINATORS = {".", "!", "?", ",", ";"}


def apply_negation(tokens):
    out = []
    negate = False
    for token in tokens:
        if token in NEGATION_TERMINATORS:
            negate = False
            out.append(token)
            continue
        if token in NEGATION_WORDS:
            negate = True
            out.append(token)
            continue
        out.append(f"NOT_{token}" if negate else token)
    return out
```

```python
>>> apply_negation(["not", "good", "at", "all", ".", "but", "funny"])
['not', 'NOT_good', 'NOT_at', 'NOT_all', '.', 'but', 'funny']
```

现在，`good` 和 `NOT_good` 是不同的特征。分类器可以给它们赋予正负相反的权重。三行预处理，就能在情感分析基准上带来可测量的准确率提升。

### 步骤 5：真正重要的评估指标

类别不平衡时，只看准确率会产生误导。真实的情感语料通常有 70-80% 是正向，或有 70-80% 是负向；一个始终预测多数类的分类器就能达到 80% 准确率，却毫无价值。下面这些指标和信息，每一项都要报告：

- **各类别的精确率与召回率。** 每类各算一对，再分别取宏平均，得到兼顾类别平衡的单一数值。
- **Macro-F1（宏平均，不平衡数据的主要指标）。** 对各类别的 F1 分数取等权平均。类别不平衡时，用它代替准确率。
- **Weighted-F1（加权，另一种选择）。** 与宏平均类似，但按类别频率加权。如果这种不平衡本身具有业务意义，就将它与宏平均 F1 一并报告。
- **混淆矩阵。** 展示原始计数。在相信任何标量指标之前，都要先检查它；它能揭示模型混淆了哪两个类别。
- **各类别的错误样本。** 每类抽出 5 个预测错误的样本，读一读。没有什么能代替亲自查看实际错误。

对于严重不平衡的数据（比例 > 95-5），应报告 **ROC 曲线下面积（AUROC）** 和 **精确率-召回率曲线下面积（AUPRC）**，而不是准确率。AUPRC 对少数类更敏感，而少数类通常才是你关心的对象，例如垃圾信息、欺诈或少见的情感类别。

**要避免的常见错误。** 在不平衡数据上报告micro-F1（微平均），而不是宏平均 F1，会得到一个看起来很高的数字，因为它由多数类主导。宏平均 F1 会迫使你关注少数类的表现。

```python
def evaluate(y_true, y_pred):
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    tn = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)
    precision = tp / (tp + fp) if tp + fp else 0
    recall = tp / (tp + fn) if tp + fn else 0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0
    return {"tp": tp, "fp": fp, "tn": tn, "fn": fn, "precision": precision, "recall": recall, "f1": f1}
```

## 实际使用

scikit-learn 用六行代码就能正确完成这件事。

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True, stop_words=None)),
    ("clf", LogisticRegression(C=1.0, max_iter=1000)),
])
pipe.fit(X_train, y_train)
print(pipe.score(X_test, y_test))
```

注意三点。`stop_words=None` 会保留否定词；`ngram_range=(1, 2)` 会加入二元片段，使 `not_good` 成为一个特征；`sublinear_tf=True` 会减弱重复词的影响。在 SST-2 上，这三个标志决定了基线准确率是 75% 还是 85%。

### 何时采用 transformer

- 讽刺检测。传统模型在这里行不通，就是如此。
- 情感在文中发生转变的长评论。
- 方面级情感分析（aspect-based sentiment）。“Camera was great but battery was terrible.” 你需要把情感归属于具体方面。只能使用 Transformer 或结构化输出模型。
- 非英语的低资源语言。多语言 BERT 可以直接提供一个零样本基线。

如果你有上述任一需求，就跳到阶段 7（深入学习 Transformer）。否则，基于 TF-IDF、二元片段和否定处理的朴素 Bayes 或逻辑回归，就是你在 2026 年的生产基线。

### 再谈可复现性陷阱

重新训练情感模型很常见，重新评估却不常见。论文报告的准确率使用了特定的数据划分、预处理和分词器。如果你在比较新模型和基线时，没有使用完全相同的流水线，得到的差异就会产生误导。始终用自己的流水线重新得到基线结果，不要直接使用论文中的数字。

## 交付成果

保存为 `outputs/prompt-sentiment-baseline.md`：

```markdown
---
name: sentiment-baseline
description: Design a sentiment analysis baseline for a new dataset.
phase: 5
lesson: 05
---

Given a dataset description (domain, language, size, label granularity, latency budget), you output:

1. Feature extraction recipe. Specify tokenizer, n-gram range, stopword policy (usually keep), negation handling (scoped prefix or bigrams).
2. Classifier. Naive Bayes for baseline, logistic regression for production, transformer only if the domain needs sarcasm / aspects / cross-lingual.
3. Evaluation plan. Report precision, recall, F1, confusion matrix, and per-class error samples (not just scalars).
4. One failure mode to monitor post-deployment. Domain drift and sarcasm are the top two.

Refuse to recommend dropping stopwords for sentiment tasks. Refuse to report accuracy as the sole metric when classes are imbalanced (e.g., 90% positive). Flag subword-rich languages as needing FastText or transformer embeddings over word-level TF-IDF.
```

## 练习

1. **简单。** 将 `apply_negation` 作为预处理步骤加入 scikit-learn 流水线，在一个小型情感数据集上测量 F1 的变化。
2. **中等。** 实现按类别加权的逻辑回归：向 scikit-learn 传入 `class_weight="balanced"`，或者自己推导梯度。在人为构造的 90-10 类别不平衡数据上测量效果。
3. **困难。** 在情感模型的残差上训练第二个分类器，构建一个讽刺检测器。记录你的实验设置。当准确率低于随机猜测水平时，要提醒读者：2 类讽刺分类的随机猜测水平约为 50%，而大多数初次尝试都处于这一水平。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|-----------------|-----------------------|
| 情感极性（polarity） | 正向或负向 | 二元标签；有时扩展为中性，或更细的粒度（5 星）。 |
| 方面级情感分析 | 各方面的情感极性 | 将情感归属于文本中提及的具体实体或属性。 |
| 否定范围标记 | 反转邻近 token | 给“not”之后的 token 加上 `NOT_` 前缀，直到标点为止。 |
| Laplace 平滑 | 给计数加 1 | 避免朴素 Bayes 中出现零概率特征。 |
| L2 正则化 | 缩小权重 | 在损失中加入 `lambda * sum(w^2)`。对稀疏文本特征必不可少。 |

## 延伸阅读

- [Pang and Lee (2008). Opinion Mining and Sentiment Analysis](https://www.cs.cornell.edu/home/llee/opinion-mining-sentiment-analysis-survey.html) — 奠基性的综述。篇幅很长，但前四节涵盖了传统方法的全部内容。
- [Wang and Manning (2012). Baselines and Bigrams: Simple, Good Sentiment and Topic Classification](https://aclanthology.org/P12-2018/) — 这篇论文表明，在短文本上，二元片段加朴素 Bayes 很难被超越。
- [scikit-learn text feature extraction docs](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) — `CountVectorizer`、`TfidfVectorizer` 及其各项可调参数的参考文档。
