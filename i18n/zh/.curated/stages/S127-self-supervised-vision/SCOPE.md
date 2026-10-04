# S127-self-supervised-vision English-first 支持范围

状态：本地 own3 候选，未安装、未发布，不增加正式课程数。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；原控制 `f9b5e9cbe4012f54483794f920c0d87b06a7573d`。

## 当前正文与独立审校身份

- Lesson: 04-17
- Current target SHA256: c0e38861e2a1223b56af3fea9f1c8c19a605c9bf3684712f6778265468b36fa6 (12997 B)
- Current draft record SHA256: 235984d33a630072f8511f66406c24c107c4ba0470835d3ab1bdc12710eec3f3 (58172 B)
- Historical author handoff SHA256: de4175725589c7fbafff3f21dad29493d9435acc53291302aca6930e130db021
- Original full independent review SHA256: 09d4acbe6769315da67a3d461a628e101cae6f7e28781905a7313425e077f44d; companion SHA256: 6ef68967c7377aed6e5ece8fcc160da5dae20ea33a3337632f3e9756fe05fa80
- Current incremental closure SHA256: ba20b1b417b690bc2d14111360635028262cf4dd34e6171fefbf80658bc5a0b3
- First complete body SHA256: f2ee58a25adf8512b78b1089b0331f794e3364172db8ee47ebbbf27212495c8e
- First successful capture record SHA256: 71616e3b9cd15e61bf4ba89972e5acd8d93aa8e0c28979c4a288e18b5674f7e0
- Current local strict evidence SHA256: 846ec79c498d822ea5f802f68ee3107c5274c6fdae44f08392a5d67bf9d7654b; historical evidence only, not rerun

125块原完整技术与中文独审 REQUEST_CHANGES 原样保留；R02 只核 b0105 一句并 PASS，继承124块原覆盖。一般下游 linear head 为线性头，分类探测专属线性分类头保持。

Preflight 2026-10-04T21:32:03.217012+00:00; full first body written 2026-10-04T21:34:48.538378+00:00, no separately recorded before-write timestamp. First capture succeeded at 2026-10-04T21:34:48.589872+00:00. R01 author wording and provenance metadata revision retained; correction of capture default run_date is record metadata, not a source-code change. R02 one-sentence semantic correction by a separate editor after the original author handoff: 2026-10-04T21:46:43.273393+00:00 to 2026-10-04T21:46:43.274470+00:00. Original handoff and full REQUEST_CHANGES stay on907ee32/831efc5; currentc0e38861/235984d3 uses R02 PASS plus124 exact unchanged blocks.

真实修订身份与时间（同字节快照不计额外修订）：

```json
[
  {
    "revision": "R01",
    "before_utc": "2026-10-04T21:36:05.357089+00:00",
    "after_utc": "2026-10-04T21:36:05.367962+00:00",
    "receipt_sha256": "a21e33139656281167ff2792e4f4baaf86129ae5519a60eb730e34772155f0db",
    "old_target_sha256": "f2ee58a25adf8512b78b1089b0331f794e3364172db8ee47ebbbf27212495c8e",
    "new_target_sha256": "907ee32c7760aaa410e64458ba03c4bd9bf02cbd4473dbcf34d247299093432f",
    "diff_sha256": "59f37a3d00e513f67da1bd88244f7cd441944025a248525176ba57af420962de",
    "old_record_sha256": "71616e3b9cd15e61bf4ba89972e5acd8d93aa8e0c28979c4a288e18b5674f7e0",
    "new_record_sha256": "831efc5c6ae54def2860d150bc1c0a00dbe8de620df5fabe01c066717f6b55e0",
    "record_diff_sha256": "01b9442c9286a48ec23bc0e006da4e965b64d031ed93523fb16b9665ca6f8bb4",
    "same_byte_alias_only": false
  },
  {
    "revision": "R02",
    "before_utc": "2026-10-04T21:46:43.273393+00:00",
    "after_utc": "2026-10-04T21:46:43.274470+00:00",
    "receipt_sha256": "846ec79c498d822ea5f802f68ee3107c5274c6fdae44f08392a5d67bf9d7654b",
    "old_target_sha256": "907ee32c7760aaa410e64458ba03c4bd9bf02cbd4473dbcf34d247299093432f",
    "new_target_sha256": "c0e38861e2a1223b56af3fea9f1c8c19a605c9bf3684712f6778265468b36fa6",
    "diff_sha256": "ccb0371b5ba1ebeebca6925662d89bdfba13330c2a5cce3d75781c5902d5b9d0",
    "old_record_sha256": "831efc5c6ae54def2860d150bc1c0a00dbe8de620df5fabe01c066717f6b55e0",
    "new_record_sha256": "235984d33a630072f8511f66406c24c107c4ba0470835d3ab1bdc12710eec3f3",
    "record_diff_sha256": "459fcad1377c5d543198e741d3ff16eb25aebda2a3c2557272d9ab5332c411cc",
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

源先修原文：**Prerequisites:** Phase 4 Lesson 04 (Image Classification), Phase 4 Lesson 14 (ViT)

仅以固定英文及相关术语为翻译前提，不增加中文先修正式验收门槛。作者与审校者的亲读和固定既有英文全文证据复用各按原报告保留，不冒称本轮重新全文阅读所有先修或所有术语。

冻结源准备时 formal136，INDEX commit d93dcd48f5d24a0dec7bfac2de9230ab1c098fdb / SHA256 cd532f05d6cff2133b5a418167a1e08e2f59779679350b618a41167a5082b593，独立回执 SHA256 32000870ed2c3bb0934fb30cab1374737e6a5a2d0bbff271ca0beb91c388145a。actual135 运行 2026-10-04T20:38:42.005823+00:00 至 2026-10-04T20:38:53.725717+00:00，RESULTS SHA256 9fb594aa0d6c417666f579729ca0f3c93b5bff6abff693f8058309434ac3982b，不覆盖本3课；这不是当前实时计数。历史 book5/6及site43空锚点限制保持，不借旧批次声称本课发布通过。

## 作者源风险与有限提案

源风险实际文件 SHA256 de4175725589c7fbafff3f21dad29493d9435acc53291302aca6930e130db021 (20744 B)；CPU提案实际文件 SHA256 de4175725589c7fbafff3f21dad29493d9435acc53291302aca6930e130db021 (20744 B)。以下技术事实和提案保留；CPU状态NOT_RUN，提案不是执行结果。

[
  {
    "id": "SRC-01",
    "where": "docs/en.md:13,51,180,234; code/main.py:5-12",
    "finding": "批512可用而32失败、小批坍缩/停滞是过度一般化的源断言，代码没有SSL训练。随机配对loss≈log(2N−1)仅在相似度logits近均匀等条件下成立；随机32维单位向量再除tau=0.1不保证≈3.4。相同配对低loss取决于其他相似度与温度，大批本身并不保证更低。降温损失单调性同样不是任意样本都保证。",
    "action": "原断言与数值忠实保留，未冒充运行证据"
  },
  {
    "id": "SRC-02",
    "where": "quiz.json:8,34; docs/en.md protected InfoNCE formula",
    "finding": "quiz将batch32解释为30 negatives，却对1024写2046；按本课N对/2N视图公式，N=32时每anchor应有2N−2=62 negatives。quiz另把encoder FLOPs说成与可见图像块严格成正比，忽略注意力项的非线性。",
    "action": "quiz只作静态上下文阅读，未翻译或改源"
  },
  {
    "id": "SRC-03",
    "where": "code/main.py info_nce/random_mask_indices/DinoHead; docs/en.md:235",
    "finding": "info_nce未验证L2归一化、形状和tau>0；random_mask_indices未约束mask_ratio。DinoHead共用self.proj，teacher只是detach，不含EMA教师训练或坍缩实验。单次中心化输出不能证明几轮内坍缩。",
    "action": "无课程import/main/tests，未给出实测结论"
  },
  {
    "id": "SRC-04",
    "where": "docs/en.md:72-95,236; code/main.py random_mask_indices",
    "finding": "代码只生成MAE式遮蔽索引，不含MAE编码器、解码器或重构训练。练习指定第10课TinyUNet做MAE主干，却未说明适配ViT式可见token编码/重构；保证胜过监督线性探测的结论缺实验。75%/15%熵解释是概括，图中同一家族共享教师EMA或75%遮蔽的描绘也简化了各方法差异。",
    "action": "忠实翻译，不补训练实现，不擅自把TinyUNet改成ViT"
  },
  {
    "id": "SRC-05",
    "where": "docs/en.md:19-21,68,98-106,204-223,249",
    "finding": "$10M标注成本、跨数据/方法性能、current/2026生产默认、最强特征、线性探测准确率与2-5百分点、3x预训练加速、timm所有checkpoint等均是固定英文断言。此次没有上网或跑模型核验，线性探测的“纯粹”衡量也有训练协议影响。",
    "action": "保留时态、数值、断言强度；不作为当前事实背书"
  },
  {
    "id": "SRC-06",
    "where": "outputs/prompt-ssl-pretraining-picker.md:23-39",
    "finding": "顺序规则为ViT分类且100万≤图像<1亿、200≤GPU小时<1000留空；>=1亿且200≤GPU小时<5000时rule7条件不匹配，降级措辞不能明确消除此空档。低预算一律不能收敛/小数据一律checkpoint占优等缺条件。",
    "action": "上下文风险单列；outputs不改且不执行"
  },
  {
    "id": "SRC-07",
    "where": "outputs/skill-linear-probe-runner.md:35,73-86,102",
    "finding": "说明要求训练末验证准确率，模板返回best_val；extract将输入送device却不负责encoder.to(device)，非CPU需调用方先迁移。整份验证特征一次上设备有内存风险。规则将重复特征提取说成retraining且100x是无条件估计。",
    "action": "输出技能未运行，未把模板表现说成实际结果"
  },
  {
    "id": "SRC-08",
    "where": "package; docs/en.md:118,144,208-216; quiz.json",
    "finding": "quiz仅5题（2pre/3post）、无lesson/title且无code/tests，不满足AGENTS课程合同。torchvision/transformers/timm超出根allowlist，from_pretrained会下载，pil_image未定义。裸围栏3处仅补text。普通段落__getitem__可能在GFM中显示为强调文字，figure依赖站点机制；尚未做GFM/网站检查。",
    "action": "不修改源码合同；任何运行/呈现结论留待相应真实门槛"
  }
]

CPU proposal (NOT_RUN):
{
  "status": "NOT_RUN",
  "scope": "如需另外授权，可仅用stdlib和独立小型人工向量计算对称InfoNCE的有限数值例子、按有限输入枚举picker规则空档；不导入课程、不训练、不用GPU/模型/API/网络/安装。",
  "limits": "≤16 pairs, ≤32 dimensions, ≤4 temperatures, ≤1 second of scalar arithmetic intended; no resource measurement claimed.",
  "purpose": "区分源均匀logits公式与随机logits断言；不是SSL训练复现。"
}

## 原独立审校保留的源边界

```json
[
  {
    "id": "SRC-I01",
    "segments": [
      "04-17:b0009",
      "04-17:b0031",
      "04-17:b0085",
      "04-17:b0091",
      "04-17:b0117"
    ],
    "source_lines": [
      12,
      15,
      53,
      166,
      180,
      234
    ],
    "finding": "512成功/32失败、512-8192必要批大小和降温趋势是无条件源概括；随机32维单位向量的非均匀logits不保证交叉熵为log31≈3.4。大批本身也不保证相同配对损失更低。",
    "basis": "固定英文及InfoNCE表达式静态推理，未运行数值实验",
    "translation_action": "准确保留原文；没有把预测或should写成实测"
  },
  {
    "id": "SRC-I02",
    "segments": [
      "04-17:b0029",
      "04-17:b0083"
    ],
    "path": "phases/04-computer-vision/17-self-supervised-vision/quiz.json",
    "finding": "quiz把batch32写30负例而把1024写2046；依本课N对/2N视图定义，32对每anchor负例应为2N-2=62。只读quiz，不改正文/quiz。",
    "basis": "公式索引计数的静态逻辑"
  },
  {
    "id": "SRC-I03",
    "segments": [
      "04-17:b0035",
      "04-17:b0039",
      "04-17:b0117"
    ],
    "path": "phases/04-computer-vision/17-self-supervised-vision/code/main.py",
    "finding": "DinoHead共用投影层，teacher只有detach；无独立EMA教师权重更新、优化循环或坍缩训练。centre均值更新与teacher权重EMA不是同一对象。",
    "translation_action": "教师语义忠实，练习未被宣称已完成"
  },
  {
    "id": "SRC-I04",
    "segments": [
      "04-17:b0023",
      "04-17:b0045",
      "04-17:b0051",
      "04-17:b0059",
      "04-17:b0061",
      "04-17:b0095",
      "04-17:b0117"
    ],
    "finding": "MAE示例只生成遮蔽索引。Lesson10实际为diffusion TinyUNet(x,t)；源未给其适配MAE可见块编码、重构和probe特征的办法。保证优于监督probe、统一75%族系、熵解释、3x速度都仍是固定源断言。",
    "translation_action": "未擅自换ViT、补训练或新增严格检查例外"
  },
  {
    "id": "SRC-I05",
    "segments": [
      "04-17:b0013",
      "04-17:b0015",
      "04-17:b0041",
      "04-17:b0067",
      "04-17:b0069",
      "04-17:b0101",
      "04-17:b0105",
      "04-17:b0107",
      "04-17:b0121"
    ],
    "finding": "估计标注成本、跨方法数字、pure probe、2026生产默认/SOTA/最强特征、任意下游线性头和timm every checkpoint等主张均未做当前事实核验，probe表现也依训练协议。",
    "translation_action": "不暗修事实、不背书当前状态"
  },
  {
    "id": "SRC-I06",
    "segments": [
      "04-17:b0113"
    ],
    "path": "phases/04-computer-vision/17-self-supervised-vision/outputs/prompt-ssl-pretraining-picker.md",
    "finding": "按top-down规则，部分ViT分类图像规模与200-1000或200-5000GPU小时预算组合没有命中；低预算/小数据绝对结论缺条件。",
    "translation_action": "仅作为源产物读审，不执行该prompt也不改规则"
  },
  {
    "id": "SRC-I07",
    "segments": [
      "04-17:b0113"
    ],
    "path": "phases/04-computer-vision/17-self-supervised-vision/outputs/skill-linear-probe-runner.md",
    "finding": "叙述end-of-training准确率与返回best_val不同；encoder需调用方迁移device，整验证特征一次上设备有容量风险；重复提取误称retraining及100x属源概括。",
    "translation_action": "只读模板，未运行"
  },
  {
    "id": "SRC-I08",
    "segments": [
      "04-17:b0071",
      "04-17:b0077",
      "04-17:b0079",
      "04-17:b0103"
    ],
    "finding": "课程只有5题（2pre/3post）、无lesson/title及code/tests，依赖torchvision/transformers/timm超根allowlist；pil_image未定义/from_pretrained涉及下载。裸__getitem__潜在强调、figure站点机制均需真实呈现门禁确认。",
    "translation_action": "只允许三bare fences补text；未运行课程、网络、GFM或回归"
  }
]
```

固定源准备发现，未暗改源：

```json
[
  {
    "where": "docs/en.md InfoNCE; main.py; quiz.json",
    "finding": "InfoNCE requires externally normalized pairs and valid positive temperature; no input guards. Random-pair loss≈log(2N−1), low-loss and small-batch-collapse claims are not guaranteed by code. Quiz says32-pair batch has30 negatives, inconsistent with2N−2=62."
  },
  {
    "where": "main.py DinoHead/masking; docs/en.md exercises; outputs",
    "finding": "DinoHead uses a shared projection with detached output, no EMA teacher training or collapse experiment; mask indices alone do not implement MAE. Exercise names TinyUNet from04-10 as MAE backbone without adaptation. Picker has uncovered compute/data bands; linear-probe text says final accuracy but template returns best validation accuracy."
  },
  {
    "where": "docs/en.md dated benchmarks/Use It; package",
    "finding": "External2026 performance/compute/default claims retained but unverified; torchvision/transformers/timm and pretrained downloads are not executed. Quiz5(2pre/3post), missinglesson/title; no tests. Protected figure/Mermaid and bare fences require later authored checks."
  }
]
```

课程main/import/tests、模型/CPU/GPU、API/网络/安装/服务均NOT_RUN；本轮不重跑strict、离线重放、GFM或累计回归。记录默认日期更正只是作者record元数据修订，不改源代码或冻结检查器。后续页面、远端内容及适用批次仍分别验收。
