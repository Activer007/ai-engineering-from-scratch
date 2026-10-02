# S09 概率与分布术语增量 v1.0

2026-10-02。联用核心及既有数学词表；本课从离散事件到连续密度，再到logits/softmax和抽样。首现适当给中英对应；数字、量级、单位、API、公式、条件次序、代码及图标识保护。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| sample space / event / outcome | 样本空间 / 事件 / 结果 | 事件是样本空间子集，结果与事件层级不混同 |
| probability / distribution | 概率 / 分布（概率分布） | P是事件概率，分布描述随机变量，不泛称每个预测/损失都必有概率解释 |
| random variable | 随机变量 | 与单次样本、算法随机种子区分 |
| conditional probability | 条件概率 | P(A\|B)指给定B时A，条件方向绝不能倒置；分母P(B)原样 |
| independence | 独立性 | 概率独立与线性无关不同；不能把互斥当作独立 |
| mutually exclusive | 互斥 | 事件不能同时发生，非“互不影响” |
| probability mass function / PMF | 概率质量函数（PMF） | 离散结果的概率，求和归一；与连续密度不同 |
| probability density function / PDF | 概率密度函数（PDF） | 可大于1，区间积分才是概率；不是文档格式PDF |
| Bernoulli / categorical | Bernoulli分布（伯努利分布）/ 类别分布（categorical） | 单次两结果/多结果，不混成二项或多项计数分布 |
| uniform distribution | 均匀分布 | 离散/连续语境分开，支持域与区间端点保持 |
| normal / Gaussian | 正态分布（Gaussian，高斯分布） | mu均值、sigma标准差、sigma^2方差保持 |
| Poisson | Poisson分布（泊松分布） | 计数分布，lambda参数角色和离散k不混用 |
| expected value / mean | 期望 / 均值 | 概率加权与普通样本均值语境分开 |
| variance / standard deviation | 方差 / 标准差 | 平方偏差与平方根区分；sigma不是sigma^2 |
| joint / marginal distribution | 联合分布 / 边际分布 | 对谁求和消去与保留哪个变量必须明确；行列总和不交换 |
| Central Limit Theorem / CLT | 中心极限定理（CLT） | 源缺归一化/有限方差等条件单列，不能悄悄补写或强化 |
| entropy / cross-entropy | 熵 / 交叉熵 | 与KL散度不同；正确类别负对数是特定标签情形 |
| negative log-likelihood | 负对数似然 | 与任意分布差异/距离不等同 |
| log probability | 对数概率 | 此处事件概率/离散质量，不能无条件套到PDF密度的对数 |
| logits / logit | logits（未归一化分数）/ logit | 模型输出语境保留English；不要强译成概率或对数概率 |
| softmax / log-softmax | softmax / log-softmax | 函数/API拼写保留；平移不变、指数、减最大值与输出次序原样 |
| log-sum-exp | log-sum-exp | 数值技巧专名，log_softmax代码标识符不改 |
| overflow / underflow | 上溢 / 下溢 | 浮点范围/精度语境，源“exp(102)溢出”和30项下溢须单列dtype边界 |
| sampling / without replacement | 抽样 / 不放回 | 分布抽样与数据子集取样按语境；随机次数n和分布参数不混用 |
| inverse transform / rejection sampling | 逆变换抽样 / 拒绝抽样 | 保持方法差异，不混为重参数化 |
| reparameterization trick | 重参数化技巧 | VAE专用语境，非任意分布的通用直接抽样法 |
| loaded dice | 不均匀骰子（loaded dice） | 各面概率不均匀，不是加载到内存的骰子 |
| face card | 人头牌（J、Q、K） | 本源12/52语境；King为K牌，条件方向/4与12不变 |

P(A|B)在Markdown表格中必须保留源\|转义，不能变成多列。数字范围、50,000、10,000、索引3、输出概率与表中边际值原样。代码与数学载荷保持，裸围栏仅补text；正文乘号/中文加粗边界需真实GFM检查，必要修复只做可逆语法转义或空格并记录。既有源技术/不完整可视化/库依赖问题单列，不安装新依赖或改源程序。
