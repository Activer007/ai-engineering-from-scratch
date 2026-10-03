# 水印：SynthID、Stable Signature、C2PA

> 三项技术构成了 2026 年 AI 生成内容来源信息（provenance）的技术框架。SynthID（Google DeepMind）：图像水印于 2023 年八月推出，文本+视频水印于 2024 年五月推出（Gemini + Veo），文本水印于 2024 年十月通过 Responsible GenAI Toolkit 开源，统一多媒体检测器于 2025 年十一月随 Gemini 3 Pro 推出。文本水印以难以察觉的方式调整下一 token（词元）的采样概率；图像/视频水印能经受压缩、裁剪、滤镜和帧率变化。Stable Signature（Fernandez 等人，ICCV 2023，arXiv:2303.15435）：通过微调（fine-tuning）潜在扩散解码器，让每个输出都包含一条固定消息；对裁剪后仅保留 10% 内容的生成图像，在误报率 FPR<1e-6 时检测率 >90%。后续研究 "Stable Signature is Unstable"（arXiv:2405.07145，2024 年五月）表明，微调能在保持质量的同时去除水印。C2PA：经过密码学签名、可检测篡改的元数据标准（C2PA 2.2 Explainer 2025）。水印与 C2PA 相互补充：元数据可以被剥离，但能携带更丰富的来源信息；水印在转码后仍能保留，但携带的信息较少。

**Type:** Build
**Languages:** Python (stdlib, token-watermark embed + detect)
**Prerequisites:** 阶段 10 · 04（采样）、阶段 01 · 09（信息论）
**Time:** ~75 分钟

## 学习目标

- 描述 token 级水印（SynthID-text 风格）及其可被检测的机制。
- 描述 Stable Signature，以及 2024 年攻破它的去除攻击。
- 说明 C2PA 的作用，以及它为何与水印互补。
- 描述主要局限：特定模型的信号、改写下的鲁棒性，以及保持语义的攻击（arXiv:2508.20228）。

## 要解决的问题

2023-2024 年，深度伪造和 AI 生成内容大规模进入政治与消费场景。水印是为此提出的一种技术性来源信息信号：在创建时标记生成内容，之后再进行检测。2025 年的证据表明：没有任何水印能够无条件保持鲁棒，但将它与 C2PA 元数据分层结合，可以提供一套可用的来源信息方案。

## 核心概念

### 文本水印（SynthID-text 风格）

Kirchenbauer 等人于 2023 年提出、由 Google 投入生产应用的机制：

1. 在每个解码步骤，对之前的 K 个 token 进行哈希，将词表伪随机地划分为“绿色”和“红色”两个集合。
2. 给绿色集合的 logits（未经归一化的分数）加上 δ，使采样偏向绿色集合。
3. 生成内容中的绿色 token 数量多于随机情况下的预期数量。

检测：重新对每个前缀计算哈希，统计生成内容中的绿色 token 数量，并计算 z 分数。带水印文本的 z 分数 >0，人类文本的 z 分数 ~0。

特性：
- 读者难以察觉（δ 足够小，因此质量损失较小）。
- 只要能访问词表划分函数，就能检测。
- 无法抵抗改写：重写文本会破坏信号。

SynthID-text 于 2024 年十月通过 Google 的 Responsible GenAI Toolkit 开源。

### Stable Signature（图像）

Fernandez 等人，ICCV 2023。微调潜在扩散解码器，使每张生成图像都包含一条嵌入潜在表示的固定二进制消息。检测时，通过神经解码器从潜在表示中解码。对于裁剪后仅保留 10% 内容的图像，在 FPR<1e-6 时检测率 >90%。

2024 年五月的 "Stable Signature is Unstable"（arXiv:2405.07145）表明：微调解码器可以在保持图像质量的同时去除水印。生成后的对抗性微调成本很低；水印的对抗鲁棒性有限。

### SynthID 统一检测器（2025 年十一月）

随 Gemini 3 Pro 一同推出：一个多媒体检测器，通过一个 API（应用程序编程接口）读取文本、图像、音频和视频中的 SynthID 信号。它统一了 Google 的来源信息技术栈。

### C2PA

内容来源与真实性联盟（Coalition for Content Provenance and Authenticity）。经过密码学签名、可检测篡改的元数据标准。C2PA 2.2 Explainer（2025）。C2PA 清单记录来源信息声明（由谁创建、何时创建、经历了哪些变换），并由创建者的密钥签名。

与水印互补：
- 元数据可以被剥离；水印则不能被轻易去除。
- 元数据很丰富（包含完整的来源信息链）；水印携带的是比特。
- C2PA 依赖平台采用；水印则会自动嵌入。

Google 在 Search、Ads 和 "About this image" 中同时集成了两者。

### 局限

- **特定模型。** SynthID 为启用 SynthID 的模型所生成的内容添加水印。未启用 SynthID 的模型生成的内容没有这种水印，因此“没有 SynthID 信号”并不能证明内容真实。
- **改写。** 文本水印无法在保持语义的改写后保留下来。
- **变换攻击。** arXiv:2508.20228（2025）展示了保持语义的攻击，能破坏文本水印和许多图像水印。
- **微调去除。** 根据 "Stable Signature is Unstable"，生成后的微调可以去除嵌入的水印。

### 欧盟《人工智能法案》第 50 条

AI 生成内容标注透明度准则（根据[欧盟委员会状态页面](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content)，初稿于 2025 年十二月发布，第二稿于 2026 年三月发布，预计于 2026 年六月定稿）。截至 2026 年四月，该准则仍处于草案阶段，时间安排可能变化。这是要求采取上述技术措施的监管层。深度伪造内容必须标注。

### 本课在阶段 18 中的位置

第 22-23 课讨论模型输出的内容（私有数据、来源信息信号）。第 27 课涵盖训练数据治理。第 24 课介绍要求采取这些技术措施的监管框架。

```figure
an-watermark-greenlist
```

## 实际使用

`code/main.py` 构建了一个玩具文本水印。token 是 0..N-1 范围内的整数；带水印的采样偏向由哈希定义的绿色集合。检测器计算绿色 token 的 z 分数。你可以观察对长度为 1000 个 token 的生成序列的检测，看改写如何破坏信号，并测量人类文本上的误报率。

## 交付成果

本课产出 `outputs/skill-provenance-audit.md`。给定一个声称具有来源信息的内容部署，它会审计：水印机制（如有）、C2PA 签名链（如有）、两者各自的对抗鲁棒性，以及对各模态的覆盖情况。

## 练习

1. 运行 `code/main.py`。报告长度为 1000 个 token 的带水印生成序列与人类撰写文本的 z 分数。确定 95% 置信阈值下的误报率。

2. 实现一种改写攻击，用同义词替换 30% 的 token。重新测量 z 分数。

3. 阅读 Kirchenbauer 等人 2023 年论文中关于鲁棒性的第 6 节。为什么文本水印经不起改写，而图像水印可以经受裁剪？

4. 设计一个使用 SynthID-text + C2PA 元数据的部署方案。描述消费者看到的来源信息链。指出每个组件的一种失效模式。

5. 2024 年的 "Stable Signature is Unstable" 结果表明，微调能够去除图像水印。设计一种限制此攻击的部署控制措施，例如要求对微调后的模型检查点进行签名发布。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|-----------------|------------------------|
| SynthID | “Google 的水印” | 跨模态来源信息信号；覆盖文本、图像、音频、视频 |
| token 水印 | “Kirchenbauer 风格” | 基于偏置采样的文本水印，可通过绿色 token 的 z 分数检测 |
| Stable Signature | “图像水印” | 通过微调解码器实现的水印；ICCV 2023 |
| C2PA | “那个元数据标准” | 经过密码学签名、可检测篡改的来源信息元数据 |
| 改写鲁棒性 | “换个说法会不会破坏它” | 文本水印的一项性质；目前有限 |
| 微调去除 | “对抗性去水印” | 通过微调解码器去除图像水印的攻击 |
| 跨模态检测器 | “统一 SynthID” | 2025 年十一月推出的跨模态统一 API |

## 延伸阅读

- [Kirchenbauer 等人 — A Watermark for Large Language Models（ICML 2023，arXiv:2301.10226）](https://arxiv.org/abs/2301.10226) — token 水印机制
- [Fernandez 等人 — Stable Signature（ICCV 2023，arXiv:2303.15435）](https://arxiv.org/abs/2303.15435) — 图像水印论文
- ["Stable Signature is Unstable"（arXiv:2405.07145）](https://arxiv.org/abs/2405.07145) — 去除攻击
- [Google DeepMind — SynthID](https://deepmind.google/models/synthid/) — 跨模态水印
- [C2PA 2.2 Explainer（2025）](https://c2pa.org/specifications/specifications/2.2/explainer/Explainer.html) — 元数据标准
