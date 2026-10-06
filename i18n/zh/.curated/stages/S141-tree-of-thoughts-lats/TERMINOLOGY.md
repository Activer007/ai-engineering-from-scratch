# S141-tree-of-thoughts-lats terminology support

Fixed English: 1bafaa88bb4668356791150bec3a6d7df38387eb. Preauthor support candidate only. The coordinator supplies the exact common146 pins and formal154 baseline in DEPENDENCIES.json. Own3 publication/readback/installation and all future author proposal/calibration, first-write, capture, target/record, strict and independent language-review evidence remain pending/null.

## Source-grounded term preparation

This support glossary refines the source-only proposal using verified core terminology, the ADDENDUM heading/first-use rules and relevant S18, S76, S89, S128, S132 and S138 terminology. The core and those six stage glossaries were read in full; only the relevant ADDENDUM rules were read. The complete shared set is to be pinned by the coordinator, not falsely described as freshly read. Historical status text in a reference glossary does not establish its current publication or course status. These entries are terminology, not a Chinese lesson draft or the future author's own calibration receipt.

| English | Proposed Chinese | Semantic boundary / inherited vocabulary |
|---|---|---|
| Tree of Thoughts / ToT | 思维树（Tree of Thoughts，ToT） | Algorithm name/acronym retained on first use; nodes are coherent intermediate thoughts, not individual tokens. |
| Language Agent Tree Search / LATS | 语言智能体树搜索（Language Agent Tree Search，LATS） | Keep LATS. Distinguish the paper's method from the source's deliberately simplified symbolic MCTS program. |
| chain-of-thought / CoT | 思维链（chain-of-thought，CoT） | A reasoning sequence; do not silently equate every CoT method with an inability to use repeated samples. Translate the actual source claim faithfully. |
| thought / intermediate step | 思考步骤 / 中间步骤 | S132 uses 思考 for Thought. A thought is a coherent reasoning unit; protected Thought labels and example strings stay English. |
| Monte Carlo Tree Search / MCTS | 蒙特卡洛树搜索（Monte Carlo Tree Search，MCTS） | S18 Monte Carlo vocabulary; not Markov chain Monte Carlo (MCMC), gradient descent or a newly trained model. |
| breadth-first search / BFS | 广度优先搜索（BFS） | S76. The source and ToT paper use BFS with top-b pruning; keep the name. Do not convert it into an unpruned-search guarantee. |
| depth-first search / DFS | 深度优先搜索（DFS） | S76. A strategy discussed in the lesson, not an implementation present in the local toy code. |
| beam search / beam width | 束搜索（beam search）/ 束宽 | S89/S128. Top-k candidates retained at a level; the beam-comparison exercise is underspecified because the supplied BFS already prunes. |
| node / edge / root / leaf / child / ancestor | 节点 / 边 / 根节点 / 叶节点 / 子节点 / 祖先节点 | S76 graph vocabulary; a leaf is a structural property and need not already be a complete successful answer. |
| search frontier / pruning / backtracking | 搜索前沿 / 剪枝 / 回溯 | Frontier means candidate states awaiting expansion. Backtracking is search control, not gradient backpropagation or an automatic guarantee of recovery. |
| branching factor / depth cap | 分支因子 / 深度上限 | Number of generated successors versus number of reasoning levels. K, k and source limits remain unchanged. |
| policy / value function | 策略 / 价值函数 | Next-action generator versus state/trajectory scorer. Policy here is not access authorization; value is not a model parameter update. |
| self-evaluation / evaluator | 自我评估 / 评估器 | S138. Separate model self-score, symbolic heuristic and external environment reward; the toy value() does not call an LLM. |
| reflection / Self-Reflector / episodic memory | 反思 / 自我反思器 / 情景记忆 | S138. Natural-language feedback may condition later attempts; do not claim the toy MCTS implements a reflection buffer. |
| observation / environment feedback | 观察结果 / 环境反馈 | S132. Feedback can inform valuation, but a tool output is not automatically reliable ground truth. |
| trajectory / rollout | 轨迹 / 模拟轨迹 | S138 trajectory. In MCTS, rollout is simulated continuation from a node; as a verb use 模拟推进. It is not software rollout/deployment. |
| select / expand / simulate / backpropagate | 选择 / 扩展 / 模拟 / 回传 | The four MCTS phases. 回传 updates visit counts and accumulated rewards/value estimates along a search path, not gradients or neural-network weights. |
| UCT / upper confidence bound for trees | 树搜索置信上限（UCT） | Preserve the exact source formula, Q, N and c. Do not add a statistical guarantee or silently change the source's expansion of the acronym. |
| exploration / exploitation | 探索 / 利用 | S18. Sampling less-visited possibilities versus following estimated value; exploitation is not a security attack here. |
| visit count / value estimate / reward | 访问次数 / 价值估计 / 奖励 | Counts, averages and observed reward are distinct. The code's node-expansion count is not a token count or visit count. |
| symbolic score / noisy evaluator | 符号计算评分 / 有噪声的评估器 | Symbolic distance is not prompted self-evaluation. A high score is not by itself proof of a correct answer. |
| evolutionary search / machine-checkable fitness | 演化搜索 / 可机器核验的适应度 | Search over candidate programs; fitness is the evaluator's objective, not biological fitness or an assumed formal proof. |
| token budget / search cost / wall-clock latency | token 预算 / 搜索成本 / 实际耗时 | Core token first appears as token（词元）. Text usage, monetary cost, node expansions and elapsed time are separate measurements. |
| evaluator fidelity / signal-to-noise | 评估器保真度 / 信噪比 | Reliability of the scoring signal; do not invent a numerical minimum that the source does not establish. |
| pass@1 / HumanEval / WebShop / Game of 24 | pass@1 / HumanEval / WebShop / 24 点游戏 | Preserve benchmark identifiers, metric spelling and numbers. Paper-time headlines are not contemporary SOTA or local test results. |

## First use, inheritance and protected surfaces

- Follow core first-use rules: Chinese plus source English/acronym for translatable technical terms at their first body occurrence; later use the agreed term. Keep names, APIs and code identifiers exact. Source English/acronym capitalization takes precedence over typographic normalization.
- Inherit agent as 智能体, LLM as 大语言模型（LLM）, token as token（词元）, prompt as 提示词（prompt）, tool call as 工具调用, ReAct as ReAct, observation as 观察结果, and stop condition as 停止条件 from the core/S132 vocabulary. Reflexion is the proper name, while reflection is 反思.
- The source's thought/action/observation roles, LATS policy/value/self-reflector roles and MCTS select/expand/simulate/backpropagate phases are different decompositions. Do not interchange their labels or imply all roles are present in the symbolic demo.
- Use 回传 for MCTS backpropagation, explicitly distinguished from gradient-based 反向传播 when necessary. Here Q accumulates reward statistics and N counts visits. Source formulas and code remain exact rather than being rewritten to match terminology.
- Preserve the claim 100–1000x and all source numeric variants. The token-cost discrepancy, missing complex-valued matrix qualifier, exercise section mismatch and quiz contract discrepancy belong in source-risk records, not unmarked corrections to the Chinese body. Calibration does not endorse source factual accuracy.
- Nine shared headings follow the ADDENDUM: 学习目标、要解决的问题、核心概念、动手实现、实际使用、交付成果、练习、关键术语、延伸阅读. Do not create absent sections. Keep metadata keys Type/Languages/Prerequisites/Time and type/language names Build/Python unchanged; natural-language prerequisite labels and minutes may be translated faithfully.
- Protect code, inline code, formulas, variable names, source numbers and units, all paths and URLs, ASCII/SVG payloads and the exact tree-of-thoughts figure identifier. At actual authoring, only the already permitted reversible text tags may be added to the two bare body fences, with changes recorded. Do not translate labels inside the protected diagrams or add an image embed absent from source.
- The unembedded tot-lats-tree.svg is a separate future asset with the exact source hash and target path in SCOPE.md and the dependency inputs. It must appear in later asset and double-replay manifests even though the body does not link it.
- Keep citation titles and names searchable: Yao, Zhou, NeurIPS, ICML, GPT-4, GPT-3.5, ReAct, Reflexion, CRITIC, LangGraph, LangChain, LlamaIndex, TreeOfThoughts and AlphaEvolve, along with all other actual source identifiers. References to framework availability and 2026 practice remain source assertions, not new verification.

No Chinese lesson body or author chronology is created by this glossary. Publication and independent exact-byte readback followed by own3 installation remain mandatory before authoring. No terminology change permits a source repair, additional checker exception, model/API call, download, training or course runtime.
