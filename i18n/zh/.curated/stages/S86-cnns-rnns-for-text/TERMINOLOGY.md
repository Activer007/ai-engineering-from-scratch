# S86-cnns-rnns-for-text 术语增量 v1.0

日期：2026-10-04 UTC。此为源作者提案校准后冻结的起草支持快照；不代表译文完成、独立审校或正式接受。

固定英文：`1bafaa88bb4668356791150bec3a6d7df38387eb`。规范标题：CNNs and RNNs for Text。

正式术语基线：actual103，83份TERM（81 accepted stage＋core2），各路径和固定来源见同目录 DEPENDENCIES.json。旧 pending S61/S66/S79 未纳入。作者完整英文阅读后提出以下词义；没有复用旧中文课文、segments或format_revisions。

| Source term | Chinese treatment | Boundary |
|---|---|---|
| CNNs and RNNs for Text | 用于文本处理的 CNN 和 RNN | Course title rendering; preserve CNN/RNN acronyms |
| convolution / convolutional neural network | 卷积 / 卷积神经网络 | CNN retained where source uses the acronym |
| TextCNN | TextCNN | Preserve named architecture |
| recurrence / recurrent neural network | 循环机制 / 循环神经网络 | Not 递归; explain repeated state transition in time |
| RNN / LSTM / GRU | RNN / LSTM / GRU | Preserve acronym; no invented expansion in protected terms |
| hidden state | 隐藏状态 | Neural-network state; never 工作流“隐性状态” |
| cell state | 细胞状态 | Distinguish from hidden state; new course-local term; no conflicting entry in formal83 TERM set |
| bidirectional / BiLSTM | 双向 / BiLSTM | Two temporal directions; not backpropagation |
| token | token（词元）；后续 token | Core first-mention convention; do not collapse to word |
| word embedding | 词嵌入（word embedding） | Along S49; distinguish context-conditioned vectors from static inputs |
| contextualized embeddings | 上下文嵌入 | Along S49 static/contextual distinction |
| n-gram / trigram | 连续 n 元片段（n-gram）/ 三元片段（trigram） | Align S49 character n-gram wording; here consecutive words/tokens, not arbitrary triples |
| filter / filter width | 滤波器（filter）/ 滤波器宽度 | Along S83; distinguish sequence width from embedding channels |
| feature map / activation | 特征图 / 激活值 | Per-filter activations before pooling |
| global max-pooling | 全局最大池化 | Takes strongest activation over sequence positions |
| mean-pool / last-state pooling | 平均池化 / 末状态池化 | Last state refers to last hidden state, not the last input token |
| position-invariant | 位置不变的 / 位置不变性 | No assertion that the entire network ignores word order |
| concatenate | 拼接 | Not sum or average |
| classifier head | 分类头 | Distinguish encoder from downstream prediction layer |
| parameter sharing / shared parameters | 参数共享（parameter sharing）/ 共享参数 | Along S83; same W/U/b used across time steps |
| input / forget / output gate | 输入门 / 遗忘门 / 输出门 | Gate names; not approval/verification gates |
| vanishing / exploding gradients | 梯度消失 / 梯度爆炸 | Distinguish scalar illustration from actual network gradient |
| long-range / distant dependency | 长距离依赖 | Keep length thresholds as source claims |
| sequential bottleneck | 串行计算瓶颈 | Source means dependence across time, not generic ordered workflow |
| fixed-size context vector | 固定大小的上下文向量 | “大小” concerns dimensionality here |
| encoder / decoder | 编码器 / 解码器 | Distinguish encoder state from embeddings |
| frozen encoder / frozen embeddings | 冻结的编码器 / 冻结的嵌入 | No parameter update; not cached inference output |
| fine-tune / fine-tuning | 微调 | Preserve code and prompt payload spelling |
| edge / on-device inference | 边缘端 / 设备端推理 | No new deployment recommendation beyond source |
| streaming / online classification | 流式 / 在线分类 | Online means incoming stream, not merely network-connected |
| sequence labeling / tagging | 序列标注 / 标注 | NER/BiLSTM-CRF kept as named source terms |
| baseline | 基线 | Model comparator, not proof of acceptance |
| regularization / dropout | 正则化 / Dropout（随机失活） | Along S69; preserve API identifiers |
| forward / backward | 前向传播 / 反向传播 | For bidirectional direction prose use 正向/反向; avoid conflating meanings |

## 结构与词义边界

首现使用 token（词元），以后用 token；神经网络 hidden state 用隐藏状态，与S01/S84工作流用语区分。细胞状态为本课上下文的新增词义，81份正式 stage TERM 无冲突条目。trigram 用三元片段，与S50原词条一致；不译为三元组。

不添加源无的学习目标。保护两份不同提示词载荷，各自忠实，不合并同步。元数据键与Build/Python保持；自然语言时间单位可译。核心/补充既有术语优先，学习代码不构成执行授权。
