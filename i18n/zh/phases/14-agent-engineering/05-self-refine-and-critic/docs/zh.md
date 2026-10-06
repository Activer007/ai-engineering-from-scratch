# Self-Refine 与 CRITIC：输出迭代改进

> Self-Refine（Madaan 等，2023）让一个大语言模型（LLM）在循环中承担三种角色：生成（generate）、反馈（feedback）、改进（refine）。在 7 项任务上的平均绝对提升为 +20。CRITIC（Gou 等，2023）通过外部工具进行核验，增强反馈步骤的可靠性。到了 2026 年，各个框架都以“评估器—优化器（evaluator-optimizer）”（Anthropic）或安全护栏（guardrail）循环（OpenAI Agents SDK，SDK 即软件开发工具包）的形式提供这一模式。

**Type:** Build
**Languages:** Python (stdlib)
**Prerequisites:** 阶段 14 · 01（智能体循环）、阶段 14 · 03（Reflexion）
**Time:** ~60 分钟

## 学习目标

- 列出 Self-Refine 的三种提示词（prompt）：生成、反馈、改进，并解释为什么历史信息对改进提示词很重要。
- 解释 CRITIC 的关键洞见：没有外部信息作为依据时，LLM 的自我核验（self-verification）并不可靠。
- 仅用标准库实现一个带历史记录、可选用外部核验器（external verifier）的 Self-Refine 循环。
- 将这一模式对应到 Anthropic 的“评估器—优化器”工作流和 OpenAI Agents SDK 的输出安全护栏（output guardrails）。

## 要解决的问题

智能体（agent）生成了一个差一点就正确的答案。可能某行代码有语法错误，可能摘要太长，也可能计划遗漏了某种边界情况。你希望智能体对自己的输出作出评议（critique），然后加以修正。

Self-Refine 表明，用单一模型就能做到这一点，无需训练数据，也无需强化学习（RL）。但有一个问题：对于确凿的事实，LLM 不擅长自我核验。CRITIC 给出的解决办法是：通过外部工具（搜索、代码解释器、计算器、测试运行器）完成核验步骤。

这两篇论文共同定义了 2026 年迭代改进的默认做法：生成、核验（尽可能借助外部工具）、改进，在核验器判定通过时停止。

## 核心概念

### Self-Refine（Madaan 等，NeurIPS 2023）

一个 LLM，三种角色：

```text
generate(task)            -> output_0
feedback(task, output_0)  -> critique_0
refine(task, output_0, critique_0, history) -> output_1
feedback(task, output_1)  -> critique_1
refine(task, output_1, critique_1, history) -> output_2
...
stop when feedback says "no issues" or budget exhausted.
```

关键细节：`refine` 会看到完整历史，即所有先前的输出和评议，从而避免重复犯错。论文对此做了消融实验：移除历史后，质量会大幅下降。

主要结果：在 7 项任务（数学、代码、首字母缩略词、对话）上的平均绝对提升为 +20，所用模型包括 GPT-4。无需训练，无需外部工具，只用单一模型。

### CRITIC（Gou 等，arXiv:2305.11738，v4，2024 年二月）

Self-Refine 的弱点在于：反馈步骤是由 LLM 给自己评分。对于事实性陈述，这并不可靠，因为幻觉（hallucination）往往在生成它的模型看来也很有说服力。CRITIC 用 `verify(task, output, tools)` 替代 `feedback(task, output)`，其中 `tools` 包括：

- 用于核查事实性陈述的搜索引擎。
- 用于检查代码正确性的代码解释器。
- 用于算术运算的计算器。
- 领域专用核验器（单元测试、类型检查器、静态检查工具）。

核验器生成以工具结果为依据的结构化评议（structured critique）。随后，改进器（refiner）以这份评议为条件进行改进。

主要结果：CRITIC 在事实类任务上优于 Self-Refine，因为它的评议有外部依据。在没有外部核验器的任务（创意写作、格式调整）上，CRITIC 就退化为 Self-Refine。

### 停止条件

常见的形式有两种：

1. **核验器判定通过。** 外部测试返回成功。在有条件使用时优先采用（单元测试、类型检查器、安全护栏断言）。
2. **不再给出反馈。** 模型说“输出没有问题”。成本更低，但不可靠；需要配合迭代次数上限。

2026 年的默认做法是将二者结合：“若核验器判定通过 OR 模型说没有问题 AND iterations >= 2 OR iterations >= max_iterations，则停止。”

### 评估器—优化器（Evaluator-Optimizer，Anthropic，2024）

Anthropic 在 2024 年十二月的文章中将其列为五种工作流模式之一。其中有两种角色：

- 评估器（Evaluator）：给输出评分，并生成评议。
- 优化器（Optimizer）：根据评议修改输出。

循环执行，直到评估器判定通过。这就是 Anthropic 表述下的 Self-Refine/CRITIC。Anthropic 补充的关键工程细节是：评估器与优化器的提示词应该有显著差异，避免模型只是机械地认可输出。

### OpenAI Agents SDK 输出安全护栏

OpenAI Agents SDK 以“输出安全护栏”的形式提供这一模式。安全护栏是一种验证器，会对智能体的最终输出运行检查。如果安全护栏被触发（抛出 `OutputGuardrailTripwireTriggered`），输出就会被拒绝，智能体可以重试。安全护栏可以调用工具（CRITIC 风格），也可以是纯函数（Self-Refine 风格）。

### 2026 年的常见陷阱

- **机械认可循环（rubber-stamp loop）。** 同一模型使用风格相同的提示词进行生成和评议，最终总会得出“我看没问题”的结论。应使用结构上不同的提示词，或用一个更小、更便宜的模型来作评议。
- **过度改进（over-refinement）。** 每轮改进都会增加延迟和 token（词元）用量。将预算设为 1-3 轮；超过这个范围就转交人工审查。
- **在简单任务上使用 CRITIC。** 如果没有外部核验器，CRITIC 就退化为 Self-Refine；不要为桩核验器付出额外延迟。

```figure
self-refine
```

## 动手实现

`code/main.py` 在一个玩具任务上实现了 Self-Refine 和 CRITIC：根据给定主题生成简短的项目符号列表。核验器检查格式（3 个条目，每条少于 60 个字符）。CRITIC 另外加入一个外部“事实核验器”，对已知幻觉施加惩罚。

组件：

- `generate`：脚本化生成器。
- `feedback`：LLM 风格的自我评议。
- `verify_external`：CRITIC 风格、以外部信息为依据的核验器。
- `refine`：根据历史记录重写输出。
- 停止条件：核验器判定通过，或最多迭代 4 次。

运行：

```text
python3 code/main.py
```

比较 Self-Refine 和 CRITIC 的运行结果。CRITIC 能发现 Self-Refine 漏掉的事实错误，因为外部核验器具备自我评议器所没有的外部依据。

## 实际使用

Anthropic 的评估器—优化器就是用适合 Claude 的术语来描述这一模式。OpenAI Agents SDK 的输出安全护栏具有 CRITIC 的形式，因为安全护栏可以调用工具。LangGraph 提供的反思节点与 Self-Refine 相似。Google 的 Gemini 2.5 Computer Use 增加了逐步安全评估器，这是 CRITIC 的一种变体：每个行动都在提交前进行核验。

## 交付成果

`outputs/skill-refine-loop.md` 根据任务形式、核验器是否可用以及迭代预算，配置一个评估器—优化器循环。它会生成用于生成器、评估器/核验器、优化器的提示词，以及一套停止策略。

## 练习

1. 以 max_iterations=1 运行玩具示例。CRITIC 仍然有帮助吗？
2. 将外部核验器换成一个有噪声的核验器（随机产生 30% 的误报）。循环会怎么做？这就是 2026 年大多数安全护栏技术栈的现实。
3. 实现一个“生成器和评议器使用不同模型”的变体：大模型生成，小模型评议。它比使用同一模型更好吗？
4. 阅读 CRITIC 第 3 节（arXiv:2305.11738 v4）。说出三类核验工具，并各举一个例子。
5. 将 OpenAI Agents SDK 的 `output_guardrails` 对应到 CRITIC 的核验器角色。这个 SDK 哪些地方做得不对，哪些地方做对了？

## 关键术语

| 术语 | 人们常怎么说 | 实际含义 |
|------|----------------|------------------------|
| Self-Refine | “能自行修正的 LLM” | 在一个模型中执行生成 -> 反馈 -> 改进循环，并保留历史 |
| CRITIC | “以工具结果为依据的核验” | 用外部核验器（搜索、代码、计算器、测试）替代反馈 |
| 评估器—优化器 | “Anthropic 工作流模式” | 两种角色：评估器评分，优化器修改，循环直至收敛 |
| 输出安全护栏 | “事后检查” | OpenAI Agents SDK 中的验证器，在智能体生成输出后运行 |
| 核验步骤 | “评议阶段” | 决定成败的关键选择：以外部信息为依据，还是自行评分 |
| 改进历史 | “模型已经尝试过什么” | 将先前输出 + 评议放在改进提示词的开头；移除后质量会骤降 |
| 机械认可循环 | “自我附和失效” | 使用相同提示词的评议只会返回“看起来不错”；用结构上不同的提示词解决 |
| 停止条件 | “收敛测试” | 核验器判定通过 OR 没有反馈 AND 迭代次数上限；绝不只用单一条件 |

## 延伸阅读

- [Madaan 等，Self-Refine（arXiv:2303.17651）](https://arxiv.org/abs/2303.17651)：该方法的原始论文
- [Gou 等，CRITIC（arXiv:2305.11738）](https://arxiv.org/abs/2305.11738)：以工具结果为依据的核验
- [Anthropic，Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)：评估器—优化器工作流模式
- [OpenAI Agents SDK 文档](https://openai.github.io/openai-agents-python/)：具有 CRITIC 形式的输出安全护栏核验器
