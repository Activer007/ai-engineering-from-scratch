# S97-semantic-segmentation-unet 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Semantic Segmentation — U-Net。

本地 check-only 候选，未安装或发布。复用作者固定95 TERM校准，定向复核相关条目与英文；不声称重新全文审查全部旧历史。以下保留作者提案，不要求强制改词，不改既有术语。103 common = 95 TERM + 8 controls；本课own3独立另计，总支持106。S98原样SVG是额外非支持资产。词表数不是正式课程数。

| English | 建议中文 | 首现与边界 |
|---|---|---|
| semantic / instance / panoptic segmentation | 语义分割 / 实例分割 / 全景分割 | 学习目标首次中英对应；分别每像素类别、前景对象实例、所有像素类别及实例 ID |
| things / stuff | 可数对象（things）/ 背景区域（stuff） | 三分任务说明；stuff 不直接等同于合成数据的背景 0 类 |
| upsample / upsampling | 上采样 | 空间分辨率扩大，区别音频重采样或概率抽样 |
| contracting encoder / expanding decoder | 降采样编码器 / 上采样解码器 | 下行缩小空间尺寸，上行扩大；沿 S85 降采样 |
| bottleneck (U-Net) | 瓶颈层 | 最低空间分辨率特征层；区别 S85 ResNet Bottleneck 瓶颈块 |
| transposed convolution | 转置卷积（transposed convolution） | 首次学习目标；不称真正逆卷积，deconvolution 仅保留术语表的口头别称 |
| bilinear upsampling | 双线性上采样（bilinear upsampling） | 上采样策略首现；插值后接卷积，不是可学习转置卷积 |
| checkerboard artifacts | 棋盘格伪影（checkerboard artifacts） | 输出空间周期伪影；artifact 不在此译为产物 |
| Dice loss / Dice | Dice 损失 / Dice | 模型重叠损失及评估名；不强行音译 |
| macro Dice | 宏平均 Dice（macro Dice） | 逐类别 Dice 再平均，区别微平均与按类频率加权 |
| per-class IoU / mIoU | 各类别的 IoU / 平均交并比 mIoU | 沿 S16/S94 交并比；平均值不能替代逐类结果 |
| boundary F1 | 边界 F1 | 在评估说明中定义，无重复 F1 双语括注，避免新增受保护数字 |
| ground-truth mask / probability map | 真实掩码 / 概率图 | 沿 S40 ground truth；概率与 logits 原始分数分开 |
| pixel accuracy / boundary accuracy | 像素准确率 / 边界准确性 | 前者比例指标，后者边界定位质量；不误用精确率 |
| dilated convolution | 空洞卷积（dilated convolution） | 分辨率权衡段首次；扩大感受野，保留源对 DeepLab 的概括 |

## 沿用和消歧

沿用 S85/S83/S30 降采样、S85 跳跃连接、S40 真实值及 S94 交并比。U-Net bottleneck 为瓶颈层，区别 ResNet Bottleneck（瓶颈块）和图论/性能瓶颈；checkerboard artifacts 为棋盘格伪影，不套产物。things/stuff 区分可数对象与背景区域，不等同背景0类；macro Dice 为逐类后平均，不是加权平均。

## 保护规则

核心及补充表优先，首次正文遵守中英对应；API、模型ID、标识符、路径、链接、数值、公式、代码与图载荷保持。通用章节沿补充表，英文没有的章节不补造。自然语言数量等值且不跨源块移动。源问题另列，不静默改数学、代码或技术含义。

词表仅用于一致性，不复用旧中文课文/segments；规范中文质量示例仅附带曝光，未引用其措辞。新译只依赖固定英文与术语，不等待先修中文正式验收。publication pending/null仅表示本次冻结未绑定发布提交；后续真实提交由外部记录和独立回读绑定，不自引用。
