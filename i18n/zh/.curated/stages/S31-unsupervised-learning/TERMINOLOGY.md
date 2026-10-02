# S31 无监督学习术语增量 v1.0

联用核心、补充及S05–S30固定词表；40份依赖见DEPENDENCIES.json。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| unsupervised learning / clustering / cluster | 无监督学习 / 聚类 / 簇 | 沿S22；cluster在数据分组中用簇，不是基础设施集群 |
| centroid | 质心（centroid） | 沿S22，簇内均值中心，不等同medoid |
| K-Means / Lloyd / K-Means++ | K-Means / Lloyd 算法 / K-Means++ | 专名与大小写、加号保留，非API不强制汉化 |
| inertia | 惯性（inertia） | K-Means的簇内距离平方和，不是优化器动量或力学质量 |
| elbow method / silhouette score | 肘部法 / 轮廓系数 | silhouette对单点为系数、整体为均值，a/b是距离不是相似度；源措辞另列 |
| DBSCAN / eps / min_samples | DBSCAN / eps / min_samples | 算法名与参数不译；半径端点及是否包含自身依原实现 |
| core / border / noise point | 核心点 / 边界点 / 噪声点 | 不与网络边界或神经元激活混同 |
| hierarchical / agglomerative clustering | 层次聚类 / 凝聚聚类 | 凝聚式从下到上，区别分裂式 |
| dendrogram | 树状图（dendrogram） | 合并层级，不是分类决策树 |
| single / complete / average linkage | 单链接 / 全链接 / 平均链接 | 两簇跨簇点对的最小/最大/平均距离 |
| Ward linkage | Ward 链接 / Ward 方法 | 增加最少的簇内平方和，源variance措辞保留、条件单列 |
| Gaussian mixture model / GMM | 高斯混合模型 / GMM | 单个高斯分量与整体混合分布区别；本实现球形方差不能冒称全协方差 |
| hard / soft assignment | 硬分配 / 软分配 | 簇归属及概率分布，不是内存分配 |
| Expectation-Maximization / EM | 期望最大化 / EM | E步计算归属概率，M步参数更新；不是保证全局最优 |
| mixing weight / responsibility | 混合权重 / 责任度 | 先验分量权重与点的后验归属概率不同，代码标识符原样 |
| anomaly / outlier | 异常 / 离群点 | 沿S22/S28；低密度不自动等同业务异常，源概括单列 |
