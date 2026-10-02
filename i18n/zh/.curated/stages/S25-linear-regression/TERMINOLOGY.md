# S25 线性回归术语增量 v1.0

2026-10-02。联用核心及S05–S24固定词表；34依赖均只读支持/术语，不复用既有中文课正文。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| linear / multiple linear regression | 线性回归 / 多元线性回归 | multiple是多个输入特征，不是多个目标的multivariate概念 |
| weight / slope | 权重 / 斜率 | 单输入w可解释为斜率，多元权重语境保留 |
| bias / intercept | 偏置 / 截距 | 加性b项，不是S22泛化误差的偏差 |
| cost function / loss function | 代价函数 / 损失函数 | 按源各自用词，代价可含正则项；不擅自更改损失归一化 |
| mean squared error (MSE) | 均方误差（MSE） | n分母与平方保持，不能替换为RMSE；公式原样 |
| gradient descent / learning rate | 梯度下降 / 学习率 | 参数更新方向、2/n因子与符号保护 |
| normal equation / closed-form | 正规方程 / 闭式解 | 沿用S19，不译成正态方程；满秩/可逆前提缺口单列 |
| hyperplane | 超平面 | 多特征的仿射预测面，源以linear概括不暗改 |
| standardization / feature scaling | 标准化 / 特征缩放 | 减均值除标准差，不等于任意区间归一化；常量列行为看实现 |
| polynomial regression / degree | 多项式回归 / 次数 | 关于特征非线性、关于权重线性；degree不是矩阵秩或角度 |
| R-squared / R^2 | R平方（R-squared）/ R^2 | 决定系数语境；常量y未定义及训练/测试均值参照另列 |
| residual / sum of squared residuals | 残差 / 残差平方和 | SS_res/SS_tot标识符原样，残差方向依源代码 |
| Ridge / Lasso / ElasticNet | Ridge回归（岭回归）/ Lasso回归 / ElasticNet | 专名保留；L1/L2的alpha/lambda数值约定不能跨实现混用 |
| batch / stochastic / mini-batch gradient descent | 批量 / 随机 / 小批量梯度下降 | SGD保留缩写，batch不是阶段批次；并非必定哪种最快 |
| epoch / training run | 训练轮次 / 一次训练运行 | 沿S22对run与epoch的区分，不把两个概念互换 |
| shrinkage / sparse solution | 收缩 / 稀疏解 | 权重范数缩小与逐个分量变小不同；零系数主张按源保留另列 |
| skill / regression baseline | 技能（skill）/ 回归基线 | outputs中的技能产物路径原样；不等于模型能力认证 |
