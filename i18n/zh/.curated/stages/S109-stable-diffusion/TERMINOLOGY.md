# S109-stable-diffusion 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Stable Diffusion — Architecture & Fine-Tuning。

本地check-only own3候选，未安装、未发布，不计课程完成。复用101 TERM上下文校准和已有独立语言审校；定向核对本课词义，不重扫全部历史词表。原common109为101 TERM+8 controls，own3另计、未来总112，不替换原支持身份。原提案表格数据行逐字保留。

| EN | 本课译法 | 语境与边界 |
|---|---|---|
| Stable Diffusion | Stable Diffusion | 模型专名保留，不译成普通“稳定扩散” |
| DDPM / VAE / ODE | 去噪扩散概率模型（DDPM）/ 变分自编码器（VAE）/ 常微分方程（ODE） | 引句首现说明，源开篇把所有采样概括成确定性ODE的问题单列 |
| latent diffusion / latent space / latent | 潜在扩散 / 潜在空间 / 潜在表示 | 沿S80；图像编码后的表示，不套S38重采样器潜向量，也不把latent一律译为统计潜变量 |
| pipeline | 管线（pipeline）；后续管线 | 沿S57/S72/S77/S88/S101；非shell管道或流水线并行 |
| text encoder / denoiser | 文本编码器 / 去噪器 | 编码文本和预测图像潜在噪声角色分开 |
| classifier-free guidance / CFG | 无分类器引导；CFG | 不额外运行分类器；一组权重进行有条件和无条件预测 |
| guidance scale | 引导强度（guidance scale） | w=0无条件、w=1普通条件、w>1加强提示词影响；main.py误标签单列 |
| conditioning / conditional / unconditional | 条件输入（或以…为条件）/ 有条件 / 无条件 | 不套S19预条件化；按名词/形容词语法使用 |
| cross-attention / self-attention | 交叉注意力 / 自注意力 | ADDENDUM/S45/S92；本课由潜在token关注文本token，与Flamingo方向不同 |
| token / embedding | token（词元）/ 嵌入（embedding） | 沿核心；不是单词、身份令牌或特征选择嵌入法 |
| LoRA / fine-tuning / full fine-tuning | LoRA（低秩适配）/ 微调 / 全量微调 | 沿核心/S91；保留矩阵乘法、alpha、r及基座冻结方向 |
| base model / adapter | 基座模型 / 适配器 | 沿ADDENDUM；base pipeline按对象译基础管线，不机械套基座 |
| rank | 秩 | LoRA矩阵秩，不是张量阶、排名或排序 |
| scheduler / sampler | 调度器 / 采样器 | 本课正文为扩散采样算法，非S52/S58/S88学习率调度器；输出训练技能内另有学习率调度语境 |
| img2img / image-to-image / inpainting | Img2img（图生图）/ 图生图 / 图像修补 | 掩码白色再生成、黑色保留；源文对真实像素不变的绝对断言未验证 |
| mask | 掩码 | 图像空间区域，不是Dropout或注意力掩码 |
| skip connection | 跳跃连接 | 沿S85/S97；U-Net编码器和解码器匹配分辨率的连接 |
| gradient checkpointing | 梯度检查点（gradient checkpointing） | 沿S32/S82，激活重计算，不是梯度检查或训练状态检查点 |
| fidelity / precision | 保真度 / 精度 | 后者为float16、bfloat16、int8数值类型，不是分类精确率 |
| artefact / shipped artifact | 伪影 / 交付成果 | 图像失真与可复用文档产物分开 |
| subject / identity preservation | 主体 / 主体身份特征保留 | 可为宠物、标志或角色，不局限人物身份识别 |
| captions / trigger phrase | 图像描述 / 触发短语 | 数据集文本标注和模型卡风格激活词；示例文本和字符串保持 |

## 沿用和消歧

潜在空间/潜在表示沿图像语境；pipeline为管线，base model为基座模型、base pipeline为基础管线。CFG是无分类器引导；w=1的源代码误标签不改变术语定义。scheduler按扩散采样或训练学习率上下文区分，rank为矩阵秩。两次真实修订分别改善资源/潜在表示/基础管线表达，以及统一要解决的问题、实际使用两标题。

## 保护规则

核心及补充表优先。API、模型、专名、标识符、路径、URL、公式、数值及代码/图载荷保持；按本课语境说明首现，不将异义词机械统一。源内矛盾、宽泛或版本性断言另列SCOPE，不静默改写源技术含义，不把翻译/语言PASS当作运行或安全验证。

只依赖固定英文及术语起草，不要求先修中文正式验收；本表不包含旧中文正文或segments。支持候选、语言审校、真实GFM、运行和批次分别记录。
