# S100-instance-segmentation-mask-rcnn English-first 支持范围

状态：本地 check-only own3 候选，未安装、未发布，不增加正式课程数。当前正文已有独立完整技术/中文语言 PASS；该结论只绑定下列正文版本，不代替支持安装、真实 GFM、远端字节核验或适用批次回归。

## 固定英文与唯一目标

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Source tree: `3d90647a3449a7b228a6b6025ed2b333ef99e81c`
- Lesson: 04-08
- Canonical docs H1: Instance Segmentation — Mask R-CNN
- Source: `phases/04-computer-vision/08-instance-segmentation-mask-rcnn/docs/en.md`
- Source Git blob: `2516968ed3638bf89924cdf5a5ac842307cfae9c`
- Source SHA256: `b7ced123dcc47406affd5cc13916ffb6954f8417a29d8b99526c61ec97a4168b`
- Target: `i18n/zh/phases/04-computer-vision/08-instance-segmentation-mask-rcnn/docs/zh.md`
- Eventual record: `i18n/zh/.curated/lessons/04-08/translation.json`
- Original core blocks: 139
- English prerequisite line: **Prerequisites:** Phase 4 Lesson 06 (YOLO), Phase 4 Lesson 07 (U-Net)
- Actual first write UTC: 2026-10-04T12:36:37.972663+00:00 through 2026-10-04T12:36:37.972894+00:00
- First-write receipt SHA256: `a8477ae6fc55a1a7620fbeb20afb6d05521b7aca664c4ac3a0cf872635d47106`
- Original complete first draft: 15422 bytes, SHA256 `c9cc1835d348d72eaef6db1fbe546edd1a1973b6e2150156dae5cc4dc2007645`
- Current reviewed target: 15446 bytes, SHA256 `07012e2029bbccda65d05dbca5e873b82295d4f131214906c524d8ab6ba44075`
- Current draft record SHA256: `ce96bca87bf5559e7555adb1d7921feb9ba05e78bbdb0c2ed166f10b188cdff4`
- Independent language review SHA256: `f83b69fb359fa2b1db6cfda6021725ece0f13d2349e92f3e67be9debe55b38fc`
- Existing local strict receipt SHA256: `3d5ec0429fb792098c3f85ee7e9c8541203c84234f3520caf9d70ece9c2abd9b`

首写按原回执和原字节核对，不用 mtime 重建，不倒推为当时独审或完整支持绑定已经通过。本课包源身份见 DEPENDENCIES.source_files；先修英文为 04-06, 04-07，没有先修中文 formal 门禁。

## 固定支持与当前溯源

共同准备清单 SHA256 `77791cbf3d18671859db330f107b2d64fcb138a37287707ad51bd1a360718d82`，引用原103 pin清单 SHA256 `aa1ce658c805ba06f4b25859601ecd36f9bd3cdd622d075d7a56b360d295d8b6`。files/support_pins保留原103全部身份和顺序，reference_glossary_pins仅95 TERM；8 controls、own3分计。own3只含本阶段 DEPENDENCIES.json、SCOPE.md、TERMINOLOGY.md；未来安装后总106。target/record、兄弟阶段和非支持资产不进入own3。保持历史role/classification，不复制后续共同清单的新归类。

当前as-of采用正式独立回读真实时间 2026-10-04T12:55:32.520157+00:00：正式已审草稿114，INDEX commit `19db65d17eca63e7716fe5e10028bf82fa44c309`、SHA256 `332a1eb6a5a5003b78940290084f7337a3a9fa5afd5f76c63f26c86f26f2c17f`；独立回读凭据 SHA256 `cb33fc7a548110448fbe1ef68027657482f4a22ac04a43495d25907ed49c2fcd`。最新实际批次114只新增覆盖 S96/S92/S94，不覆盖 S100/S101/S102；本课适用批次仍待运行。当前溯源不改作者首写、共同准备113或原pin清单107/108的历史时点。

保留 schema_version=1、DEPENDENCIES version=1、原 f9 core及既有 S07/S19 精确控制，不新增 loader、checker 例外、发布框架或 current-support 重分类表。own3 hash由外部manifest固定，无自引用。原33 fixture仅复用固定身份，不读其中文body/segments、不安装到作者目录、不重跑33/24/50。

## 已有证据与实际限制

- “四项损失”与完整五项公式并存；正文称技能支持任意 torchvision 检测模型，实际输出仅支持两种 Mask R-CNN。均为源问题，不改译文含义或产物范围
- 固定 quiz 五题、无 code/tests；文档 torch.linspace 未传 device 而程序传入 device。没有补题、补 tests 或同步修改源码
- RoIAlign 的宽泛模型适用断言、损失权重构造参数、梯度/边界等价、冻结参数与运行状态、46M/91 类标签、500 图像经验阈值等未作外部版本验证；不能据本次翻译背书
- 无正文相对 SVG。原作者离线 parser 的 13 个纯中文标题空锚点属于站点限制，非真实 GFM 结果；figure 和 Mermaid 原载荷保留
- CPU RoIAlign 三组小张量方案仅为提案：NOT_RUN，未获执行 GO。源准备的 30 秒与作者后续提案的 60 秒/2GiB 是不同历史提案，未选定/合并为已授权上限。绝不运行 main、模型构造、权重下载、训练、GPU或安装

## 核验与发布边界

本准备只做新候选JSON/字节/hash、当前作者绑定/首写原字节、17个本课包文件及6个先修英文必要Git pin核对；95术语表校准与原共同commit身份复用固定证据，不宣称本轮再次解析全部共同commit。S85–S96 commit:path在准备时对象库不可解析的既有限制保留，未联网补取。没有全源5423扫描，没有课程运行、模型、main/tests、下载、安装、GFM/site/mobile/book/CI或回归执行。

只生成候选，不写作者、原支持、英文源、INDEX、queue或远端。建议分支 `zh/stage-100-instance-segmentation-mask-rcnn` 仅为名称，未查或创建。publication pending/null仅表示冻结时未发布；后续发布须绑定真实提交及独立完整字节回读。语言PASS、静态PASS和正式114背景均不转化为本候选的发布或批次通过。

S100历史追认：原独审 REQUEST_CHANGES 报告SHA256 `d74fe5a423269bb92b0bc8d5b32da288b5fc111fcb9eada3e17b6f6f6b970e1d` 保留；005仅补 quantisation 首现及恢复唯一限定，REREVIEW-005关闭两项。原HANDOFF的旧正文/record hash不再作为当前绑定，005补充及上述新hash才是当前依据。95TERM校准中较早target hash是历史快照，不静默换成最终hash。
