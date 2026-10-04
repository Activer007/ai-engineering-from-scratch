# S94-object-detection-yolo English-first 支持范围

状态：本地check-only候选，未安装、未发布。作者已真实正文起草；本支持准备不启动作者、不替代评审、不增加正式107。不能以先修中文是否正式接受作为准备/起草门禁。

## 固定英文与唯一目标

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Source tree: `3d90647a3449a7b228a6b6025ed2b333ef99e81c`
- Lesson: 04-06
- Canonical docs H1: Object Detection — YOLO from Scratch
- Source: `phases/04-computer-vision/06-object-detection-yolo/docs/en.md`
- Source Git blob: `8443653421888eca0c17c94a5b84ec48a1905c96`
- Source SHA256: `2274e5867a4df25fb17a700b8ad129fa6a45b6eb1aebf0673af7a2bc95bb2a79`
- Target: `i18n/zh/phases/04-computer-vision/06-object-detection-yolo/docs/zh.md`
- Eventual record: `i18n/zh/.curated/lessons/04-06/translation.json`
- Original core blocks: 165
- English prerequisite line: **Prerequisites:** Phase 4 Lesson 03 (CNNs), Phase 4 Lesson 04 (Image Classification), Phase 4 Lesson 05 (Transfer Learning)
- Actual first write UTC: 2026-10-04T09:58:21.511264+00:00
- First-write receipt SHA256: 80ee6f9a25a852ae22ba8e0a0fe82046282cbf062292f3afb043867043fb9af7
- First target: 394 bytes, partial opening only; SHA256 eafb686f8c83ee0ea141a5cac44a2e808817656350384551a0a9e1e18810ee9e

完整课程输入为DEPENDENCIES.json.source_files，元数据/题名依docs H1，不由quiz缩短标题覆盖。首写时间来自原回执，原快照已核hash；不由mtime重构，也不拿草稿作为翻译记忆。

## 固定支持与历史

正式INDEX `0a1d387aec90759759d1bbb07bb4cd61c1f114a8`，SHA256 `7233acb6aeb253ae9812c7bc38a28bdf719d64f0fb4a7d4237eae02c5a20e8c2`，107课。全部100common已存在且原字节核验一致；本课own3仅候选，合计103。92参考TERM和8controls分别计数；正式87TERM（85accepted stage+core2），active-reviewed5为S88/S89/S91/S92/S93。保留S90旧TERM内106/active历史及原pin标签，通过独立current classification表标示已正式接受，不重写旧术语。

schema_version=1及原f9 core/S07/S19 controls保持，不扩展schema/loader/权限/CI。原33测试fixture仅独立测试元数据，不读取其中文body/segments、不装入作者目录；原33/24/50套件及日志未改。own stage仅DEPENDENCIES.json、SCOPE.md、TERMINOLOGY.md三条精确路径，不允许兄弟stage/target/record/asset混入。

publication pending/null仅freeze-time尚未发布快照，非永久未发布。实际后续commit必须外部record和远端回读绑定，不自引用当前文件、不造SHA。三个课程可分别准备/冻结/校验，互不等待先修中文验收。

## 源风险与运行边界

- 五份课程源文件，无原tests或独立SVG。quiz仅五题（pre2/post3），不补造源内容。main是单图像、类别无关NMS的教学实现，不是完整批处理生产检测器。
- 文档encode/assign_targets缺逆sigmoid，而main存储logit；文档loss缺单批次处理；开篇输出形状漏anchor因子。文档exp无main的截断保护，postprocess参数也不同。保留两处原文，技术差异独立记录。
- NMS循环最坏为平方比较工作量，不因排序便证明O(N log N)；相同分数与跨库等价性、现代YOLO普适性及预训练主干目标都未经本准备实测。objectness与其乘类别概率的后处理分数不能混称。
- prompt首匹配第4规则被第1规则覆盖；AP/mAP定义及损失权重概括保留但不当新证明。锚框聚类output是配方，不是已运行聚类程序。
- 本课无源执行GO。本支持准备不执行main、导入torch/课程模块、预训练调用、训练、GPU、下载、依赖安装或框架比较；将来任何有界fixture须独立授权。

## 原core绑定与验证范围

每个blocks含separator各有一个segment，heading_path保留源英文heading stack，ordinal仅非separator递增；精确source hash及完整target组装都须匹配。glossary/addendum路径hash成对，reference_glossary_pins只含92，support_pins/DEPENDENCIES.files保持完整100。own3精确hash由外部候选冻结清单绑定，无自引用依赖hash。真实作者时间、部分/完整首稿及后续修订分开记录。

支持准备只执行静态字节、Git对象、AST/JSON/XML/原core分块与自有check-only契约校验；不执行课程源码，不声称CI、实际GFM/site/mobile/book或中文接受。S96另行隔离运行证据与S94/S95未GO严格分开。禁止安装到作者/远端/INDEX/queue，禁止改英文、原支持、共享术语或源代码。所需docs/i18n.md规范含既有中文示例，确实暴露且未复用；未读旧中文课文/segments/format_revisions或452/457。
