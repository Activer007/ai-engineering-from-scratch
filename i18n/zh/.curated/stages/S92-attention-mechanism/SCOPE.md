# S92-attention-mechanism English-first 支持范围

状态：本地完整候选，未安装；精确冻结须协调者确认。本文件不启动或验收作者、不授权修改正文record、不授权远端发布。正式基线106与所有本轮draft状态严格分开。

## 固定英文与唯一目标

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Source root tree: `3d90647a3449a7b228a6b6025ed2b333ef99e81c`
- Lesson: `05-10`
- Canonical docs H1: Attention Mechanism — The Breakthrough
- Source: `phases/05-nlp-foundations-to-advanced/10-attention-mechanism/docs/en.md`
- Source Git blob: `f05f25084408ea9017a268012811e2a91c20ac8d`
- Source SHA256: `f31dde76b3cd616e1c7d242a9d36fc4f5dd2c4a8514bd026da2d4b9e652ae49b`
- Target: `i18n/zh/phases/05-nlp-foundations-to-advanced/10-attention-mechanism/docs/zh.md`
- Eventual record: `i18n/zh/.curated/lessons/05-10/translation.json`
- Original core blocks: 113
- English prerequisite line: **Prerequisites:** Phase 5 · 09 (Sequence-to-Sequence Models)
- Actual first substantive write UTC (author receipt): 2026-10-04T08:21:40.248530+00:00
- First-write receipt SHA256: 894ba97cfc6d87580bffe767318722ba099040174d7ebb8c31a2b9c20707cddf

完整固定课程输入见 DEPENDENCIES.json.source_files。英语先修仅用于学习上下文，不以中文正式验收为门禁。规范课题来自docs H1，不以quiz.title替换。first-write日期来自作者实际回执元数据，不从本文件生成时间或稿件mtime重构；支持准备没有读取稿件快照正文。

## 参考术语和原控制

正式INDEX `5f141d89c43b37f87caa05c037e8c71580b8ff7a`，SHA256 `0341f3a9425449d3bce93d88985afd55a5945de56bd4700a208004e093bfe467`，独立回读proof SHA256 `7537cf07210ced9b1aa85745bcf08c61639996abdc250ea45639b9388a9b8e83`，确认106课。97唯一common输入为86正式TERM＋3 active-reviewed S88/S89/S90 TERM＋8原controls；reference_glossary_pins只含89词表，support_pins和DEPENDENCIES.files均为相同97集合。本课own3另计100。S85现为正式accepted；其旧固定TERM来源及全部原字节不变，旧支持内105/active叙述是冻结时历史，不覆盖当前106状态。新draft不计正式接受。

core/f9、原test/check脚本及S07/S19八个controls byte-identical；schema_version=1，不扩展schema、不添加checker例外。原33三个fixture只列独立测试用途，不读取其旧正文/segments，不安装进作者根目录；原33/24/50套件和历史日志不改、不删除。现有94已逐项读回一致，新增3TERM及本课own3仍待精确GO，不能推断安装完成。

support_publication的pending/null是预发布冻结快照，非永久未发布状态，也不自指当前文件commit。实际后续发布commit须从外部record/远端回读绑定；未知时不得造SHA。历史不删除。

## 保护与已知源边界

- Seven fixed files include two zero-byte .gitkeep files; no source tests. Eight-question quiz (pre2/check3/post3) and lack of Learning Objectives are preserved.
- Docs use NumPy/PyTorch, main is a stdlib dot/additive demonstration. Main does not implement the general form, training, GRU, batches, masking or multi-head attention. Exercise requests are not implemented capabilities.
- The 89%/length5/length80 cross-lesson claim differs from fixed 05-09 English numbers. General-attention code has four body lines despite the Three lines each statement. Preserve both sources; do not reconcile.
- d_s == d_h is dot attention's exact hard condition. Do not strengthen the nearby bidirectional-encoder heuristic into a new impossibility claim. Preserve Bahdanau s_{t-1}/Luong s_t timing and every axis/formula.
- Context reshapes each step describes changing content, not changing the fixed (d_h,) dimensionality. Score and normalized weight remain distinct. Raw weights alone are not evidence of reasoning; retain ablation/counterfactual caveat.
- Embedded prompt and output markdown differ. Preserve each original payload. Two naked output-fence openings may receive text only; source asset and all numerical statements remain exact.
- The unchanged English-labelled SVG has already been byte-copied by the author under prior explicit authorization. It is separate asset support, not translated prose, TERM or a counted common/own3 file. Its exact source/target/hash are below.
- Author-reported isolated main and supplementary stdlib checks are separate runtime evidence. This support preparation executes no course code and does not upgrade those checks into source-provided tests or full correctness.

### 单列的不翻译源资产

- Source: phases/05-nlp-foundations-to-advanced/10-attention-mechanism/assets/attention.svg
- Actual relative target: i18n/zh/phases/05-nlp-foundations-to-advanced/10-attention-mechanism/assets/attention.svg
- Git blob: dcf5b12c0b9464197add90bdf610356390fa07a5
- SHA256: abaad9e3a3b47e68928ee037a72d985826805a96610335cf3d2188dc745c306b
- Bytes: 4767; 原bytecopy已读回一致，SVG标签/几何均未翻译或改动。本支持准备没有执行资产复制，也不声称已做像素审校。

## 组装和验证边界

原core每个blocks含separator各有一个segment；heading_path保留原英文heading stack，ordinal仅对非separator递增；source hash取精确块，拼接target须复原完整目标字节。core词表及可选addendum成对绑定，89参考词表与97全支持不可混用。本课3支持文件精确hash由外部冻结/安装回执绑定，禁止自引用依赖清单hash。provenance使用本轮真实时间及已知事实，不能复制capture硬编码历史日期。

本支持准备只静态读取英文、术语、控制、作者术语提案和源风险及回执元数据。docs/i18n.md既有中文规范例子的必要暴露已记录且未复用。未读旧中文正文/segments/format_revisions或452/457；未改作者正文record、英文、shared TERM、controls、INDEX/queue、其他课程或远端。

本地支持字节校验不是独立技术/中文审校、实际GFM、CI、site/mobile/book、课程运行或正式验收。后续check/replay/评审各自依具体授权和精确字节重新绑定，不从支持候选推断PASS。本文件不授予训练/GPU/download/install/network、生产操作、原课程main或测试执行权限。
