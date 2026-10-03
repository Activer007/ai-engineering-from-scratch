# S72 JAX 入门术语增量 v1.0

2026-10-03。仅依据固定英文03-12；联用核心、补充及78项固定依赖，尤其S08/S14与03-01至03-10对应已接受词表。术语不修正源概括、历史归属、性能或API适用范围。

| EN | 推荐呈现 | 语境与保护边界 |
|---|---|---|
| pure function / functional | 纯函数（pure function）/ 函数式 | 显式输入状态、返回结果；与面向对象对照，不把函数式当作函数数量 |
| mutable / immutable state | 可变 / 不可变状态 | 状态原地修改与返回新数组不同；所有API和代码原样 |
| eager execution / mutation | 即时执行 / 即时修改 | 源对PyTorch的概括另列风险，不暗补torch.compile |
| automatic differentiation / functional autodiff | 自动微分 / 函数式自动微分 | 沿S08；变换函数求导与张量梯度存储对照 |
| JIT / XLA | 即时编译（JIT）/ XLA（加速线性代数，Accelerated Linear Algebra） | 与即时执行区分；编译和设备执行、首次和后续调用分开 |
| tracing / kernel launch | 跟踪（tracing）/ 计算内核启动 | 跟踪抽象值、编译和实际执行不同；不是OS内核 |
| vectorization / batching | 向量化 / 分批 | vmap变换与手写批次轴管理区别；不把融合和加速当已测 |
| data parallelism / sharding | 数据并行 / 分片 | pmap、shard_map、pmean、psum原样；源自动切批概括保留另审 |
| pytree / leaf | pytree（嵌套树结构）/ 叶节点 | 嵌套列表、元组、字典及数组；叶节点不必全是可训练参数 |
| explicit state / side effect | 显式状态 / 副作用 | 参数和优化器状态作为输入输出；不将无状态对象等同无任何配置 |
| PRNG key / split | 伪随机数生成器（PRNG）密钥 / 拆分 | 这里是随机状态，不是账户凭据；seed译随机种子，与key不同 |
| per-example gradient | 逐样本梯度 | 每个样本的参数梯度，与批次平均梯度区别 |
| gradient transform / clipping | 梯度变换 / 梯度裁剪 | 沿S43；Optax变换的更新量与原始梯度可不同 |
| warmup / checkpointing | 预热 / 检查点保存与恢复 | 编译基准预热和学习率预热依语境区分；非S32梯度检查点重计算 |
| multi-layer perceptron / MLP | 多层感知机（MLP） | 沿S08/S29，隐藏层维度和类别数保持 |
| He initialization / weight decay | He初始化 / 权重衰减 | 沿S53/S43；初始化尺度、偏置和衰减语义不互换 |
| pipeline | 管线 | 沿S57；不译为流水线，流水线并行另论 |

JAX、PyTorch、TensorFlow、NumPy、Flax、Equinox、Optax、Orbax、CLU、DeepMind、Anthropic、Gemini、Claude、ReLU、softmax及所有API/命令/路径保持英文。自然语言API首次释义应用程序编程接口；SGD首次可释随机梯度下降。million/billion保留原量级并解释；分钟可中文；100x及10-100x可译100倍及10-100倍并记录等值映射。参考标题和作者保留，中文描述与裸URL以ASCII空格分离。不得借词表对受保护围栏、数学或技术结论作静默修正。
