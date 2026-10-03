# S63 迷你框架术语增量 v1.0

2026-10-03。继承核心、补充表与 70 项固定依赖；尤其沿用 S27/S29/S32/S35/S40/S43/S48/S53/S58 的阶段 03 术语。唯一课文来源为固定英文 03-10；不以术语修正源技术问题。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| framework / Module abstraction | 框架 / Module（模块）抽象 | 类名原样；统一前向、反向及参数接口 |
| forward / backward pass | 前向传播 / 反向传播 | 沿 S29/S32；梯度计算不同于优化器更新 |
| Sequential / composite pattern | Sequential（顺序容器）/ 组合模式 | 顺序连接模块，反向遍历逆序，容器自身也是模块 |
| trainable parameters / weights / biases | 可训练参数 / 权重 / 偏置 | 偏置参数不同于统计偏差，标识符原样 |
| Dropout / BatchNorm | Dropout（随机失活）/ BatchNorm（批量归一化） | 沿 S48；训练/评估模式不同，不能暗补完整批量梯度 |
| running statistics / running averages | 运行统计量 / 运行平均值 | 沿 S48；均值、方差、二阶矩不互换 |
| DataLoader / batching / shuffle | DataLoader（数据加载器）/ 分批 / 打乱顺序 | 分批迭代不保证批量参数更新 |
| optimizer / SGD / Adam | 优化器 / 随机梯度下降（SGD）/ Adam | Adam 保留专名；源 variance 说法保持并另列限制 |
| MSE / binary cross-entropy | 均方误差（MSE）/ 二元交叉熵 | 沿 S40；代码类名与均值因子保护 |
| gradient accumulation / zero grad | 梯度累积 / 梯度清零 | 样本、批次与轮次区分，沿 S32 |
| learning rate schedule / warmup | 学习率调度 / 预热（warmup） | LR 保留并说明；沿 S58 |
| weight decay / L2 regularization | 权重衰减 / L2 正则化 | 沿 S43/S48；源将二者等同的简写另列 |
| circle classification / feedforward network | 圆形区域分类 / 前馈网络 | 二维点的圆内外标签，不译为圆形图像识别 |

PyTorch、TensorFlow、Keras、ReLU、Sigmoid、Tanh、Adam、numpy 及全部 API/类名/路径/公式/图表载荷原样。参考书、论文标题及作者原样，介绍文字译中文。自然量词 ten/five 译十/五并记录等值；源阿拉伯数字不换算。GFM/site/CI 与技术正确性分开验收。
