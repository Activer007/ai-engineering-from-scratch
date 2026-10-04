# S103-image-generation-gans English-first 支持范围

状态：本地check-only own3候选，未安装、未发布，不增加正式课程数。当前独立技术/中文语言PASS只绑定以下版本，不代替支持安装、真实GFM、远端最终字节核验及适用批次回归。

## 固定英文与唯一目标

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Source tree: `3d90647a3449a7b228a6b6025ed2b333ef99e81c`
- Lesson: 04-09
- Canonical docs H1: Image Generation — GANs
- Source: `phases/04-computer-vision/09-image-generation-gans/docs/en.md`
- Source Git blob: `895b3b1a6611efe90aa1d1091aebe2fb5a82a361`
- Source SHA256: `dcdc65b519fc2a23620cde11212f4d3269b63bd52d568d72ef08c04867c33409`
- Target: `i18n/zh/phases/04-computer-vision/09-image-generation-gans/docs/zh.md`
- Eventual record: `i18n/zh/.curated/lessons/04-09/translation.json`
- Original core blocks: 139
- English prerequisite line: **Prerequisites:** Phase 4 Lesson 03 (CNNs), Phase 3 Lesson 06 (Optimizers), Phase 3 Lesson 07 (Regularization)
- Actual first write UTC: 2026-10-04T13:13:29.216940+00:00 through 2026-10-04T13:13:29.217056+00:00
- First-write receipt SHA256: `a73e1f056da390581579bd3f1ea7f373ad1ea12c6db16ed36beed33c0f6f9aba`
- Original complete first draft: 15828 bytes, SHA256 `bc3b69e5b016f6119c22156a42d9cf30adf65718e1c282c2c6fecb434ba642b3`
- Current reviewed target: 16048 bytes, SHA256 `b9751fb5b549beba2e065ab8e7d7d06bea0f53b736c8239477b858df9e88c17c`
- Current draft record SHA256: `744f31ccce9ec6458b84cbbe8be2c17794d51473bc948896337750fb09f965f4`
- Independent language review SHA256: `02cc9ff684c7dea18bc8b2cc023f2f8ed10a8e7a1f003764b129a6cde9d7f3e0`
- Existing local strict receipt SHA256: `44bd37299f9d5b8ad5fad3b0ee0914182b66356fe89afe214c7d86e5d53d9e91`

首写以原回执和原字节为准，不用mtime重建，不倒推为当时独审或own3已通过。本课源文件见DEPENDENCIES.source_files；先修固定英文已定位，无先修中文formal门禁。

## 固定支持与当前溯源

共同准备清单SHA256 `7db275332617ab8b0b74dd3553c3b9a5fa55af88e3425f775a3ad2ad14c975be`。files/support_pins为有记录的公开投影，保留common106原顺序、公共身份与历史role/classification，并非原内部对象逐字段完全相等；仅去除S97–S99条目的6个私有路径定位值，保留其receipt SHA256。reference_glossary_pins为98 TERM，另8 controls；own3只含本阶段DEPENDENCIES.json、SCOPE.md、TERMINOLOGY.md，总109。正文、record、兄弟阶段及图资产均不算own3。旧已核Git身份复用，不重写历史类别或首写时点。

当前as-of使用正式独立回读真实时间2026-10-04T13:35:00.058967+00:00：正式已审草稿116，INDEX commit `87aefb26c69dfc70159c408dadb77b99fafb5767`、SHA256 `af432e0712968b91ad367649d22e161548e1a5da896018173913b0491fada8b4`；独立回读SHA256 `5e7989b5964153a704bbf591e710565e67d2993d287060ce10f164e77f7a3d39`。最新actual114只新增覆盖S96/S92/S94，不覆盖S103/S104/S105；本课所属批次待运行，不继承历史PASS。

保留record schema_version=1、DEPENDENCIES version=1及原f9 core/S07/S19精确控制。own3 hash由外部manifest固定，无自引用，不新增builder/checker/audit框架或重分类表。原33 fixture只复用既有固定身份，不读取其旧中文正文或执行回归。

## 已有证据与实际限制

- Step 1正文称四层均stride2/padding1，首层代码实际stride1/padding0；两者分别保留，不静默修正源含义。
- SN helper缺少Discriminator.forward的展平包装；替换后的返回形状、1-Lipschitz保证和通常无需TTUR均未运行验证。谱归一化技术与矩阵谱范数标量分开。
- beta1的博弈解释与quiz惯性说明有表达张力；docs采样未恢复G.train()而main会恢复；两常用库/三项目计数、历史与2026/SOTA断言均不背书。
- 固定quiz五题（2pre/3post），无check及lesson/title；没有code/tests。两处裸围栏仅补text，11围栏载荷保留；无linked SVG。
- 旧离线renderer识别1表、8代码块、2Mermaid、1figure及14个纯中文空锚点，BLOCKED_SOURCE_RENDERER不是实际GFM失败或通过；真实页面待查。
- 有限CPU提案仅为stdlib静态AST及标量形状算术，单进程≤5秒；NOT_RUN，未获GO，不import课程、不建模型/forward/训练/采样/下载/安装/GPU。

S103历史绑定保留：初版HANDOFF正文SHA256 `9cb3fa499da1e7d5c399bfc0bad43d7bd1a3f261aba20a11e34d70d62be6ff19`、record SHA256 `1658398e57b6126fc1c8eb1d97f5d845dd1b7bf8b7bdb384704b5f285f0a409e`，原REQUEST_CHANGES报告SHA256 `3eb3cdd7136223a628f6dbe0b26fd96bec93fcd66a4a117cb03e059215080a24`不覆盖。revision-03仅补scaffold首现；当前依据是上列新body/record及revision-03独立追认。校准文件中的旧target hash是历史快照，不追写。

## 核验与发布边界

本准备仅核新候选JSON/字节/hash、当前作者/首写绑定、本三课17个源文件及7个先修英文的必要Git pin；复用98TERM校准与既有common身份。S85–S96历史commit:path在原准备对象库缺失的限制保留，未fetch、未补造。没有全源扫描、课程执行/import、main/tests/模型/训练/GPU、安装/下载、实际GFM/site/mobile/PDF/CI或全库回归。

只生成候选，不写作者、英文源、原支持、INDEX、queue或远端。publication pending/null是冻结时点的状态；后续发布须另有真实commit及独立完整字节回读。语言PASS和静态核对不代表本课已正式登记、运行或批次通过。
