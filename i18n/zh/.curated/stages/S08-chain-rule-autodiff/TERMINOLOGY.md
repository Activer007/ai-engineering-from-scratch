# S08 链式法则与自动微分术语增量 v1.0

2026-10-02。联用核心、增补与S05–S07数学词表；本课从标量链式法则进入计算图实现，不将标量示例泛化为所有张量/控制流情形。API、类、属性、操作符、数值、公式与代码载荷保护。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| computation / computational graph | 计算图（computation graph） | 数据和求导依赖；不是神经网络架构图的同义词 |
| automatic differentiation / autodiff | 自动微分 | 非符号求导/数值差分；源exact表述限制单列 |
| autograd engine | 自动微分引擎（autograd engine） | autograd作为模块名保持英文，Value类原样 |
| forward pass / backward pass | 前向传播 / 反向传播 | 分别计算值和梯度，不等同参数更新 |
| forward mode / reverse mode | 前向模式 / 反向模式 | 求导方向与传播pass概念区分；按输入或输出播种 |
| seed / seed gradient | 初始值（seed）/ 种子梯度 | 导数初始化语境；不要套用random.seed随机种子 |
| local derivative | 局部导数 | 在对应中间值处求值；多路径贡献需要相加 |
| upstream gradient | 上游梯度（来自输出侧） | 反向传播语境，out.grad来自损失/输出方向，不能交换乘数角色 |
| gradient accumulation | 梯度累积 | +=把多条使用路径贡献求和；与多次backward未清零不同 |
| topological sort | 拓扑排序（topological sort） | 依赖先于使用者；逆序遍历传播梯度 |
| directed acyclic graph / DAG | 有向无环图（DAG） | 仅源实际给定图模型，不声称所有动态程序静态无环 |
| dual number | 对偶数（dual number） | a+b*epsilon且epsilon^2=0；不是复数i^2=-1 |
| closure | 闭包（closure） | 捕获局部对象构建_backward；不译为封闭图 |
| dynamic graph / define-by-run | 动态图 / 运行时定义（define-by-run） | 每次执行前向构图；源描述简化另列 |
| node / children / parent | 节点 / 子节点 / 父节点 | children在该源码指产生当前值的输入依赖；按源术语保留并注意前向/反向关系 |
| gradient checking | 梯度检查（gradient checking） | 有限差分对照与容差判断，不是精确正确性的完整证明 |
| multi-layer perceptron / MLP | 多层感知机（MLP） | 简单多层网络，保留缩写 |
| neuron / layer | 神经元 / 层 | 加权和+偏置+激活，与单个Value标量节点不同 |
| XOR | 异或（XOR） | 此例输出标签-1/1适配tanh，不能改成0/1 |
| ReLU / tanh | ReLU / tanh | 代码relu/tanh原样；零点导数约定不默改 |
| finite difference | 有限差分 | 扰动h、误差阈值、每参数两次前向的成本保持 |

PyTorch、TensorFlow、JAX、NumPy、micrograd和所有Value/Neuron/Layer/MLP/Tensor类名原样。保留Language单数、million等量级与数字/单位，时间元数据可自然翻译。裸围栏仅补text标签；必要GFM修复必须最小可逆并记录。torch是否可用及源码示例省略/输入域/重复backward行为单独记录，不能擅自补程序或改源含义。
