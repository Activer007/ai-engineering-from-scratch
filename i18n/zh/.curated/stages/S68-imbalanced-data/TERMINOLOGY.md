# S68 不平衡数据处理术语增量

2026-10-03。联用核心、补充和74项固定支持文件；不复用旧中文课文。通用标题沿补充表。源技术问题单列，不在译文中暗修。

| English | 中文或保留形式 | 语境与边界 |
|---|---|---|
| class imbalance / majority / minority class | 类别不平衡 / 多数类 / 少数类 | 样本数量分布，不作个人资格或公平性判定 |
| random oversampling / undersampling | 随机过采样 / 随机欠采样 | 重复少数类与删减多数类；不混同合成样本 |
| SMOTE | SMOTE（合成少数类过采样技术） | 保留算法缩写；少数类近邻之间插值 |
| precision / recall / accuracy | 精确率 / 召回率 / 准确率 | 沿S28/S39；分母及FP/FN方向严格区分 |
| F1 / F-beta / harmonic mean | F1分数 / F-beta分数 / 调和平均值 | 指标公式和beta原样，不改为算术平均 |
| AUPRC | AUPRC（精确率-召回率曲线下面积） | 不自动等同平均精确率；源随机基线说法另列 |
| Matthews Correlation Coefficient / MCC | Matthews相关系数 / MCC | 缩写保留；退化分母与取零惯例分开 |
| class weights / cost-sensitive learning | 类别权重 / 代价敏感学习 | 损失加权与真实误分类代价；权重不是类别概率 |
| threshold tuning / calibration | 阈值调优 / 校准 | 决策截断与概率校准不同；阈值迁移风险另列 |
| logistic regression / decision boundary | 逻辑回归 / 决策边界 | 沿S28；API和代码名原样 |
| pipeline / bootstrap / balanced bagging | 管线 / bootstrap（自助抽样）/ 平衡Bagging | 沿S57/S47；源练习对bootstrap的简化另列 |
| training / validation / test set | 训练集 / 验证集 / 测试集 | 拟合、调参与最终评估职责分开 |

NumPy、scikit-learn、imbalanced-learn、Platt、Borderline-SMOTE、API、所有代码注释/字符串、Mermaid/figure载荷和公式保持原样。数学英文变量在公式中保留。强调标记边界保持源空白，中文标点不破坏GFM强调。自然语言数词可对应中文，数字及单位不改。
