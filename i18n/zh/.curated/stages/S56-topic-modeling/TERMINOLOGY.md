# S56 主题建模术语增量 v1.0

2026-10-02。协调者已确认。联用核心、增补及截至 S51 的 61 项固定支持依赖；概率分布抽样沿 S18，簇与离群点沿 S31，词表与 TF-IDF 沿 S44，嵌入沿 S49。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| topic modeling / topic | 主题建模（topic modeling）/ 主题 | LDA 的词概率分布与 BERTopic 的文档簇依原文分别解释 |
| LDA / Latent Dirichlet Allocation | LDA（隐 Dirichlet 分配） | 保留缩写与 Dirichlet 专名；不是 linear discriminant analysis |
| latent topic / mixed membership | 潜在主题 / 混合成员关系（mixed membership） | 每篇文档在所有主题上的分布，不等同单一硬分类 |
| generative story / inference | 生成过程 / 推断 | 先抽主题再抽词；反向由观测词推断文档主题与主题词分布 |
| collapsed Gibbs sampling | 折叠 Gibbs 抽样（collapsed Gibbs sampling） | 积分消去参数后的条件抽样；不与解码采样或梯度优化混同 |
| variational Bayes | 变分 Bayes | 推断方法名保留 Bayes；不在译文补加源未给出的推导 |
| class-based TF-IDF | 基于类别的 TF-IDF | TF-IDF 首现释为词频-逆文档频率；类别在此为文档簇 |
| soft membership | 软成员关系（soft membership） | HDBSCAN 概率向量语境，不等同 LDA 的生成式混合比例 |
| topic coherence / topic diversity | 主题连贯性（topic coherence）/ 主题多样性（topic diversity） | 连贯性与去重词占比不同；正文和词表的 c_v 定义差异仅列源风险 |
| NPMI | 归一化点互信息（NPMI） | 不把 PMI、NPMI、余弦相似度或其聚合相互替代 |
| outlier / noise label | 离群点 / 噪声标签 | 保留 -1 与过滤条件，簇不是计算集群 |
| manifold learning / dimensionality reduction | 流形学习 / 降维 | 保留局部结构的描述，不把 384 维向量或 ~5 维推广为所有模型固定参数 |
| NMF | 非负矩阵分解（NMF） | 非负约束与 LDA 的概率生成模型区分 |
| chunk and aggregate | 分块后聚合 | 长文档输入的处理步骤，不能将截断等同分块 |

BERTopic、BERT、Transformer、UMAP、HDBSCAN、Top2Vec、FASTopic、scikit-learn、gensim、20 Newsgroups、论文英文题名、模型 ID、API、代码与 SVG 原字节保护。普通 one/two/both/per-document 等数量关系按中文自然等值表达逐块记录，阿拉伯数字、负号与量纲保持。源择型或性能断言照源表达；不把未运行的生产库或数据集练习记为通过。
