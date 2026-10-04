# S134-text-to-speech English-first 支持范围

准备时刻：2026-10-04T23:08:24.948368+00:00。状态：正文起草前 own3 本地候选，尚未发布或安装 own3。课程 06-07，Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro；固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb。common136 =128 TERM +8 controls；本课 own3 独立计数，完整支持集合拟为139，不增加正式课程数。

## 已固定范围

仅计划翻译 phases/06-speech-and-audio/07-text-to-speech/docs/en.md 至 i18n/zh/phases/06-speech-and-audio/07-text-to-speech/docs/zh.md。完整静态阅读本课全部 5 个英文包文件；必要英文先修的本次全文阅读和精确旧全文阅读复用逐项写在 DEPENDENCIES.json，包含路径、SHA、Git blob、字节数和复用证据。源先修原文：**Prerequisites:** Phase 6 · 02 (Spectrograms & Mel), Phase 5 · 09 (Seq2Seq), Phase 7 · 05 (Full Transformer)。先修依据固定英文与相关术语，不要求先修中文正式验收。

common136 只追加已发布并独核的 S127、S128、S129 TERM；未纳入 S130–S132 TERM。S117 沿真实修订 ff4d56e72126e854321b5d95a7c43a8b57a485bf / 6631ae3d6b514d374a63bd21afa98eaedeb995e2aeed3e664e037e6de6ea0c85。common 集合 SHA256：8e508ca2b84d6b40df38b3377e1946deadd0138fd55b359f9c8503a736b03fec。原身份、顺序、角色和分类保持；公开投影不包含本地定位信息。

## 待发生事实

作者未开始，首写、首稿、capture、record、修订、strict、完整英文技术对照和另次中文通读全部 pending。对应时间、hash、字节数为 null，修订列表为空。本候选不冒充作者提案或独审。后续首写/独审真实历史进入 review；若词表改变，另发真实支持增量，保留当前冻结证据。

## 固定英文源风险

- docs/en.md model table / Use It / APIs：Fixed2026 rankings, English-only/closed-vocabulary Kokoro, model sizes, dates, architecture summaries, licenses and example API return contracts are unverified source claims. Preserve rather than silently update; no model/API/network use.
- docs/en.md HiFiGAN / pseudocode / assets/tts.svg; code/main.py：Prose/SVG use256 samples per mel frame while main uses300 for12.5ms at24kHz. HiFiGAN is a sketch with undefined blocks; acoustic_model and speaker placeholders are pseudocode. Do not imply full implementation or real synthesis.
- code/main.py phonemize/duration/mel_schedule：Toy substring lookup silently drops unknown characters and the digit6, without actual text normalisation; duration is a table plus seeded random jitter. zip silently truncates unequal lists. Printed quality board is hardcoded, not measured.
- docs/en.md evaluation / pitfalls / package：MOS and automatic predictors assess different quantities; ASR CER and SECS remain proxies. Sample-rate mismatch does not by itself establish aliasing; source warning retained. No quiz/tests/learning-objectives section. SVG and figure protected; no audio recording, cloning or rendering performed.

源缺陷单列，不通过译文更改代码、数字、数学、URL、模型名、图示载荷或技术断言。原 strict 控件不改；尚无正文，本课 strict pending，不运行空稿检查。

课程 main/import/tests、CPU/GPU/模型、API/网络/下载/安装、签名、GFM/网站/PDF/累计回归均 NOT_RUN。正式141与实际141仅为准备时已核快照，不覆盖本课。发布时刻和 commit 由真实外部回读证据记载，不预填。
