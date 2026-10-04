# S91-transfer-learning 术语增量 v1.0

日期：2026-10-04 UTC。作者新提案已与完整固定89份参考词表校准。本文件是待协调者精确字节确认的本地预发布支持候选，不是译文审校或正式接受。冻结后保留该预发布快照；publication字段的null仅表示冻结时尚未绑定发布提交，不自引用本文件的Git提交，也不声称永久未发布。实际发布commit由后续作者record和远端回读receipt绑定。

固定英文：`1bafaa88bb4668356791150bec3a6d7df38387eb`。规范 docs H1：Transfer Learning & Fine-Tuning。

本轮核验正式基线为106课。参考集合为86份正式TERM（84 accepted stage＋core2）和3份active-reviewed TERM（S88/S89/S90），共89份；另有8份原controls，common共97。本课own3另计，总100。S85现属正式已接受，不沿用旧支持快照中的active状态；旧TERM原字节和历史105叙述保留，其历史文字不是本轮状态。S88/S89/S90与本轮新draft不提前计入正式106。完整固定来源见 DEPENDENCIES.json。

| English | Proposed Chinese | Meaning / first-use rule |
|---|---|---|
| feature extraction | 特征提取（feature extraction） | Frozen backbone with a trained new head, distinct from feature selection; first objective |
| domain distance | 领域差异（domain distance） | Difference between pretrained and target distributions, not measured physical distance; first objective |
| discriminative learning rates / discriminative LR | 差异化学习率（discriminative learning rates）/ 差异化学习率 | Per-stage different learning rates; not a discriminative model or numerical differentiation algorithm; first objective |
| feature drift | 特征漂移（feature drift） | Pretrained representations change undesirably under excessive updates; first objective |
| progressive unfreezing | 逐步解冻 | Unfreeze from late toward early stages, one per epoch; used descriptively in first objective and explicit Step 6 |
| layer-wise LR decay | 逐层学习率衰减（layer-wise LR decay） | Multiply base LR by decay^(L - k); distinct from a time-based LR scheduler |
| linear probe | 线性探测（linear probe） | Fit/evaluate a linear classifier above a frozen representation; source's zero-shot phrasing is preserved and flagged |
| GroupNorm | GroupNorm（组归一化） | Proper algorithm name retained; not a new PyTorch import or replacement in executable code |
| catastrophic collapse | 灾难性崩溃（catastrophic collapse） | Source's all-inputs-one-class failure, distinguished from catastrophic forgetting |
| full fine-tune | 全量微调 | Full-model tuning in the exercise, no training performed here |
| cached moments | 缓存矩估计 | Optimizer moments, not wall-clock moments or cache timestamps |
| linear head | 线性分类头 | Linear classifier distinct from the frozen representation |

## 沿用的术语

| English | 中文 | 语义边界 |
|---|---|---|
| transfer learning | 迁移学习（transfer learning） | 沿S85；不只等同冻结主干一种方式 |
| backbone / frozen backbone | 主干网络（backbone）/ 冻结的主干网络 | 沿ADDENDUM、S85；权重冻结不等于所有运行状态冻结 |
| classifier head / stem | 分类头（classifier head）/ 输入端特征提取层（stem） | 沿S85；stem不是NLP词干 |
| fine-tuning | 微调（fine-tuning） | 沿核心；区分新分类头训练与全模型更新 |
| catastrophic forgetting | 灾难性遗忘（catastrophic forgetting） | 沿ADDENDUM；不是灾难性消去或本课灾难性崩溃 |
| BatchNorm / BN | 批量归一化（BN） | 算法说明；代码/API中的BatchNorm拼写保持 |
| running statistics / moving average | 运行统计量 / 移动平均 | 沿S48/S63；不与模型参数混同 |
| Dropout | Dropout（随机失活） | 沿S48/S69/S85；API标识符不改 |
| learning rate / LR | 学习率（learning rate，LR） | 沿S58；LR缩写保持，与有效更新量分开 |
| epoch / parameter group | 轮（epoch）/ 参数组 | 沿S43/S69/S85；不同于单个更新步 |
| feature extractor | 特征提取器 | 沿S83；不是特征选择器 |
| logits / prompt / API | logits（未经归一化的分数）/ 提示词（prompt）/ API（应用程序编程接口） | 沿核心及S88；标识符原样 |

## 词义和结构边界

核心/补充词表优先；首现按既定中英对应，专名、API、代码标识符保留。通用章节标题沿ADDENDUM，但不得新增源没有的章节。保护数字、单位、形状、轴次序、公式、代码、图载荷、链接、路径和源文件间差异。自然语言数量须等值逐块对照。

参考术语仅供一致性校准，不能复用旧译文正文。支持准备未读取旧中文课文、旧record的segments或format_revisions、452/457材料；按需读取的docs/i18n.md规范含既有中文质量示例，这项暴露已如实记录，示例措辞未复用。source阅读、术语准备及作者draft不构成新增正式完成课。

差异化学习率（discriminative learning rates / discriminative LR）专指按层或阶段赋不同学习率；这里不沿S36/S55模型分类语境的“判别式”，也不引入有限差分。逐层学习率衰减是沿层深度的倍率，不与S58随训练时间变化的学习率调度混同。
领域差异（domain distance）描述预训练与目标任务分布的相近程度，不暗指本源计算了距离度量；与S55领域偏移及S51领域漂移区分。线性探测（linear probe）是在冻结表示上训练并评估线性分类器；不把源zero-shot措辞变成“完全不训练分类头”的新定义。
