# S90 / 14-50：选择能改变决策的最小工作范围

固定正文提交：e56814eee13e0896151b20d4e6e723df5c6f9911；支持提交：f6d305f6b542908bd6c05d6e781869762cab9b35。原文提交：1bafaa88bb4668356791150bec3a6d7df38387eb。草稿 PR：https://github.com/Activer007/ai-engineering-from-scratch/pull/94。

本封装只追加 review.json 的 actual_GitHub_GFM 与 candidate_single_course_actual107 两个字段，并新增本阶段 TASKS.json、VALIDATION.json、REPORT.md，共四文件。原 review 的 49 个顶层字段、全部值和最终闭括号前的原字节前缀保留；author_self_review、61 块完整双审、31 内容块、30 分隔块、源问题和运行记录均未删除或重新嵌套。原 review 273972 字节，新 review 304118 字节。中文、translation.json、三份支持文件、原 source/code/core 均不修改。

reference_glossary_pins 实际为 86 份术语文件；common support 94 项含这 86 份术语及 8 份原控制/检查器；own support 另有 3 份。不是 S85 旧字段的 91 条规则，也不声称语义通读全部词表。独立远端证据含 12 次完整 base64 读取、固定/当前分支六文件与新 Git 字节核验；原 5423 文件、60,903,817 字节及 LICENSE 原样保留。正文提交仅在支持父提交上新增本课三文件。

完整技术与中文独审保留作者 8 条及独审 7 条源问题。required_proof 标签覆盖不等于真实服务识别或操作人员信任已获实证；合格方案按 (score, -effort, name) 取最大，不保证全局最少投入。alternatives 仍包含不合格方案且无 eligible 字段；fixture 没有自然语言选择理由字段；stop rule 是正文和练习要求，示例代码未实现。docs H1 与 quiz 短标题不同，两者事实分别保留。不得以翻译验收静默修源或背书教学断言。

原 stdlib main 与五个原测试在历史隔离副本中各执行一次，共六条命令全部退出 0，生成 JSON 与固定 fixture 逐字节相等。它们不是本封装新跑的课程测试，也不是练习、真实事件、生产自动修复或新实证。首次完整草稿未单独保存的原始限制仍保留，不把后来文件冒称首次快照。

GitHub 固定中文页面的主报告与独立像素复审绑定同一正文。独立复审实看全部 14 张原始 JPEG，核主清单 38 项及 42 个输入。61 个 lossless 块和全文 DOM 在明确 Markdown/空白规整后完全匹配；10 标题、12 段（含引言及元数据）、6 列表、6×2 表、1 可见普通代码、1 Mermaid、2 inline 路径及 2 外链完整。隐藏 Mermaid 源码 pre 不算第二个可见普通代码块。

默认 Mermaid 由视口 04+05 的同状态组合完整显示 8 节点、9 有向边、No/Yes 分支及全部长标签。主覆盖视口 09/03/04/05/06/07/08 连续重叠，实际高度 747、滚动后排除顶部 110 的工作区间覆盖正文 348–3334.421875；以逐块可见内容和实图重叠佐证，而非把 DOM 或坐标当作看过像素。

原生 Open dialog 默认裁掉下部节点；一次 Zoom out 后 Required proof 位于上沿外。未测 Pan、Reset、Zoom in，不授予全交互通过。Escape 与 iframe 数量不能单独证明关闭；关闭按钮后的实际正文像素及 isVisible=false 共同支持关闭。全页图有空白 Mermaid 和穿过动手区的 sticky 栏，只作补充。JPEG 1165×747 与 CSS inner1180×757、visual1165×757 的差异根因未建立，工作区间不是经标定的像素变换。初始 svg 八匹配诊断保留，未注入或修改 DOM、SVG、截图；本封装没有重新访问或截图。

实际107回归基于独立正式106索引 5f141d89c43b37f87caa05c037e8c71580b8ff7a（SHA256 0341f3a9425449d3bce93d88985afd55a5945de56bd4700a208004e093bfe467），且只加入14-50。S88/S89及旧待验收09-01、10-05、10-06均排除。原33/S07 24/S19 50控制全部通过；原 strict 直接105，仅保留 S07 b0213 与 S19 b0245 两项既有精确边界，没有新增例外。两个新目录各107篇 Markdown 字节相同，13个 SVG 各两份独立复制，三项仓库审计退出0。实跑时间 2026-10-04T08:41:07.213233+00:00 至 2026-10-04T08:41:21.704474+00:00；目录 run-id 不当作实际执行时间。19 组原始日志、命令观测、输出文件和前后输入绑定均重新读取；旧回归不替代本轮。

回归 all_pass=false。book 本次实际 5/6 通过、1 失败、0 跳过、0 预期失败，缺失 xelatex.fmt 且有自动 mktexfmt 诊断；没有安装、手工修配置/缓存或整本 PDF 通过。原站点解析器虽退出0，仍有10个空中文标题 ID，因此 BLOCKED_SOURCE_RENDERER；GFM正文可读不等于课程网站已通过。

正文 head 的 statuses 与 PR 触发 workflow 首分页均为空，不是 CI pass，也不是未来 final head 检查。当前正式计数仍106，增量0；未来 final9 读回、final head CI、PR正文读回及单课正式107索引均 pending。没有生成未知提交号，不合并、不发布、不推进其他课程。
