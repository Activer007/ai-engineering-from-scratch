# S45 Mini GPT 预训练术语增量 v1.0

2026-10-02。联用核心、补充表及 DEPENDENCIES.json 固定的 51 项支持文件；沿用 S37 预训练与 token、S38 因果掩码与残差连接、S40 logits 与交叉熵。本阶段术语已由协调者于 2026-10-02 确认。

| EN | 推荐呈现 | 语境与边界 |
|---|---|---|
| pre-training / checkpoint | 预训练 / 模型检查点 | 与微调、梯度检查点区分；不表示本次已训练或下载模型 |
| autoregressive / next-token prediction | 自回归 / 下一 token 预测 | 每个输出以先前 token 为条件；token 不等于单词 |
| token embedding / positional embedding | token 嵌入 / 位置嵌入 | 输入索引查表；不将输入嵌入、输出投影或位置向量角色互换 |
| language model head / logits head | 语言模型输出头 / logits 输出头 | logits 为 softmax 前未归一化分数；不是概率或对数概率 |
| weight tying | 权重绑定（weight tying） | 输入嵌入与输出投影共享同一矩阵；源参数表计算差距另列 |
| pre-norm / post-norm | 前置归一化 / 后置归一化 | 相对于注意力或前馈子层；与归一化轴和训练先后无关 |
| self-attention / multi-head attention | 自注意力 / 多头注意力 | 保留 Q/K/V 角色、头数、每头维度与形状变化 |
| LayerNorm / residual connection | LayerNorm（层归一化）/ 残差连接 | 类名原样；直接加法路径不等于全部参数梯度已实现 |
| KV cache / Prefill / Decode | KV cache（键值缓存）/ 预填充 / 解码 | 首现解释；新 token 的 Q/K/V 与旧缓存区分，源遗漏单列 |
| compute-bound / memory-bound | 受算力限制 / 受内存带宽限制 | 后者按源 GPU 带宽讨论语境；不是内存容量耗尽 |
| warmup / cosine decay | 预热 / 余弦衰减 | 沿 S11；学习率调度，不是模型缓存预热 |
| gradient accumulation / gradient clipping | 梯度累积 / 梯度裁剪 | 与参数更新、无反向传播的前向演示区分 |
| temperature / greedy decoding | 温度 / 贪心解码 | 温度影响采样分布；源温度零与实际除法代码矛盾单列 |
| top-p / nucleus sampling | top-p / 核采样 | 累计概率超过阈值的最小集合；top-k 与 top-p 标识原样 |
| wall-clock time / context window | 实际耗时 / 上下文窗口 | 端到端用时；裁剪旧 token 不等于已实现缓存 |

专名和缩写按源保留：GPT-2 Small、Mini GPT、GPT-4、Llama 3 405B、NVIDIA、A100、H100、PyTorch、numpy、GELU、ReLU、softmax、Adam、FFN、MLP、FP32、FLOPs、FLOPS。书名、论文题名、URL、公式和围栏负载保持原样。

数量映射：三个正文块 b0003、b0017、b0021 的 `124 million` 保留源数字和单位，并解释为“一亿二千四百万”，即 124 × 10^6；不改为不同阿拉伯数字，不放宽原 strict。`124M`、`38M`、`1.5B`、`405B`、`16K` 均保留源形，M/B/K 的量级分别是百万/十亿/千。元数据 `~120 minutes` → `~120 分钟`；文字 twelve → 十二、one → 一个、three → 三个等按原数量等值翻译。参数个数、层数、头数、token 数和内存单位不得互换。
