# S60 子词分词术语增量 v1.0

2026-10-03。联用核心、增补及 66 项固定依赖；沿 S33/10-02、S54 术语，不引用其正文。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| subword tokenization / tokenizer | 子词分词（subword tokenization）/ 分词器（tokenizer） | token 首现词元说明，不等同单词或认证令牌 |
| BPE / byte-level BPE | BPE（字节对编码）/ 字节级 BPE | 迭代符号可为已合并 token；区分字符算法与256字节覆盖 |
| WordPiece / Unigram | WordPiece（子词分词算法）/ Unigram（基于概率的子词分词算法） | 算法专名保留；对数似然方向问题另列，不暗修 |
| SentencePiece / tiktoken / HF Tokenizers | SentencePiece（分词库）/ tiktoken / HF Tokenizers | 库、训练和仅编码区别；首次解释 SentencePiece |
| vocabulary / merge list | 词表 / 合并列表 | 有序合并规则与最终残留符号集不是完整可编码词表 |
| character coverage / whitespace | 字符覆盖率 / 空白字符 | 空格、字节、字符区分，▁ 与参数名不译 |
| likelihood / log-likelihood | 似然 / 对数似然 | 保留源增加方向及概率分词表述，风险账本解释 |
| pre-tokenization / subword regularization | 预分词 / 子词正则化 | 不混为向量归一化或普通字符切片 |
| held-out / compression ratio | 留出 / 压缩率 | 留出词未用于训练；沿 S33，不混同存储压缩 |
| tokenizer drift / context-window budgeting | 分词器漂移 / 上下文窗口预算规划 | 检查哈希与预算不是运行已验证声明 |

通用章节沿增补：要解决的问题、核心概念、动手实现、实际使用、交付成果、练习、关键术语、延伸阅读。元数据标签及 Learn/Python 不变；~60 minutes→~60 分钟。three algorithms/libraries/facts/words→三种算法/三个库/三个事实/三个词；single→单个；zero→零；one→一种。32k、50-100k、200k+、<1B、1-10B、5-10x、40 bits 和 O(n·|merges|) 源数值/单位保留，k/B 用千/十亿括注解释。强调边界保留空格，代码和围栏英语原样。
