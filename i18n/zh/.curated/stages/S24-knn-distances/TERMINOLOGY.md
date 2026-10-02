# S24 K近邻与距离术语增量 v1.0

2026-10-02。主协调已确认无冲突。联用核心、补充及 S05–S22 固定词表；距离沿用 S16，维数与维数灾难沿用 S13，分类/回归/偏差方差沿用 S22。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| K-nearest neighbors / KNN | K近邻（KNN） | 保留 K 与缩写；不与最近质心分类器混同 |
| nearest neighbor / approximate nearest neighbor | 最近邻 / 近似最近邻 | 精确与近似搜索区分，ANN 不是人工神经网络 |
| lazy / eager learning | 惰性学习 / 急切学习 | 首现 EN，并注明按训练时机区分；不是模型是否勤奋或计算图 eager 执行 |
| majority vote / distance-weighted voting | 多数投票 / 按距离加权投票 | 票数与距离倒数权重分别呈现，平票与零距离风险单列 |
| KD-tree / ball tree | KD树 / 球树 | 特征轴分区与嵌套超球分开，源复杂度限制不暗补 |
| bounding volume / backtracking / pruning | 包围体 / 回溯 / 剪枝 | 搜索几何与排除分支，不是概率置信区间 |
| brute-force search | 暴力搜索 | 计算全部距离，源省略排序成本单列 |
| curse of dimensionality / intrinsic dimension | 维数灾难 / 内在维数 | 空间维数不等于样本量，源阈值和比值并非普适保证 |
| product quantization | 乘积量化 | 搜索向量压缩语境；不与乘法或所有低精度量化混同 |
| Voronoi diagram | Voronoi图 | 最近训练点诱导的空间划分；按源呈现 K=1 边界 |
| feature scaling / standardization / normalization | 特征缩放 / 标准化 / 归一化 | 一般尺度变换与减均值除标准差不同，不机械统一 |
| non-parametric / extrapolation | 非参数 / 外推 | 无固定参数形式不等于没有 K 等超参数；回归目标范围与输入范围分开 |
| metric / cosine distance / Minkowski | 度量 / 余弦距离 / Minkowski | 源数学公理与 p 定义域不足单列，不改公式 |

SVM、RAG、PCA、UMAP、t-SNE、HNSW、IVF、LSH、TF-IDF、FAISS、Annoy、scikit-learn 及 Python 类/API 原样。自然量级 millions/billion 保留并释义，所有 K、N、d、时间复杂度、数字与单位保持。必要 GFM 最小空格或转义必须可逆并重新绑定审核。
