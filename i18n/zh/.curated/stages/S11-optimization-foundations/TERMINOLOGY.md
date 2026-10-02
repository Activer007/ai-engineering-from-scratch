# S11 优化术语增量 v1.0

2026-10-02。联用核心和S05–S10数学词表；优化器名/API保持英文。重点区分状态量、梯度方向、学习率与衰减、统计偏差与模型偏置。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| optimization / optimizer | 优化 / 优化器 | 求损失最小值语境，不笼统译成性能加速 |
| vanilla gradient descent | 基础梯度下降（vanilla gradient descent） | 普通GD，不译香草；GradientDescent类原样 |
| gradient / negative gradient | 梯度 / 负梯度 | 上升方向与参数更新减号区分，源Mermaid相反文字不能暗改载荷 |
| batch / mini-batch | 批量 / 小批量（mini-batch） | 全数据集与少量样本不同；不要与翻译工作批次混用 |
| SGD | 随机梯度下降（SGD） | 理论单样本与实践常指mini-batch两语境按源保留 |
| momentum / velocity | 动量 / 速度（velocity） | 累积历史梯度的状态量，不是代码运行速度 |
| Adam | Adam（自适应矩估计，Adaptive Moment Estimation） | 专名/类名保留；矩不是矩阵，二阶矩不是方差或Hessian |
| first / second moment | 一阶矩 / 二阶矩 | Adam的m为梯度滑动均值，v为梯度平方滑动均值；与动量velocity中v分开 |
| bias correction | 偏差校正（bias correction） | 修正零初始化造成的矩估计偏差，不是网络偏置参数b |
| beta / epsilon | beta / epsilon | 代码标识符及beta1/beta2/t保持，epsilon在sqrt外的位置不能改 |
| learning rate / effective step | 学习率 / 有效更新步 | lr、逐参数缩放与实际梯度/动量乘积不同 |
| learning rate schedule | 学习率调度（schedule） | 随训练步骤/epoch变化，不是任务日程 |
| step / exponential decay | 阶梯衰减 / 指数衰减 | 时间步t与N个epoch间隔、factor倍数原样 |
| cosine annealing | 余弦退火（cosine annealing） | lr_min/lr_max/t/T与pi位置保持 |
| warmup | 预热（warmup） | 训练初期逐步增大学习率，不是先执行模型缓存预热 |
| weight decay / AdamW | 权重衰减 / AdamW | 与学习率衰减区别；decoupled为解耦，不能把AdamW说成原Adam同一正则实现 |
| gradient clipping | 梯度裁剪 | 不等于权重裁剪；源“优化器处理”需与显式clip调用区分 |
| convex / strictly convex | 凸 / 严格凸 | 不能把普通凸函数改成严格凸来修源唯一极小值断言 |
| local / global minimum | 局部 / 全局极小值 | 极小值点与函数值按语境，源关于必然收敛/大多近全局的泛化单列 |
| saddle point | 鞍点 | 不能当极小值或仅平坦点；来源描述缺条件不暗修 |
| loss landscape / weight space | 损失曲面 / 权重空间 | N参数自变量空间与N+1维图像区分，source1,000,001数值保持 |
| sharp / flat minimum | 尖锐 / 平坦极小值 | 相对参数化、尺度与方向，不无条件保证泛化；源结论单列 |
| generalization / test accuracy | 泛化 / 测试准确率 | 训练loss/收敛速度不等于测试集表现 |
| convergence / overshoot | 收敛 / 越过目标（overshoot） | 步数、停止准则、发散与数值溢出分别记录 |
| Rosenbrock | Rosenbrock函数 | 专名保留，最优点(1,1)、系数100和梯度符号原样 |
| parameter group | 参数组 | 优化器配置语境，不是分布的超参数先验组 |

数字、单位/量级、公式、代码/图载荷、路径与链接保护，Language单数保留。表格调度公式裸乘号及中文strong闭合后的边界需用GFM检查，必要修复只做可逆语法转义或空格并重绑审校。算法性能/收敛/泛化的源过度概括不能悄悄改成限定结论；记录在source_issues。
