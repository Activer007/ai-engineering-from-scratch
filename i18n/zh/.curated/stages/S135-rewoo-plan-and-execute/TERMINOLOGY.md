# S135-rewoo-plan-and-execute 术语约定

固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb。正文起草前支持候选，依据本课完整英文、14-01 固定完整英文旧读和 common136。S130–S132 未公开 TERM 不作 pin；作者首写、capture、record、strict 和独审尚未发生。

| English | 本课中文 | 依据与语义边界 |
|---|---|---|
| ReWOO / reasoning without observations | ReWOO / 不依赖观测的推理 | 规划阶段不读取工具观测；不说整个系统完全没有观测 |
| Plan-and-Execute / plan-then-execute | Plan-and-Execute（规划后执行）/ 先规划再执行 | 保留模式名称；可选重新规划与静态计划区分 |
| Plan-and-Act | Plan-and-Act | 作为专名保留，首现说明规划与行动分离的模式 |
| decoupled planning / interleaved loop | 解耦规划 / 交错循环 | 规划与执行分离；交错是思考、行动、观测顺序交替 |
| Planner / Worker / Solver | 规划器 / 工作单元 / 求解器 | 本课三角色；Worker 通过工具注册表执行，不冒称线程或独立LLM。S111 的工作智能体属于不同具体语境 |
| executor / replanner | 执行器 / 重新规划器 | 与 Solver 合成最终答案的职责分开 |
| plan DAG / topological order | 计划有向无环图（DAG）/ 拓扑顺序 | 依赖先后约束；有拓扑顺序不等于当前实现会并行 |
| evidence / evidence reference | 证据 / 证据引用 | 本课工具输出及其占位引用；不是独立审核回执 |
| dispatch / tool registry | 分派 / 工具注册表 | 根据工具名转交调用；引用替换与工具运行不同阶段 |
| failure localization / degrade gracefully | 故障定位 / 平稳降级 | 保留源鲁棒性主张，但不声称脚本覆盖全部错误 |
| planner distillation / teacher | 规划器蒸馏 / 教师模型 | 用大模型的规划轨迹训练小模型，非把观测也作为规划输入 |
| trajectory / long-horizon task | 轨迹 / 长时程任务 | 多步行动任务，horizon 不按墙钟时长解释 |
| synthetic plan data / plan trace | 合成计划数据 / 规划轨迹 | 训练数据和运行期间的工具结果区别 |
| token efficiency / character count | token 使用效率 / 字符数 | token 首次解释为词元；字符数只是脚本近似，不等于 tokenizer 实测 |
| absolute accuracy improvement | 准确率的绝对提升 | 区别相对百分比增长；保留源数字及符号约束 |
| parallel group / schema validation | 并行组 / schema 校验 | schema 首现解释为结构约束；技能要求不等于代码已实现 |

沿用智能体、提示词、工具调用、观测、模型微调等现有语境。代码、行内代码、占位符、模型ID、数字、URL、路径、SVG、figure 载荷保持。源功能落差、引用错位和性能断言单列，不擅修原文。后续作者或审校如有真实术语修订，保留本候选和发布身份并记录增量。
