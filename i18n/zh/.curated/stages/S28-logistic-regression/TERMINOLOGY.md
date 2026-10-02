# S28 逻辑回归术语增量 v1.0

2026-10-02。联用核心、补充与S05–S27固定词表；37依赖只读支持/术语。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| logistic regression | 逻辑回归（logistic regression） | 概率分类模型；不是对类别编号做普通线性回归 |
| sigmoid / softmax | sigmoid / softmax | 函数名保留，不强行改写API；开区间数学式与有限精度实现边界分列 |
| logit / score / probability | logit / 分数 / 概率 | sigmoid/softmax前后角色分开，不默认概率已校准 |
| binary / categorical cross-entropy | 二元交叉熵 / 类别交叉熵 | 二分类与多分类目标分开，沿用S12交叉熵语境，缩写BCE若出现保留 |
| log loss / negative log-likelihood | 对数损失 / 负对数似然 | 符号方向、平均因子与自然对数约定保留 |
| accuracy / precision | 准确率 / 精确率 | 分类precision不是数值计算精度，也不是准确率；沿用S17语境规则 |
| recall / sensitivity | 召回率 / 灵敏度 | sensitivity在筛查语境；不是模型对输入扰动的敏感度 |
| true/false positive, true/false negative | 真/假阳性、真/假阴性 | TP/FP/TN/FN标记及混淆矩阵行列绝不互换；非医疗语境可解释为命中/误报/漏报 |
| confusion matrix | 混淆矩阵 | 行为实际类别、列为预测类别依源表，不套用另一库布局 |
| F1 / harmonic mean | F1分数 / 调和平均值 | 与balanced accuracy平衡准确率不是同一个指标；源口语栏保留并单列 |
| threshold / threshold tuning | 阈值 / 阈值调优 | >=与>边界按代码/源文分别保留；test集调优风险另列 |
| one-hot encoding | one-hot（独热）编码 | 沿S12/S18；位置k和类别索引、整型标签分开 |
| one-vs-rest / multinomial | one-vs-rest（一对其余）/ multinomial（多项式） | 分类策略/库参数语境，不能与多项式特征混同 |
| ROC / AUC / TPR / FPR | ROC曲线 / 曲线下面积 / 真阳性率 / 假阳性率 | 分母不同，梯形积分和阈值次序要求只记录源缺项 |
| outlier / decision boundary | 离群点 / 决策边界 | sigmoid压缩不等于全模型对离群值鲁棒 |
| epoch / training run | 训练轮次 / 一次训练运行 | 沿S22/S25，不能把训练run理解成单个epoch |
