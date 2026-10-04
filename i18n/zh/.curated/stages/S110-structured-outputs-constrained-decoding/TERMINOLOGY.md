# S110-structured-outputs-constrained-decoding 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Structured Outputs & Constrained Decoding。

本地check-only own3候选，未安装、未发布，不计课程完成。复用101 TERM上下文校准和已有独立语言审校；定向核对本课词义，不重扫全部历史词表。原common109为101 TERM+8 controls，own3另计、未来总112，不替换原支持身份。原提案表格数据行逐字保留。

| EN | 本课推荐呈现 | 依据与边界 |
|---|---|---|
| structured outputs | 结构化输出 | 本课标题；不是只保证 JSON 语法的 JSON 模式 |
| constrained decoding | 约束解码（constrained decoding） | 沿 S71；在生成步屏蔽不符合文法的 token，不等于验证内容事实 |
| contract | 契约 | 沿 S93/S96 软件约束语境；不是法律合同。S14 的形状约定是另一具体搭配 |
| LLM / prompt / API | 大语言模型（LLM）/ 提示词（prompt）/ API（应用程序编程接口） | 沿核心及 S101；首次解释，代码中不改 |
| token / vocabulary | token（词元）/ 词表 | 沿核心、S33/S60/S101；token 不等于单词或字符，toy 的一字一 token 不能外推 |
| logits | logits（未经归一化的分数） | 沿核心补充、S69/S88/S91；不是概率或对数概率 |
| logit processor | logits 处理器（logit processor） | 本课新增组合；保留英文单数名称，处理对象为 logits 向量 |
| masking | 屏蔽 | 本课表示将无效 token 的 logits 设为负无穷；不是图像分割区域，也不是删改词表 |
| sampling / sampler | 采样 / 采样器 | 沿 S18/S78 解码语境；训练数据抽样与音频采样不混用 |
| probability mass | 概率质量 | 沿 S09/S16；softmax 后的离散概率，不是 logits 本身 |
| schema / JSON Schema | schema（结构定义）/ JSON Schema | 沿核心；包含字段、类型和约束，不能只译“格式” |
| grammar / regex | 文法 / 正则表达式（regex） | 形式语言上下文；沿 S33 的 regex 译法 |
| finite-state machine / FSM | 有限状态机（finite-state machine，FSM） | 本课新增；O(1)、递归展平为源断言，未验证当前实现 |
| context-free grammar / CFG | 上下文无关文法（context-free grammar，CFG） | 本课 CFG 仅此含义，绝不套用 04-11 的 classifier-free guidance（无分类器引导） |
| accepting path / accept state | 通向接受状态的路径 / 接受状态 | 描述状态机可达性，输出不是状态；不声称任意递归文法都会终止 |
| recursive schema / flattening | 递归 schema / 展平 | 固定深度展开与真正递归区别；不在翻译中修订源库能力断言 |
| guided decoding | 引导解码（guided decoding） | 本课 vLLM 名称；与扩散图像引导术语按上下文区别 |
| validation / compliance rate | 校验 / 约束符合率 | 与训练用验证集不同；不替换为语义准确率 |
| semantic accuracy / semantic validity | 语义准确率 / 语义有效性 | 与 JSON 语法有效、schema 符合分开；本课正文与受保护输出技能分别出现 |
| reasoning / inference | 推理过程 / 推理 | 前者指答案前的过程字段，后者指模型推理服务；字段顺序强制建议仅忠实保留 |
| scaffolding | 固定结构片段 | 此处是必然出现的 JSON 字节，不能套核心项目目录“脚手架”定义 |
| retriever | 检索器 | 沿 S101；候选检索与受约束采样分工分开 |
| sentinel | 哨兵值 | 代表缺失/未知的特殊值，代码 null 原样 |
| enum / field order | 枚举 / 字段顺序 | 字段名与 API 标识符保护；不暗加 schema 保障 |
| open-weights model | 开放权重模型 | 不偷换成开源模型；模型 ID 保持 |
| F1 / latency | F1 分数 / 延迟 | 沿 S28/S36 与核心；源 F1=0.0/延迟断言未验证 |

## 沿用和消歧

CFG专指上下文无关文法，不与无分类器引导混用。token不是单词或字符，logits不是概率；文法约束、schema符合和答案正确分别说明。contract用软件契约，scaffolding在这里是固定结构片段；开放权重不改成开源。初次六处自审修订与随后两标题统一分别保留。

## 保护规则

核心及补充表优先。API、模型、专名、标识符、路径、URL、公式、数值及代码/图载荷保持；按本课语境说明首现，不将异义词机械统一。源内矛盾、宽泛或版本性断言另列SCOPE，不静默改写源技术含义，不把翻译/语言PASS当作运行或安全验证。

只依赖固定英文及术语起草，不要求先修中文正式验收；本表不包含旧中文正文或segments。支持候选、语言审校、真实GFM、运行和批次分别记录。
