# S14 张量操作术语增量 v1.0

2026-10-02。联用核心及S05–S13术语；突出形状、轴、内存语义与框架差异，不把源概括当作已验证保证。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| tensor | 张量（tensor） | 此处程序多维数组语境；不扩展为抽象数学张量完整定义 |
| rank / order | 阶（rank/order） | 本课为轴数；二维矩阵的张量阶2与矩阵秩不相同，避免直接沿用矩阵rank译法 |
| axis / dimension / shape | 轴 / 维度 / 形状（shape） | 轴索引、轴长度、维数/ndim分开；所有shape元组顺序原样 |
| stride | 步幅（stride） | 此教学类和PyTorch通常按元素；NumPy ndarray.strides按字节，不能混同 |
| row-major / column-major | 行优先 / 列优先 | C order/F order保留；内存次序与矩阵数学转置分开 |
| contiguous / non-contiguous | 连续 / 非连续（contiguous/non-contiguous） | 指相应内存布局，源一概断言转置必非连续单列 |
| view / copy | 视图（view）/ 副本（copy） | 共享数据缓冲区与重新分配数据不同；源scratch实现和框架可能不同 |
| reshape / transpose / permute | 重塑形状 / 转置 / 轴置换 | 方法/API名称原样；reshape不等于随意交换元素，transpose参数含义依库 |
| squeeze / unsqueeze | 压缩单例轴 / 插入单例轴 | 单例轴长度为1；API方法名保留，不能当成数值压缩 |
| broadcasting / broadcast | 广播（broadcasting）/ 广播 | 从右对齐、相等或1；不意味着所有运算零分配或无结果副本 |
| element-wise | 逐元素 | 元素对应运算，不是矩阵乘法；广播后输出shape可能扩大 |
| reduction | 归约（reduction） | sum/mean/max沿轴聚合，不与S13降维同译 |
| einsum / Einstein summation | einsum / 爱因斯坦求和 | 表达式及引号内容原样，区分保留、求和与重复对角下标 |
| contraction | 缩并（contraction） | 对下标求和/乘积语境；不是所有einsum都减少阶数 |
| outer product / dot product | 外积 / 点积 | i,j->ij与i,i->区别；输出标量shape()原样 |
| NCHW / NHWC | NCHW / NHWC | channels-first通道优先，channels-last通道后置；B/H在不同上下文分别batch/head/height需明确 |
| multi-head attention | 多头注意力 | Q/K/V、head split/merge、T/S和D/E各轴语义严格保留 |
| attention scores / weights | 注意力分数 / 注意力权重 | softmax前后区分；mask和softmax稳定性不暗加 |
| projection / head split / merge | 投影 / 拆分注意力头 / 合并注意力头 | reshape+transpose与乘权重矩阵不同 |
| global average pooling | 全局平均池化 | H/W归约，保留B/C；序列平均池化保留B/D |
| autograd / BLAS kernel | autograd（自动求导）/ BLAS计算内核 | kernel不是核函数、OS或Jupyter内核；品牌/API原样 |
| shape contract | 形状约定（shape contract） | 操作输入/输出尺寸要求，不是法律合同 |

只保留/翻译源义，表内stride单位、transpose示例、view限制、广播unsqueeze要求、简化batch norm和未定义attention变量等源问题独立定位。代码、公式/图、API/错误字符串/数值/shape/路径/链接保护；裸围栏仅补text，GFM最小语法调整需重绑审校。
