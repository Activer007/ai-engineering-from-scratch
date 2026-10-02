# S33 从零构建分词器术语增量 v1.0

2026-10-02。主协调确认。联用核心、试点 10/01 补充与截至 S30 的固定词表。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| tokenizer / token | 分词器 / token（词元） | 首处解释；token 不等同单词，不译为认证令牌 |
| BPE / byte-level BPE | BPE（字节对编码）/ 字节级 BPE | 合并迭代的符号可以是先前合并 token，不局限初始字符对 |
| byte-level fallback | 字节级回退 | 完整256字节基础词表的回退能力；不保证本课ASCII预分词实现保全输入 |
| pre-tokenization / regex | 预分词 / 正则表达式 | regex 包标识符不译；Unicode属性转义与ASCII回退区别 |
| Unicode / NFKC normalization | Unicode / NFKC 规范化 | 字符规范化，不用数值“归一化”；源分解/组合定义错误另记 |
| canonical / compatibility decomposition, composition | 规范 / 兼容分解、组合 | 根据原文逐一译出，不悄悄修复NFKC两步倒置 |
| vocabulary / merge table | 词表 / 合并表 | token ID到字节串与有序合并规则不同，不互换 |
| special token | 特殊 token | 精确匹配标记，不等同所有用户字符串都安全变成控制标记 |
| chat template | 聊天模板 | 消息列表到token序列的格式；各模型标记保持源字面值 |
| leading space / whitespace | 前导空格 / 空白字符 | 空格、制表符、换行不可混用；示例字符串逐字保护 |
| fertility | 平均每词 token 数（fertility） | 沿试点，不与每字符token数或压缩比无条件互换 |
| compression ratio | 压缩率 | 依源度量/语料，token数不等同压缩后的存储字节数 |
| subword / ligature | 子词 / 连字 | Unicode码点、用户感知字符、UTF-8字节区别 |
| WordPiece / SentencePiece / Unigram | WordPiece（子词分词算法）/ SentencePiece（分词库）/ Unigram（基于概率的子词分词算法） | 沿10/01；库与算法不混同，源Llama代际概括单列 |

GPT-2/GPT-4/Llama 3/Mistral、OpenAI、HuggingFace、tiktoken、regex、CJK、ASCII、UTF-8 与代码符号不改。trillion/million/gigabytes 保留并解释自然数量单位，不改原数字或单位量纲。特殊token表中的转义竖线、裸围栏仅补text，其他GFM修复须协调者实际观察与重新绑定。
