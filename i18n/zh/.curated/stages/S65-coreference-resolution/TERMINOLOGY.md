# S65 共指消解术语增量 v1.0

2026-10-03。沿用核心/补充表与 70 项固定依赖；前置术语取 S55 命名实体识别、S46 词性标注与句法分析。只读已审术语，不读取旧译正文。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| coreference resolution / corefer | 共指消解（coreference resolution）/ 共指 | 多个表达式指向同一现实实体，不等同实体链接到知识库 |
| mention / span | 提及（mention）/ 文本跨度（span） | 沿 S55，连续文本区间；不是线性代数的张成 |
| antecedent / referent | 先行项（antecedent）/ 指称对象 | 前者为较早提及，后者为所指实体；不互换 |
| cluster / clustering | 簇 / 聚类 | 簇中提及同指一个实体；不把簇误当单条提及 |
| nominal / pronominal / appositive | 名词性提及 / 代词性提及 / 同位语 | 保留英文例子的实体、代词和边界 |
| anaphora / cataphora | 回指 / 后指 | 后文指向前文 / 前文指向后文；术语首次括注英文 |
| bridging anaphora / zero anaphora | 桥接回指 / 零形回指 | 桥接不必实体同一；原文分类保留、风险另记 |
| mention-pair / mention-ranking | 提及对 / 提及排序 | 成对同指判断与为单个提及排序先行项是不同建模方式 |
| transitive closure / span-based | 传递闭包 / 基于文本跨度的 | 保留 (m_i, m_j) 变量，不增加公式或推导 |
| agreement / recency / syntactic role | 一致性 / 邻近性 / 句法角色 | gender/number 指性别和语法数；source toy 未实现角色加分等差异另列 |
| precision / recall / accuracy | 精确率 / 召回率 / 准确率 | 沿 S55/S46；不把 mention-link accuracy 翻译为 F1 |
| NER / IE / QA / KG | 命名实体识别 / 信息抽取 / 问答 / 知识图谱 | 首次正文保留缩写并解释；POS 为词性，Parsing 为句法分析 |
| LLM / prompt / token | 大语言模型（LLM）/ 提示词（prompt）/ token（词元） | 沿核心词表；英文示例及保护提示词围栏原样 |

MUC、B³、CEAF、CEAF-φ4、BLANC、LEA、CoNLL F1、SpanBERT、XLM-R、OntoNotes、AllenNLP、spaCy-experimental、GPT-4o、Claude 与引用题名保留。通用章节沿 addendum；Pitfalls → 常见陷阱。粗体闭合边界保留空格。自然语言 Three/two/Five/first three → 三/两/五/前三，metadata minutes → 分钟，300-word → 300 个单词；数值 60-80%、~83、~15、2,000、50+、2025–26 等保留原形。不改 source 年代、模型兼容性或经验数字，统一记源风险。
