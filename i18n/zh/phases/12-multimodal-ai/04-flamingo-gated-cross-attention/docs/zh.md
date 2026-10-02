# Flamingo 与少样本视觉语言模型中的门控交叉注意力

> DeepMind 的 Flamingo（2022）率先做到了两件事：它证明，单个模型可以处理图像、视频和文本任意交错的序列；它还证明，视觉语言模型（VLM）可以进行上下文学习（in-context learning）：只需在少样本（few-shot）提示词（prompt）中提供三组（图像、描述）示例，模型就能为新图像生成描述，无须进行任何梯度更新。背后的机制是门控交叉注意力（gated cross-attention）：在冻结的大语言模型（LLM）现有层之间插入交叉注意力层，并使用一个可学习的 tanh 门控。门控从零开始，使 LLM 在初始化时保留原有的文本能力。本课将逐步讲解 Flamingo 的 Perceiver 重采样器（Perceiver resampler）与门控交叉注意力架构。这套架构是 Gemini 交错输入和 Idefics2 视觉 token（词元）的先驱。

**Type:** Learn
**Languages:** Python (stdlib, gated cross-attention + Perceiver resampler demo)
**Prerequisites:** 阶段 12 · 03（BLIP-2 Q-Former）
**Time:** ~120 分钟

## 学习目标

- 解释门控交叉注意力如何通过 tanh(gate) = 0，在初始化时保留冻结 LLM 的文本能力。
- 逐步说明 Perceiver 重采样器的处理过程：通过交叉注意力，将 N 个图像块映射为数量固定为 K 的“潜在查询”（latent queries）。
- 描述 Flamingo 如何通过遵循图像位置的因果掩码（causal mask），处理图文交错序列。
- 复现少样本多模态提示词的结构：先给出 3 组图像与描述示例，再给出待处理的图像。

## 要解决的问题

BLIP-2 将 32 个视觉 token 送入冻结 LLM 的输入层。这适用于每条提示词只包含一张图像的情况。但如果你想输入*多张*图像，并与文本交错排列呢？例如：“这是图像 A，请描述它；这是图像 B，请描述它；现在这是图像 C，请描述它。”LLM 的自注意力（self-attention）就需要在同一条序列中处理图像 token 和文本 token，而哪些位置可以关注哪些图像，也会变得难以处理。

Flamingo 的回答是：完全不改变 LLM 的输入序列，而是在现有 LLM 块之间插入额外的交叉注意力层。文本 token 仍像往常一样经过 LLM 的因果自注意力。每隔几个 LLM 块，文本 token 还会通过一个新增的门控层，以交叉注意力关注图像特征。门控初始化为零，因此在第零步，新增层都是空操作（no-op），模型的行为与预训练 LLM 完全相同。随着训练推进，门控逐渐打开，视觉信息开始流入。

Flamingo 回答的第二个问题是：如何处理每条提示词中数量不定的图像（0 张、1 张或多张）？答案是 Perceiver 重采样器。这个小型交叉注意力模块接收任意数量的图像块，生成数量固定的视觉潜向量 token。无论提示词中有多少张图像，LLM 的交叉注意力层看到的形状都相同。

## 核心概念

### 冻结的 LLM

Flamingo 以冻结的 Chinchilla 70B LLM 为起点（B 表示十亿）。全部 70B 权重都保持不变。原有的文本自注意力与前馈网络（FFN）照常运行。

### Perceiver 重采样器

对于提示词中的每张图像，视觉 Transformer（ViT）会生成 N 个图像块 token。Perceiver 重采样器有数量固定为 K 的可学习潜向量（latent vectors；Flamingo 使用 K=64）。每个重采样器块分为两个子步骤：

1. 交叉注意力：K 个潜向量关注 N 个图像块 token（Q 来自潜向量，K/V 来自图像块）。
2. 在潜向量之间进行自注意力计算，再经过 FFN。

经过 6 个重采样器块后，无论 ViT 生成了多少图像块，输出都是 K=64 个维度为 1024 的视觉 token。一张 224x224 图像（196 个图像块）和一张 480x480 图像（900 个图像块），最后都输出 64 个重采样器 token。

对于视频，重采样器沿时间维度应用：每帧的图像块生成 64 个潜向量，时间位置编码使模型能够区分 t=0 与 t=N。整个视频最终表示为 T * 64 个视觉 token。

### 门控交叉注意力

在冻结 LLM 中，每隔 M 层（Flamingo 使用 M=4）插入一个新的门控交叉注意力块：

```text
x_after_llm_block = llm_block(x_before)
cross = cross_attn(x_after, resampler_output)
gated = tanh(alpha) * cross + x_after
x_before_next_block = gated
```

- `alpha` 是初始化为零的可学习标量。
- `tanh(0) = 0`，因此门控分支在初始化时的贡献为零。
- 随着 `alpha` 偏离零，交叉注意力的贡献幅度平滑增大。
- 残差连接（residual connection）意味着，即使门控完全打开，也不会覆盖 LLM 的文本表示，只会在其上叠加视觉信息。

这是 Flamingo 最重要的设计选择：视觉条件信息通过加法注入，并受门控控制，且在初始化时贡献为零。处于第 0 步的 Flamingo，在纯文本输入上的行为与 Chinchilla 70B 完全一致。

### 面向交错输入的掩码交叉注意力

在“\<image A> 描述 A \<image B> 描述 B \<image C> ?”这样的提示词中，每个文本 token 都只能看到序列中出现在它之前的图像。交叉注意力掩码施加以下约束：位于 `t` 的文本 token，只能关注图像索引满足 `i < i_t` 的图像重采样器 token，其中 `i_t` 是位置 `t` 之前最近一张图像的索引。“只看到前面最近的一张图像”和“看到前面的所有图像”都是可行的选择；Flamingo 选择了前者。

### 上下文少样本学习

Flamingo 的提示词如下所示：

```text
<image1> A photo of a cat. <image2> A photo of a dog. <image3> A photo of a
```

模型从中看出续写模式，输出“bird”（鸟），或 image3 中实际呈现的对象。整个过程没有梯度更新。冻结 LLM 的上下文学习能力通过门控交叉注意力得以延续。这是论文的核心结论，也是它的重要性所在。

### 训练数据

Flamingo 使用了三个数据集进行训练：

1. MultiModal MassiveWeb（M3W）：43M 个图文交错的网页（M 表示百万），重建其中的阅读顺序。
2. 图文对（ALIGN + LTIP）：4.4B 对。
3. 视频文本对（VTP）：27M 段短视频。

OBELICS（2023）是交错网页语料库的开放复现版本，Idefics、Idefics2 和大多数开放的“类 Flamingo”模型都使用它训练。

### OpenFlamingo 与 Otter

OpenFlamingo（2023）是开放复现版本，架构完全相同：在冻结的 LLaMA 或 MPT 上使用 Perceiver 重采样器与门控交叉注意力。其模型检查点有 3B、4B、9B 三种规模。由于基座 LLM 更小、数据更少，它的质量落后于 Flamingo。

Otter（2023）在 OpenFlamingo 的基础上，使用多模态指令数据集 MIMIC-IT 进行指令微调（instruction tuning），表明门控交叉注意力同样适用于指令遵循。

### 后续衍生模型

- Idefics / Idefics2 / Idefics3：Hugging Face 的门控交叉注意力一系，架构逐步简化（Idefics2 移除了重采样器，改用图像块 token 与自适应池化）。
- 从 Flamingo 到 Chameleon 的转变：到 2024 年，许多团队转向早期融合（early fusion，第 12.11 课）；在要求冻结主干网络的生产场景中，Flamingo 风格的门控交叉注意力仍在使用。
- Gemini 的交错输入：从概念上继承了 Flamingo 交错格式的灵活性，但具体机制属于专有技术。

### 与 BLIP-2 的比较

| | BLIP-2 | Flamingo |
|---|---|---|
| 视觉桥接模块 | 在输入端使用一次 Q-Former | 每隔 M 层使用一次门控交叉注意力 |
| 视觉 token | 每张图像 32 个 | 每个交叉注意力层中，每张图像 64 个 |
| 冻结 LLM | 是 | 是 |
| 上下文少样本能力 | 弱 | 强，是论文的核心亮点 |
| 交错输入 | 无原生支持 | 支持，这是设计目标 |
| 训练数据 | 130M 对 | 1.3B 对 + 43M 个交错网页 |
| 参数量 | 188M 参数参与训练 | 约 10B 参数参与训练（交叉注意力层） |
| 计算资源 | 在 8 张 A100 上训练数天 | 在数千个 TPUv4 上训练数周 |

如果预算有限，要做单图视觉问答（VQA），选 BLIP-2。如果需要交错输入、少样本学习或多图推理，选 Flamingo/Idefics2。

```figure
cross-attention-fusion
```

## 实际使用

`code/main.py` 演示了：

1. 用 Perceiver 重采样器处理 36 个模拟图像块 token，并使用 8 个可学习潜向量（纯 Python 交叉注意力）。
2. 执行一次门控交叉注意力计算：`alpha = 0` → 输出等于输入（LLM 不变）；随后设为 `alpha = 2.0` → 混入视觉信息。
3. 构建交错输入掩码，为“（图像 1）（文本 1）（图像 2）（文本 2）”序列生成 2D（二维）注意力掩码。

## 交付成果

本课产出 `outputs/skill-gated-bridge-diagnostic.md`。给定一个开放 VLM 的配置（是否使用重采样器、交叉注意力频率、门控方案），它会识别其中源自 Flamingo 的组成部分，并解释其冻结策略。这有助于排查为什么微调会损害文本表现，答案是门控开得太大、太快。

## 练习

1. 计算 Flamingo-9B 的视觉参数量：9B LLM + 1.4B 门控交叉注意力层 + 64M 重采样器。参与训练的参数占总参数量的比例是多少？

2. 在 PyTorch 中实现门控残差 `y = tanh(alpha) * cross + x`。通过实验表明，当 `alpha=0` 时，初始化状态下严格满足 `y==x`。

3. 阅读 OpenFlamingo 第 3.2 节（arXiv:2308.01390），了解一个批次中各条提示词的图像数量不同时，模型如何处理多张图像。描述其填充策略。

4. 为什么 Flamingo 的交叉注意力掩码允许文本 token 关注的*只有前面最近的一张*图像，而不是前面所有图像？阅读 Flamingo 论文第 2.4 节，解释其中的权衡。

5. 上下文少样本学习：为一个新的 Flamingo 变体构造提示词，其中包含 4 个“图像 → 主体对象颜色”的示例。描述当示例数量从 0 变到 8 时，你预期准确率会呈现怎样的变化。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|------------------------|
| Perceiver 重采样器 | “潜向量数量固定的交叉注意力” | 将数量可变的输入图像块转换为固定 K 个 token 的模块 |
| 门控交叉注意力 | “tanh 门控桥接模块” | 残差层 `y = tanh(alpha)*cross + x`，alpha 可学习，初始化为 0 |
| 交错输入 | “混合序列” | 图像与文本按阅读顺序自由混合的提示词格式 |
| 冻结的 LLM | “没有 LLM 梯度” | 文本 LLM 的权重不更新；只训练重采样器与交叉注意力层 |
| 少样本 | “上下文中的示例” | 在提示词中给出少量（图像、答案）对，模型无须微调即可泛化 |
| OBELICS | “交错网页语料库” | 开放数据集，包含 141M 个网页，其图像与文本按阅读顺序排列 |
| Chinchilla | “70B 冻结基座” | Flamingo 冻结的文本 LLM，来自 DeepMind 的 Chinchilla 论文 |
| 门控调度（gate schedule） | “alpha 如何变化” | 训练过程中交叉注意力门控打开的速率 |
| 交叉注意力频率（cross-attn frequency） | “每隔 M 层” | 插入门控交叉注意力块的频率；Flamingo 使用 M=4 |
| OpenFlamingo | “开放复现版本” | MosaicML/LAION 的 3-9B 开放模型检查点；架构与 Flamingo 完全相同 |

## 延伸阅读

- [Alayrac 等 — Flamingo（arXiv:2204.14198）](https://arxiv.org/abs/2204.14198) — 原始论文。
- [Awadalla 等 — OpenFlamingo（arXiv:2308.01390）](https://arxiv.org/abs/2308.01390) — 开放复现。
- [Laurençon 等 — OBELICS（arXiv:2306.16527）](https://arxiv.org/abs/2306.16527) — 交错网页语料库。
- [Jaegle 等 — Perceiver IO（arXiv:2107.14795）](https://arxiv.org/abs/2107.14795) — 通用 Perceiver 架构。
- [Li 等 — Otter（arXiv:2305.03726）](https://arxiv.org/abs/2305.03726) — 经指令微调的 Flamingo 衍生模型。
- [Laurençon 等 — Idefics2（arXiv:2405.02246）](https://arxiv.org/abs/2405.02246) — 对 Flamingo 方法的现代简化版本。
