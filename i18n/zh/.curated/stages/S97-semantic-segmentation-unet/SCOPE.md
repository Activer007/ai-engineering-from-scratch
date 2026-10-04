# S97-semantic-segmentation-unet English-first 支持范围

状态：本地check-only own3候选，未安装、未发布，不增加正式课程数。三课可分别推进；准备/新译只依赖固定英文与术语，不要求先修中文正式验收。

## 固定英文与唯一目标

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Source tree: `3d90647a3449a7b228a6b6025ed2b333ef99e81c`
- Lesson: 04-07
- Canonical docs H1: Semantic Segmentation — U-Net
- Source: `phases/04-computer-vision/07-semantic-segmentation-unet/docs/en.md`
- Source Git blob: `6739f33a49e8a26e66f6dd8311c403e06fad9309`
- Source SHA256: `7c1b00723a204bfc263ea5c3c3219b04b1549a7d2fc7e3297a4a6611609e54f1`
- Target: `i18n/zh/phases/04-computer-vision/07-semantic-segmentation-unet/docs/zh.md`
- Eventual record: `i18n/zh/.curated/lessons/04-07/translation.json`
- Original core blocks: 159
- English prerequisite line: **Prerequisites:** Phase 4 Lesson 03 (CNNs), Phase 4 Lesson 04 (Image Classification)
- Actual first write UTC: 2026-10-04T11:14:21.555044Z through 2026-10-04T11:14:21.555455Z
- First-write receipt SHA256: `1850d07c8b337d160fce14d3d3ade48f85e0aed0e8092b933b59ee005018f0fa`
- Original complete first draft: 19511 bytes, SHA256 `b36b4a8ea34b2447f3d4dc966ae97193ef1d1ed69fa0938d91b6665718ab147c`

首写按原回执与原字节核对，不以mtime重建，不倒推为当时独审/完整绑定通过。完整课程源身份见DEPENDENCIES.source_files；题名按docs H1，不用quiz短标题覆盖。

## 固定支持与当前溯源

共同清单SHA256 `aa1ce658c805ba06f4b25859601ecd36f9bd3cdd622d075d7a56b360d295d8b6`；103common原路径、顺序、commit、blob、SHA、字节数、模式及历史role/classification保持。95 TERM与8controls分计；own3仅本阶段DEPENDENCIES.json、SCOPE.md、TERMINOLOGY.md三文件，未来安装后总106，本准备未安装。target/record/兄弟阶段不进入own3。

当前as-of：2026-10-04T12:19:14.262484+00:00，正式已审草稿112；INDEX commit `d138d2c621b50d6a7f5a40eb370a5cd9da7951df`、SHA256 `f78d53ea04f46c02e4ee8b8710f089305aa432634c41b380135716cd8ee582be`；独立回读凭据SHA256 `87e4542bd4c8ba608e563adc74782ce49c1ed1c29e31d711f0bcb9d7ee834207`。最新实际批次仍111，覆盖S88/S93/S91；S96及本课不受该批次覆盖。112仅作本次溯源，不改作者首写及共同清单107/108历史，也不重分类旧pin标签。

保留schema_version=1、DEPENDENCIES version=1、原f9 core与既有S07/S19精确控制，不新增schema、loader、checker例外或发布框架。files/support_pins完整103，reference_glossary_pins仅95；own3 hash由外部manifest固定，无自引用。原33 fixture仅复用固定身份，不读其中文body/segments、不装作者目录；不重跑33/24/50或全源审计。

## 已有证据与待处理

独立语言审未在本支持准备中复核；引用作者原core静态PASS，source-format pending另列。

- Source-format pending：固定英文 Key Terms 的 Dice loss 行含六个未转义竖线；已保存真实 GitHub GFM DOM 的第三单元格只剩 `1 - 2`，后续公式与说明被截断。保留源数学和现行 strict，不新增 checker 例外，不改公式，不宣称本课 GFM 完整性通过。仅挂起本课，不阻塞 S98/S99。
- 转置卷积学习目标与实际 bilinear Upsample、必须整除16与插值适配、文档与 main 合成数据、Dice epsilon 和 IoU 聚合均有源内差异。quiz kernel/stride 解释矛盾、五题且无原 tests，均不在翻译中修补。
- 无相对 SVG；Mermaid 和 figure 载荷保持。base2/eval/no_grad 的有界 CPU 方案仅为提案，无 GO、未执行；不运行训练 main、GPU、下载或安装。

## 核验与发布边界

本准备只做必要静态字节、模式、JSON、首写绑定以及固定英文Git pin核对；共同commit身份复用冻结清单，本轮定向核本地支持字节/模式，不声称所有共同commit均从本地对象重新解析。没有课程main/tests/AST、训练、GPU、下载、安装、网络、CI、GFM/site/mobile/book执行。已有语言或core PASS不扩充为这些通过声明。

只生成候选，不写作者、原支持、INDEX、queue、英文源或远端。建议分支 `zh/stage-97-semantic-segmentation-unet` 仅为名字，未联网查询或创建。publication pending/null为冻结时状态；实际后续发布须用提交及外部独立字节回读绑定，不虚构SHA。
