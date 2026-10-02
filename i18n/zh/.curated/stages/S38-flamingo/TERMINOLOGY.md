# S38 Flamingo 与门控交叉注意力术语增量 v1.0

2026-10-02。固定英文为 1bafaa88bb4668356791150bec3a6d7df38387eb，课程 12/04。沿用核心表、补充表和依赖清单固定术语；仅记录本阶段增量。可学习查询沿试点 BLIP-2 约定，前向传播与参数更新、冻结与停止梯度的区别沿 S29/S32。术语由协调者确认后采用。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| Perceiver resampler | Perceiver 重采样器（Perceiver resampler） | Perceiver 为专名；对特征序列进行注意力汇聚，不是音频采样率变换 |
| gated cross-attention | 门控交叉注意力（gated cross-attention） | LLM 侧为文本查询、视觉 K/V；与重采样器的可学习查询/图像 K/V 分清 |
| learnable latent queries | 可学习的潜在查询（latent queries） | fixed 指查询数量固定，不是权重冻结；沿用可学习查询，不暗示概率随机变量 |
| latents / latent vectors | 潜向量（latent vectors） | 这里是可学习的向量表示，非统计学潜变量；重采样后表示随输入而变 |
| interleaved input | 交错输入；图文交错输入 | 按阅读顺序排列，不能译为特征拼接已发生或早期融合已确定 |
| in-context few-shot learning | 上下文少样本学习 | 提示词示例中的适应不更新权重；不同于预训练阶段训练新增模块 |
| causal mask | 因果掩码（causal mask） | 文本自注意力禁止前瞻；图像位置掩码是另一约束，源不等式错误另列 |
| gate / gate schedule | 门控 / 门控调度（gate schedule） | tanh、alpha 原样；零门控输出为零不等于 alpha 梯度为零 |
| residual connection | 残差连接（residual connection） | 加法保留直接路径，不保证非零视觉支路不会损害文本表现 |
| cross-attn frequency | 交叉注意力频率（cross-attn frequency） | 每隔多少 LLM 层插入一次；M=4 的泛化风险不在译文纠正 |
| frozen LLM | 冻结的 LLM | 权重不更新，不表示反向传播不经过冻结运算；源表内“No LLM gradients”原意保留并单列风险 |
| visual bridge / backbone | 视觉桥接模块 / 主干网络 | 学习新的桥接模块与冻结既有模型分开 |
| model checkpoint | 模型检查点 | 区别于 S32 的梯度检查点（激活重计算）；不能假称已下载或测试检查点 |

专名保留：Flamingo、Chinchilla、BLIP-2、Q-Former、Perceiver、OpenFlamingo、Otter、Idefics/Idefics2/Idefics3、Gemini、Chameleon、LLaMA、MPT、MIMIC-IT、M3W、OBELICS、ALIGN、LTIP、VTP、Hugging Face、MosaicML/LAION、DeepMind、PyTorch、ViT、FFN、tanh。首次正文按需解释 VLM、LLM、ViT、FFN、VQA、token。

数字量级保持 70B、43M 等源形；首次分别说明 B 表示十亿、M 表示百万，不替换源数字。~120 minutes → ~120 分钟；three example pairs → 三组示例、two sub-steps → 两个子步骤等自然语言数量等值翻译。图形 figure 标识、公式、围栏负载、行内代码和 URL 原样；两个裸围栏仅补 text。
