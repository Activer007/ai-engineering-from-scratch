# S49 Word2Vec 术语增量 v1.0

2026-10-02。协调者已确认。联用核心、增补及截至 S46 的 56 项固定支持依赖；本课词嵌入承接 S44，梯度承接 S32，词元/词表区别承接 S41。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| word embedding / embedding table | 词嵌入（word embedding）/ 嵌入表 | 输入中心词表和输出上下文词表角色分开；不是特征选择的嵌入法 |
| distributional hypothesis | 分布假设（distributional hypothesis） | 基于词语上下文的语言学假设，不是随机分布参数假设 |
| center word / context word / training pair | 中心词 / 上下文词 / 训练词对 | 保留有向词对次序；window 的源边界与示例不暗修 |
| Skip-gram / CBOW | Skip-gram / 连续词袋（CBOW，continuous bag of words） | 名称保留；预测上下文与预测中心的方向不能交换 |
| negative sampling / subsampling | 负采样（negative sampling）/ 子采样（subsampling） | 本课算法通称；抽取负词不与生成解码采样混同；筛除后的个数不保证等于 k |
| one-hot / softmax / sigmoid | one-hot（独热）/ softmax / sigmoid | 沿固定表；API 名原样，不将 softmax 目标与负采样目标视为相同 |
| logistic loss / dot product | 逻辑损失（logistic loss）/ 点积 | 正词对与负词对目标及两张表的梯度分别保持 |
| static / contextual embedding | 静态嵌入 / 上下文嵌入 | 词类型的固定向量与每次出现的上下文向量区别 |
| polysemy / analogy | 多义性（polysemy）/ 类比 | 例词和向量算式原样，类比成功不等于完整语义理解 |
| OOV / subword / character n-gram | 词表外（OOV，out of vocabulary）/ 子词 / 字符连续 n 元片段 | token（词元）不机械等同 word；具体算法覆盖边界单列 |
| TF-IDF / vocabulary / epoch | TF-IDF（词频-逆文档频率）/ 词表 / 轮（epoch） | 首现释义；词表大小、向量维数与训练轮数不互换 |
| bias axis / gender-neutral | 偏见轴 / 性别中立 | 本课公平性语境中的社会偏见，与统计估计偏差或神经元偏置分开；源去偏保证单列 |
| intrinsic / downstream evaluation | 内在评估 / 下游评估 | 原输出提示词保持英文，评估范围不由翻译扩大 |

Word2Vec、GloVe、fastText、Google News、Firth、Mikolov、Rong、ELMo、BERT、Transformer、gensim、NumPy、PCA、t-SNE 与 API/路径/论文题名原样。100k、10k、3M 及 300d 等源缩写保持，k 表示千、M 表示百万、d 表示向量维数。trillion-token → 万亿 token、billions of tokens → 数十亿 token、decade → 十年等采用自然中文等值映射并逐块入记录；不改变原阿拉伯数字或数量控制。
