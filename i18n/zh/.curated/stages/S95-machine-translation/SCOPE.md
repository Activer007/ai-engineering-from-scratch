# S95-machine-translation English-first 支持范围

状态：本地check-only候选，未安装、未发布。作者已真实正文起草；本支持准备不启动作者、不替代评审、不增加正式107。不能以先修中文是否正式接受作为准备/起草门禁。

## 固定英文与唯一目标

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Source tree: `3d90647a3449a7b228a6b6025ed2b333ef99e81c`
- Lesson: 05-11
- Canonical docs H1: Machine Translation
- Source: `phases/05-nlp-foundations-to-advanced/11-machine-translation/docs/en.md`
- Source Git blob: `8a100fe16e9e188700cb4b2901fca4c97ca464ff`
- Source SHA256: `956eeb576fdea61cef4a66b8f4c6b1b1caa47eea8e7488aace436c9c177b09ca`
- Target: `i18n/zh/phases/05-nlp-foundations-to-advanced/11-machine-translation/docs/zh.md`
- Eventual record: `i18n/zh/.curated/lessons/05-11/translation.json`
- Original core blocks: 95
- English prerequisite line: **Prerequisites:** Phase 5 · 10 (Attention Mechanism), Phase 5 · 04 (GloVe, FastText, Subword)
- Actual first write UTC: 2026-10-04T09:57:36.513196+00:00
- First-write receipt SHA256: f385d93bc4b9c0585d02c8a02e62b83a71585152564a7f5ede957a79df6a0a55
- First target: 275 bytes, partial opening only; SHA256 a1cc230f71e1033ba64c4116bc99b9a9682bec0524be60bd2329dc9ca9185bb7

完整课程输入为DEPENDENCIES.json.source_files，元数据/题名依docs H1，不由quiz缩短标题覆盖。首写时间来自原回执，原快照已核hash；不由mtime重构，也不拿草稿作为翻译记忆。

## 固定支持与历史

正式INDEX `0a1d387aec90759759d1bbb07bb4cd61c1f114a8`，SHA256 `7233acb6aeb253ae9812c7bc38a28bdf719d64f0fb4a7d4237eae02c5a20e8c2`，107课。全部100common已存在且原字节核验一致；本课own3仅候选，合计103。92参考TERM和8controls分别计数；正式87TERM（85accepted stage+core2），active-reviewed5为S88/S89/S91/S92/S93。保留S90旧TERM内106/active历史及原pin标签，通过独立current classification表标示已正式接受，不重写旧术语。

schema_version=1及原f9 core/S07/S19 controls保持，不扩展schema/loader/权限/CI。原33测试fixture仅独立测试元数据，不读取其中文body/segments、不装入作者目录；原33/24/50套件及日志未改。own stage仅DEPENDENCIES.json、SCOPE.md、TERMINOLOGY.md三条精确路径，不允许兄弟stage/target/record/asset混入。

publication pending/null仅freeze-time尚未发布快照，非永久未发布。实际后续commit必须外部record和远端回读绑定，不自引用当前文件、不造SHA。三个课程可分别准备/冻结/校验，互不等待先修中文验收。

## 源风险与运行边界

- 七份课程源含两个零字节.gitkeep，无原tests或Learning Objectives。quiz为八题（pre2/check3/post3），不补删结构。源H1为Machine Translation，不能补新副标题。
- main仅stdlib教学BLEU/chrF，不执行文档的NLLB、sacrebleu、COMET或训练管线。BLEU小写化、简化标点、单参考、无平滑；短于四token的完全相同句也可为零。chrF保留空格、按存在的阶数均值后计算beta=2，不保证sacrebleu等价。
- 原输出要求预计BLEU/chrF范围，不是实测分数；reference-free不授权伪造基于参考的指标。文档与独立output的提示词措辞不同，各自原样保留。
- 2026模型/指标默认、80%/20%、~80%、30/40/50 BLEU、under1 noise、BLEURT-QE及分词/训练API说明均为固定英语声明，未做时效/模型许可/质量背书。文档依赖超出allowlist，不在此安装。
- 英文SVG仅原字节副本，独立计数，不进入100common/own3/103。seq2seq-alignment共享figure为概念图，既有视口风险不冒称浏览器通过。
- 本课无源执行GO。本准备不运行main、模型、微调、评测库、语言识别、下载、GPU或网络推理；仅静态读取/解析。

原样SVG：phases/05-nlp-foundations-to-advanced/11-machine-translation/assets/mt-pipeline.svg → i18n/zh/phases/05-nlp-foundations-to-advanced/11-machine-translation/assets/mt-pipeline.svg；Git blob 73e2785ae5b59ba1064fc735b569b31c30f74ca3；SHA256 0f054ea22adce5d73dabe6375ebf7b9a6ce0b7c5720987751c03f3f7e27b079f；3189 bytes。源/目标已静态字节读回一致，无标签翻译、无像素验收；不含于9文件发布计划。

## 原core绑定与验证范围

每个blocks含separator各有一个segment，heading_path保留源英文heading stack，ordinal仅非separator递增；精确source hash及完整target组装都须匹配。glossary/addendum路径hash成对，reference_glossary_pins只含92，support_pins/DEPENDENCIES.files保持完整100。own3精确hash由外部候选冻结清单绑定，无自引用依赖hash。真实作者时间、部分/完整首稿及后续修订分开记录。

支持准备只执行静态字节、Git对象、AST/JSON/XML/原core分块与自有check-only契约校验；不执行课程源码，不声称CI、实际GFM/site/mobile/book或中文接受。S96另行隔离运行证据与S94/S95未GO严格分开。禁止安装到作者/远端/INDEX/queue，禁止改英文、原支持、共享术语或源代码。所需docs/i18n.md规范含既有中文示例，确实暴露且未复用；未读旧中文课文/segments/format_revisions或452/457。
