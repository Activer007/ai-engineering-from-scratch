# S41 文本处理术语增量 v1.0

2026-10-02。主协调已确认。沿核心、试点10/01、S33及截至S36的固定词表；46项只读依赖。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| tokenization / tokenizer / token | 分词 / 分词器 / token（词元） | token不必是单词，沿10/01；代码和示例输入字符串不译 |
| stemming / stemmer / stem | 词干提取 / 词干提取器 / 词干 | 规则剥离的输出，不等于语言学词根，也未必是词典词 |
| lemmatization / lemmatizer / lemma | 词形还原 / 词形还原器 / 词典原形（lemma） | 不用“词元原形”与token混同；需要的上下文按源呈现 |
| morphology / morphological analyzer | 词形学 / 词形分析器 | 语言学语境，区别图像形态学；时态、数、格均保留 |
| morphologizer | morphologizer（词形标注组件） | spaCy组件名原样；并不自动等于lemmatizer，源混用另列 |
| POS tagging / POS tag / POS tagger | 词性标注 / 词性标记 / 词性标注器 | NOUN、VERB、ADJ、AUX等标签与Penn Treebank/WordNet映射不改 |
| contraction / apostrophe | 缩约形式 / 撇号 | ASCII直撇号与Unicode弯撇号由源正则区别；不改don't等词项 |
| suffix / double consonant | 后缀 / 双辅音 | Porter步骤优先次序、1a/1b和ies->i等规则字面值保护 |
| lookup table / fallback | 查找表 / 回退规则 | 未命中与默认POS的不同来源分开，不声称完整语法分析 |
| stopword removal / lowercasing | 去除停用词 / 转小写 | 两项预处理不同，代码lower与Unicode规范化/大小写折叠不混同 |
| reproducibility drift | 可复现性漂移 | 库版本引起行为变化；源具体spaCy示例未验证，不声称普遍版本变化 |
| training / inference mismatch | 训练与推理不一致 | 训练和服务阶段同一输入处理约定，不是训练误差/测试误差的通用别名 |

Porter、WordNet、Penn Treebank、NLTK、spaCy、tokenizers、transformers、en_core_web_sm等保留。英文算法论文标题与全部URL不变。普通英文数量three/five译为三/五并记录等值映射；数字书写形式、版本2.x/3.x、20测试样句及元数据字段保持控制。
