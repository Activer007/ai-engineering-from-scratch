# S117-runtime-feedback-loops 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；规范题名：Runtime Feedback Loops。

本地check-only own3候选，未安装、未发布、不增加正式课程数。复用既有107 TERM校准与当前独立技术/中文审校；common115=107 TERM+8 controls，own3另计，未来总118。原术语提案表格行逐字保留，外围作者工作说明不发布。

| 英文 | 本稿用法 | 语境 |
|---|---|---|
| runtime feedback loop | 运行时反馈循环 | 下一轮依赖真实命令反馈，不是遥测跨运行汇总 |
| feedback runner | 反馈运行器（feedback runner） | 对命令执行作薄封装，产生结构化记录 |
| feedback record | 反馈记录 | command/output/exit/duration的JSONL条目 |
| agent / agent loop | 智能体（agent）/ 智能体循环 | 沿核心表及S104 |
| stdout / stderr | 标准输出 stdout / 标准错误 stderr | 沿S02；标识符不译 |
| shell | Shell（命令解释器） | 沿S01/S02；argv参数列表不误作Shell字符串 |
| telemetry | 遥测（telemetry） | 沿S99，供人跨时段审查 |
| wall-clock duration | 墙钟耗时（wall-clock duration，即实际经过的时间） | 区分语言运行时与耗时；不暗示计时器单调性 |
| verification gate | 验证关卡（verification gate） | 任务末尾读取记录，非运行器自动成功断言；用词沿 S111 工程检查语境（[固定术语表](https://github.com/Activer007/ai-engineering-from-scratch/blob/16c5ca8c98db36d73e0c81cb4cf995867ec84862/i18n/zh/.curated/stages/S111-delegate-with-isolation/TERMINOLOGY.md)） |
| deterministic truncation / tail truncation | 确定性截断 / 尾部截断 | 头部+尾部保留；保留源“相同记录”断言并另列边界 |
| redaction | 脱敏（redaction） | 沿补充表；输出脱敏不等于整个record保护 |
| rotation policy | 轮转策略 | 保留1 MB、.1/.2/.5；源实现限制另列 |
| parent-command id / retry chain | 父命令 ID / 重试链 | 指向前一次尝试，不是调用栈 |
| Refuse-on-null | 空值即拒绝 | 缺反馈不推进；不推定非零exit为成功 |
| Agent note | 智能体备注 | 读结果前的一行预期 |
| Telemetry split | 遥测分离 | 下一轮反馈与运维遥测分开 |
| workbench / fixture | 工作台（workbench）/ 测试样例（fixture） | 沿核心/补充表、S102 |
| JSONL / TUI / PII | JSONL（每行一个 JSON 对象的格式）/ TUI（终端用户界面）/ PII（个人身份信息） | 保留缩写，首次出现补中文说明 |

## 沿用和保护

核心及补充表优先，只按本课语境使用术语；保留代码、专名、API、模型ID、路径、URL、公式、数字和图载荷。英文没有的内容不补造，源矛盾或宽泛主张在SCOPE单列，不静默改写技术含义。通用标题沿既有九项约定，不据此补造源文缺失章节。

固定英文与术语足以起稿，先修中文正式验收不是门禁。语言审校、真实GFM、运行、远端回读和批次回归分别记录；本候选不把翻译PASS当作运行或安全验证。
