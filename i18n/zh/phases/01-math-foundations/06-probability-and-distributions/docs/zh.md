# 概率与分布

> 概率是 AI 表达不确定性所用的语言。

**Type:** Learn
**Language:** Python
**Prerequisites:** 第 1 阶段，第 01-04 课
**Time:** ~75 分钟

## 学习目标

- 从零实现 Bernoulli 分布（伯努利分布）、类别分布（categorical）、Poisson 分布（泊松分布）、均匀分布和正态分布的概率质量函数（PMF）与概率密度函数（PDF）
- 计算期望与方差，并用中心极限定理（CLT）解释高斯分布为何如此常见
- 运用数值稳定性技巧（减去最大的 logit），构建 softmax 和 log-softmax 函数
- 根据 logits 计算交叉熵损失，并理解它与负对数似然的联系

## 要解决的问题

分类器输出 `[0.03, 0.91, 0.06]`。语言模型从 50,000 个候选词中选出下一个词。扩散模型通过从学到的分布中抽样来生成图像。这些都是概率的实际应用。

模型的每一次预测都是一个概率分布。每个损失函数都在衡量预测分布与真实分布的差异。每一步训练都会调整参数，让一个分布变得更像另一个分布。不懂概率，你就无法读懂任何一篇机器学习（ML）论文、调试任何一个模型，也无法理解训练损失为什么会变成 NaN。

## 核心概念

### 事件、样本空间与概率

样本空间（sample space）S 是所有可能结果组成的集合。事件（event）是样本空间的一个子集。概率将事件映射为 0 到 1 之间的数。

```text
Coin flip:
  S = {H, T}
  P(H) = 0.5,  P(T) = 0.5

Single die roll:
  S = {1, 2, 3, 4, 5, 6}
  P(even) = P({2, 4, 6}) = 3/6 = 0.5
```

整个概率体系由三条公理定义：
1. 对任意事件 A，都有 P(A) >= 0
2. P(S) = 1（总会有某个结果发生）
3. 当 A 和 B 不能同时发生时，P(A or B) = P(A) + P(B)

其他一切（Bayes 定理、期望、分布）都可以从这三条规则推导出来。

### 条件概率与独立性

P(A|B) 是在 B 已经发生的条件下，A 发生的概率，即条件概率（conditional probability）。

```text
P(A|B) = P(A and B) / P(B)

Example: deck of cards
  P(King | Face card) = P(King and Face card) / P(Face card)
                      = (4/52) / (12/52)
                      = 4/12 = 1/3
```

如果得知一个事件是否发生，并不能提供关于另一个事件的任何信息，那么这两个事件就是独立的：

```text
Independent:   P(A|B) = P(A)
Equivalent to: P(A and B) = P(A) * P(B)
```

各次抛硬币的结果相互独立。不放回地抽牌则不是。

### 概率质量函数与概率密度函数

离散随机变量（random variable）具有概率质量函数（PMF）。每种结果都有一个确定的概率，可以直接从函数中读出。

```text
PMF: P(X = k)

Fair die:
  P(X = 1) = 1/6
  P(X = 2) = 1/6
  ...
  P(X = 6) = 1/6

  Sum of all probabilities = 1
```

连续随机变量具有概率密度函数（PDF）。单个点处的密度不是概率。对某个区间上的密度积分，才能得到概率。

```text
PDF: f(x)

P(a <= X <= b) = integral of f(x) from a to b

f(x) can be greater than 1 (density, not probability)
integral from -inf to +inf of f(x) dx = 1
```

这一区别在机器学习中很重要。分类输出是 PMF（离散选项），变分自编码器（VAE）的潜在空间则使用 PDF（连续变量）。

### 常见分布

**Bernoulli 分布：** 一次试验，两种结果。用于二分类建模。

```text
P(X = 1) = p
P(X = 0) = 1 - p
Mean = p,  Variance = p(1-p)
```

**类别分布：** 一次试验，k 种结果。用于多分类建模（softmax 输出）。

```text
P(X = i) = p_i,  where sum of p_i = 1
Example: P(cat) = 0.7,  P(dog) = 0.2,  P(bird) = 0.1
```

**均匀分布：** 所有结果出现的可能性都相同。用于随机初始化。

```text
Discrete: P(X = k) = 1/n for k in {1, ..., n}
Continuous: f(x) = 1/(b-a) for x in [a, b]
```

**正态分布（Gaussian，高斯分布）：** 即钟形曲线。其参数为均值（mu）和方差（sigma^2）。

```text
f(x) = (1 / sqrt(2*pi*sigma^2)) * exp(-(x - mu)^2 / (2*sigma^2))

Standard normal: mu = 0, sigma = 1
  68% of data within 1 sigma
  95% within 2 sigma
  99.7% within 3 sigma
```

**Poisson 分布：** 描述固定区间内稀有事件发生的次数。用于事件发生率建模。

```text
P(X = k) = (lambda^k * e^(-lambda)) / k!
Mean = lambda,  Variance = lambda
```

### 期望与方差

期望（expected value）是各种结果的加权平均。

```text
Discrete:   E[X] = sum of x_i * P(X = x_i)
Continuous: E[X] = integral of x * f(x) dx
```

方差（variance）衡量取值在均值周围的离散程度。

```text
Var(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2
Standard deviation = sqrt(Var(X))
```

在机器学习中，期望以损失函数的形式出现，即在数据分布上的平均损失。方差反映模型的稳定性。梯度方差大，意味着训练中的噪声大。

### 联合分布与边际分布

联合分布（joint distribution）P(X, Y) 同时描述两个随机变量。

联合 PMF 示例（X = 天气，Y = 雨伞）：

| | Y=0（不带伞） | Y=1（带伞） | 边际概率 P(X) |
|---|---|---|---|
| X=0（晴天） | 0.40 | 0.10 | P(X=0) = 0.50 |
| X=1（雨天） | 0.05 | 0.45 | P(X=1) = 0.50 |
| **边际概率 P(Y)** | P(Y=0) = 0.45 | P(Y=1) = 0.55 | 1.00 |

边际分布（marginal distribution）通过对另一个变量的所有取值求和，将该变量消去：

```text
P(X = x) = sum over all y of P(X = x, Y = y)
```

上表的行总和与列总和就是相应的边际概率。

### 为什么正态分布随处可见

中心极限定理：许多相互独立的随机变量之和（或平均值）会收敛到正态分布，无论它们原本服从什么分布。

```text
Roll 1 die:  uniform distribution (flat)
Average of 2 dice:  triangular (peaked)
Average of 30 dice: nearly perfect bell curve

This works for ANY starting distribution.
```

这也解释了为什么：
- 测量误差近似服从正态分布（来自许多微小且相互独立的来源）
- 神经网络的权重初始化使用正态分布
- 随机梯度下降（SGD）中的梯度噪声近似服从正态分布（许多样本梯度之和）
- 在均值与方差给定时，正态分布是熵最大的分布

### 对数概率

直接使用概率值会带来数值问题。将许多很小的概率相乘，结果很快就会下溢（underflow）为零。

```text
P(sentence) = P(word1) * P(word2) * ... * P(word_n)
            = 0.01 * 0.003 * 0.02 * ...
            -> 0.0 (underflow after ~30 terms)
```

对数概率（log probability）可以解决这个问题：乘法变成了加法。

```text
log P(sentence) = log P(word1) + log P(word2) + ... + log P(word_n)
                = -4.6 + -5.8 + -3.9 + ...
                -> finite number (no underflow)
```

规则：
- log(a * b) = log(a) + log(b)
- 对数概率始终 <= 0（因为 0 < P <= 1）
- 越负，发生的可能性越小
- 交叉熵损失就是正确类别的负对数概率

### 用 softmax 构造概率分布

神经网络输出原始分数，即 logits（未归一化分数）。softmax 将它们转换为有效的概率分布。

```text
softmax(z_i) = exp(z_i) / sum(exp(z_j) for all j)

Properties:
  - All outputs are in (0, 1)
  - All outputs sum to 1
  - Preserves relative ordering of inputs
  - exp() amplifies differences between logits
```

softmax 的技巧：在取指数之前减去最大的 logit，防止上溢（overflow）。

```text
z = [100, 101, 102]
exp(102) = overflow

z_shifted = z - max(z) = [-2, -1, 0]
exp(0) = 1  (safe)

Same result, no overflow.
```

log-softmax 将 softmax 与对数运算结合起来，以提高数值稳定性。PyTorch 在计算交叉熵损失时，内部就采用这种做法。

### 抽样

抽样（sampling）就是从某个分布中随机抽取值。在机器学习中：
- Dropout 随机抽样，决定将哪些神经元的输出置零
- 数据增强随机抽取变换
- 语言模型从预测分布中抽取下一个 token（词元）
- 扩散模型抽取噪声，再逐步去噪

从任意分布中抽样，需要使用逆变换抽样（inverse transform sampling）、拒绝抽样（rejection sampling）或重参数化技巧（reparameterization trick，用于 VAE）等方法。

```figure
gaussian-pdf
```

## 动手实现

### 第 1 步：概率基础

```python
import math
import random

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def conditional_probability(p_a_and_b, p_b):
    return p_a_and_b / p_b

p_king_given_face = conditional_probability(4/52, 12/52)
print(f"P(King | Face card) = {p_king_given_face:.4f}")
```

### 第 2 步：从零实现 PMF 与 PDF

```python
def bernoulli_pmf(k, p):
    return p if k == 1 else (1 - p)

def categorical_pmf(k, probs):
    return probs[k]

def poisson_pmf(k, lam):
    return (lam ** k) * math.exp(-lam) / factorial(k)

def uniform_pdf(x, a, b):
    if a <= x <= b:
        return 1.0 / (b - a)
    return 0.0

def normal_pdf(x, mu, sigma):
    coeff = 1.0 / (sigma * math.sqrt(2 * math.pi))
    exponent = -0.5 * ((x - mu) / sigma) ** 2
    return coeff * math.exp(exponent)
```

### 第 3 步：期望与方差

```python
def expected_value(values, probabilities):
    return sum(v * p for v, p in zip(values, probabilities))

def variance(values, probabilities):
    mu = expected_value(values, probabilities)
    return sum(p * (v - mu) ** 2 for v, p in zip(values, probabilities))

die_values = [1, 2, 3, 4, 5, 6]
die_probs = [1/6] * 6
mu = expected_value(die_values, die_probs)
var = variance(die_values, die_probs)
print(f"Die: E[X] = {mu:.4f}, Var(X) = {var:.4f}, SD = {var**0.5:.4f}")
```

### 第 4 步：从分布中抽样

```python
def sample_bernoulli(p, n=1):
    return [1 if random.random() < p else 0 for _ in range(n)]

def sample_categorical(probs, n=1):
    cumulative = []
    total = 0
    for p in probs:
        total += p
        cumulative.append(total)
    samples = []
    for _ in range(n):
        r = random.random()
        for i, c in enumerate(cumulative):
            if r <= c:
                samples.append(i)
                break
    return samples

def sample_normal_box_muller(mu, sigma, n=1):
    samples = []
    for _ in range(n):
        u1 = random.random()
        u2 = random.random()
        z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        samples.append(mu + sigma * z)
    return samples
```

### 第 5 步：softmax 与对数概率

```python
def softmax(logits):
    max_logit = max(logits)
    shifted = [z - max_logit for z in logits]
    exps = [math.exp(z) for z in shifted]
    total = sum(exps)
    return [e / total for e in exps]

def log_softmax(logits):
    max_logit = max(logits)
    shifted = [z - max_logit for z in logits]
    log_sum_exp = max_logit + math.log(sum(math.exp(z) for z in shifted))
    return [z - log_sum_exp for z in logits]

def cross_entropy_loss(logits, target_index):
    log_probs = log_softmax(logits)
    return -log_probs[target_index]
```

### 第 6 步：演示中心极限定理

```python
def demonstrate_clt(dist_fn, n_samples, n_averages):
    averages = []
    for _ in range(n_averages):
        samples = [dist_fn() for _ in range(n_samples)]
        averages.append(sum(samples) / len(samples))
    return averages
```

### 第 7 步：可视化

```python
import matplotlib.pyplot as plt

xs = [mu + sigma * (i - 500) / 100 for i in range(1001)]
ys = [normal_pdf(x, mu, sigma) for x, mu, sigma in ...]
plt.plot(xs, ys)
```

包含所有可视化的完整实现位于 `code/probability.py`。

## 实际使用

使用 NumPy 和 SciPy，上面的操作都可以用一行代码完成：

```python
import numpy as np
from scipy import stats

normal = stats.norm(loc=0, scale=1)
samples = normal.rvs(size=10000)
print(f"Mean: {np.mean(samples):.4f}, Std: {np.std(samples):.4f}")
print(f"P(X < 1.96) = {normal.cdf(1.96):.4f}")

logits = np.array([2.0, 1.0, 0.1])
from scipy.special import softmax, log_softmax
probs = softmax(logits)
log_probs = log_softmax(logits)
print(f"Softmax: {probs}")
print(f"Log-softmax: {log_probs}")
```

这些功能你都已经从零实现过了。现在，你知道调用库函数时背后发生了什么。

## 练习

1. 为指数分布实现逆变换抽样。抽取 10,000 个值，将直方图与真实的 PDF 比较，验证实现。

2. 为两个不均匀骰子（loaded dice）构建联合分布表。计算边际分布，并检查这两个骰子的结果是否相互独立。

3. 一个 5 类分类器输出 logits `[2.0, 0.5, -1.0, 3.0, 0.1]`，正确类别的索引为 3。计算它的交叉熵损失，再用 PyTorch 的 `nn.CrossEntropyLoss` 验证答案。

4. 编写一个函数，接收一组对数概率，返回最可能的序列、总对数概率以及等价的原始概率。用一个包含 50 个词、每个词的概率均为 0.01 的句子测试它。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|----------------------|
| 样本空间 | “所有可能性” | 一次试验中所有可能结果组成的集合 S |
| PMF | “概率函数” | 给出每个离散结果的确切概率的函数；所有概率之和为 1 |
| PDF | “概率曲线” | 连续变量的密度函数；在某个区间上对它积分，才能得到概率 |
| 条件概率 | “给定某个条件时的概率” | P(A\|B) = P(A and B) / P(B)。Bayes 思维与 Bayes 定理的基础 |
| 独立性 | “它们互不影响” | P(A and B) = P(A) * P(B)。得知一个事件是否发生，并不能提供关于另一个事件的信息 |
| 期望 | “平均值” | 所有结果按概率加权求和。损失函数就是一个期望 |
| 方差 | “分散程度” | 与均值之差的平方的期望。高方差 = 估计噪声大、不稳定 |
| 正态分布 | “钟形曲线” | f(x) = (1/sqrt(2\*pi\*sigma^2)) \* exp(-(x-mu)^2/(2\*sigma^2))。由于中心极限定理，它随处可见 |
| 中心极限定理 | “平均值会变成正态分布” | 无论样本来自什么分布，许多独立样本的均值都会收敛到正态分布 |
| 联合分布 | “两个变量放在一起” | P(X, Y) 描述 X 和 Y 各种结果组合的概率 |
| 边际分布 | “对另一个变量求和并将其消去” | P(X) = sum_y P(X, Y)。从联合分布中还原出单个变量的分布 |
| 对数概率 | “概率的对数” | log P(x)。将乘积变成和，防止长序列中出现数值下溢 |
| softmax | “把分数变成概率” | softmax(z_i) = exp(z_i) / sum(exp(z_j))。将实值 logits 映射为有效的概率分布 |
| 交叉熵 | “损失函数” | -sum(p_true * log(p_predicted))。衡量两个分布的差异程度，越小越好 |
| logits | “模型的原始输出” | softmax 之前的未归一化分数，名称来自 logistic 函数 |
| 抽样 | “随机抽取值” | 按照概率分布生成值，是模型生成输出的方式 |

## 延伸阅读

- [3Blue1Brown：中心极限定理究竟是什么？](https://www.youtube.com/watch?v=zeJD6dqJ5lo) - 直观展示平均值为何会趋于正态分布
- [Stanford CS229 概率复习资料](https://cs229.stanford.edu/section/cs229-prob.pdf) - 简明参考资料，涵盖本课内容及更多主题
- [log-sum-exp 技巧](https://gregorygundersen.com/blog/2020/02/09/log-sum-exp/) - 为什么数值稳定性重要，以及如何实现它
