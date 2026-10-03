# S80 水印：SynthID、Stable Signature 与 C2PA 范围

2026-10-03。作者仅在独立 worktree 本地完成 18-23；记录保持 draft。完整读取固定英文 118 行与 code/main.py 111 行后开始，不使用旧中文、翻译缓存、upstream PR452/457 或同波作者稿。

## 固定输入与输出

- 源提交：`1bafaa88bb4668356791150bec3a6d7df38387eb`
- 英文：`phases/18-ethics-safety-alignment/23-watermarking-synthid-stable-signature-c2pa/docs/en.md`
- 源 SHA256：`ae55115b02803bcdeaa1a2e65035857646ce3b9703e3d2eb5fd9992b958c767c`
- 中文：`i18n/zh/phases/18-ethics-safety-alignment/23-watermarking-synthid-stable-signature-c2pa/docs/zh.md`
- 记录：`i18n/zh/.curated/lessons/18-23/translation.json`
- 代码：`phases/18-ethics-safety-alignment/23-watermarking-synthid-stable-signature-c2pa/code/main.py`，SHA256 `4ee455c7a9f1d0e575a3212f980ecfc6a87721279a977b11bdfe94dea7d36152`
- 支持组成由本阶段 `DEPENDENCIES.json` 的正好 83 个不可变 path/commit/SHA256 元组定义；已逐一校验工作文件与本地 immutable Git blob，不重锁、不改已接受词表。00-04 三个固定测试样例仅用于原 33 控制测试，不属于支持 pins 或新译课数。

## 前置条件证据

- 英文前置 10-04（sampling）对应已接受 S45。固定英文 `phases/10-llms-from-scratch/04-pre-training-mini-gpt/docs/en.md` 439–461 行的 Text Generation 明确归一化 logits 并以 `np.random.choice(..., p=probs)` 采样；不因目录标题不同判作缺课。
- 英文前置 01-09 信息论对应已接受 S12。只采用上述接受课术语与固定英文必要语义，不读取既有中文正文。
- 正式 95 索引由协调者管理；不把同波其他作者、待验收 S61/S66/S73 或未来课计作接受前置。

## 写作和执行边界

完整英中逐块对照与独立的中文单语通读由本作者分别完成并绑定最终字节，随后交另一作者独审。本作者不写自身独审 review.json，不执行 commit/fetch/push/remote/index 更新。

保留所有代码、figure 载荷、数值、运算符、行内代码、路径、链接、Type/Languages 值；本课只有 `figure` 载荷，无相对 SVG，资产清单为空。无标签围栏只可补 text；不新增校验例外。术语沿核心及补充表；provenance 为来源信息，tamper-evident 为可检测篡改，不能扩为不可篡改。

执行只限已完整审读的原函数，以 stdlib、固定种子、离线合成整数 token、长度 0–64、最多 8 次采样/扰动调用，外层 30 秒 timeout 与 PYTHONDONTWRITEBYTECODE=1。检查奇偶二分、短前缀、bias 两端与 z 分数。绝不执行默认 100×1000 sweep，不用真实文本/音视频/模型，不运行真实 SynthID/Stable Signature、C2PA 密钥签名或元数据更改，不下载、不调用网络/API、不执行 outputs 提示词。

## 分离的风险与验收门禁

随机整数替换不等于同义词语义改写，合成 token 不等于人类文本，缩小 fixture 不证明生产鲁棒性或稀有误报率。来源的 SynthID 历史/统一 API、Stable Signature 解码/微调表述、FPR/鲁棒性、2026 法规时间线与深伪标注断言均原义保留，问题另列；不是当前法律建议。

原 strict、原 33 控制、两处全新输出目录精确字节回放与 83 pins 复核属于本地门禁。另一作者独审、精确 immutable commit 的完整真实 GitHub GFM 视觉验收、正式网站锚点/移动布局/figure 交互、托管 CI、用户发布批准和完整书籍构建分别待验。源 figure 占位符不算验证交互；空 CI 数组不算成功。作者完成不等于接受、合并或发布。
