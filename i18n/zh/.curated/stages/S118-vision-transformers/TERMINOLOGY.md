# S118-vision-transformers 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；规范题名：Vision Transformers (ViT)。

本地check-only own3候选，未安装、未发布、不增加正式课程数。common121=113 TERM+8 controls，own3另计，未来总124。原10行术语提案与沿用/消歧说明逐字保留；113表为逐项身份校验、全文术语检索和适用行阅读，不声称逐字通读所有无关术语行。

| English | 本课译法 | 对齐与边界 |
|---|---|---|
| Vision Transformers (ViT) | 视觉 Transformer（ViT） | Transformer、ViT 保留；不译“变压器” |
| patch / patch embedding | 图像块 / 图像块嵌入（patch embedding） | 沿 S83 局部图像块；非软件补丁；一个卷积同时分块与投影 |
| class token | 类别 token（class token） | 新增本课语境；首现解释 token 为词元，后续保留 token；[CLS] 原样 |
| learned positional embedding | 可学习的位置嵌入 | 沿 S45 位置嵌入；不是位置插值，也不等于固定正弦编码 |
| pre-LN / post-LN | 前置层归一化 / 后置层归一化 | 首现保留英文；LayerNorm 沿 S45/S48；不交换残差相加与归一化位置 |
| stochastic depth | 随机深度（stochastic depth） | 训练时随机丢弃整个块；不等同常规按元素 Dropout |
| repeated augmentation | 重复增强（repeated augmentation） | 按源保持同一图像在每批采样 3 次；不是增添新样本数断言 |
| inverted bottleneck | 倒置瓶颈（inverted bottleneck） | 架构结构，不是性能瓶颈；不与 S85 普通 Bottleneck 直接互换 |
| Masked Autoencoder / MAE | 掩码自编码器（MAE） | 沿 S67 自编码器；75% 遮蔽、25% 可见，重构遮蔽部分，预训练后丢弃解码器 |
| mask / reconstruct | 遮蔽 / 重构 | 此处图像块遮蔽操作；非分割区域标签、认证权限或注意力因果掩码 |

沿用：S83 平移等变性、逐通道卷积；S88 归纳偏置、数据增强；S85/S91 主干网络、分类头；S91 线性探测、微调；S14/S45/S92 多头注意力、自注意力、缩放点积；S11/S43/S58 学习率预热；S38 残差连接；S08/S69 多层感知机（MLP）。架构名、模型 ID、GELU、API、token、路径与代码不强译。head 的注意力头与分类头分别处理。

九个通用章节标题沿 ADDENDUM，不以“术语统一”改变原文的技术范围、断言强度或先修课号。代码、Mermaid、figure 内容全部保留英文。

## 沿用和保护

固定英文与术语足以起稿，先修中文正式验收不是门禁。核心和补充表优先；代码、数字、数学、API、路径、URL和图载荷受保护，源问题见SCOPE。术语校准、自审、独审、真实GFM、远端回读和批次回归分别记录，未把作者自审或旧批次PASS提升为当前课程验收。
