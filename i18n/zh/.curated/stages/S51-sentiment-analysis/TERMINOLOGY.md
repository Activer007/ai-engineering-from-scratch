# S51 情感分析术语增量 v1.0

2026-10-02。联用固定核心、补充及截至 S46 的 56 项控制/术语依赖；朴素 Bayes 沿 S36，文本与词袋沿 S41/S44，分类指标沿 S28/S39。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| sentiment analysis / polarity | 情感分析（sentiment analysis）/ 情感极性（polarity） | 情感标签正向/负向与二分类指标正类/负类区分 |
| aspect-based sentiment | 方面级情感分析（aspect-based sentiment） | 将情感归属于文本中的具体实体或属性，不等同整篇情感 |
| negation scoping | 否定范围标记（negation scoping） | 本课指在否定词之后、下一个标点之前给 token 加 `NOT_` 前缀；非完整语言学否定分析 |
| Naive Bayes / multinomial Naive Bayes | 朴素 Bayes（Naive Bayes）/ 多项式朴素 Bayes | 沿 S36；给定标签后的条件独立，词项计数和类别先验分开 |
| logistic regression / class-weighted | 逻辑回归（logistic regression）/ 按类别加权 | 沿 S28；负特征权重不等于负概率，类别权重不等于 F1 汇总权重 |
| BoW / TF-IDF / n-gram / bigram | 词袋（BoW）/ TF-IDF（词频-逆文档频率）/ 连续 n 元片段 / 二元片段 | 沿 S44；`not good`、`not_good` 和 `NOT_good` 字面形式保持 |
| token / tokenizer / stopword | token（词元）/ 分词器 / 停用词 | 沿 S41；标点与缩约形式按源分词正则分析 |
| Laplace / additive smoothing | Laplace 平滑（拉普拉斯平滑）/ 加性平滑 | alpha=1.0 为加一特例；源称谓与一般 alpha 边界分别记录 |
| accuracy / precision / recall | 准确率 / 精确率 / 召回率 | 沿 S28/S39；precision 不是准确率或数值精度 |
| macro-F1 / micro-F1 / weighted-F1 | 宏平均 F1 / 微平均 F1 / 加权 F1 | 首现保留英文；宏平均对各类 F1 等权，微平均聚合计数，加权按类别频率 |
| AUROC / AUPRC | ROC 曲线下面积（AUROC）/ 精确率-召回率曲线下面积（AUPRC） | 首现中文释义，不能未经说明与 average precision 等同 |
| confusion matrix / per-class error samples | 混淆矩阵 / 各类别的错误样本 | TP/FP/FN/TN、数字标签和 `+`/`-` 标签依源保持 |
| L2 regularization / sublinear TF | L2 正则化 / 次线性 TF | 正则化与 L2 归一化不同；源梯度与术语表公式系数差异不暗修 |
| sarcasm / zero-shot / domain drift | 讽刺 / 零样本 / 领域漂移 | 不把讽刺检测、跨语言或领域泛化表述为已验证能力 |

保留 scikit-learn、NumPy、IMDb、SST-2、Yelp、BERT、FastText、SVM、模型名、API/标志/路径/URL，以及参考资料的英文题名。自然语言 two/three/six/tens of thousands 等数量采用中文等值表达并逐块记录；代码、提示词与字符串均原样。
