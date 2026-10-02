# 朴素 Bayes

> “朴素”的假设是错的，但它仍然有效。这正是它的妙处。

**Type:** Build
**Language:** Python
**Prerequisites:** 第 2 阶段，第 01-07 课（分类、Bayes 定理）
**Time:** ~75 分钟

## 学习目标

- 从零实现用于文本分类的多项式朴素 Bayes（Multinomial Naive Bayes），并加入 Laplace 平滑（拉普拉斯平滑）
- 解释为什么朴素独立性假设在数学上是错的，却能在实践中给出正确的类别排序
- 比较 Multinomial、Bernoulli 和 Gaussian 三种朴素 Bayes 变体，并根据给定的特征类型选择合适的变体
- 在高维稀疏数据上比较朴素 Bayes 与逻辑回归，解释其中的偏差与方差权衡

## 要解决的问题

你需要对文本分类：把邮件分为垃圾邮件和正常邮件，把客户评论分为正面和负面，把支持工单分到不同类别。你有数千个特征（每个词对应一个），训练数据却有限。

大多数分类器在这里都会遇到困难。逻辑回归需要足够多的样本，才能可靠地估计数千个权重。决策树每次按一个词划分，很容易严重过拟合。在 10,000 维空间中，KNN 没有意义，因为每个点到其他任意点的距离都一样远。

朴素 Bayes（Naive Bayes，简称 NB）能够应对这种情况。它作出一个在数学上错误的假设（给定类别后，每个特征都独立于其他所有特征），但在文本分类上仍能胜过更“聪明”的模型，尤其是在训练集较小时。它只需遍历一遍数据就能完成训练，可以扩展到数百万个特征。它还会给出概率估计（不过，由于独立性假设，这些概率往往校准得不好）。

理解为什么错误的假设能带来好的预测，会让你领会机器学习中的一个基本道理：最好的模型不是最正确的模型，而是对你的数据具有最佳偏差与方差权衡的模型。

## 核心概念

### Bayes 定理（快速回顾）

Bayes 定理（贝叶斯定理）可以转换条件概率的方向：

```text
P(class | features) = P(features | class) * P(class) / P(features)
```

我们想要的是 `P(class | features)`，即给定文档中的词后，该文档属于某个类别的概率。可以通过以下各项计算：
- `P(features | class)`：在该类别的文档中观察到这些词的似然（likelihood）
- `P(class)`：该类别的先验概率（总体而言，垃圾邮件有多常见？）
- `P(features)`：证据，对所有类别都相同，因此比较类别时可以忽略

`P(class | features)` 最高的类别胜出。

### 朴素独立性假设

精确计算 `P(features | class)` 需要估计所有特征共同出现的联合概率。若词表有 10,000 个词，就需要在 2^10,000 种可能组合上估计一个分布。这是不可能的。

朴素假设是：给定类别后，每个特征都条件独立。

```text
P(w1, w2, ..., wn | class) = P(w1 | class) * P(w2 | class) * ... * P(wn | class)
```

你不再估计一个不可能求得的联合分布，而是估计 n 个简单的单特征分布，每个分布只需要计数。

这个假设显然是错的。“machine”和“learning”这两个词在任何文档中都不是独立的。但分类器不需要正确的概率估计，它需要的是正确的排序，也就是哪个类别的概率最高。独立性假设会引入系统性误差，但这些误差对所有类别的影响相似，所以排序仍然正确。

### 为什么它仍然有效

有三个原因：

1. **排序比校准更重要。** 分类只需要排在首位的类别正确。即使真实概率是 0.7，而 P(spam) = 0.99999，分类器仍然能正确选出垃圾邮件。我们不需要正确的概率，需要的是正确的胜出类别。

2. **高偏差、低方差。** 独立性假设是一种很强的先验。它对模型施加了很强的约束，从而防止过拟合。训练数据有限时，一个略有偏差但稳定的模型，胜过一个理论上正确却极不稳定的模型。这就是偏差与方差权衡的体现。

3. **特征冗余相互抵消。** 相关特征提供了重复的证据。分类器会把这些证据计算两次，但对于正确类别，它也会计算两次。如果“machine”和“learning”总是一起出现，那么两者都会为“tech”类别提供证据。NB 把它们算了两次，但算给的是正确类别。

还有第四个实际原因：朴素 Bayes 极快。训练只需遍历一遍数据，统计频数。预测就是矩阵乘法。你可以在几秒内用一百万篇文档完成训练。与较慢的模型相比，这种速度让你能够更快地迭代，尝试更多特征集，开展更多实验。

### 逐步推算

来看一个具体例子。假设有两个类别：垃圾邮件 spam 和正常邮件 not-spam。词表包含三个词：“free”、“money”和“meeting”。

训练数据：
- 垃圾邮件中“free”出现 80 次、“money”出现 60 次、“meeting”出现 10 次（总共 150 个词）
- 正常邮件中“free”出现 5 次、“money”出现 10 次、“meeting”出现 100 次（总共 115 个词）
- 40% 的邮件是垃圾邮件，60% 是正常邮件

使用 Laplace 平滑（alpha=1）：

```text
P(free | spam)    = (80 + 1) / (150 + 3) = 81/153 = 0.529
P(money | spam)   = (60 + 1) / (150 + 3) = 61/153 = 0.399
P(meeting | spam) = (10 + 1) / (150 + 3) = 11/153 = 0.072

P(free | not-spam)    = (5 + 1) / (115 + 3) = 6/118 = 0.051
P(money | not-spam)   = (10 + 1) / (115 + 3) = 11/118 = 0.093
P(meeting | not-spam) = (100 + 1) / (115 + 3) = 101/118 = 0.856
```

新邮件包含：“free”（2 次）、“money”（1 次）、“meeting”（0 次）。

```text
log P(spam | email) = log(0.4) + 2*log(0.529) + 1*log(0.399) + 0*log(0.072)
                    = -0.916 + 2*(-0.637) + (-0.919) + 0
                    = -3.109

log P(not-spam | email) = log(0.6) + 2*log(0.051) + 1*log(0.093) + 0*log(0.856)
                        = -0.511 + 2*(-2.976) + (-2.375) + 0
                        = -8.838
```

垃圾邮件类别以很大优势胜出。“free”出现两次，为垃圾邮件提供了强有力的证据。注意，“meeting”没有出现，对两个对数和的贡献都为零（0 * log(P)）。在 Multinomial NB 中，未出现的词没有影响。显式建模词缺席情况的是 Bernoulli NB。

### 三种变体

朴素 Bayes 有三种变体，各自对 `P(feature | class)` 采用不同的建模方式。

#### 多项式朴素 Bayes

把每个特征建模为计数。最适合特征为词频或 TF-IDF（词频-逆文档频率，Term Frequency - Inverse Document Frequency）值的文本数据。

```text
P(word_i | class) = (count of word_i in class + alpha) / (total words in class + alpha * vocab_size)
```

`alpha` 是 Laplace 平滑参数（下文解释）。这种变体是文本分类的主力。

#### Gaussian 朴素 Bayes

Gaussian（高斯）朴素 Bayes 把每个特征建模为正态分布，最适合连续特征。

```text
P(x_i | class) = (1 / sqrt(2 * pi * var)) * exp(-(x_i - mean)^2 / (2 * var))
```

每个类别都为每个特征分别估计自己的均值和方差。当每个类别内部的特征确实呈钟形分布时，这种方法效果很好。

#### Bernoulli 朴素 Bayes

Bernoulli（伯努利）朴素 Bayes 把每个特征建模为二元变量（出现或不出现），最适合短文本或二元特征向量。

```text
P(word_i | class) = (docs in class containing word_i + alpha) / (total docs in class + 2 * alpha)
```

与 Multinomial 不同，Bernoulli 会显式惩罚词的缺席。如果“free”通常出现在垃圾邮件中，但这封邮件没有这个词，Bernoulli 就会把它视为反对垃圾邮件类别的证据。

### 各种变体适用于什么情况

| 变体 | 特征类型 | 最适用场景 | 示例 |
|---------|-------------|----------|---------|
| Multinomial | 计数或频率 | 文本分类、词袋（bag-of-words） | 垃圾邮件、主题分类 |
| Gaussian | 连续值 | 特征近似正态分布的表格数据 | Iris 分类、传感器数据 |
| Bernoulli | 二元值（0/1） | 短文本、二元特征向量 | 垃圾短信、出现/缺席特征 |

### Laplace 平滑

如果一个词出现在测试数据中，却从未在某个类别的训练数据中出现，会怎样？

没有平滑时：`P(word | class) = 0/N = 0`。整个乘积中只要乘上一个零，就会使 `P(class | features) = 0`，无论其他证据是什么。只需一个未见过的词，就会破坏整个预测，无论还有多少其他证据支持它。

Laplace 平滑为每个特征计数加上一个小计数 `alpha`（通常为 1）：

```text
P(word_i | class) = (count(word_i, class) + alpha) / (total_words_in_class + alpha * vocab_size)
```

当 alpha=1 时，每个词至少都有一个很小的概率。测试邮件中出现“discombobulate”这个词，不再会让垃圾邮件的概率归零。这种平滑有一种贝叶斯解释：它等价于在词分布上设置一个均匀的 Dirichlet 先验。

alpha 越大，平滑越强（分布越均匀）；alpha 越小，模型越相信数据。Alpha 是需要调优的超参数。

alpha 的影响：

| Alpha | 效果 | 使用场景 |
|-------|--------|-------------|
| 0.001 | 几乎不平滑，相信数据 | 训练集非常大，预计不会出现未见过的特征 |
| 0.1 | 轻度平滑 | 训练集较大 |
| 1.0 | 标准 Laplace 平滑 | 默认起点 |
| 10.0 | 强平滑，使分布更平坦 | 训练集非常小，预计会出现许多未见过的特征 |

### 对数空间计算

将数百个概率（每个都小于 1）相乘，会导致浮点下溢。即使真实值是一个极小的正数，浮点运算中的乘积也会变成零。

解决办法是在对数空间中计算：不把概率相乘，而是把它们的对数相加：

```text
log P(class | x1, x2, ..., xn) = log P(class) + sum_i log P(xi | class)
```

这样，预测就变成了点积：

```text
log_scores = X @ log_feature_probs.T + log_class_priors
prediction = argmax(log_scores)
```

矩阵乘法。这就是朴素 Bayes 预测如此快的原因：它与单层线性模型进行的是同一种运算。

### 朴素 Bayes 与逻辑回归

两者都是用于文本的线性分类器，区别在于建模的对象。

| 方面 | 朴素 Bayes | 逻辑回归 |
|--------|------------|-------------------|
| 类型 | 生成式（建模 P(X\|Y)） | 判别式（建模 P(Y\|X)） |
| 训练 | 统计频数 | 优化损失函数 |
| 数据少时 | 更好（强先验有帮助） | 更差（不足以估计权重） |
| 数据多时 | 更差（错误假设带来不利影响） | 更好（边界灵活） |
| 特征 | 假设独立 | 能处理相关性 |
| 速度 | 单遍处理，非常快 | 迭代优化 |
| 校准 | 概率较差 | 概率更好 |

经验法则：先用朴素 Bayes。如果数据足够多，而且 NB 的表现进入平台期，再切换到逻辑回归。

### 分类流水线

```mermaid
flowchart LR
    A[Raw Text] --> B[Tokenize]
    B --> C[Build Vocabulary]
    C --> D[Count Word Frequencies]
    D --> E[Apply Smoothing]
    E --> F[Compute Log Probabilities]
    F --> G[Predict: argmax P class given words]

    style A fill:#f9f,stroke:#333
    style G fill:#9f9,stroke:#333
```

实际中，我们在对数空间里计算，以避免浮点下溢。不把许多小概率相乘，而是把它们的对数相加：

```text
log P(class | features) = log P(class) + sum_i log P(feature_i | class)
```

```figure
naive-bayes
```

## 动手实现

`code/naive_bayes.py` 中的代码从零实现了 MultinomialNB 和 GaussianNB。

### MultinomialNB

从零实现的步骤如下：

1. **fit(X, y)**: 对每个类别，统计每个特征的频数，加入 Laplace 平滑，计算对数概率，并存储类别先验（类别频率的对数）。

2. **predict_log_proba(X)**: 对每个样本，计算所有类别的 log P(class) 加上各个 log P(feature_i | class) 的和。这是一次矩阵乘法：X @ log_probs.T + log_priors。

3. **predict(X)**: 返回对数概率最高的类别。

```python
class MultinomialNB:
    def __init__(self, alpha=1.0):
        self.alpha = alpha

    def fit(self, X, y):
        classes = np.unique(y)
        n_classes = len(classes)
        n_features = X.shape[1]

        self.classes_ = classes
        self.class_log_prior_ = np.zeros(n_classes)
        self.feature_log_prob_ = np.zeros((n_classes, n_features))

        for i, c in enumerate(classes):
            X_c = X[y == c]
            self.class_log_prior_[i] = np.log(X_c.shape[0] / X.shape[0])
            counts = X_c.sum(axis=0) + self.alpha
            self.feature_log_prob_[i] = np.log(counts / counts.sum())

        return self
```

关键在于：拟合完成后，预测只需要矩阵乘法再加上一个偏置。这就是朴素 Bayes 速度如此快的原因。

### GaussianNB

对于连续特征，我们按类别、按特征估计均值和方差：

```python
class GaussianNB:
    def __init__(self):
        pass

    def fit(self, X, y):
        classes = np.unique(y)
        self.classes_ = classes
        self.means_ = np.zeros((len(classes), X.shape[1]))
        self.vars_ = np.zeros((len(classes), X.shape[1]))
        self.priors_ = np.zeros(len(classes))

        for i, c in enumerate(classes):
            X_c = X[y == c]
            self.means_[i] = X_c.mean(axis=0)
            self.vars_[i] = X_c.var(axis=0) + 1e-9
            self.priors_[i] = X_c.shape[0] / X.shape[0]

        return self
```

预测时，对每个特征使用 Gaussian 概率密度函数（PDF），再跨特征相乘（在对数空间中则相加）。

### 演示：文本分类

代码生成合成的词袋数据，模拟两个类别（科技文章与体育文章）。每个类别都有不同的词频分布。MultinomialNB 根据词计数进行分类。

合成数据的生成方式如下：创建 200 个“词”（特征列）。编号 0-39 的词在科技文章中频率高，在体育文章中频率低；编号 80-119 的词在体育文章中频率高，在科技文章中频率低；编号 40-79 的词在两类文章中都是中等频率。这模拟了现实中的一种情况：有些词是很强的类别指示信号，其他词则是噪声。

### 演示：连续特征

代码生成类似 Iris 的数据（3 个类别、4 个特征、Gaussian 簇）。GaussianNB 根据每个类别的均值和方差进行分类。每个类别都有不同的中心（均值向量）和不同的离散程度（方差），模拟现实数据中不同类别的测量值存在系统性差异的情况。

代码还演示了：
- **平滑比较：** 使用不同的 alpha 值训练 MultinomialNB，展示平滑强度对准确率的影响
- **训练集大小实验：** 随着训练数据从 20 个样本增加到 1600 个样本，NB 的准确率如何提高。即使样本很少，NB 也能达到不错的准确率，这是它的主要优势
- **混淆矩阵：** 通过每个类别的精确率、召回率和 F1 分数，展示 NB 在哪里出错

### 预测速度

朴素 Bayes 预测是矩阵乘法。对于 n 个样本、d 个特征和 k 个类别：
- MultinomialNB：一次矩阵乘法 (n x d) @ (d x k) = O(n * d * k)
- GaussianNB：n * k 次 Gaussian PDF 求值，每次覆盖 d 个特征，复杂度为 O(n * d * k)

两者在每个维度上的复杂度都是线性的。相比之下，KNN 需要计算到所有训练点的距离，采用 RBF 核的 SVM 需要对所有支持向量计算核函数。在预测时，NB 要快几个数量级。

## 实际使用

使用 sklearn，两种变体都只需一行代码：

```python
from sklearn.naive_bayes import GaussianNB, MultinomialNB

gnb = GaussianNB()
gnb.fit(X_train, y_train)
print(f"GaussianNB accuracy: {gnb.score(X_test, y_test):.3f}")

mnb = MultinomialNB(alpha=1.0)
mnb.fit(X_train_counts, y_train)
print(f"MultinomialNB accuracy: {mnb.score(X_test_counts, y_test):.3f}")
```

使用 sklearn 进行文本分类：

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

text_clf = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB(alpha=1.0)),
])

text_clf.fit(train_texts, train_labels)
accuracy = text_clf.score(test_texts, test_labels)
```

`naive_bayes.py` 中的代码在相同数据上比较从零实现的版本与 sklearn，以验证正确性。

### TF-IDF 与朴素 Bayes

原始词计数给每个词的每次出现赋予相同权重。但像“the”和“is”这样的常见词，在每个类别中都频繁出现，不携带任何信息。TF-IDF（词频-逆文档频率，Term Frequency - Inverse Document Frequency）降低常见词的权重，提高稀有且有区分力的词的权重。

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

text_clf = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB(alpha=0.1)),
])
```

TF-IDF 值非负，因此可以用于 MultinomialNB。TF-IDF + MultinomialNB 是文本分类中最强的基线之一。在训练样本少于 10,000 个的数据集上，它经常胜过更复杂的模型。

### 用 BernoulliNB 处理短文本

对于短文本（推文、短信、聊天消息），BernoulliNB 可能胜过 MultinomialNB。短文本的词计数较少，因此 MultinomialNB 所依赖的频率信息噪声较大。BernoulliNB 只关心出现与否，对短文本而言，这种信息更可靠。

```python
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer

text_clf = Pipeline([
    ("vectorizer", CountVectorizer(binary=True)),
    ("classifier", BernoulliNB(alpha=1.0)),
])
```

CountVectorizer 的 `binary=True` 标志会把所有计数转换为 0/1。没有它，BernoulliNB 仍然能工作，但接收到的是它原本并非为之设计的计数。

### 校准 NB 的概率

NB 的概率校准较差。当 NB 给出 P(spam) = 0.95 时，真实概率可能是 0.7。如果需要可靠的概率估计（例如用于设置阈值，或与其他模型结合），可以使用 sklearn 的 CalibratedClassifierCV：

```python
from sklearn.calibration import CalibratedClassifierCV

calibrated_nb = CalibratedClassifierCV(MultinomialNB(), cv=5, method="sigmoid")
calibrated_nb.fit(X_train, y_train)
proba = calibrated_nb.predict_proba(X_test)
```

它利用交叉验证，在 NB 的原始分数上拟合一个逻辑回归模型。得到的概率会更接近真实的类别频率。

### 常见陷阱

1. **负特征值。** MultinomialNB 要求特征非负。如果特征有负值（例如某些设置下的 TF-IDF 或标准化后的特征），改用 GaussianNB，或者平移特征，使其为正。

2. **零方差特征。** GaussianNB 会除以方差。如果某个特征在某个类别中的方差为零（所有值都相同），概率计算就会出错。代码为所有方差加上一个很小的平滑项（1e-9），防止这种情况发生。

3. **类别不平衡。** 如果 99% 的邮件是正常邮件，先验 P(not-spam) = 0.99 就会强到压过似然证据。可以手动设置类别先验，或使用 sklearn 的 class_prior 参数。

4. **特征缩放。** MultinomialNB 不需要缩放（它处理的是计数）。GaussianNB 也不需要缩放（它估计各个特征的统计量）。这是它们相对逻辑回归和 SVM 的一个优势，后两者对特征尺度敏感。

## 交付成果

本课产出：
- `outputs/skill-naive-bayes-chooser.md`：帮助选择合适 NB 变体的决策技能
- `code/naive_bayes.py`：从零实现的 MultinomialNB 和 GaussianNB，附与 sklearn 的比较

### 朴素 Bayes 何时失效

当独立性假设导致排序错误（而不只是概率错误）时，NB 就会失效。这会发生在以下情况：

1. **强特征交互。** 如果类别取决于两个特征的组合，而不取决于任何一个单独特征（类似 XOR，即异或的模式），NB 就会完全错过。每个特征单独都不提供证据，NB 也无法以非线性方式将它们组合起来。

2. **高度相关的特征提供相反证据。** 如果特征 A 指向“spam”，特征 B 指向“not-spam”，但 A 和 B 完全相关（现实中总是一致），NB 就会在本不存在冲突的地方看到冲突证据。

3. **非常大的训练集。** 数据足够多时，逻辑回归等判别式模型会学到真实的决策边界，并胜过 NB。曾在小数据集上有所帮助的独立性假设，此时反而限制了模型。

实际中，这些失效模式在文本分类中很少见。文本特征数量多，单个特征的作用弱，独立性假设带来的误差往往会相互抵消。对于特征较少且相关性很强的表格数据，应优先考虑逻辑回归或基于树的模型。

## 练习

1. **平滑实验。** 在文本数据上，用 0.01、0.1、1.0、10.0 和 100.0 这些 alpha 值训练 MultinomialNB。绘制准确率随 alpha 变化的图。性能在哪里达到峰值？为什么 alpha 非常大时会损害性能？

2. **特征独立性检验。** 选取一个真实文本数据集，挑出两个明显相关的词（“machine”和“learning”）。计算 P(word1 | class) * P(word2 | class)，并与 P(word1 AND word2 | class) 比较。独立性假设错得有多大？它会影响分类准确率吗？

3. **实现 Bernoulli。** 为代码扩展一个 BernoulliNB 类。把词袋转换为二元值（出现/缺席），在文本数据上与 MultinomialNB 比较准确率。Bernoulli 何时胜出？

4. **NB 与逻辑回归。** 在文本数据上训练两者。从 100 个训练样本开始，增加到 10,000 个。绘制两个模型的准确率随训练集大小变化的图。逻辑回归何时超过朴素 Bayes？

5. **垃圾邮件过滤器。** 构建一个完整的垃圾邮件分类器：对原始邮件文本分词，构建词表，创建词袋特征，训练 MultinomialNB，并使用精确率和召回率评估（而不只看准确率，为什么？）。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|----------------------|
| 朴素 Bayes（Naive Bayes） | “简单的概率分类器” | 应用 Bayes 定理，并假设给定类别后特征条件独立的分类器 |
| 条件独立（Conditional independence） | “特征互不影响” | P(A, B \| C) = P(A \| C) * P(B \| C)，知道 C 后，再知道 B 不会提供任何关于 A 的新信息 |
| Laplace 平滑 | “加一平滑” | 为每个特征添加一个小计数，防止零概率主导预测 |
| 先验（Prior） | “看到数据前的看法” | P(class)，观察任何特征之前各类别的概率 |
| 似然（Likelihood） | “数据有多吻合” | P(features \| class)，已知类别时观察到这些特征的概率 |
| 后验（Posterior） | “看到数据后的看法” | P(class \| features)，观察特征后更新得到的类别概率 |
| 生成式模型（Generative model） | “建模数据的生成方式” | 学习 P(X \| Y) 和 P(Y)，再通过 Bayes 定理得到 P(Y \| X) 的模型 |
| 判别式模型（Discriminative model） | “建模决策边界” | 不对 X 的生成方式建模，而是直接学习 P(Y \| X) 的模型 |
| 对数概率（Log probability） | “避免下溢” | 使用 log P 而非 P 进行计算，防止许多小数的乘积在浮点运算中变成零 |

## 延伸阅读

- [scikit-learn Naive Bayes 文档](https://scikit-learn.org/stable/modules/naive_bayes.html)：三种变体及其数学细节
- [McCallum and Nigam, A Comparison of Event Models for Naive Bayes Text Classification (1998)](https://www.cs.cmu.edu/~knigam/papers/multinomial-aaaiws98.pdf)：文本任务中 Multinomial 与 Bernoulli 的经典比较
- [Rennie et al., Tackling the Poor Assumptions of Naive Bayes Text Classifiers (2003)](https://people.csail.mit.edu/jrennie/papers/icml03-nb.pdf)：针对文本的 NB 改进
- [Ng and Jordan, On Discriminative vs. Generative Classifiers (2001)](https://ai.stanford.edu/~ang/papers/nips01-discriminativegenerative.pdf)：证明数据较少时 NB 比 LR 收敛更快
