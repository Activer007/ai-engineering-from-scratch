# S119-long-context-evaluation 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；规范题名：Long-Context Evaluation — NIAH, RULER, LongBench, MRCR。

本地check-only own3候选，未安装、未发布、不增加正式课程数。common121=113 TERM+8 controls，own3另计，未来总124。没有单独术语提案或校准文件；忠实整理原HANDOFF的8条terminology_proposals及START的113表身份/适用行校准说明，未补造作者文件或校准时间。

| English | 本课译法 | 语境与依据 |
|---|---|---|
| Needle-in-a-Haystack / NIAH | 大海捞针（Needle-in-a-Haystack，NIAH） | A planted fact at controlled depth; needle subsequently 针/找针, filler 填充文本, haystack 草堆文本. Fixed05-28 b0021; no existing equivalent term row found in113 calibrated files. |
| RULER / LongBench v2 / MRCR / NoLiMa / HELMET / BABILong | Names retained; MRCR explained 多轮共指消解 | Benchmark names, not translated brands; variants8-needle/24-needle/100-needle retained and explained. Fixed05-28 b0023–b0033; core no-force-translation and S65共指消解. |
| effective retrieval length / effective reasoning length | 有效检索长度 / 有效推理长度 | Task-specific threshold-qualified context length; distinct from advertised maximum. Fixed05-28 b0037–b0039; S45上下文窗口. |
| lost in the middle / depth bias | 中间信息丢失 / 深度偏差 | Insufficient attention to the middle of long inputs; no claim of deleting tokens. Fixed05-28 b0073/b0095. |
| multi-needle / multi-hop tracing / aggregation | 多针 / 多跳追踪 / 聚合 | Simultaneous planted facts versus chaining assignments versus aggregating information. Fixed05-28; S70多跳, S56聚合. |
| non-lexical needle | 非词面匹配的针 | No literal overlap between needle and query; keep separate from filler-overlap pitfall. Fixed05-28 b0029/b0095. |
| long in-context learning | 长上下文学习（in-context learning） | LongBench task category, not training a model to accept longer context. Fixed05-28 b0025 and S38上下文学习 concept. |
| prefill / time-to-first-token / accuracy / regression | 预填充 / 首 token 延迟 / 准确率 / 回归测试 | Performance phases/metric semantics; regression here checks model upgrades. Core token/latency, S45 prefill, S28/S39 accuracy, S95/S102 regression context. |

## 沿用和保护

固定英文与术语足以起稿，先修中文正式验收不是门禁。核心和补充表优先；代码、数字、数学、API、路径、URL和图载荷受保护，源问题见SCOPE。术语校准、自审、独审、真实GFM、远端回读和批次回归分别记录，未把作者自审或旧批次PASS提升为当前课程验收。
