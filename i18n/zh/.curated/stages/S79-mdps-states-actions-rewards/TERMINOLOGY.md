# S79 马尔可夫决策过程术语增量 v1.0

2026-10-03。联用固定核心、补充词表及 S09 概率、S22 ML 概览术语。来源为固定英文 `phases/09-reinforcement-learning/01-mdps-states-actions-rewards/docs/en.md`，commit `1bafaa88bb4668356791150bec3a6d7df38387eb`。公式、行内代码、代码、图和成果提示词不改。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| Markov Decision Process / MDP | 马尔可夫决策过程（MDP） | 状态、动作、转移、奖励、折扣五项；与纯马尔可夫链区分 |
| reinforcement learning / RL | 强化学习（RL） | 环境交互与奖励语境；保留 Q-learning、PPO、DPO、GRPO、RLHF 等缩写 |
| agent / policy | 智能体（agent）/ 策略（policy） | 策略为给定状态的动作分布；不是数据访问策略 |
| state / action / transition | 状态 / 动作 / 转移 | 状态充分性不等于当前单次观测；动作和下一状态不互换 |
| reward / return / value / Q-value | 奖励 / 回报 / 价值 / Q 值 | 单步标量、未来奖励之和、期望回报、固定首动作的期望回报；不混称收益 |
| discount / discount factor | 折扣因子 | γ 的未来奖励权重语境，不是价格折扣 |
| Markov property | 马尔可夫性质 | 给定当前状态和动作后，对历史的条件独立；公式条件方向原样 |
| Bellman equation / fixed point | Bellman 方程 / 不动点 | 价值分解为即时奖励与折扣后的后继价值；Bellman 专名保持 |
| rollout / episode | 轨迹采样（rollout）/ 回合 | 源实现返回未折扣且有步数上限的累计奖励，不当作折扣价值估计 |
| policy evaluation | 策略评估 | 固定策略下求值，不是策略改进；docs 原位迭代与 main 同步迭代差异另列 |
| terminal / absorbing state | 终止状态 / 吸收状态 | 进入终点这一步仍奖励 -1，终点调用 step 才是 0.0 |
| effective horizon / finite horizon | 有效时域 / 有限时域 | 不同于 max_steps 硬截断；1/(1-γ) 的近似含义保持 |
| dynamic programming / Monte Carlo / temporal difference | 动态规划 / 蒙特卡洛 / 时序差分 | 完整期望迭代、采样、一步自举的区别 |
| bootstrapping | 自举 | 用当前估计构造更新目标；不是统计 bootstrap 重采样 |
| credit assignment | 信用分配 | 早期动作对远期奖励的贡献归属，不是金融授信 |
| sparse reward / shaped reward | 稀疏奖励 / 塑形奖励 | 中间奖励信号；不擅自保证任意塑形都保留最优策略 |
| reward hacking / proxy reward | 奖励投机 / 代理奖励 | 对替代信号的投机优化，不是系统入侵 |
| frame stacking / recurrent state | 帧堆叠 / 循环状态 | 补足历史信息；DQN、LSTM/GRU 标识保持 |
| scalar / sufficient statistic | 标量 / 充分统计量 | 数学含义，不混同向量或完整历史记录 |
| GridWorld / greedy down+right policy | GridWorld（网格世界）/ 贪心向下加向右策略 | greedy 是源函数命名；随机选择 down/right 可在边界自环，不称为 6 步最优策略 |
| RL pipeline / prompt / token / LLM | 强化学习管线 / 提示词（prompt）/ token（词元）/ 大语言模型（LLM） | 沿用核心首现规则；pipeline 与流水线并行不同 |

通用章节沿用补充表；Pitfalls 译为“常见陷阱”。元数据 `minutes` → “分钟”，`Phase 1 · 06` / `Phase 2 · 01` 中数值保持。正文 five/Five、three 等自然语言数量等值翻译；不得把 1000、10,000、0/1、{+100, -100} 或 -6 改写成另一数值形式。中文加粗保留源边界空格；关键术语表中 `π(a \| s)` 转义原样。源技术争议在作者报告单列，不修改正文论断。
