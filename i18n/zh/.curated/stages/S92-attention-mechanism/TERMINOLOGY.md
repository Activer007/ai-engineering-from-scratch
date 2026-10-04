# S92-attention-mechanism 术语增量 v1.0

日期：2026-10-04 UTC。作者新提案已与完整固定89份参考词表校准。本文件是待协调者精确字节确认的本地预发布支持候选，不是译文审校或正式接受。冻结后保留该预发布快照；publication字段的null仅表示冻结时尚未绑定发布提交，不自引用本文件的Git提交，也不声称永久未发布。实际发布commit由后续作者record和远端回读receipt绑定。

固定英文：`1bafaa88bb4668356791150bec3a6d7df38387eb`。规范 docs H1：Attention Mechanism — The Breakthrough。

本轮核验正式基线为106课。参考集合为86份正式TERM（84 accepted stage＋core2）和3份active-reviewed TERM（S88/S89/S90），共89份；另有8份原controls，common共97。本课own3另计，总100。S85现属正式已接受，不沿用旧支持快照中的active状态；旧TERM原字节和历史105叙述保留，其历史文字不是本轮状态。S88/S89/S90与本轮新draft不提前计入正式106。完整固定来源见 DEPENDENCIES.json。

| English | Proposed Chinese / rendering | Context and boundary | Existing alignment |
|---|---|---|---|
| Attention Mechanism — The Breakthrough | 注意力机制：关键突破 | Exact source H1, no subtitle from another lesson | New course title |
| attention | 注意力；注意力机制 | Query-key scores weight a value sequence | Core TERM |
| attention score / weight | 注意力分数 / 注意力权重 | Before / after softmax; never interchangeable | S14 |
| additive attention | 加性注意力（additive attention） | Bahdanau learned projections, tanh and final scalar projection; not adding weights directly | New specificity; source Shapes and Build Step 1 |
| multiplicative attention | 乘性注意力（multiplicative attention） | Luong dot/general score families; dot has equality constraint | New specificity; source Shapes and Key Terms |
| query / key / value | 查询 / 键 / 值 | Q queries, K is scored against, V is summed; unrelated to API keys, financial value, or PRNG key | Core attention semantics; source Build Step 4 |
| self-attention / multi-head attention | 自注意力 / 多头注意力 | First explanatory mention also keeps English; self-sequence relation vs parallel projected heads | Core addendum, S14, S45 |
| scaled dot-product attention | 缩放点积注意力（scaled dot-product attention） | Preserve source bridge claim; do not silently add Transformer equations | Source Build Step 4 |
| hidden state | 隐藏状态（hidden state） | Neural-network representation; not notebook/workflow hidden state | S29, S35, S86 |
| encoder / decoder | 编码器 / 解码器 | State producer / state-conditioned output generator | S29, S86 |
| context / context vector | 上下文 / 上下文向量 | Weighted average changes at each decoding step; vector dimensionality remains d_h | S86 fixed-size context-vector terminology |
| reshape each step (prose metaphor) | 内容随每一步改变 | Does not mean tensor shape changes | Source Concept vs Shapes table |
| broadcasting | 广播（broadcasting） | Decoder projection broadcast over encoder positions; not a matrix multiplication rule | S05, S14 |
| alignment / alignment matrix | 对齐关系 / 对齐矩阵 | Matching sequence positions; weights arranged by decoder and encoder positions | Source numerical example and Use It |
| masking / padding token | 掩码 / 填充 token | Exercise requirement only; not implemented in shipped main | S37 mask, core token |
| token | token（词元）；后续 token | First occurrence explained; not always a word | Core, S86 |
| ablation / counterfactual check | 消融实验 / 反事实检验 | Required evidence before treating weights as reasoning explanations | S70 for ablation; source caveat for counterfactual |
| RNN / GRU / BiLSTM | 循环神经网络（RNN）/ GRU（门控循环单元）/ BiLSTM（双向长短期记忆网络） | First prose explanation only; protected identifiers untouched | S06 RNN, S46/S55 BiLSTM, S86 acronym preservation |

## 词义和结构边界

核心/补充词表优先；首现按既定中英对应，专名、API、代码标识符保留。通用章节标题沿ADDENDUM，但不得新增源没有的章节。保护数字、单位、形状、轴次序、公式、代码、图载荷、链接、路径和源文件间差异。自然语言数量须等值逐块对照。

参考术语仅供一致性校准，不能复用旧译文正文。支持准备未读取旧中文课文、旧record的segments或format_revisions、452/457材料；按需读取的docs/i18n.md规范含既有中文质量示例，这项暴露已如实记录，示例措辞未复用。source阅读、术语准备及作者draft不构成新增正式完成课。

查询/键/值是注意力Q/K/V角色，键不是API密钥或JAX PRNG key，值不是产品价值。隐藏状态沿S29/S86神经网络含义，不用S01隐式状态或S84工作流隐性状态。编码器/解码器、固定大小的上下文向量沿S86及S89。对齐矩阵的行/列分别对应解码/编码位置；不得把改变上下文内容译成改变其张量形状。
