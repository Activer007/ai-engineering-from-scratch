# S80 水印与来源信息术语增量 v1.0

2026-10-03。联用核心、补充表及 DEPENDENCIES.json 的 83 项 immutable 支持文件。仅服务固定英文 18-23；来源技术问题单列，不以译文暗修。

| EN | 推荐呈现 | 语境与边界 |
|---|---|---|
| watermarking / watermark | 水印技术 / 水印 | 生成时嵌入可检测信号；不意味着所有模型或变换均覆盖 |
| provenance / provenance chain | 来源信息（provenance）/ 来源信息链 | 沿核心用语，包含创建者、时间、变换等可追溯记录；不保证内容真实性 |
| token / token watermark | token（词元）/ token 水印 | 沿核心保留 token；toy 的整数索引不是人类文本或同义词 |
| green / red set | 绿色集合 / 红色集合 | 指词表分区而非像素颜色；代码只在两种奇偶分区中切换 |
| logits | logits（未经归一化的分数） | 保持 logits 与概率区别；toy 用组选择概率，不是真实模型 logits |
| pseudorandom partition | 伪随机划分 | 源机制用哈希上下文；不额外承诺密码学安全或任意分区 |
| z-score / FPR | z 分数 / 误报率（FPR） | 标准化检测统计量与误报比例；有限合成 fixture 不能确认稀有 FPR |
| latent diffusion decoder / latent representation | 潜在扩散解码器 / 潜在表示 | 按源角色保留，源检测器输入和微调时序问题单列 |
| fine-tuning / fine-tune removal | 微调（fine-tuning）/ 微调去除 | 与生成后编辑图像不同；源 post-generation 表述不暗修 |
| paraphrase / meaning-preserving | 改写 / 保持语义 | 自然语言重述保持含义；随机 token 替换仅为源 toy 命名，不背书语义保持 |
| adversarial robustness | 对抗鲁棒性 | 对恶意变换的抵抗性，与普通压缩/裁剪适应性分开 |
| tamper-evident | 可检测篡改 | 沿补充表，绝不译成不可篡改或绝对防篡改 |
| cryptographically signed / signing chain | 经过密码学签名 / 签名链 | 元数据真实性/完整性证据；不运行密钥、签名或元数据操作 |
| C2PA manifest | C2PA 清单 | 记录来源信息声明；与一般模型采样、水印有效性不同 |
| transcoding / frame-rate changes | 转码 / 帧率变化 | 仅按源鲁棒性陈述翻译，本次未做媒体实测 |
| cross-modal / multi-media detector | 跨模态 / 多媒体检测器 | 品牌历史与统一 API 断言保留源时间，不宣称当前已验证 |
| checkpoint / signed release | 模型检查点 / 签名发布 | 沿 S45 的 checkpoint 用法；练习设计要求不等于授权发布 |

专名、论文题名与标识原样：SynthID、SynthID-text、Stable Signature、"Stable Signature is Unstable"、Responsible GenAI Toolkit、Google DeepMind、Gemini、Veo、Gemini 3 Pro、Kirchenbauer、Fernandez、C2PA、ICCV、ICML、API、arXiv。API 正文首现补“应用程序编程接口”；C2PA 全称译“内容来源与真实性联盟”。

通用章节使用：学习目标、要解决的问题、核心概念、实际使用、交付成果、练习、关键术语、延伸阅读。元数据 `~75 minutes` 等值译 `~75 分钟`。August/May/October/November/December/March/June/April 对应八月/五月/十月/十一月/十二月/三月/六月/四月，年份数字保留；数字串、百分比、K、δ、>0、~0、>90%、FPR<1e-6 和 0..N-1 按源保持。
