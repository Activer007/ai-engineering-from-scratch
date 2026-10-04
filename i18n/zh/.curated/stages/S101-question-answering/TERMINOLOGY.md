# S101-question-answering 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Question Answering Systems。

本地 check-only own3 候选，未安装或发布。复用作者 95 TERM 固定校准及当前独立语言审核，定向核对相关词义，不声称本轮重读全部历史词表。以下作者提案数据行逐字保留；不要求改动当前正文或旧术语表。原 common103 = 95 TERM + 8 controls；own3 另计，未来总支持106，不把后来新增 common106 套入作者首次输入。

| English | 中文呈现 | 语境与既有对齐 |
|---|---|---|
| Question Answering / QA | 问答（QA） | 沿 S65；标题为问答系统 |
| extractive QA | 抽取式问答（Extractive QA） | 从给定文本定位答案；与生成答案区别 |
| open-domain QA | 开放域问答（Open-domain QA） | 没有给定段落，先检索再作答 |
| generative / closed-book QA | 生成式 / 闭卷问答 | 闭卷为不检索、依参数记忆作答；不是把全部生成式 RAG 归为闭卷 |
| answer span | 答案所在的文本跨度（span，即答案片段） | span 沿 S55/S65 的连续文本区间；后文以答案片段指称，非线性代数的张成 |
| parametric memory | 存储在参数中的记忆 | 模型权重所承载的知识，不是另接记忆数据库或统计参数检验 |
| retrieval-augmented generation / RAG | 检索增强生成（RAG） | 沿 S55/S59/S64；源亦将抽取阅读器列入其管线，不静默改架构范围 |
| retriever / reader | 检索器 / 阅读器 | 找相关段落 / 根据段落抽取或生成答案，二者分工不得互换 |
| dense / hybrid retrieval | 稠密 / 混合检索 | 沿 S59/S64；稠密指向量表示，混合与 BM25 组合 |
| reranker / RRF | 重排序器 / 倒数排名融合（RRF） | 沿 S59/S64；排序与排名融合不混为重新检索 |
| pipeline | 管线 | 沿 S57/S59/S72/S95；不是流水线并行 |
| null answer / null score | 空答案 / 空答案分数 | SQuAD 2.0 无答案输出；需保留默认与显式开关的条件区别 |
| Exact Match / EM | 完全匹配（Exact Match，EM） | 不是 S31 期望最大化算法；QA 答案规范化后的严格匹配 |
| token-level F1 | token 级 F1 | 沿 S55；保留 token 粒度，不混实体级 F1 |
| normalization | 规范化 | 本课答案字符串转小写、去标点和冠词；不同于数值归一化、mean/std 标准化；沿 S33 的文本语境 |
| citation accuracy | 引文准确率 | 引用段落支持答案的指标；源将字符串匹配等同支持检查的过强说法单列 |
| refusal calibration | 拒答校准 | 无足够依据时正确说不知道，不是所有拒答都正确 |
| retrieval recall | 检索召回率 | 正确段落是否进入前 k；precision/recall/accuracy 沿 S28/S39/S94 |
| faithfulness | 忠实度（faithfulness） | 答案断言是否由检索上下文支持；与 S95 机器翻译 adequacy 的具体对象不同 |
| answer relevance | 答案相关性 | 答案是否回应问题，保留假想问题评估说明 |
| context precision / context recall | 上下文精确率 / 上下文召回率 | 相关块比例 / 所需信息覆盖；精确率不是数值精度 |
| NLI / entailment | 自然语言推断（NLI）/ 蕴含关系 | 源 RAGAS 忠实度说明，不宣称已实测 |
| reference-free scoring | 无参考评分 | 沿 S95；reference 是参考答案，不是参考译文，也不等于无上下文 |
| LLM-as-judge | 以大语言模型为评判者（LLM-as-judge） | 沿 S95；与人工评判分开 |
| hallucination | 幻觉（hallucination） | 沿 S74/S95；本课以输出未获检索上下文支持解释 |
| prompt / token / LLM | 提示词（prompt）/ token（词元）/ 大语言模型（LLM） | 沿核心首现规则，后文沿用简写 |

## 沿用和消歧

normalization 在本课是答案字符串规范化（小写化、去标点、去冠词），沿 S33 文本语境，区别数值归一化或均值/标准差标准化。answer span 是连续文本跨度，首次解释答案片段，沿 S55/S65，后文可用答案片段；不是线性代数的张成。

抽取式/生成式区分答案形式，开放域区分是否先检索；生成式 RAG 不自动等同于闭卷。EM 在本课为完全匹配，非期望最大化。faithfulness 指答案受检索上下文支持，与 S95 译文充分性及其他任务同词的对象不同，不强制机械替词；无参考评分不等于无上下文。引文的字符串存在性与蕴含支持性分开，源强断言不因译文忠实而变成已验证结论。

## 保护规则

核心及补充表优先，通用章节沿既有规范，英文没有的章节不补造。API、模型、专名、标识符、路径、URL、公式、数值、代码与图载荷保持；首次正文按本课语境中英对应，不把同词跨任务机械统一。源内矛盾、宽泛或版本性断言单列，不静默修正英文含义、数学或代码。

词表用于一致性，不复用旧中文课文/segments；规范自带质量示例仅附带曝光且未复用。起草只依赖固定英文与术语，不等待先修中文正式验收。支持候选、语言 PASS、课程运行、GFM与正式计数分别记录。
