# S64 嵌入模型术语增量 v1.0

2026-10-03；固定英文 05-22，联用核心、增补和 70 项固定支持依赖，承接 S49 Word2Vec、S59 信息检索及 S54/S60。不使用旧中文课文。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| embedding / dense / sparse / multi-vector | 嵌入（embedding）/ 稠密 / 稀疏 / 多向量 | 向量表示，不与特征选择嵌入法混同 |
| passage / token / vocabulary | 文本段落 / token（词元）/ 词表 | 一个段落向量与每个词元一个向量区分 |
| RAG / prompt | 检索增强生成（RAG）/ 提示词（prompt） | 首现解释 |
| bi-encoder / cross-encoder / reranker | 双编码器（bi-encoder）/ 交叉编码器（cross-encoder）/ 重排序器 | 独立编码与联合编码区分 |
| late interaction / MaxSim | 后期交互（late interaction）/ MaxSim | 每个查询 token 取文档最大相似度再求和 |
| Matryoshka Representation Learning | Matryoshka 表示学习（套娃表示学习） | 训练目标与任意向量截断不是同一事物；源无损断言不暗修 |
| RRF / recall / precision | 倒数排名融合（RRF）/ 召回率 / 精确率 | 排名融合不等于原始分数融合 |
| MTEB / BEIR | MTEB（大规模文本嵌入基准）/ BEIR（检索基准） | 源年份、任务数、分数保持；不声称当前已验证 |
| asymmetric encoding / checkpoint | 非对称编码 / 检查点 | 不把所有非对称模型理解为不同投影；原文定义保留单列风险 |
| Hashing Trick / normalization / quantization | 哈希技巧 / 归一化 / 量化 | toy 是有符号计数向量，不是已训练嵌入 |
| MRR / Pareto-optimal / p99 | MRR（平均倒数排名）/ Pareto 最优 / p99（第 99 百分位延迟） | 原指标及数值保留；p99 正文不另增数字 |

模型 ID、算法专名、API（应用程序编程接口）、代码、论文标题、路径、URL、figure 内容全保留。首现 k 表示千、M 表示百万；32k+、137M、100M、600M、335M、$/1M 等源形保留。自然数量等值映射：one/per→一个/每个，five→五个，three-tier→三层，all three→三种，first few→前几个，two→两，~60 minutes→~60 分钟；不改变阿拉伯数字或量纲。通用标题遵循增补；Pitfalls→常见陷阱。保留强调边界空格，避免中文标点使 GFM 粗体失效。
