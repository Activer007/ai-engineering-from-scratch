# S114-turn-feedback-into-system 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；规范题名：Turn Every Agent Correction into a System Improvement。

本地check-only own3候选，未安装、未发布，不计课程完成。复用107 TERM上下文校准和已有独立技术/中文审校；不重扫全部历史词表。common115=107 TERM+8 controls，own3另计，未来总118。原提案表格数据行逐字保留。

| English | 本稿用语 | 语境与边界 |
|---|---|---|
| agent | 智能体（agent） | 沿核心表；首个正文出现说明 |
| correction | 纠正 | 对智能体行为或结果的纠正，不是泛指拼写校对 |
| control / durable control | 控制措施 / 持久控制措施（durable controls） | 沿 S102；测试、边界、示例和工具等措施，不只指提示词 |
| promote / promotion | 转化为、固化为控制措施 | 系统改进语境；不是升职、促销或模型升版 |
| earliest effective layer | 最早能奏效的层 | 系统中最早能够防止复发的责任层，不套镜像层或神经网络层 |
| scope boundary | 工作范围边界（scope boundary） | 缺少可执行约束；并非抽象边界作为程序对象“执行” |
| regression | 质量退步（regression） | 沿 S102；软件回归语境，不是连续量预测 |
| canonical example | 标准示例 | 用于约束输出格式；不同于 Unicode 规范分解 |
| fingerprint | 指纹（fingerprints） | 用于稳定标识和去重；不声称任意语义等价识别或不存在碰撞 |
| feedback ratchet | 反馈棘轮 | 沿 S102；将反馈固化为后续系统改进的机制 |
| symptom / root cause | 问题表现（symptom）/ 根本原因（root cause） | 区分可观察现象与背后原因；不将推测写成已验证根因 |
| recurrence / recurrence count | 复发 / 复发次数（recurrence count） | 沿 S102；故障再现，不是 RNN 循环机制 |
| ownership / owner | 责任归属 / 负责方（owner） | 沿 S99/S102；可由个人、团队或相应责任主体承担，不是文件所有权 |
| retirement / retirement check | 停用 / 停用检查（retirement check） | 沿 S102；源要求复查/停用日期，不代表程序实现自动到期或删除 |
| normalization | 规范化处理（normalization） | 沿 S101 文本语境；原因字符串措辞处理，不是数值归一化 |
| output shape / output format | 输出格式 | 沿 S105；不是张量形状；实验 JSON 仍称输出 |
| friction | 阻力（friction） | 沿 S84；工作阻碍，不是物理摩擦力 |
| workbench | 工作台（workbench） | 沿核心与 S102 |

## 沿用和消歧

控制措施、反馈棘轮、质量退步、复发、负责方与停用沿相关固定词表；持久控制不是只写一段提示词。规范化是原因字符串处理，非数值归一化；指纹不证明任意语义等价或无碰撞。工作范围边界缺少的是可执行约束，不是抽象边界本身不能作为程序对象运行。

## 保护规则

核心及补充表优先。首次出现按本课语境说明，专名、API、模型ID、标识符、路径、URL、公式、数值及代码/图载荷保持；英文没有的章节不补造。源内矛盾、宽泛或版本性断言另列SCOPE，不静默改写技术含义，不把翻译PASS当作运行或安全验证。

只依赖固定英文和术语起草；先修中文正式验收不是门禁。既有政策内质量示例曾附带出现，已披露且未复用；未使用旧中文课程正文、segments或作者记录。语言审校、真实GFM、运行和批次分别记录。
