# S29 多层网络与前向传播术语增量 v1.0

2026-10-02。联用核心、补充及 S05–S27 固定词表。前向/反向传播沿用 S08，形状/维度沿用 S14，隐藏层/激活函数/权重偏置沿用 S27。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| multi-layer network / forward pass | 多层网络 / 前向传播 | 计算输出与学习/更新参数分开；Layer/Network 类名原样 |
| input / hidden / output layer | 输入层 / 隐藏层 / 输出层 | 当前课全连接网络结构，不泛推所有模型 |
| hidden state | 隐藏状态（hidden state） | 神经网络中间表示，不同于 S01 notebook 乱序执行的隐式状态 |
| weight matrix / bias vector | 权重矩阵 / 偏置向量 | 当前层为行、上一层为列；b是加性偏置，不是统计偏差 |
| activation / element-wise | 激活 / 逐元素 | 函数、输出激活值按语境；sigmoid 保留专名 |
| shape / dimension / dimensionality | 形状 / 维度 / 维数 | 轴长度、矩阵形状和空间维数不混同；元组顺序原样 |
| universal approximation theorem | 通用逼近定理 | 表达能力不同于优化保证；紧集/函数域/输出层条件缺失另记 |
| shallow-wide / deep network | 浅而宽的网络 / 深层网络 | 深度与每层宽度分开，不把更深当普适更优 |
| composability / chain layers | 可组合性 / 依次连接各层 | 顺序、并行、堆叠不同结构，保留源模型举例 |
| encoder / decoder | 编码器 / 解码器 | Whisper/BERT/T5 等专名保留；不等同 token 分词器 |
| clamp | 限制在区间内（clamp） | 本课将sigmoid输入限在[-500,500]，不是梯度裁剪 |
| hand-tuned weights | 手动调节的权重 | 固定设置而非训练学得；与 S27 手动设置一致 |
| trainable parameter | 可训练参数 | 权重与偏置数量之和，不是当前前向示例已经实现训练 |
| leaky step | leaky step（带泄漏的阶跃）函数 | 本课自定义分段函数，不能误写成 LeakyReLU |

RBF/MLP/LLM、sigmoid、PyTorch、NumPy/numpy、Whisper、BERT、T5、ReLU 和 API 原样。源中 z=Wx+b 称线性变换、图表权重方向冲突、math.exp(1000)与逼近能力强断言均只单列；自然量级 millions/billions保留并解释。
