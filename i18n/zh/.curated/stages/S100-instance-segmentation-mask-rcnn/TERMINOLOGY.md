# S100-instance-segmentation-mask-rcnn 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Instance Segmentation — Mask R-CNN。

本地 check-only own3 候选，未安装或发布。复用作者 95 TERM 固定校准及当前独立语言审核，定向核对相关词义，不声称本轮重读全部历史词表。以下作者提案数据行逐字保留；不要求改动当前正文或旧术语表。原 common103 = 95 TERM + 8 controls；own3 另计，未来总支持106，不把后来新增 common106 套入作者首次输入。

| English | 本课呈现 | 语义边界 |
|---|---|---|
| instance / semantic / panoptic segmentation | 实例分割 / 语义分割 / 全景分割 | 与先修英文及 S97 本地候选一致；区分每目标、每类别和综合任务 |
| mask / binary mask | 掩码 / 二值掩码 | 目标区域掩码，不套注意力 mask 或 Dropout 掩码定义 |
| backbone / frozen backbone | 主干网络 / 冻结的主干网络 | 沿 ADDENDUM、S85、S91；冻结参数不自动等于冻结运行统计状态 |
| feature map / stride | 特征图 / 步幅 | 沿 S83、S85；空间下采样间隔，非张量内存布局步幅 |
| FPN / Feature Pyramid Network | 特征金字塔网络（FPN） | 自顶向下和横向连接；保留缩写、层级和 C 通道 |
| RPN / Region Proposal Network | 区域提议网络（RPN） | 生成候选框的网络；不套概率分布的提议分布 |
| proposal / proposal box | 候选区域 / 候选框 | 视对象选择；proposal 的几何表示为框 |
| bounding box / box head | 边界框 / 边界框头 | 沿 S94；定位回归与类别预测两个职责均保留 |
| mask head / heads | 掩码头 / 预测头 | 模块名称；head 不是句法中心词 |
| FCN | 全卷积网络（FCN） | 掩码头中的小型卷积网络，不译全连接网络 |
| RoIAlign / RoIPool | 保留原名 | 正文解释双线性采样/整数舍入；不改图载荷 |
| bilinear sampling / interpolation | 双线性采样 / 插值 | 空间坐标语境，不套语言模型平滑或概率抽样 |
| quantisation / rounding | 量化 / 舍入 | 此处是坐标量化，不扩为模型权重量化 |
| anchor / anchor box | 锚框（anchor）/ 锚框 | 沿 S94，不套 S40 锚样本或 S74 文本锚定 |
| objectness / objectness score | 目标存在性 / 目标存在性分数 | 沿 S94；不是类别置信度或最终乘积得分 |
| regression offset / box regression | 回归偏移量 / 边界框回归 | 连续几何调整，不改变符号或坐标 |
| NMS / IoU | 非极大值抑制（NMS）/ 交并比（IoU） | 沿 S94；阈值 0.7 与代码比较符号保留 |
| deconv | 转置卷积（deconv） | 根据 S97 本地候选及先修 04-07 英文的别称说明；保留英文别称，不误指数学逆卷积 |
| upsample | 上采样 | 空间分辨率扩大，沿 S97 本地候选 |
| cross-entropy / binary cross-entropy | 交叉熵 / 二元交叉熵 | 沿 S12/S28/S40/S88；逐像素二分类与类别分类区分 |
| smooth L1 | 平滑 L1 | 沿 S40；不擅自等同所有 Huber 实现 |
| background class | 背景类 | 类别 0；不是 shell 后台、不是所有场景背景区域的完整语义 |
| AP / mAP | 平均精确率 / 平均精确率均值 | 沿 S39/S94；AP 精确率不是准确率、浮点精度或 Bayes MAP |
| boundary precision | 边界精度 | 定位几何质量，不译边界精确率 |
| bottleneck | 瓶颈 | 此处为限制性能的预测头，不是 U-Net 瓶颈层或 ResNet Bottleneck 类 |
| fine-tuning / epoch | 微调 / 轮（epoch） | 沿 core/S43/S85/S88；不暗示已运行训练 |
| prompt / skill | 提示词（prompt）/ 技能 | 沿 core/S88；输出产物路径保护 |

## 沿用和消歧

沿用 S94 边界框、目标存在性、交并比和非极大值抑制；目标掩码区别注意力 mask。RoIAlign 的双线性采样保留浮点坐标，quantisation 在此是坐标量化，不能套用模型权重量化；RoIPool 的整数舍入、空间采样和插值各有边界。deconv 译转置卷积，保留别称，不解释为数学逆卷积；性能 bottleneck 不套 U-Net 瓶颈层或 ResNet 瓶颈块。

S97 补充参照单列：作者在 2026-10-04T12:41:49Z 读取当时的本地候选，commit 为 null；后来同字节术语文件发布于 `bfc72c4478e6f5281dd698097cbc5f1a90937179`，路径 `i18n/zh/.curated/stages/S97-semantic-segmentation-unet/TERMINOLOGY.md`，SHA256 `5eda3951e1e0f874862691337a9f8575be0d4e509d8bf0537a14d0a9ca6b8b57`。这只是额外术语参照，不追写为作者首次输入、不插入原 common103/95、不增加本课 own3。

源文“四项损失”与公式五项的冲突保留：公式包含 L_rpn_cls、L_rpn_box、L_box_cls、L_box_reg、L_mask。词表不负责把源文改成五项，也不删公式项；详细源限制另列 SCOPE。

## 保护规则

核心及补充表优先，通用章节沿既有规范，英文没有的章节不补造。API、模型、专名、标识符、路径、URL、公式、数值、代码与图载荷保持；首次正文按本课语境中英对应，不把同词跨任务机械统一。源内矛盾、宽泛或版本性断言单列，不静默修正英文含义、数学或代码。

词表用于一致性，不复用旧中文课文/segments；规范自带质量示例仅附带曝光且未复用。起草只依赖固定英文与术语，不等待先修中文正式验收。支持候选、语言 PASS、课程运行、GFM与正式计数分别记录。
