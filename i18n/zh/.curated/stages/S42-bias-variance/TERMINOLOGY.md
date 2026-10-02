# S42 术语增量：偏差—方差权衡

继承核心 v1.0、补充 v1.1 及51项固定支持文件，按语境使用，不改共享旧词表。

| EN | ZH / 呈现 | 语境和保留规则 |
|---|---|---|
| bias / variance | 偏差 / 方差 | 统计预测分解；不是神经网络加性偏置或社会偏见，沿S22 |
| irreducible noise / error | 不可约噪声 / 不可约误差 | 源的平方损失分解；不暗补或删除概率假设 |
| double descent | 双下降 | 首现中英；不是梯度的两次下降 |
| interpolation threshold | 插值阈值 | 模型能够拟合训练点的容量区域；p~n原符号保持 |
| underparameterized / overparameterized | 欠参数化 / 过参数化 | 参数数与样本数；不混为欠拟合/过拟合 |
| implicit regularization / implicit bias | 隐式正则化 / 隐式偏好 | 后者在选择简单解语境，不与误差分解偏差混淆 |
| learning curve / validation curve | 学习曲线 / 验证曲线 | 本课分别扫训练集大小/模型复杂度；其他语境学习曲线不作全局限定义 |
| bootstrap sampling / sample | bootstrap 抽样（自助抽样）/ bootstrap 样本 | 沿S17/S23；源实际重新生成独立数据却称bootstrap的问题另列 |
| Bagging / Boosting / Stacking | Bagging（自助聚合）/ Boosting（提升法）/ Stacking（堆叠集成） | 保留算法专名，首现解释；不把方差变化表当无条件定理 |
| Dropout / early stopping | Dropout（随机失活）/ 早停 | 沿S22；保持英文专名，不是永久删除神经元 |
| Ridge / Lasso | Ridge（岭回归）/ Lasso | 专名与API不强译；L1/L2数值标识保持 |
| meta-learner / base model | 元学习器 / 基模型 | 集成模型语境 |
| sweet spot | 最佳平衡点 | 权衡语境，不固定为任意最优保证 |

Bias^2、bias^2、sigma^2、variance、E[f_hat(x)] 等源公式字面保持；代码围栏仅给原裸围栏补text。普通数量词等值映射写入课程记录，分钟可译；无新通用控制例外。
