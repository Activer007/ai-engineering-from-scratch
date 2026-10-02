# S48 正则化术语增量 v1.0

2026-10-02。继承核心、补充与 S15/S22/S39/S40/S42/S43 等固定词表；来源为固定英文 03/07，不修正源事实。

| EN | 推荐呈现 | 语境 / 保留规则 |
|---|---|---|
| regularization / normalization | 正则化 / 归一化 | 防止过拟合的方法与数值变换不同，沿既有词表 |
| Dropout / inverted dropout | Dropout（随机失活）/ 倒置 Dropout（inverted dropout） | 首次说明训练时除以保留概率进行反向缩放；不指反向传播；类名保留 |
| co-adaptation / redundant representation | 协同适应（co-adaptation）/ 冗余表示 | 神经元依赖特定其他神经元；不是永久删除 |
| mask / keep probability | 掩码 / 保留概率 | Bernoulli(1 - p)，与丢弃概率 p 区分 |
| ensemble / subnetwork | 集成 / 子网络 | 源近似和等价断言保留并另列适用边界 |
| weight decay / decoupled weight decay | 权重衰减 / 解耦权重衰减 | 沿 S43；不暗等同 Adam 中的 L2 梯度惩罚 |
| BatchNorm / batch normalization | BatchNorm / 批量归一化 | 沿 S15；跨批量的统计与特征轴不同 |
| LayerNorm / layer normalization | LayerNorm / 层归一化 | 样本内特征归一化，类/API 名保留 |
| RMSNorm / root mean square | RMSNorm（均方根归一化）/ 均方根 | 无减均值；源公式缺 epsilon 与加速断言另列 |
| running statistics / running average | 运行统计量 / 运行平均值 | 训练累积供推理使用；指数移动平均沿 S43 |
| internal covariate shift | 内部协变量偏移（internal covariate shift） | 层输入分布变化；源对论文结论的强表述不暗修 |
| scale and shift / re-centering | 缩放和平移 / 重新中心化 | gamma/beta 可学习参数；不与模型扩容混同 |
| Post-LN / Pre-LN | Post-LN（后置层归一化）/ Pre-LN（前置层归一化） | 保持架构顺序与英文缩写 |
| data augmentation / invariance | 数据增强（data augmentation）/ 不变性 | 标签保持假设按原文，图片/文本/音频处理不同 |
| early stopping / patience | 早停 / 耐心窗口（patience） | 等待若干训练轮未改善；验证集与测试集混用只列源风险 |
| generalization gap / train-test gap | 泛化差距 / 训练与测试差距 | 不同于训练集和测试集划分；不擅改百分比为百分点 |
| spatial dropout / feature channel | 空间 Dropout（spatial dropout）/ 特征通道 | 整组通道失活与单神经元失活区别 |

MLP、CNN、LLM 首次释义；Lipschitz、ImageNet、GPT-3、LLaMA、Mistral、PyTorch 及 API 保留。数量词自然中文并记录等值，175/500 billion 保留原数字与量级并括中文释义，避免改变原数值控制。
