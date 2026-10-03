# S77 /04-01 图像基础：像素、通道与色彩空间

日期：2026-10-03 UTC。状态：作者写作，非接受或发布。

- 唯一源 commit：`1bafaa88bb4668356791150bec3a6d7df38387eb`
- 英文：`phases/04-computer-vision/01-image-fundamentals/docs/en.md`，446 行，SHA256 `a1c3b51b94cc6bdf13f5b1b23e29275d6004fe0c7e226a7b0fbc1a6db95aacb8`
- 目标：`i18n/zh/phases/04-computer-vision/01-image-fundamentals/docs/zh.md`
- 记录：`i18n/zh/.curated/lessons/04-01/translation.json`，保持 draft，作者不代签独审
- 配套代码：`phases/04-computer-vision/01-image-fundamentals/code/main.py`，207 行，SHA256 `5b534d254b4c1bbf245ce57f82d41daa44145c58408c00439a64ac12da8f4e71`
- 先修：01-12 Tensor Operations（S14）、03-11 Intro to PyTorch（S69），均属于协调确认的实际95接受集合；S69术语精确锁定于 `c5a7764b15ef7c20f13b3a390d55c66d1ac4f6e4`
- 支持：本阶段 DEPENDENCIES.json 的83项不可变 path/commit/SHA256，已逐项比较本地文件与Git对象；原33控制的三份00-04测试资料独立且不作为翻译记忆
- 翻译：从固定英文全文新译，不读取旧中文、缓存、upstream452/457或他人译稿；仅采用接受术语。代码、注释、提示词、Mermaid、figure、数学、路径、链接与数字受保护；裸围栏只补 text。源无相对SVG引用，不引入无关资产
- 有界执行：已读完整代码，仅可执行原128x192x3合成NumPy默认与3倍缩放，另用1–8像素轴有限合成夹具。30秒外部timeout，CPU/单线程/PYTHONDONTWRITEBYTECODE；可选已安装torch微型CPU插值，缺失即skip。不运行PIL/OpenCV/torchvision、不安装、不联网、不加载真实图像/模型/数据、不执行输出提示词
- 核验：原strict、原33控制、两个全新目录精确字节重放；作者逐块技术对照和独立中文通读后，还需另一作者两次全文复核
- 源风险：另列技术账，尤其不可逆预处理概括、标准化不保证单图零均值单位方差、HSV约定、端点对齐与align_corners=False差异、uint8/float范围、二维灰度及单像素粗糙度边界，不静默修补
- 发布门禁：真实GitHub GFM精确commit/hash视觉验收另做，包含两幅Mermaid每个标签；figure交互、课程站点锚点/移动端、CI、整书构建与用户发布批准均为独立门禁。作者不commit/push/fetch、不写索引或公开review
