# S123-reviewer-agent 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；规范题名：Reviewer Agent: Separate Builder from Marker。

本地支持候选，未安装或发布，不增加正式课程数。冻结 common127=119 TERM+8 controls；own3另计，未来总130。原7条角色/评分/关卡术语提案逐字段保留；rubric沿S116评分细则，S120评分准则为已注明语境同义项，不做全局替换。

| English | 本课译法 | 语境与依据 |
|---|---|---|
| builder / reviewer / marker | 构建者 / 审查者 / 评分者 | No matching role rows in the 119 common terminology files; new contextual proposal, core agent remains 智能体. reviewer/builder first explained in hook; marker appears only in title. 构建者写代码并在下一轮修复；审查者只读输入并写报告；marker指打分职责，不是标记器。 |
| rubric / reviewer rubric | 评分细则 / 审查者评分细则 | Follow S116 rubric=评分细则; S120 contextual LLM评分准则 recorded as synonym without global replacement. Not just a checklist; preserve five explicit dimensions and scores. |
| verification gate / verdict / finding | 验证关卡 / 判定结果 / 发现项 | S111/S120 Deterministic evidence gate differs from qualitative reviewer judgment. |
| problem fit / scope discipline / handoff readiness | 问题契合度 / 范围约束遵守情况 / 交接就绪程度 | Current fixed English rubric; handoff follows S84/S111/S120. Scope contract may deliberately grow; no false prohibition of all changes. |
| soft fail / hard fail / confidence floor | 软性失败 / 硬性失败 / 置信度下限 | Current fixed English; confidence follows S84 evidence-strength sense. Keep strict below thresholds, any-zero condition only where source provides it; not a calibrated probability guarantee. |
| stub / role separation / calibration set | 桩实现 / 角色分离 / 校准集 | Current fixed English; calibration follows S116 reviewer agreement context. Teaching stubs are not semantic scorers, live model calls or enforced read-only permissions. |
| position bias / verbosity bias / self-preference / authority | 位置偏差 / 冗长偏差 / 自我偏好 / 权威偏差 | S116 judge/positional bias plus current source definitions. Authority here means overrating known authors, not authorization or access permission. |

## 沿用和保护

核心与补充表优先，固定英文和相关术语足以起稿，先修中文正式验收不是额外门槛。保留代码、API、路径、URL、数字、数学与图载荷。源风险见SCOPE，语言PASS不等于运行、呈现、回归或发布通过。
