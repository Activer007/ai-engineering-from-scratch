# S13 降维术语增量 v1.0

2026-10-02。联用核心及 S05–S12 数学词表。保持 PCA、t-SNE、UMAP 等缩写/API；语境区分核函数、Jupyter kernel 和操作系统内核。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| dimensionality reduction | 降维（dimensionality reduction） | 减少特征空间维数，不是缩减训练样本数 |
| curse of dimensionality | 维数灾难（curse of dimensionality） | 源距离/体积/样本复杂度的条件缺口另列 |
| high-dimensional / ambient dimension | 高维 / 环境维数 | 数据所在空间维数不等于内在维数 |
| manifold / intrinsic dimension | 流形（manifold）/ 内在维数 | 曲面类比，不保证任何数据都位于低维流形 |
| PCA / principal component | 主成分分析（PCA）/ 主成分 | 沿用 S06，特征向量方向与投影得分分开 |
| covariance matrix | 协方差矩阵 | 不等于标准化后的相关系数矩阵；np.cov样本分母n-1保留 |
| center / standardize | 中心化 / 标准化 | 减均值与按标准差缩放不同，本课PCA仅前者 |
| positive semi-definite | 半正定（positive semi-definite） | 零特征值允许，不误译成正定 |
| eigendecomposition | 特征分解（eigendecomposition） | eigenvalue/vector沿用特征值/特征向量，不混奇异值 |
| orthogonal / orthonormal | 正交 / 标准正交 | 正交性与单位范数不同，重特征值的基不唯一 |
| explained variance ratio | 方差解释率（explained variance ratio） | 保留总方差比例；源95%information不能暗改成95%variance |
| cumulative explained variance | 累计解释方差 | 累加比例时按源上下文，阈值与分类信息非同义 |
| elbow method | 肘部法（elbow method） | 曲线拐点启发式，不保证唯一最佳k |
| projection / reconstruction | 投影 / 重构 | 中心化数据与原坐标加回均值需分清；源漏项单列 |
| t-SNE | t-SNE（t分布随机邻域嵌入） | t-Distributed Stochastic Neighbor Embedding；缩写大小写保留 |
| perplexity | 困惑度（perplexity） | 此处是t-SNE邻域熵参数，区别于S12语言模型评估指标 |
| UMAP | UMAP（均匀流形近似与投影） | Uniform Manifold Approximation and Projection；不保证全局距离保真 |
| fuzzy topological representation | 模糊拓扑表示 | fuzzy数学集合/图语境，不是图画不清晰 |
| kernel PCA / kernel trick | 核PCA / 核技巧（kernel trick） | 核函数诱导特征空间；不是OS/Jupyter内核或GPU kernel |
| RBF / Gaussian kernel | 径向基函数（RBF）核 / 高斯核 | gamma、范数平方、负号和exp保持 |
| pre-image | 原像（pre-image） | 特征空间回原输入的近似问题，不是图片预览 |
| reconstruction error / MSE | 重构误差 / 均方误差（MSE） | 元素平均与样本平方和及丢弃特征值之和不同，不能暗改源等式 |
| downstream performance | 下游任务表现 | 解释方差不等于目标预测价值；分训练/验证/测试 |
| n_components / components_ | 保留英文标识符 | 模型参数k与特征数d/样本数n、行/列方向不可混 |

表格RBF公式的转义竖线和裸乘号需真实GFM检查，必要仅最小可逆语法调整并重新绑定审校。代码、公式/图载荷、数值、复杂度、路径/链接/API原样；源技术错误仅定位记录，不以翻译名义改代码或引入额外研究任务。
