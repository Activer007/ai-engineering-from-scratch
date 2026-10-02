# S39 模型评估术语增量 v1.0

联用核心、补充及S05–S36固定术语；46项依赖见DEPENDENCIES.json。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| model evaluation / metric / score | 模型评估 / 指标 / 分数 | 分数高低方向取决指标，不默认所有损失越高越好 |
| training / validation / test set | 训练集 / 验证集 / 测试集 | 拟合、选型调参、最终留出评估职责分开 |
| hold-out / test contamination | 留出 / 测试集污染 | 一次性使用原则依源，不能承诺绝对无偏或跨分布保证 |
| K-fold cross-validation / fold | K折交叉验证 / 折 | K变量保护，折不等于一次epoch |
| stratified split / stratified K-fold | 分层划分 / 分层K折 | 按类别比例分层，区别时间/分组隔离，源舍入与少数类代码边界单列 |
| precision / recall / sensitivity / accuracy | 精确率 / 召回率 / 灵敏度 / 准确率 | 沿S28，precision不是准确率、浮点精度，FP/FN分母不可换 |
| confusion matrix / TP TN FP FN | 混淆矩阵 / 保留缩写 | 行实际、列预测依源；程序返回tuple顺序按API保护 |
| AUC-ROC / ROC / TPR / FPR | ROC曲线下面积 / ROC / 真阳性率 / 假阳性率 | 阈值排序与起止点、同分约定另列；不能把源0.5–1范围暗改成0–1 |
| precision-recall curve / average precision | 精确率-召回率曲线 / 平均精确率 | PR/AUC/AP保留，插值/加权定义不同不自动等同 |
| MSE / RMSE / MAE / R-squared | 均方误差 / 均方根误差 / 平均绝对误差 / R平方 | 沿S25/S28，目标量纲、常量目标退化、均值baseline区别 |
| bias / variance / underfitting / overfitting | 偏差 / 方差 / 欠拟合 / 过拟合 | 偏差不是神经网络bias偏置，沿S22/S34 |
| learning / validation curve | 学习曲线 / 验证曲线 | 横轴训练样本量与超参数区别；指标方向依源 |
| nested cross-validation | 嵌套交叉验证 | 外层评估、内层调参，不把同一验证集反复查看当独立test |
| permutation test / null distribution / p-value | 置换检验 / 零假设分布 / p值 | 沿S17统计术语，标签打乱与模型差异检验目标区别 |
| paired t-statistic / degrees of freedom | 成对t统计量 / 自由度 | CV折并非独立样本，源分母与临界值条件只单列 |
| preprocessing / scaler / pipeline | 预处理 / 缩放器 / 流水线 | 沿S34，每折fit只用训练子集，代码反例忠实保留 |
