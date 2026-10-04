# S120-verification-gates English-first 支持范围

状态：本地check-only own3候选，未安装、未发布、不增加正式课程数。独立技术/中文PASS只绑定当前字节，其他验收证据分别记录。

## 固定英文与唯一目标

- Source commit: 1bafaa88bb4668356791150bec3a6d7df38387eb
- Source tree: 3d90647a3449a7b228a6b6025ed2b333ef99e81c
- Lesson: 14-38
- Canonical docs H1: Verification Gates
- Source: phases/14-agent-engineering/38-verification-gates/docs/en.md
- Source Git blob: 5b387ae8c8a977eb50eb50c7e0e61926a733a4cc
- Source SHA256: 4959114e249714257295b82f895d03c8b8a144bd1c689883bc9cf7f25c9785a0
- Target: i18n/zh/phases/14-agent-engineering/38-verification-gates/docs/zh.md
- Eventual record: i18n/zh/.curated/lessons/14-38/translation.json
- Original core blocks: 91
- English prerequisite line: **Prerequisites:** Phase 14 · 33 (Rules), Phase 14 · 36 (Scope), Phase 14 · 37 (Feedback)
- Original pre-write declaration UTC: 2026-10-04T18:10:44.977527+00:00
- First write started UTC: null
- First complete target written UTC: 2026-10-04T18:12:18.611186+00:00
- First-write receipt SHA256: 988f2a8adba96c0465923d4f5237dbb45f30654b5a8c8b16196be862e386bf65
- Original complete first draft: 9544 bytes, SHA256 d0f6979c855b23efa0bade948a18075ac785783b16e4af34e29dbf823bdd3577
- Original translation record: null: first capture failed; no valid original first-body record
- Current reviewed target: 9534 bytes, SHA256 27197b41092db44d3be695366aae3c26bf2f49e598f3c0ad9d234fc151f10761
- Current draft record: 38671 bytes, SHA256 cfdca259baee5053e572460cd72524909f8507f7637fd1728c5ba67ada7c170f
- Original HANDOFF SHA256: c982d69f646bb257e9b87d5300b1f3e6cbadaff6bed13a77608c45e510514a35
- Existing original strict stdout SHA256: 2fa86706513ad504c9ac143b6bbc576108926c629e73d3da96a1c36d59ac9cf0

Pre-first-write declaration 2026-10-04T18:10:44.977527+00:00; complete first body timestamp 2026-10-04T18:12:18.611186+00:00. Separate composition/write-start timestamps were not recorded and stay null. First capture failed, so no valid record for the original first body exists; original_translation_record_sha256 stays null. The first successful capture follows revision01; its actual record is separately bound to that revision, then record-metadata-01 and body revision02. Revision receipts have one event timestamp, not invented before/after intervals.

原HANDOFF的待独审与旧计数是当时事实，不改写。当前独审由其后独立报告绑定；校准与首写时间不倒填。原11行术语校准表与首次说明逐字保留，原113表相关语境筛查声明独立绑定；不重新发明术语或首写前校准时点。

## 真实修订与审校绑定

首次capture真实失败：exit1，b0059把March写作“3 月”新增数字签名；revision01改为“三月”并做另5处文字调整后才有成功record。随后record-metadata-01仅更正capture硬编码run_date与补充表/作者证据；revision02把“可能悄悄删除”修回源断言“会悄悄删除”。两次正文修订与一次record元数据修订分开，未加strict例外。失败stdout为空、stderr725B与exit日志均保留；失败不会被后续PASS抹去。

- Revision 01: before UTC None, after/event UTC 2026-10-04T18:13:54.994120+00:00; target d0f6979c855b23efa0bade948a18075ac785783b16e4af34e29dbf823bdd3577 → 0cc392ea58a3a4cb25531c020e9c7f359d8c3f5775d2d4fd0fd47018cab57aff; record null → 522693ce99213aede099ce12da5a09280a356f1d6907c869ffaaa9b7db9a3f41; original receipt SHA256 5da41a4f8ae267a74be3a1913f2babe68132ffed8fc9d81130f1806daa547aa8
- Revision record-metadata-01: before UTC None, after/event UTC 2026-10-04T18:13:55.070699+00:00; target 0cc392ea58a3a4cb25531c020e9c7f359d8c3f5775d2d4fd0fd47018cab57aff → 0cc392ea58a3a4cb25531c020e9c7f359d8c3f5775d2d4fd0fd47018cab57aff; record 522693ce99213aede099ce12da5a09280a356f1d6907c869ffaaa9b7db9a3f41 → 4b9800d90fe4bec522b3aebccb812395fa2ab92635732dd5d165515d8f748c42; original receipt SHA256 8dc35e5967bbf9cbc7d24dd7963238f11b7b6b9d8175c1f69e3dd718383367ed
- Revision 02: before UTC None, after/event UTC 2026-10-04T18:14:49.280120+00:00; target 0cc392ea58a3a4cb25531c020e9c7f359d8c3f5775d2d4fd0fd47018cab57aff → 27197b41092db44d3be695366aae3c26bf2f49e598f3c0ad9d234fc151f10761; record 4b9800d90fe4bec522b3aebccb812395fa2ab92635732dd5d165515d8f748c42 → cfdca259baee5053e572460cd72524909f8507f7637fd1728c5ba67ada7c170f; original receipt SHA256 8d485eab39b7fd8cbd85917a3ee8890470947983d103632d9a40179d13b77b19

独立全文英中对照及另次中文通读PASS覆盖91块，当前target/record精确匹配。独立JSON报告SHA256 f460a92bc69f30c40e56c99789c29509b19423a431e7a2f06e4441a8143c7238，配套报告SHA256 085a7e9e5de0075691f1059a6764f7e6c935de0a052f4687310240194bf5b9d0。无剩余翻译必改项。以上引用既有独审，不重新审校或运行strict。原首稿和所有old/new快照保持；相同字节别名不算修订。作者未另存独立diff文件时diff hash为null，真实change收据与完整快照绑定，不补造旧文件。

首capture失败证据：CAPTURE-FIRST.stdout.txt SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855, CAPTURE-FIRST.stderr.txt SHA256 df7bda2f9e0c2f42be5a158b91c95822a6efdd4f63e4fae6589c83900d93d18b, CAPTURE-FIRST.exit.txt SHA256 4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865。首次成功capture原record SHA256 522693ce99213aede099ce12da5a09280a356f1d6907c869ffaaa9b7db9a3f41，只属于revision01之后，不属于原首稿。

## 固定支持与冻结溯源

common清单SHA256 015a3ae6b4db3e97dd9856c6fe2f4f74cf88b4095788022ffd5fbb13fa4661d8。files/support_pins保留原121条顺序及全部公共身份与历史role/classification，仅删36个私有locator，receipt SHA256仍保留；公开投影不声称与私有清单逐字段完全一致。113 TERM+8 controls，own3只有本课DEPENDENCIES/SCOPE/TERMINOLOGY，未来总124。正文、record和SVG不计own3；S119原linkedSVG字节独立保护。

as-of冻结于2026-10-04T18:38:56.231263+00:00：正式129，INDEX commit ebc28192c8eb5951cc5c8ce698946bdd440e16b3、SHA256 83c72bb1cdfa5524de2c22d9b16b13ddd84232819081f879b7472eeba8deee88、独立回读SHA256 ae3571ed47148dccf326b0963eefd786326ca1990d94860d2ae8be6b2198fee7。actual129仅覆盖S110最终修订版/S112/S113和此前126，运行2026-10-04T18:19:22.909427+00:00至2026-10-04T18:19:34.538511+00:00，结果SHA256 61542dcb61255e7b3cb7cf2b7cbecb46925c6bf30bde1bfb0fb77897a220a1e5，回归正式增量0；不覆盖S118/S119/S120，三课未来批次NOT_RUN。book五过一失败（缺xelatex.fmt）、站点36空锚点及未完成发布门禁继续保留，不把翻译回归PASS称作全面成功。冻结后不为追新鲜度重写。

DEPENDENCIES version1与原f9 core/S07/S19 controls不变；original33 test-only fixture只沿用旧固定身份，未读取旧中文课文或执行。own3 hash由外部manifest绑定，无自引用；不依据formal129重新分类历史TERM。固定英文先修即可支撑翻译，中文formal不是额外门槛。

## 源问题与实际限制

以下原作者风险材料按原内容保留，来源SHA256 d223cc61ce6c1f74eee4afffb83f097dc7e9d602f1e4cda84b25678344e94a8f；其中旧待验状态只代表作者记录当时，当前语言PASS另见上述独审。涉及执行的文字仅为历史提案，不是本次运行授权。

# S120 固定英文源风险（静态阅读，未修源）

基线为 1bafaa88bb4668356791150bec3a6d7df38387eb；本课 en.md SHA256 4959114e249714257295b82f895d03c8b8a144bd1c689883bc9cf7f25c9785a0。风险不因译文 strict PASS 消失，译文不表示可执行指导或生产安全已验收。

## R1 报告路径、输入与函数签名不一致
- en.md b0035/mission/skill 指定 outputs/verification/<task_id>.json；b0053又说脚本旁；main实际使用 HERE / verification_report_{task_id}.json，HERE为code目录。override日志也写code旁的overrides.jsonl，与文档outputs/verification/overrides.jsonl不同。均忠实保留，没有翻译修路由。
- docs/mission/skill声称verify(task_id, artifacts)和各产物加载器/diff输入。实际verify接受Artifacts，未加载文件、读取diff、读取scope_contract.allowed_files或验证命令真的执行过；feedback/report由调用者提供。输出未列被消费的源产物路径，而skill明确要求它们。

## R2 签名覆盖与人类豁免边界
- record_override签名的是task_id、finding_code、reason、user_id、head_commit、ts的规范化JSON；_sign用HMAC-SHA256并截断为32个十六进制字符。verify_signature排除signature字段后重算。这里仅静态核读，无签名、密钥读取或环境读取。
- 没有绑定diff、报告内容hash或产物路径；head_commit和user_id都是调用者提供的字符串，没有读取/认证真实HEAD或人类身份。持有共享HMAC秘密不等于“仅人类可豁免”。
- verify从不读取或应用override记录，也不调用verify_signature；签名辅助函数不是验证关卡的豁免执行路径。未配置秘密时demo会跳过记录而继续，未证明生产豁免拒绝链。

## R3 关卡逻辑与输入校验缺口
- 空acceptance_commands加空feedback不会触发缺少验收命令；空rule_report无失败项；空scope_report无写入项。与skill的失败即拒绝要求不等价。这里只比较传入字符串/报告，不证明执行来源、实际写文件边界或commit绑定。
- _rule_findings把每个未通过规则都设为block，不查看源规则severity；off_scope固定warn，未实现按路径的项目策略。
- coverage输入直接转float，没有有限性/范围校验；NaN等比较可能不产生预期block。缺失coverage只warn；并非默认强制下限。
- docs b0065说“previous merge's floor”；代码实际比较previous覆盖率。精确1个百分点下降不触发regression block，仍会产生minor_regression warn；strict再提升。不得把百分点改成百分比或把代码实现回填到译文。
- 代码打印失败报告但main没有以报告失败状态设置非零进程退出码；CI拒绝合并需要另行接线，不能由演示退出码推断。

## R4 教学与外部断言
- 学习目标/小标题说无例外拒绝，随后允许人类签名豁免；直接先修14-33亦有操作者边界。保留张力，不合并为新保证。
- “Four patterns”实际列五种；mission将签名豁免日志列为out of scope但main实现辅助函数。quiz实际7题（2 pre/3 check/2 post），没有code/tests目录。
- 文中pre-commit不可绕过、每层失败必由下一层捕获、2026供应商/文章主张及所链文章的准确性均未独立核实，不把翻译视为背书。表格“both”的指代保留，不猜测。
- source的1个裸围栏只按原工具既有许可补text；Mermaid与figure载荷完全保留，未做网页/站点交互验收。

## 安全有限CPU提案（仅文字，NOT_RUN）

如果以后另获明确执行许可，可在一次性隔离副本中进行有时间/内存上限、无网络的纯函数fixture检验：仅验证干净输入、缺命令、null退出码、空规则/验收集合、非有限覆盖率、1个百分点边界与strict提升。先静态抽取纯数据/verify依赖，避免导入或调用main、override、秘密加载器、报告落盘路径；不访问账户/环境秘密，不安装包。预期终止条件为一组固定fixture完成或到达5秒限制，结果只写隔离目录。当前没有执行此提案，也没有课程main/tests/import/API/安装/网络运行。


独立审校的源限制（与原作者风险分别绑定，均不表示源已修复）：

- SR01：文档声明verify(task_id, artifacts)并消费diff和本地桩加载器；实际签名为verify(art, strict=False, coverage_floor=...)，Artifacts无diff字段，main直接构造三个Artifacts，不是逐一加载磁盘产物。 译文保留文档签名及输入，不暗改成实现说明。
- SR02：正式文档/mission/skill指定outputs/verification/<task_id>.json与outputs/verification/overrides.jsonl；main写code/verification_report_T-xxx.json，覆盖日志写code/overrides.jsonl。docs第86行又明确“脚本旁”。 两种原文路径均照译；本次未创建报告或日志。
- SR03：verify未读取override或调用verify_signature。_sign用共享环境密钥的HMAC-SHA256前32个十六进制字符；user_id/head_commit为调用者输入，签名只能在密钥与消息可信的前提下校验完整性，不能独自证明人类身份、批准权限或真实HEAD。record_override仅检非空，字段reason/user_id与文档override_reason/overridden_by也不同；没有验证git跟踪。 中文signed/人类豁免均忠实保留为源政策描述，不把演示HMAC当身份保证；未运行或签名。
- SR04：空acceptance_commands/feedback/rule_report与空scope_report不会自己产生block；缺覆盖率只warn，默认非strict仍可通过；若提供无回退的合格覆盖率，strict也没有空验收专门拒绝项。报告不记录所消费产物路径，且没有绑定反馈记录的任务、cwd、HEAD或执行真实性。 这属于源示例与skill拒绝规则的落差，不新增中文隐含保证。
- SR05：float转换后无isfinite或0..1范围检查；current为NaN时floor比较和delta比较不产生阻断；floor或previous为NaN也削弱对应检查，非数值可抛转换异常。上述为静态控制流推断，非运行结果。 不在译文中加入输入验证或伪造测试证据。
- SR06：正文称previous merge的floor，代码比较previous覆盖率观测值；previous缺失默认为current，覆盖率缺失为warn；回退超过0.01且不isclose为block，较小正回退含恰约1个百分点为warn，在strict下也block。因而正文不是全部实现规则。 保留80%和1个百分点及原floor词义；独立列边界，不将其改成1%相对值。
- SR07：_rule_findings把任意passed为假/缺失的规则设block，不读取rule severity；_scope_findings只信任两个报告字段，off_scope固定warn再由strict提升，没有直接比较touched_files与scope.allowed_files。表内source=both的指代也不明确。 保留表中block或warn及“两者”，不擅加缺失的数据来源。
- SR08：仅以str(command)匹配给定验收字符串；任一验收记录非零就block，历史失败后成功重试仍未被最新结果消解；任何反馈null都会block。未处理14-37的parent_command_id链，也未校验命令在正确环境真实执行。 翻译没有把这些简化检查夸大为完整验收证明。
- SR09：Four patterns后实际五段；覆盖率和strict列为练习但源码已实现，mission将签名日志列出范围却有实现；quiz实际7题（2pre/3check/2post）而AGENTS要求6题（1/3/2），该lesson未提供测试文件。 忠实保留“四种”和练习，不修源或凭空补测。
- SR10：pre-commit non-bypassable、确定性层保证后层捕获、Hybrid Norm归属，以及覆盖率足以阻止删测试等强断言未由本课实现证明。本次网络未用，7外链仅核字节，不报告可达性或事实核验。 按原强度翻译，尤其保留作者将“可能删除”修回“会删除”的历史；源事实不以译文背书。
- SR11：“每个其他组成要素均在上游”与图中下游Reviewer不完全一致。练习的人类键入60秒豁免未定义身份、文件关联或可靠时间来源，不能直接充当安全授权。 不借翻译新增豁免限制或改变原任务要求；运行与安全验收仍未通过。

直接先修映射与源歧义另按固定准备清单保留，原清单SHA256 1d2a5be48d376fddbbcc3dae1a2ca2f169bdad3326777540efaa3de3eab38271：

- 14-33 / Agent Instructions as Executable Constraints：Unique fixed phase/lesson number; short selected label is an abbreviation of this H1. Full English prerequisite read. Chinese acceptance is not an authoring gate. Rules H1 is Agent Instructions as Executable Constraints. Recorded human override policy contrasts with14-38 learning objective without exception; preserve scope/tension rather than reconcile.
- 14-36 / Scope Contracts and Task Boundaries：Unique fixed phase/lesson number; short selected label is an abbreviation of this H1. Full English prerequisite read. Chinese acceptance is not an authoring gate. Allowed files intersect, forbidden files union, time budget minimum, approvals accumulate. network_egress None means defer,[]means deny-all; warning budgets are not block overrides.
- 14-37 / Runtime Feedback Loops：Unique fixed phase/lesson number; short selected label is an abbreviation of this H1. Full English prerequisite read. Chinese acceptance is not an authoring gate. Feedback evidence for the run differs from telemetry; missing exit_code:null cannot prove success. stdout/stderr tail field wording contrasts with head+tail capture; production redaction/rotation/retry mechanisms not validated.

## 准备与发布边界

本次仅绑定完整作者HANDOFF/首稿/真实修订/术语/源风险、既有独立91块PASS和strict缓存，核固定16份源课包、7份直接先修与三个目录common121字节身份。原作者正文/record/source/core/common全部保持，own3只在本地候选目录。未安装支持、未写远端/INDEX/queue，未运行课程main/tests/import/CPU/model/API/GPU/签名/安装/下载或任何strict与回归。真实GFM、站点、手机、PDF、CI、用户批准与发布分别待相应证据；忠实翻译不背书源的安全/性能/2026事实。
