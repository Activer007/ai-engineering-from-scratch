# S98-text-summarization 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Text Summarization。

本地 check-only 候选，未安装或发布。复用作者固定95 TERM校准，定向复核相关条目与英文；不声称重新全文审查全部旧历史。以下保留作者提案，不要求强制改词，不改既有术语。103 common = 95 TERM + 8 controls；本课own3独立另计，总支持106。S98原样SVG是额外非支持资产。词表数不是正式课程数。

| English | Proposed Chinese | Actual context / constraint | Source blocks |
|---|---|---|---|
| text summarization / summary | 文本摘要 / 摘要 | 文档压缩任务与其结果；区别密码学 digest 和统计 sketch | b0001, b0009 |
| extractive summarization / extractive | 抽取式摘要 / 抽取式 | 选取原文句子；不把方式名称解释成绝对安全保证 | b0009, b0021, b0091 |
| abstractive summarization / abstractive | 生成式摘要 / 生成式 | 以输入文档为条件生成新文本；不是抽象代数的抽象 | b0009, b0023, b0091 |
| sentence ranking | 句子排序 | 按分数取前 k 句；rank 与矩阵秩分开 | b0011, b0021 |
| sentence similarity graph | 句子相似度图 | 句子为节点，相似度为边；PageRank/TextRank 专名保留 | b0021, b0091 |
| log-normalized word overlap | 对数归一化的词重叠程度 | 本地实现的实际计数/分母语义另外记录，不改其算法 | b0035 |
| damping factor | 阻尼系数 | 沿 S76 阻尼；0.85 原样，不同于学习率或动量 | b0035 |
| gap-sentence pretraining objective | 缺失句预训练目标 | Pegasus 的目标，首次保留英文；不自行加入源未解释的句子选择或重建步骤 | b0023 |
| ROUGE | ROUGE（面向召回的摘要评估指标） | 保留 Recall-Oriented Understudy for Gisting Evaluation 全称；中文为作用说明，并非另造官方全称 | b0025 |
| longest common subsequence / LCS | 最长公共子序列 / LCS | 子序列不同于连续子串；ROUGE-L名称保持 | b0025, b0091 |
| factuality | 事实性 | 本课明示口径是摘要陈述得到原文支持，不能升级为独立验证现实世界真值 | b0055, b0067, b0091 |
| faithfulness | 忠实性 | 相对原文的忠实程度；与 S95 adequacy 的忠实度保持各自语境 | b0053 |
| entailment | 蕴含关系 | source sentence→summary sentence的支持关系，不泛译相关性 | b0067 |
| entity swap | 实体错换 | John Smith→John Brown 的事实错误；技能模板的遗漏方向探针另列源风险 | b0063; protected b0083 |
| number drift | 数字漂移 | 25,000→25 million 的数字/量级变化；million保留并解释 | b0063 |
| polarity flip | 极性反转 | “拒绝”→“接受”的陈述含义反转；不能只译成情感极性 | b0063 |
| fact invention | 编造事实 | 原文无CEO，摘要却增添其批准；与单纯措辞改写分开 | b0063 |
| factuality gate | 事实性检查关卡 | 当前仅见受保护技能围栏，正文未自行添加译句；此行供协调者术语准备 | protected b0083 |
| chunked map-reduce summarization | 分块映射—归约摘要 | 当前仅见受保护技能围栏；并非只截断输入。没有在正文另加新解释 | protected b0083 |

## 沿用和消歧

沿用词干提取、精确率/召回率、阻尼、交叉注意力、token（词元）、幻觉与流畅度。summary 不套密码学 digest；factuality 为原文支持的事实性，faithfulness 为相对原文的忠实性，S95 adequacy 的忠实度按语境区分。longest common subsequence 不是连续子串；ROUGE召回率与库F-measure分开。

## 保护规则

核心及补充表优先，首次正文遵守中英对应；API、模型ID、标识符、路径、链接、数值、公式、代码与图载荷保持。通用章节沿补充表，英文没有的章节不补造。自然语言数量等值且不跨源块移动。源问题另列，不静默改数学、代码或技术含义。

词表仅用于一致性，不复用旧中文课文/segments；规范中文质量示例仅附带曝光，未引用其措辞。新译只依赖固定英文与术语，不等待先修中文正式验收。publication pending/null仅表示本次冻结未绑定发布提交；后续真实提交由外部记录和独立回读绑定，不自引用。
