# S106-image-generation-diffusion 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Image Generation — Diffusion Models。

本地 check-only own3 候选，未安装、未发布，不计课程完成。复用作者101 TERM校准和当前独立语言审校；定向核对本课词义，不重扫全部历史词表。原common109为101 TERM+8 controls，own3另计、未来总112，不替换原支持身份。作者提案表格数据行逐字保留，不要求修改正文或旧词表。

| English | 中文呈现 | 语境与边界 |
|---|---|---|
| diffusion model | 扩散模型（diffusion model） | 引言首现；生成架构概念 |
| forward noising / reverse diffusion | 正向加噪 / 反向扩散 | 沿 S78；不同于前向/反向传播 |
| DDPM / DDIM | 去噪扩散概率模型（DDPM）/ 去噪扩散隐式模型（DDIM） | 学习目标首现；缩写保持 |
| sampler / sampling / sample | 采样器 / 采样；概率分布取值用抽样 / 样本 | S09/S18/S78分布抽样；图像生成算法通称采样器，不机械全局替換 |
| ancestral sampling | 祖先抽样 | 沿 S18；逆向链逐条件分布取值，不等于MCMC平稳迭代 |
| time conditioning | 时间条件化（time conditioning） | 用时间步告知网络噪声水平，不是钟表时间特征 |
| text conditioning | 文本条件化（text conditioning） | 图像生成文本条件 |
| inpainting / super-resolution | 图像修复（inpainting）/ 超分辨率（super-resolution） | 与一般图像编辑区别；不补具体实现 |
| classifier-free guidance | 无分类器引导（classifier-free guidance） | 下一课生产系统组件，不声称本课实现 |
| Gaussian noise | 高斯噪声（Gaussian noise） | S09高斯分布的噪声语境；不是Gaussian elimination |
| closed form | 闭式表达式（closed form） | 概率分布/一步抽样公式，区别求逆算法建议 |
| noise schedule / beta schedule | 噪声调度 / beta 调度 | 沿 S78；不是学习率调度；beta为方差，非标准差 |
| alpha_bar_t | 累计保留因子 | 保护乘积及变量；从源公式看是信号功率保留系数，幅度乘子是sqrt(alpha_bar_t)，正文不擅增改 |
| sinusoidal time embeddings | 正弦时间嵌入（sinusoidal time embeddings） | 保留时间步、多频率向量；区别SiLU激活 |
| bottleneck (U-Net) | 瓶颈层（bottleneck） | 沿S97；不是ResNet Bottleneck瓶颈块或性能瓶颈 |
| MSE | 均方误差（MSE） | 沿S40；与RMSE区别 |
| collapse / oscillation | 坍塌 / 振荡 | 此处生成模型训练语境；不把collapse译成程序崩溃 |
| scheduler | 调度器（scheduler） | diffusers扩散采样调度器；不能套S88学习率调度器 |
| LoRA / fine-tuning | LoRA（低秩适配）/ 微调（fine-tuning） | 沿核心；仅翻译库功能 |
| signal-to-noise ratio | 信噪比（signal-to-noise ratio） | 成果说明；未绘制SNR或实测 |
| epoch | 轮（epoch） | 沿S43/S69/S85；不等时间步或单个训练更新 |
| ODE | 常微分方程（ODE） | 术语表首次解释；忠实保留源对DDIM的概括 |

## 沿用和消歧

概率分布取值沿既有表用抽样，图像生成算法用采样器/采样；不用单一译法覆盖两种语境。正向加噪/反向扩散不是前向/反向传播；time conditioning不是钟表特征，扩散scheduler不是学习率调度器。alpha_bar与sqrt(alpha_bar)分别是功率保留因子与幅度系数；瓶颈层、坍塌和epoch按本课含义。两次真实修订保留：坍塌不误写程序崩溃，并改善抽取噪声、两级U-Net及逐渐加噪的中文表达。

## 保护规则

核心及补充表优先。API、模型、专名、标识符、路径、URL、公式、数值及代码/图载荷保持；按本课语境说明首现，不将异义词机械统一。源内矛盾、宽泛或版本性断言另列SCOPE，不静默改写源技术含义，不把翻译/语言PASS当作运行或安全验证。

只依赖固定英文及术语起草，不要求先修中文正式验收；本表不包含旧中文正文或segments。支持候选、语言审校、真实GFM、运行和批次分别记录。
