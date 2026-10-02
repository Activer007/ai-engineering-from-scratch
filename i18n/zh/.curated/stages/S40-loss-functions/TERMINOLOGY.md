# S40 损失函数术语增量 v1.0

2026-10-02。联用核心及截至 S36 的固定词表，沿用 S12 的交叉熵、标签平滑与 one-hot，S11 损失曲面，S28 logits / 负对数似然，S35 激活值与梯度的区分。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| loss function / ground truth | 损失函数 / 真实值 | 按预测目标语境，不将训练损失等同评估指标 |
| mean squared error / MSE | 均方误差（MSE） | 平均因子与每样本梯度按源保护 |
| binary / categorical cross-entropy | 二元交叉熵（BCE）/ 类别交叉熵（categorical cross-entropy） | 二分类与多分类 one-hot 目标语境，CCE 保留 |
| one-hot / hard target / soft target | one-hot（独热）/ 硬目标 / 软目标 | 目标概率向量与类别索引分开 |
| label smoothing | 标签平滑（label smoothing） | alpha 混合及 0.91 / 0.9 源矛盾单列，不改数值 |
| contrastive loss / representation collapse | 对比损失（contrastive loss）/ 表示坍缩 | 成对表示学习；源坍缩零损失说法不暗修 |
| positive pair / negative pair | 正样本对 / 负样本对 | 相似配对关系，不默认类别标签 |
| triplet loss / anchor | 三元组损失（triplet loss）/ 锚样本（anchor） | 锚、正、负三种角色与距离间隔 |
| hard negative / semi-hard negative mining | 困难负样本 / 半困难负样本挖掘 | 距离边界按英文，半困难的缺省条件单列 |
| focal loss | 焦点损失（focal loss） | 降低容易样本权重；gamma 和 alpha 的不同作用保护 |
| temperature / margin | 温度 / 间隔 | 分布尖锐程度与距离约束，tau 不等于优化器学习率 |
| loss landscape | 损失曲面 | 预测空间与参数空间的凸性区别不暗补进正文 |
| logit / softmax / negative log-likelihood | logit（未归一化分数）/ softmax / 负对数似然 | 沿 S28 与核心补充；概率与 log 概率不同 |
| knowledge distillation / teacher model | 知识蒸馏（knowledge distillation）/ 教师模型 | 固定教师软目标的 KL / 交叉熵关系 |
| Huber / smooth L1 / MAE | Huber / 平滑 L1 / 平均绝对误差（MAE） | 名称、缩放与阈值按源，不自动等同实现 |

InfoNCE、NT-Xent、SimCLR、CLIP、GPT、RetinaNet、PyTorch、sigmoid、softmax 与全部 API/路径/参考标题原样。首次用中文解释本课语境；数字与公式严格保留。自然量级词可按协调批准记录等值中文映射，不放宽原控制。
