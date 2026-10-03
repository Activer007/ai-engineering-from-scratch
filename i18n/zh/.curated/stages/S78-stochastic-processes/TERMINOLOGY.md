# S78 随机过程术语增量 v1.0

2026-10-03。联用核心、补充、S09/S10/S18 已接受术语。译文只来自固定英文；数学变量、数量、代码、图、专名与路径原样保留。

| EN | 推荐呈现 | 语境与区别 |
|---|---|---|
| stochastic process | 随机过程（stochastic process） | 随时间演化的随机性；不等同单个静态分布 |
| random walk | 随机游走（random walk） | 一维/二维位置随机增量；位移、距离、方差与标准差区分 |
| Markov chain / Markov property | 马尔可夫链 / 马尔可夫性（Markov property） | 给定当前状态的条件独立性；不把普通 token 自身默认为完整状态 |
| transition matrix / stationary distribution | 转移矩阵 / 平稳分布 | pi*P=pi；存在、唯一性及收敛不同，源条件不暗补 |
| eigendecomposition / left eigenvector | 特征分解 / 左特征向量 | P 的左向量对应 P^T 右向量；特征值与奇异值不混用 |
| power method / spectral gap | 幂法 / 谱隙（spectral gap） | 迭代求平稳分布；源第二大特征值与模的差异另列 |
| irreducible / aperiodic | 不可约 / 非周期 | 可达性与周期不同；不能译成无循环 |
| absorbing state / barrier | 吸收态 / 吸收边界 | 进入后不离开；与普通边界截断不同 |
| mixing time / total variation distance | 混合时间 / 全变差距离 | 到平稳分布距离阈值；源1/gap仅粗略描述，非精确步数 |
| Brownian motion / increment | 布朗运动（Brownian motion）/ 增量 | 连续时间过程；保持方差 t、sqrt(dt) 与独立增量 |
| gambler's ruin / martingale | 赌徒破产 / 鞅（martingale） | 公平游走吸收概率 k/N；不改期望条件含义 |
| Langevin dynamics / energy landscape | Langevin 动力学 / 能量景观 | 梯度与噪声的竞争；连续平稳分布与离散步长偏差分开记风险 |
| MCMC | 马尔可夫链蒙特卡洛（MCMC） | 构造具有目标平稳分布的链；不等同独立样本 |
| sampling / sample | 抽样 / 样本；解码时采样 / 采样结果 | 遵循 S09/S10/S18：概率分布抽样，LLM token 解码采样 |
| Metropolis-Hastings / proposal distribution | Metropolis-Hastings / 提议分布 | 专名不强译；提议与接受率方向、Q条件次序完整保留 |
| detailed balance / burn-in / thinning | 细致平衡 / 预热期 / 抽稀 | 沿用 S18；固定预热期和抽稀不保证收敛 |
| temperature / exploration / exploitation | 温度 / 探索 / 利用 | 解码与物理能量语境明确；零温极限与除零区别源风险单列 |
| forward / reverse diffusion | 正向 / 反向扩散 | 加噪过程与学习去噪链不同；不暗示运行了反向训练 |
| noise schedule / double-well potential | 噪声调度 / 双阱势 | beta步次变化与两个势阱，非双峰概率本身 |
| SGLD | 随机梯度 Langevin 动力学（SGLD） | 小批量梯度与校准噪声；源“免费后验”措辞不作为运行保证 |
| pipeline / ML pipeline | 管线 / 机器学习管线 | 与流水线并行区分，本课没有新增此概念 |

通用章节使用学习目标、要解决的问题、核心概念、动手实现、实际使用、交付成果、关联知识、练习、关键术语、延伸阅读。Type/Learn、Language/Python 等固定标签和值不改。所有代码块注释、示例输出、Mermaid 节点和 figure 标识符均保留英文。英语论文题名保留原题，中文翻译其说明。
