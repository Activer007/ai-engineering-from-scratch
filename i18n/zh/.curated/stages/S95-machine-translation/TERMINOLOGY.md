# S95-machine-translation 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Machine Translation。

这是完整固定92份词表校准后的本地check-only候选，尚未安装或发布，不构成中文审校或正式接受。原术语提案无需强制改词；以下词义只用于本课语境。正式基线107；87正式TERM=85 accepted stage+core2，active-reviewed5=S88/S89/S91/S92/S93，总92；8原controls另计，100common+本课own3=103。S95原样SVG另计。原支持日期、旧状态叙述与字节保留，不据此否定S90现已正式接受。

| English | 推荐中文 | 首现、语境与边界 |
|---|---|---|
| Machine Translation / MT | 机器翻译 / 机器翻译（MT） | 源 H1，无额外副标题；MT 在正文首次解释 |
| NMT | 神经机器翻译 | 源关键术语表定义；不是所有神经翻译系统均经本任务验证 |
| reference translation / reference | 参考译文 | 评估参照文本，不是论文引用或模型输入原文 |
| hypothesis / candidate translation | 候选译文 | 供评估的模型输出，不用统计学“假设”；代码变量和围栏保持英文 |
| clipped n-gram precision | 截断计数后的连续 n 元片段精确率 | main.py 对候选计数按参考计数封顶；正文没有细化处不增补算法 |
| brevity penalty | 简短惩罚（brevity penalty） | BLEU 对过短候选译文的惩罚，区别模型生成参数 length_penalty 的长度惩罚 |
| chrF / character-level F-score | chrF / 字符级 F 分数 | 教学实现不是 sacrebleu 等价性保证；字符与 token 不混同 |
| heuristic / learned metrics | 启发式指标 / 学习型指标 | 三类评估家族；训练与关联性概括按源保留，事实疑问单列 |
| reference-free evaluation / scoring | 无参考评估 / 无参考评分 | 无参考译文；不表示无原文，也不授权编造 BLEU 或 chrF 实测分数 |
| LLM-as-judge | 以大语言模型为评判者（LLM-as-judge） | 依提示词评估；与独立人工评判不同 |
| adequacy / fluency | 忠实度 / 流畅度 | 是否传达原文与表达是否通顺分开，流畅不等于准确 |
| hallucination | 幻觉（hallucination） | 原文没有依据的新增内容，沿 S74 的幻觉率语境 |
| off-target generation | 目标语言偏离（off-target generation） | 生成了错误语言；不是偏题、丢失实体或句长不足 |
| terminology drift | 术语漂移（terminology drift） | 同一术语在不同文档中译法不一致；不等于分词器漂移 |
| register / formality | 语体 / 正式程度 | 源围栏中的 register 保持原字节；正文按正式程度语境表述，不译为注册 |
| formality mismatch | 正式程度不匹配（formality mismatch） | 法语 tu/vous、日语礼貌程度；模型多数形式不保证适用 |
| language-ID check | 语言识别检查 | 验证输出语言；不是身份证明或准确性总体验收 |
| detokenize / detruecase | 反分词 / 还原大小写 | 将子词输出还原为文本并处理大小写，不解释成恢复 token 编号 |
| length explosion | 长度暴增 | 过长译文；保留源 ~5 token 概括的风险，不发明运行结果 |
| regression detection | 检测质量退步 | 回归测试式质量退化，不是回归预测模型 |
| estimated score / measured score | 估算分数 / 实测分数 | 两者不能混写；交付提示词原文是预计范围，不是已运行指标 |

## 沿用和消歧

沿用：attention / cross-attention→注意力 / 交叉注意力；encoder / decoder→编码器 / 解码器；subword tokenization / tokenizer / token→子词分词 / 分词器（tokenizer）/ token（词元）；n-gram→连续n元片段；beam search / beam width / greedy decoding→束搜索 / 束宽 / 贪心解码；parallel corpus→平行语料库；constrained decoding→约束解码；fine-tuning→微调；pipeline→管线。brevity penalty为简短惩罚，与生成参数length_penalty的长度惩罚分开；hypothesis为候选译文而非统计假设，regression detection为检测质量退步而非回归预测。

## 保护规则

核心及补充表优先，首次正文说明中英对应，API、模型ID、语言代码、公式、数值单位、路径、链接、代码与图载荷保持。九个通用章节沿补充表，英文无的章节不补造。自然语言数量变化必须等值逐块记录。源技术疑问单列，不能静默改写。

参考词表只用于术语一致性，未复用旧中文课程正文/segments/format_revisions。必要阅读docs/i18n.md已暴露其中既有中文质量示例；未引用或复用该示例措辞。支持、作者草稿及局部测试均不增加正式完成数。

publication pending/null只记录冻结时尚未绑定发布提交；冻结后不自指当前文件commit。实际发布须由后续record/外部远端回读绑定，不能删除历史或编造SHA。
