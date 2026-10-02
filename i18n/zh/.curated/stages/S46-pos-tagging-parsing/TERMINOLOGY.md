# S46 词性标注与句法分析术语增量 v1.0

2026-10-02。主协调确认。沿核心、增补及 S41 文本处理词表；本阶段 51 项固定依赖只读。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| POS tagging / POS tag / POS tagger | 词性标注 / 词性标记 / 词性标注器 | 沿 S41；词性类别与命名实体类别不混同 |
| token / lemmatization / lemma / morphology | token（词元）/ 词形还原 / 词典原形 / 词形学 | 沿 S41；词元不等于词典原形，词形不指图像形态 |
| syntactic parsing | 句法分析 | 分析句子结构，不是文件格式解析 |
| constituency parsing / dependency parsing | 成分句法分析 / 依存句法分析 | 短语层级与词间依存关系分别呈现，不互换 |
| head / dependent / relation | 中心词 / 依存词 / 关系 | 依存弧的三个角色；原 (head, dependent, relation) 三元组保留 |
| argument / grammatical relation | 论元 / 语法关系 | argument 为动词支配的句法或语义成分，不是函数参数 |
| tagset / tag lattice | 标记集 / 词性标记格（tag lattice） | 格为 Viterbi 动态规划的状态结构，不是 token 网格 |
| most-frequent-tag baseline | 最常见词性标记基线 | 每个词在训练集中的众数标记；未见词回退为全体标记众数 |
| bigram HMM | 二元 HMM；隐 Markov 模型（HMM） | 隐状态为标记、观测为词；不是朴素 Bayes 的类别独立假设 |
| transition / emission probability | 转移概率 / 发射概率 | 前者为给定前一个标记时当前标记的概率，后者为给定标记时词的概率 |
| Laplace smoothing | Laplace 平滑（拉普拉斯平滑） | 沿 S10/S36；本课 alpha=0.01，并非加一特例 |
| Viterbi / decoding / backtrace | Viterbi / 解码 / 回溯 | 最大概率完整标记序列；与逐位置边缘概率最大化不同 |
| transition-based / graph-based | 基于转移的 / 基于图的 | 句法分析器家族；不改 arc-eager、arc-standard 等标识符 |
| shift-reduce / maximum spanning tree | 移进-归约 / 最大生成树 | 栈操作与图解码分开；源关于 Eisner/归约动作的简化另列 |
| biaffine / CRF / BiLSTM-CRF | 双仿射 / 条件随机场（CRF）/ 双向长短期记忆网络与 CRF 的组合（BiLSTM-CRF） | 专名 Dozat-Manning 保留；不是普通逐 token 独立分类的同义词 |
| gazetteer | 专名词表（gazetteer） | NLP 中的实体名称资源，不窄化为地图 |
| precision / recall / accuracy | 精确率 / 召回率 / 准确率 | 沿 S28/S39，不把准确率与标注者一致率混用 |

PTB、UD、Penn Treebank、Universal Dependencies、Brown、spaCy、Stanza/stanza、NLTK、trankit、MaltParser、Eisner、Chen、Manning、Viterbi 及代码、标签、模型 ID 全部保留。自然语言 twenty years → 二十年；two → 两；single/one → 一个；2010s → 2010 年代，量纲逐项记入作者记录。裸围栏只补 text；figure、代码和产物提示词不译、不执行产物提示词。
