# S122-dialogue-state-tracking 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；规范题名：Dialogue State Tracking。

本地支持候选，未安装或发布，不增加正式课程数。冻结 common127=119 TERM+8 controls；own3另计，未来总130。原18行术语提案及保护说明完整保留。原record只在两次正文修订后capture；不把final-body capture冒称首稿record。

| English | 本课呈现 | 语境与边界 |
|---|---|---|
| dialogue state tracking / DST | 对话状态追踪（Dialogue State Tracking，DST） | 多轮维护当前目标的结构化状态，不是生成对话回复 |
| slot / slot-value pair / slot-value dict | 槽位 / 槽位—值对 / 槽位—值字典 | 槽位沿 S104；键是具名参数，值是当前取值，整张字典是当前状态 |
| domain | 领域（domain） | 餐厅/酒店/出租车的任务领域及槽位集合，不是网络域名 |
| Joint Goal Accuracy / JGA | 联合目标准确率（Joint Goal Accuracy，JGA） | 按轮全槽位完全匹配；不等于单槽位平均准确率或对话终态匹配率 |
| closed-vocab / open-vocab | 封闭词表 / 开放词表 | 可枚举候选与开放文本值的差别；不改变源对应用范围的判断 |
| free-form / closed-set | 自由形式 / 封闭集合 | 槽值集合性质，不套嵌入空间的开闭集合数学意义 |
| ontology-free | 无本体（Ontology-free） | 沿 S55/S74 本体译法；本课说明为不使用固定 schema/槽位列表 |
| correction / overwrite / append | 更正 / 覆盖 / 追加 | 区分修改既有值与增加另一个值；不宣称 toy 实现了完整更正策略 |
| explicit negation / implicit confirmation | 明确否定 / 隐式确认 | 源对清空和接受预订的讨论，不隐含实际业务授权 |
| coreference resolution | 共指消解（coreference resolution） | 沿 S65；跨轮或指向系统之前话语，不混同实体链接 |
| full-history regeneration | 基于完整历史重新生成 | 与增量更新不同；本课源建议和成本断言保留 |
| schema / structured output / constrained decoding | schema（结构定义）/ 结构化输出 / 约束解码（constrained decoding） | 沿核心/S110，结构有效不等于语义正确 |
| pipeline / extractor / normalizer | 管线 / 抽取器 / 规范化器 | 沿 NLP 语境；图中和代码内标识符不翻译 |
| guardrail / agent / prompt | 安全护栏（guardrail）/ 智能体（agent）/ 提示词（prompt） | 沿核心词表，首现保留英文解释 |
| LLM / API / token | 大语言模型（LLM）/ API（应用程序编程接口）/ token（词元） | 沿核心；token 不是固定单词或字符 |
| LoRA / ASR / EM / TOD | LoRA（低秩适配）/ 自动语音识别（ASR）/ EM（期望最大化）/ 面向任务对话（TOD） | LoRA、ASR 沿核心/S30；EM/TOD 文末释义，不更名方法 |
| named parameter / names | 具名参数 / 名称 | names 涵盖餐厅名称，不能收窄为个人姓名 |
| labeled data / no labels | 有标注数据 / 无标注 | labels 为监督标注，不是 HTML 标签 |

保留：TripPy、BERT-DST、LDST、LLaMA、LoRA、BERT、ChatGPT、MultiWOZ、Instructor、Pydantic、Python、JSON、API、LLM、DST、JGA、ASR、EM、TOD；所有字段/取值例子、公式 O(n²)、数字、7 pm、路径、引用题名、URL、figure/SVG 与代码载荷。普通中文章节沿 addendum；标题采用“对话状态追踪”。

## 沿用和保护

核心与补充表优先，固定英文和相关术语足以起稿，先修中文正式验收不是额外门槛。保留代码、API、路径、URL、数字、数学与图载荷。源风险见SCOPE，语言PASS不等于运行、呈现、回归或发布通过。
