# S23 决策树与随机森林术语增量 v1.0

2026-10-02。联用核心、补充与 S05–S22 固定词表。沿用熵、信息增益、偏差/方差、置换重要性、不纯度/基数及自助法语境，不作全局机械替换。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| decision tree / random forest | 决策树 / 随机森林 | 模型名称；DecisionTree/RandomForest 类名保留 |
| split / split criterion / threshold | 划分 / 划分准则 / 阈值 | 树节点划分，不混同训练测试集划分对象 |
| internal / leaf / root node | 内部节点 / 叶节点 / 根节点 | 子节点与子树分开；pure 不等于单样本 |
| Gini impurity / entropy | Gini 不纯度 / 熵 | Gini 专名保留，概率分布与计数不混同 |
| information gain / variance reduction | 信息增益 / 方差减少量 | 分类不纯度与回归目标方差的减少；公式权重保护 |
| pre-pruning / post-pruning | 预剪枝 / 后剪枝 | 生长过程提前停止与长成后移除子树 |
| cost-complexity / reduced error pruning | 代价复杂度剪枝 / 错误率降低剪枝 | 叶节点数惩罚与验证误差准则分开 |
| bootstrap sampling / sample | bootstrap 抽样（自助抽样）/ bootstrap 样本 | 从训练集有放回抽样；样本一词在此可指整个重采样数据集 |
| bagging / bootstrap aggregating | Bagging（自助聚合）| 多次自助抽样训练再聚合，不是任意无放回子集 |
| out-of-bag samples | 袋外样本 | 未进入该树 bootstrap 数据集的原始样本，不是所有树共用独立测试集 |
| feature randomization | 特征随机化 | 每次划分抽取候选特征子集，不改变特征值 |
| ensemble / weak learner | 集成 / 弱学习器 | 多模型聚合；不把任意完整深树必定称为弱学习器 |
| mean decrease in impurity / MDI | 平均不纯度减少量（MDI）| 重要性依节点样本权重及归一化；源概括另记 |
| permutation importance / cardinality | 置换重要性 / 基数 | 沿用补充表；随机打乱特征与不同取值数量 |
| majority voting / piecewise constant | 多数投票 / 分段常数 | 分类聚合与回归预测形式不同 |
| gradient boosted trees | 梯度提升树 | XGBoost/LightGBM/CatBoost/scikit-learn 专名保留 |

混合类别输入、随机森林不会过拟合、默认特征数、纯叶与单样本、特征重要性可靠性等英文条件不足不在译文暗补。原代码、数值、公式和 API 保留；GFM 如需修复仅最小可逆适配并重新绑定独立审校。
