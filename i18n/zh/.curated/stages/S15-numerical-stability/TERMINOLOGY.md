# S15 数值稳定性术语增量 v1.0

2026-10-02。联用核心及S05–S14词表，不覆盖既有定义。API、float32/float16/bfloat16、NaN/Inf及代码/数学/数值均保留；来源技术简化另列，不在译文中暗修。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| numerical stability | 数值稳定性 | 浮点计算误差/表示范围语境，不是训练泛化的同义词 |
| floating point / IEEE 754 | 浮点数（floating point）/ IEEE 754 | 数值表示与标准名；dtype大小写随源保留 |
| sign bit / exponent / mantissa | 符号位 / 指数 / 尾数（mantissa，也称significand） | 源将尾数字段与有效数混用；隐含位/正规与次正规条件只记风险 |
| precision / range | 精度 / 表示范围 | 有效数字位数与可表示数量级分开，不把bfloat16称更高精度 |
| rounding error / noise | 舍入误差 / 舍入噪声 | 与数据噪声/截断误差区分，原文truncate保留为截断 |
| catastrophic cancellation | 灾难性消去（catastrophic cancellation） | 两个接近浮点数相减导致有效数字丢失 |
| overflow / underflow | 上溢 / 下溢 | 沿用S09；下溢与必然归零不等同，源简化单列 |
| machine epsilon | 机器epsilon（machine epsilon） | epsilon字段/阈值原样；练习等号方向与表内定义冲突另记 |
| log-sum-exp / max-subtraction | log-sum-exp / 减去最大值 | 专名保留；指数运算结果与指数参数区分 |
| log-space / log-probability | 对数域 / 对数概率 | 加法对应乘概率，不混为概率直接相加 |
| centered finite difference | 中心有限差分 | 与前向差分不同；h、2h与O(h^2)保持 |
| analytical / numerical gradient | 解析梯度 / 数值梯度 | 反向传播计算与有限差分近似分开；检查阈值不是普适证明 |
| mixed precision / loss scaling | 混合精度 / 损失缩放 | 前向/反向精度、master权重、缩放/反缩放方向保持 |
| dynamic loss scaling | 动态损失缩放 | 溢出后减半、连续N步后加倍；数值原样 |
| gradient clipping | 梯度裁剪 | 沿用S11；不同于直接裁剪权重 |
| clip by value / by norm | 按值裁剪 / 按范数裁剪 | 前者逐元素限幅可改方向，后者全向量缩放保方向 |
| batch / layer / RMS normalization | 批量归一化 / 层归一化 / RMS归一化（均方根归一化） | 归一化与正则化区别；源统一recenter和LayerNorm公式风险单列 |
| NaN / Inf | NaN（非数）/ Inf（无穷大） | 代码nan/inf大小写原样；Python标量异常与数组传播行为不同 |
| dead ReLU | 失活的ReLU | 输入全负语境，不改类名；LeakyReLU/GELU原样 |
| parallel reduction | 并行归约 | 沿用S14，不译成降维；累加次序与浮点非结合性相关 |

进一步阅读保留论文标题的可检索英文专名并新译描述；百分比2%及1-3%按源保留，不擅自改为百分点。代码、裸说明围栏和figure载荷完全保留；任何真实GFM最小修复需重新绑定审校hash。
