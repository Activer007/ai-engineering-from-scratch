# S93-preserve-judgment-specs 术语增量 v1.0

日期：2026-10-04 UTC。作者新提案已与完整固定89份参考词表校准。本文件是待协调者精确字节确认的本地预发布支持候选，不是译文审校或正式接受。冻结后保留该预发布快照；publication字段的null仅表示冻结时尚未绑定发布提交，不自引用本文件的Git提交，也不声称永久未发布。实际发布commit由后续作者record和远端回读receipt绑定。

固定英文：`1bafaa88bb4668356791150bec3a6d7df38387eb`。规范 docs H1：Write Specifications That Preserve Judgment。

本轮核验正式基线为106课。参考集合为86份正式TERM（84 accepted stage＋core2）和3份active-reviewed TERM（S88/S89/S90），共89份；另有8份原controls，common共97。本课own3另计，总100。S85现属正式已接受，不沿用旧支持快照中的active状态；旧TERM原字节和历史105叙述保留，其历史文字不是本轮状态。S88/S89/S90与本轮新draft不提前计入正式106。完整固定来源见 DEPENDENCIES.json。

| English | Proposed Chinese | Boundary |
|---|---|---|
| specification | 规格说明（specification） | Distinct from requirement 需求; not a code script |
| preserve judgment | 保留判断空间 | Meaningful discretion within constraints, not withholding judgment |
| invariant | 不变条件（invariant） | A condition required to remain true, not merely a passing example |
| executable contract | 可执行契约（executable contract） | Representation validated by this lab; does not assert real product execution |
| proof | 验证证据（proof） | Evidence that must match the claim's level |
| proof receipt | 验证凭据 | A record of verification, not a payment receipt |
| locked / bounded / delegated | 锁定 / 有界 / 委托 | Exact English mode words retained at first definition; no alteration of literals in protected content |
| surface | 组成要素 | Contract structure, not a UI surface |
| authority | 权限（authority） | Authorized action; consistent with S87 and S84, not credibility or prestige |
| public compatibility / public behavior | 对外兼容性 / 对外行为 | Publicly exposed behavior, not ownership of public resources |
| wire test | 传输测试（wire test） | Source immediately limits it to serialization and transport behavior; English retained to avoid over-specific translation |
| human checkpoint | 人工检查点 | Required human decision point; the demo emits only a routing list |
| browser journey | 浏览器中的用户旅程 | An observed interface path, not a unit test |
| non-goal / outcome | 非目标 / 结果 | Existing S81 meanings retained |
| production write | 生产环境写入操作 | Existing S84 meaning; no actual production action authorized |

## 词义和结构边界

核心/补充词表优先；首现按既定中英对应，专名、API、代码标识符保留。通用章节标题沿ADDENDUM，但不得新增源没有的章节。保护数字、单位、形状、轴次序、公式、代码、图载荷、链接、路径和源文件间差异。自然语言数量须等值逐块对照。

参考术语仅供一致性校准，不能复用旧译文正文。支持准备未读取旧中文课文、旧record的segments或format_revisions、452/457材料；按需读取的docs/i18n.md规范含既有中文质量示例，这项暴露已如实记录，示例措辞未复用。source阅读、术语准备及作者draft不构成新增正式完成课。

invariant统一为不变条件（invariant），沿新S88的相同“始终成立的条件”含义；不与不变性（invariance）、位置不变性或数学量混同。specification统一规格说明，requirement是需求；preserve judgment为保留判断空间，具体指有边界的自主判断，不是暂停判断或无限自主权。
authority沿S84/S87/S90为权限；讨论归属时用权限归属，边界用权限边界。locked/bounded/delegated为锁定/有界/委托，分别是不由智能体自行选择、在显式限制内选择、负责选择并解释。英文模式和代码字面量保持。
proof按源语境为所需验证证据；proof receipt为验证凭据。它们不能被字符串、schema executable状态或低层测试PASS代替。wire test译传输测试（wire test），保留英文及序列化/传输行为限定，避免扩写成更窄的传输线协议测试。
