# S107-multilingual-nlp 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Multilingual NLP。

本地 check-only own3 候选，未安装、未发布，不计课程完成。复用作者101 TERM校准和当前独立语言审校；定向核对本课词义，不重扫全部历史词表。原common109为101 TERM+8 controls，own3另计、未来总112，不替换原支持身份。作者提案JSON数据值逐值保留，不要求修改正文或旧词表。

| English | 本课呈现 | 语义边界（原提案） |
|---|---|---|
| multilingual NLP | 多语言自然语言处理（NLP） |  |
| cross-lingual transfer | 跨语言迁移（cross-lingual transfer） |  |
| high-resource / low-resource language | 高资源语言 / 低资源语言 |  |
| typologically related | 语言类型学上相近 |  |
| genetic relatedness | 语言谱系上的亲缘关系 |  |
| fertility tax | 平均每词 token 数偏高带来的代价 |  |
| variant recovery tax | 识别变体的代价 |  |
| capacity spillover tax | 模型容量被挤占的代价 |  |
| byte-level fallback | 字节级回退 |  |
| script | 文字系统 |  |
| few-shot fine-tuning | 少样本微调；目标语言带标签样本用于训练，非 in-context 示例 |  |

## 沿用和消歧

source language是迁移所用语言，不是翻译源文件；typological similarity、语言谱系亲缘和语料规模不能混同。fertility是平均每词token数，script是文字系统，tax是额外代价。few-shot是带标签微调；零样本缺少训练标签不等于无需评估标签。95-98%相对于英语基线，M/k/B分别保留百万/千/十亿量级。NLI/蕴含、Unicode规范化与recall@5沿正文释义。真实修订移除了good predictions被增强为明确准确率承诺的措辞，并澄清104/100统计支持语言数量；没有改变源数值。

## 保护规则

核心及补充表优先。API、模型、专名、标识符、路径、URL、公式、数值及代码/图载荷保持；按本课语境说明首现，不将异义词机械统一。源内矛盾、宽泛或版本性断言另列SCOPE，不静默改写源技术含义，不把翻译/语言PASS当作运行或安全验证。

只依赖固定英文及术语起草，不要求先修中文正式验收；本表不包含旧中文正文或segments。支持候选、语言审校、真实GFM、运行和批次分别记录。
