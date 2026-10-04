# S129-workbench-for-real-repos English-first 支持范围

状态：本地 own3 候选，未安装、未发布，不增加正式课程数。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；原控制 `f9b5e9cbe4012f54483794f920c0d87b06a7573d`。

## 当前正文与独立审校身份

- Lesson: 14-41
- Current target SHA256: 4628963e911bf89f5485a1678f3d2b17fad52229192ebf71260ea3adfd8efd0d (8572 B)
- Current draft record SHA256: 885cc38a8aedb397d146f557a7d3522480627cc24dee0da06b1d810b614df6c8 (40754 B)
- Historical author handoff SHA256: a56d03c2988cb3d871d6e08d8c369f4a16766f64358149986fb4104bf5faa13e
- Original full independent review SHA256: eecc5cb4227fd2d2864d651240aaa48e8d00d727be2fb1019570ff23e8dd2df4; companion SHA256: 22784d76bbe854775d027cc84a48be8582b23b322a1b057e5c9b4cfdee5c16d6
- Current incremental closure SHA256: 9008a77baa3c8bec9d6f8a04abd79b9fce63313965ae8c56690c35f2ea08942c
- First complete body SHA256: b266a44b47d15f5bcdcc8f4776b7c198033e2ac00a376f3955e5539f03667cd4
- First successful capture record SHA256: ef3c97980b0b8b68b3222d0a49bef48de356dffac59fd6ab091f58d9217c2147
- Current local strict evidence SHA256: d68be961a91abd8c582147356acc9a9eaf0cc8a435b9c40089962dd68acaf971; historical evidence only, not rerun

97块原完整技术与单独中文审读 required_revision 原样保留；R03 只核最后延伸阅读一句，PASS并继承96块原覆盖。旧HANDOFF仍绑定R02，绝不当成R03当前身份。

Preflight 2026-10-04T21:34:15.329629+00:00; first body write 2026-10-04T21:36:03.414266+00:00 to 2026-10-04T21:36:03.445618+00:00; successful first capture completed 2026-10-04T21:36:03.493205+00:00. Three real body/record revisions retained. Revision01 default date correction is record provenance metadata, not source-code modification. Revision02 benchmark terminology adjustment retained. R03 final sentence correction 2026-10-04T21:46:02.752865+00:00 to 2026-10-04T21:46:02.815889+00:00, restoring evaluation-harness referent and plug-in direction. Old full required_revision stays on234e3d43/01173740; current4628963e/885cc38a uses incremental PASS plus96 unchanged blocks.

真实修订身份与时间（同字节快照不计额外修订）：

```json
[
  {
    "revision": "revision-01",
    "before_utc": "2026-10-04T21:37:32.861449+00:00",
    "after_utc": "2026-10-04T21:37:32.885151+00:00",
    "receipt_sha256": "1c2910353274596b6a949c50c10dce3a504cf93dc7d1055c8e6cd3e6a1caa778",
    "old_target_sha256": "b266a44b47d15f5bcdcc8f4776b7c198033e2ac00a376f3955e5539f03667cd4",
    "new_target_sha256": "d766fa49ba5b3922d7b8b397a6ea81437ba0f91659ad14a38c270c7d7d1a2e94",
    "diff_sha256": "d1bc69d4b62b81960f23da3b6c0a2911767b920ff65e653d037c9efb0a9379e0",
    "old_record_sha256": "ef3c97980b0b8b68b3222d0a49bef48de356dffac59fd6ab091f58d9217c2147",
    "new_record_sha256": "c098f54d59699e7e2edc8509e15756b01c786133fd5193b7be22fd8fe2f33e73",
    "record_diff_sha256": "4a8ac5a24828078b3c90e57fe9841a5ab491d0e22c37417d9a5debf2ef6730f3",
    "same_byte_alias_only": false
  },
  {
    "revision": "revision-02",
    "before_utc": "2026-10-04T21:38:34.598760+00:00",
    "after_utc": "2026-10-04T21:38:34.613948+00:00",
    "receipt_sha256": "667b02954fab94631e4803bd9128a5234015313cc0afd7527e4659dd9bcf008f",
    "old_target_sha256": "d766fa49ba5b3922d7b8b397a6ea81437ba0f91659ad14a38c270c7d7d1a2e94",
    "new_target_sha256": "234e3d4389676855620db3e8b9bf8ed102a97f5f89697866e3b5ce869365f6c7",
    "diff_sha256": "92f0625755948269c8641ba6064a65927668be62ff36c0b8799f168c35c60a84",
    "old_record_sha256": "c098f54d59699e7e2edc8509e15756b01c786133fd5193b7be22fd8fe2f33e73",
    "new_record_sha256": "0117374054cf795c586b951e13aee088ba5324993a69791346153d8b26cb264b",
    "record_diff_sha256": "8fc95d67394f2164ea96499e286ecc4c3b286f489a6f2e75a158de3f374305ce",
    "same_byte_alias_only": false
  },
  {
    "revision": "revision-03",
    "before_utc": "2026-10-04T21:46:02.752865+00:00",
    "after_utc": "2026-10-04T21:46:02.815889+00:00",
    "receipt_sha256": "d68be961a91abd8c582147356acc9a9eaf0cc8a435b9c40089962dd68acaf971",
    "old_target_sha256": "234e3d4389676855620db3e8b9bf8ed102a97f5f89697866e3b5ce869365f6c7",
    "new_target_sha256": "4628963e911bf89f5485a1678f3d2b17fad52229192ebf71260ea3adfd8efd0d",
    "diff_sha256": "a6fecbc1ce949bb60ccc3762a21ab237fb193ca20bc7117dab2aaaa801a33364",
    "old_record_sha256": "0117374054cf795c586b951e13aee088ba5324993a69791346153d8b26cb264b",
    "new_record_sha256": "885cc38a8aedb397d146f557a7d3522480627cc24dee0da06b1d810b614df6c8",
    "record_diff_sha256": "49ecf277de4e08554973c7b002941d5bb7524d2a1b42ab3714b98ebd78dbcf79",
    "same_byte_alias_only": false
  }
]
```

## 固定支持与先修边界

原作者 common130 清单 SHA256 e51d3368dbe2c835265c058c21c0755c12391d520b55cd2bbe81dc5ef9842222，122 TERM +8 controls；S117 已绑定 ff4d56e72126e854321b5d95a7c43a8b57a485bf / 6631ae3d6b514d374a63bd21afa98eaedeb995e2aeed3e664e037e6de6ea0c85，不需要旧pin overlay。既有130项身份、顺序、角色和分类保持，公开投影仅移除54个私有定位值。

候选只追加 S124–S126 三个已真实发布且独立完整回读的TERM：当前 common133、125 TERM、8 controls，加本课own3后136。原作者common130、首稿、所有record和旧审原样保留；后续公共record才绑定真实已发布own3。支持存在不表示课程完成。

```json
[
  {
    "sha256": "9988ab24148ee475e13088f7dddb2f168fc41691d30a38064edc8f47b08b06bc",
    "git_blob": "1f33813c653af239b721d58cdeedf8c14deebe6b",
    "bytes": 3441,
    "mode": "100644",
    "commit": "2d669fb077200f418bd394dbe6607d4b462aa92b",
    "path": "i18n/zh/.curated/stages/S124-vision-pipeline-capstone/TERMINOLOGY.md",
    "role": "reference_stage_terminology",
    "stage_id": "S124-vision-pipeline-capstone",
    "support_only_not_course_completion": true,
    "publication_receipt_sha256": "cc07313595a0cb93318a479d266f5536455ca1f4c097af396e1d1d890c432db9"
  },
  {
    "sha256": "33a598835fa1d3a77025cdf1735aea6ff87ff3e4f2dbd4b1449a245099ec40f3",
    "git_blob": "8e6e6486d71743b5ea9f6872e9b67afff0d962c0",
    "bytes": 3022,
    "mode": "100644",
    "commit": "647571e1c10741600cf60a72ee7cad8d0f1e0836",
    "path": "i18n/zh/.curated/stages/S125-audio-classification/TERMINOLOGY.md",
    "role": "reference_stage_terminology",
    "stage_id": "S125-audio-classification",
    "support_only_not_course_completion": true,
    "publication_receipt_sha256": "d6b417bc3063fbae2bbbdfef0ef75eeb7fd36b43345b40f5e5ec15a228c72aeb"
  },
  {
    "sha256": "0798cee6881f485da35c7cff4fbed7607aaa4f3226c075fcf9604261d8d0fe66",
    "git_blob": "777e8d4129b04b50951d5cc0187022687e1a71c8",
    "bytes": 2094,
    "mode": "100644",
    "commit": "6020bfcdce9ae76125147c11e98ac3c8158f7fb5",
    "path": "i18n/zh/.curated/stages/S126-multi-session-handoff/TERMINOLOGY.md",
    "role": "reference_stage_terminology",
    "stage_id": "S126-multi-session-handoff",
    "support_only_not_course_completion": true,
    "publication_receipt_sha256": "9ae16e13ddb1a81ea1d75256a4bb87c79c03d11f2abf5c0cb5e58d692a126bfe"
  }
]
```

源先修原文：**Prerequisites:** Phases 14 · 32 to 14 · 40

仅以固定英文及相关术语为翻译前提，不增加中文先修正式验收门槛。作者与审校者的亲读和固定既有英文全文证据复用各按原报告保留，不冒称本轮重新全文阅读所有先修或所有术语。

冻结源准备时 formal136，INDEX commit d93dcd48f5d24a0dec7bfac2de9230ab1c098fdb / SHA256 cd532f05d6cff2133b5a418167a1e08e2f59779679350b618a41167a5082b593，独立回执 SHA256 32000870ed2c3bb0934fb30cab1374737e6a5a2d0bbff271ca0beb91c388145a。actual135 运行 2026-10-04T20:38:42.005823+00:00 至 2026-10-04T20:38:53.725717+00:00，RESULTS SHA256 9fb594aa0d6c417666f579729ca0f3c93b5bff6abff693f8058309434ac3982b，不覆盖本3课；这不是当前实时计数。历史 book5/6及site43空锚点限制保持，不借旧批次声称本课发布通过。

## 作者源风险与有限提案

源风险实际文件 SHA256 3469203051bce7dea745ed48f864c17e8c7f10a991d9e373ad034c582acb1153 (3510 B)；CPU提案实际文件 SHA256 3469203051bce7dea745ed48f864c17e8c7f10a991d9e373ad034c582acb1153 (3510 B)。以下技术事实和提案保留；CPU状态NOT_RUN，提案不是执行结果。

# S129 固定英文源风险与运行边界

本课固定英文：1bafaa88bb4668356791150bec3a6d7df38387eb，docs/en.md SHA-256 75d2298297ec8a23832dea06df7e12a448e1030b265465aac178dc914b881d27。以下来自完整静态阅读，不是运行结果；不在中文正文里修复英文，不改 code/quiz/mission/outputs。

1. 五项结果不是测量值。code/main.py:52–75 的 run_prompt_only/run_workbench 直接构造 TaskOutcome，tests_actually_run、acceptance_met、handoff_quality、reviewer_total 均为常量；files_outside_scope 仅对硬编码 touched 列表做允许集合筛选。没有真实编辑、运行测试、验收命令、反馈运行器、验证关卡、审查者或交接包生成。docs b0049、mission Acceptance、报告叙述比实现强，不能把翻译 PASS 或脚本输出当作实际工作台收益证据。
2. 样例与路径边界。code/main.py:19–35 是普通 Python 函数，直接保存未校验的明文 password；没有 FastAPI 导入、HTTP 路由、422 或带类型信息的错误封装。样例仅在 main 调用 write_sample 后创建。FORBIDDEN 未使用；touched 中 README.md 与生成的 sample_app/README.md 也不一致。真实代码并未执行路径策略或安全检查。
3. 会覆盖文件。write_sample 与 write_report 将覆盖脚本旁的 sample_app/*、before-after-report.md、comparison.json。本次没有运行，没有创建这些课程输出。不能在既有用户代码仓库直接演示后宣称无破坏。
4. 外部数值断言未核验。Terminal Bench 排名、Vercel 的 80%→100%/删除80%、Harvey 2x/两倍以上、88%、WebAgent 40-50%→低于10%、131k/30天以及2026年月均仅忠实保留固定源说法。来源链接未联网打开。前30名之外到第五名不能由此推得恰好二十五位；标题 Top-30 与正文 outside top30 的差别亦原样保留。
5. 数量与文档契约。导语 eleven lessons 与显式先修14·32–14·40九课不一致；正文保留“十一课”。quiz 有7题（2 pre/3 check/2 post），不符合根 AGENTS 的6题约定；没有 code/tests。不能报课程测试PASS或补造缺失测试。
6. 交付物的能力范围。outputs/skill-workbench-benchmark.md 是要求生成 portable harness、CI、延迟与false-negative评测的文本，并没有提供这些实现。main 无计时、真实LLM、离线能力验证或回归评测。中文保留“评测框架”源表述；不据此声称可直接部署。
7. 图示与呈现。正文有一段 Mermaid、一个 figure ID wb-ab-runs，无相对 SVG。载荷保持；本轮没有真实 GFM/站点/移动/PDF 渲染。原命令围栏仅按既有许可补 text，不新增 strict 例外。
8. 语境性术语。false negative 在源文中特指“仅用提示词更快”的对照任务，并非分类器漏报统计；second-day task 未正式定义，译文保留第二天语义，未扩写为已实现的运维流程。

## CPU 限定提案：NOT_RUN

仅供协调者另行决策；本作者没有执行课程 main/import/tests。若需要验证序列化和输出形状，可以在独立临时目录放置本课固定副本，确认不会覆盖已有成果，以10秒超时、离线、无模型/API/安装/GPU运行 python3 code/main.py。可检查退出码、JSON字段和报告文件；这只能说明脚本输出机制能运行，不能证明五项结果是实测、测试已执行、工作台优于提示词或安全边界有效。没有原测试套件可运行，不新增声称“课程测试通过”。


## 原独立审校保留的源边界

```json
[
  {
    "id": "SR1",
    "location": "code/main.py:52–75;docs/en.md:82;mission.md:15–18",
    "finding": "五结果为常量与硬编码touched集合筛选，非实测；没有真实编辑、测试/验收、feedback runner、gate、review或handoff。译文忠实，不是行为证据。"
  },
  {
    "id": "SR2",
    "location": "code/main.py:19–35,48–49,54,67,102–108",
    "finding": "普通Python保存未校验明文密码；无HTTP/FastAPI/422/error envelope；FORBIDDEN未用，README touched路径不一致，声明不是实际边界。"
  },
  {
    "id": "SR3",
    "location": "code/main.py:99,102–108,122–125",
    "finding": "运行会写/覆盖脚本旁sample_app与报告/JSON；本审不运行。"
  },
  {
    "id": "SR4",
    "location": "docs/en.md:94–108,144–148",
    "finding": "2026外部数值与归因未联网核实；outside top30到第5不能推出恰好25名，标题/正文差异原样保留。"
  },
  {
    "id": "SR5",
    "location": "docs/en.md:3,7;quiz.json;code/",
    "finding": "十一课与32–40九门先修不符；7题2pre/3check/2post偏离六题规范；无code/tests，不报测试PASS。"
  },
  {
    "id": "SR6",
    "location": "outputs/skill-workbench-benchmark.md:10–31;docs/en.md:122",
    "finding": "技能文本是生成要求，没有通用评测框架/CI/计时/真实LLM/离线与false-negative评测实现。"
  },
  {
    "id": "SR7",
    "location": "docs/en.md:90;code/main.py:116–120",
    "finding": "console table源描述与实际逐字段打印不完全一致，不静默修中文。"
  },
  {
    "id": "SR8",
    "location": "docs/en.md:106,127–128,139",
    "finding": "false negative为特殊任务语境；second-day task未正式定义，译文保留限制不新增解释。"
  }
]
```

固定源准备发现，未暗改源：

```json
[
  {
    "where": "code/main.py run_prompt_only/run_workbench; docs/en.md Build/mission",
    "finding": "Five outcomes are hardcoded dataclass values; no app modification, acceptance/test execution, feedback runner, gate, reviewer or handoff generation occurs. Scripted constants demonstrate report shape rather than measure the claimed pipeline comparison; no runtime PASS inferred."
  },
  {
    "where": "code/main.py write_sample/write_report; docs/en.md sample app",
    "finding": "Sample app is generated only on main, plainPython signup stores unvalidated passwords and is not FastAPI or routedHTTP. Forbidden set is unused; touched paths are declared lists. Running would overwrite sample_app and reports next toscript; no existing sample_app or real benchmarks were run."
  },
  {
    "where": "docs/en.md productionpatterns/opening; outputs; quiz",
    "finding": "Externalrank/success/88%/long-context claims and exact25-rank conclusion remain unverified; eleven lessons differs from explicit32–40 range ofnine. Portable harness/CI/latency/false-negative evaluation are requested output patterns, not implemented. Quiz7(2pre/3check/2post), no tests, bare fence; preserve source meaning."
  }
]
```

课程main/import/tests、模型/CPU/GPU、API/网络/安装/服务均NOT_RUN；本轮不重跑strict、离线重放、GFM或累计回归。记录默认日期更正只是作者record元数据修订，不改源代码或冻结检查器。后续页面、远端内容及适用批次仍分别验收。
