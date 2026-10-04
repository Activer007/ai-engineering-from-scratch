# S127-self-supervised-vision 术语约定

固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；本地 own3 候选，未安装、未发布。原作者术语提案证据 SHA256 `de4175725589c7fbafff3f21dad29493d9435acc53291302aca6930e130db021`；当前源语境与实际修订边界如下。原 common130 保持，本候选仅追加已独核 S124–S126 TERM 为 common133。

| English | 本课中文 | 依据 | 语义边界 |
|---|---|---|---|
| self-supervised / contrastive learning | 自监督 / 对比学习 | S22、S40既有 | 从数据本身构造监督信号；不把半监督与无标签预训练混同 |
| representation collapse | 表示坍缩 | S40既有 | 所有输入趋向常量表示；不是GAN模式坍缩 |
| linear probe / linear classification head | 线性探测 / 线性分类头 | S91既有 | 分类探测语境冻结特征上训练线性分类器；原分类专属段落保持，不是零训练或全量微调 |
| linear head (generic downstream task) | 线性头 | R02 单句语义范围修订及独立增量 PASS | 一般下游任务不擅自限定分类；b0105 使用线性头，classification probe 专属段落仍使用线性分类头 |
| patch / MAE / mask | 图像块 / 掩码自编码器（MAE）/ 遮蔽 | S118既有 | 遮蔽是操作；掩码token是解码占位；不与分割掩码混用 |
| exponential moving average (EMA) | 指数移动平均（EMA） | S43既有 | 教师权重更新与中心均值缓冲分别处理 |
| projection head | 投影头（projection head） | ADDENDUM既有术语，当前SSL编码器之后的投影语境 | 不是分类头，不套用视觉语言桥接的维度定义 |
| pretext task | 前置任务（pretext task） | 作者语境提案 | 预训练目标任务，不是课程先修条件；不改成下游任务 |
| centering / sharpening / centre buffer | 中心化 / 锐化 / 中心值缓冲区 | 中心化沿既有数值术语；锐化在本课为分布温度语境提案 | 减均值与除温度分开；锐化不是图像滤波 |
| mask ratio | 遮蔽比例 | 作者语境提案，与S118遮蔽术语一致 | 被遮蔽图像块占比，75%遮蔽与25%可见不交换 |
| dense prediction / dense correspondence | 密集预测 / 密集对应 | 视觉语境提案 | 不是全连接层；保留检索/迁移/预测不同任务 |

原作者合并 linear probe / linear head 的历史提案完整保留；当前仅按已通过 R02 区分一般下游线性头与分类探测线性分类头。代码、公式、数字、路径、Mermaid/figure 载荷保持，术语参考不代表课程执行或正式验收。
