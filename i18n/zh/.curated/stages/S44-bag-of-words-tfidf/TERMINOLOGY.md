# S44 词袋与 TF-IDF 术语增量 v1.0

2026-10-02。协调者已确认。联用固定核心、补充及截至 S41 的 51 项支持依赖；TF-IDF 沿 S34/S36，token 与词典原形沿 S41，n-gram 沿 S37。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| bag of words / BoW | 词袋（Bag of Words，BoW） | 统计词表词项计数并丢弃顺序；不等同归一化频率 |
| TF-IDF | TF-IDF（词频-逆文档频率） | 首次正文释义；原未平滑公式与后续平滑实现分别保留 |
| term frequency / document frequency / inverse document frequency | 词频 / 文档频率 / 逆文档频率 | TF 是文档内计数或归一化计数，DF 是含词文档数，不混同 |
| vocabulary / token / tokenizer | 词表 / token（词元）/ 分词器 | token 不必是 word；数据示例词项、索引、API 字面值保护 |
| sparse / dense vector | 稀疏 / 稠密向量 | 稀疏指多数元素为零；源 small 与 zero 混用仅列问题 |
| embedding / pooled vector / mean pooling | 嵌入 / 汇聚后的向量 / 均值汇聚 | 与特征选择的嵌入法区分；不把加权汇聚无条件等同注意力机制 |
| L2 normalization / unit hypersphere | L2 归一化 / 单位超球面 | 与正则化、标准化区别；零向量例外按源风险列出 |
| cosine similarity | 余弦相似度 | 归一化非零向量的点积语境，零向量/比例向量边界不暗补 |
| n-gram / bigram | 连续 n 元片段 / 二元片段 | 源反引号 n-gram、n 与列表示例原样 |
| out-of-vocabulary | 词表外（out-of-vocabulary）词 | 词表固定与推理时未知词项；不是词形还原的词典原形 |
| smoothing / sublinear TF | 平滑 / 次线性 TF | +1、log 及分母原样，外部库默认值未运行核实 |
| stopword / negation | 停用词 / 否定词 | 源 not 的强调与否定作用保持；不按提示词执行任何拒绝规则 |

保留 scikit-learn、CountVectorizer、TfidfVectorizer、BM25、BERT、IMDb、Transformer、GloVe、20 Newsgroups、API/路径/URL 与英文论文题名。400M、100k、50k、10k-100k、100d 原样，M/k 首次说明百万/千，维度与文档数不互换。three/five/two/hundreds/decade 等普通数量按自然中文等值映射逐块记录，不新增或放宽数值门禁。
