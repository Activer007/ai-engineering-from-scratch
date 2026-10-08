# S165-self-attention-from-scratch terminology proposal

Source-only lexical proposal, 2026-10-08 UTC. No Chinese lesson prose has been drafted. Fixed source: `1bafaa88bb4668356791150bec3a6d7df38387eb`.

The 164 common pin objects are retained exactly in DEPENDENCIES.json (156 terminology files and eight controls). All common candidate bytes were verified locally. A full-text lexical search over the 156 terminology files and reading of relevant matches supports this proposal; this is not a claim to have semantically read every unrelated row. Publication, independent support readback, installed167 and separate author calibration remain pending. Prior terminology files retain their historical status prose; those statements are not new S165 claims.

| English | Proposed Chinese / rendering | Context and alignment |
|---|---|---|
| Self-Attention from Scratch | 从零实现自注意力 | New title proposal for this exact source H1. |
| self-attention / cross-attention | 自注意力 / 交叉注意力 | Core addendum, S92. Same-sequence Q/K/V versus Q from one sequence and K/V from another. |
| query / key / value | 查询 / 键 / 值 | S92. Q/K/V roles; not credentials, database indexes or product value. |
| scaled dot-product attention | 缩放点积注意力（scaled dot-product attention） | S92 and S151. Keep sqrt(dk), transpose and softmax axis unchanged. |
| attention score / attention weight | 注意力分数 / 注意力权重 | S92. Before versus after softmax, never interchangeable. |
| attention matrix | 注意力矩阵 | State whether referring to scores or weights in each source context. |
| multi-head attention / attention head | 多头注意力 / 注意力头 | S14, S45, S92. Heads are parallel projections, not layers or classification heads. |
| causal masking / causal mask | 因果掩码操作 / 因果掩码 | S38, S151. Blocks future positions; exercise scope, not implemented-demo claim. |
| bidirectional / autoregressive attention | 双向注意力 / 自回归注意力 | Source objective distinguishes unrestricted versus decoder-style access. |
| token | token（词元）；后续 token | Core. Not necessarily one word; no credential sense. |
| embedding / token embedding | 嵌入 / token 嵌入 | Core. Vector representation rather than an insertion operation. |
| logits | logits（未经归一化的分数） | Core addendum. Keep code identifiers unchanged. |
| softmax / softmax saturation | softmax / softmax 饱和 | Core naming; no transliteration or universal non-saturation guarantee. |
| row-wise softmax | 逐行 softmax | Each query row normalizes over keys; do not swap axes. |
| weighted sum / weighted blend | 加权和 / 加权组合 | Preserve the source operation and its uncorrected example coefficients. |
| weight matrix | 权重矩阵 | S05, S29. Distinguish model parameters from attention weights. |
| learned projection / linear projection | 学习得到的投影 / 线性投影 | Preserve source conceptual phrasing; demos only initialize randomly and do not train. |
| numerical stability / vanishing gradients | 数值稳定性 / 梯度消失 | Subtracting row maximum; no all-masked-row behavior guarantee. |
| context vector / hidden state | 上下文向量 / 隐藏状态 | S89, S92. Do not conflate context contents with changing tensor shape. |
| concatenation / output projection | 拼接 / 输出投影 | Preserve concatenation axis and final Wo multiplication. |
| Xavier-like scaling | 类似 Xavier 的缩放 | Keep the source qualifier; no exact initializer-equivalence claim. |
| soft database lookup | 软数据库查找 | Conceptual analogy: similarity-weighted values rather than an exact-key return. |
| coreference | 共指 | Relationship example, not evidence learned by random weights. |

Core and addendum take precedence. First prose mentions use the established Chinese/English convention; code, API names, math, tensor shapes, dimensions, seeds, paths, links, Mermaid and figure payloads remain unchanged. This support proposal is not Chinese semantic review and does not close the separate pre-prose calibration gate.
