# S136-image-retrieval-metric terminology support

Fixed English 1bafaa88bb4668356791150bec3a6d7df38387eb. Preauthor support candidate only. Common142 =134 TERM +8 controls; own3 pending publication. Newly available S132 TERM is appended from its independent fixed-commit readback; English prerequisites remain unchanged. No author proposal, calibration, first write, capture, record, strict or independent language review is claimed.

| English | Proposed Chinese | Semantic boundary / prior terminology |
|---|---|---|
| image retrieval / metric learning | 图像检索 / 度量学习 | Metric 是距离结构语境，不套评估指标；沿 S16/S24 |
| embedding space / backbone | 嵌入空间 / 主干网络 | 沿核心及 S75/S118 |
| anchor / positive / negative | 锚样本 / 正样本 / 负样本 | 沿 S40；不是检测锚框 |
| triplet loss / contrastive loss | 三元组损失 / 对比损失 | 沿 S40；公式与平方/非平方源差异单列 |
| hard / semi-hard negative mining | 困难 / 半困难负样本挖掘 | 沿 S40；保留相对正样本及 margin 的严格边界 |
| margin / temperature | 间隔 / 温度 | 沿 S40；不当作学习率 |
| proxy-based loss / class prototype | 基于代理的损失 / 类别原型 | 代理是可学习代表向量，不是网络代理 |
| L2 normalization / squared L2 | L2 归一化 / 平方 L2 距离 | 单位范数和距离平方分开 |
| cosine similarity / inner product | 余弦相似度 / 内积 | 沿 S16/S130；源中点积捷径条件不能扩大 |
| Recall@K / precision@K | Recall@K（召回率）/ precision@K（精确率） | 沿 S59；本课 Recall@K 定义为查询命中率，不重写成其他分母 |
| gallery / query / catalogue | 图库 / 查询 / 图像目录 | 候选图像集合、检索输入与业务目录分开 |
| instance-level / category-level retrieval | 实例级 / 类别级检索 | 同一具体对象与同一类别不同 |
| re-ranking / nearest neighbour | 重排序 / 最近邻 | 沿检索语境；不保证重排序必然提升指标 |
| held-out split / self-match | 留出划分 / 自匹配 | 排除同一图像需稳定 ID，不把同类都去掉 |
| FAISS / HNSW / product quantisation | FAISS / HNSW / 乘积量化 | 沿 S24；模型与索引标识符保留 |
| InfoNCE / NT-Xent / ProxyNCA | InfoNCE / NT-Xent / ProxyNCA | 专名保留，不能把不同损失当作完全相同公式 |

Preserve code, inline code, numbers, mathematical expressions, identifiers, URLs, paths, Mermaid/SVG and figure payloads. Fixed-source discrepancies are recorded separately rather than silently repaired. Real later author changes must retain this frozen snapshot and their actual chronology.

Support-only revision 2026-10-05T08:40:00.217783+00:00: append S132 TERM; original preparation and all terminology rows retained. Previous common141 candidate SHA256: 021c44d5196bc76b5195aedd31c3c3b0a6613e790d6d662fff4473d9acd3f3fd.
