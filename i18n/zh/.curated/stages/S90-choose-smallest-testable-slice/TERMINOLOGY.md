# S90-choose-smallest-testable-slice 术语增量 v1.0

日期：2026-10-04 UTC。作者新提案已与完整固定参考术语集合校准；本文件保存冻结时的预发布支持快照，精确字节冻结由协调者确认回执证明。publication字段的null记录冻结时的历史状态，不自引用本文件的Git提交；实际发布commit由后续作者record和远端回读receipt绑定。它不是译文审校或正式接受。

固定英文：`1bafaa88bb4668356791150bec3a6d7df38387eb`。规范 docs H1：Choose the Smallest Slice That Can Change the Decision。

正式基线保持105课；参考集合为85份正式TERM（83 accepted stage＋core2）及1份 active-reviewed S85 TERM，共86份。S85的固定TERM提交为 `1a364d8283c864eccac467bb32a850a0d0779eef`，已独立语言审/GFM，但不将其标为正式106或中文先修门禁。来源逐项见 DEPENDENCIES.json。

| EN | 本课中文 | 依据与边界 |
|---|---|---|
| slice | 工作范围；按句意可用本次小范围工作/验证 | 沿用S81语义，不译成数据“切片”；标题采用“最小工作范围”。代码类名 Slice 不变 |
| outcome / outcome value | 结果；预期结果 / 结果价值 | 沿用S81、S84、S87；不是交付物或代码输出 |
| workflow | 工作流（workflow） | 沿用S84、S87；不省掉真实工作流的风险环节 |
| assumption / open assumption | 假设 / 尚未验证的假设 | 沿用S87；这里open不指开源，代码覆盖标签不等于已完成实证验证 |
| required proof set | 一组必须验证的事项；必须验证的事项集合 | 作者提案：强调候选资格要求的完整覆盖；实现中为required_proof标签集合，不声称是已验证的证据 |
| eligible / eligibility gate | 符合条件；具备候选资格 / 候选资格这一门槛 | 作者提案：先筛选覆盖，再计算比较分数；不把高分当成覆盖豁免 |
| uncertainty reduction / uncertainty reduced | 不确定性的降低程度 | 沿用S87 uncertainty=不确定性；不是提高模型确定性或统计置信度 |
| effort | 投入 | 作者提案：代码为分母中的正数维度，不擅自限定为开发小时或资金 |
| consequence | 后果；后果程度 | 作者提案：体现风险影响，不改成预期收益；量表方向为越小越好 |
| reversibility / reversible | 可逆性 / 可逆的 | 沿用S87；不是说历史事件或证据本身可撤销 |
| production commitment | 生产环境投入 | 沿用S87 commitment语境选择；不仅指口头承诺 |
| read-only replay | 只读回放 | 精确沿用S87；不暗示生产写入操作 |
| incident | 事件 | 沿用S84、S87事件响应词汇；不是泛指新闻 |
| service identification | 服务识别；服务识别能力 | 作者提案：需验证的能力标签，service-identification字符串不翻译 |
| operator trust | 操作人员的信任程度 | 作者提案：不凭空指定为值班工程师，不声称真实信任测量已执行 |
| data feasibility | 数据可行性 | 沿用S87 feasibility=可行性；合成数据界面演示不能验证此项 |
| production auto-remediator | 生产环境中的自动修复系统 | 沿用S87自动修复；源文示例，未执行任何真实生产动作 |
| UI-only minimum | 只做用户界面（UI）的最小方案 | 作者提案；保留UI缩写并解释 |
| operational uncertainty | 实际运行中的不确定性 | 作者提案：不要把从检验范围排除说成已经消除或解决 |
| happy path / exception | 正常路径 / 例外情况 | 沿用S84；不局限为代码运行异常 |
| artifact | 产物 | 沿用核心表、S81、S84；可说服人的演示不等于可重复测量 |
| reusable machinery | 可复用的基础机制 | 作者提案：平台化建设语境；不是物理机器 |
| stop rule | 停止规则 | 作者提案：结果可以触发放弃、换目标、换机制、补证据、缩权限；不等于只停止程序 |
| authority | 权限；权限范围 | 沿用S87及S84权限语义；不是权威性或证据可信度 |
| decisive evidence | 足以作出决策的证据 | 沿用S87 decisive语义；可促使否定或改变方向，不暗示已证明成功 |
| pilot | 试点 | 作者提案：小规模试行，不译成飞行员 |

## 词义和结构边界

核心/补充词表优先；首现按既定中英对应，专名/API/代码标识符保留。九种通用章节标题沿ADDENDUM。保护数字、单位、形状、轴次序、公式、代码、图载荷、链接、路径和源文件间差异。自然语言数量须等值并逐块对照，不改变数字字面量。

参考术语仅用于一致性；没有读取历史中文课文、translation segments、format_revisions或旧作者缓存。来源词表不等于可复用中文正文，source阅读/术语定义不计新增完成课。

slice统一工作范围；docs长标题译“选择能改变决策的最小工作范围”，quiz短标题仍作为独立固定源事实。viable在MVP引用说明中为可行，不机械套用S87组织语境的可持续性。required proof set是必须验证的事项集合，不把代码标签覆盖写成已完成实证验证。
