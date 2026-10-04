# S113-nli-textual-entailment 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；规范题名：Natural Language Inference — Textual Entailment。

本地check-only own3候选，未安装、未发布，不计课程完成。复用107 TERM上下文校准和已有独立技术/中文审校；不重扫全部历史词表。common115=107 TERM+8 controls，own3另计，未来总118。原提案表格数据行逐字保留。

| English | 本课译法 | 对齐与语境 |
|---|---|---|
| Natural Language Inference / NLI | 自然语言推断（Natural Language Inference，NLI） | 沿 S101；区别模型运行阶段的“推理” |
| textual entailment / entailment | 文本蕴含 / 蕴含关系 | 沿 S98/S101；前提支持假设，不是一般相关性 |
| premise / hypothesis | 前提 / 假设 | 文本对的方向不交换；hypothesis 不是 S95 的候选译文 |
| contradiction / neutral | 矛盾 / 中立 | 中立表示不能推出真或假；源 unrelated 简化单列 |
| logical entailment / first-order logic | 逻辑蕴含 / 一阶逻辑 | 保留与自然语言读者推断的区分 |
| grounded QA | 有依据的问答（QA） | 沿 S101 的依据与检索上下文语境 |
| zero-shot classification | 零样本分类（zero-shot classification） | 沿 S51/S55；不暗示微调或训练发生 |
| verbalized label | 用自然语言表述的标签 | 标签转成假设句，不是改变标签集合 |
| hallucination | 幻觉（hallucination） | 沿 S74/S95/S101；源将非蕴含等同幻觉的强断言单列 |
| faithfulness | 忠实度（faithfulness） | 采用直接先修 S101 的答案/检索上下文语境；S98“忠实性”不机械覆盖 |
| atomic claim | 原子断言 | 答案拆分后的逐项陈述，不等同整段答案 |
| RAG | 检索增强生成（RAG） | 沿 S55/S64/S70/S101 |
| pipeline | 管线（pipeline） | 沿 S57/S72/S101；不译“流水线” |
| transformer encoder | Transformer 编码器 | 架构/API/模型名保持；源统一编码序列简化单列 |
| softmax / cross-entropy | softmax / 交叉熵（cross-entropy） | 沿 S09/S12/S28/S40；概念损失不等于玩具代码已计算 |
| lexical overlap / negation detection | 词汇重叠程度 / 否定检测 | 沿 S44/S51；玩具代码无否定作用域或语义推断保证 |
| subsequence heuristic | 子序列启发式 | 子序列不是连续子串；源对基准的概括不暗改 |
| hypothesis-only shortcut / baseline | 只看假设的捷径 / 基线 | 预测时不看前提，不能译为“仅有一个假设” |
| label leakage | 标签泄漏 | 假设中的标注线索与目标标签的相关性 |
| held-out / in-distribution | 留出 / 分布内 | 沿 S39/S50；不混训练与测试 |
| accuracy / F1 | 准确率 / F1 | 沿 S28/S39/S51；20+、10+保留“点”，不改百分比 |
| threshold / calibration | 阈值 / 校准 | 沿 S28/S68；源0.5与严格大于代码保持 |
| document-level / document-length | 文档级 / 文档长度 | 任务粒度与输入长度区分；模型支持范围未验证 |
| domain mismatch / adversarial | 领域不匹配 / 对抗性 | 特定领域、长度和基准概括均未外部验证 |
| false-positive / false-negative rate | 假阳性率 / 假阴性率 | 沿 S67 的分类指标语境；不交换两者 |
| gold context | 金标准上下文 | 评估参考上下文，不是随意标准化输入 |

## 沿用和消歧

推断指NLI关系判断，模型运行语境的推理另论；前提到假设的方向保持，hypothesis不套机器翻译候选译文。忠实度沿直接先修答案/检索上下文语境；中立不推出真或假，非蕴含不被本表升级为现实虚假保证。实验英文输入保留并附中文说明；20+ F1与t/h块内自然中文重排由独审按块内多重集核过，不是符号/角色漂移。

## 保护规则

核心及补充表优先。首次出现按本课语境说明，专名、API、模型ID、标识符、路径、URL、公式、数值及代码/图载荷保持；英文没有的章节不补造。源内矛盾、宽泛或版本性断言另列SCOPE，不静默改写技术含义，不把翻译PASS当作运行或安全验证。

只依赖固定英文和术语起草；先修中文正式验收不是门禁。既有政策内质量示例曾附带出现，已披露且未复用；未使用旧中文课程正文、segments或作者记录。语言审校、真实GFM、运行和批次分别记录。
