# S36 朴素 Bayes 术语增量 v1.0

2026-10-02。主协调确认。联用核心、增补、S10 Bayes 基础及截至 S33 的固定词表；43 项依赖只读。TF-IDF 与同期 S34 统一。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| Naive Bayes / NB | 朴素 Bayes（Naive Bayes）/ NB | 条件于类别的独立假设，不改成无条件独立 |
| Bayes' theorem | Bayes 定理（贝叶斯定理） | 沿 S10；条件方向与分母保持 |
| Multinomial / Gaussian / Bernoulli Naive Bayes | 多项式 / Gaussian（高斯）/ Bernoulli（伯努利）朴素 Bayes | 专名保留；类名 MultinomialNB、GaussianNB、BernoulliNB 原样；多项式分布不等同多项式特征 |
| conditional independence | 条件独立 | 给定类别后独立；相关特征导致排序不变的概括只列源风险 |
| prior / likelihood / posterior / evidence | 先验 / 似然 / 后验 / 证据 | 沿 S10；不互换，Gaussian PDF 为密度而非点概率 |
| Laplace / add-one smoothing | Laplace 平滑（拉普拉斯平滑）/ 加一平滑 | 一般 alpha 与加一特例区分；词项次数与文档数区分 |
| bag-of-words / word frequency / vocabulary | 词袋 / 词频 / 词表 | 代码词项和特征索引不译，不把词项计数混成文档频率 |
| TF-IDF | TF-IDF（词频-逆文档频率） | 首现中文和英文展开；非负权重与精确多项式计数模型区别只记源风险 |
| log score / log posterior probability | 对数分数 / 对数后验概率 | 未归一化分数不能等同对数后验；源等式与 API 名不暗修 |
| generative / discriminative model | 生成式 / 判别式模型 | P(X\|Y)、P(Y)、P(Y\|X) 各自角色不变 |
| calibration / ranking | 校准 / 排序 | 概率校准不等于分类准确率，排序正确并非独立性违背时的保证 |
| bias-variance / bias term | 偏差与方差 / 偏置项 | 统计偏差与模型相加的偏置严格区别 |
| precision / recall / F1 / accuracy | 精确率 / 召回率 / F1 分数 / 准确率 | 沿 S28；不混用数值精度 |
| presence / absence | 出现 / 缺席（或未出现） | Bernoulli 对缺席的建模与 Multinomial 零计数不同 |

所有概率条件方向、表格转义竖线、裸乘号、log、变量与模型参数保持原文。源有关 BernoulliNB 默认二值化、class_prior/priors、TF-IDF 负值、校准保证和速度/小样本优势的强断言单列，不借翻译订正。
