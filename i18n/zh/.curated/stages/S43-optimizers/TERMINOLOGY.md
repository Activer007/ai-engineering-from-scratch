# S43 优化器术语增量 v1.0

2026-10-02。沿用核心、补充表及 S11/S15/S20/S25/S32/S35/S40 已固定词表。来源为固定英文 03/06；术语不修正源事实或公式。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| optimizer / vanilla SGD | 优化器 / 基础 SGD | SGD 首次为随机梯度下降（SGD）；不是批量梯度下降的同义词 |
| Adam | Adam（自适应矩估计，Adaptive Moment Estimation） | 专名和类名保留；矩不是矩阵 |
| momentum / velocity | 动量 / 速度（velocity） | 历史梯度累积状态；源未乘 1-beta 的式子不是归一化均值，另列源风险 |
| exponential moving average | 指数移动平均（exponential moving average） | 历史样本指数加权；沿用 S11 的滑动均值含义 |
| first / second moment | 一阶矩 / 二阶矩 | 二阶矩与方差、Hessian 不等同；源围栏 variance 原样保护 |
| bias correction | 偏差校正（bias correction） | 零初始化矩估计的统计偏差，不是偏置参数 b |
| RMS / RMSProp | 均方根（RMS）/ RMSProp | RMSProp 保留算法名；逐参数平方梯度平均的平方根 |
| adaptive / effective learning rate | 自适应 / 有效学习率 | 与含 m_hat 的实际更新量区别；练习混用按源保留并另记 |
| weight decay / decoupled weight decay | 权重衰减 / 解耦权重衰减 | 区别学习率衰减和 L2 正则化；AdamW 专名保留 |
| learning rate schedule / warmup | 学习率调度 / 预热（warmup） | 训练步骤上的学习率变化，不是运行时缓存预热 |
| cosine decay / step schedule | 余弦衰减 / 阶梯调度 | 不改变源时间步或 epoch 定义；CosineAnnealingLR API 保留 |
| Nesterov momentum / lookahead position | Nesterov 动量 / 前瞻位置（lookahead position） | 在前瞻位置计算梯度；不混同另一优化器 Lookahead |
| gradient clipping / global norm | 梯度裁剪 / 全局范数 | 针对整组梯度而非单个权重；裁剪不保证任意学习率均稳定 |
| parameter group / epoch | 参数组 / 轮（epoch） | 参数组配置与训练轮次区别；单样本更新步不等于整轮 |
| loss landscape / flat minimum | 损失曲面 / 平坦极小值 | 沿 S11；收敛速度、训练准确率、泛化效果不能互代 |

SGD、RMSProp、Adam、AdamW、Nesterov、Transformer、CNN、GAN、BERT、GPT、LLaMA、Stable Diffusion、PyTorch 及所有 API/参数名原样保留；首次需要时补中文释义。源推荐、默认值、性能比例和历史归属均忠实保留并分列验证边界。
