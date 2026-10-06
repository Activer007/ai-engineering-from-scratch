# 工具使用与函数调用

> Toolformer（Schick 等，2023）开创了自监督工具调用标注。Berkeley 函数调用排行榜（Berkeley Function Calling Leaderboard，BFCL）V4（Patil 等，2025）确立了 2026 年的标准：评分权重为 40% 智能体类（agentic）、30% 多轮类（multi-turn）、10% Live（真实用户提示词类）、10% Non-Live（合成测试用例类）、10% 幻觉类（hallucination）。单轮问题已经解决。记忆、动态决策和长时程工具调用链则尚未解决。

**Type:** Build
**Languages:** Python (stdlib)
**Prerequisites:** 阶段 14 · 01（智能体循环），阶段 13 · 01（函数调用深入解析）
**Time:** ~60 分钟

## 学习目标

- 解释 Toolformer 的自监督训练信号：只有执行工具后能降低下一 token（词元）预测损失，才保留工具调用标注。
- 列出 BFCL V4 的五类评测及各自衡量的内容。
- 用标准库实现一个工具注册表（tool registry），支持 schema（结构定义）校验、参数类型转换和执行沙箱隔离（sandboxing）。
- 分析 2026 年三个尚未解决的问题：长时程工具调用链、动态决策和记忆。

## 要解决的问题

早期的工具使用关注：模型能否预测出正确的函数调用（function calling）？现代工具使用关注：模型能否在具备记忆、只能观测到部分环境信息的情况下，连续衔接工具执行 40 步，从工具故障中恢复，同时不臆造并不存在的工具？

Toolformer 奠定了基线：模型可以通过自监督学习何时调用工具。BFCL V4 定义了 2026 年的评测目标。生产环境中的智能体（agent）所要应对的，正是两者之间的差距。

## 核心概念

### Toolformer（Schick 等，NeurIPS 2023）

思路：让模型在自己的预训练语料库中标注候选 API（应用程序编程接口）调用。逐一执行这些候选调用。只有在加入工具结果后，下一 token 的预测损失降低，才保留该标注。随后在筛选后的语料库上进行微调（fine-tuning）。

涵盖的工具：计算器、问答（QA）系统、搜索引擎、翻译器和日历。自监督信号只关心工具是否有助于预测文本，不使用人工标签。

关于规模的结果：工具使用能力会随着规模增大而涌现。工具调用标注会损害较小模型的表现，却能让较大模型受益。这就是为什么 2026 年的前沿模型内置了较强的工具使用能力，而大多数 7B 模型需要专门进行工具使用微调才能可靠工作。

### Berkeley Function Calling Leaderboard V4（Patil 等，ICML 2025）

BFCL 是 2026 年事实上的评测标准。V4 的评分权重构成如下：

- **智能体类（Agentic，40%）** — 完整的智能体轨迹：记忆、多轮交互、动态决策。
- **多轮类（Multi-Turn，30%）** — 包含工具调用链的交互式对话。
- **Live（10%）** — 用户提交的真实提示词（prompt），其分布更难应对。
- **Non-Live（10%）** — 合成测试用例。
- **幻觉类（Hallucination，10%）** — 检测何时不应调用任何工具。

V3 引入了基于状态的评测：执行一串工具调用后，检查 API 的实际状态（例如“文件是否已创建？”），而不是匹配工具调用的抽象语法树（AST）。V4 新增了网页搜索、记忆和格式敏感性类别。

2026 年的关键发现：单轮函数调用已接近解决。失败集中在记忆（跨轮次携带上下文）、动态决策（根据先前结果选择工具）、长时程调用链（经过 20+ 步后发生漂移）和幻觉检测（没有合适工具时拒绝调用）上。

### 工具 schema

每家提供商都有自己的 schema。它们在细节上不同，但具有相同的基本形态：

```text
name: string
description: string (what it does, when to use it)
input_schema: JSON Schema (properties, required, types, enums)
```

Anthropic 直接使用 `input_schema`。OpenAI 使用 `function.parameters`。两者都接受 JSON Schema。描述起着关键作用：模型会阅读描述来选择正确的工具。糟糕的工具描述是选错工具这一类失败的首要（#1）根因。

### 实参校验

不要信任任何工具调用。需要校验：

1. **类型强制转换。** schema 要求 int 时，模型可能返回字符串 "5"。含义明确时进行转换；有歧义时则拒绝。
2. **枚举值校验。** 如果 schema 声明 `status in {"open", "closed"}`，模型却输出 `"in_progress"`，就拒绝该调用，并返回说明原因的错误。
3. **必填字段。** 缺少必填字段 -> 立即向模型返回错误观察结果，而不是让程序崩溃。
4. **格式校验。** 日期、电子邮件地址、URL：使用相应的解析器校验，而不是正则表达式。

每次校验失败都应返回结构化观察结果，让模型能够以正确的结构重试。

### 并行工具调用

现代提供商支持在一个助手轮次中发出并行工具调用。循环过程如下：

1. 模型发出 3 个工具调用，各自带有不同的 `tool_use_id`。
2. 运行时（runtime）执行这些调用；如果它们相互独立，就并行执行。
3. 每个结果都以 `tool_result` 块的形式返回，并通过 `tool_use_id` 关联到对应调用。

工程规则：关联 ID（correlation ID）至关重要。把它们弄反，就会将工具调用与错误的结果配对。

### 沙箱隔离

工具执行是沙箱边界。详见第 09 课。简而言之，每个工具都应指定读写访问范围、网络访问、超时限制和内存上限。通用的 `run_shell(cmd)` 是危险信号；用途明确的 `git_status()` 更安全。

```figure
tool-routing
```

## 动手实现

`code/main.py` 实现了一个具备生产系统形态的工具注册表：

- JSON Schema 子集校验器，仅使用标准库。
- 工具注册信息包含描述、输入 schema、超时限制和执行器。
- 参数类型转换与枚举值校验。
- 带有关联 ID 的并行工具分派。
- 以结构化字符串形式返回的错误观察结果。

运行：

```text
python3 code/main.py
```

行为轨迹（trace）展示了一个微型智能体在一个轮次内调用三个工具，其中一次调用被故意构造成不合法的形式，因此遭到拒绝，并返回说明原因的错误，让模型可以据此采取行动。

## 实际使用

每家提供商都有自己的工具 schema：Anthropic、OpenAI、Gemini、Bedrock。如果需要支持多家提供商，就使用转换层，例如 OpenAI Agents SDK（SDK 指软件开发工具包）、Vercel AI SDK 或 LangChain 工具适配器。BFCL 是参考基准测试；如果工具使用是产品的核心能力，就在交付前用它评测你的智能体。

## 交付成果

`outputs/skill-tool-registry.md` 可为给定的任务领域生成工具目录、schema 和注册表。其中包含描述质量检查：每个工具的描述是否告诉了模型何时应该使用它？

## 练习

1. 添加一个空操作（"no-op"）工具，让模型能够明确拒绝使用其他任何工具。在类似 BFCL 的幻觉测试中进行衡量。
2. 实现参数类型转换，处理以字符串表示的整数和浮点数。转换从什么时候开始会掩盖真正的缺陷？
3. 为每个工具添加超时限制，并添加熔断器（circuit breaker）：连续失败 3 次后，在接下来的 60s 内拒绝使用该工具。这会怎样改变模型从故障中恢复的方式？
4. 阅读 BFCL V4 的说明。选择一个类别（例如“多轮”），让你的智能体处理 10 条示例提示词，并报告通过率。
5. 将标准库校验器移植到 Pydantic 或 Zod。Pydantic/Zod 捕获了哪些简化实现漏掉的问题？

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|------------------------|
| 函数调用 | “工具使用” | 带有 schema 校验的结构化输出工具调用 |
| Toolformer | “自监督工具调用标注” | Schick 2023：保留那些结果能降低下一 token 预测损失的工具调用 |
| BFCL | “Berkeley Function Calling Leaderboard” | 2026 年的基准测试：评分权重为 40% 智能体类、30% 多轮类、10% Live、10% Non-Live、10% 幻觉类 |
| 工具 schema | “提供给模型的函数签名” | name、description，以及实参的 JSON Schema |
| tool_use_id | “关联 ID” | 将工具调用与其结果关联起来；对并行分派至关重要 |
| 幻觉检测 | “知道何时不应调用” | V4 类别：没有合适工具时拒绝调用 |
| 参数类型转换 | “字符串转整数修复” | 针对可预见的 schema 不匹配进行有限修复；有歧义时拒绝 |
| 沙箱隔离 | “工具执行边界” | 每个工具的读写访问范围、网络、超时限制、内存上限 |

## 延伸阅读

- [Schick et al., Toolformer (arXiv:2302.04761)](https://arxiv.org/abs/2302.04761) — 自监督工具调用标注
- [Berkeley Function Calling Leaderboard (V4)](https://gorilla.cs.berkeley.edu/leaderboard.html) — 2026 年的评测基准
- [Anthropic, Tool use documentation](https://platform.claude.com/docs/en/agent-sdk/overview) — Claude Agent SDK 中用于生产环境的工具 schema
- [OpenAI Agents SDK docs](https://openai.github.io/openai-agents-python/) — 函数工具类型与 Guardrails（安全护栏）
