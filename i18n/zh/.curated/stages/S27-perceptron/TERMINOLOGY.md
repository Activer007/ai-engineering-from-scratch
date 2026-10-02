# S27 感知机术语增量 v1.0

2026-10-02。主协调已确认。联用核心、补充及 S05–S24 固定词表；沿用 S08 计算图、链式法则、反向传播及多层感知机，不改变词义。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| perceptron / multi-layer perceptron | 感知机 / 多层感知机 | Perceptron 类名不译；单个阶跃单元与现代多层网络区分 |
| weight / bias | 权重 / 偏置 | bias 为加性参数 b，区别 S22 的统计偏差 |
| activation function / activation | 激活函数 / 激活值或激活 | 函数、神经元输出值、激活动作按语境，不能一律译函数 |
| step function | 阶跃函数 | >=0 输出1、<0输出0，边界归属保持 |
| sigmoid / ReLU | sigmoid / ReLU | 专名保留；源将 ReLU 归入光滑函数的概括另列 |
| linear classifier / hyperplane | 线性分类器 / 超平面 | 二分类边界 w*x+b=0，源高维/零权重简化不暗加条件 |
| linearly separable / non-linearly-separable | 线性可分 / 线性不可分 | 原输入特征空间单个超平面能否分开，不能混为数据是否线性函数 |
| AND / OR / NAND / NOT / XOR | AND（与）/ OR（或）/ NAND（与非）/ NOT（非）/ XOR（异或） | 逻辑门名、代码标签、复合表达式原样，首现中文解释 |
| learning rule / learning rate | 学习规则 / 学习率 | 误差 target-prediction、更新正号与输入符号分别核对 |
| epoch / convergence | 训练轮次 / 收敛 | 训练全数据一轮不等于单样本更新；有限失败演示不是一般证明 |
| hidden layer / output layer | 隐藏层 / 输出层 | saved_w_output 为更新前权重，传梯度次序保护 |
| hand-wired weights | 手动设置的权重 | 按逻辑门指定数值，不称自动训练得到 |

所有代码、Unicode/Mermaid/figure、公式、数值、模型类名和路径原样。三项参考作者、年份、英文书/论文标题及原 URL 保留；源的历史因果断言不额外研究。必要 GFM 修复只能最小可逆地加空格或转义，再独立绑定新字节。
