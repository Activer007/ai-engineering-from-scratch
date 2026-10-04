# S108-plan-from-evidence English-first 支持范围

状态：本地check-only own3候选，未安装、未发布，不增加正式课程数。当前独立技术/中文语言PASS只绑定以下版本，不代替支持安装、真实GFM、远端最终字节核验及适用批次回归。

## 固定英文与唯一目标

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Source tree: `3d90647a3449a7b228a6b6025ed2b333ef99e81c`
- Lesson: 14-44
- Canonical docs H1: Build an Evidence-Backed Execution Plan
- Source: `phases/14-agent-engineering/44-plan-from-evidence/docs/en.md`
- Source Git blob: `26296937321825c7c9131337539052b6b49669cf`
- Source SHA256: `1018b075aafa5bb25c695859db764d57a00d1991c450c75511ce0bc3cb6c8139`
- Target: `i18n/zh/phases/14-agent-engineering/44-plan-from-evidence/docs/zh.md`
- Eventual record: `i18n/zh/.curated/lessons/14-44/translation.json`
- Original core blocks: 83
- English prerequisite line: **Prerequisites:** Phase 14 lesson 43
- Actual first write UTC: 2026-10-04T14:07:00.362914+00:00 through 2026-10-04T14:07:00.363751+00:00
- First-write receipt SHA256: `6c20643e23606067105e7d16dd1c110b9e65baf6eedbf25a5d7744eeb765b5cd`
- Original complete first draft: 5111 bytes, SHA256 `ce9e1943428d8192958ea232b0878cbefa5fd28163379bad326e7ca23a45bf9a`
- Original translation record: 33108 bytes, SHA256 `99f5b7d4fb7a996631a7c97ca5fe9aca0a114437c0f37decaa8e80a4c1391af9`
- Current reviewed target: 5081 bytes, SHA256 `e2612b01f213d9b13fc5f3c8488a9cfbce42da7bb29befc28487a5b700865cf9`
- Current draft record SHA256: `99f5b7d4fb7a996631a7c97ca5fe9aca0a114437c0f37decaa8e80a4c1391af9`
- Independent language review SHA256: `3b1095bbec5f3baec8545507a80bbb854c53ee8f26515c1d5651730bdebe158d`
- Existing local strict receipt SHA256: `673acad8900506757ea671cf0600ac1036843a0f6099a0356477d4b4c83d5e1d`

首写以原回执和原字节为准，不用mtime重建，不倒推为当时独审或own3已通过。本课源文件见DEPENDENCIES.source_files；先修固定英文已定位，无先修中文formal门禁。

## 真实修订绑定

- Revision 001: 2026-10-04T14:08:12.100500+00:00 through 2026-10-04T14:08:12.101152+00:00; target `ce9e1943428d8192958ea232b0878cbefa5fd28163379bad326e7ca23a45bf9a` → `e2612b01f213d9b13fc5f3c8488a9cfbce42da7bb29befc28487a5b700865cf9`; receipt SHA256 `f1ad89c1bf191d1ee0d17c2b69800b5d3fb9bcf8f0b9f80750f1e5d1eef89ea6`; diff SHA256 `cc570152e88b440435423ef8323f1d14c3fd775c6a1194cbd5c8c3b64601ed86`

修订首尾快照及原差异均保留，只用技术事实和hash作公开绑定；不替换首写或初始record，不把后续版本当作首次版本。独立审校针对最终target/record，未要求新的翻译修订。

## 固定支持与当前溯源

共同准备清单SHA256 `aef5293c38284a7c281852d115973b8e1eb24c4b2a4787226bf578714b723e13`。files/support_pins为有记录的公开投影，保留common109原顺序、公共身份与历史role/classification，并非原内部对象逐字段完全相等；去除S97–S102条目的12个私有路径定位值，保留其receipt SHA256。reference_glossary_pins为101 TERM，另8 controls；own3只含本阶段DEPENDENCIES.json、SCOPE.md、TERMINOLOGY.md，总112。正文、record、兄弟阶段及图资产均不算own3。旧已核Git身份复用，不重写历史类别或首写时点。

当前冻结as-of为正式批次结果独立回读真实时间2026-10-04T14:39:28.193462+00:00：正式已审草稿117，INDEX commit `03379392933fa99905d1ba604dfb14c174060eb6`、SHA256 `98f0af00d276f873998de9313e8fd14c8553fc4e27a9dce473dcb1f8358532aa`；独立回读SHA256 `428e243e351cdfc5e8d655b232b779e5d58c41898f1fe9b7d4e0b96463bf53bf`。actual117于2026-10-04T14:25:30.110274+00:00至2026-10-04T14:25:40.159393+00:00真实执行，新覆盖S98/S99/S102，结果SHA256 `382c6ca8bf3cfe5eade9c2d0309848adc319e9c519ffe8ea1d4e649cd275083b`，正式增量0；不覆盖S106/S107/S108。本课所属批次尚未运行，不继承历史PASS。book5/6缺xelatex.fmt、站点空标题ID及CI/移动端/交互/发布等限制保留。

保留record schema_version=1、DEPENDENCIES version=1及原f9 core/S07/S19精确控制。own3 hash由外部manifest固定，无自引用，不新增builder/checker/audit框架或重分类表。原33 fixture只复用既有固定身份，不读取其旧中文正文或执行回归。

## 已有证据与实际限制

- 规范题名取实际docs H1“Build an Evidence-Backed Execution Plan”；quiz的“Plan from Evidence”仅为短题名。依赖的是固定英文14-43，不要求该先修中文formal通过。
- validate只检查ID、非空evidence tuple、非空白proof、未知依赖及环；不核实引用事实/路径或证据真实性，不运行proof，不逐项拒绝tuple内空字符串；review contract也可作为非空proof。
- execution_waves按依赖拓扑分层，不检测文件/资源冲突、不执行任务，也不证明真实安全并发。单独调用会按ID字典覆盖重复项；正常validate/plan_document先拦截。环错误可能包含环的下游受阻节点。
- 可恢复执行是设计要求；输出JSON仅有status/issues/waves/items，没有逐项完成状态、已运行验证凭据或产物变更记录。completed变量仅用于拓扑分层，不是实际执行状态。
- 不可逆动作前解决不确定性及人工批准需要判断；WorkItem没有审批字段，validate不实现该门槛。示例路径和proof命令是课程字符串，不是已核仓库事实或本次执行指令。
- 本课Mermaid依赖图、bash命令及源载荷保持，无SVG；源quiz6题、7个原测试均仅静态证据。main按__file__覆盖outputs/evidence-plan.json。本作者较晚的有限CPU提案为另获GO后完整5文件临时副本内运行main及7测试，各≤5秒、合计≤10秒，只写副本；先前源准备的AST-only方案仍是历史提案。两种方案均NOT_RUN，不执行proof字符串、网络、安装、下载或模型。

## 核验与发布边界

本准备仅核新候选JSON/字节/hash、当前作者/首写/真实修订绑定、本三课17个源文件及6个先修英文的既有身份与当前字节；复用101 TERM校准及已核common身份，不重新解析所有历史commit:path。S85–S96历史commit:path在原准备对象库缺失的限制保留，未fetch、未补造。固定源准备清单SHA256 `366f8db5752f3a40784a05d22380aa212096e5dd164c2b40d11f6e97286a1a66`。

没有全源扫描、课程执行/import、main/tests/CPU实验/模型/训练/GPU、安装/下载、实际GFM/site/mobile/PDF/CI或全库回归。只生成候选，不写作者、英文源、原支持、INDEX、queue或远端。publication pending/null是冻结时点的状态；后续发布须另有真实commit及独立完整字节回读。语言PASS和静态核对不代表本课已正式登记、运行或批次通过。
