# S132-the-agent-loop 术语约定

固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；本地 own3 候选，未安装、未发布。原术语提案 SHA256 c4912f0dcce136fd4cc262063cc7cb92b33cce67d35ce1cdc868e35a54c6b3c0；首写前校准 SHA256 c4912f0dcce136fd4cc262063cc7cb92b33cce67d35ce1cdc868e35a54c6b3c0。原 common133 不变，本候选追加已独核 S127–S129 TERM 为 common136。

| 英文 | 本课采用 | 语境、依据和边界 |
|---|---|---|
| agent / agent loop | 智能体（agent）/ 智能体循环 | core、S104、S117；不是网络代理 |
| ReAct / Thought / Action / Observation | ReAct / 思考 / 行动 / 观察结果 | 源文三要素；保留受保护英文标签和示例；首次学习目标中说明三者 |
| observation formatter | 观察结果格式化器 | 将工具输出转换成模型可读字符串，不是图表格式 |
| LLM / token / prompt | 大语言模型（LLM）/ token（词元）/ 提示词（prompt） | core；token 不译凭据令牌 |
| API / SDK | API（应用程序编程接口）/ SDK（软件开发工具包） | core；产品完整名不改，首现解释缩写 |
| schema | schema（结构定义） | core、S110、S122、S126；不降格为仅格式 |
| tool registry / tool call | 工具注册表 / 工具调用 | core registry 定义；按名称分派到可调用对象，非注册机构 |
| message buffer / turn / turn budget | 消息缓冲区 / 轮次 / 轮次预算 | 源文 control flow；预算限定循环迭代次数，不等同 token 预算或工具耗时上限 |
| stop condition | 停止条件 | 源五要素；不增补源实现没有的停止能力 |
| harness / runtime | 运行框架（harness）/ 运行时（runtime） | core addendum、S01、S120、S126；不译成运行耗时 |
| reasoning trace / trace | 推理轨迹 / 行为轨迹（trace） | 推理过程与完整运行记录；S84/S102 行为证据语境，不是 S06 矩阵的迹 |
| tracing spans | 追踪跨度（span） | 可观测性中一次操作的追踪单元；不是 S05 张成或 NLP 文本跨度 |
| actor model / actor | actor 模型 / actor（消息处理主体） | AutoGen 并发消息传递模型；不机械套用 S84 工作流“执行者”或译为演员 |
| guardrail / trust boundary | 安全护栏（guardrail）/ 信任边界 | core；触发限制不保证绝对安全 |
| evals / eval trajectories | 评测 / 评测轨迹 | S70、core addendum；不是已实测验收 |
| hallucination / in-context examples / RL | 幻觉（hallucination）/ 上下文示例 / 强化学习（RL） | S74/S95/S101、S38、S22；源绝对百分点保留 +34、+10 |
| native reasoning / reasoning channel | 原生推理 / 推理通道 | 源过程字段语境，非模型推理服务性能；跨提供商加密互通是源断言、另列风险 |
| checkpointing / workflow | 检查点保存 / 工作流 | 持久状态保存，区别 S32 梯度检查点；S84 工作流 |
| verification gate | 验证关卡 | S111/S117/S120 已校正工程语境；源正文未出现，不补造，不把其它多义词机械替换 |

品牌、模型/接口名、数值、范围、路径、链接目标、内联代码、figure payload 逐字保护；两个无语言标签围栏仅依据冻结 curated 工具既有规则增加 text。无术语 strict 豁免或检查器修改。

当前 R02 在 b0009 首现采用“工具注册表（tool registry）”，符合 registry 首次中英规则；ToolRegistry 代码标识符及后续提法保持。原提案和初版审校误判均保留，当前闭环依据修正后的 required_revision 报告及独立 R02 增量 SHA256 310300cec219a8619558f1f0ee350d5c3681a668f6fca6a425521d2170857dde。
