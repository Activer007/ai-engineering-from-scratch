# S12 信息论术语增量 v1.0

2026-10-02。联用核心和 S05–S11 数学词表。自然对数与以 2 为底对数、真分布 P 与模型分布 Q、离散熵与微分熵不可混淆；源误差单列，不用译文暗修。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| information theory | 信息论 | Shannon 开创的理论，不是一般信息技术 |
| information content / surprise | 信息量 / 惊讶程度 | 单个事件 -log p；不当成整分布平均熵 |
| entropy | 熵（entropy） | 本课离散概率为主；未声明条件的连续类比单列 |
| cross-entropy | 交叉熵（cross-entropy） | H(P,Q) 的 P 为事件来源、Q 为编码/模型，不交换顺序 |
| KL divergence | KL 散度（Kullback–Leibler divergence） | D_KL(P ∥ Q) 非对称；不是满足全部公理的距离度量 |
| mutual information / MI | 互信息（mutual information，MI） | 总体统计依赖量，不把有限样本估计当成全知；单变量排序不保证覆盖交互 |
| conditional / joint entropy | 条件熵 / 联合熵 | H(Y∣X) 观察 X 后 Y 的剩余不确定性；竖线保护表格列 |
| marginal distribution | 边缘分布 | 由联合分布求和得出，不是某分布的尾部 |
| bits / nats / hartleys | 比特（bits）/ 奈特（nats）/ 哈特莱（hartleys） | 英文单位也保留，分别对应 log2/ln/log10；1 nat=1/ln(2) bits |
| log-likelihood / NLL | 对数似然 / 负对数似然（NLL） | 似然不是后验，求和与样本平均区别；硬标签 CE 等价需按源条件 |
| one-hot / hard target | one-hot（独热）/ 硬目标 | 类别索引与概率向量分开；术语不强行全汉化 |
| soft target / label smoothing | 软目标 / 标签平滑（label smoothing） | epsilon 均匀混合，真类0.925与其余0.025保持 |
| logits / softmax | logits / softmax | logits 是未归一化分数，不能当概率；类名 CrossEntropyLoss 原样 |
| calibration | 校准（calibration） | 概率可信程度与准确率/置信度不同；不无条件保证改善 |
| regularization | 正则化 | 与归一化（normalization）不同，uniform term不是预测自身熵的别名 |
| perplexity | 困惑度（perplexity） | 平均 token 交叉熵的指数，底与单位匹配；有效选择数非实际词表尺寸或严格上界 |
| token / vocabulary | token / 词表 | 模型分词单元不等于词/字符；跨词表与语料比较边界单列 |
| compression / encoding | 压缩 / 编码 | 无损平均码长与单次事件长度分开，Shannon 边界需要编码模型条件 |
| Pearson / Spearman correlation | Pearson / Spearman 相关系数 | 线性与单调关系不同；源泛称correlation按语境保留 |
| binning | 分箱（binning） | 有限样本互信息估计的离散化，不是数据训练批量 |
| support / zero probability | 支持集 / 零概率 | p>0而q=0时CE/KL可无穷；不要通过改代码掩盖输入边界 |

代码、公式/图载荷、数值、API、路径和链接原样；裸围栏仅补 text。GFM 表内竖线、公式乘号以及中文 strong 边界需实际渲染验证。源对连续条件熵、低 MI 必为噪声、标签平滑校准、CE 浪费比特与 KL、困惑度 benchmark、数值稳定性的断言均另列来源问题。
