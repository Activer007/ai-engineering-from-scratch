# S32 反向传播术语增量 v1.0

2026-10-02。联用核心、补充及截至 S30 的固定词表。计算图与自动微分沿 S08，梯度裁剪及混合精度沿 S15，权重、偏置与前向传播沿 S27/S29。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| backpropagation / backward pass | 反向传播 | 沿 S08；计算梯度与优化器更新参数分开 |
| autograd engine / automatic differentiation | 自动微分引擎 / 自动微分 | 首现保留 autograd engine；Autograd 和 API 名原样 |
| computational graph / directed acyclic graph | 计算图 / 有向无环图 | 运算依赖，不机械等同网络架构 |
| topological sort | 拓扑排序 | 依赖先于使用节点；反向传播按逆序处理 |
| local derivative / gradient accumulation | 局部导数 / 梯度累积 | 多条路径贡献相加，不等于重复 backward 无需清零 |
| vanishing / exploding gradients | 梯度消失 / 梯度爆炸 | 不能由 sigmoid 导数单独推导整个网络界限；源缺条件另列 |
| sigmoid saturation | sigmoid 饱和 | 输出接近端点与浮点导数行为分开 |
| memory-computation tradeoff | 内存与计算的权衡 | 存储中间激活以避免重复计算，不泛推所有实现必须存全部中间值 |
| online SGD / full batch | 在线随机梯度下降（online SGD）/ 完整批次 | 每样本更新与批量累积区别；不补源未保证的收敛性质 |
| weight initialization / break symmetry | 权重初始化 / 打破对称性 | sqrt(2/n_inputs) 的初始化及随机性说明按源保留 |
| gradient checkpointing | 梯度检查点（gradient checkpointing） | 重算中间激活的内存优化，不是梯度检查或持久训练 checkpoint |
| inference / training | 推理 / 训练 | 前向输出与梯度计算、参数更新区分，不声称每种 API 都完全同一内部流程 |
| no-op / learnable Value | 空操作 / 可学习的 Value | Value、Neuron、Layer、Network 类名及方法名原样 |

sigmoid、ReLU、PyTorch、Claude、GPT、GPU、NaN、XOR 与全部标识符、参考论文/视频标题保留。million/millions 量级保持源词并解释；元数据分钟可译。源中严格小于 0.25、标量与向量公式、finite difference 与精确梯度混用等只记风险。
