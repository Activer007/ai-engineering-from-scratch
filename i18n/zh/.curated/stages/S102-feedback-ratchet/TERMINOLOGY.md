# S102-feedback-ratchet 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Build a Feedback Ratchet with Ownership and Retirement。

本地 check-only own3 候选，未安装或发布。复用作者 95 TERM 固定校准及当前独立语言审核，定向核对相关词义，不声称本轮重读全部历史词表。以下作者提案数据行逐字保留；不要求改动当前正文或旧术语表。原 common103 = 95 TERM + 8 controls；own3 另计，未来总支持106，不把后来新增 common106 套入作者首次输入。

| EN | 本课中文 | 语境与边界 |
|---|---|---|
| feedback ratchet | 反馈棘轮 | 将观察转化为持久系统改进的机制；不是物理装置 |
| ownership / owner | 责任归属 / 负责方 | 源示例有 platform/security/evaluation 等团队责任主体，不限定为自然人，也不是文件所有权 |
| ratchet action | 反馈棘轮改进行动；后文反馈改进行动 | 包含负责方、优先级、产物、验证、审查窗口与停用条件 |
| promotion | 将观察提升为系统改进的机制 | 不是升职、商业促销或模型升版；不暗示本程序实际落实所有控制 |
| control / durable control | 控制措施 / 持久控制措施 | 测试、权限、上下文、运行时等保护机制，不等同只加一段提示词 |
| retirement / retirement condition | 停用 / 停用条件 | 停用需证据；源码仅生成检查文本，不实施自动到期或删除 |
| owning layer | 负责的系统层 | 最早能处理原因的层次，不套用镜像层或神经网络层 |
| recurrence | 复发；再次发生 | 故障再现，不套用 RNN 循环机制 |
| severity / frequency | 严重程度 / 发生频率 | 源程序优先级为二者乘积；不另加数学公式或保证 |
| policy / permission boundary | 策略 / 权限边界 | 系统安全和权限治理，不是强化学习动作策略 |
| authority gap | 权限缺口 | 沿 S87/S90/S93 权限语义，不是权威性或可信度不足 |
| backlog / shaped backlog item | 待办清单 / 经梳理明确的待办项 | 产品工作安排；不是消息队列积压量 |
| false positive / regression | 误报 / 质量退步 | 业务评估及软件回归语境；沿 S10/S28/S37 与 S95，不是回归预测模型 |
| trace / incident log | 行为轨迹（trace）/ 事件日志 | 精确沿 S84 相关语义，不是矩阵迹 |
| outcome frame / slice | 结果框架（outcome frame）/ 工作范围 | 沿 S81/S90；结果不是交付文件，slice 不是数据切片 |
| artifact / invariant | 产物（artifact）/ 不变条件（invariant） | 沿核心/S84/S93；不把产物存在当作验证已经通过 |
| workflow / handoff / workbench | 工作流（workflow）/ 交接（handoff）/ 工作台（workbench） | 沿 S84 和核心表，首次中文说明，API/路径不变 |

## 沿用和消歧

ownership 为责任归属，owner 为负责方，可由个人或团队承担，不是文件/财产所有权；one owner 的单一责任主体条件保持。retirement 为控制措施停用，须有证据和停用条件；review or expiry window 与 retirement condition 分列，不能把到期窗口解释为自动删除或自动失效。

feedback ratchet 保留“反馈棘轮”，通过负责方、持久变更、验证和复查表达把反馈固化为系统改进。policy、authority、regression、slice、invariant 分别按系统策略、权限、质量退步、工作范围、不变条件处理，不强套强化学习策略、回归预测或数据切片。程序仅保存验证/停用文本，不代表措施已经落实。

## 保护规则

核心及补充表优先，通用章节沿既有规范，英文没有的章节不补造。API、模型、专名、标识符、路径、URL、公式、数值、代码与图载荷保持；首次正文按本课语境中英对应，不把同词跨任务机械统一。源内矛盾、宽泛或版本性断言单列，不静默修正英文含义、数学或代码。

词表用于一致性，不复用旧中文课文/segments；规范自带质量示例仅附带曝光且未复用。起草只依赖固定英文与术语，不等待先修中文正式验收。支持候选、语言 PASS、课程运行、GFM与正式计数分别记录。
