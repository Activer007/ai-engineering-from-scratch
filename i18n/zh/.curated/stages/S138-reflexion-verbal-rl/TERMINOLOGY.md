# S138-reflexion-verbal-rl terminology support

Fixed English 1bafaa88bb4668356791150bec3a6d7df38387eb. Preauthor support candidate only. Common142 =134 TERM +8 controls; own3 pending publication. Newly available S132 TERM is appended from its independent fixed-commit readback; English prerequisites remain unchanged. No author proposal, calibration, first write, capture, record, strict or independent language review is claimed.

| English | Proposed Chinese | Semantic boundary / prior terminology |
|---|---|---|
| Reflexion / verbal reinforcement learning | Reflexion / 语言强化学习 | 保留论文专名；自然语言反思作用于提示词，不声称更新模型权重 |
| Actor / Evaluator / Self-Reflector | 行动者 / 评估器 / 自我反思器 | 本课三角色，区别 S135 的规划器/工作单元/求解器 |
| reflection / corrective insight | 反思 / 纠错认识 | 智能体失败分析，不套 S06 的几何反射或 S104 的复述技巧 |
| episodic memory / reflection buffer | 情景记忆 / 反思缓冲区 | 按任务类别保留的反思，不是神经参数记忆 |
| trajectory / trial / fresh re-attempt | 轨迹 / 尝试 / 重新开始的尝试 | 轨迹沿 S135；不是训练轮 epoch 或墙钟时长 |
| scalar / binary evaluator | 标量 / 二值评估器 | 数值分数包含通过/失败，不把全部标量等同二值 |
| heuristic / self-evaluated feedback | 启发式 / 自我评估反馈 | 人工规则与模型自评分开 |
| ground truth / tool-grounded verification | 真实值 / 以工具结果为依据的核验 | 沿 S40；工具输出本身不自动保证真实 |
| gradient update / weight update | 梯度更新 / 权重更新 | 本课无权重更新，不扩大成没有任何学习过程 |
| memory rot / stale reflection | 记忆陈旧化 / 过时反思 | 陈旧或错误内容积累，不是存储位损坏 |
| TTL / expiry by trial count | TTL（存活期限）/ 按尝试次数到期 | 本课按尝试计数，区别墙钟时间与 FIFO 长度上限 |
| bounded buffer / FIFO | 有界缓冲区 / 先进先出（FIFO） | 有界长度不等同 TTL 或持久化 |
| deduplication / compaction | 去重 / 压缩整理 | 去除重复、合并摘要与删去最旧项分别表达 |
| task-class / user / agent scope | 任务类别 / 用户 / 智能体范围 | 作用范围不可自动扩大，保留源默认约束 |
| sleep-time reflection / off the hot path | 空闲时反思 / 移出关键响应路径 | 不是操作系统睡眠；避免阻塞主响应的异步语境 |
| failure signature / reproducible task | 故障特征 / 可重复的任务 | 故障特征不是密码学签名，可重复不保证成功 |

Preserve code, inline code, numbers, mathematical expressions, identifiers, URLs, paths, Mermaid/SVG and figure payloads. Fixed-source discrepancies are recorded separately rather than silently repaired. Real later author changes must retain this frozen snapshot and their actual chronology.

Support-only revision 2026-10-05T08:40:00.217783+00:00: append S132 TERM; original preparation and all terminology rows retained. Previous common141 candidate SHA256: f19892df0b23dfbfd70756d7b5a57b325652c9845062afe7890fcef18534b01c.
