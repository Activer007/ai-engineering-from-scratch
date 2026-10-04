# S126-multi-session-handoff English-first 支持范围

状态：本地 own3 候选，未安装、未发布、不增加正式课程数。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；原控制 `f9b5e9cbe4012f54483794f920c0d87b06a7573d`。

## 当前作者与独立审校身份

- Lesson: 14-40
- Target SHA256: a0a0a8ddc0eb6c4f55945dbde308fd1e26a3084f1db29a8a6e78f75cbd6afb1b (12322 B)
- Original author record SHA256: ab5ec62bdd1d593140d2ab9e47c3db236cc6eb9edd522dac18eb7ffbc16ea6b2 (44150 B), status=draft
- Author handoff SHA256: 4442efb009b534d1539c098913c529ecb22be75fa60dcdea999757ae052eab1a
- Original independent review SHA256: a42306c98681543a9b3936318de0d8cbc0e4f75ce9c883724647be34867f14e2; companion SHA256: 079a11b0af23e5629c3c10704d29b9b247aae4dd4ade7ccb5d6d24f3729af340
- First complete body SHA256: 5e05c9736aa90c2b74524866cba9533840898f9a784ed792202e28c0cfeaa027
- First-body record SHA256: 9c2e6e9d162145babdaa545dedea89ec5c6372cd2e6a622834a734aa5aaa6363
- Original local strict evidence SHA256: 7a9c02dcb42dc772ab7a972c0c198a20af10cc08559b04fb26cda05e5e4a06a4; cached evidence only, not rerun

97块完整独审，首次capture成功和一次修订分别绑定；证据实际保存位置只在本地manifest中如实列出，不迁移作者文件。

Prewrite 2026-10-04T20:50:09.415644+00:00; body write 2026-10-04T20:53:07.688339+00:00 to 2026-10-04T20:53:07.711557+00:00; first capture succeeded 2026-10-04T20:53:24.719946+00:00 to 2026-10-04T20:53:24.770646+00:00. FIRST-BODY first_record=null describes the earlier body-write instant only, not a failed capture. One real body/record revision 2026-10-04T20:54:09.783062+00:00 to 2026-10-04T20:54:09.802787+00:00. Original author evidence directory remains at its actual location, without relocation or backfilled timestamps.

首capture真实成功且首record存在；FIRST-BODY早先null不误记为失败。一次3处用词+record日期/addendum修订。原证据实际位置保留，未搬迁重跑。

真实修订身份与时间（同字节快照不计额外修订）：

```json
[
  {
    "revision": "revision-001",
    "before_utc": "2026-10-04T20:54:09.783062+00:00",
    "after_utc": "2026-10-04T20:54:09.802787+00:00",
    "receipt_sha256": "70ac691947495201f185275c00b3c260049ed6b6f42419002f47bca18d9a8f3e",
    "old_target_sha256": "5e05c9736aa90c2b74524866cba9533840898f9a784ed792202e28c0cfeaa027",
    "new_target_sha256": "a0a0a8ddc0eb6c4f55945dbde308fd1e26a3084f1db29a8a6e78f75cbd6afb1b",
    "diff_sha256": "8236e11d8d5fd139e95e8dcb17748f5cb1f9f14a83c044e5ca86ca9871bfd529",
    "old_record_sha256": "9c2e6e9d162145babdaa545dedea89ec5c6372cd2e6a622834a734aa5aaa6363",
    "new_record_sha256": "ab5ec62bdd1d593140d2ab9e47c3db236cc6eb9edd522dac18eb7ffbc16ea6b2",
    "record_diff_sha256": "92bee57c3a9c2e3f9ade291e9fd2318932e39a3aa1b42eff42b19636cb4ffcba",
    "same_byte_alias_only": false
  }
]
```

## 固定支持与先修边界

原作者 common127 清单 SHA256 d1e95747c784a6e4be7b97903ec98b907d947ceae995fea2c01597aac965be53，119 TERM +8 controls；S117 已绑定真实 ff4d56e72126e854321b5d95a7c43a8b57a485bf / 6631ae3d6b514d374a63bd21afa98eaedeb995e2aeed3e664e037e6de6ea0c85，本轮不需要替换此pin。既有127项身份、顺序、角色和分类保持，公开投影仅移除48个私有locator值。

只在候选中追加 S121–S123 三个已发布且独立完整回读的TERM：当前 common130、122 TERM、8 controls，加本课own3后133。正文、record、SVG不计支持数量，支持存在不代表课程完成。原作者127清单/首次记录/所有旧审保持原样，后续公共record按当前候选真实pin补齐并保留历史。

新增3个公共术语固定身份：

```json
[
  {
    "sha256": "224443a907deb63876fd9a332584ef6236feb600ecb0807d5f65f7a4e3df4bfa",
    "git_blob": "3278fb1e0041b3a298a8ba5043160e2b7e713c9b",
    "bytes": 2024,
    "mode": "100644",
    "commit": "2a02a363657534dfcb27f1c0030e98533245e7e2",
    "path": "i18n/zh/.curated/stages/S121-real-time-edge/TERMINOLOGY.md",
    "role": "reference_stage_terminology",
    "stage_id": "S121-real-time-edge",
    "support_only_not_course_completion": true,
    "publication_receipt_sha256": "949fd7948374cc229cfd7a7c0573d7e57ae87cd9b38b5e0c61876ee2fd469f81"
  },
  {
    "sha256": "77cc307ef60939900163a8c19fc8a87f2104b2207a19fbf7e0ee7ac503f3abf5",
    "git_blob": "f6e23ac9376aa6fc6f127252aa162fc9ee099777",
    "bytes": 3778,
    "mode": "100644",
    "commit": "9744547f8c13ae9ce9375f40ed3a4260b88e1ffb",
    "path": "i18n/zh/.curated/stages/S122-dialogue-state-tracking/TERMINOLOGY.md",
    "role": "reference_stage_terminology",
    "stage_id": "S122-dialogue-state-tracking",
    "support_only_not_course_completion": true,
    "publication_receipt_sha256": "a680212e816081d94c1ff38fe7d79c2fe8ad4a13262c7c382031043f7b7a30ed"
  },
  {
    "sha256": "5ff55f2ad11b6159a4e765580debb4e4c56311a01ec6b974cad37bd926fc1425",
    "git_blob": "f7357c7558a881fbb7903f39ed144373b2e42601",
    "bytes": 2689,
    "mode": "100644",
    "commit": "16764b99f5a4350eb10080a930f01464ca16c431",
    "path": "i18n/zh/.curated/stages/S123-reviewer-agent/TERMINOLOGY.md",
    "role": "reference_stage_terminology",
    "stage_id": "S123-reviewer-agent",
    "support_only_not_course_completion": true,
    "publication_receipt_sha256": "2f46b36dd8ac1d54bcd12ddc206ba860002faebd6da559c0cb0a77dc3f75349b"
  }
]
```

源先修原文：Phase 14 · 34 (Repo Memory), Phase 14 · 38 (Verification), Phase 14 · 39 (Reviewer)

固定英文先修身份来自已读准备材料；读取范围按作者和独审原证据分别保留，不冒称本次重新全文审读。 只依据固定英文与相关术语即可翻译，不增加中文先修正式验收要求。

冻结源准备时 formal134，INDEX commit 57e6fdd85d87ba64726514e4c4433d3a1d9dca44 / SHA256 7659fc93786f56524138d8525e646f2a2cdb92a0569fef7ac9b98fce357d1673，独立回执 SHA256 7ca593614e44ebe780dd30120dfc3122868f90d3188484041a32511aed8abaff。actual132 运行 2026-10-04T19:24:29.438439+00:00 至 2026-10-04T19:24:41.076837+00:00 / RESULTS SHA256 d307d12f3aec999a804086e8588efe9bb69a04868dcc32b2d9061eec2a4f95fd，不覆盖本3课；不是当前实时计数。旧book5/6与site空锚点/重复项限制保持，不借历史批次声明本课发布通过。

## 作者源风险与有限提案

来源SHA256 59dd89e4342f35b76a8f9befa047577e9054a668526bc8e5ad289715cbc0ff00；CPU提案实际来源SHA256 59dd89e4342f35b76a8f9befa047577e9054a668526bc8e5ad289715cbc0ff00。以下技术事实与提案完整保留；NOT_RUN，提案不等于执行结果。

# S126 源文风险与执行边界

固定英文：1bafaa88bb4668356791150bec3a6d7df38387eb。以下是作者对本课5文件与3个直接英文先修的完整静态阅读发现，不是执行测试，也不对外部时效性声明背书。正文保留源意，没有用译文修复实现。源码、任务、quiz及skill均未修改。

1. **加载器与清理前置条件未实现。** `docs/en.md:75,83–88`、`mission.md:11` 声称加载器和 `clean_state.json` 空阻断列表检查。`code/main.py:19–26,73–92,124–141` 只有 dataclass 和内存样例，没有输入文件加载器、清理器、工作树/提交/stash/分支/HEAD/功能看板检查，也不检查 `clean_state.json`。课文清理命令和规则仅是课程内容，不授权实际清理本工作树。
2. **反馈裁剪不保证小包或30条限制。** `code/main.py:42–53` 保留最后5条以及全部非零退出记录；失败多时可超过 `outputs/skill-handoff-generator.md:25` 的30条限制。按 `id(r)` 对象身份去重，并非按记录内容或稳定记录ID；先发尾部再发较早失败记录，不保持全日志顺序。没有数目上限。
3. **缺失反馈状态不等于安全。** `code/main.py:44,83` 将 `None` 或缺失退出码排除在失败记录之外，若在尾部之外还会被裁掉。`14-38` 英文将空退出码视为阻断级；此代码并未实施该验证关卡的拒绝策略。非零退出测试本身也可能含格式错误的非数字值，缺少schema验证。
4. **其他列表也保留完整历史。** `code/main.py:79–84` 的 `commands_run`、`failed_attempts` 不随 `feedback_tail` 裁剪；即使尾部较小，交接包整体仍可无限增长。失败说明仅有命令和退出码，未说明原因；summary只拼接任务、审查结论与关卡状态（:77），未汇总实际工作内容、改动理由。
5. **缺失字段/报告未严格拒绝。** `code/main.py:74` 对缺失 `next_action` 填入警告字符串，因此“非空”不能保证实际可执行下一步。报告缺失、验证 `passed=False`、阻断发现等不会阻止生成。与skill:17,22,29–31的拒绝要求有差距；也没有会话时长、空diff异常检查。
6. **风险推导容错可能掩盖异常。** `code/main.py:56–69` 对缺失或不可转整数的review total默认10；即使低于7，也只添加warn，不使用审查者的soft/hard fail状态；状态blockers同样统一为warn。转int不是完整schema校验。不能把此输出当成安全或完整验证。
7. **判定结果路径是拼接字符串。** `code/main.py:87–90` 构造 `outputs/verification/<task_id>.json` 和 `outputs/review/<task_id>.json`，不验证文件存在、任务关联或内容。先修14-38/14-39英文演示分别描述把报告写在脚本旁；真实前序产物不自动位于此规范路径。demo内 `pytest`、`ruff`、路径、退出码都是固定样例，不是执行证据。
8. **两种格式与持久化限制。** Markdown呈现七个主要字段，JSON还包含 `task_id` 与 `feedback_tail`；后者没有Markdown对应章节（:97–121）。主函数顺序 `write_text` 写两个文件（:144–145），无原子成对写入、事务、fsync或异常回滚，运行会覆盖脚本目录的 `handoff.md`/`handoff.json`。译文中“两者同源/以JSON为准”不能当成实测一致性或恢复保证。
9. **生产模式仍是设计建议。** docs:106,114–122中的branch/last_known_good_commit/status、一主题一active包、归档、会话结束hook、跨产品加载、PR集成未在main实现；`handoff.schema.json` 与hook是skill要生成的成果，而非本课已经存在的文件。练习中的逐假设评分也不由本课或14-39所述五维总评分直接提供，需扩展数据结构；不擅自给译文补实现。
10. **外部与版本性主张未验证。** docs:102–108及延伸阅读中的Codex端点/AES blob和本地回退、Claude Code五阶段/95%、OpenCode隐藏及5标题摘要、Hermes Issue#20372日期与主张、50-75%经验、过时交接比坏输出更常见等都只作固定源翻译。端点与blob表述本身概念混用；未访问链接、未更新事实。heading的“before 50-75%”与正文“at 50-75%”原样区分，未调成一致。
11. **源格式及课程契约差异。** docs:92为裸围栏，仅译文开头补 `text`，命令载荷不改。包无tests目录。quiz有7题（2pre/3check/2post），与根AGENTS的6题（1pre/3check/2post）不同；多个正确项明显更长，未跑bias检查。skill:35–43还包含裸围栏与Unicode目录树，不是本次译文目标，未改。

## 执行与发布状态

- 原翻译控制 `capture/check/render` 已安全离线执行，日志见 `FIRST-CAPTURE.json`、`LOCAL-CHECKS.json`；这不执行课程main或导入课程模块
- 本课main、import、tests、模型、CPU/GPU示例、API、网络、安装、服务、签名：NOT_RUN
- 仓库全量审计、控制回归、累计回归、真实GitHub GFM、网站、手机、PDF、CI：NOT_RUN；未创建远端分支、提交、PR、INDEX或queue更新
- 如另获授权，有限CPU验证提案是：在一次性隔离目录、无网络和无安装条件下，对裁剪纯函数及生成函数使用少量固定合成输入，覆盖空输入、缺失退出码、31条失败、重复值/重复对象、缺失next_action与验证失败。不得在原课程目录运行main；该提案未执行，不能记作通过


## 独立源边界

```json
[
  {
    "id": "SRC1",
    "severity": "source",
    "detail": "docs/mission声明loader但main只构造内存WorkbenchSnapshot，无四文件磁盘loader。"
  },
  {
    "id": "SRC2",
    "severity": "source",
    "detail": "clean_state.json检查/空列表断言未在main实现；工作树/分支/测试清理条件是源要求非本轮已执行。"
  },
  {
    "id": "SRC3",
    "severity": "source",
    "detail": "trim_feedback保留last5+全部失败，无30条硬上限；skill要求tail<=30可能冲突。"
  },
  {
    "id": "SRC4",
    "severity": "source",
    "detail": "去重按Python对象id而非业务record_id；相同内容不同对象仍重复，先tail后旧失败不是全局时间排序。"
  },
  {
    "id": "SRC5",
    "severity": "source",
    "detail": "commands_run和failed_attempts仍收集全量反馈，只有feedback_tail裁剪，包整体未受界限。"
  },
  {
    "id": "SRC6",
    "severity": "source",
    "detail": "derive_risks对缺失/非法review total默认10，潜在fail-open；对False等int语义、阻断态及expected reviewer未做严格schema校验。"
  },
  {
    "id": "SRC7",
    "severity": "source",
    "detail": "缺next_action使用nonempty needs-human文本，未拒绝；缺verification/review/异常diff等skill拒绝规则未实现。"
  },
  {
    "id": "SRC8",
    "severity": "source",
    "detail": "branch,last_known_good_commit,status生命周期、session-end hook、schema都未实现；不能把生产建议视为demo功能。"
  },
  {
    "id": "SRC9",
    "severity": "source",
    "detail": "输出路径code旁vsoutputs/handoff/session_id为演示/目标区别，verdict_pointer构造outputs/verification/task.json不校验存在。"
  },
  {
    "id": "SRC10",
    "severity": "source",
    "detail": "动态厂商压缩机制/比例/Issue引用未外部核验；仅忠实译源，不新主张事实。"
  },
  {
    "id": "SRC11",
    "severity": "source",
    "detail": "源feature_list引用14-36与scope contracts标题不完全匹配；保留引用，勿自动改编号。"
  },
  {
    "id": "SRC12",
    "severity": "source",
    "detail": "generate_handoff的Markdown没有feedback_tail段但JSON含该字段；七核心字段仍在，不声称所有JSON字段双格式一致。"
  }
]
```

源准备发现（仅读、未代改源）：

```json
[
  {
    "location": "docs/en.md:75,83–88; code/main.py generate_handoff/main",
    "finding": "Docs claim a loader and enforced clean_state precondition; main constructs in-memory stubs and neither loads these files nor checks clean_state/branch/committed changes. Treat cleanup instructions as lesson content, not commands for this preparation."
  },
  {
    "location": "code/main.py trim_feedback/generate_handoff; outputs/skill-handoff-generator.md",
    "finding": "All nonzero failures can exceed the skill30-entry limit. Deduplication uses object identity, tail is emitted before older failures, and missing exit_code is omitted as failure. commands_run/failed_attempts retain full history so packet size is not bounded by feedback_tail."
  },
  {
    "location": "code/main.py generate_handoff/derive_risks/main",
    "finding": "Missing next_action is replaced by a warning string, malformed review total defaults to10, and absent fields are not strictly refused. Canonical verdict paths are only fabricated strings, not checked against actual earlier script-local reports; Markdown omits feedback_tail present in JSON."
  },
  {
    "location": "docs/en.md production patterns; quiz.json; package",
    "finding": "Branch/LKG/status, archival policy, hooks, schema, loader and atomic paired file writes are not implemented. Dated compaction/50–75% claims not externally verified; one bare fence, quiz7(2pre/3check/2post), no tests. Main would overwrite script-local handoff.md/json if run."
  }
]
```

课程 main/import/tests、模型/CPU/GPU、API/网络/安装/服务/签名均 NOT_RUN；本轮不重跑原strict、离线重放、GFM、控制或累计回归。已有局部strict和独审仅按其真实输入哈希复用；own3仍未安装，后续页面、远端内容和适用批次尚待处理。
