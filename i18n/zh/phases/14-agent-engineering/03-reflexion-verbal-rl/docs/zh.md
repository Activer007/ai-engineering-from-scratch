# Reflexion：语言强化学习

> 基于梯度的强化学习（RL）需要数千次尝试和一个 GPU 集群，才能修正一种失败模式。Reflexion（Shinn 等人，NeurIPS 2023）用自然语言来完成这件事：每次尝试失败后，智能体（agent）都会写下一条反思，将其存入情景记忆（episodic memory），并以这份记忆为条件开展下一次尝试。Letta 的空闲时计算（sleep-time compute）、Claude Code 的 CLAUDE.md 经验记录，以及 pro-workflow 的 learn-rule，背后都是这一模式。

**Type:** Build
**Languages:** Python (stdlib)
**Prerequisites:** 第 14 阶段 · 01（智能体循环），第 14 阶段 · 02（ReWOO）
**Time:** ~60 分钟

## 学习目标

- 说出 Reflexion 的三个组件（行动者 Actor、评估器 Evaluator、自我反思器 Self-Reflector），以及情景记忆的作用。
- 用标准库实现一个 Reflexion 循环，包含二值评估器、反思缓冲区和从头重新开始的尝试。
- 针对给定任务，在标量、启发式和自我评估这几类反馈来源中作出选择。
- 解释为什么语言强化能够发现并纠正一些错误，而基于梯度的 RL 需要数千次尝试才能修正这些错误。

## 要解决的问题

智能体没能完成一项任务。在标准 RL 中，你会再运行数千次尝试，计算梯度，更新权重。这既昂贵又缓慢，而且大多数生产环境中的智能体都没有足够的训练预算来应对每一次失败。

Reflexion（Shinn 等人，arXiv:2303.11366）提出了另一个问题：如果智能体只是思考自己为什么失败，再把这个想法放进提示词（prompt）里重试，会怎样？没有权重更新，没有梯度，只有保存在各次尝试之间的自然语言。

结果是：在 ALFWorld 上，它超过了 ReAct 和其他未经微调（fine-tuning）的基线。在 HotpotQA 上，它比 ReAct 有所提升。在代码生成（HumanEval/MBPP）上，它达到了当时的最先进水平。这一切都没有进行哪怕一次梯度更新。

## 核心概念

### 三个组件

```text
Actor         : generates a trajectory (ReAct-style loop)
Evaluator     : scores the trajectory — binary, heuristic, or self-eval
Self-Reflector: writes a natural-language reflection on the failure
```

再加上一个数据结构：

```text
Episodic memory: list of prior reflections, prepended to the next trial's prompt
```

每次尝试都会运行行动者，由评估器为这次尝试评分。如果分数较低，自我反思器就会生成一条反思（“我选错了工具，因为我把问题误读成了在问 X，而它其实问的是 Y”）。这条反思会进入情景记忆。下一次尝试会从头开始，但能看到这条反思。

### 三类评估器

1. **标量（Scalar）**：来自外部的二值信号。ALFWorld 中是成功或失败，HumanEval 中是测试通过或不通过。这种方式最简单，信号也最明确。
2. **启发式（Heuristic）**：预先定义的故障特征。“如果智能体连续两次生成相同的行动，就标记为陷入停滞。”“如果轨迹超过 50 步，就标记为效率低下。”
3. **自我评估（Self-evaluated）**：大语言模型（LLM）为自己的轨迹评分。在没有真实值可用时需要这种方式。它的信号较弱，适合搭配以工具结果为依据的核验（第 05 课，CRITIC）。

2026 年的默认做法是混合使用：有标量反馈就用标量反馈，没有时用自我评估，再以启发式规则作为安全护栏（guardrail）。

### 为什么这个模式能推广

与其说 Reflexion 是一种新算法，不如说它是一个有了名称的模式。几乎每个生产环境中的“自我修复”智能体，都在运行它的某种变体：

- Letta 的空闲时计算（第 08 课）：由一个独立的智能体反思过去的对话，并写入记忆块。
- Claude Code 的 `CLAUDE.md` / “保存记忆”模式：将反思记为经验，放在后续会话的开头。
- pro-workflow 的 `/learn-rule` 命令：将纠正意见记为明确的规则。
- LangGraph 的反思节点：由一个节点为输出评分，并在需要时转入改进流程。

它们都源于同一个认识：自然语言足以承载丰富的信息，把“我从失败中学到了什么”传递到后续运行中。

### 何时有效，何时无效

Reflexion 在以下情况下有效：

- 有明确的失败信号（测试失败、工具报错、答案错误）。
- 任务类别可重复（可以再次提出同一类型的问题）。
- 反思有机会改善轨迹（有足够的行动预算）。

Reflexion 在以下情况下没有帮助：

- 智能体第一次尝试就已经成功。
- 失败来自外部（网络中断、工具损坏）：反思“网络中断了”并不能帮助后续运行。
- 反思变成了迷信：为一次偶发的不稳定运行编出一套说辞并存下来。

2026 年的一个陷阱是记忆陈旧化（memory rot）。反思不断累积，其中有些已经过时或本来就不正确；随着情景记忆缓冲区变大，后续运行会越来越慢。缓解方法包括定期压缩整理（第 06 课）、为反思设置 TTL（存活期限），或者使用一个独立的空闲时清理智能体（Letta）。

```figure
react-trace
```

## 动手实现

`code/main.py` 用一个玩具谜题实现了 Reflexion：生成一个包含 3 个元素的列表，使其元素之和等于目标值。行动者输出候选列表；评估器检查总和；自我反思器写下一行文字，说明哪里出了问题。这条反思会进入情景记忆，供下一次尝试使用。

组件如下：

- `Actor`：一个按脚本运行的策略，看到反思后会改进。
- `Evaluator.binary()`：根据总和是否等于目标值，判定通过或失败。
- `SelfReflector`：生成一行关于失败原因的诊断。
- `EpisodicMemory`：一个带有 TTL 语义的有界列表。

运行：

```text
python3 code/main.py
```

行为轨迹展示了三次尝试。第 1 次尝试失败，系统存下一条反思；第 2 次尝试看到了这条反思，有所改进但仍然失败；第 3 次尝试成功。与不使用反思的基线运行相比，基线始终停留在第 1 次尝试的答案上。

## 实际使用

LangGraph 提供了反思节点这一模式。Claude Code 的 `/memory` 命令和 pro-workflow 的 `/learn-rule` 将情景记忆缓冲区外置为一个 markdown 文件。Letta 的空闲时计算会在空闲期间运行自我反思器，让主智能体仍以响应延迟为主要约束。OpenAI Agents SDK（软件开发工具包）不直接提供 Reflexion；你需要用一个根据评分拒绝轨迹的自定义 Guardrail（安全护栏），以及一个能在多次运行之间保留记忆的 `Session` 来构建它。

## 交付成果

`outputs/skill-reflexion-buffer.md` 用于创建并维护一个情景记忆缓冲区，包含反思记录、TTL 和去重功能。给定一种任务类别和一次失败，它会输出一条真正有助于下一次尝试的反思，而不是泛泛地说“再仔细一点”。

## 练习

1. 把二值评估器换成返回距离度量（距离目标值有多远）的标量评估器。它会收敛得更快吗？
2. 给反思加上 10 次尝试的 TTL。超过这个期限后，较早的反思是有害还是有帮助？
3. 实现一个启发式评估器：如果重复了相同的行动，就把这次尝试标记为陷入停滞。它会怎样与自我反思器交互？
4. 让 Reflexion 使用一个刻意忽略反思的对抗性行动者运行。至少需要怎样设计反思提示词，才能迫使行动者注意到这些反思？
5. 阅读 Reflexion 论文中关于 AlfWorld 的第 4 节。从概念上复现成功率提高 130% 的结果：与原始 ReAct 相比，关键差别是什么？

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|------------------------|
| Reflexion | “自我纠正” | Shinn 等人于 2023 年提出：行动者、评估器、自我反思器，加上情景记忆 |
| 语言强化 | “不使用梯度的学习” | 放在下一次尝试的提示词开头的自然语言反思 |
| 情景记忆 | “按任务保存的反思” | 为一种任务类别保存既往反思的有界缓冲区 |
| 标量评估器 | “二值成功信号” | 来自真实值的通过/失败判定或数值评分 |
| 启发式评估器 | “基于模式的检测器” | 预先定义的故障特征，例如循环停滞、步数过多 |
| 自我评估器 | “让 LLM 评判自己的行为轨迹” | 没有真实值时采用的较弱反馈方案，应搭配以工具结果为依据的核验 |
| 记忆陈旧化 | “过时的反思” | 情景记忆缓冲区被过时条目填满，可用压缩整理/TTL 解决 |
| 空闲时反思 | “异步自我反思” | 将自我反思器移出关键响应路径运行，让主智能体保持快速响应 |

## 延伸阅读

- [Shinn et al., Reflexion: Language Agents with Verbal Reinforcement Learning (arXiv:2303.11366)](https://arxiv.org/abs/2303.11366)：该方法的原始论文
- [Letta, Sleep-time Compute](https://www.letta.com/blog/sleep-time-compute)：生产环境中的异步反思
- [Anthropic, Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)：将情景记忆缓冲区作为上下文的一部分进行管理
- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)：反思节点模式
