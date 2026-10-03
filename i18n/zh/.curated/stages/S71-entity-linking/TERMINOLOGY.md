# S71 实体链接与消歧术语增量 v1.0

2026-10-03。固定英文 05-25；沿用核心、补充表及 74 项不可变支持文件。前置术语承接已接受 S55 命名实体识别及 S65 共指消解，向量语境参照 S64；不读取旧译正文。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| entity linking / EL | 实体链接（entity linking，EL） | 将提及映射到唯一知识库条目，不等同 NER 类型标注或共指聚类 |
| disambiguation / disambiguator | 消歧 / 消歧器 | 根据上下文选择候选实体；不与候选生成混同 |
| mention / surface form / span | 提及（mention）/ 表面形式（surface form）/ 文本跨度 | 承接 S65/S55；保留英文示例中的实体字符串与边界 |
| knowledge base / KB / knowledge graph | 知识库（KB）/ 知识图谱 | KB 是知识库，不是存储单位；KB id 为知识库标识符 |
| candidate generation / alias index | 候选生成（candidate generation）/ 别名索引（alias index） | 表面形式到候选知识库条目的映射 |
| prior / context similarity / Jaccard overlap | 先验 / 上下文相似度 / Jaccard 重叠度 | 乘积公式与 main.py 加权相加不同，保留原文并单列源问题 |
| embedding / encoder / cosine similarity | 嵌入（embedding）/ 编码器 / 余弦相似度 | 向量表示；归一化后点积与余弦相似度的关系不扩写源代码 |
| generative / constrained decoding / trie | 生成式 / 约束解码（constrained decoding）/ 前缀树（trie） | token 与 character 的源描述差异不暗改 |
| mention recall / gold mention / top-1 accuracy | 提及召回率 / 标准答案中的提及 / top-1 准确率 | 保留源候选召回的定义、floor 表述与 99%/80% 例子，问题另列 |
| NIL / in-KB / out-of-KB | NIL（知识库中无匹配条目）/ 库内 / 库外 | 未知别名返回 None 与真正 NIL 检测分开 |
| popularity bias / KB staleness | 热门实体偏差 / 知识库过时 | 频繁实体与领域同名实体的混淆；不过度泛化模型公平性结论 |
| cross-lingual / held-out / fine-tuning | 跨语言 / 留出 / 微调（fine-tuning） | 首次按语境中英说明；保留基准名与模型名 |
| coreference / cluster | 共指消解 / 簇 | 同簇提及汇总为规范实体，不译成每次提及一个新实体 |
| NER / LLM / token / prompt | 命名实体识别（NER）/ 大语言模型（LLM）/ token（词元）/ 提示词（prompt） | 首现解释；围栏中的提示词和输出技能原样 |

通用章节遵循补充表；Pitfalls → 常见陷阱。保留品牌、模型名、论文标题、库名、Wikipedia/Wikidata/DBpedia、PERSON、NIL、AIDA-CoNLL、P@1、F1、所有实体 ID。粗体和斜体边界保留源空格以避免中文标点使 GFM 失效。

数量映射：Two/three/one → 两/三/一；decade → 十年；token-by-token → 逐 token；character-by-character → 逐字符；minutes → 分钟。~18M、34k、1k 等保留源缩写原形；M/k 首现用文字说明百万/千，不增加阿拉伯数字。top-1、10-30、2020-2024、2023+、1,393、30、50、100 等数字及单位不改。引用题名保持原文，后接中文描述。源事实疑点记入作者报告，不悄悄订正译文。
