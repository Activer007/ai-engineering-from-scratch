# S125-audio-classification English-first 支持范围

状态：本地 own3 候选，未安装、未发布、不增加正式课程数。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；原控制 `f9b5e9cbe4012f54483794f920c0d87b06a7573d`。

## 当前作者与独立审校身份

- Lesson: 06-03
- Target SHA256: aa29f35ac040b2c7cb800ae42c9b7a767086ca7ed0a51857f897c28fe543536a (10399 B)
- Original author record SHA256: de7355a55368746e7fb073f8c40937c5e25bc71b3ba00ff402a7766397cb7dcf (48585 B), status=draft
- Author handoff SHA256: 999372e7a4ab5a1161e9d83d25cd7331dfe237a00f6f62e0c9a3b7692ef76a10
- Original independent review SHA256: ed45de255e04e42bc3047629b97a653726e333777806b25bb1250e75aedc0927; companion SHA256: 43a652e94b5f0727ce4f7bfe8e5d95cde798525bd199a7eab9c5db45e86a2ef3
- First complete body SHA256: 837440403ce84273e34182922e20cbacf3116cf998d9b4df0687f7d468fb2c9c
- First-body record SHA256: null; no record fabricated
- Original local strict evidence SHA256: f83baef7f4b3ade55766b7975a8895472928fd0227a2f96b4938b929748ae0f0; cached evidence only, not rerun

95块完整独审，最终aa29f35正文/de735记录；03-06编号与CNNs标题错配保持源事实，原SVG受字节保护。

Preflight 2026-10-04T20:50:28.247951+00:00; first body recorded 2026-10-04T20:52:43.426023+00:00. First capture failed by 2026-10-04T20:52:43.480421+00:00: repeated F1 number token, no first record. Three actual revision events retain exact start/end: revision01 body repair and first successful capture; revision02 record-only provenance/TERM/SVG binding with unchanged551b body; revision03 final body/record aa29f35/de735. The intermediate body is not the final independently reviewed body.

首capture真实exit1，首record保持null；revision01首次成功capture，revision02仅record元数据，revision03最终正文+record。共3事件、2正文修订，不把中间551b稿当最终aa29f35。

真实修订身份与时间（同字节快照不计额外修订）：

```json
[
  {
    "revision": "revision-01",
    "before_utc": "2026-10-04T20:53:17.859265+00:00",
    "after_utc": "2026-10-04T20:53:17.913898+00:00",
    "receipt_sha256": "f72e02947580cc7ea6ffe20eb6a96afebd536c32233dc90422713083cd090bbe",
    "old_target_sha256": "837440403ce84273e34182922e20cbacf3116cf998d9b4df0687f7d468fb2c9c",
    "new_target_sha256": "551bce1408fd286420581e212f70ee1d87f0cf24770cd174ac7a708ccf65f214",
    "diff_sha256": "301f32269d6513b66c6a5510068d1dec6ffa1a2e6e30cbade5ba7afd868ba3f8",
    "old_record_sha256": null,
    "new_record_sha256": "66e886f9e3bc787a7e0a96cad1037474ffe8d4be760ebc2be8a78e602f181640",
    "record_diff_sha256": null,
    "same_byte_alias_only": false
  },
  {
    "revision": "revision-02",
    "before_utc": "2026-10-04T20:54:02.559575+00:00",
    "after_utc": "2026-10-04T20:54:02.564417+00:00",
    "receipt_sha256": "93fd9c6c5df7c84b09059bfe6812148c3531b4ba3c30d33288fb72b79c781163",
    "old_target_sha256": "551bce1408fd286420581e212f70ee1d87f0cf24770cd174ac7a708ccf65f214",
    "new_target_sha256": "551bce1408fd286420581e212f70ee1d87f0cf24770cd174ac7a708ccf65f214",
    "diff_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "old_record_sha256": "66e886f9e3bc787a7e0a96cad1037474ffe8d4be760ebc2be8a78e602f181640",
    "new_record_sha256": "20fb501e728de941d3410f35dff8a461f86a40c6822940d2554c0cd14ceab4ee",
    "record_diff_sha256": "c4178ea4e30ecc17755ead01cdea2cb3ab63c339868dc855853013ded1f1a82d",
    "same_byte_alias_only": false
  },
  {
    "revision": "revision-03",
    "before_utc": "2026-10-04T20:55:12.825915+00:00",
    "after_utc": "2026-10-04T20:55:12.830203+00:00",
    "receipt_sha256": "01395cf5b8db00e1c015cdf61157a53f1c854aef53cc9c03c74cbf636446c46d",
    "old_target_sha256": "551bce1408fd286420581e212f70ee1d87f0cf24770cd174ac7a708ccf65f214",
    "new_target_sha256": "aa29f35ac040b2c7cb800ae42c9b7a767086ca7ed0a51857f897c28fe543536a",
    "diff_sha256": "71998cd0e18395169f56474559d31474cf33177346a0fb8d8f5a53a3718b94f1",
    "old_record_sha256": "20fb501e728de941d3410f35dff8a461f86a40c6822940d2554c0cd14ceab4ee",
    "new_record_sha256": "de7355a55368746e7fb073f8c40937c5e25bc71b3ba00ff402a7766397cb7dcf",
    "record_diff_sha256": "12f259dafdcce12c4612c1e31e01a30d44cffe75a8266bcfa3cc9ee3a749723f",
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

源先修原文：Phase 6 · 02 (Spectrograms & Mel), Phase 3 · 06 (CNNs), Phase 5 · 08 (CNNs & RNNs for Text)

固定编号03-06实际是Optimizers；源括注CNNs不改，04-03仅为标题歧义补充英文入口，不是新增正式先修验收门槛。 只依据固定英文与相关术语即可翻译，不增加中文先修正式验收要求。

冻结源准备时 formal134，INDEX commit 57e6fdd85d87ba64726514e4c4433d3a1d9dca44 / SHA256 7659fc93786f56524138d8525e646f2a2cdb92a0569fef7ac9b98fce357d1673，独立回执 SHA256 7ca593614e44ebe780dd30120dfc3122868f90d3188484041a32511aed8abaff。actual132 运行 2026-10-04T19:24:29.438439+00:00 至 2026-10-04T19:24:41.076837+00:00 / RESULTS SHA256 d307d12f3aec999a804086e8588efe9bb69a04868dcc32b2d9061eec2a4f95fd，不覆盖本3课；不是当前实时计数。旧book5/6与site空锚点/重复项限制保持，不借历史批次声明本课发布通过。

## 作者源风险与有限提案

来源SHA256 999372e7a4ab5a1161e9d83d25cd7331dfe237a00f6f62e0c9a3b7692ef76a10；CPU提案实际来源SHA256 999372e7a4ab5a1161e9d83d25cd7331dfe237a00f6f62e0c9a3b7692ef76a10。以下技术事实与提案完整保留；NOT_RUN，提案不等于执行结果。


以下为静态源对照发现或需要后续事实核验的源声明，不是译错，不是本次运行失败。

1. **先修编号/标题错配**：en.md:7 的 Phase3·06(CNNs) 在固定树实际是 Optimizers。中文保留编号与源括注，不替换为04-03；已全文读两个真实英文入口。
2. **AudioCNN 参数量**：en.md 的 `nn.Conv2d`/Linear 默认参数可静态计为320+18,496+73,856+6,450=99,122，而随后的3M及SVG3M与之不符。没有加载PyTorch或运行模型，正文仍保留3M。~10 min、RTX4090与80%+没有实测支持。
3. **AST 示例并未展示微调循环**：代码只有 feature extractor/checkpoint loading 与 forward/logits，没有训练数据循环、loss、backward、optimizer；`audio` 也不是片段内定义的变量。正文“The example fine-tunes AST”按源翻译；课程main只实现合成纯音MFCC+k-NN，不执行CNN/AST/BEATs比较。
4. **示例与 main 的 helper/default 不同**：文中 featurize_mfcc/stft_magnitude、frame_len400/hop160、k5；main 为 featurize/stft_mag、frame_len256/hop128、k3。概念段说展平MFCC，实际示范用均值+方差汇总。不能据本文将代码段当作完整独立可运行程序。
5. **main 输入边界缺失**：短信号的 frame_signal 仍产生不足帧长的切片，stft_mag 随后按完整帧长索引；空帧、空bank、非法k没有显式防御；cosine的zip对不同向量长度静默截断。仅静态阅读，未制造或运行错误样例。
6. **数据/模型/指标时效声明未外部核验**：包括 millions of hours、2026默认模型、BEATs是否上Hub、用1-10%监督数据、1-2mAP/1/4compute、97.0%/0.548/99.0%排行、Whisper零增强接近SOTA、95%SOTA小时级等。正文与图中的年代/指标不完全相同，均保留源值。
7. **AudioSet 标签数和 mAP 定义**：源多处把632类类别体系直接当数据集类别数；把mAP定义为跨类别和阈值平均，也未限定实际计算协议；多标签列表写UrbanSound-style，不能据此推断UrbanSound8K的任务标签性质。没有用检测任务的IoU阈值定义擅自补齐音频指标。
8. **练习/课程契约限制**：Hard先说ESC-50 fold1，接着要求5折交叉验证，具体protocol未解释。包中无quiz和tests。transformers/torchaudio不在根AGENTS依赖白名单；from_pretrained可能下载权重。所有安装、下载、训练与练习命令仅保留，未执行。
9. **图形验收待办**：SVG原样；真实GitHub GFM需检查3表、6围栏、图示英文载荷与长行，figure只是源注册标识。静态XML不代表真实页面检查。


- 本次不需要任何课程CPU执行。若后续确需验证，仅可另行批准无网络、无模型的微型确定性数值用例，限制最多2帧、每帧16采样点、进程超时5秒与内存上限；这只是有界提案，未运行，也不能用其声称训练或基准通过

## 独立源边界

```json
[
  {
    "id": "SRC01",
    "segments": [
      "06-03:b0005"
    ],
    "source_lines": [
      7,
      7
    ],
    "classification": "CONFIRMED_SOURCE_MISMATCH",
    "finding": "03-06固定树为Optimizers而非CNNs；已完整补读04-03 CNNs。",
    "disposition": "另行源元数据修正，译文不换号。",
    "translation_error": false
  },
  {
    "id": "SRC02",
    "segments": [
      "06-03:b0063",
      "06-03:b0065"
    ],
    "source_lines": [
      102,
      120
    ],
    "classification": "CONFIRMED_STATIC_ARITHMETIC_MISMATCH",
    "finding": "AudioCNN默认参数：32×(1×9+1)=320；64×(32×9+1)=18496；128×(64×9+1)=73856；50×(128+1)=6450；合计99122，非源文/SVG3M。",
    "disposition": "须源作者修订；10min和80%+未测量。",
    "translation_error": false
  },
  {
    "id": "SRC03",
    "segments": [
      "06-03:b0067",
      "06-03:b0069",
      "06-03:b0071"
    ],
    "source_lines": [
      122,
      138
    ],
    "classification": "CONFIRMED_STATIC_IMPLEMENTATION_GAP",
    "finding": "AST片段只有载入、extractor和forward/logits，没有loss/backward/optimizer/训练loop，audio在片段中未定义，却称example fine-tunes。",
    "disposition": "补源训练示例前不能宣称可运行微调教程；译文不暗补。",
    "translation_error": false
  },
  {
    "id": "SRC04",
    "segments": [
      "06-03:b0017",
      "06-03:b0047",
      "06-03:b0051",
      "06-03:b0057",
      "06-03:b0087"
    ],
    "source_lines": [
      20,
      163
    ],
    "classification": "CONFIRMED_CROSS_FILE_DEMO_LIMIT",
    "finding": "概念展平MFCC而代码均值方差聚合；正文helper/default为featurize_mfcc/stft_magnitude/400/160/k5，main为featurize/stft_mag/256/128/k3。main只做4类合成纯音MFCC+k-NN，无CNN/AST/BEATs比较。",
    "disposition": "不能把main结果当真实数据训练/架构benchmark。",
    "translation_error": false
  },
  {
    "id": "SRC05",
    "segments": [
      "06-03:b0029",
      "06-03:b0035",
      "06-03:b0091",
      "06-03:b0095"
    ],
    "source_lines": [
      32,
      183
    ],
    "classification": "SOURCE_DEFINITION_RISK_NOT_EXTERNALLY_ADJUDICATED",
    "finding": "632类taxonomy与dataset类别数混写；mAP称跨classes和thresholds但未定义音频协议；UrbanSound-style多标签描述不宜直接等同UrbanSound8K。",
    "disposition": "保留源义；不借检测课IoU定义补足，不宣称已外部事实核验。",
    "translation_error": false
  },
  {
    "id": "SRC06",
    "segments": [
      "06-03:b0019",
      "06-03:b0021",
      "06-03:b0023",
      "06-03:b0025",
      "06-03:b0039",
      "06-03:b0053",
      "06-03:b0071",
      "06-03:b0077",
      "06-03:b0079",
      "06-03:b0091",
      "06-03:b0095"
    ],
    "source_lines": [
      22,
      183
    ],
    "classification": "TIME_SENSITIVE_CLAIMS_UNVERIFIED",
    "finding": "millions of hours、2026默认架构/Hub状态、1-10%监督量、1-2mAP/1/4计算、97.0%/0.548/99.0%、95%SOTA小时级与2017基线均为源声明。图文年代/指标也不完全相同。",
    "disposition": "仅审忠实性，未外部事实/存活/benchmark核验。",
    "translation_error": false
  },
  {
    "id": "SRC07",
    "segments": [
      "06-03:b0087"
    ],
    "source_lines": [
      161,
      163
    ],
    "classification": "SOURCE_PROTOCOL_UNDERSPECIFIED",
    "finding": "Hard先fold1训练又要求5折交叉验证，训练/验证折划分未阐明；mask值的具体协议未展开。",
    "disposition": "另行澄清英文；不擅改中文练习。",
    "translation_error": false
  },
  {
    "id": "SRC08",
    "segments": [
      "06-03:b0051",
      "06-03:b0057"
    ],
    "source_lines": [
      71,
      96
    ],
    "classification": "STATIC_INPUT_BOUNDARY_RISK",
    "finding": "main短于frame_len的帧仍按完整帧索引；summarize空帧、knn空bank/非法k缺显式保护；cosine不同维度zip静默截断。",
    "disposition": "仅静态阅读，未构造或执行失败用例。",
    "translation_error": false
  },
  {
    "id": "SRC09",
    "segments": [
      "06-03:b0069",
      "06-03:b0087"
    ],
    "source_lines": [
      124,
      163
    ],
    "classification": "SOURCE_CONTRACT_RUNTIME_LIMIT",
    "finding": "包无quiz/tests；transformers/torchaudio不在根AGENTS依赖白名单；from_pretrained可下载权重。",
    "disposition": "未import/安装/下载/训练/执行课程/API/GPU。",
    "translation_error": false
  },
  {
    "id": "SRC10",
    "segments": [
      "06-03:b0015",
      "06-03:b0041"
    ],
    "source_lines": [
      18,
      54
    ],
    "classification": "PRESENTATION_PENDING",
    "finding": "SVG原样和相对路径已核，figure为源注册标识；XML解析不等于图形可读。",
    "disposition": "真实GFM/网站/移动端/PDF/CI/远端门槛由协调者续办。",
    "translation_error": false
  }
]
```

源准备发现（仅读、未代改源）：

```json
[
  {
    "location": "docs/en.md:7",
    "finding": "Phase3·06 is titled Optimizers, not CNNs. Preserve declared numbering/title in translation and record mismatch; read actual03-06 plus supplemental04-03 CNNs—LeNet to ResNet, without silently remapping source."
  },
  {
    "location": "docs/en.md:120,138; code/main.py",
    "finding": "Declared AudioCNN layers have99,122 parameters for default50 classes, not3M. AST snippet loads a checkpoint and performs a forward call, with no training loop despite prose saying fine-tunes. main implements only synthetic-tone k-NN, not CNN/AST/BEATs evaluation."
  },
  {
    "location": "code/main.py framing/summarize/knn; docs/en.md Step1 and Step3",
    "finding": "Short signals may produce undersized frames then index beyond them; empty frame/bank and invalid k are unguarded, zip silently truncates unequal feature lengths. Tutorial helper names/default frame/hop/k differ from main; these are static limits, not executed failures."
  },
  {
    "location": "docs/en.md benchmark tables/Key Terms; assets/audio-classification.svg",
    "finding": "Dated benchmark/model/default/dataset-label assertions are source claims not independently verified here. mAP definition and multi-label distinctions must not be silently repaired. Existing SVG is protected and needs later real visual review; no quiz or tests are present in fixed package."
  }
]
```

课程 main/import/tests、模型/CPU/GPU、API/网络/安装/服务/签名均 NOT_RUN；本轮不重跑原strict、离线重放、GFM、控制或累计回归。已有局部strict和独审仅按其真实输入哈希复用；own3仍未安装，后续页面、远端内容和适用批次尚待处理。
