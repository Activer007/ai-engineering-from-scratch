# Anthropic 的工作流模式：简单优于复杂

> Schluntz 和 Zhang（Anthropic，2024 年十二月）将工作流（workflow，预定义路径）与智能体（agent，动态使用工具）区分开来。五种工作流模式足以应对大多数情况。从直接调用 API（应用程序编程接口）开始。只有无法预先确定步骤时，才引入智能体。

**Type:** Learn + Build
**Languages:** Python (stdlib)
**Prerequisites:** Phase 14 · 01（智能体循环）
**Time:** ~60 分钟

## 学习目标

- 说出 Anthropic 的五种工作流模式：提示词串联（prompt chaining）、路由（routing）、并行化（parallelization）、编排器—工作单元（orchestrator-workers）、评估器—优化器（evaluator-optimizer）。
- 解释智能体与工作流的区别，以及各自的工程成本。
- 判断何时应选择工作流而不是智能体，以及何时反过来选择。
- 使用标准库，以脚本化大语言模型（LLM）为调用对象，实现全部五种模式。

## 要解决的问题

有些问题只需要一次函数调用，团队却动辄使用多智能体框架。代价实实在在：框架增加的层次会遮蔽提示词（prompt）、隐藏控制流，并引入过早的复杂性。Schluntz 和 Zhang 在 2024 年十二月发表的文章，是业界反对这种做法的文章中被引用最多的一篇：从简单方案起步，只有收益足以抵偿成本时才增加复杂性。

## 核心概念

### 工作流与智能体

- **工作流。** 通过预定义代码路径编排 LLM 和工具。流程图由工程师掌控。
- **智能体。** LLM 动态指挥自己的工具，自行决定执行步骤。流程图由模型掌控。

两者各有用武之地。工作流更便宜、更快，也更容易调试。智能体能够处理开放式问题，但其失效模式更难分析。

### 增强型大语言模型

五种模式都建立在同一个基础上：一个接入了三种能力的增强型大语言模型（augmented LLM），即搜索（检索）、工具（行动）和记忆（持久化）。任何 API 调用都可以使用这些能力。

### 五种模式

1. **提示词串联。** 第 1 次调用的输出成为第 2 次调用的输入。适用于可以清晰地按线性步骤分解的任务。步骤之间可以设置程序化关卡（programmatic gate）。

2. **路由。** 分类器 LLM 选择要调用的下游 LLM 或工具。适用于不同类别的输入需要不同处理方式的场景（1 级支持、退款、缺陷或销售）。

3. **并行化。** 并发运行 N 次 LLM 调用，再聚合结果。有两种形式：分块处理（sectioning，处理不同的数据块）和投票（voting，使用相同提示词运行 N 次，以多数投票或综合结果得出结论）。

4. **编排器—工作单元。** 编排器 LLM 动态决定运行哪些工作单元（同样是 LLM），并综合其输出。它类似于智能体循环，但编排器不会无限循环。

5. **评估器—优化器。** 一个 LLM 提出答案，另一个 LLM 对其进行评估。反复迭代，直到评估器判定通过。这是 Self-Refine（第 05 课）的推广形式。

### 工作流何时优于智能体

- **可预测的任务。** 如果能够列出各个步骤，就应当这样做。
- **受成本约束的任务。** 工作流的步骤数有界；智能体的步骤数可能不断膨胀。
- **受合规约束的任务。** 审计人员希望直接查看流程图，而不是从执行轨迹中推断它。

### 智能体何时优于工作流

- **开放式研究。** 下一步取决于上一步返回的结果。
- **长度可变的任务。** 工作可能持续几分钟到几小时，步骤数事先未知。
- **全新领域。** 尚不清楚怎样的工作流才合适时，先探索，再将流程固化。

### 配套的上下文工程

“Effective context engineering for AI agents”（Anthropic，2025）系统阐述了与之相关的上下文工程（context engineering）：200k 的上下文窗口是一项预算，而不是一个容器。需要决定纳入什么、何时压缩整理、何时允许上下文增长。本课程 Phase 14 的上下文压缩一课对此有详细讲解（重新编号之前，是 Phase 14 较早的第 06 课）。

```figure
workflow-chain
```

## 动手实现

`code/main.py` 以 `ScriptedLLM` 为调用对象，实现了全部五种工作流模式：

- `prompt_chain(input, steps)` — 顺序执行。
- `route(input, classifier, handlers)` — 分类并分派。
- `parallel_vote(prompt, n, aggregator)` — 运行 N 次，再聚合。
- `orchestrator_workers(task, workers)` — 编排器选择工作单元。
- `evaluator_optimizer(task, proposer, evaluator, max_iter)` — 循环直到通过。

运行：

```text
python3 code/main.py
```

每种模式都会打印自己的行为轨迹（trace）。每种模式的代码总共为 ~10-15 行；框架的代码规模则以千行为单位。

## 实际使用

- 大多数任务直接调用 API 即可。
- 只有模式确实需要持久状态（LangGraph）、actor 模型并发（AutoGen v0.4）或角色模板化（CrewAI）时，才使用框架。
- 如果想采用 Claude Code 的运行框架（harness）形态，又不想从头重建，就使用 Claude Agent SDK（软件开发工具包）。

## 交付成果

`outputs/skill-workflow-picker.md` 为给定的任务描述选择合适的模式，包括选择理由，以及工作流不足以胜任时向智能体重构的路径。

## 练习

1. 实现带置信度阈值的路由。低于阈值 -> 转交人工处理。对于 1 级支持场景，这个阈值应设在什么位置？
2. 为 `parallel_vote` 添加超时限制。如果一次调用挂起，会发生什么？缺少部分投票时，如何聚合结果？
3. 将 `evaluator_optimizer` 改造成多臂老虎机（bandit）：跨迭代保留 top-2 个输出，避免较晚出现的好结果被随后出现的坏结果覆盖。
4. 将提示词串联与路由结合：路由器从三条提示词链中选择一条。测量其 token（词元）成本，并与单个大提示词的方案比较。
5. 从你的生产功能中选一个，画出工作流图并统计步骤数。在这个场景中，智能体真的更好吗？

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|------------------------|
| 工作流 | “预定义流程” | 由工程师掌控的 LLM 与工具调用图 |
| 智能体 | “自主 AI” | 由模型掌控的图；动态指挥工具 |
| 增强型大语言模型 | “带工具的 LLM” | LLM + 搜索 + 工具 + 记忆；基本单元 |
| 提示词串联 | “顺序调用” | 第 N 次调用的输出成为第 N+1 次调用的输入 |
| 路由 | “分类器分派” | 选择由哪条链或哪个模型处理输入 |
| 并行化 | “扇出” | N 次并发调用；通过分块处理或投票来聚合 |
| 编排器—工作单元 | “分派智能体” | 编排器 LLM 动态选择专长 LLM |
| 评估器—优化器 | “提案生成器 + 评判器” | 迭代直到评估器判定通过；Self-Refine 的推广形式 |

## 延伸阅读

- [Anthropic，Building Effective Agents（2024 年十二月）](https://www.anthropic.com/research/building-effective-agents) — 五种工作流模式
- [Anthropic，Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — 配套学科
- [LangGraph 概览](https://docs.langchain.com/oss/python/langgraph/overview) — 有状态图何时值得付出相应成本
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) — 产品化的编排器—工作单元模式
