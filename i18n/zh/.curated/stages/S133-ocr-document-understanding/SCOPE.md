# S133-ocr-document-understanding English-first 支持范围

准备时刻：2026-10-04T23:07:00.341253+00:00。状态：正文起草前 own3 本地候选，尚未发布或安装 own3。课程 04-19，OCR & Document Understanding；固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb。common136 =128 TERM +8 controls；本课 own3 独立计数，完整支持集合拟为139，不增加正式课程数。

## 已固定范围

仅计划翻译 phases/04-computer-vision/19-ocr-document-understanding/docs/en.md 至 i18n/zh/phases/04-computer-vision/19-ocr-document-understanding/docs/zh.md。完整静态阅读本课全部 5 个英文包文件；必要英文先修的本次全文阅读和精确旧全文阅读复用逐项写在 DEPENDENCIES.json，包含路径、SHA、Git blob、字节数和复用证据。源先修原文：**Prerequisites:** Phase 4 Lesson 06 (Detection), Phase 7 Lesson 02 (Self-Attention)。先修依据固定英文与相关术语，不要求先修中文正式验收。

common136 只追加已发布并独核的 S127、S128、S129 TERM；未纳入 S130–S132 TERM。S117 沿真实修订 ff4d56e72126e854321b5d95a7c43a8b57a485bf / 6631ae3d6b514d374a63bd21afa98eaedeb995e2aeed3e664e037e6de6ea0c85。common 集合 SHA256：8e508ca2b84d6b40df38b3377e1946deadd0138fd55b359f9c8503a736b03fec。原身份、顺序、角色和分类保持；公开投影不包含本地定位信息。

## 待发生事实

作者未开始，首写、首稿、capture、record、修订、strict、完整英文技术对照和另次中文通读全部 pending。对应时间、hash、字节数为 null，修订列表为空。本候选不冒充作者提案或独审。后续首写/独审真实历史进入 review；若词表改变，另发真实支持增量，保留当前冻结证据。

## 固定英文源风险

- docs/en.md synthetic_line/training; code/main.py：All alphanumeric characters produce identical rectangles; equal-length strings are visually indistinguishable. Claimed loss drop and character recognition are not established. Height32 pools to2 before mean, unlike max-pools-to1 prose.
- docs/en.md layout/model descriptions：LayoutLMv3, DocLayNet and Donut are grouped under simplified or mismatched model/input descriptions. Fixed2026/default/best/CER assertions are retained and unverified.
- outputs/skill-ctc-decoder.md：Skill promises length normalisation but uses raw log-probability scoring. No input guards; beam-width and accuracy claims not verified by execution.
- quiz.json/package：Five questions(2pre/3post), missing lesson/title and tests. Protected Mermaid/figure, code/numbers/URLs remain unchanged; external OCR packages and pretrained downloads not run.

源缺陷单列，不通过译文更改代码、数字、数学、URL、模型名、图示载荷或技术断言。原 strict 控件不改；尚无正文，本课 strict pending，不运行空稿检查。

课程 main/import/tests、CPU/GPU/模型、API/网络/下载/安装、签名、GFM/网站/PDF/累计回归均 NOT_RUN。正式141与实际141仅为准备时已核快照，不覆盖本课。发布时刻和 commit 由真实外部回读证据记载，不预填。
