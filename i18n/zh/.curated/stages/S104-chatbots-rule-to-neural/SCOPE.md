# S104-chatbots-rule-to-neural English-first 支持范围

状态：本地check-only own3候选，未安装、未发布，不增加正式课程数。当前独立技术/中文语言PASS只绑定以下版本，不代替支持安装、真实GFM、远端最终字节核验及适用批次回归。

## 固定英文与唯一目标

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Source tree: `3d90647a3449a7b228a6b6025ed2b333ef99e81c`
- Lesson: 05-17
- Canonical docs H1: Chatbots — Rule-Based to Neural to LLM Agents
- Source: `phases/05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural/docs/en.md`
- Source Git blob: `fa1dbf927bb05bde8abb25ff782a026b5440d7e4`
- Source SHA256: `2ef49d5cdfcc8229bfe5ee7b1954de73ab30ad64711e53997efc9cca59ba25f0`
- Target: `i18n/zh/phases/05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural/docs/zh.md`
- Eventual record: `i18n/zh/.curated/lessons/05-17/translation.json`
- Original core blocks: 121
- English prerequisite line: **Prerequisites:** Phase 5 · 13 (Question Answering), Phase 5 · 14 (Information Retrieval)
- Actual first write UTC: 2026-10-04T13:15:57.356511+00:00 through 2026-10-04T13:15:57.356793+00:00
- First-write receipt SHA256: `b84bef90aeeb7673a04fdde5596c9cc4f5bdae9c53442e76f4789e12cc01d8d6`
- Original complete first draft: 19805 bytes, SHA256 `ed139baf91d960115b7d7b50a3afcc73896f4052d47da87619bef3d1236044f3`
- Current reviewed target: 19821 bytes, SHA256 `6ac5d70c27878f1f8d33c40b576d062cf0473181da855d3879c59d366db4b089`
- Current draft record SHA256: `eabd9e0d79b029c66366716edda2a0e2cae8fbc7ab9508da60bda284ac3ba8b0`
- Independent language review SHA256: `7272cdb3a0d25fc34490ef144b9edb1e7319f7337476e16284c1b6c92e121314`
- Existing local strict receipt SHA256: `ccc9ba9b3cff6f43a6dcf1d6ded6cd7f466c60b602133c3065771f4c36d02520`

首写以原回执和原字节为准，不用mtime重建，不倒推为当时独审或own3已通过。本课源文件见DEPENDENCIES.source_files；先修固定英文已定位，无先修中文formal门禁。

## 固定支持与当前溯源

共同准备清单SHA256 `7db275332617ab8b0b74dd3553c3b9a5fa55af88e3425f775a3ad2ad14c975be`。files/support_pins为有记录的公开投影，保留common106原顺序、公共身份与历史role/classification，并非原内部对象逐字段完全相等；仅去除S97–S99条目的6个私有路径定位值，保留其receipt SHA256。reference_glossary_pins为98 TERM，另8 controls；own3只含本阶段DEPENDENCIES.json、SCOPE.md、TERMINOLOGY.md，总109。正文、record、兄弟阶段及图资产均不算own3。旧已核Git身份复用，不重写历史类别或首写时点。

当前as-of使用正式独立回读真实时间2026-10-04T13:35:00.058967+00:00：正式已审草稿116，INDEX commit `87aefb26c69dfc70159c408dadb77b99fafb5767`、SHA256 `af432e0712968b91ad367649d22e161548e1a5da896018173913b0491fada8b4`；独立回读SHA256 `5e7989b5964153a704bbf591e710565e67d2993d287060ce10f164e77f7a3d39`。最新actual114只新增覆盖S96/S92/S94，不覆盖S103/S104/S105；本课所属批次待运行，不继承历史PASS。

保留record schema_version=1、DEPENDENCIES version=1及原f9 core/S07/S19精确控制。own3 hash由外部manifest固定，无自引用，不新增builder/checker/audit框架或重分类表。原33 fixture只复用既有固定身份，不读取其旧中文正文或执行回归。

## 已有证据与实际限制

- 目录rule-to-neural不缩小实际H1的LLM Agents范围；规则式、检索式、神经生成、LLM智能体四范式、混合路由、历史及安全段均保留。四范式不是互斥技术分类；最后两种混合与四路并用的源内张力未调和。
- 检索没有幻觉、RAG避免幻觉、PVE阻止计划外操作属于源保证；历史数字、攻击率/CVE/CVSS及2026生产概括未外部事实核验或安全验证。
- main为stdlib Jaccard/0.3/二元组和LLM文本占位；正文是sentence-transformers/0.5、混合路由0.6及transformers/FLAN-T5示意。不得将main当作真实模型或语义检索验证。
- 有限循环只校验工具名及参数字典；关键词路由和未定义变量不构成生产确认/PVE/授权层。未调用工具、API或执行示意操作。
- quiz八题（2pre/3check/3post），无code/tests及Learning Objectives；不补造章节、测试或题目。chatbot.svg与chatbot-lineage figure是不同渲染面。
- 有限CPU提案仅为后续获GO后临时副本的stdlib main、单CPU≤5秒；NOT_RUN。固定输入断言亦需另行批准；禁真实工具回调、模型/API/网络/安装/下载/GPU。

原样linked SVG另计：`i18n/zh/phases/05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural/assets/chatbot.svg`，4365 bytes，SHA256 `ae97cf97765cc8426d8d8c6db88b9660f0911fb254dde8d3679a98d9951547b1`；不纳入common106或own3。

## 核验与发布边界

本准备仅核新候选JSON/字节/hash、当前作者/首写绑定、本三课17个源文件及7个先修英文的必要Git pin；复用98TERM校准与既有common身份。S85–S96历史commit:path在原准备对象库缺失的限制保留，未fetch、未补造。没有全源扫描、课程执行/import、main/tests/模型/训练/GPU、安装/下载、实际GFM/site/mobile/PDF/CI或全库回归。

只生成候选，不写作者、英文源、原支持、INDEX、queue或远端。publication pending/null是冻结时点的状态；后续发布须另有真实commit及独立完整字节回读。语言PASS和静态核对不代表本课已正式登记、运行或批次通过。
