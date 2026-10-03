# S59 信息检索与搜索术语增量 v1.0

2026-10-03；联用冻结核心、增补表及 66 项依赖，特别是 S44 词袋与 TF-IDF、S54 子词嵌入。来源为固定英文 05-14；不使用旧中文课文。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| information retrieval / IR | 信息检索（IR） | RAG 与搜索底层检索流程 |
| sparse / dense / hybrid retrieval | 稀疏 / 稠密 / 混合检索 | sparse 是词项信号；dense 是向量表征，fake-dense 不是真实嵌入 |
| embedding / bi-encoder / cross-encoder | 嵌入（embedding）/ 双编码器（bi-encoder）/ 交叉编码器（cross-encoder） | 独立编码对比联合编码，不改模型标识 |
| Reciprocal Rank Fusion / RRF | 倒数排名融合（RRF） | 只按排名合并，不按原始分数；代码 rank 从零计数，公式排名从一计数 |
| rerank / reranker | 重排序 / 重排序器 | 候选集合再打分，不混同重新检索 |
| inverted index / term-frequency saturation | 倒排索引 / 词频饱和 | 概念倒排索引与 toy 全扫描实现区分 |
| Recall@k / MRR / nDCG@k | Recall@k（召回率）/ MRR（平均倒数排名）/ nDCG@k（归一化折损累计增益） | 按源定义翻译；Recall 的单相关文档简化另列问题 |
| learned-sparse / late interaction | 学习型稀疏 / 后期交互 | SPLADE/ColBERT 原名保留，不承诺已验证优越性 |
| chunking / parent-doc pattern | 分块 / 父文档模式 | 小子块检索后换回父段落上下文 |
| HyDE / query expansion | HyDE（假设文档嵌入）/ 查询扩展 | 原文免费精确率提升之说保留并列风险 |
| L2-normalize / cosine | L2 归一化 / 余弦相似度 | 非零向量的单位范数，不混同正则化 |

BM25、RAG、FAISS、pgvector、Elasticsearch、OpenSearch、Qdrant、Weaviate、Vespa、Milvus、SPLADE、ColBERT、论文标题、模型 ID、API、路径与 URL 原样。RAG 首次释义检索增强生成；LLM、token、prompt 沿核心首现解释。通用章节依增补统一。普通英文数量词逐块等值映射；millions→数百万，Four→四，Three/two→三/两，one→一个；数值 50-200ms、top-30、top-5、1k-100k、100k-10M、10M+、8K、70-90% 原样保留。不得把比例或延迟当本轮实测结果。
