# S145-diffusion-transformers-rectified-flow terminology support

Fixed English: 1bafaa88bb4668356791150bec3a6d7df38387eb, lesson 04-23. Preauthor support candidate only; lexical entries are not Chinese lesson prose. Common149 (141 terminology + 8 controls) and own3 have separate identities. Publication/readback/installation and actual author calibration/first write remain pending.

Core TERMINOLOGY.md was read completely. ADDENDUM preamble/common headings and relevant attention row were read; full relevant S106, S109, S118 and S40 terminology was read. Targeted common-term searches also checked S15/S45/S48 normalization and residual rows, S121 distillation, S134 flow matching, and S103 FID row/provenance. All referenced payloads match immutable common149 pins. Historical candidate labels inside pinned supports do not change their externally verified roles. This is support-preparer calibration; it is not the future author's proposal or independent lesson review.

| English | Candidate Chinese rendering | Context and calibration |
|---|---|---|
| Diffusion Transformer / DiT | 扩散 Transformer（DiT） | New lesson-specific compound; preserve Transformer/DiT architecture names. Not an electrical transformer. |
| rectified flow | 整流流（rectified flow） | New short lexical mapping. Keep the English at first body occurrence; do not confuse with ReLU/rectification of electrical current. |
| flow matching / Rectified Flow Matching | 流匹配 / 整流流匹配（Rectified Flow Matching） | Flow matching follows S134; the longer term is lesson-specific. Do not equate every flow model with this straight interpolation. |
| velocity / velocity target | 速度 / 速度目标 | New generative-ODE context; epsilon - x_0 points data→noise in the protected parameterization. It is not a noise prediction or a physical speed measurement. |
| straight-line interpolation / trajectory | 直线插值 / 轨迹 | Geometry of the source construction; do not assert the learned sampling ODE is exactly straight. |
| ODE / SDE | 常微分方程（ODE）/ 随机微分方程（SDE） | ODE follows S106/S109; SDE is a lesson-specific addition. Deterministic/stochastic distinction remains. |
| Euler sampler / Euler steps | Euler 采样器 / Euler 步 | Retain the named method; backward integration sign is protected. No change to step counts. |
| adaptive layer norm / AdaLN | 自适应层归一化（AdaLN） | Layer normalization follows S15/S45/S48/S118; adaptive qualifier is new. API LayerNorm stays literal. |
| AdaLN-Zero / zero init | AdaLN-Zero / 零初始化 | Keep algorithm/class names. Zero gates make residual block identity; do not silently change the source sentence's referent. |
| scale / shift / gate | 缩放量 / 偏移量 / 门控量 | Context-specific modulation outputs. Protected scale, shift, gate identifiers remain English. Scale is not model size here. |
| identity mapping / residual connection | 恒等映射 / 残差连接 | Residual term follows S45/S118. Do not confuse identity with authentication or class identity. |
| patch / patch embedding / unpatchify | 图像块 / 图像块嵌入 / 将图像块重组为图像 | Patch terms follow S118; unpatchify is a short new verbal mapping, not a software patch reversal. |
| latent patches / latent space | 潜在表示的图像块 / 潜在空间 | S109 visual latent context. Do not claim the RGB toy includes a VAE when it does not. |
| MMDiT / multimodal | MMDiT / 多模态 | MMDiT retained; explain multimodal DiT at first use without renaming model IDs. |
| single-stream / double-stream | 单流 / 双流 | New architecture distinction: separate modality weights versus concatenation/shared weights. Not streaming generation. |
| joint attention / joint self-attention | 联合注意力 / 联合自注意力 | Self-attention follows core/ADDENDUM/S109. Distinguish from cross-attention and preserve separate weights. |
| conditioning / conditional / unconditional | 条件输入（或以…为条件）/ 有条件 / 无条件 | Follow S109 grammar; use 时间条件化 or 文本条件化 for the operation per S106. Not numerical preconditioning. |
| classifier-free guidance / CFG | 无分类器引导（CFG） | Follow S106/S109; first occurrence can include the full English. Do not imply a separate classifier. |
| guidance scale | 引导强度 | S109; protected guidance_scale stays unchanged. Preserve schnell's 0.0. |
| distillation / teacher / student | 蒸馏 / 教师模型 / 学生模型 | S40/S121. Step distillation means fewer sampling steps, not necessarily fewer parameters. |
| consistency model / LCM | 一致性模型 / 潜在一致性模型（LCM） | New short lexical entries; preserve method distinction from adversarial diffusion distillation. |
| denoiser / text encoder / sampler / scheduler | 去噪器 / 文本编码器 / 采样器 / 调度器 | S106/S109. Scheduler in diffusers concerns sampling; a training output may instead mean learning-rate scheduler. |
| MSE / FID | 均方误差（MSE）/ FID（Fréchet Inception 距离） | MSE follows S40; FID follows pinned S103 (row and provenance read). First body occurrence retains Fréchet Inception Distance. The source exercise calls this a FID proxy; it is not a computed standard score. |
| precision / latency / throughput | 精度 / 延迟 / 吞吐量 | Core/S109; numerical precision differs from metric precision. No actual speed measurement. |
| prompt adherence / typography | 提示词遵循程度 / 文字排版 | New lexical context for generated images; do not upgrade to guaranteed spelling or correctness. |
| permissive / non-commercial / research license | 宽松许可 / 非商业许可 / 研究用途许可 | Descriptive labels only. Preserve exact model-card license names and do not infer legal clearance. |

Common headings: 学习目标、要解决的问题、核心概念、动手实现、实际使用、交付成果、练习、关键术语、延伸阅读. Keep the source's order and existing Step numbers; do not add absent sections. Metadata keys and Learn + Build/Python remain English; ~75 minutes may become ~75 分钟.

First body use should follow core English/acronym explanation rules. All model and algorithm names, quoted IDs, class/function names, protected code, Mermaid/figure payloads, formula symbols, signs, numeric quantities, paths and URLs remain exact. Keep sample/sampling contextual: distribution draws versus image-generation sampling. Keep model checkpoints distinct from gradient checkpointing; no blanket global replacement. No old Chinese lesson body or translation segment is included in this support.
