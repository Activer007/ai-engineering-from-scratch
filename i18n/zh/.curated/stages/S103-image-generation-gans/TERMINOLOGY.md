# S103-image-generation-gans 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Image Generation — GANs。

本地 check-only own3 候选，未安装、未发布，不计课程完成。复用作者98 TERM校准和当前独立语言审校；定向核对本课词义，不重扫全部历史词表。原common106为98 TERM+8 controls，own3另计、未来总109，不套早期common103或后续common109。作者提案JSON数据值逐值保留，不要求修改正文或旧词表。

| English | 本课呈现 | 语义边界（原提案） |
|---|---|---|
| generative adversarial network / GAN | 生成对抗网络（GAN） |  |
| generator / discriminator | 生成器 / 判别器 |  |
| minimax game | 极小极大博弈 |  |
| DCGAN | 深度卷积生成对抗网络（DCGAN） |  |
| non-saturating loss | 非饱和损失 |  |
| spectral normalisation / spectral norm / SN | 谱归一化（SN） | Normalization technique, not merely the scalar matrix spectral norm; source guarantee recorded separately. |
| TTUR / two-timescale update rule | 双时间尺度更新规则（TTUR） |  |
| mode collapse | 模式坍缩 | Distinct from representation collapse or catastrophic forgetting. |
| minibatch discrimination | 小批量判别 |  |
| label conditioning / class conditioning | 标签条件控制 / 类别条件控制 |  |
| FID / Fréchet Inception Distance | FID（Fréchet Inception 距离） |  |
| image-to-image translation | 图像到图像转换 |  |
| Jensen-Shannon divergence | Jensen-Shannon 散度 |  |
| latent space | 潜在空间 |  |

## 沿用和消歧

沿core的scaffold / workbench行：scaffold→脚手架；revision-03已在正文首现补“脚手架（scaffold）”，不新增术语替换。FID沿作者提案保留Fréchet Inception专名；正文首现另保留完整英文Fréchet Inception Distance，词表短写不是要求删除该全称。它是Inception-v3特征分布的距离，不是像素距离或已测得的生成质量。SN在本课指谱归一化技术，不能把矩阵谱范数与整网1-Lipschitz保证混为同一个已验证结论。image-to-image translation为图像转换，不套机器翻译；mode collapse不套表示坍缩或灾难性遗忘。

## 保护规则

核心及补充表优先。API、模型、专名、标识符、路径、URL、公式、数值及代码/图载荷保持；按本课语境说明首现，不将异义词机械统一。源内矛盾、宽泛或版本性断言另列SCOPE，不静默改写源技术含义，不把翻译/语言PASS当作运行或安全验证。

只依赖固定英文及术语起草，不要求先修中文正式验收；本表不包含旧中文正文或segments。支持候选、语言审校、真实GFM、运行和批次分别记录。
