# S53 权重初始化术语增量 v1.0

2026-10-02。继承核心、补充与 61 项固定词表，尤其 S05/S32/S35/S43/S48；来源固定英文 03/08，不以术语修源事实。

| EN | 推荐呈现 | 语境 / 保留规则 |
|---|---|---|
| weight initialization / zero initialization | 权重初始化 / 零初始化 | 初始化参数值；不等同训练更新，沿 S32 |
| symmetry / symmetry breaking | 对称性 / 打破对称性 | 隐藏神经元交换对称性；不保证随机后一定学习不同特征 |
| weight space / random scale | 权重空间 / 随机初始化的尺度 | 本课 random.gauss 的 scale 是标准差，不能混作方差 |
| fan-in / fan-out | 输入连接数（fan-in）/ 输出连接数（fan-out） | fan_in/fan_out 标识符原样；矩阵为 fan_out 行、fan_in 列 |
| variance propagation | 方差传播（variance propagation） | 方差与二阶矩、平均绝对值不同；源推导缺假设另列 |
| activation magnitude / exploding activations | 激活值幅度 / 激活值爆炸 | 沿 S35；前向数值幅度不替代反向梯度或训练稳定性 |
| Xavier/Glorot / Kaiming/He initialization | Xavier/Glorot 初始化 / Kaiming/He 初始化 | 人名算法原样；sigmoid/tanh/ReLU/GELU 适用边界按源另记 |
| residual scaling / residual stream | 残差缩放（residual scaling）/ 残差流 | 缩放权重与缩放整个层输出不同；1/sqrt(2N) 和1/sqrt(N)矛盾不暗改 |
| residual projection | 残差投影 | 投影参数与全部残差子层权重范围区别 |
| orthogonal / orthonormal initialization | 正交初始化 / 标准正交初始化 | 沿 S05；矩形矩阵 U 的形状与增益条件不暗补 |
| LeCun / SELU | LeCun / SELU（缩放指数线性单元） | 保人名与缩写，源 SELU/tanh 对比不改 |
| SVD / singular vectors | 奇异值分解（SVD）/ 奇异向量 | 源练习只指定 U，完整/薄 SVD 与矩形范围单列 |
| dead network / saturation | 失效的网络 / 饱和 | 源指梯度全零或激活饱和，不强行等同单个 ReLU 神经元失活 |
| init health check | 初始化健康检查 | 初始化诊断函数，非医学语境；API 标识原样 |

GPT-2、Llama 3、HuggingFace、PyTorch、Xavier、Glorot、Kaiming、He、sigmoid、tanh、ReLU、GELU、Swish 及全部代码/API 原样。自然量词用中文等值并记录；N、B、Var、标准差、层数、神经元数、参数数、训练轮及概率分母不互换。源所有公式数值保留，不据计算结果悄改。
