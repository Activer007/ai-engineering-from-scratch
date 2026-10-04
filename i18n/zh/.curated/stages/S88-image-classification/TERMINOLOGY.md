# S88-image-classification 术语增量 v1.0

日期：2026-10-04 UTC。作者新提案已与完整固定参考术语集合校准；本文件保存冻结时的预发布支持快照，精确字节冻结由协调者确认回执证明。publication字段的null记录冻结时的历史状态，不自引用本文件的Git提交；实际发布commit由后续作者record和远端回读receipt绑定。它不是译文审校或正式接受。

固定英文：`1bafaa88bb4668356791150bec3a6d7df38387eb`。规范 docs H1：Image Classification。

正式基线保持105课；参考集合为85份正式TERM（83 accepted stage＋core2）及1份 active-reviewed S85 TERM，共86份。S85的固定TERM提交为 `1a364d8283c864eccac467bb32a850a0d0779eef`，已独立语言审/GFM，但不将其标为正式106或中文先修门禁。来源逐项见 DEPENDENCIES.json。

| English | Proposed Chinese | Meaning and preservation |
|---|---|---|
| image classification / classifier | 图像分类 / 分类器 | Class prediction for whole images, distinguish region/pixel tasks |
| pipeline | 管线（pipeline） | S77 visual-processing terminology |
| pixel / RGB | 像素 / RGB（红绿蓝） | S77; dimensions unchanged |
| dataset / synthetic dataset | 数据集 / 合成数据集 | Keep CIFAR-10/CIFAR-100 names |
| dataloader / DataLoader | 数据加载器 / DataLoader（数据加载器） | API class name intact |
| augmentation / random transform | 数据增强 / 随机变换 | Input changes preserving the label in source description |
| normalization / standardize | 标准化 | Mean/std operation, following S77; distinct from BN |
| batch normalization / batchnorm | 批量归一化（BN） | S85 frozen terminology snapshot |
| mixup / Mixup | mixup（混合样本及标签）/ Mixup | Algorithm name retained; both images and labels interpolated |
| cutmix / Cutmix | cutmix / Cutmix | Algorithm name retained; rectangle-pasting payload is protected |
| cutout / Cutout | cutout（随机遮挡）/ Cutout | Algorithm name retained; exercise zeroes 8x8 square |
| label smoothing | 标签平滑（label smoothing） | Never silently reconcile the source's distinct epsilon formulas |
| one-hot | one-hot（独热） | Target representation, not temperature |
| soft label / soft target | 软标签 / 软目标 | Probability-distribution targets |
| logit / logits | logits（未经归一化的分数） | Retain logits, avoid assuming binary log-odds interpretation |
| cross-entropy | 交叉熵（cross-entropy） | Loss on logits, not softmax outputs |
| NLL | 负对数似然（NLL） | Name retained; source fusion explanation preserved |
| log-sum-exp | log-sum-exp | Mathematical technique; formula unchanged and numerical issue separately recorded |
| inductive bias | 归纳偏置（inductive bias） | Translation-related architectural bias from shared weights |
| weight sharing | 权重共享 | S83 parameter-sharing meaning; not weight tying across arbitrary layers |
| invariance | 不变性 | Do not change to S83 translation equivariance |
| color jitter / occlusion | 颜色扰动 / 遮挡 | Source natural-language transformations |
| reflect padding / zero padding | 反射填充（reflect padding）/ 零填充 | S83; identifiers remain reflect/zeros |
| calibration / ECE | 校准（calibration）/ ECE（期望校准误差） | Confidence-frequency agreement; does not imply fixture has measured ECE |
| temperature scaling | 温度缩放（temperature scaling） | Scalar calibration technique |
| accuracy / precision / recall | 准确率 / 精确率（precision）/ 召回率（recall） | Keep concepts separate |
| per-class accuracy / aggregate accuracy | 各类别准确率 / 总体准确率 | Do not equate aggregate with class-balanced metric |
| confusion matrix | 混淆矩阵（confusion matrix） | Rows true, columns predicted; formula axes unchanged |
| Top-1 / Top-5 / Top-k accuracy | Top-1 / Top-5 / Top-k 准确率 | Numeric ranks preserved |
| optimizer / scheduler | 优化器 / 学习率调度器 | Scheduler is advanced once per epoch in source |
| epoch / batch | 轮（epoch）/ 批次 | S85 epoch; never infer test run permission from exercise |
| forward pass / backward | 前向传播 / 反向传播 | Gradient calculation separate from optimizer step |
| dropout | Dropout（随机失活） | S85; APIs unchanged |
| computation graph | 计算图 | .item() breaks metric retention of autograd graph |
| Argmax | Argmax（最大值对应的索引） | Source capitalization kept |
| ablation | 消融实验（ablation） | Exercise comparisons; no actual execution implied |
| weight decay | 权重衰减 | Hyperparameter values preserved |
| invariant | 不变条件 | Required training-loop properties, distinct from image invariance |
| prompt / skill | 提示词（prompt）/ 技能 | Linked outputs remain original protected bytes |

## 词义和结构边界

核心/补充词表优先；首现按既定中英对应，专名/API/代码标识符保留。九种通用章节标题沿ADDENDUM。保护数字、单位、形状、轴次序、公式、代码、图载荷、链接、路径和源文件间差异。自然语言数量须等值并逐块对照，不改变数字字面量。

参考术语仅用于一致性；没有读取历史中文课文、translation segments、format_revisions或旧作者缓存。来源词表不等于可复用中文正文，source阅读/术语定义不计新增完成课。

logits首现统一“logits（未经归一化的分数）”；one-hot统一“one-hot（独热）”；NLL首现统一“负对数似然（NLL）”。mean/std变换译标准化、BN译批量归一化；分类precision/recall/accuracy为精确率/召回率/准确率。invariant为不变条件，invariance为不变性，不合并。
