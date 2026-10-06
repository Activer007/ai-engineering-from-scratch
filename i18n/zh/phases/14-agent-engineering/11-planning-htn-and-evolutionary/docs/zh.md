# 使用 HTN 与演化搜索进行规划

> 符号规划（symbolic planning）适用于计划（plan）可证明正确（provably correct）的场景。演化代码搜索（evolutionary code search）适用于适应度函数（fitness function）可由机器核验的场景。ChatHTN (2025) 与 AlphaEvolve (2025) 展示了这两种方法与大语言模型（LLM）结合后各自能实现什么。

**Type:** Build
**Languages:** Python (stdlib)
**Prerequisites:** 阶段 14 · 02（ReWOO 与 Plan-and-Execute）
**Time:** ~75 分钟

## 学习目标

- 解释分层任务网络（Hierarchical Task Networks，HTN）：任务（task）、方法（method）、规划算子（operator）、前置条件（precondition）与效果（effect）。
- 说明 ChatHTN 的混合循环（hybrid loop）：符号搜索（symbolic search）结合 LLM 回退（LLM fallback）分解（decomposition）。
- 解释 AlphaEvolve 的演化循环，以及为什么它必须有程序化评估器（programmatic evaluator）才能工作。
- 仅用标准库（stdlib）实现两个简化示例（toy）：一个 HTN 规划器（planner）和一个演化搜索（evolutionary search）。

## 要解决的问题

ReWOO（第 02 课）、Plan-and-Execute（规划后执行）和 ReAct 涵盖了大多数智能体（agent）规划场景。但它们有两类场景处理得不够好：

1. **正确性可证明的计划。** 调度（scheduling）、飞行路径规划（flight pathing）、合规工作流（compliance workflows）：计划必须在构造时就保证健全性（soundness）。LLM 给出的计划即使表达流畅，只要偶尔会凭空编造一个步骤，就不可接受。
2. **适应度函数可由机器核验的优化问题。** 矩阵乘法（matrix multiplication）、调度启发式方法（scheduling heuristics）、编译器优化处理阶段（compiler passes）：目标不是“正确的计划”，而是“最好的计划”。

HTN 规划与 AlphaEvolve 解决的是两种不同的问题。两者都用 LLM 增强自身能力，而不是替代自身机制。

## 核心概念

### 分层任务网络

HTN 包括：

- **任务**：复合任务（compound task，需要分解）与原始任务（primitive task，可直接执行）。
- **方法**：将复合任务分解为子任务（subtask）的方式，带有前置条件。
- **规划算子**：带有前置条件和效果的原始动作。
- **状态（state）**：一组事实（fact）。

规划（planning）：给定目标任务（goal task）与初始状态（initial state），找到一种将其分解为原始规划算子（primitive operator）的方案，使各算子的前置条件按顺序得到满足。

HTN 的历史早于 LLM，至今仍是构建可证明正确的计划时的参照。

### ChatHTN（Gopalakrishnan 等，2025）

ChatHTN（arXiv:2505.11814）将符号 HTN 与 LLM 查询交错进行：

1. 尝试用现有方法分解当前复合任务。
2. 如果没有适用的方法，就询问 LLM：“在状态 `s` 下，你会怎样分解 `task`？”
3. 将 LLM 的响应转换为候选子任务。
4. 根据规划算子的 schema（结构定义）进行校验，拒绝无效分解。
5. 递归处理（recurse）。

论文的核心主张是：生成的每个计划都可证明具有健全性，因为 LLM 的建议只会作为候选分解进入流程，绝不会直接修改计划。符号层负责保证正确性；LLM 扩充方法库（method library）。

在线方法学习（online method learning，OpenReview `gwYEDY9j2x`，2025 年的后续研究）引入了一个学习器（learner），通过回归（regression）对 LLM 生成的分解进行泛化（generalize），将 LLM 查询频率最多降低 75%。

### AlphaEvolve（Novikov 等，2025）

AlphaEvolve（arXiv:2506.13131，DeepMind，June 2025）走的是另一条路线：由 Gemini 2.0 Flash/Pro 集成（ensemble）协调演化代码搜索。

循环过程：

1. 从一个种子程序（seed program）和一个程序化评估器开始，后者返回适应度分数（fitness score）。
2. LLM 集成提出变异（mutation）方案。
3. 让评估器评估这些变异方案。
4. 保留最好的，再次进行变异。

已发表的成果：

- 在 4x4 复数矩阵（complex matrix）乘法上，首次实现了 56 年来对 Strassen 方法的改进，仅需 48 次标量乘法（scalar multiplications）。
- 通过一种 Borg 调度启发式方法，为 Google 收回了 0.7% 的算力。
- 在一项前沿工作负载（frontier workload）上，让 FlashAttention 加速 32%。

硬性约束是：适应度函数必须可由机器核验。对自然语言回答进行演化搜索不会收敛（converge）。

### 何时选择哪一种

| 问题类别 | 采用的方法 | 原因 |
|---------------|-----|-----|
| 带有硬约束（hard constraints）的调度 | HTN + ChatHTN | 可证明的健全性 |
| 编译器优化（compiler optimization） | AlphaEvolve | 可机器核验的适应度（machine-checkable fitness） |
| 多步骤任务执行 | ReAct / ReWOO | LLM 参与循环，但没有形式化保证（formal guarantees） |
| 以测试为依据改进代码 | AlphaEvolve | 测试就是评估器 |
| 受规则约束的自动化（policy-bound automation） | HTN | 前置条件对规则进行编码 |

### 这种模式会在哪里出问题

- **没有规划算子的 HTN。** 缺少前置条件与效果的 schema，健全性主张就无法成立。ChatHTN 中“由 LLM 建议分解”的做法，需要 schema 来拒绝无效动作。
- **没有真正评估器的 AlphaEvolve。** “问 LLM 代码是否更好”不是适应度函数。评估器必须是确定性的（deterministic），而且速度要快。
- **过度设计（over-engineering）。** 大多数智能体任务都不需要这两种方法。先考虑 ReAct 或 ReWOO。

```figure
htn-tree-expand
```

## 动手实现

`code/main.py` 实现了两个简化示例：

- 一个仅使用标准库的 HTN 规划器，包含规划算子、方法、前置条件、效果，以及一个 `LLMFallback`：当没有方法匹配某个复合任务时，它就会介入。这里的“LLM”是按预设脚本分解的组件（scripted decomposer），因此规划器可以离线运行。
- 一个仅使用标准库、针对算术程序（arithmetic programs）的演化搜索：逐步构建表达式（expressions），使其在测试集（test set）上的输出将 `|f(x) - target|` 降至最小。评估器是确定性的。

运行方式：

```text
python3 code/main.py
```

运行轨迹（trace）展示了 HTN 规划器如何分解复合任务（包括一次规划中途的 LLM 回退），以及演化循环如何收敛到目标表达式。

## 实际使用

- **HTN 规划器**：可以使用 `pyhop`、`SHOP3`，也可以自行构建，以实现面向特定领域的规则执行（policy enforcement）。
- **ChatHTN**：目前是研究代码；这种模式（符号机制 + LLM 回退）可以直接迁移到任何 HTN 规划器。
- **AlphaEvolve**：见 DeepMind 的论文；这种模式（集成 + 评估器）可以复现。OpenEvolve 及类似的开源分叉正在出现。
- **智能体框架（agent frameworks）**：目前还没有框架为 HTN 或 AlphaEvolve 提供一等支持（first-class）。可以将其构建为子智能体（subagent）或后台工作单元（background worker）。

## 交付成果

`outputs/skill-hybrid-planner.md` 会生成一个混合规划器脚手架（hybrid planner scaffold，可选 HTN 或演化搜索），并明确限定 LLM 的职责。

## 练习

1. 为 HTN 规划器加入回溯（backtracking）：当某个规划算子的后置条件（postcondition）在运行时（runtime）不成立时，回滚（rollback）并尝试下一个方法。
2. 为 ChatHTN 添加 LLM 方法缓存（method cache）：当 LLM 在状态模式（state pattern）`P` 下分解任务 `T` 时，存储结果。下次调用时先重新检查方法库。
3. 将演化搜索的评估器替换为真正的测试套件（test suite）。通过演化得到一个能通过 20 个测试用例（test cases）的排序函数（sort function）；报告收敛需要多少代（generations）。
4. 阅读 AlphaEvolve 的评估器设计说明。为你关心的领域设计一个评估器，例如 SQL 查询优化、测试套件最小化（test-suite minimization）或部署 YAML。
5. 将两者结合：用 HTN 将复合任务分解为子任务，再对每个子任务的原始规划算子使用演化搜索。它在哪些场景表现出色，又会在哪些场景造成过度设计？

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|------------------------|
| HTN | “分层规划器” | 通过规划算子、前置条件与效果进行任务分解 |
| 方法 | “分解规则” | 将复合任务拆分为子任务的方式 |
| 规划算子 | “原始动作” | 带有前置条件和效果的具体步骤 |
| ChatHTN | “LLM + HTN” | 没有方法匹配时，符号规划器会询问 LLM |
| AlphaEvolve | “演化代码搜索” | LLM 集成对代码进行变异；确定性评估器进行选择 |
| 适应度函数 | “评估器” | 针对输出计算的、确定性的、可由机器核验的分数 |
| 在线方法学习 | “缓存的 LLM 分解” | 存储并泛化 LLM 计划，以降低查询成本 |

## 延伸阅读

- [Gopalakrishnan et al., ChatHTN (arXiv:2505.11814)](https://arxiv.org/abs/2505.11814)：符号机制与 LLM 结合的混合规划器
- [Novikov et al., AlphaEvolve (arXiv:2506.13131)](https://arxiv.org/abs/2506.13131)：通过 LLM 变异进行演化代码搜索
- [Anthropic, Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)：何时使用规划器，何时使用简单循环
