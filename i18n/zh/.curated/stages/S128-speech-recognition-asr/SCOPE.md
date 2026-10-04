# S128-speech-recognition-asr English-first 支持范围

状态：本地 own3 候选，未安装、未发布，不增加正式课程数。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；原控制 `f9b5e9cbe4012f54483794f920c0d87b06a7573d`。

## 当前正文与独立审校身份

- Lesson: 06-04
- Current target SHA256: 6221ffe50ebbd3978187c32a5533c402ff773bc6c1d5be54f22549394e3f97f8 (10713 B)
- Current draft record SHA256: 2e051c19c1ae6ce4d1cc9613676af68d97a50004a7d5c688899fd23dbdf6773f (46030 B)
- Historical author handoff SHA256: a16194a26c51c7b2826f9c1b6396ad6d46755348172c41cbdbe756b148eb063a
- Original full independent review SHA256: 117916387af6d970701cf444d528765bd327a3fef546e301286ef045c0827f76; companion SHA256: b131dbd5de78a22508ecf8f9e02a3624fe57d1cc460f148107d510ba00b0a30e
- Current incremental closure SHA256: not applicable; full review binds current bytes
- First complete body SHA256: 1051e0f68b5a7f6e8ddb7f0cd92d3927529440b479f236393a6f5b803cbfdc21
- First successful capture record SHA256: c2bef7ed7ae3382b23e3b8e685187b39ced9b426584459748184308909f2d8af
- Current local strict evidence SHA256: 30cf5daf798d22a054da4e304647274064023d27b84540b34d56a1fa3963b141; historical evidence only, not rerun

97块独立完整技术与单独中文审读通过；一次真实修订与首capture成功保留，原SVG5660字节保持，仅静态保护不宣称视觉通过。

Prewrite 2026-10-04T21:32:23.142136+00:00; full first draft written 2026-10-04T21:34:28.092552+00:00, no separate before-write timestamp. First capture succeeded 2026-10-04T21:34:44.861788+00:00 to 2026-10-04T21:34:44.921617+00:00. One actual body/record revision 2026-10-04T21:35:57.936725+00:00 to 2026-10-04T21:35:57.940404+00:00; original capture default date correction changes provenance metadata only. Final6221ffe5/2e051c19 and original5660-byte SVG independently reviewed; no subsequent body revision.

真实修订身份与时间（同字节快照不计额外修订）：

```json
[
  {
    "revision": "revision-01",
    "before_utc": "2026-10-04T21:35:57.936725+00:00",
    "after_utc": "2026-10-04T21:35:57.940404+00:00",
    "receipt_sha256": "2f73628225eee6ba7d5991ec9b3478f35c945f8c23ebcce870495422eb11529f",
    "old_target_sha256": "1051e0f68b5a7f6e8ddb7f0cd92d3927529440b479f236393a6f5b803cbfdc21",
    "new_target_sha256": "6221ffe50ebbd3978187c32a5533c402ff773bc6c1d5be54f22549394e3f97f8",
    "diff_sha256": "6b0bb16000cba1132742f8129006c2653e38cb4b19005ea28a5548d5043d10bb",
    "old_record_sha256": "c2bef7ed7ae3382b23e3b8e685187b39ced9b426584459748184308909f2d8af",
    "new_record_sha256": "2e051c19c1ae6ce4d1cc9613676af68d97a50004a7d5c688899fd23dbdf6773f",
    "record_diff_sha256": "4458350db6f2871b7c7fe03b8dbac0ae720f060e86cf7408ec862d3b2bd47b12",
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

源先修原文：**Prerequisites:** Phase 6 · 02 (Spectrograms & Mel), Phase 5 · 08 (CNNs & RNNs for Text), Phase 5 · 10 (Attention)

仅以固定英文及相关术语为翻译前提，不增加中文先修正式验收门槛。作者与审校者的亲读和固定既有英文全文证据复用各按原报告保留，不冒称本轮重新全文阅读所有先修或所有术语。

冻结源准备时 formal136，INDEX commit d93dcd48f5d24a0dec7bfac2de9230ab1c098fdb / SHA256 cd532f05d6cff2133b5a418167a1e08e2f59779679350b618a41167a5082b593，独立回执 SHA256 32000870ed2c3bb0934fb30cab1374737e6a5a2d0bbff271ca0beb91c388145a。actual135 运行 2026-10-04T20:38:42.005823+00:00 至 2026-10-04T20:38:53.725717+00:00，RESULTS SHA256 9fb594aa0d6c417666f579729ca0f3c93b5bff6abff693f8058309434ac3982b，不覆盖本3课；这不是当前实时计数。历史 book5/6及site43空锚点限制保持，不借旧批次声称本课发布通过。

## 作者源风险与有限提案

源风险实际文件 SHA256 b7f7dfa343910c8c856dc4ef25e24572536141bb080562851b40f8a16e1211ee (3800 B)；CPU提案实际文件 SHA256 b7f7dfa343910c8c856dc4ef25e24572536141bb080562851b40f8a16e1211ee (3800 B)。以下技术事实和提案保留；CPU状态NOT_RUN，提案不是执行结果。

# S128 固定英文源风险与未运行事项

本文件只报告静态阅读发现。未执行、导入课程 main 或测试；未调用 ASR 模型、音频下载、GPU、API、网络或安装。翻译忠实保留固定源，不修订其算法、数据、版本、数值、断言强度或可执行载荷。

1. CTC 束搜索并非完整 prefix CTC。docs/en.md Step 2 只对候选路径排序，未对相同输出前缀正确合并概率；main.py 虽按输出序列合并概率，但仍没有分别跟踪 blank/nonblank 前缀状态。blank 之后与前缀末 token 相同的字母仍不追加，故可能吞掉 hello 的第二个 l。main 本来就打印此警告；源文件未经改动，警告保留。译文保留“概念框架”和练习中要求正确处理 blank 合并的语气，没有把它说成完整正确算法，也未把 main 的额外警告私自添加进正文。
2. main.py 的 corrupt 函数直接减加 swap_strength，可能产生负值或大于 1 的值，没有恢复概率约束。ctc_beam 中 log(max(pi, 1e-10)) 截断不能等同概率归一化；doc 的 frame_logits 实际按概率向量使用。正文代码和命名原封不动，不悄悄执行 softmax 或改名。
3. main.py 手写 exp/log 概率合并在长序列中可能下溢，未使用稳定的 log-sum-exp。这里只静态指出，不宣称已构造或跑过复现。
4. 空参考 WER 策略不同：doc 在 max(1,len(r)) 上作除法，空参考、非空候选时可返回候选词数；main 空参考、非空候选一律返回 1.0。两者都未实现正文建议的转小写/去标点。保持差异，不能将规范化建议当成辅助函数现有功能。
5. CTC 的零前瞻/流式能力和 RNN-T 的流式能力仍受编码器未来上下文约束。固定源未完整说明该条件。Step 5 的 streaming_audio 未定义，循环逐块调用通用 pipeline 本身不构成带跨块状态的流式 ASR 实现。译文保留源末段对分块注意力/跨块状态的要求，不声称此循环已满足。
6. 2026 SOTA、WER 1.40/1.58 等、模型排名/大小、最高质量、24 GB 与 ~20× 实时、移动端延迟、推荐模型/API 和库支持情况均未联网核实。WER >20% 的可用性及 <5% 的人类水平也依语料与场景而定。译文如实保留源的时间、数字和断言，未把源表常量写成实际测量结果。
7. 源以 CTC loss“对齐求和”、WER“对应词级 Levenshtein 距离”、RNN-T“CTC＋predictor”等作教学简写，省略严格损失/归一化定义。译文维持源简写，不扩成新的数学推导或暗修。
8. 相对 SVG 已复制原字节，source/target SHA 都是 11785fe8282cd0cdd573ee4ffef0836b7fee0bceb1a41a46a95cb0a50819e20d。仅完整静态读取 XML，没有进行视觉渲染；图中长标签是否溢出、GFM 是否展示自定义 figure，待后续真实页面检查。
9. 固定包没有 quiz、tests 或 Learning Objectives。未添加这些章节或声称有对应测试通过。

## 可供后续授权的有限 CPU 提案，状态均 NOT_RUN

- 仅以独立、短小、纯标准库测试样例验证贪心折叠顺序：a a _ _ a b b _ c 应为 aabc；重复字母必须由 blank 分开保留。
- 对已明确标注的简化 beam 构造有限反例，比较有无 blank 前缀状态；不得以结果修补当前固定译文代码。
- 在不导入课程模块的隔离短程序中对空参考、完全匹配、单替换/删除/插入的 WER 约定作对照。
- 若未来另获执行许可，需先约定超时与输入上限，不下载语料、模型或依赖，不访问 GPU/API/网络。不运行本课 main，不将排行榜常量当 benchmark。

独立语言审校、真实 GFM/SVG 桌面检查、远端完整回读、累计回归、网站/手机/PDF/CI 均不属于本次已通过项目。


## 原独立审校保留的源边界

```json
[
  {
    "id": "SR01",
    "scope": "fixed-source algorithm limitation",
    "segments": [
      "06-04:b0053",
      "06-04:b0055",
      "06-04:b0089"
    ],
    "source_location": "docs/en.md:76-92,163-165; code/main.py:ctc_beam/main",
    "finding": "文中 beam 只排序候选且不正确合并同前缀概率；main 虽聚合相同输出序列，仍无 blank/nonblank 前缀状态，可能吞掉 hello 的第二个 l。main 原有警告保留。",
    "disposition": "仅单列；不修改固定算法，不把概念框架或练习修复要求写成算法已正确。"
  },
  {
    "id": "SR02",
    "scope": "fixed-source metric convention difference",
    "segments": [
      "06-04:b0035",
      "06-04:b0059",
      "06-04:b0081"
    ],
    "source_location": "docs/en.md:40,96-113,153; code/main.py:wer",
    "finding": "文中 max(1,len(r)) 使空参考且非空候选返回候选词数，main 则返回 1.0；两个函数均未实现正文所要求的转小写/去标点。",
    "disposition": "差异准确保留；规范化建议不能视为 helper 已实现的能力。"
  },
  {
    "id": "SR03",
    "scope": "fixed-source probability/numerical limitation",
    "segments": [
      "06-04:b0047",
      "06-04:b0053"
    ],
    "source_location": "docs/en.md:59-90; code/main.py:corrupt/ctc_beam",
    "finding": "corrupt 直接加减 swap_strength 可产生负值或大于 1 的值且不归一化；log(max(pi,1e-10)) 不是修复概率约束；main 的 exp/log 合并长序列可下溢。frame_logits 实按概率输入。",
    "disposition": "仅静态阅读发现，未运行复现，未改变量名或添 softmax。"
  },
  {
    "id": "SR04",
    "scope": "fixed-source streaming/model support limitation",
    "segments": [
      "06-04:b0013",
      "06-04:b0023",
      "06-04:b0025",
      "06-04:b0027",
      "06-04:b0029",
      "06-04:b0031",
      "06-04:b0067",
      "06-04:b0069",
      "06-04:b0071"
    ],
    "source_location": "docs/en.md:16-36,126-135; assets/asr-formulations.svg",
    "finding": "CTC/RNN-T 的可流式与零前瞻受编码器未来上下文约束；逐块 pipeline 循环含未定义 streaming_audio，也不展示状态承接。库/模型 API 支持未核实。",
    "disposition": "保留固定源和末段跨块状态要求；不背书为可直接运行的流式实现。"
  },
  {
    "id": "SR05",
    "scope": "fixed-source dated performance/generalization claims",
    "segments": [
      "06-04:b0015",
      "06-04:b0031",
      "06-04:b0035",
      "06-04:b0037",
      "06-04:b0039",
      "06-04:b0065",
      "06-04:b0077",
      "06-04:b0097"
    ],
    "source_location": "docs/en.md:20,36,40-49,124,141-148,184-185; code/main.py; assets/asr-formulations.svg",
    "finding": "2026 排名、WER、参数量、离线最佳、24 GB/~20×、<500 ms 选型、榜首及 25+ 动态模型数量均未联网核实；20%/5% 可用性/人类水平依语料场景而定。",
    "disposition": "原数字、名称、年份、断言强度忠实保留；它们不是本次 benchmark 或推荐验证结果。"
  },
  {
    "id": "SR06",
    "scope": "fixed-source pedagogical simplification",
    "segments": [
      "06-04:b0021",
      "06-04:b0025",
      "06-04:b0035",
      "06-04:b0093"
    ],
    "source_location": "docs/en.md:26,30,40,171-174",
    "finding": "CTC loss 对齐求和、RNN-T 联合分布与 CTC+predictor、WER 对应 Levenshtein 等为教学简写，未给完整负对数/条件分布/归一化表述。",
    "disposition": "不以译者身份补推导或暗修定义；与明确中译错误分开。"
  },
  {
    "id": "SR07",
    "scope": "rendering/release gate outside review",
    "segments": [
      "06-04:b0019",
      "06-04:b0041"
    ],
    "source_location": "docs/en.md:24,51-53; assets/asr-formulations.svg",
    "finding": "SVG XML 及 figure 载荷只作完整静态阅读和字节保护核验；长标签实际布局、GFM 图示、网站渲染均未观察。",
    "disposition": "后续页面检查继续独立；语言通过不等于视觉、远端、累计回归或发布通过。"
  }
]
```

固定源准备发现，未暗改源：

```json
[
  {
    "where": "docs/en.md CTC beam; code/main.py ctc_beam/main",
    "finding": "Simplified beam lacks blank/nonblank prefix states, so repeated letters separated by blank can be lost. main explicitly warns about this; preserve warning. Doc beam and main differ in probability aggregation; neither is full prefix CTC."
  },
  {
    "where": "code/main.py corrupt/ctc_beam/wer; docs/en.md WER",
    "finding": "corrupt can create negative or >1 values without normalization, then log clamps them. Manual exp/log addition can underflow for long sequences. Empty-reference WER policy differs between prose snippet and main; normalization recommended in prose is not performed by either helper."
  },
  {
    "where": "docs/en.md streaming/model tables; assets/asr-formulations.svg",
    "finding": "CTC/RNN-T streamability depends on encoder lookahead; generic pipeline loop is not stateful streaming implementation. DatedWER/ranking/model/API/real-time claims are unverified. SVG is protected for later actual visual review; no quiz/tests/learning-objectives section in fixed package."
  }
]
```

课程main/import/tests、模型/CPU/GPU、API/网络/安装/服务均NOT_RUN；本轮不重跑strict、离线重放、GFM或累计回归。记录默认日期更正只是作者record元数据修订，不改源代码或冻结检查器。后续页面、远端内容及适用批次仍分别验收。
