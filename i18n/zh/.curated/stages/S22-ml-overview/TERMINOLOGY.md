# S22 ML 概览术语增量 v1.0

2026-10-02。联用核心、补充及S05–S21固定词表；本表用于后续ML基础课程共享语境。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| supervised / unsupervised learning | 监督学习 / 无监督学习 | 是否使用输入对应标签，不等于所有无监督方法没有目标函数 |
| reinforcement learning / agent / policy | 强化学习 / 智能体 / 策略（policy） | 环境动作奖励语境；不是软件安全策略，RLHF缩写保留 |
| semi-supervised / self-supervised | 半监督 / 自监督 | 少量人工标签与数据自身构造监督信号分开 |
| label / label propagation / pseudo-labeling | 标签 / 标签传播 / 伪标签 | label此处监督目标，不是UI标签页或分类类名本身 |
| consistency regularization | 一致性正则化 | 扰动输入预测一致；不是数据库一致性保证 |
| masked language modeling / contrastive learning | 掩码语言建模 / 对比学习 | BERT、SimCLR保留专名；mask并非授权遮罩 |
| next-token prediction | 下一token预测 | token保英文；源words与token简化不静默改正文含义 |
| classification / regression / clustering | 分类 / 回归 / 聚类 | 预测离散类别、连续量与分组语境各自区分 |
| nearest centroid classifier / centroid | 最近质心分类器 / 质心 | 类内均值中心；不等同K近邻，NearestCentroid类名原样 |
| baseline / random baseline | 基线 / 随机基线 | 预测性能参照，不是源Git基线或网络基线 |
| feature / label / hyperparameter | 特征 / 标签 / 超参数 | 输入属性、监督目标与学习过程设置分开；API不翻译 |
| generalization / representation | 泛化 / 表示 | 新数据预测与学习所得表示；非通用智能保证 |
| overfitting / underfitting | 过拟合 / 欠拟合 | 训练与未见数据误差的学习语境；源复杂度绝对化另列 |
| bias / variance | 偏差 / 方差 | 泛化误差分解；bias此处不是网络加性偏置b或社会偏见 |
| irreducible noise | 不可约噪声 | 源误差分解条件另记；英文表达式逐字保留 |
| data leakage / class imbalance | 数据泄漏 / 类别不平衡 | 沿用S17泄漏语境；类别频率并非公平性结论 |
| training / validation / test set | 训练集 / 验证集 / 测试集 | 拟合、选型调参与最终评估区分；源混用另列 |
| cross-validation / fold | 交叉验证 / 折 | 轮换留出数据的划分单元，不是独立样本保证 |
| data drift | 数据漂移 | 新输入分布变化，不等于必定导致性能下降；源强断言另列 |
| Dropout / early stopping | Dropout / 早停 | 模型训练技巧；Dropout专名保留，零化不是永久删除神经元 |
| decision boundary / feature scaling | 决策边界 / 特征缩放 | 最近质心的欧氏距离与尺度相关；不预先添加源没有的缩放 |
| No Free Lunch theorem | 没有免费午餐定理 | 比较范围与假设单列，不改成特定数据分布绝无优势 |
| deterministic rules / heuristic | 确定性规则 / 启发式方法 | 确定性与正确性是不同性质；只忠实呈现源文 |
