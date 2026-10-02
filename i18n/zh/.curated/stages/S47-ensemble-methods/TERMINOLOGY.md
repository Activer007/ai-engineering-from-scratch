# S47 集成方法术语增量

联用核心与截至S46的56项固定支持文件。bias为统计偏差，沿S42；不与网络偏置或社会偏见混同。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| ensemble / base learner / weak learner | 集成 / 基学习器 / 弱学习器 | 学习器组合语境；不暗补弱学习定理条件 |
| Bagging / Boosting / Stacking | Bagging（自助聚合）/ Boosting（提升法）/ Stacking（堆叠集成） | 沿S42，算法名保留；元学习这里指模型组合，不等同所有meta-learning任务 |
| bootstrap sample / out-of-bag | bootstrap样本（自助抽样样本）/ 袋外 | 沿S23/S42；有放回，袋外集合随各次抽样变化 |
| decision stump | 决策树桩 | 仅一次分裂的基学习器；源深度1数字保持 |
| AdaBoost | AdaBoost（自适应提升，Adaptive Boosting） | 算法和API保留；源标记正负1及alpha公式保护 |
| gradient boosting / pseudo-residual | 梯度提升 / 伪残差 | 负梯度语境，平方损失系数约定另列风险 |
| shrinkage | 收缩系数 | 本课learning_rate控制每棵树贡献，区别直接收缩模型权重 |
| weighted quantile sketch | 加权分位数摘要 | 近似分位数数据结构，不是密码学内容摘要；首现保留英文 |
| sparsity-aware split / column subsampling | 稀疏感知分裂 / 列子采样 | 缺失值分裂方向与特征随机化；不改API |
| cache line | 缓存行 | CPU内存层次语境，不是文件中的一行 |
| meta-feature / meta-learner | 元特征 / 元学习器 | 基模型预测构成的特征；训练集内生成与折外生成区别 |
| hard / soft voting | 硬投票 / 软投票 | 类别多数与概率均值，不混成同一操作 |
| diversity / decorrelation | 多样性 / 去相关 | 模型误差多样性；源独立与不相关条件不能互换 |

XGBoost、LightGBM、AdaBoost、SVM、TabNet、NODE、sklearn/scikit-learn、Kaggle、全部类/字段/函数/路径/链接按源保留。百分比不换为百分点；21/101模型的74%/84%源数值即使有限算术不符仍保留，另列来源风险。一般single/three等中文数量逐块映射。
