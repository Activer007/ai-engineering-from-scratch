# S18 采样方法术语增量 v1.0

2026-10-02。联用核心、补充及 S05–S16 词表。主协调已确认：分布语境沿用抽样，LLM 解码用采样；标题采样方法作为跨语境总称。不机械全局替换 sampling。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| sampling / sample | 抽样 / 样本；解码时采样 / 采样结果 | 概率分布抽样沿用 S09/S10，LLM token 解码沿用既有 GPT 课采样 |
| inverse CDF / inverse transform sampling | 逆 CDF / 逆变换抽样 | CDF 为累积分布函数；连续一般逆与广义逆区别只单列源前提 |
| rejection sampling | 拒绝抽样 | 提议后按概率接受，不能把“拒绝”当认证/授权行为 |
| proposal distribution / envelope bound | 提议分布 / 包络界 | M 约束 p <= M*q，与 PDF 最大值不可无条件等同；源遗漏单列 |
| importance / self-normalized importance sampling | 重要性 / 自归一化重要性抽样 | p/q 方向与加权平均分母保持；自归一化不保证任意场景方差更低 |
| partition function / evidence | 配分函数 / 证据 | 能量模型与贝叶斯归一化语境，不是磁盘分区 |
| Monte Carlo / MCMC | Monte Carlo（蒙特卡洛）/ 马尔可夫链蒙特卡洛（MCMC） | 独立抽样均值与相关链样本区分 |
| Markov chain / stationary distribution | 马尔可夫链 / 平稳分布 | 平稳性与从任意初态收敛不等同，混合条件不暗加 |
| Metropolis-Hastings / Gibbs | Metropolis-Hastings / Gibbs 抽样 | 算法专名保留，条件更新与所有坐标联合移动区分 |
| detailed balance | 细致平衡（detailed balance） | 关于平稳分布加权转移流的条件，不等于任意链都保证遍历收敛 |
| burn-in / thinning / mixing | 预热期（burn-in）/ 抽稀（thinning）/ 混合 | 预热期丢弃初始链样本，不是 S11 学习率 warmup；固定步数不保证收敛 |
| temperature / greedy decoding | 温度 / 贪心解码 | T 为零需特别处理；正文片段与 canonical 不同的零温处理另记 |
| top-k / nucleus / top-p sampling | top-k / 核采样（nucleus/top-p sampling）/ top-p 采样 | 解码语境用采样；p 的累积阈值、k 的候选数分开 |
| reparameterization trick | 重参数化技巧 | 参数无关随机源加参数可微变换，保持 mu/sigma/log_var 对象 |
| Gumbel-Max / Gumbel-Softmax | Gumbel-Max / Gumbel-Softmax | 硬最大值与连续近似区别，log-probability 不等于任意 logits 的 log |
| straight-through estimator | 直通估计器 | 硬前向、软梯度反向；源 Python 返回 hard/soft 不是自动微分实现 |
| continuous relaxation / soft one-hot | 连续松弛 / 软 one-hot（独热） | 概率向量近似离散样本，硬 one-hot 不同 |
| stratified sampling / stratum | 分层抽样 / 层 | 分区后各层抽样，区别模型网络层与任意准 Monte Carlo 保证 |
| ancestral sampling | 祖先抽样（ancestral sampling） | 顺条件分布依次生成；扩散反向链语境，非 MCMC 平稳迭代的同义词 |
| exploration / exploitation | 探索 / 利用 | 多臂老虎机策略取舍，exploitation 此处不是攻击 |
| heavy tails / bimodal | 重尾 / 双峰 | 离中心极端样本与两个密度峰的概念，不是数据长度 |

所有概率、公式、符号、阈值、闭/开区间、数组值、代码与图载荷保持。方法/库/作者名字和 Cauchy、Box-Muller、Gaussian、PPO/TRPO、VAE、NeRF、NUTS/HMC、PyMC、emcee、NumPyro/JAX 原样。非允许 SciPy/matplotlib 示例仅保留，不为翻译安装运行。必要 GFM 修复仅最小可逆空格/转义并重新绑定审校。
