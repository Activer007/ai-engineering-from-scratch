# S116-llm-evaluation-frameworks 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；规范题名：LLM Evaluation — RAGAS, DeepEval, G-Eval。

本地check-only own3候选，未安装、未发布、不增加正式课程数。复用既有107 TERM校准与当前独立技术/中文审校；common115=107 TERM+8 controls，own3另计，未来总118。原术语提案表格行逐字保留，外围作者工作说明不发布。

| English | 本课用法 | 语境 |
|---|---|---|
| LLM-as-judge | 以大语言模型为评判者（LLM-as-judge） | 沿S95/S101；非人工判断本身 |
| faithfulness | 忠实度（faithfulness） | 沿S101，答案断言受检索上下文支持的比例 |
| answer relevance | 答案相关性 | 沿S101，回应原问题的程度 |
| context precision / context recall | 上下文精确率 / 上下文召回率 | 沿S101，相关块比例 / 标准答案信息覆盖 |
| rubric | 评分细则（rubric） | 对输出进行评判的明确标准 |
| atomic claims | 原子断言（atomic claims） | 拆解后的简单事实断言 |
| judge bias / positional bias | 评判者偏差 / 位置偏差 | 评判偏好，不是神经网络偏置；社会bias指标译偏见 |
| calibration / Spearman rho | 校准（calibration）/ Spearman秩相关系数rho | 本课评判与人工评分相关性，不是概率校准 |
| reference-free | 无参考 | 无标准参考答案，不表示无检索上下文 |
| CI gate | CI门禁 | 沿补充表CI/CD门禁，不是RNN门 |
| golden dataset rot | 标准评估集退化 | 无版本评估集随时间漂移，破坏纵向比较 |
| bottom quantile | 得分最低的分位区间；低分位区间 | 按评分排序的尾部，不等同均值 |
| regression | 质量退步；回归测试中的退步 | 沿S95/S102，与统计预测任务分开 |

## 沿用和保护

核心及补充表优先，只按本课语境使用术语；保留代码、专名、API、模型ID、路径、URL、公式、数字和图载荷。英文没有的内容不补造，源矛盾或宽泛主张在SCOPE单列，不静默改写技术含义。通用标题沿既有九项约定，不据此补造源文缺失章节。

固定英文与术语足以起稿，先修中文正式验收不是门禁。语言审校、真实GFM、运行、远端回读和批次回归分别记录；本候选不把翻译PASS当作运行或安全验证。
