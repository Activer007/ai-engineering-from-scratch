# S55 命名实体识别术语增量 v1.0

2026-10-02。术语已由协调者确认。沿用固定核心/补充表与 61 项依赖；命名实体识别沿 S37，HMM/CRF/专名词表沿 S46，文本单位沿 S41，词嵌入沿 S49，分类指标沿 S28/S39/S51。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| named entity recognition / NER | 命名实体识别（NER） | 为连续文本中的实体标注类型；不等同仅提取人名 |
| BIO tagging / sequence labeling | BIO 标注 / 序列标注（sequence labeling） | B/I/O 及 BILOU 标签原样；BIO 与 BILOU 的边界能力不暗中混同 |
| span / nested entity | 文本跨度（span）/ 嵌套实体（nested entity） | 本课跨度为连续 token 的区间，不是线性代数的张成；区间端点和类型保持 |
| token / token classification head | token（词元）/ token 分类头 | 不把词元一律等同单词或字符；模型头不等同整套模型 |
| gazetteer / rule-based | 专名词表（gazetteer）/ 基于规则的 | 沿 S46；实体名称资源不窄化为地名表，词典消歧能力按源表述 |
| HMM / transition / emission | 隐 Markov 模型（HMM）/ 转移概率 / 发射概率 | 沿 S46；给定标记的 token 概率与标记间转移方向分开 |
| CRF / discriminative | 条件随机场（CRF）/ 判别式 | 沿 S46/S36；源对 BIO 合法序列保证的过强断言单列，不改代码或译文 |
| BiLSTM-CRF / hidden state | 双向长短期记忆网络与 CRF 的组合（BiLSTM-CRF）/ 隐藏状态 | 沿 S46；正文代码仅生成 emissions，不因类名声称包含 CRF 解码或训练 |
| word shape / hand-crafted feature | 词形模式（word shape）/ 手工设计的特征 | 大小写、数字等字符模式；不同于词形还原或词形学分析 |
| entity-level F1 / token-level F1 | 实体级 F1 / token 级 F1 | 保留跨度匹配与类型语境；precision/recall/accuracy 沿精确率/召回率/准确率 |
| zero-shot / few-shot / fine-tuning | 零样本 / 少样本 / 微调 | 提示词示例不等于权重更新；首次按上下文保留英文 |
| RAG / schema / ontology | 检索增强生成（RAG）/ schema（结构定义）/ 本体（ontology） | 不把实体类别集合与代码结构定义混为一谈 |
| domain shift / sparse type | 领域偏移（domain shift）/ 样本稀少的类型 | 领域改变与罕见标签分开；不把“稀疏”误解为矩阵存储格式 |

专名、标签和缩写保持源形，包括 Apple、Google、PERSON、ORG、GPE、PRODUCT、FACILITY、DRUG_BRAND、ADVERSE_EVENT、DOSE、Viterbi、BERT、GloVe、fastText、spaCy、Scispacy、BioBERT、ZeroTuneBio、CoNLL、Hugging Face、模型 ID、库名和参考题名。源 `Bank of America Tower` 等英文例句保留实体边界示例。

自然语言 five → 五、millions → 数百万、tens of thousands → 数万、thousands → 数千，逐块记录数量/单位与等值意义；`75 minutes` → `75 分钟`，`50ms`、`98%+`、`11-12%` 等数值和单位保留，不把百分比改成百分点。章节名遵循核心补充表固定九项；强强调闭合符之后接中文解释时使用 ASCII 空格，保护 GFM 边界。
