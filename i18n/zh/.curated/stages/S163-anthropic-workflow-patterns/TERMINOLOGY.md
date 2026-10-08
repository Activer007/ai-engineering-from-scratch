# S163 Anthropic workflow patterns terminology proposal

Fixed English 1bafaa88bb4668356791150bec3a6d7df38387eb; lesson 14-12. Source-only lexical proposal by the assigned preparer/author, before Chinese lesson prose. This is not completed post-installation author calibration. Common164 is a local candidate; independent review, publication, readback, installation and coordinator prose clearance remain pending.

| English | Proposed Chinese | Inheritance and boundary |
|---|---|---|
| workflow / agent / agent loop | 工作流（workflow）/ 智能体（agent）/ 智能体循环 | S132; engineer-owned predefined paths versus model-directed steps, not static versus stateful |
| LLM / prompt / token | 大语言模型（LLM）/ 提示词（prompt）/ token（词元） | Core first-body-use conventions; token is not necessarily a word |
| augmented LLM | 增强型大语言模型（augmented LLM） | Scoped compound: retrieval, tools and memory; not model retraining |
| prompt chaining / prompt chain | 提示词串联 / 提示词链 | Scoped pattern: previous call output becomes next call input |
| routing / classifier / dispatch | 路由 / 分类器 / 分派 | S147 dispatch; routing is selection of handler, not network routing |
| parallelization / concurrent calls / sequential | 并行化 / 并发调用 / 顺序执行 | S147; distinguish source conceptual concurrency from sequential demo |
| sectioning / voting / majority voting | 分块处理 / 投票 / 多数投票 | Sectioning covers different chunks; voting repeats the same prompt. Majority follows S23/S24 |
| aggregate / synthesis | 聚合 / 综合 | Combining outputs versus producing a synthesized answer; do not invent an LLM synthesizer in demo |
| orchestrator-workers / orchestrator / worker | 编排器—工作单元 / 编排器 / 工作单元 | Scoped pattern; workers are LLM calls, not necessarily autonomous agents, threads or processes |
| evaluator-optimizer / evaluator / optimizer | 评估器—优化器 / 评估器 / 优化器 | Exact S144 lexical convention; optimizer revises outputs, not model weights |
| proposer / judge / iterative refinement | 提案生成器 / 评判器 / 迭代改进 | S144 iterative improvement; evaluation success distinct from budget exhaustion |
| programmatic gate | 程序化关卡 | S132 engineering gate sense; optional source condition, no new security guarantee |
| stop condition / iteration budget / turn budget | 停止条件 / 迭代预算 / 轮次预算 | S132/S144; do not conflate steps, tokens and wall-clock time |
| context engineering / context window / compact | 上下文工程 / 上下文窗口 / 压缩整理 | Context engineering scoped compound; S150 compaction, not file compression; keep pre-renumber reference unresolved |
| memory / persistence / retrieval | 记忆 / 持久化 / 检索 | S150/S132; contextual memory distinct from host RAM |
| durable state / actor-model concurrency / role templating | 持久状态 / actor 模型并发 / 角色模板化 | S132 actor model, not actor in reinforcement learning |
| harness / trace / tool call | 运行框架（harness）/ 行为轨迹（trace）/ 工具调用 | S132; trace is run record, not matrix trace |
| API / SDK | API（应用程序编程接口）/ SDK（软件开发工具包） | Core; retain complete product names |
| cost-bound / compliance-bound | 受成本约束的 / 受合规约束的 | Describes task constraints, not a measured cost or compliance certification |
| tier-1 support / confidence threshold / timeout | 一线支持 / 置信度阈值 / 超时限制 | S147 timeout; exercise proposals are not existing implemented features |
| bandit / top-2 | 多臂老虎机 / top-2 | Exercise analogy; preserve protected numeric spelling, no implemented bandit claimed |
| Self-Refine / CRITIC / ScriptedLLM | Self-Refine / CRITIC / ScriptedLLM | Method and class names remain exact; ScriptedLLM is deterministic mock |

Core first-body-use rules apply to eligible prose. Protect all identifiers, names, numbers, metadata keys and type/language values, code, URLs, paths and figure payload. Retain Anthropic, Schluntz, Zhang, LangGraph, AutoGen v0.4, CrewAI, Claude Agent SDK, Claude Code and OpenAI Agents SDK exactly. Common headings use ADDENDUM only where those headings exist. The single bare fence may later receive only the existing reversible text tag. No terminology decision authorizes source fixes or a checker exception.

Semantic lexical reading: core TERMINOLOGY.md complete, ADDENDUM lines 1–35, S132 complete, S144 complete, S147 complete, S150 complete; targeted S23/S24 majority-voting rows. All164 candidate payload identities were checked; this does not claim full semantic reading of every historical TERM file. Frozen historical lifecycle labels do not override current evidence. Post-installation author calibration and independent support review remain pending.
