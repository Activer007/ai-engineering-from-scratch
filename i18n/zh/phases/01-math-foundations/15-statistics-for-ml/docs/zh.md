# 机器学习统计学

> 统计学能帮你判断：模型是真的有效，还是只是运气好。

**Type:** Build
**Language:** Python
**Prerequisites:** 阶段 1，第 06 课（概率与分布）、第 07 课（Bayes 定理）
**Time:** ~120 分钟

## 学习目标

- 从零计算描述统计量、Pearson/Spearman 相关系数和协方差矩阵
- 进行假设检验（t 检验、卡方检验），并正确解释 p 值和置信区间
- 在不作分布假设的情况下，用 bootstrap 重采样为任意指标构建置信区间
- 用效应量区分统计显著性与实际显著性

## 要解决的问题

你训练了两个模型。模型 A 在测试集上的得分为 0.87，模型 B 的得分为 0.89。你部署了模型 B。三周后，生产环境中的指标反而比以前更差。发生了什么？

模型 B 实际上并没有优于模型 A。0.02 的差异只是噪声。可能是测试集太小，也可能是方差太大，或者两者兼有。你把随机波动包装成改进，发布了出去。

这样的事不断发生：Kaggle 排行榜大洗牌，论文结果无法复现，A/B 测试仅凭几百个样本就宣布胜出者。根本原因总是相同的：有人跳过了统计分析。

统计学为你提供了区分信号与噪声的工具。它能告诉你，差异什么时候是真实的、你应当有多大把握，以及需要多少数据才能信任一个结果。每条机器学习（ML）流水线、每次模型比较、每项实验都需要统计学。没有它，你只能靠猜。

## 核心概念

### 描述统计：概括数据的特征

建模之前，你需要先了解数据是什么样的。描述统计（descriptive statistics）将数据集概括为几个能反映其分布形态的数字。

**集中趋势指标（measures of central tendency）** 回答的是“中心在哪里？”

```text
Mean:   sum of all values / count
        mu = (1/n) * sum(x_i)

Median: middle value when sorted
        Robust to outliers. If you have [1, 2, 3, 4, 1000], the mean is 202
        but the median is 3.

Mode:   most frequent value
        Useful for categorical data. For continuous data, rarely informative.
```

均值是平衡点，中位数则是将数据一分为二的位置。两者偏离时，分布就是偏斜的。收入分布中，mean >> median，即均值远大于中位数，这是亿万富翁造成的右偏。训练期间的损失分布则经常呈现 mean << median，即均值远小于中位数，这是容易样本造成的左偏。

**离散程度指标（measures of spread）** 回答的是“数据有多分散？”

```text
Variance:   average squared deviation from the mean
            sigma^2 = (1/n) * sum((x_i - mu)^2)

Standard deviation:  square root of variance
                     sigma = sqrt(sigma^2)
                     Same units as the data, so more interpretable.

Range:      max - min
            Sensitive to outliers. Almost never useful alone.

IQR:        Q3 - Q1 (interquartile range)
            The range of the middle 50% of the data.
            Robust to outliers. Used for box plots and outlier detection.
```

**百分位数（percentile）** 将排序后的数据分成 100 个等份。第 25 百分位数（Q1）表示有 25% 的值低于该位置。第 50 百分位数就是中位数。第 75 百分位数是 Q3。

```text
For latency monitoring:
  P50 = median latency        (typical user experience)
  P95 = 95th percentile       (bad but not worst case)
  P99 = 99th percentile       (tail latency, often 10x the median)
```

在 ML 中，百分位数可用于关注推理延迟、预测置信度的分布，以及理解误差分布。一个模型即使平均误差很低，P99 误差却很糟糕，也可能无法用于安全攸关的应用。

**样本统计量与总体统计量。** 从样本计算方差时，应除以 (n-1)，而不是 n。这就是 Bessel 校正（Bessel's correction）。它补偿了样本均值并非真实总体均值这一事实带来的影响。分母取 n 时，会系统性地低估真实方差；取 (n-1) 时，估计就是无偏的。

```text
Population variance: sigma^2 = (1/N) * sum((x_i - mu)^2)
Sample variance:     s^2     = (1/(n-1)) * sum((x_i - x_bar)^2)
```

实际使用时，如果 n 很大，例如有数千个样本，这一差别可以忽略；如果 n 较小，例如只有几十个样本，这一差别就很重要。

### 相关性：变量如何一起变化

相关性衡量两个变量之间线性关系的强度与方向。

**Pearson 相关系数（Pearson correlation coefficient）** 衡量线性关联：

```text
r = sum((x_i - x_bar)(y_i - y_bar)) / (n * s_x * s_y)

r = +1:  perfect positive linear relationship
r = -1:  perfect negative linear relationship
r =  0:  no linear relationship (but there might be a nonlinear one!)

Range: [-1, 1]
```

Pearson 假设变量之间是线性关系，而且两个变量都近似服从正态分布。它对离群值很敏感。一个极端点，就可能把 r 从 0.1 拉到 0.9。

**Spearman 秩相关（Spearman rank correlation）** 衡量单调关联：

```text
1. Replace each value with its rank (1, 2, 3, ...)
2. Compute Pearson correlation on the ranks

Spearman catches any monotonic relationship, not just linear.
If y = x^3, Pearson gives r < 1 but Spearman gives rho = 1.
```

**各自的适用场景：**

```text
Pearson:    Both variables are continuous and roughly normal.
            You care about the linear relationship specifically.
            No extreme outliers.

Spearman:   Ordinal data (rankings, ratings).
            Data is not normally distributed.
            You suspect a monotonic but not linear relationship.
            Outliers are present.
```

**黄金法则：** 相关不代表因果。冰淇淋销量与溺水死亡人数存在相关性，因为两者都会在夏季增加。模型准确率与参数数量存在相关性，但增加参数并不会自动提高准确率，过拟合就是一个反例。

### 协方差矩阵

两个变量之间的协方差，衡量它们如何共同变化：

```text
Cov(X, Y) = (1/n) * sum((x_i - x_bar)(y_i - y_bar))

Cov(X, Y) > 0:  X and Y tend to increase together
Cov(X, Y) < 0:  when X increases, Y tends to decrease
Cov(X, Y) = 0:  no linear co-movement
```

对于 d 个特征，协方差矩阵 C 是一个 d x d 矩阵，其中 C[i][j] = Cov(feature_i, feature_j)。对角元素 C[i][i] 是各个特征的方差。

```text
C = | Var(x1)      Cov(x1,x2)  Cov(x1,x3) |
    | Cov(x2,x1)  Var(x2)      Cov(x2,x3) |
    | Cov(x3,x1)  Cov(x3,x2)  Var(x3)     |

Properties:
  - Symmetric: C[i][j] = C[j][i]
  - Positive semi-definite: all eigenvalues >= 0
  - Diagonal = variances
  - Off-diagonal = covariances
```

**与 PCA 的联系。** PCA 会对协方差矩阵进行特征分解。特征向量就是主成分，也就是方差最大的方向；特征值则告诉你每个主成分保留了多少方差。这正是第 10 课介绍的内容。现在你可以理解，为什么应当分解协方差矩阵：它编码了数据中所有两两变量之间的线性关系。

**与相关性的联系。** 相关矩阵就是标准化变量的协方差矩阵，即每个变量都除以自身标准差后的协方差矩阵。相关系数对协方差进行了归一化，使所有值都落在 [-1, 1] 内。

### 假设检验

假设检验（hypothesis testing）是一套在不确定性下作出决策的框架。你先提出一个论断，然后收集数据，再判断数据是否与该论断相符。

**基本设定：**

```text
Null hypothesis (H0):        the default assumption, usually "no effect"
Alternative hypothesis (H1): what you are trying to show

Example:
  H0: Model A and Model B have the same accuracy
  H1: Model B has higher accuracy than Model A
```

**p 值（p-value）** 是在 H0 为真的假设下，出现与观测数据同样极端的数据的概率。它不是 H0 为真的概率。这是统计学中最常见的误解。

```text
p-value = P(data this extreme | H0 is true)

If p-value < alpha (typically 0.05):
    Reject H0. The result is "statistically significant."
If p-value >= alpha:
    Fail to reject H0. You do not have enough evidence.
    This does NOT mean H0 is true.
```

**置信区间（confidence interval）** 给出参数可能取值的范围：

```text
95% confidence interval for the mean:
    x_bar +/- z * (s / sqrt(n))

where z = 1.96 for 95% confidence

Interpretation: if you repeated this experiment many times, 95% of the
computed intervals would contain the true mean. It does NOT mean there
is a 95% probability the true mean is in this specific interval.
```

置信区间的宽度反映了估计的精度。区间宽，意味着不确定性高；区间窄，意味着估计精度较高，但如果数据存在偏差，估计未必准确。

### t 检验

t 检验（t-test）用于比较均值，有几种不同形式。

**单样本 t 检验：** 总体均值是否与某个假设值不同？

```text
t = (x_bar - mu_0) / (s / sqrt(n))

degrees of freedom = n - 1
```

**双样本 t 检验（独立样本）：** 两组的均值是否不同？

```text
t = (x_bar_1 - x_bar_2) / sqrt(s1^2/n1 + s2^2/n2)

This is Welch's t-test, which does not assume equal variances.
Always use Welch's unless you have a specific reason for equal variances.
```

**配对 t 检验：** 用于成对的测量值，例如在相同的数据划分上评估同一个模型：

```text
Compute d_i = x_i - y_i for each pair
Then run a one-sample t-test on the d_i values against mu_0 = 0
```

在 ML 中，配对 t 检验很常见：让两个模型在同样的 10 个交叉验证折上运行，然后逐对比较它们的得分。

### 卡方检验

卡方检验（chi-squared test）用于检查观测频数是否与期望频数相符，适用于类别数据。

```text
chi^2 = sum((observed - expected)^2 / expected)

Example: does a language model's output distribution match the
training distribution across categories?

Category    Observed   Expected
Positive       120        100
Negative        80        100
chi^2 = (120-100)^2/100 + (80-100)^2/100 = 4 + 4 = 8

With 1 degree of freedom, chi^2 = 8 gives p < 0.005.
The difference is significant.
```

### ML 模型的 A/B 测试

ML 中的 A/B 测试与网页 A/B 测试并不相同。模型比较有一些特有的挑战：

```text
1. Same test set:    Both models must be evaluated on identical data.
                     Different test sets make comparison meaningless.

2. Multiple metrics: Accuracy alone is not enough. You need precision,
                     recall, F1, latency, and fairness metrics.

3. Variance:         Use cross-validation or bootstrap to estimate
                     the variance of each metric, not just point estimates.

4. Data leakage:     If the test set was used during model selection,
                     your comparison is biased. Hold out a final test set.
```

**具体步骤：**

```text
1. Define your metric and significance level (alpha = 0.05)
2. Run both models on the same k-fold cross-validation splits
3. Collect paired scores: [(a1, b1), (a2, b2), ..., (ak, bk)]
4. Compute differences: d_i = b_i - a_i
5. Run a paired t-test on the differences
6. Check: is the mean difference significantly different from 0?
7. Compute a confidence interval for the mean difference
8. Compute effect size (Cohen's d) to judge practical significance
```

### 统计显著性与实际显著性

一个结果可以具有统计显著性，却没有实际意义。只要数据足够多，即使微不足道的差异也会变得统计显著。

```text
Example:
  Model A accuracy: 0.9234
  Model B accuracy: 0.9237
  n = 1,000,000 test samples
  p-value = 0.001

Statistically significant? Yes.
Practically significant? A 0.03% improvement is not worth the
engineering cost of deploying a new model.
```

**效应量（effect size）** 用于量化差异有多大，与样本量无关：

```text
Cohen's d = (mean_1 - mean_2) / pooled_std

d = 0.2:  small effect
d = 0.5:  medium effect
d = 0.8:  large effect
```

务必同时报告 p 值和效应量。p 值告诉你差异是否真实，效应量告诉你这个差异是否重要。

### 多重比较问题

检验许多个假设时，总会有一些结果因偶然而“显著”。如果在 alpha = 0.05 下检验 20 项，即使都不存在真实效应，预期也会出现 1 个假阳性。

```text
P(at least one false positive) = 1 - (1 - alpha)^m

m = 20 tests, alpha = 0.05:
P(false positive) = 1 - 0.95^20 = 0.64

You have a 64% chance of at least one false positive.
```

**Bonferroni 校正（Bonferroni correction）：** 将 alpha 除以检验次数。

```text
Adjusted alpha = alpha / m = 0.05 / 20 = 0.0025

Only reject H0 if p-value < 0.0025.
Conservative but simple. Works when tests are independent.
```

在 ML 中，当你用多个指标比较一个模型、测试许多超参数配置，或在多个数据集上评估时，这一点就很重要。

### bootstrap 方法

bootstrap（自助法）通过对数据进行有放回重采样，估计统计量的抽样分布。它不需要对底层分布作任何假设。

**算法步骤：**

```text
1. You have n data points
2. Draw n samples WITH replacement (some points appear multiple times,
   some not at all)
3. Compute your statistic on this bootstrap sample
4. Repeat B times (typically B = 1000 to 10000)
5. The distribution of bootstrap statistics approximates the
   sampling distribution
```

**bootstrap 置信区间（百分位法）：**

```text
Sort the B bootstrap statistics
95% CI = [2.5th percentile, 97.5th percentile]
```

**为什么 bootstrap 对 ML 很重要：**

```text
- Test set accuracy is a point estimate. Bootstrap gives you
  confidence intervals.
- You cannot assume metric distributions are normal (especially
  for AUC, F1, precision at k).
- Bootstrap works for ANY statistic: median, ratio of two means,
  difference in AUC between two models.
- No closed-form formula needed.
```

**用 bootstrap 比较模型：**

```text
1. You have predictions from Model A and Model B on the same test set
2. For each bootstrap iteration:
   a. Resample test indices with replacement
   b. Compute metric_A and metric_B on the resampled set
   c. Store diff = metric_B - metric_A
3. 95% CI for the difference:
   [2.5th percentile of diffs, 97.5th percentile of diffs]
4. If the CI does not contain 0, the difference is significant
```

它比配对 t 检验更稳健，因为它不作任何分布假设。

### 参数检验与非参数检验

**参数检验（parametric tests）** 假设数据服从某种特定分布，通常是正态分布：

```text
t-test:         assumes normally distributed data (or large n by CLT)
ANOVA:          assumes normality and equal variances
Pearson r:      assumes bivariate normality
```

**非参数检验（non-parametric tests）** 不作任何分布假设：

```text
Mann-Whitney U:     compares two groups (replaces independent t-test)
Wilcoxon signed-rank: compares paired data (replaces paired t-test)
Spearman rho:       correlation on ranks (replaces Pearson)
Kruskal-Wallis:     compares multiple groups (replaces ANOVA)
```

**非参数检验的适用场景：**

```text
- Small sample size (n < 30) and data is clearly non-normal
- Ordinal data (ratings, rankings)
- Heavy outliers you cannot remove
- Skewed distributions
```

**参数检验的适用场景：**

```text
- Large sample size (CLT makes the test statistic approximately normal)
- Data is roughly symmetric without extreme outliers
- More statistical power (better at detecting real differences)
```

在 ML 实验中，n 通常较小，例如只有 5 或 10 个交叉验证折，因此 Wilcoxon 符号秩检验等非参数检验，往往比 t 检验更合适。

### 中心极限定理：实际意义

中心极限定理（CLT）指出，随着 n 增大，样本均值的分布会趋近于正态分布，而不论原始总体服从什么分布。

```text
If X_1, X_2, ..., X_n are iid with mean mu and variance sigma^2:

    X_bar ~ Normal(mu, sigma^2 / n)    as n -> infinity

Works for n >= 30 in most cases.
For highly skewed distributions, you might need n >= 100.
```

**为什么这对 ML 很重要：**

```text
1. Justifies confidence intervals and t-tests on aggregated metrics
2. Explains why averaging over cross-validation folds gives stable
   estimates even when individual folds vary wildly
3. Mini-batch gradient descent works because the average gradient
   over a batch approximates the true gradient (CLT in action)
4. Ensemble methods: averaging predictions from many models gives
   more stable output than any single model
```

**CLT 不能做到的事：**

```text
- Does NOT make your data normal. It makes the MEAN of samples normal.
- Does NOT work for heavy-tailed distributions with infinite variance
  (Cauchy distribution).
- Does NOT apply to dependent data (time series without correction).
```

### ML 论文中常见的统计错误

1. **在训练集上测试。** 这必然导致过拟合。务必留出模型在训练期间从未见过的数据。

2. **不报告置信区间。** 只报告一个准确率数值，却不说明不确定性，会让结果无法复现，也无法验证。

3. **忽视多重比较。** 测试 50 种配置，只报告最好的一种而不作校正，会抬高假阳性率。

4. **混淆统计显著性与实际显著性。** 准确率提高 0.01% 时，即使 p 值为 0.001，也没有意义。

5. **在不平衡数据上使用准确率。** 如果数据集中有 99% 的样本属于负类，那么 99% 的准确率意味着模型什么也没学到。应使用精确率、召回率、F1 或 AUC。

6. **挑选有利的指标。** 只报告模型胜出的那个指标。诚实的评估应报告所有相关指标。

7. **训练集与测试集划分之间发生信息泄漏。** 例如先归一化再划分，或者用未来的数据预测过去。

8. **测试集很小，而且没有方差估计。** 在 100 个样本上评估，就声称有 2% 的提升，这是噪声，不是信号。

9. **数据并不独立，却假定它们独立。** 例如同一患者的医学图像、同一文档中的多个句子。同一组内的观测值是相关的。

10. **p 值操纵（p-hacking）。** 不断尝试不同的检验、子集或排除标准，直到得到 p < 0.05。这样的结果只是搜索过程造成的假象。

## 动手实现

你将实现：

1. **从零实现描述统计**，包括均值、中位数、众数、标准差、百分位数和 IQR
2. **相关系数函数**，包括 Pearson、Spearman 相关系数及协方差矩阵
3. **假设检验**，包括单样本 t 检验、双样本 t 检验和卡方检验
4. **bootstrap 置信区间**，用于任意统计量，不需要任何假设
5. **A/B 测试模拟器**，生成数据、进行检验，并检查 I 类与 II 类错误
6. **统计显著性与实际显著性的演示**，展示较大的 n 如何让一切都变得“显著”

全部从零实现，只使用 `math` 和 `random`，不使用 numpy，也不使用 scipy。

```figure
f3-bootstrap-resample
```

## 关键术语

| 术语 | 定义 |
|---|---|
| 均值 | 数值之和除以数量，对离群值敏感。 |
| 中位数 | 排序后数据的中间值，对离群值具有鲁棒性。 |
| 标准差 | 方差的平方根，以数据原有单位衡量离散程度。 |
| 百分位数 | 低于该值的数据占给定百分比。 |
| IQR（四分位距） | Q3 减去 Q1，反映中间 50% 数据的离散范围。 |
| Pearson 相关系数 | 衡量两个变量的线性关联，范围为 [-1, 1]。 |
| Spearman 相关系数 | 通过秩衡量单调关联。 |
| 协方差矩阵 | 所有特征两两之间的协方差组成的矩阵。 |
| 零假设 | 默认不存在效应或差异的假设。 |
| p 值 | 给定零假设为真时，出现如此极端的数据的概率。 |
| 置信区间 | 在给定置信水平下，参数可能取值的范围。 |
| t 检验 | 检验均值是否有显著差异，使用 t 分布。 |
| 卡方检验 | 检验观测频数是否与期望频数不同。 |
| 效应量 | 差异的大小，与样本量无关，常用的是 Cohen's d。 |
| Bonferroni 校正 | 将显著性阈值除以检验次数，以控制假阳性。 |
| bootstrap | 有放回重采样，用于估计抽样分布。 |
| I 类错误 | 假阳性：在零假设为真时拒绝 H0。 |
| II 类错误 | 假阴性：在零假设为假时未拒绝 H0。 |
| 统计功效 | 正确拒绝为假的 H0 的概率。功效 = 1 减去 II 类错误率。 |
| 中心极限定理 | 随着样本量增大，样本均值趋向正态分布。 |
| 参数检验 | 假设数据服从特定分布，通常是正态分布。 |
| 非参数检验 | 不作任何分布假设，基于秩或符号进行检验。 |
