# S50 N-gram 语言模型术语增量 v1.0

2026-10-02。协调者已确认。联用 56 项固定依赖；n-gram 沿 S37/S44，信息量与单位沿 S12，Laplace 平滑沿 S10/S36，token 沿核心及 S41。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| n-gram / n-gram language model | 连续 n 元片段 / n 元语言模型（n-gram language model） | 模型与片段分别表述；标题保留 N-gram，token 不必是单词 |
| unigram / bigram / trigram | 一元片段 / 二元片段 / 三元片段 | 语言模型用一元/二元/三元模型；这里的 unigram 不是 Unigram 子词分词算法 |
| smoothing / Laplace / add-one | 平滑 / Laplace 平滑（拉普拉斯平滑）/ 加一平滑 | 平滑概率质量；原代码加一而非任意 alpha，代码载荷不改 |
| Good-Turing / Kneser-Ney / Katz backoff | Good-Turing / Kneser-Ney / Katz 回退 | 人名算法保留英文；平滑、插值和条件回退不混同 |
| absolute discounting / discount | 绝对折扣法 / 折扣 | 从计数中扣除 D；不是金融贴现，D 的边界与归一化缺口另记 |
| continuation probability | 延续概率（continuation probability） | 按不同左上下文的种类数衡量，区别原始词频；不能把未见组合等同词表外词 |
| interpolation / backoff | 插值 / 回退 | 前者加权组合，后者按条件缩短上下文；代码为插值式 KN |
| frequency-of-frequencies | 频次的频次 | 统计出现给定次数的事件数，不是词频总和 |
| entropy / cross-entropy / negative log-likelihood | 熵 / 交叉熵 / 负对数似然 | 总体熵、模型编码代价及有限样本平均不得互换 |
| bits / nats | bits（比特）/ nats（奈特） | 英文单位保留，分别对应 log2 与自然对数；字符/token 的分母差异不能仅靠换对数底消除 |
| perplexity / branching factor | 困惑度 / 分支因子 | 有效选择数的解释不等于实际词表大小；比较还需相同数据、分词、边界与 OOV 约定 |
| token / vocabulary / OOV | token（词元）/ 词表 / 词表外（OOV） | 源 `<UNK>`、`<s>`、`</s>` 及示例词项不改；词表外处理与未见 n-gram 区别 |
| held-out test set / baseline / MLE | 留出测试集 / 基线 / 最大似然估计（MLE） | 留出集与训练集分开，源性能比例不保证在任意数据上成立 |
| sampling / greedy / beam search / temperature | 采样 / 贪心 / 束搜索 / 温度 | 贪心加随机性不自动成为束搜索；不同种子不保证不同序列，源断言单列 |
| rescoring / on-device autocomplete | 重评分 / 设备端自动补全 | 候选排序与初次生成不同；未实际调用 KenLM 或键盘系统 |

自然数量用中文等值表达：Fifty years → 五十年、a few hundred letters → 几百个字母、three-quarters → 四分之三、two tokens → 两个 token、Three moving parts → 三个组成部分。`~45 minutes` → `~45 分钟`，`10x` → `10 倍`；数字、范围、百分比、字母/token 分母保持语义和块内绑定。`100K` 原样。表内 `bits/letter` 保留并用中文说明。

Transformer、RNN、Shannon、Brown、San Francisco、San、Francisco、KenLM、Shakespeare、Birkbeck、Kneser-Ney、Good-Turing、Katz 及参考标题保留英文。所有代码、SVG、figure、路径、API、URL、公式与数值保持固定源字节或受保护 token；交付提示词原样保留且不执行。
