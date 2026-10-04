# S99-prototype-pilot-production 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Choose Prototype, Pilot, or Production Deliberately。

本地 check-only 候选，未安装或发布。复用作者固定95 TERM校准，定向复核相关条目与英文；不声称重新全文审查全部旧历史。以下保留作者提案，不要求强制改词，不改既有术语。103 common = 95 TERM + 8 controls；本课own3独立另计，总支持106。S98原样SVG是额外非支持资产。词表数不是正式课程数。

| English | 中文用法 | 语境与边界 |
|---|---|---|
| prototype | 原型（prototype） | 以最少真实暴露回答机制问题，可在技术上完整而仍可弃用 |
| pilot | 试点（pilot） | 沿 S90；真实受众与真实条件须限制范围，不是飞行员 |
| production | 生产阶段（production）；生产系统/生产数据按修饰对象 | 持续承担可靠性、风险与运维责任，不等同部署或仅模型注册状态 |
| learning environment / learning stage | 学习与验证环境 / 学习与验证阶段 | 为解答未知问题，不是模型训练环境或训练 epoch |
| unknown / learning question | 未知问题 / 要验证的问题 | 当前决策尚需回答的问题，不把字段 unknown 名称翻译 |
| consequence | 后果 | 沿 S90，不混为概率加权风险评分，低后果为后果较轻 |
| readiness / operational readiness | 就绪程度 / 运维就绪程度；运维已就绪 | 不等同模型成熟度或真实控制已经验证 |
| authority | 权限（authority）；权限范围 | 沿 S84/S87/S90/S93，指获准的访问与行动，不是权威性 |
| ownership | 责任归属；为其负责 | 组织/人承担持续责任，不是文件所有权、知识产权 |
| human owner | 由人担任负责人 | 明确人负责，不发明实际负责人姓名 |
| stage drift | 阶段漂移 | 用户、数据、权限增加而控制/责任未跟上；不套数据/术语漂移 |
| discardable / disposable | 可弃用 / 用后即弃 | 与可逆不同，不要求实际执行删除 |
| isolated | 保持隔离 | 不添加源未给出的“相互”隔离对象 |
| exit criteria | 退出条件 | 指扩大、修订或停止的判定，不等同 shell 退出码 |
| outcome and guardrail thresholds | 结果与安全护栏（guardrail）的阈值 | 沿核心及 S96；不杜撰具体数值或声称清单已强制执行 |
| service level objective | 服务等级目标（service level objective，SLO） | 与源代码 SLO 一致；目标本身不是已证明达成的保证 |
| on-call and incident ownership | 值班与事件处置的责任归属 | 事件沿 S81/S84，不是新闻事件；不省掉两类责任 |
| rollback / recovery | 回滚 / 恢复 | 两项不同要求；不可逆仍被判 pilot 是源边界，不修算法 |
| retirement path | 退役路径 | 系统生命周期退出安排，不是员工退休 |
| rollback receipt | 回滚凭据 | 沿 S93 receipt 为验证凭据的语义，不是付款收据 |
| telemetry | 遥测 | 与配置、访问控制、文档共同体现阶段，不声称本实验已采集 |
| bounded pilot | 范围受限的试点 | 精确沿 S96；不套 S93 的 bounded 决策模式枚举 |

## 沿用和消歧

沿用 S90 试点、S84/S87/S90/S93 权限、核心安全护栏及 S96 范围受限的试点。learning environment 为学习与验证环境，不是模型训练；ownership 是责任归属，与 authority 权限分开。production 为持续责任的生产阶段，不套 S57 模型注册标签；rollback/recovery 分为回滚/恢复，discardable 与 reversible 不同。

## 保护规则

核心及补充表优先，首次正文遵守中英对应；API、模型ID、标识符、路径、链接、数值、公式、代码与图载荷保持。通用章节沿补充表，英文没有的章节不补造。自然语言数量等值且不跨源块移动。源问题另列，不静默改数学、代码或技术含义。

词表仅用于一致性，不复用旧中文课文/segments；规范中文质量示例仅附带曝光，未引用其措辞。新译只依赖固定英文与术语，不等待先修中文正式验收。publication pending/null仅表示本次冻结未绑定发布提交；后续真实提交由外部记录和独立回读绑定，不自引用。
