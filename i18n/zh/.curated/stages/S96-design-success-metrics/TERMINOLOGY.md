# S96-design-success-metrics 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Design Success Metrics Before the Result Exists。

这是完整固定92份词表校准后的本地check-only候选，尚未安装或发布，不构成中文审校或正式接受。原术语提案无需强制改词；以下词义只用于本课语境。正式基线107；87正式TERM=85 accepted stage+core2，active-reviewed5=S88/S89/S91/S92/S93，总92；8原controls另计，100common+本课own3=103。S95原样SVG另计。原支持日期、旧状态叙述与字节保留，不据此否定S90现已正式接受。

| English | Proposed Chinese | Context and boundary |
|---|---|---|
| outcome / output | 结果；预期结果 / 产出 | S81/S84/S87/S90/S93: observable improvement versus delivered form. No model-output meaning unless code I/O |
| metric / outcome metric | 指标 / 结果指标（outcome metric） | S39 evaluation sense, not S16/S24 mathematical distance axioms |
| guardrail / guardrail metric | 安全护栏（guardrail）/ 安全护栏指标 | Core term retained. Here means monitoring a fixed constraint; supplied value does not enforce production access or prove safety |
| counter-metric | 制衡指标（counter-metric） | Detects cost or harm shifted elsewhere; not a second copy of the outcome metric and not an automatically required field in the implementation |
| metric contract | 指标契约 | Required definition of how a metric supports a decision; does not assert code implements population or a complete aggregate gate |
| threshold | 阈值 | S23/S28; preserve inclusive at-most/at-least, strict below 0.75, and all source numbers |
| direction | 比较方向 | Here at most / at least; not a spatial direction |
| window / measurement window | 测量窗口 | Time or sample boundary. Ten incident replays is sample scope, not a duration; does not use audio window terminology |
| source | 数据来源 | Reproducibility of the metric's number, not necessarily source code |
| population | 总体（population） | S17 statistical sense; example specifically on-call engineers in the pilot, not every user or every incident |
| operationalize | 转化为可测量的量；转化为可测量的问题 | Contextual phrase: choose metrics to answer the questions; not system operations |
| workflow | 工作流（workflow） | S84/S87/S90; all work steps and effects, not just a UI |
| incident / on-call engineer | 事件 / 值班工程师 | S81/S84; operational incident context |
| production write | 生产环境写入操作 | Exact S84/S93 meaning; protected production_writes and other identifiers unchanged |
| operator workload / trust | 操作人员的工作量 / 信任程度 | S90 operator is not automatically narrowed to on-call engineer |
| offline replay | 离线回放 | Source says offline, not synonymous with guaranteed read-only enforcement |
| bounded pilot | 范围受限的试点 | Pilot follows S90. Bounded here describes pilot scope, not the S93 code enum decision mode |
| pass / fail / ambiguous | 通过 / 失败 / 尚无法明确判断 | S87 ambiguity semantics; three evidence decision paths, not implemented aggregate statuses |
| inclusive thresholds | 包含等号的阈值条件 | at-most is <=, at-least is >=; equality passes for valid present values |
| median / variance | 中位数 / 方差 | S17 and S09/S39; preserve statistical meanings and do not invent aggregation performed by code |
| measurement plan / valid | 测量计划 / 有效 | valid describes validation of plan structure only; a failed threshold or missing value may coexist with top-level valid |
| evidence gate | 证据门槛（evidence gate） | A required evidence boundary. Final sentence follows source; does not claim implemented production release approval |

## 沿用和消歧

沿用S81/S84/S87/S90/S93结果与产出区分、生产环境写入操作、操作人员的信任程度；安全护栏沿核心定义，制衡指标不与结果指标复写混同。总体是指定试点中的人员集合，十次事件回放是样本窗口。offline replay译离线回放，不自行增加只读保证；bounded pilot为范围受限的试点，不套S93决策模式enum。valid只译计划结构有效，尚无法明确判断保留第三条证据决策分支。

## 保护规则

核心及补充表优先，首次正文说明中英对应，API、模型ID、语言代码、公式、数值单位、路径、链接、代码与图载荷保持。九个通用章节沿补充表，英文无的章节不补造。自然语言数量变化必须等值逐块记录。源技术疑问单列，不能静默改写。

参考词表只用于术语一致性，未复用旧中文课程正文/segments/format_revisions。必要阅读docs/i18n.md已暴露其中既有中文质量示例；未引用或复用该示例措辞。支持、作者草稿及局部测试均不增加正式完成数。

publication pending/null只记录冻结时尚未绑定发布提交；冻结后不自指当前文件commit。实际发布须由后续record/外部远端回读绑定，不能删除历史或编造SHA。
