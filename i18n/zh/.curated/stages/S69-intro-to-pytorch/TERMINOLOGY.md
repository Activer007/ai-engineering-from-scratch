# S69 PyTorch 入门术语增量 v1.0

2026-10-03。继承核心、补充表及 74 项固定依赖，尤其已接受的 S63 迷你框架与 S14/S32/S43/S48/S58。唯一课文来源为固定英文 03-11；不借术语修正原文。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| tensor / shape / dtype / device | 张量（tensor）/ 形状（shape）/ 数据类型（dtype）/ 设备（device） | 元组、API、精度与设备标识符原样 |
| eager execution / static computation graph | 即时执行（eager execution）/ 静态计算图 | 运行时执行与预先定义计算图，不暗改历史断言 |
| autograd / tape-based autodiff | autograd（自动求导）/ 基于操作记录带的自动微分 | tape 为前向操作记录，反向遍历；不是磁带设备 |
| leaf tensor / requires_grad | 叶张量 / requires_grad | 保留属性名；源 only 的例外单列风险 |
| nn.Module / parameter registration | nn.Module / 参数注册 | 模块基类与自动发现参数；不译类名 |
| forward / backward / gradient accumulation | 前向传播 / 反向传播 / 梯度累积 | 梯度计算不同于优化器更新 |
| reshape / contiguous | 重塑形状 / 连续 | 沿 S14；源常数时间与 always 概括不静默修正 |
| logits / loss function | logits（未经归一化的分数）/ 损失函数 | 与 softmax 概率分开；类名和公式原样 |
| MLP / CNN / LLM | 多层感知机（MLP）/ 卷积神经网络（CNN）/ 大语言模型（LLM） | 专名不翻译；数字保护 |
| dropout / batch norm | Dropout（随机失活）/ 批量归一化 | 沿 S48/S63；训练与评估模式不同 |
| state dict / serialization / buffer | 状态字典 / 序列化 / 缓冲区 | 参数和缓冲区分别说明；源术语表遗漏不暗补 |
| mixed precision / master weights | 混合精度 / 主权重 | 源统一 float16 描述忠实保留，适用边界另列 |
| Dataset / DataLoader / epoch | Dataset（数据集）/ DataLoader（数据加载器）/ 轮（epoch） | API 原样；进程数、批次、样本与轮次分开 |
| learning rate scheduling / momentum | 学习率调度 / 动量 | 沿 S43/S58；LR 首次解释学习率 |

自然语言时间 minutes/seconds/hours 译分钟/秒/小时，次数 Five/three/two 按五/三/两等值表达；M、s/epoch 及数字、形状、单位符号保持源形。论文和阅读材料标题保留英文，介绍文字译中文。通用九个章节按补充表。术语表是译法约定，不代表源性能、历史或 API 概括已经验证。
