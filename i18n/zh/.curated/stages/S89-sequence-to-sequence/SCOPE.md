# S89-sequence-to-sequence English-first 支持范围

状态：冻结时的预发布支持快照，精确字节冻结由协调者回执证明。三位作者已在独立范围中新写正文；本支持文件不声称启动作者、译文验收或正式新增课，也不以S85正式106作为门禁。

## 固定英文与唯一目标

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Lesson: `05-09`
- Canonical docs H1: Sequence-to-Sequence Models
- Source: `phases/05-nlp-foundations-to-advanced/09-sequence-to-sequence/docs/en.md`
- Source Git blob: `9b9c4c83f923c5ec83d562c2667c2d81cfbfcc5d`
- Source SHA256: `83d570d30ef505439edbbe90a16c984e6c5e552468ed53a54919b36d2dd43d49`
- Target: `i18n/zh/phases/05-nlp-foundations-to-advanced/09-sequence-to-sequence/docs/zh.md`
- Eventual record: `i18n/zh/.curated/lessons/05-09/translation.json`
- Original core blocks: 101
- English prerequisite line: **Prerequisites:** Phase 5 · 08 (CNNs + RNNs for Text), Phase 3 · 11 (PyTorch Intro)

课程完整固定输入清单见同目录 DEPENDENCIES.json.source_files；学习先修只提供上下文，不要求上游中文正式验收。规范课题来自真实docs H1，不以quiz.title替换。

## 参考术语和原控制

正式基线 `86ba1f188074b2a26acdd60345e8c31d74c181ea` 保持105课。94个唯一支持输入由85份正式TERM＋1份active-reviewed S85 TERM＋8原controls组成。S85尚未在此基线正式接受；仅复用其已审术语。旧91的每条commit/blob/bytes/SHA256均从固定Git对象重核，新增S85/S86/S87三条TERM，实际集合无重复。reference_glossary_pins只含86词表；support_pins含94；本课自身3支持文件另计。publication.commit=null保存冻结时的历史状态，不是公开后的当前发表状态，也不自引用本文件Git提交。实际发布commit由后续作者record与远端回读receipt绑定，不伪造SHA。

原f9 core、S07/S19控制和33/24/50套件一字不改；无新增checker例外。原33三文件只作独立测试夹具，绝不进入作者支持或正文阅读范围。任何新原33运行必须在新tmp副本补.git，仅只读固定对象；共享缺.git夹具及旧15 errors原始日志保持，不覆盖、不粉饰。

## 保护与已知源边界

- docs H1 and quiz title are Sequence-to-Sequence Models. Preserve the real source title and source section set; no invented Learning Objectives.
- Main is a stdlib fixed-context toy simulation; epochs and n_train are unused. It does not train a GRU, implement teacher forcing/beam search, or run BART.
- Eight source quiz questions remain unchanged; no quiz normalization. An unlinked assets/seq2seq.svg remains source-only, with no invented translated asset or link.
- Source b0061 (lines 131–136) has a bare output fence. Coordinator has separately authorized opening-only ``` to ```text under the original core contract; payload and closing fence remain exact. This is not a checker exception.
- Do not execute original main, PyTorch examples, transformers.from_pretrained, training, checkpoint downloads or installation. Static checks are not model-performance reproduction.

## 组装和验证权限

按原core schema_version=1和真实blocks生成segment，保留separator、原英文heading_path、非separator ordinal及各块source hash，拼接target精确对应译稿字节。此文件不扩展作者权限；record写入最终位置由协调者明确许可。provenance记录本次真实日期和已知运行事实，不复制capture硬编码历史日期。

仅原裸围栏可补text tag，载荷/结束围栏不变并留痕；代码、数学、Mermaid/figure/SVG、提示词、路径/URL、原元数据及源问题不得暗修。不得读旧中文正文、segments、format_revisions；不得改英文、shared TERM、原controls、INDEX/queue/claims、其他课程或远端。本支持文件本身不授权source/runtime/training/install/network；如有另外的明确授权和实际运行，其权限及结果以对应独立记录为准。

后续原core静态check、两份不同新目录replay、独立技术与中文语言审校、实际GFM及原33/24/50各自记录。parser PASS不是GFM、CI、site/mobile/book或正式验收；本支持文件不宣称任何运行或视觉PASS；另行实际执行的结果须独立留证。
