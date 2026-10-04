# S101-question-answering English-first 支持范围

状态：本地 check-only own3 候选，未安装、未发布，不增加正式课程数。当前正文已有独立完整技术/中文语言 PASS；该结论只绑定下列正文版本，不代替支持安装、真实 GFM、远端字节核验或适用批次回归。

## 固定英文与唯一目标

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Source tree: `3d90647a3449a7b228a6b6025ed2b333ef99e81c`
- Lesson: 05-13
- Canonical docs H1: Question Answering Systems
- Source: `phases/05-nlp-foundations-to-advanced/13-question-answering/docs/en.md`
- Source Git blob: `85944817ddc3d40d9103aa260ede61764eb8b348`
- Source SHA256: `0fcd3cb8c48f9b9f0a1597958ed41da266022394329bd44bf1c29eae8453d7f9`
- Target: `i18n/zh/phases/05-nlp-foundations-to-advanced/13-question-answering/docs/zh.md`
- Eventual record: `i18n/zh/.curated/lessons/05-13/translation.json`
- Original core blocks: 93
- English prerequisite line: **Prerequisites:** Phase 5 · 11 (Machine Translation), Phase 5 · 10 (Attention Mechanism)
- Actual first write UTC: 2026-10-04T12:37:02.295599+00:00 through 2026-10-04T12:37:02.295917+00:00
- First-write receipt SHA256: `a160ed0a6fec0e5206abdcc616aff71d09c219e04706a1ba4426a79ebcaaddbc`
- Original complete first draft: 12285 bytes, SHA256 `8a42f5154954fb991635657083c1412150f1ddacf09077ccbf0b88d091ed6a39`
- Current reviewed target: 12325 bytes, SHA256 `19a9231ff23a87ae3c43e34366dbde07bada1cf69c7023e4b7de2ac5799c24f7`
- Current draft record SHA256: `1bd7788f1609100872b34aef88553a6a150c44a300f42e3041a5c1be92732cc1`
- Independent language review SHA256: `25445c944510c999dc8558ec62af856bff62a942b004be737df8b94f2e93eb03`
- Existing local strict receipt SHA256: `b02b4cdcecaa331dd5d6a0f76b89652c6a08397dac509b26ac78fb7fff4fbae7`

首写按原回执和原字节核对，不用 mtime 重建，不倒推为当时独审或完整支持绑定已经通过。本课包源身份见 DEPENDENCIES.source_files；先修英文为 05-11, 05-10，没有先修中文 formal 门禁。

## 固定支持与当前溯源

共同准备清单 SHA256 `77791cbf3d18671859db330f107b2d64fcb138a37287707ad51bd1a360718d82`，引用原103 pin清单 SHA256 `aa1ce658c805ba06f4b25859601ecd36f9bd3cdd622d075d7a56b360d295d8b6`。files/support_pins保留原103全部身份和顺序，reference_glossary_pins仅95 TERM；8 controls、own3分计。own3只含本阶段 DEPENDENCIES.json、SCOPE.md、TERMINOLOGY.md；未来安装后总106。target/record、兄弟阶段和非支持资产不进入own3。保持历史role/classification，不复制后续共同清单的新归类。

当前as-of采用正式独立回读真实时间 2026-10-04T12:55:32.520157+00:00：正式已审草稿114，INDEX commit `19db65d17eca63e7716fe5e10028bf82fa44c309`、SHA256 `332a1eb6a5a5003b78940290084f7337a3a9fa5afd5f76c63f26c86f26f2c17f`；独立回读凭据 SHA256 `cb33fc7a548110448fbe1ef68027657482f4a22ac04a43495d25907ed49c2fcd`。最新实际批次114只新增覆盖 S96/S92/S94，不覆盖 S100/S101/S102；本课适用批次仍待运行。当前溯源不改作者首写、共同准备113或原pin清单107/108的历史时点。

保留 schema_version=1、DEPENDENCIES version=1、原 f9 core及既有 S07/S19 精确控制，不新增 loader、checker 例外、发布框架或 current-support 重分类表。own3 hash由外部manifest固定，无自引用。原33 fixture仅复用固定身份，不读其中文body/segments、不安装到作者目录、不重跑33/24/50。

## 已有证据与实际限制

- 开头“抽取式绝不产生幻觉/不能处理无答案问题”与 SQuAD 2.0 空答案段落及 SVG 例外有源内张力；复制片段不等于回答正确
- 源示例 start=57/end=70 与日期字面位置不一致；40-60% 降幅无本课实验支持。输出与数字保持，未冒称实测
- 引文字符串匹配不独立证明蕴含；RAGAS 2026 默认地位、四维全部无参考、统一 NLI 与四标量等是未版本化源断言，未外部核实
- checked-in main 是 stdlib 玩具词法检索/EM/token-F1，与正文预训练稠密模型管线不同；quiz 八题、没有 code/tests，未补写或运行
- 原样 qa.svg 为 5192 bytes、SHA256 `b6fc27d780cf9a26eab8c264599bf14cec37834bbd519183976c0471bb8588f6`；单列非支持资产，不加入 own3/common103。自定义 qa-span figure 与 SVG 分开，真实 GFM尚待检查
- 固定字符串 normalize/exact_match/token_f1/toy_retrieve 与 offset CPU 方案仅为提案：NOT_RUN；不导入或执行 main，不运行模型片段，不安装/联网/下载/GPU

## 核验与发布边界

本准备只做新候选JSON/字节/hash、当前作者绑定/首写原字节、17个本课包文件及6个先修英文必要Git pin核对；95术语表校准与原共同commit身份复用固定证据，不宣称本轮再次解析全部共同commit。S85–S96 commit:path在准备时对象库不可解析的既有限制保留，未联网补取。没有全源5423扫描，没有课程运行、模型、main/tests、下载、安装、GFM/site/mobile/book/CI或回归执行。

只生成候选，不写作者、原支持、英文源、INDEX、queue或远端。建议分支 `zh/stage-101-question-answering` 仅为名称，未查或创建。publication pending/null仅表示冻结时未发布；后续发布须绑定真实提交及独立完整字节回读。语言PASS、静态PASS和正式114背景均不转化为本候选的发布或批次通过。
