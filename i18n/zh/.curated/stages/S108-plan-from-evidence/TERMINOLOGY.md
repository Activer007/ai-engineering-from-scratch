# S108-plan-from-evidence 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Build an Evidence-Backed Execution Plan。

本地 check-only own3 候选，未安装、未发布，不计课程完成。复用作者101 TERM校准和当前独立语言审校；定向核对本课词义，不重扫全部历史词表。原common109为101 TERM+8 controls，own3另计、未来总112，不替换原支持身份。作者提案表格数据行逐字保留，不要求修改正文或旧词表。

| Source term | Draft Chinese | Context and boundary |
|---|---|---|
| evidence-backed execution plan | 有证据支撑的执行计划 | Actual docs H1; quiz short title is only a source note |
| task frame | 任务框架（task frame） | Bounded task definition from English prerequisite 14-43; no old Chinese consulted |
| work item | 工作项（work item） | Stable plan unit with change/evidence/dependencies/proof |
| dependency graph / dependency | 依赖图（dependency graph）/ 依赖关系、依赖项 | Work prerequisites, not software packages or syntactic dependency parsing |
| terminal node | 终止节点 | Terminal point in the work graph, not a shell terminal |
| contract | 契约（contract） | Shared behavior/interface agreement, not a legal transaction |
| surface | 组成要素（surface） | Align core addendum/S93; tests, implementation, documentation, integration |
| evidence | 证据 | Repository facts supporting change; a stored string is not verified evidence |
| proof | 验证证据（proof） | Align S93 concept; in required-check contexts use 验证依据/完成验证方式, in ran/commands contexts 验证/验证命令; no assertion of completed execution |
| receipt / repository receipt | 证据凭据 / 仓库中的证据凭据 | Support for a repository fact; not a payment receipt; source code checks tuple/text presence only |
| topological sort | 拓扑排序（topological sort） | Align S08/S32/S76; does not prove resource/file independence |
| cycle | 环 / 依赖环 | Dependency cycle; not a loop that is actually executed |
| execution wave | 执行批次（execution wave） | Dependency-level groups; not a real concurrent executor |
| integration gate | 集成门禁（integration gate） | Final check after both implementation and documentation; source graph payload remains English |
| resumable | 可恢复执行的 | Design requirement, not a claim JSON stores durable completion/proof receipts |
| schema | schema（结构定义） | Align core; keep English and explain first occurrence |
| artifact | 产物（artifact） | Align core/S81/S84/S90/S102; not image artifacts |
| handoff | 交接（handoff） | Align S84/S102 |
| irreversibility / uncertainty | 不可逆性 / 不确定性 | Align S87/S90; last plan-rejection check requires judgment |
| delegation contract | 委派契约 | Intended role of JSON in next lesson; not a claim of implemented permission enforcement |

## 沿用和消歧

evidence/proof/receipt分别表达仓库证据、验证证据或具体完成检查、证据凭据，不套贝叶斯证据或付款收据。terminal node不是命令行终端，dependency不是包依赖，wave不是实际并发执行。contract是行为/接口契约，surface是组成要素，artifact是产物。真实修订保留helper的通用范围、依赖解除阻塞与完成的区别，以及不可逆动作本身的发生时序，不倒推首写已经具有修订后的表述。

## 保护规则

核心及补充表优先。API、模型、专名、标识符、路径、URL、公式、数值及代码/图载荷保持；按本课语境说明首现，不将异义词机械统一。源内矛盾、宽泛或版本性断言另列SCOPE，不静默改写源技术含义，不把翻译/语言PASS当作运行或安全验证。

只依赖固定英文及术语起草，不要求先修中文正式验收；本表不包含旧中文正文或segments。支持候选、语言审校、真实GFM、运行和批次分别记录。
