# 思维树与 LATS：审慎搜索

> 单条思维链（chain-of-thought，CoT）轨迹没有回溯的余地。思维树（Tree of Thoughts，ToT；Yao 等，2023）将推理变成一棵树，并在每个节点上进行自我评估（self-evaluation）。语言智能体树搜索（Language Agent Tree Search，LATS；Zhou 等，2024）在蒙特卡洛树搜索（Monte Carlo Tree Search，MCTS）框架下统一了 ToT、ReAct 和 Reflexion。在 24 点游戏中，准确率从 4%（CoT）升至 74%（ToT）；LATS 在 HumanEval 上达到 92.7% 的 pass@1。

**Type:** Build
**Languages:** Python (stdlib)
**Prerequisites:** 阶段 14 · 01（智能体循环），阶段 14 · 03（Reflexion）
**Time:** ~75 分钟

## 学习目标

- 将推理表述为搜索：节点是“思考步骤（thoughts）”，边是“扩展（expansions）”，价值表示“有多大希望”。
- 仅用标准库实现一个 ToT 风格的广度优先搜索（BFS）树搜索，并使用自我评估评分。
- 将其扩展为一个简化的 LATS MCTS 循环，包含选择（select）/ 扩展（expand）/ 模拟（simulate）/ 回传（backpropagate）。
- 判断何时值得为搜索付出成倍的 token（词元）开销（24 点游戏、代码生成），何时单条轨迹就已足够（简单问答）。

## 要解决的问题

思维链沿着一条线性路径前进。如果第一步出错，后续每一步都会建立在错误的前提上。在 24 点游戏中（用四个数字和 + − × ÷ 运算凑出 24），GPT-4 的 CoT 准确率只有 4%。模型早早选错了子表达式，随后便无法挽回。

推理需要能够提出多个候选项、评估它们、选择有希望的候选项，并在遇到死路时回溯。这就是搜索。思维树和 LATS 是两种典型的形式化方案。

## 核心概念

### 思维树（Yao 等，NeurIPS 2023）

每个节点都是一个连贯的中间步骤（“一次思考”）。每个节点都可以扩展出 K 个子思考步骤。大语言模型（LLM）通过评分提示词（prompt）对每个节点进行自我评估。搜索以 BFS、深度优先搜索（DFS）或束搜索（beam search）的方式探索这棵树。

```text
                     (root: "find 24 from 4 6 4 1")
                    /               |            \
           ("6 - 4 = 2")    ("4 + 1 = 5")    ("4 * 6 = 24")  <- Score: HIGH
              /   \              |                  |
          ...    ...          ...                finish
```

自我评估是关键支柱。论文展示了三种方式：`sure / likely / impossible` 分类、`1..10` 数值评分，以及在候选项之间投票。三种方式在 24 点游戏中都明显优于 CoT（4% -> 74%，使用 GPT-4）。

### LATS（Zhou 等，ICML 2024）

LATS 在 MCTS 框架下统一了 ToT、ReAct 和 Reflexion。LLM 扮演三种角色：

- **策略（Policy）**：提出下一步行动的候选项（ReAct 风格）。
- **价值函数（Value function）**：为尚未完成的轨迹评分（ToT 风格的自我评估）。
- **自我反思器（Self-reflector）**：失败时写下自然语言反思（reflection，Reflexion 风格），并用它重新引导后续的模拟轨迹（rollouts）。

环境反馈（观察结果）也会融入价值函数，使搜索以真实的工具结果为依据，而不只是依赖模型的判断。论文发表时的结果：HumanEval pass@1 为 92.7%，使用 GPT-4（当时最先进的水平，即 SOTA）；WebShop 平均得分为 75.9，使用 GPT-3.5，接近基于梯度的微调（fine-tuning）水平。

### MCTS 极简介绍

每次迭代包含四个阶段：

1. **选择（Select）**：使用树搜索置信上限（UCT，upper confidence bound for trees）从根节点走到叶节点。
2. **扩展（Expand）**：通过策略生成 K 个子节点。
3. **模拟（Simulate）**：从一个子节点出发，按策略模拟推进，再用价值函数（或环境奖励）为叶节点评分。
4. **回传（Backpropagate）**：沿路径向上更新访问次数和价值估计。

UCT 公式：`Q(s, a) + c * sqrt(ln N(s) / N(s, a))`。第一项是利用（exploitation）；第二项是探索（exploration）。根据具体任务调整 `c`。

### 成本的现实

搜索会使 token 用量激增。在 24 点游戏中，ToT 的 token 用量是 CoT 的 100–1000x（倍）。LATS 也类似。搜索并非没有代价；应将搜索留给以下任务：

- 已明确证明单条轨迹不足以完成的任务（24 点游戏、复杂代码）。
- 正确性比实际耗时更重要的任务。
- 拥有低成本、可靠价值函数的任务（代码的单元测试、数学问题的明确目标）。

如果任务只有一个正确答案，而评估器又有噪声，搜索往往会让情况更糟：它会找到一个“得分很高”的错误答案。

### 2026 年的定位

多数生产环境中的智能体（agent）并不运行 LATS。它们运行 ReAct，并以工具结果为依据进行核验（CRITIC，第 05 课）。搜索主要出现在以下专门场景：

- 运行测试并将测试结果用作价值函数的编程智能体（HumanEval 风格）。
- 探索多条查询路径的深度研究智能体。
- LangGraph 子图内侧重规划的工作流。

AlphaEvolve（第 11 课）是 2025 年的极致案例：对代码进行演化搜索（evolutionary search），使用可机器核验的适应度（machine-checkable fitness），取得前沿突破（4x4 矩阵乘法迎来 56 年来的首次改进）。

```figure
tree-of-thoughts
```

## 动手实现

`code/main.py` 实现了：

- 在一个简化的“选择算术运算”任务上运行的微型 ToT BFS。
- 在同一任务上运行的简化 LATS MCTS 循环（Select / Expand / Simulate / Backpropagate），使用 UCT 进行选择。
- 一个将符号计算评分（symbolic score）与自我评估评分结合起来的价值函数。

运行：

```text
python3 code/main.py
```

运行轨迹展示了两者的对比：ToT 使用 BFS，为每个节点扩展出三个候选项；LATS 则通过 MCTS 收敛到最佳模拟轨迹。程序会打印两者的 token 数量。

## 实际使用

LangGraph 以子图模式提供 ToT 风格的探索；LangChain 团队关于 LATS 的博客文章（2024 年五月）是参考教程。LlamaIndex 提供了一个 `TreeOfThoughts` 智能体。对 2026 年的大多数生产智能体来说，这种模式只有在满足 `if task_complexity > threshold: use_search()` 这一条件时才会启用；参见第 05 课的评估器—优化器模式。

## 交付成果

`outputs/skill-search-policy.md` 根据任务形态、预算和评估器保真度（evaluator fidelity），在沿单条轨迹运行的 ReAct、ToT、LATS 和演化搜索之间进行选择。

## 练习

1. 分别以 UCT c=0.1 和 c=2.0 运行简化的 LATS。运行轨迹有什么变化？
2. 将价值函数替换为噪声更大的评分器（加入随机扰动）。MCTS 还能找到最佳叶节点吗？它能容忍的最低信噪比（signal-to-noise）是多少？
3. 实现束搜索版 ToT（每层保留 top-k），并与 BFS 比较。在 token 预算紧张时，哪一种更好？
4. 阅读 LATS 第 5.1 节。复现 HumanEval 的轨迹数量：需要多少条模拟轨迹才能达到报告中的 pass@1？
5. 阅读 LATS 论文中关于“何时 LATS 帮助较小”的讨论。用一段话写出根据任务形态选择搜索策略的决策规则。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|------------------------|
| 思维树（Tree of Thoughts） | “带分支的 CoT” | Yao 等提出的思考节点树，对节点进行自我评估 |
| LATS | “用于 LLM 的 MCTS” | Zhou 等提出，在 MCTS 框架下统一 ToT + ReAct + Reflexion |
| UCT | “置信上限” | 用于选择的公式，平衡利用（Q）与探索（ln N / n） |
| 价值函数 | “这个状态有多好” | 通过提示词让 LLM 给出的评分，或环境奖励；用于回传 |
| 策略 | “行动提议者” | ReAct 风格的生成器；输出下一步思考/行动的候选项 |
| 模拟轨迹（Rollout） | “模拟出的轨迹” | 按策略从一个节点走到叶节点，再用价值函数评分 |
| 回传（Backpropagate） | “更新祖先节点” | 将叶节点的奖励沿路径向上传递，更新访问次数和 Q |
| 搜索成本 | “token 用量爆炸” | token 用量达到 CoT 的 100-1000x（倍，24 点游戏）；采用前先做好预算 |

## 延伸阅读

- [Yao et al., Tree of Thoughts (arXiv:2305.10601)](https://arxiv.org/abs/2305.10601)：奠基论文
- [Zhou et al., LATS (arXiv:2310.04406)](https://arxiv.org/abs/2310.04406)：结合 Reflexion 反馈的 MCTS
- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)：用于搜索的子图模式
- [AlphaEvolve (arXiv:2506.13131)](https://arxiv.org/abs/2506.13131)：使用程序化评估器的演化搜索
