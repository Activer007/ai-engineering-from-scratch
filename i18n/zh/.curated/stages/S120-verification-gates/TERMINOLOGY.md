# S120-verification-gates 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；规范题名：Verification Gates。

本地check-only own3候选，未安装、未发布、不增加正式课程数。common121=113 TERM+8 controls，own3另计，未来总124。原11行术语校准表与首次说明逐字保留，原113表相关语境筛查声明独立绑定；不重新发明术语或首写前校准时点。

| English | 本课译法 | 依据与边界 |
|---|---|---|
| verification gate / merge gate | 验证关卡 / 合并关卡 | 沿 S111 工程检查语境；不套用神经网络“门控” |
| workbench / artifact / surface | 工作台 / 产物 / 组成要素 | 核心、S102、S108、S114；不以产物存在代表验证成功 |
| scope contract / scope creep | 范围契约 / 范围蔓延 | contract为本课作者提案；creep沿S104；正文完整保留约束/报告的不同角色 |
| block / warn severity | 阻断级 / 警告级 | 严重级别，不套用核心权重“块”；受保护字段保留 |
| finding / verdict | 发现（或发现项）/ 判定结果 | 检查产物的术语，不增加安全/正确性证明 |
| signed override / override log | 签名豁免 / 豁免日志 | 不把共享HMAC实现当成人类身份或授权证明；源问题单列 |
| acceptance command | 验收命令 | 命令/执行证据与声称通过分开；沿S105验收语境 |
| coverage floor / percentage point | 覆盖率下限 / 百分点 | 原文1 percentage point严格译1个百分点，不改成1%相对变化 |
| defense-in-depth / hook | 纵深防御 / 钩子 | 沿核心补充表与S73/S82 |
| handoff / harness | 交接 / 运行框架 | 沿S84/S102/S111与核心补充表 |
| deterministic / LLM rubric | 确定性 / LLM评分准则 | 判定状态与定性审查分开；不把确定性等同正确性 |

首次说明：agent、verification gate、workbench、artifact、CI、LLM、defense-in-depth、hook、schema、handoff。产品名、API、路径、命令、Git字段、URL和图代码原样。March使用“三月”保留原数字签名，不引入3。章节名沿固定补充表。

## 沿用和保护

固定英文与术语足以起稿，先修中文正式验收不是门禁。核心和补充表优先；代码、数字、数学、API、路径、URL和图载荷受保护，源问题见SCOPE。术语校准、自审、独审、真实GFM、远端回读和批次回归分别记录，未把作者自审或旧批次PASS提升为当前课程验收。
