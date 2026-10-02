# S37 预训练数据处理流水线术语增量 v1.0

2026-10-02。作者提案，待协调者确认。联用固定核心、试点补充及 DEPENDENCIES.json 指定词表。此文件不覆盖旧控制或课程正文。

| EN | 推荐呈现 | 语境与边界 |
|---|---|---|
| data pipeline / streaming | 数据处理流水线 / 流式读取 | 沿 S04；这里是数据迭代，不是模型的流式输出。原实现全部载入列表的差距另记 |
| pre-training | 预训练（pre-training） | 与微调区分；本次不实际训练模型 |
| token / tokenizer / tokenization | token（词元）/ 分词器 / 分词 | 沿核心与 S33，不把 token 当成词、字或认证令牌 |
| deduplication / exact / near-duplicate | 去重 / 完全重复 / 近重复 | 近重复基于片段集合相似度，不能保证发现所有语义重复 |
| shingling / shingle / n-gram | 构造片段集合 / 片段 / 连续 n 元片段 | 首现中英；源示例字符串和片段集合逐字保留；不要理解为单个哈希值 |
| MinHash / LSH | MinHash / 局部敏感哈希（Locality-Sensitive Hashing，LSH） | 沿 S16；专名、缩写保留，不等同无条件精确去重 |
| signature / band / bucket | 签名 / 分带 / 桶 | 此处是 MinHash 摘要结构、签名分组与 LSH 分桶，不是数字签名或密码学认证 |
| Jaccard similarity | Jaccard 相似度 | 沿 S16；交集大小/并集大小，空集处理按源代码另记 |
| precision / recall / false positive | 精确率 / 召回率 / 误报 | 沿 S17/S28；这里是去重候选筛选，不是浮点精度 |
| sequence packing / padding token | 序列打包 / 填充 token | 多文档拼接及固定长度填充，不掩盖源中最后序列仍有填充的事实 |
| attention mask / block-diagonal attention mask | 注意力掩码 / 分块对角注意力掩码 | 正文概念与实际仅为 padding mask 的代码差距单列 |
| end-of-sequence token | 序列结束 token | [EOS]、eos_id 等标记保持；不把填充 token 与 EOS 互换 |
| perplexity / perplexity filter | 困惑度 / 困惑度过滤器 | 沿 S12，语言模型意义；不能与 t-SNE 困惑度混淆；练习 bottom 20% 歧义不暗修 |
| corpus / bigram language model | 语料库 / 二元语言模型 | 本地生成示例语料与正文所称 Project Gutenberg 语料差距单列 |
| compression ratio / fertility | 压缩率 / 平均每词 token 数（fertility） | 沿 S33；前者在此按每 token 字符数，不是压缩文件存储比例 |
| overtraining / compute-optimal / inference-optimal | 超量训练 / 计算最优 / 推理最优 | 相对于 Chinchilla 计算最优配比继续训练，不与过拟合（overfitting）混同 |
| PII / NER | 个人身份信息 / 命名实体识别 | PII 沿试点补充；不把匿名化能力说成已在当前代码实现 |
| throughput / sequence utilization | 吞吐量 / 序列利用率 | 不把单机小语料耗时当成 GPU/TB 级供给性能 |

## 数量、单位和专名

- `terabytes` → “太字节级”，两处：b0009、b0015。保留复数量级，不假造明确容量
- `15.6 trillion` → “15.6 万亿”，b0017、b0031；`8.1 trillion` → “8.1 万亿”，b0017；`1.4 trillion` → “1.4 万亿”，b0019。trillion = 万亿，数值不变
- `300 billion` → “300 billion（三千亿）”，b0017、b0019。协调者明确选择源形保留并用自然中文解释，符合固定 ADDENDUM 的默认规则。等值关系为 300 × 10^9 = 三千亿；不是“三百亿”，不加进正文新的阿拉伯数字以避开原 strict 块内数字门禁
- `~90 minutes` → “~90 分钟”，b0005。时间量纲与近似性不变
- `10x` / `3-4x` / `10-50x` → “10 倍”/“3-4 倍”/“10-50 倍”，分别保留原数字及倍数语义；b0097 中仍忠实保留原文“相同损失”的断言
- `70B`、`280B`、`175B`、`300B`、`1.4T`、`2T`、`15T`、`15.6T` 等缩写原样；表内参数量和训练 token 数不互换
- TB、GB、FLOPs、所有百分比、O(n^2)、N_opt/C/D_opt 公式、数字符号与模型中的数字原样
- Common Crawl、Wikipedia、GitHub、BookCorpus、Pile、arXiv、S2ORC、StackOverflow、Reddit、C4、RefinedWeb、DeepMind、Meta、Project Gutenberg、HuggingFace、fastText、MinHash、Chinchilla 及所有模型/数据集 ID 原样。英文论文题名保留可检索性，描述独立新译
