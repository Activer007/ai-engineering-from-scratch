# S74 关系抽取与知识图谱构建术语增量 v1.0

2026-10-03。固定英文05-26；继承核心/补充表和78项不可变支持文件。实体与跨度沿S55，实体链接沿S71，共指沿S65，pipeline沿S57“管线”，provenance沿核心“来源信息”。仅借鉴术语，不读取旧中文正文。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| relation extraction / RE | 关系抽取（relation extraction，RE） | 从文本识别实体之间的关系，不等同实体链接或关系数据库抽取 |
| knowledge graph / KG | 知识图谱（KG） | 节点、边及其来源信息；不把玩具邻接表等同生产图存储 |
| triple / subject / relation / object | 三元组 / 主体 / 关系 / 客体 | `(subject, relation, object)`及代码元组保持原样；保留有向关系的主体客体次序 |
| provenance / anchor / span | 来源信息（provenance）/ 锚定 / 文本跨度（span） | 以文档标识符和字符区间追溯；不是事实真伪保证 |
| ontology / closed ontology | 本体（ontology）/ 封闭本体 | 有限关系类型集合，与开放词汇关系区分；Wikidata/FIBO/UMLS保留 |
| Open IE / OpenIE | 开放信息抽取（Open IE）/ OpenIE | 开放词汇关系短语；不擅自互换源缩写拼写 |
| canonicalization / canonical id | 规范化（canonicalization）/ 规范标识符 | 表面实体名或关系映射到标准标识符；不与向量归一化混同 |
| rule / pattern-based / Hearst pattern | 基于规则 / 基于模式 / Hearst 模式 | 保留源英文实体和模式示例；正则表达式完全不改 |
| supervised classifier / generative LLM | 监督分类器 / 生成式大语言模型（LLM） | 类别预测与生成抽取分开；框架代码不因源接口错误被修改 |
| AEVS | AEVS（锚定—抽取—验证—补充） | Anchor-Extraction-Verification-Supplement与2026源主张保留；不声称已运行完整框架 |
| distant supervision / seq2seq | 远程监督（distant supervision）/ 序列到序列（seq2seq） | 用已有KG与文本对齐生成训练数据；非人工逐例标签 |
| precision / recall / hallucination rate | 精确率 / 召回率 / 幻觉率 | 区分数值指标与源文定性判断；无实测不扩写为验收结果 |
| temporal qualifier / dedup | 时间限定符 / 去重 | P580/P582等标识符原样；不把代码未实现的去重或时态处理当成已实现 |
| NER / coreference / entity linking / RAG | 命名实体识别（NER）/ 共指消解 / 实体链接 / 检索增强生成（RAG） | 前置阶段相互区分，首次正文解释缩写；pipeline统一“管线” |

专名、产品、模型ID、属性ID、API、引用题名、路径与URL保持源形。英文例句保留实体和关系字符串以对照模式/跨度；中文解释不修正源代码的方向、键大小写或数据结构错误。仅普通裸URL后必要的ASCII空格可避免中文标点吞入href；若正文乘号需最小转义，先报告独审并要求原strict通过、数学不变，绝不改保护载荷。

自然语言数量映射：Four/Three → 四/三；every/each → 每个；Step1–5标题保留1–5；minutes → 分钟；11,000+、2015–2022、2026、60-80%、2005、24、25、5、50等数值和范围保持源形。正文的“60-80%工程工作”等经验主张保留并单列源风险。通用章节遵循补充表，Pitfalls为“常见陷阱”；强调闭合符后保留ASCII空格。
