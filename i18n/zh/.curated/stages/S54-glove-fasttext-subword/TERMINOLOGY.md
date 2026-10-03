# S54 GloVe、FastText 与子词嵌入术语增量 v1.0

2026-10-02。联用核心、增补和截至 S51 的 61 项固定依赖；承接 S49 词嵌入及 S33 分词器词表。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| word embedding / embedding table | 词嵌入（word embedding）/ 嵌入表 | 中心词 W 和上下文词 W_tilde 两张表分别表示，不混同 |
| co-occurrence matrix / matrix factorization | 共现矩阵 / 矩阵分解 | 窗口内有向计数，代码按距离倒数加权；源频次简化单列 |
| character n-gram / subword | 字符连续 n 元片段（character n-gram）/ 子词 | 不等同语素，也不等同每个 token 都是完整词 |
| morpheme / root / inflected form | 语素（morpheme）/ 词根 / 屈折形式 | 语言学的词形组成与变体；字符切片不保证语素边界 |
| BPE / byte-level BPE | BPE（字节对编码）/ 字节级 BPE | 后续合并对象可以是已合并 token，不限于原始字符；字符实现与完整字节覆盖区别 |
| token / vocabulary / OOV | token（词元）/ 词表 / 词表外（OOV，out-of-vocabulary） | ID、字节、字符和词不得互换；未见词的向量保证按源另列风险 |
| GloVe / Global Vectors | GloVe / Global Vectors（全局向量） | 专名保留；频率权重函数与文字方向不一致只列源风险 |
| WordPiece / SentencePiece | WordPiece（子词分词算法）/ SentencePiece（分词库） | 沿固定试点；本课的模型族一概而论不暗修 |
| pretrained checkpoint / word boundary | 预训练检查点 / 词边界 | API、模型名与 Ġ 原样；无模型或词向量下载验证 |
| Jaccard overlap / morphology | Jaccard 重叠度 / 词形变化 | 集合交并比例；不将共享片段当作语义接近的保证 |
| TF-IDF / Skip-gram | TF-IDF（词频-逆文档频率）/ Skip-gram | TF-IDF 首现释义，训练方式与完整实现边界分开 |

Word2Vec、GloVe、FastText、LSA、HAL、GPT、BERT、T5、LLaMA、Transformer、Shakespeare、Hugging Face、论文题名和 API 原样。自然数量按逐块等值映射：one embedding per word→每个词一个嵌入，two→两个，three→三种，a million entries→一百万个条目，seven pages→七页；元数据 ~45 minutes→~45 分钟。30k-100k、1k、300d 保留，k 表示千，d 表示维数，不混同合并次数、词表条目或向量维数。强调闭合分隔符后留源边界空格，避免中文紧接标点使 GFM 粗体失效。
