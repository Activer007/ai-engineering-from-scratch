# S105-frame-task-before-code 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Frame the Task Before the Agent Writes Code。

本地 check-only own3 候选，未安装、未发布，不计课程完成。复用作者98 TERM校准和当前独立语言审校；定向核对本课词义，不重扫全部历史词表。原common106为98 TERM+8 controls，own3另计、未来总109，不套早期common103或后续common109。作者提案表格数据行逐字保留，不要求修改正文或旧词表。

| English | Chinese used | Context / boundary |
|---|---|---|
| coding agent | 编程智能体（coding agent） | 沿核心 agent→智能体，不作网络代理解释 |
| task frame | 任务框架（task frame） | 用六个字段界定目标、事实、范围、验收和未知问题的任务说明，不是运行框架，也不是音频帧 |
| repository facts | 仓库事实（repository facts） | 在代码、测试、配置或历史中核实的事实，不把合理假设视作已验证事实 |
| assumption | 假设（assumption） | 沿S87；不把示例字符串当真实证据 |
| allowed paths / forbidden paths | 允许修改的路径 / 禁止修改的路径 | 首次正文保留英文；代码和glob字面量原样；教学实现仅检查完全相同的字符串 |
| acceptance evidence | 验收证据（acceptance evidence） | 具体命令或观察所支持的任务完成主张，不等于笼统的“测试通过” |
| reconnaissance | 前期摸查（reconnaissance） | 开始修改前寻找会约束变更的仓库证据，不要求通读整个仓库 |
| domain service | 领域服务（domain service） | 与API及数据库并列的实现职责位置 |
| receipt / scope receipt | 凭据（receipt）/ 范围检查凭据 | 与S93验证凭据一致，表示可检查记录，不是支付收据 |
| public contract / public compatibility | 对外契约（public contract）/ 对外兼容性（public compatibility） | 沿S93对外行为，不是公共资产的所有权 |
| serialized shape / error shape | 序列化格式 / 错误响应格式 | 这里shape不是张量形状 |
| unknowns | 未知问题（unknowns） | 沿S99；信息空白与擅自填入的假设分开 |
| Discoverable / Decidable / Human / Deferred | 可查明 / 可自行决定 / 需人工决定 / 暂缓处理 | 分类首现完整保留原英文；可自行决定仍以任务授权为前提 |
| authority / delegated | 权限或授权 / 已获授权决定 | 沿S84/S87/S90/S93；此处不是证据权威性 |
| proof | 验证证据（proof） | 沿S93；本节先规划所需证据，不能声称已经运行成功 |
| browser journey | 浏览器中的用户旅程（browser journey） | 沿S93；明确视口和预期状态，不改成单元测试 |
| wire request | 实际传输的请求（wire request） | 保留英文以免过度限定；不擅自指定HTTP或OSI传输层 |
| authoritative test | 作为判定依据的测试；正文为“以哪个测试为准” | 与权限语境的authority分开 |
| negative space | 不应改动的范围（negative space） | 任务显式排除的相邻工作，不采用绘画“负空间”直译 |
| slice / non-goals | 本次工作范围 / 非目标 | 沿S81/S90/S93，不作数据切片解释 |
| bug / threshold | 缺陷 / 阈值 | 沿S82/S96，不擅改成安全漏洞或度量结果 |

## 沿用和消歧

frame用任务界定/任务框架，evidence用仓库证据，proof用验证证据，receipt用可检查凭据；区分音频帧、贝叶斯边际似然和支付收据。authority/delegated是权限或授权，authoritative test是作为判定依据的测试。本文无success criteria或ownership字面术语，不添加对应字段；唯一性由哪层保证不改为所有权。public是对外行为，shape是格式，negative space是明确不应改动范围。

## 保护规则

核心及补充表优先。API、模型、专名、标识符、路径、URL、公式、数值及代码/图载荷保持；按本课语境说明首现，不将异义词机械统一。源内矛盾、宽泛或版本性断言另列SCOPE，不静默改写源技术含义，不把翻译/语言PASS当作运行或安全验证。

只依赖固定英文及术语起草，不要求先修中文正式验收；本表不包含旧中文正文或segments。支持候选、语言审校、真实GFM、运行和批次分别记录。
