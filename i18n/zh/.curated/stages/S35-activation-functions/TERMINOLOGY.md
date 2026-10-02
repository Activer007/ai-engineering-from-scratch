# S35 激活函数术语增量 v1.0

2026-10-02。联用核心、补充及截至 S33 的固定词表；梯度消失/爆炸沿 S32，隐藏状态沿 S29，失活的 ReLU 沿 S15。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| activation function / activation magnitude | 激活函数 / 激活值幅度 | 激活值与梯度不同，不将前向幅度实验暗改为反向梯度测量 |
| nonlinearity / representational capacity | 非线性 / 表达能力 | 结构能表示的函数不同于训练可找到的参数 |
| zero-centered / zig-zagging | 以零为中心 / 之字形前进 | 分布中心与优化路径语境，不保证每批均值为零 |
| dead neuron / dead neuron rate | 失活神经元 / 神经元失活率 | 沿 S15 的失活；有限样本从未激活不等于所有未来输入永久失活 |
| saturation / gradient flow | 饱和 / 梯度流 | 局部激活导数与整个网络 Jacobian 分开 |
| Rectified Linear Unit / ReLU | 整流线性单元（ReLU） | 专名及 API 保留；零点导数按源约定，不补可微性质 |
| Leaky ReLU / Parametric ReLU | Leaky ReLU / 参数化 ReLU（PReLU） | 负侧斜率固定与可学习不同；alpha 与代码原样 |
| Gaussian Error Linear Unit / GELU | 高斯误差线性单元（GELU） | 精确 x*Phi(x) 与 tanh 近似分开，导数错配单列 |
| Swish / SiLU / self-gated | Swish / SiLU / 自门控 | x*sigmoid(x) 源表达保留，不暗加可调 beta |
| Exponential Linear Unit / ELU | 指数线性单元（ELU） | alpha 参数及分段边界按源保留 |
| softmax / logit | softmax / logit（原始分数） | 沿 S28；输出分布与校准置信度不同，softmax 向量输入例外单列 |
| cumulative distribution function / CDF | 累积分布函数（CDF） | 此处为标准正态分布，不混同概率密度 |
| hidden state / gate | 隐藏状态 / 门 | RNN/LSTM 状态和门控按源上下文，非 token 或 API 安全门 |
| gradient health monitor | 梯度健康监测器 | 训练中的每层幅度检查，阈值是源练习取值，不是普适标准 |

sigmoid、tanh、ReLU、GELU、Swish、SiLU、softmax、BERT、GPT、EfficientNet、PyTorch、Xavier 与代码标识原样。所有公式、近似号、数值和范围保护；不把源推荐改写成新技术建议。必要 GFM 修复只在实际观察后处理。
