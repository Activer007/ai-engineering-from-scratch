# S73 神经网络调试术语增量

继承核心、补充表和78项固定支持，尤其S32/S35/S40/S43/S53/S57/S58/S63；唯一课文源为固定英文03-13。术语不替代源事实核验。

| English | 中文 | 语境与保护 |
|---|---|---|
| debugging / silent bug | 调试 / 静默缺陷（silent bug） | 无异常但结果错误；不等同已证明的数学错误 |
| gradient checking / finite differences | 梯度检查 / 有限差分 | 区别梯度检查点；解析梯度与数值梯度不同 |
| analytical / numerical gradient | 解析梯度 / 数值梯度 | 反向传播与有限差分近似的对照 |
| vanishing / exploding gradients | 梯度消失 / 梯度爆炸 | 沿S32；阈值和层次顺序按源另记风险 |
| dead ReLU / dead neuron | 失活的ReLU / 失活神经元 | 持续零输出不同于当前批次零元素比例 |
| activation statistics / weight norm | 激活值统计量 / 权重范数 | 前向输出与参数及梯度不能互换 |
| overfit-one-batch | 单批次过拟合测试（overfit-one-batch） | 检查能否拟合少量样本，不保证完整训练正确 |
| learning rate finder / LR range test | 学习率查找器 / 学习率范围测试 | LR保留；扫描步数不是完整数据轮次的保证 |
| hook / handle | 钩子（hook）/ 句柄 | 注册回调及移除资源；API原样 |
| data pipeline / data leakage | 数据管线 / 数据泄漏 | 沿S57；不把打乱顺序本身视为泄漏的普适结论 |
| gradient accumulation / gradient clipping | 梯度累积 / 梯度裁剪 | 沿S32/S43；清零、反向计算、优化器更新分开 |
| batch normalization / dropout | 批量归一化 / Dropout（随机失活） | 沿S63；训练/评估模式和运行统计状态分开 |
| confident learning / loss truncation | 置信学习（confident learning）/ 损失截断 | 标签纠错与忽略高损失样本不等同 |
| saturation / oscillation / divergence | 饱和 / 振荡 / 发散 | 保留启发式判断的源语气，不称为完整诊断证明 |
| state restoration / dtype | 状态恢复 / 数据类型 | 参数、缓冲区、训练模式、随机状态和梯度分别检查 |

PyTorch、ReLU、LeakyReLU、GELU、Adam、SGD、Kaiming、Weights & Biases、W&B、TensorBoard和所有标识符原样。引用论文标题原样，描述译中文；数字及公式保留，原事实风险独立登记。强调边界空格保留，裸URL与中文标点留安全分隔。
