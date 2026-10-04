# S85-cnns-lenet-to-resnet 术语增量 v1.0

日期：2026-10-04 UTC。此为源作者提案校准后冻结的起草支持快照；不代表译文完成、独立审校或正式接受。

固定英文：`1bafaa88bb4668356791150bec3a6d7df38387eb`。规范标题：CNNs — LeNet to ResNet。

正式术语基线：actual103，83份TERM（81 accepted stage＋core2），各路径和固定来源见同目录 DEPENDENCIES.json。旧 pending S61/S66/S79 未纳入。作者完整英文阅读后提出以下词义；没有复用旧中文课文、segments或format_revisions。

## Inherited terms

| English source | Calibrated Chinese | Basis and technical fidelity |
|---|---|---|
| convolutional neural network / CNN | 卷积神经网络（CNN） | S69/S77/S83; preserve abbreviation and family names |
| convolution / conv | 卷积（convolution）/ 卷积 | S83; prose only, protected code/diagram labels unchanged |
| kernel / filter | 卷积核（kernel）/ 滤波器（filter） | S83 distinguishes wording even when both refer to weight tensors |
| nonlinearity | 非线性 | S83; additional ReLU supplies additional nonlinearity |
| downsample / downsampling | 降采样 | S83/S30; replaces the author's earlier 下采样 candidate |
| pooling / max pool | 池化 / 最大池化 | S83; distinct from strided-convolution implementation |
| backbone / frozen backbone | 主干网络（backbone）/ 冻结的主干网络 | ADDENDUM frozen-backbone row; replaces 骨干网络 candidate |
| feature map | 特征图 | S83; distinguish channels from spatial shape |
| channel / channel axis | 通道（channel）/ 通道轴 | S77/S83; no axis reordering |
| stride | 步幅（stride） | S83; convolution sliding interval, not memory-layout stride |
| receptive field | 感受野（receptive field） | S83; not current feature-map shape |
| residual connection | 残差连接 | S83, inherited from S38 |
| batch normalisation / batch norm / BN | 批量归一化（BN） | S69; replaces 批归一化 candidate |
| dropout | Dropout（随机失活） | S69; retain algorithm/API name |
| fully connected / dense layer | 全连接层（dense / fully connected layer） | S83; count mismatch reported separately, not harmonized |
| flatten | 展平 | S83; API remains unchanged |
| weight / bias / parameter count | 权重 / 偏置 / 参数数量 | S83; count may be shortened only if no terminology drift |
| fine-tuning | 微调（fine-tuning） | Core; no tuning performed in this task |
| tensor / shape | 张量（tensor）/ 形状（shape） | S69/S77; shapes and tuple syntax preserved |
| forward / backward | 前向传播 / 反向传播 | S69; gradient computation not optimizer update |
| epoch | 轮（epoch） | S69; exercises are not runtime authorization |
| prompt | 提示词（prompt） | Core; output prompts are protected task content |
| reusable artifact | 可复用成果 | Core; files or tools produced by the lesson |

## 本课增量术语

| English source | Chinese treatment | Fidelity note |
|---|---|---|
| classifier head / task head | 分类头（classifier head）/ 任务头 | Head is separate from main feature-extraction stack |
| feature width | 特征通道数 | Architecture width here is channel count, not image width |
| skip connection | 跳跃连接（skip connection） | Synonym used alongside residual connection, distinct from residual branch |
| identity mapping | 恒等映射（identity mapping） | Actual post-activation block is not identity for all negative inputs |
| identity shortcut / identity skip | 恒等捷径连接 / 恒等跳跃连接 | Preserve whether text refers to the shortcut branch or generic skip |
| shortcut branch / path | 捷径分支 / 捷径路径 | Can be identity or learned shape-matching projection |
| residual block | 残差块（residual block） | Core block→块; residual architecture context |
| BasicBlock | BasicBlock（基本残差块） | Class identifier never changes |
| Bottleneck | Bottleneck（瓶颈块） | 1x1 down/up reduces/expands channels, not spatial resolution here |
| bottleneck (generic) | 瓶颈结构 | Inception 1x1 branch compression; not automatically named ResNet block |
| degradation problem | 退化问题（degradation problem） | Training error also worsens; source explicitly distinguishes overfitting |
| vanishing gradients | 梯度消失 | Source's explanatory simplification remains a source claim |
| optimiser | 优化器 | Normal Chinese translation of British spelling |
| stem | 输入端特征提取层（stem） | Initial convolution stage; avoid translating as image stem or tree trunk |
| average pooling / adaptive average pooling | 平均池化 / 自适应平均池化 | Distinguish original fixed 2x2 pooling from adaptive output size |
| global average pooling | 全局平均池化 | Separate from max pooling |
| transfer learning | 迁移学习（transfer learning） | Source teaches frozen backbone and new head; does not exhaust all transfer methods |
| pre-activation / post-activation | 预激活 / 后激活 | Interpret code/output artifact without silently changing block variant |
| shape alignment / shape matching | 形状对齐 / 形状匹配 | Addition requires matched channels and spatial dimensions |
| parameter budget / parameter efficiency | 参数预算 / 参数效率 | Exact M/k scales preserved; no equal-or-better accuracy inference from source's unequal values |
| inference | 推理 | Clearly distinguish from training |
| channel mixing | 通道混合 | 1x1 convolution mixes channels rather than merging spatial locations |
| concatenate | 拼接 | Inception concatenates along channels; residual branch adds elementwise |
| grouped convolution | 分组卷积 | Distinct from a group of residual blocks and from depthwise convolution |

## First-use and structure rules

- Nine common headings follow ADDENDUM: 学习目标、要解决的问题、核心概念、动手实现、实际使用、交付成果、练习、关键术语、延伸阅读
- Metadata keys Type/Languages/Prerequisites/Time, Type values Learn + Build, language Python and all model/API names remain unchanged; natural-language prerequisite labels and `~75 minutes` may become corresponding Chinese / `~75 分钟`
- Retain source numerical symbols, M/k quantities, mathematical expressions, paths, URLs, fenced payloads, Mermaid and figure. Natural-language one/two/etc. may become equivalent Chinese quantities with per-block equivalence recorded
- Paper titles and author names remain searchable English, following S69/S83; translate their surrounding descriptions
- “conv–nonlinearity–downsample recipe” retains the three-step sequence. “1x1 down/up” must not be explained as spatial lowering/raising when it is channel compression/expansion
- “at most as bad”, “guarantee”, “escape hatch” retain the source's intended strength without adding a new optimization guarantee. Mathematical/source-risk notes remain outside the translated lesson
- Historical and accuracy assertions stay faithful source claims; shape-only validation cannot endorse them
