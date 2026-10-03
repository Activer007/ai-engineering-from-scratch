# S84 工作流发现术语

固定英文：`1bafaa88bb4668356791150bec3a6d7df38387eb` 的 `phases/14-agent-engineering/48-discover-the-real-workflow/docs/en.md`。本表在完整阅读英文、代码、6 个原测试、quiz 和输出后制定；仅用于术语一致性，不复用历史中文课文。遵循 `DEPENDENCIES.json` 的 87 项固定支持快照，不回填后续接受的术语文件。

## 沿用已接受术语

| EN | ZH / 推荐呈现 | 语境与限制 | 依据 |
|---|---|---|---|
| outcome | 结果；预期结果 | 工作完成后可观察到的结果，不等同于交付物 | S81 |
| output | 产出 | 本课工作流步骤产生的内容或对象；不能一律套用模型“输出”语境 | S81 |
| artifact | 产物（artifact） | 工单、操作手册、日志、表单、已完成的产出等可检查对象；不用“人工制品” | 核心表、S81 |
| on-call engineer | 值班工程师 | 示例中的执行者 | S81 |
| incident commander | 事件指挥员 | 事件响应中的批准/协调角色；不是智能体 | S81 |
| runbook | 操作手册（runbook） | 描述执行操作的文档；不因名称即声称其内容全部经过直接观察 | S81 |
| agent | 智能体（agent） | 若说明语境需要，遵循核心表；不混为事件指挥员或一般执行者 | 核心表 |
| Learning Objectives / Build It / Exercises / Further Reading | 学习目标 / 动手实现 / 练习 / 延伸阅读 | 保留源章节结构，不增造源没有的章节 | addendum |

## 本课语境决定

首次正文采用中英对应，后续使用中文；普通词不机械反复括注。标题可简洁。以下来源均为固定英文课文及其原始实现。

| EN | ZH / 推荐呈现 | 语境与限制 |
|---|---|---|
| workflow / workflow step | 工作流（workflow）/ 工作流步骤 | 有顺序、有证据的实际行动；不是仅指界面或自动化程序 |
| current system / current behavior | 当前系统 / 当前行为 | 先重建现在实际如何工作，不从功能愿望开始 |
| requirements / elicitation | 需求 / 需求获取（elicitation） | 获取包含解释、建模与验证，不把现成需求当作简单收集对象 |
| workaround | 变通做法（workaround） | 人们为完成工作采用的绕行办法，不强行暗示违规或漏洞利用 |
| actor | 执行者（actor） | 工作流步骤的行动主体，不译成“演员”，也不默认等于智能体 |
| trigger | 触发条件（trigger） | 使步骤开始的事件或条件，不改 Mermaid 的 `Trigger` |
| action / input | 行动 / 输入 | 本课工作步骤中的动作和所需信息，不擅加代码字段 |
| friction / friction point | 阻力（friction）/ 阻力点 | 重复劳动、延迟、重复录入或恢复等工作阻碍，不指物理摩擦力 |
| context switching | 上下文切换（context switching） | 在不同工具与信息之间切换，非专指操作系统线程切换 |
| handoff | 交接（handoff） | 行动或责任在执行者之间交接，保留源中的接续关系 |
| hidden state | 隐性状态（hidden state） | 存在于记忆、聊天或个人笔记中的事实；区别 S01 notebook 的“隐式状态”及 S29 神经网络的“隐藏状态” |
| hidden work | 隐性工作 | 可见流程之外仍需完成的工作，不等于恶意隐藏活动 |
| authority / authority boundary | 权限归属（authority）/ 权限边界 | 谁或哪个系统获准作出有重要影响的变更；不是“权威性”或证据可信度 |
| evidence / evidence ladder | 证据 / 证据层级（evidence ladder） | 行为依据的类型与强度；不同于贝叶斯归一化项 |
| direct behavior / direct observation | 直接行为证据（direct behavior）/ 直接观察 | 证据层级中的观察、轨迹、录制内容或系统事件；不夸大为全部步骤均有直接证据 |
| reported behavior | 陈述的行为（reported behavior） | 由人描述其行为；描述本身不等于直接观察 |
| inference | 推断（inference） | 团队对可能发生之事的推断，不套用模型执行阶段的“推理” |
| confidence | 置信度（confidence） | 对证据/主张的信心程度；不是置信区间，也不是经校准的概率保证 |
| direct-evidence ratio | 直接证据占比（direct-evidence ratio） | 实现按证据条目计数，四舍五入到两位小数；不偷换为步骤覆盖率 |
| trace / recording | 行为轨迹（trace）/ 录制记录 | 记录行动的证据；trace 不译为矩阵的“迹” |
| ticket / incident log | 工单 / 事件日志 | 证据产物，不是票据交易 |
| side channel | 非正式沟通渠道（side channel） | 主流程之外的沟通渠道，不机械套用安全攻击中的“侧信道” |
| exception / exception path | 例外情况（exception）/ 例外路径 | 正常工作流不再适用的情况；此处不局限于编程异常 |
| happy path | 正常路径（happy path） | 一切按预期进行的流程路径，不译为“快乐路径” |
| workflow variant | 工作流变体（workflow variant） | 因角色、风险、历史流程、经验或政策分歧而不同的做法，不能通过平均抹去差异 |
| legacy process | 旧流程 | 与当前流程并列的历史做法，不擅自判定已停止使用 |
| error recovery / failure recovery | 错误恢复 / 故障恢复 | 出错后恢复工作，不额外承诺自动恢复 |
| deployment record | 部署记录（deployment record） | 告警调查的输入及练习中缺失的对象 |
| production write | 生产环境写入操作 | 有权限要求的变更操作；原示例字符串保持英文 |
| assumption map | 假设图（assumption map） | 下一课用于整理观察到的阻力和不确定性的对象；不补造下一课内容 |

## 必须保留的英文与载荷

- `Python`、`stdlib`、`AI`、`Mermaid`、`JSON` 及其他产品、协议和语言标识保留原文；`Python (stdlib)` 元数据保持源形。
- `Type`、`Languages`、`Prerequisites`、`Time` 以及 `Learn + Build` 保持原文；自然语言的分钟单位可译。
- Nuseibeh、Easterbrook、Gotel、Finkelstein 与两篇论文题名保留英文。论文 URL、DOI 不改；只翻译其后的用途说明，不增补论文结论。
- 所有路径、代码、命令、函数/类/字段名和错误字符串保持原样，包括 `Evidence`、`WorkflowStep`、`audit`、`example`、`main`、`__file__`、`direct`、`confidence`、`grounded`、`needs-evidence`、`direct_evidence_ratio`、`outputs/workflow-evidence.json`。
- Mermaid 中的 `Trigger`、`Actor action`、`Handoff`、`Next actor action`、`Outcome`、`Direct evidence`、`Artifact`、`Reported behavior`、`supports` 与全部边保持字节不变。
- 数字、数学、提示词和 JSON/输出载荷不翻译、不修复。源文证据层级与示例 `direct=False` 的差异在审校材料中单列，不改写为已一致。
