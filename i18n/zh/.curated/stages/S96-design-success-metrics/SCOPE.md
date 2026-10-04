# S96-design-success-metrics English-first 支持范围

状态：本地check-only候选，未安装、未发布。作者已真实正文起草；本支持准备不启动作者、不替代评审、不增加正式107。不能以先修中文是否正式接受作为准备/起草门禁。

## 固定英文与唯一目标

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Source tree: `3d90647a3449a7b228a6b6025ed2b333ef99e81c`
- Lesson: 14-52
- Canonical docs H1: Design Success Metrics Before the Result Exists
- Source: `phases/14-agent-engineering/52-design-success-metrics/docs/en.md`
- Source Git blob: `8bd0e7fcc32b8000e41491fc979f72343daf8078`
- Source SHA256: `dd1c976a46c3cffd2de66283c967c8b6589217f3171e2168b8f6852fdbc27ecc`
- Target: `i18n/zh/phases/14-agent-engineering/52-design-success-metrics/docs/zh.md`
- Eventual record: `i18n/zh/.curated/lessons/14-52/translation.json`
- Original core blocks: 71
- English prerequisite line: **Prerequisites:** Phase 14 lessons 47 and 51
- Actual first write UTC: 2026-10-04T09:59:43.636709+00:00
- First-write receipt SHA256: b7260f162f91c6b5fee18b9b1712e9c5abb5d2a3c4afc8f2cae72648def9cea0
- First target: 4296 bytes, full first draft; SHA256 c0f84323a3ac4eace333218668142a98aab748247038ffbc0aaf19d982579c9d

完整课程输入为DEPENDENCIES.json.source_files，元数据/题名依docs H1，不由quiz缩短标题覆盖。首写时间来自原回执，原快照已核hash；不由mtime重构，也不拿草稿作为翻译记忆。

## 固定支持与历史

正式INDEX `0a1d387aec90759759d1bbb07bb4cd61c1f114a8`，SHA256 `7233acb6aeb253ae9812c7bc38a28bdf719d64f0fb4a7d4237eae02c5a20e8c2`，107课。全部100common已存在且原字节核验一致；本课own3仅候选，合计103。92参考TERM和8controls分别计数；正式87TERM（85accepted stage+core2），active-reviewed5为S88/S89/S91/S92/S93。保留S90旧TERM内106/active历史及原pin标签，通过独立current classification表标示已正式接受，不重写旧术语。

schema_version=1及原f9 core/S07/S19 controls保持，不扩展schema/loader/权限/CI。原33测试fixture仅独立测试元数据，不读取其中文body/segments、不装入作者目录；原33/24/50套件及日志未改。own stage仅DEPENDENCIES.json、SCOPE.md、TERMINOLOGY.md三条精确路径，不允许兄弟stage/target/record/asset混入。

publication pending/null仅freeze-time尚未发布快照，非永久未发布。实际后续commit必须外部record和远端回读绑定，不自引用当前文件、不造SHA。三个课程可分别准备/冻结/校验，互不等待先修中文验收。

## 源风险与运行边界

- 五份源文件含六项原unittest；H1为Design Success Metrics Before the Result Exists，quiz短标题Design Success Metrics及README类型差异均保留，doc元数据为Learn + Build、Python (stdlib)。
- valid只反映计划结构检查，不等于阈值全部通过、发布就绪或真实安全；缺值/失败值可以与valid并存。原代码没有实现总pass/fail/ambiguous决策、方差/样本充分性规则，也不从日志计算median/rate。
- 文档的population字段未进Metric/JSON；counter-metric未被validator强制要求；kind、数值有限性、重名和完整字段内容检查有限，不在翻译中补schema。
- at-most为<=，at-least为>=；0.9和120等号通过，源<0.75仍为严格比较。供应production_writes=0并不能实施只读控制或证明实际零写入。
- 源main按__file__覆盖outputs/measurement-report.json，单改cwd不能隔离。已单独授权的隔离原main+六项原tests退出0、产物与源示例字节相等，仅为有界技术证据；该实物摘要由外部receipt绑定。本支持准备没有重跑，未扩展到生产/真实试点/中文审校。

## 原core绑定与验证范围

每个blocks含separator各有一个segment，heading_path保留源英文heading stack，ordinal仅非separator递增；精确source hash及完整target组装都须匹配。glossary/addendum路径hash成对，reference_glossary_pins只含92，support_pins/DEPENDENCIES.files保持完整100。own3精确hash由外部候选冻结清单绑定，无自引用依赖hash。真实作者时间、部分/完整首稿及后续修订分开记录。

支持准备只执行静态字节、Git对象、AST/JSON/XML/原core分块与自有check-only契约校验；不执行课程源码，不声称CI、实际GFM/site/mobile/book或中文接受。S96另行隔离运行证据与S94/S95未GO严格分开。禁止安装到作者/远端/INDEX/queue，禁止改英文、原支持、共享术语或源代码。所需docs/i18n.md规范含既有中文示例，确实暴露且未复用；未读旧中文课文/segments/format_revisions或452/457。
