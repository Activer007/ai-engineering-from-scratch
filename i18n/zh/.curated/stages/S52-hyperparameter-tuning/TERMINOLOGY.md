# S52 超参数调优术语增量

继承61项固定依赖；下列语境统一，不改变API/公式/路径。九个通用章节名沿ADDENDUM，源已有强调分隔空格保留。

| English | 中文或保留形式 | 语境/边界 |
|---|---|---|
| hyperparameter tuning | 超参数调优 | 设置学习过程，不是学习权重参数 |
| grid/random search | 网格搜索/随机搜索 | 参数取样用抽取，不混语言生成采样 |
| Bayesian optimization | 贝叶斯优化 | 优化搜索框架，Bayes定理专名沿既有词表 |
| surrogate model | 代理模型（surrogate model） | 低成本目标近似，不是智能体agent |
| Gaussian process / GP | 高斯过程（GP） | 预测均值与不确定性，非Gaussian分布单点假设 |
| acquisition function | 采集函数（acquisition function） | 给候选点评分，不是数据采集管道 |
| Expected Improvement / EI | 期望改进（EI） | 最大化得分的代码语境，loss符号不可混 |
| Upper Confidence Bound / UCB | 置信上界（UCB） | 预测加不确定性倍数 |
| Probability of Improvement / PI | 改进概率（PI） | 超过当前最佳的概率 |
| exploration / exploitation | 探索/利用 | 沿S18优化取舍语境，不是攻击 |
| trial / evaluation / budget | 试验/评估/预算 | 一次配置评估，区别训练样本与epoch |
| pruning / median pruning | 剪枝/中位数剪枝 | 提前终止试验，不是树结构剪枝 |
| patience | 耐心窗口 | 连续无改进轮数 |
| learning rate scheduler | 学习率调度器 | 训练中改变学习率 |
| cosine annealing / warmup | 余弦退火/预热 | 不是概率退火抽样 |
| log-uniform distribution | 对数均匀分布 | log参数与线性尺度分开 |
| nested cross-validation | 嵌套交叉验证 | 外层评估/内层调优，不把严格无偏强断言暗修 |
| effective dimensionality | 有效维度 | 重要超参数维度，非向量的表示维度 |
| Hyperband / Optuna / MedianPruner | 保留英文 | 算法/库/API，不强译标识符 |
