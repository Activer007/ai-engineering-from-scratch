# 范数与距离

> 距离函数决定了“相似”的含义。选错了，所有下游环节都会出问题。

**Type:** Build
**Language:** Python
**Prerequisites:** 阶段 1，第 01 课（线性代数直觉）、第 02 课（向量、矩阵与运算）
**Time:** ~90 分钟

## 学习目标

- 从零实现 L1、L2、余弦、Mahalanobis、Jaccard 和编辑距离函数
- 为给定的机器学习（ML）任务选择合适的距离度量（metric），并解释其他选择为什么不适用
- 将 L1、L2 范数与 LASSO、Ridge 正则化及其几何约束区域联系起来
- 展示同一数据集在不同度量下如何产生不同的最近邻

## 要解决的问题

你有两个向量。它们可能是词嵌入，也可能是用户画像，或是像素数组。你需要知道：它们有多接近？

答案完全取决于你选择哪个距离函数。两个数据点在一种度量下可能互为最近邻，在另一种度量下却可能相距甚远。你的 KNN 分类器、推荐引擎、向量数据库、聚类算法和损失函数都依赖这一选择。选错了，模型就会朝着错误的目标优化。

没有一种距离在所有场景下都是最优的。L2 适用于空间数据；余弦相似度在自然语言处理（NLP）中占主导地位；Jaccard 处理集合；编辑距离处理字符串；Mahalanobis 将相关性纳入考虑；Wasserstein 搬运概率质量。每一种方法都体现了对“相似”含义的不同假设。

本课将从零构建各种主要的距离函数，说明它们各自适用的场景，并展示同样的数据如何因度量不同而产生完全不同的最近邻。

## 核心概念

### 范数：衡量向量的模长

范数（norm）衡量向量的“大小”。两个向量之间的任何距离函数都可以写成它们之差的范数：d(a, b) = ||a - b||。因此，理解范数也就是理解距离。

### L1 范数（Manhattan 距离）

L1 范数将所有分量的绝对值相加。

```text
||x||_1 = |x_1| + |x_2| + ... + |x_n|
```

之所以称为 Manhattan 距离，是因为它衡量的是在城市网格中只能沿坐标轴方向行走时的路程，不能走对角线。

```text
Point A = (1, 1)
Point B = (4, 5)

L1 distance = |4-1| + |5-1| = 3 + 4 = 7

On a grid, you walk 3 blocks east and 4 blocks north.
```

L1 的适用场景：
- 高维稀疏数据（文本特征、one-hot 独热编码）
- 希望对离群值具有鲁棒性时（单个巨大的差值不会占据主导）
- 特征选择问题（L1 正则化促进稀疏性）

与 L1 正则化（Lasso）的联系：在损失函数中加入 ||w||_1，就是惩罚权重绝对值之和。这会将较小的权重推到精确的零，从而自动进行特征选择。L1 惩罚在权重空间中形成菱形约束区域，菱形的顶点位于坐标轴上，在这些位置有些权重为零。

与损失函数的联系：平均绝对误差（Mean Absolute Error，MAE）是预测值与目标值之间 L1 距离的平均值。它对所有误差施加线性惩罚，因此相比 MSE，对离群值更具鲁棒性。

### L2 范数（欧氏距离，Euclidean distance）

L2 范数就是直线距离，即各分量平方和的平方根。

```text
||x||_2 = sqrt(x_1^2 + x_2^2 + ... + x_n^2)
```

这就是你在几何课上学过的距离，也就是 n 维的 Pythagoras 定理（勾股定理）。

```text
Point A = (1, 1)
Point B = (4, 5)

L2 distance = sqrt((4-1)^2 + (5-1)^2) = sqrt(9 + 16) = sqrt(25) = 5.0

The straight line, cutting diagonally through the grid.
```

L2 的适用场景：
- 低维到中等维数的连续数据
- 各特征尺度相近时
- 物理距离（空间数据、传感器读数）
- 像素层面的图像相似度

与 L2 正则化（Ridge）的联系：在损失函数中加入 ||w||_2^2，会对较大的权重施加惩罚。与 L1 不同，它不会将权重推到零，而是按比例将所有权重向零收缩。L2 惩罚形成圆形约束区域，因此坐标轴上没有顶点。权重会变小，但很少精确地等于零。

与损失函数的联系：均方误差（Mean Squared Error，MSE）是 L2 距离平方的平均值。平方运算对大误差施加的惩罚比小误差更重。

```text
MAE (L1 loss):  |y - y_hat|         Linear penalty. Robust to outliers.
MSE (L2 loss):  (y - y_hat)^2       Quadratic penalty. Sensitive to outliers.
```

### Lp 范数：一般形式

L1 和 L2 都是 Lp 范数的特例：

```text
||x||_p = (|x_1|^p + |x_2|^p + ... + |x_n|^p)^(1/p)
```

不同的 p 值会产生形状不同的“单位球”（与原点距离为 1 的所有点构成的集合）：

```text
p=1:    Diamond shape      (corners on axes)
p=2:    Circle/sphere      (the usual round ball)
p=3:    Superellipse       (rounded square)
p=inf:  Square/hypercube   (flat sides along axes)
```

### L-infinity 范数（Chebyshev 距离）

当 p 趋向无穷大时，Lp 范数收敛到各分量绝对值中的最大值。

```text
||x||_inf = max(|x_1|, |x_2|, ..., |x_n|)
```

两点之间的距离由它们差异最大的那个维度决定，其他所有维度都被忽略。

```text
Point A = (1, 1)
Point B = (4, 5)

L-inf distance = max(|4-1|, |5-1|) = max(3, 4) = 4
```

L-infinity 的适用场景：
- 任一维度上的最坏偏差都很重要时
- 棋盘（国际象棋中的王按 L-infinity 距离移动：向任意方向走一步的代价都是 1）
- 制造公差（每个维度都必须符合规格）

### 余弦相似度与余弦距离

余弦相似度（cosine similarity）衡量两个向量之间的夹角，忽略它们的模长。

```text
cos_sim(a, b) = (a . b) / (||a||_2 * ||b||_2)
```

其取值范围为 -1（方向相反）到 +1（方向相同）。相互垂直的向量，其余弦相似度为 0。

余弦距离将其转换为距离：cosine_distance = 1 - cosine_similarity。其取值范围为 0（方向相同）到 2（方向相反）。

```text
a = (1, 0)    b = (1, 1)

cos_sim = (1*1 + 0*1) / (1 * sqrt(2)) = 1/sqrt(2) = 0.707
cos_dist = 1 - 0.707 = 0.293
```

为什么余弦相似度在 NLP 和嵌入中占主导地位：对于文本，文档长度不应影响相似度。一篇讨论猫的文档，即使长度是另一篇同主题文档的两倍，两者仍应“相似”。余弦相似度忽略模长（长度），只关心方向。两篇词语分布相同但长度不同的文档指向同一方向，余弦相似度为 1.0。

余弦相似度的适用场景：
- 文本相似度（TF-IDF 向量、词嵌入、句子嵌入）
- 任何模长是噪声、方向是信号的领域
- 推荐系统（用户偏好向量）
- 嵌入搜索（向量数据库几乎总是使用余弦相似度或点积）

### 点积相似度与余弦相似度

两个向量的点积为：

```text
a . b = a_1*b_1 + a_2*b_2 + ... + a_n*b_n
      = ||a|| * ||b|| * cos(angle)
```

余弦相似度就是用两个向量的模长对点积进行归一化。当两个向量都已经归一化为单位向量（模长 = 1）时，点积与余弦相似度完全相同。

```text
If ||a|| = 1 and ||b|| = 1:
    a . b = cos(angle between a and b)
```

它们的区别在于：点积包含模长信息。模长较大的向量会得到更高的点积分数。在某些检索系统中，如果你希望“热门”条目排得更靠前，这一点就很重要。模长充当了一种隐含的质量或重要性信号。

```text
a = (3, 0)    b = (1, 0)    c = (0, 1)

dot(a, b) = 3     dot(a, c) = 0
cos(a, b) = 1.0   cos(a, c) = 0.0

Both agree on direction, but dot product also reflects magnitude.
```

实际使用时：
- 只关心方向上的相似性时，使用余弦相似度
- 模长包含有意义的信息时，使用点积
- 许多向量数据库（Pinecone、Weaviate、Qdrant）允许你在两者之间选择
- 如果嵌入已经过 L2 归一化，选哪一种都一样

### Mahalanobis 距离

欧氏距离对所有维度一视同仁。但如果特征之间存在相关性，或者尺度不同，L2 就会给出误导性的结果。

Mahalanobis 距离会将数据的协方差结构纳入考虑。

```text
d_M(x, y) = sqrt((x - y)^T * S^(-1) * (x - y))
```

其中，S 是数据的协方差矩阵。

直观地说，Mahalanobis 距离先对数据去相关并归一化（白化，whitening），再在变换后的空间中计算 L2 距离。如果 S 是单位矩阵（特征互不相关且具有单位方差），Mahalanobis 距离就退化为欧氏距离。

```text
Example: height and weight are correlated.
Someone 6'2" and 180 lbs is not unusual.
Someone 5'0" and 180 lbs is unusual.

Euclidean distance might say they are equally far from the mean.
Mahalanobis distance correctly identifies the second as an outlier
because it accounts for the height-weight correlation.
```

Mahalanobis 距离的适用场景：
- 离群值检测（与均值的 Mahalanobis 距离较大的点就是离群值）
- 特征具有不同尺度和相关性时的分类
- 有足够的数据来估计可靠的协方差矩阵时
- 制造业质量控制（多变量过程监控）

### Jaccard 相似度（用于集合）

Jaccard 相似度衡量两个集合的重叠程度。

```text
J(A, B) = |A intersect B| / |A union B|
```

其取值范围为 0（没有重叠）到 1（集合相同）。Jaccard 距离 = 1 - Jaccard 相似度。

```text
A = {cat, dog, fish}
B = {cat, bird, fish, snake}

Intersection = {cat, fish}         size = 2
Union = {cat, dog, fish, bird, snake}  size = 5

Jaccard similarity = 2/5 = 0.4
Jaccard distance = 0.6
```

Jaccard 的适用场景：
- 比较标签、类别或特征构成的集合
- 根据词语是否出现来衡量文档相似度（而非出现频率）
- 近重复检测（用 MinHash 近似 Jaccard）
- 比较二元特征向量（表示存在或不存在的数据）
- 评估分割模型（交并比，Intersection over Union = Jaccard）

### 编辑距离（Levenshtein 距离）

编辑距离（edit distance）计算将一个字符串转换成另一个字符串所需的最少单字符操作次数。操作包括插入、删除和替换。

```text
"kitten" -> "sitting"

kitten -> sitten  (substitute k -> s)
sitten -> sittin  (substitute e -> i)
sittin -> sitting (insert g)

Edit distance = 3
```

使用动态规划计算。填充一个矩阵，其中位置 (i, j) 的值是字符串 A 的前 i 个字符与字符串 B 的前 j 个字符之间的编辑距离。

```text
        ""  s  i  t  t  i  n  g
    ""   0  1  2  3  4  5  6  7
    k    1  1  2  3  4  5  6  7
    i    2  2  1  2  3  4  5  6
    t    3  3  2  1  2  3  4  5
    t    4  4  3  2  1  2  3  4
    e    5  5  4  3  2  2  3  4
    n    6  6  5  4  3  3  2  3
```

编辑距离的适用场景：
- 拼写检查与纠正
- DNA 序列比对（使用带权重的操作）
- 字符串模糊匹配
- 杂乱文本数据的去重

### KL 散度（不是距离，却常被当作距离使用）

KL 散度衡量一个概率分布与另一个分布有何不同。第 09 课已经介绍过它，但这里仍要讨论，因为虽然它不是距离，人们还是会将它当作“距离”使用。

```text
D_KL(P || Q) = sum(p(x) * log(p(x) / q(x)))
```

关键性质：KL 散度不对称。

```text
D_KL(P || Q) != D_KL(Q || P)
```

这意味着它不满足距离度量的基本要求。它也不满足三角不等式。它是散度，而不是距离。

前向 KL（D_KL(P || Q)）具有“均值寻求”（mean-seeking）倾向：Q 试图覆盖 P 的所有众数。
反向 KL（D_KL(Q || P)）具有“众数寻求”（mode-seeking）倾向：Q 专注于 P 的单个众数。

你会在以下场景中看到 KL 散度：
- VAE（ELBO 中的 KL 项将潜在分布推向某个先验）
- 知识蒸馏（学生模型试图匹配教师模型的分布）
- RLHF（KL 惩罚让微调后的模型保持接近基础模型）
- 策略梯度方法（约束策略更新）

### Wasserstein 距离（推土距离）

Wasserstein 距离（Earth Mover's Distance，推土距离）衡量将一个概率分布转换成另一个分布所需的最小“工作量”。可以这样理解：如果一个分布是一堆土，另一个分布是一个坑，你需要搬多少土，又要搬多远？

```text
W(P, Q) = inf over all transport plans gamma of E[d(x, y)]
```

对于 1D 分布，它可简化为两个累积分布函数（CDF）之差的绝对值的积分：

```text
W_1(P, Q) = integral |CDF_P(x) - CDF_Q(x)| dx
```

Wasserstein 的重要性：
- 它是真正的度量（对称，满足三角不等式）
- 即使两个分布没有重叠，它也能提供梯度（此时 KL 散度会趋向无穷大）
- 这一性质使它成为 Wasserstein GAN（WGAN）的核心，WGAN 解决了原始 GAN 的训练不稳定问题

```text
Distributions with no overlap:

P: [1, 0, 0, 0, 0]    Q: [0, 0, 0, 0, 1]

KL divergence: infinity (log of zero)
Wasserstein: 4 (move all mass 4 bins)

Wasserstein gives a meaningful gradient. KL does not.
```

Wasserstein 的适用场景：
- GAN 训练（WGAN、WGAN-GP）
- 比较可能不重叠的分布
- 最优传输问题
- 图像检索（比较颜色直方图）

### 为什么不同任务需要不同距离

| 任务 | 最佳距离 | 原因 |
|------|--------------|-----|
| 文本相似度 | 余弦 | 模长是噪声，方向承载含义 |
| 图像像素比较 | L2 | 空间关系很重要，各特征的尺度相近 |
| 稀疏高维特征 | L1 | 具有鲁棒性，不会放大少见的大差异 |
| 集合重叠（标签、类别） | Jaccard | 数据天然是集合，而不是向量 |
| 字符串匹配 | 编辑距离 | 操作符合人类对编辑的直觉 |
| 离群值检测 | Mahalanobis | 考虑特征的相关性与尺度 |
| 比较分布 | KL 散度 | 衡量用 Q 代替 P 所损失的信息 |
| GAN 训练 | Wasserstein | 即使分布不重叠，也能提供梯度 |
| 嵌入（向量数据库） | 余弦或点积 | 嵌入经过训练，将含义编码在方向中 |
| 推荐 | 点积 | 模长可以编码受欢迎程度或置信度 |
| DNA 序列 | 加权编辑距离 | 替换代价因核苷酸对而异 |
| 制造业质量控制 | L-infinity | 任一维度上的最坏偏差都很重要 |

### 与损失函数的联系

损失函数就是应用于预测值与目标值之间的距离函数。

```text
Loss function       Distance it uses       Behavior
MSE                 L2 squared             Penalizes large errors heavily
MAE                 L1                     Penalizes all errors equally
Huber loss          L1 for large errors,   Best of both: robust to outliers,
                    L2 for small errors    smooth gradient near zero
Cross-entropy       KL divergence          Measures distribution mismatch
Hinge loss          max(0, margin - d)     Only penalizes below margin
Triplet loss        L2 (typically)         Pulls positives close, pushes
                                           negatives away
Contrastive loss    L2                     Similar pairs close, dissimilar
                                           pairs beyond margin
```

### 与正则化的联系

正则化会在损失函数中加入对权重的范数惩罚。

```text
L1 regularization (Lasso):   loss + lambda * ||w||_1
  -> Sparse weights. Some weights become exactly zero.
  -> Automatic feature selection.
  -> Solution has corners (non-differentiable at zero).

L2 regularization (Ridge):   loss + lambda * ||w||_2^2
  -> Small weights. All weights shrink toward zero.
  -> No feature selection (nothing goes to exactly zero).
  -> Smooth solution everywhere.

Elastic Net:                  loss + lambda_1 * ||w||_1 + lambda_2 * ||w||_2^2
  -> Combines sparsity of L1 with stability of L2.
  -> Groups of correlated features are kept or dropped together.
```

为什么 L1 会产生稀疏性，而 L2 不会：想象 2D 权重空间中的约束区域。L1 是菱形，L2 是圆形。损失函数的等高线（椭圆）最有可能在菱形的顶点处与之相切，此时某个权重为零。等高线与圆形相切时则位于光滑点，此时两个权重都不为零。

### 最近邻搜索

每个距离函数都对应一个最近邻搜索问题：给定一个查询点，在数据集中找出离它最近的点。

对于包含 n 个 d 维数据点的数据集，精确最近邻搜索每次查询的复杂度为 O(n * d)。面对大型数据集，这太慢了。

近似最近邻（Approximate Nearest Neighbor，ANN）算法以少量准确性的损失换取大幅提速：

```text
Algorithm         Approach                      Used by
KD-trees          Axis-aligned space partition   scikit-learn (low-dim)
Ball trees        Nested hyperspheres            scikit-learn (medium-dim)
LSH               Random hash projections        Near-duplicate detection
HNSW              Hierarchical navigable         FAISS, Qdrant, Weaviate
                  small-world graph
IVF               Inverted file index with       FAISS (billion-scale)
                  cluster-based search
Product quant.    Compress vectors, search       FAISS (memory-constrained)
                  in compressed space
```

HNSW（Hierarchical Navigable Small World，分层可导航小世界）是现代向量数据库中的主流算法。它构建一个多层图，每个节点都与自己的近似最近邻相连。搜索从顶层（稀疏、长距离跳转）开始，逐层下降到底层（密集、短距离跳转）。

```figure
norm-unit-balls
```

## 动手实现

### 步骤 1：所有范数与距离函数

完整实现见 `code/distances.py`。每个函数都仅使用 Python 基础数学运算从零构建。

### 步骤 2：相同数据，不同距离，不同近邻

`distances.py` 中的演示创建一个数据集，选取一个查询点，并展示最近邻如何随距离度量而变化。在 L1 下“最近”的点，在 L2 或余弦度量下未必最近。

### 步骤 3：嵌入相似度搜索

代码包含一个模拟的嵌入相似度搜索：分别使用余弦相似度与 L2 距离，寻找与查询最相似的“文档”，展示两种方法的排序可能不同。

## 实际使用

最常见的实际用途是在向量数据库中查找相似条目。

```python
import numpy as np

def cosine_similarity_matrix(X):
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1, norms)
    X_normalized = X / norms
    return X_normalized @ X_normalized.T

embeddings = np.random.randn(1000, 768)

sim_matrix = cosine_similarity_matrix(embeddings)

query_idx = 0
similarities = sim_matrix[query_idx]
top_k = np.argsort(similarities)[::-1][1:6]
print(f"Top 5 most similar to item 0: {top_k}")
print(f"Similarities: {similarities[top_k]}")
```

当你调用 `model.encode(text)`，再搜索向量数据库时，底层执行的就是这些操作。嵌入模型将文本映射为向量。向量数据库计算查询向量与每个已存储向量之间的余弦相似度（或点积），并通过 ANN 算法避免逐一检查所有向量。

## 练习

1. 计算 (1, 2, 3) 与 (4, 0, 6) 之间的 L1、L2 和 L-infinity 距离。验证对于任意一对点，L-inf <= L2 <= L1 始终成立，并证明为什么这一顺序必然成立。

2. 构造两个向量，使其余弦相似度很高（> 0.9），但 L2 距离很大（> 10）。从几何角度解释这一现象。然后再构造两个向量，使其余弦相似度很低（< 0.3），但 L2 距离很小（< 0.5）。

3. 实现一个函数，接收数据集与查询点，分别返回 L1、L2、余弦和 Mahalanobis 距离下的最近邻。找出一个数据集，使这四种方法选出的最近点各不相同。

4. 使用 CDF 方法，手算 [0.5, 0.5, 0, 0] 与 [0, 0, 0.5, 0.5] 之间的 Wasserstein 距离。然后计算 [0.25, 0.25, 0.25, 0.25] 与 [0, 0, 0.5, 0.5] 之间的距离。哪个更大？为什么？

5. 实现 MinHash，用于近似计算 Jaccard 相似度。生成 100 个随机集合，计算所有集合对的精确 Jaccard 相似度，再与分别使用 50、100、200 个哈希函数的 MinHash 近似结果比较。绘制近似误差。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|----------------------|
| 范数 | “向量的大小” | 将向量映射为非负标量的函数，满足三角不等式、绝对齐次性，并且仅在向量为零向量时取零 |
| L1 范数 | “Manhattan 距离” | 分量绝对值之和。在优化中产生稀疏性，对离群值具有鲁棒性 |
| L2 范数 | “欧氏距离” | 分量平方和的平方根，即欧氏空间中的直线距离 |
| Lp 范数 | “广义范数” | 分量绝对值的 p 次幂之和，再开 p 次方根。L1 和 L2 是其特例 |
| L-infinity 范数 | “最大范数”或“Chebyshev 距离” | 分量绝对值的最大值，即 p 趋向无穷大时 Lp 的极限 |
| 余弦相似度 | “向量之间的夹角” | 用两个向量的模长归一化后的点积，范围为 -1 到 +1，忽略向量长度 |
| 余弦距离 | “1 减去余弦相似度” | 将余弦相似度转换为距离，范围为 0 到 2 |
| 点积 | “未归一化的余弦” | 对应分量乘积之和，等于余弦相似度乘以两个向量的模长 |
| Mahalanobis 距离 | “考虑相关性的距离” | 使用数据的协方差矩阵进行白化（去相关并归一化）后，在所得空间中计算的 L2 距离 |
| Jaccard 相似度 | “集合重叠” | 交集大小除以并集大小，用于集合，而不是向量 |
| 编辑距离 | “Levenshtein 距离” | 将一个字符串变成另一个字符串所需的最少插入、删除和替换次数 |
| KL 散度 | “分布之间的距离” | 不是真正的距离（不对称），衡量使用 Q 编码 P 时额外需要的 bits（比特） |
| Wasserstein 距离 | “推土距离” | 将概率质量从一个分布搬运到另一个分布所需的最小工作量，是真正的度量 |
| 近似最近邻 | “ANN 搜索” | 以远快于精确搜索的速度找到近似最近点的算法（HNSW、LSH、IVF） |
| HNSW | “向量数据库算法” | 分层可导航小世界图，用于快速近似最近邻搜索的多层图 |
| L1 正则化 | “Lasso” | 在损失中加入权重的 L1 范数，将权重推到零（稀疏性） |
| L2 正则化 | “Ridge”或“权重衰减” | 在损失中加入权重的 L2 范数平方，将权重向零收缩，但不产生稀疏性 |
| Elastic Net | “L1 + L2” | 结合 L1 和 L2 正则化，比单独使用其中任一种更善于处理相关特征组 |

## 延伸阅读

- [FAISS：高效相似度搜索库](https://github.com/facebookresearch/faiss) - Meta 用于 billion（十亿）级 ANN 搜索的库
- [Wasserstein GAN（Arjovsky 等，2017）](https://arxiv.org/abs/1701.07875) - 将推土距离引入 GAN 的论文
- [局部敏感哈希（Indyk 与 Motwani，1998）](https://dl.acm.org/doi/10.1145/276698.276876) - 基础性的 ANN 算法
- [词表示的高效估计（Mikolov 等，2013）](https://arxiv.org/abs/1301.3781) - Word2Vec，余弦相似度在其中成为嵌入的默认选择
- [sklearn.neighbors 文档](https://scikit-learn.org/stable/modules/neighbors.html) - scikit-learn 距离度量与近邻算法的实用指南
