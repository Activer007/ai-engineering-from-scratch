# S91-transfer-learning English-first 支持范围

状态：本地完整候选，未安装；精确冻结须协调者确认。本文件不启动或验收作者、不授权修改正文record、不授权远端发布。正式基线106与所有本轮draft状态严格分开。

## 固定英文与唯一目标

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Source root tree: `3d90647a3449a7b228a6b6025ed2b333ef99e81c`
- Lesson: `04-05`
- Canonical docs H1: Transfer Learning & Fine-Tuning
- Source: `phases/04-computer-vision/05-transfer-learning/docs/en.md`
- Source Git blob: `f4bf74621dc404e341d933eea1895287f56164ac`
- Source SHA256: `670f74b6d6cc2d6d61d56c868c50c482b9cd77fd3580dc427902dee9666c60a5`
- Target: `i18n/zh/phases/04-computer-vision/05-transfer-learning/docs/zh.md`
- Eventual record: `i18n/zh/.curated/lessons/04-05/translation.json`
- Original core blocks: 149
- English prerequisite line: **Prerequisites:** Phase 4 Lesson 03 (CNNs), Phase 4 Lesson 04 (Image Classification)
- Actual first substantive write UTC (author receipt): 2026-10-04T08:08:00.650462+00:00
- First-write receipt SHA256: f807fdd6c80f073da0f521e2c2ce059afd65f68c13ad7d87896d362ee3320e22

完整固定课程输入见 DEPENDENCIES.json.source_files。英语先修仅用于学习上下文，不以中文正式验收为门禁。规范课题来自docs H1，不以quiz.title替换。first-write日期来自作者实际回执元数据，不从本文件生成时间或稿件mtime重构；支持准备没有读取稿件快照正文。

## 参考术语和原控制

正式INDEX `5f141d89c43b37f87caa05c037e8c71580b8ff7a`，SHA256 `0341f3a9425449d3bce93d88985afd55a5945de56bd4700a208004e093bfe467`，独立回读proof SHA256 `7537cf07210ced9b1aa85745bcf08c61639996abdc250ea45639b9388a9b8e83`，确认106课。97唯一common输入为86正式TERM＋3 active-reviewed S88/S89/S90 TERM＋8原controls；reference_glossary_pins只含89词表，support_pins和DEPENDENCIES.files均为相同97集合。本课own3另计100。S85现为正式accepted；其旧固定TERM来源及全部原字节不变，旧支持内105/active叙述是冻结时历史，不覆盖当前106状态。新draft不计正式接受。

core/f9、原test/check脚本及S07/S19八个controls byte-identical；schema_version=1，不扩展schema、不添加checker例外。原33三个fixture只列独立测试用途，不读取其旧正文/segments，不安装进作者根目录；原33/24/50套件和历史日志不改、不删除。现有94已逐项读回一致，新增3TERM及本课own3仍待精确GO，不能推断安装完成。

support_publication的pending/null是预发布冻结快照，非永久未发布状态，也不自指当前文件commit。实际后续发布commit须从外部record/远端回读绑定；未知时不得造SHA。历史不删除。

## 保护与已知源边界

- Five fixed course files; no source tests or SVG asset. Quiz has five questions (pre2/post3), no lesson/title fields; do not normalize its schema or invent source tests.
- Source BN Step4 says without freezing weights, while code freezes affine parameters as well as running statistics. Frozen parameters do not freeze BN buffers. Keep prose/code/inspector disagreements independently; no silent repair.
- Docs parameter-group function and main differ in requires_grad filtering. Progressive-unfreezing helper is docs-only and leaves the stem frozen; cached optimizer moments are not wall-clock moments.
- Source calls a learned linear head zero-shot and treats worse fine-tuning as a guaranteed training bug. Preserve the source claim, but do not report it as demonstrated or universal evidence.
- GPU-hours, transfer percentages, CIFAR accuracy claims and synthetic demo settings are separate source statements. No training, download, GPU, pretrained-weight loading, package installation or main execution occurs in support preparation.
- Planner first-match coverage makes its edge-compute rule unreachable for declared valid size/domain inputs; undeclared compute_gpu_hours and closed/half-open endpoint differences remain unchanged.
- Only three naked doc-fence opening tags may become text under the original preservation rule; every payload/closing fence stays exact. Original outputs remain untranslated and unchanged.

## 组装和验证边界

原core每个blocks含separator各有一个segment；heading_path保留原英文heading stack，ordinal仅对非separator递增；source hash取精确块，拼接target须复原完整目标字节。core词表及可选addendum成对绑定，89参考词表与97全支持不可混用。本课3支持文件精确hash由外部冻结/安装回执绑定，禁止自引用依赖清单hash。provenance使用本轮真实时间及已知事实，不能复制capture硬编码历史日期。

本支持准备只静态读取英文、术语、控制、作者术语提案和源风险及回执元数据。docs/i18n.md既有中文规范例子的必要暴露已记录且未复用。未读旧中文正文/segments/format_revisions或452/457；未改作者正文record、英文、shared TERM、controls、INDEX/queue、其他课程或远端。

本地支持字节校验不是独立技术/中文审校、实际GFM、CI、site/mobile/book、课程运行或正式验收。后续check/replay/评审各自依具体授权和精确字节重新绑定，不从支持候选推断PASS。本文件不授予训练/GPU/download/install/network、生产操作、原课程main或测试执行权限。
