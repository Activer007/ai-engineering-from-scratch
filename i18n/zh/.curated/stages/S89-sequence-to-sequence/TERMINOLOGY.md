# S89-sequence-to-sequence 术语增量 v1.0

日期：2026-10-04 UTC。作者新提案已与完整固定参考术语集合校准；本文件保存冻结时的预发布支持快照，精确字节冻结由协调者确认回执证明。publication字段的null记录冻结时的历史状态，不自引用本文件的Git提交；实际发布commit由后续作者record和远端回读receipt绑定。它不是译文审校或正式接受。

固定英文：`1bafaa88bb4668356791150bec3a6d7df38387eb`。规范 docs H1：Sequence-to-Sequence Models。

正式基线保持105课；参考集合为85份正式TERM（83 accepted stage＋core2）及1份 active-reviewed S85 TERM，共86份。S85的固定TERM提交为 `1a364d8283c864eccac467bb32a850a0d0779eef`，已独立语言审/GFM，但不将其标为正式106或中文先修门禁。来源逐项见 DEPENDENCIES.json。

| English | 建议中文 | 语境与边界 |
|---|---|---|
| Sequence-to-Sequence Models / sequence-to-sequence | 序列到序列模型 / 序列到序列（seq2seq） | 标题用中文，正文首次解释seq2seq；源seq2seq缩写后续保留 |
| teacher forcing | 教师强制（teacher forcing）；后续教师强制 | 训练时把前一位置的真实token作为解码器输入；不是额外教师网络 |
| scheduled sampling | 计划采样（scheduled sampling）；后续计划采样 | 逐步降低教师强制比例，混入自身预测；不是学习率调度或一般随机抽样 |
| exposure bias | 曝光偏差（exposure bias）；后续曝光偏差 | 训练与推理输入分布差异；不是社会偏见或类别不平衡 |
| greedy decoding | 贪心解码（greedy decoding）；后续贪心解码 | 每步最高概率token；不是全局最佳序列保证 |
| beam search / beam width | 束搜索（beam search）/ 束宽 | 保留top-k未完成序列；宽度3-5、3、4按各源处分别保留 |
| minimum risk training | 最小风险训练（minimum risk training） | 源描述句级BLEU目标；不暗中补可微性或期望风险推导 |
| ground-truth token | 真实 token | token沿核心表首现“token（词元）”，后续保留token；不是模型预测 |
| backprop through time | 随时间反向传播 | 两个RNN沿时间展开反向传播；不是逆向生成 |
| cross-entropy loss | 交叉熵损失（cross-entropy loss） | 解码器逐步损失沿序列求和 |
| reinforcement learning fine-tuning | 强化学习微调（reinforcement learning fine-tuning） | 用指标奖励序列生成器；保留RLHF名词 |
| parallel corpus / parallel examples | 平行语料库 / 平行样本 | 成对源/目标文本；不是并行计算 |
| held-out inputs | 留出的输入 | 训练之外的比较输入；不假称测试集独立抽样细节 |

## 词义和结构边界

核心/补充词表优先；首现按既定中英对应，专名/API/代码标识符保留。九种通用章节标题沿ADDENDUM。保护数字、单位、形状、轴次序、公式、代码、图载荷、链接、路径和源文件间差异。自然语言数量须等值并逐块对照，不改变数字字面量。

参考术语仅用于一致性；没有读取历史中文课文、translation segments、format_revisions或旧作者缓存。来源词表不等于可复用中文正文，source阅读/术语定义不计新增完成课。

沿正式S86：encoder/decoder=编码器/解码器，hidden state=隐藏状态，fixed-size context vector=固定大小的上下文向量，fine-tuning=微调，streaming=流式，on-device=设备端。token首现token（词元）；logits首现logits（未经归一化的分数）。新教师强制/计划采样/曝光偏差均是本课seq2seq训练语境，不套用于学习率调度、类别偏差或额外教师网络。
