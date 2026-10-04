# S131-whisper-architecture-finetuning English-first 支持范围

状态：本地 own3 候选，未安装、未发布，不增加正式课程数。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；原控制 f9b5e9cbe4012f54483794f920c0d87b06a7573d。

## 当前正文与独立审校身份

- Lesson: 06-05
- Current target SHA256: e8a8281d870ce87d32af9339d355b05463e4501f7f0f81dc81ec60a804c2541f (10565 B)
- Current draft record SHA256: a92a55238006dcdff4196f2bedd8fb2444bd068fe29d72fefc121e6c32c89add (46674 B)
- Historical author handoff SHA256: 4217b799c845aa08954e5ec808c4f4a61985c5cd3b78adbf197c6015e950e164
- Current handoff SHA256: dae5a2b47e44070fd7265c50a07d5f58e4c8db9f15b57b4a51f2b5fd27c41a63
- Original full independent review SHA256: aa6bc7ff1f0dc8a39aa5cb81cb500a05f0ce721905afbe81b5271234155fdc10
- Current incremental closure SHA256: 04c0e1e331e562bcba5db058a475f701bf0f39fd8341db5809b9b7a436173b2e
- First complete body SHA256: b3d3669d9e8705ac2452aa5a6e24ed192a53026450d543052ec9d052abed51c3
- First-capture record SHA256: null; failed first capture
- First successful capture record SHA256: 4590b8d0d3ad6a23381ce1b72f0082012e0e86da428adbcb048d91f748fa95b8
- Historical exact-byte local strict evidence SHA256: f02a99deececd973f9fc6acaac753e0da37fb8e984fa01fe2611e10dc2f6c363; not rerun

First complete body capture failed rc1 because September became numeric9; first record remains null. R01 changes9 to九; only afterwards SECOND-CAPTURE succeeds and creates FIRST-SUCCESSFUL-RECORD. R02/R03 are body edits; R04 only asset/provenance metadata, body unchanged. R05 contains exactly four multiplier prose replacements across b0023/b0045/b0103. Original full103-block CHANGES_REQUESTED was written after R05 but remains bound to actually reviewed old before snapshots, not relabelled PASS. Real R05 incremental PASS plus100 unchanged blocks binds current bytes.

真实审校先后与各自原身份：

~~~json
[
  {
    "sha256": "aa6bc7ff1f0dc8a39aa5cb81cb500a05f0ce721905afbe81b5271234155fdc10",
    "bytes": 184516,
    "status": "CHANGES_REQUESTED"
  },
  {
    "sha256": "04c0e1e331e562bcba5db058a475f701bf0f39fd8341db5809b9b7a436173b2e",
    "bytes": 11004,
    "status": "PASS_WITH_SOURCE_RISKS"
  }
]
~~~

真实修订身份与时间（同字节快照不增加修订数）：

~~~json
[
  {
    "revision": "revision-01",
    "before_utc": "2026-10-04T22:20:57.800640+00:00",
    "after_utc": "2026-10-04T22:20:57.801451+00:00",
    "receipt_sha256": "17f9b1ee995fbc5db438d46f63f06d37cf99a1f7b8d5d03cd2cf4fd3b0d50914",
    "old_target_sha256": "b3d3669d9e8705ac2452aa5a6e24ed192a53026450d543052ec9d052abed51c3",
    "new_target_sha256": "3c716d5495aba8737a3e011c3b87db204ae00be7969a430dbff917cb1b3dbe1e",
    "diff_sha256": "e1d60b79c024cd81e7db72419c099ce86af7749fc5112abc0748a97dffe6cbfa",
    "old_record_sha256": null,
    "new_record_sha256": null,
    "record_diff_sha256": null,
    "same_byte_alias_only": false
  },
  {
    "revision": "revision-02",
    "before_utc": "2026-10-04T22:21:51.256619+00:00",
    "after_utc": "2026-10-04T22:21:51.269425+00:00",
    "receipt_sha256": "fab3de396894088003b8ae68a7af291640b3793e777dd7a20a2b43bf97d0383d",
    "old_target_sha256": "3c716d5495aba8737a3e011c3b87db204ae00be7969a430dbff917cb1b3dbe1e",
    "new_target_sha256": "19b1c98030643f7b759e6dc38b097b73ad39e2252edbda1d39b2b1de7862cc15",
    "diff_sha256": "cb4826d83735fdba8e6ce105cdec06eef695c571d6844b35a4791274faf0172b",
    "old_record_sha256": "4590b8d0d3ad6a23381ce1b72f0082012e0e86da428adbcb048d91f748fa95b8",
    "new_record_sha256": "abf945dde29dcd9097be6d986e421749a99012b78c36924e46f15334d54a32e6",
    "record_diff_sha256": "6594653d2ced9d2c5ac4a8d2d87d39494daad42645b52da8ae47c0c6f01712e0",
    "same_byte_alias_only": false
  },
  {
    "revision": "revision-03",
    "before_utc": "2026-10-04T22:22:29.872899+00:00",
    "after_utc": "2026-10-04T22:22:29.886761+00:00",
    "receipt_sha256": "10ddf66ad46495d8d2a494a21c9066155cff3a8278b2ce5a81fae483393211b4",
    "old_target_sha256": "19b1c98030643f7b759e6dc38b097b73ad39e2252edbda1d39b2b1de7862cc15",
    "new_target_sha256": "7b05350f31fc936d0405b67de1c76b1f5ffc4632a2eb74e4caa7535ca92c0de7",
    "diff_sha256": "9c809791458ba1d5fde0b1dad0fd31e891b458bb2d71bceabbd7535703c0d09f",
    "old_record_sha256": "abf945dde29dcd9097be6d986e421749a99012b78c36924e46f15334d54a32e6",
    "new_record_sha256": "e429853121aec2b1f3d3acbba9a9e9de2a8cdd2860f73f6fd06c649029b451f0",
    "record_diff_sha256": "3d75d043bdb90e8cc193bee42fcbf11d96567b9289066a62c50473b4a97901a9",
    "same_byte_alias_only": false
  },
  {
    "revision": "revision-04",
    "before_utc": "2026-10-04T22:23:11.555356+00:00",
    "after_utc": "2026-10-04T22:23:11.569381+00:00",
    "receipt_sha256": "8d95f3957952d80539b7655c81d0d31a21c564150a0262aed6c10194fa687707",
    "old_target_sha256": "7b05350f31fc936d0405b67de1c76b1f5ffc4632a2eb74e4caa7535ca92c0de7",
    "new_target_sha256": "7b05350f31fc936d0405b67de1c76b1f5ffc4632a2eb74e4caa7535ca92c0de7",
    "diff_sha256": null,
    "old_record_sha256": "e429853121aec2b1f3d3acbba9a9e9de2a8cdd2860f73f6fd06c649029b451f0",
    "new_record_sha256": "25a7bbd067f1311d7c28017ee7bb6df88c03e2ee83b6d7a5e779683f2fed4f7f",
    "record_diff_sha256": "f6e7f6d253c44025cde3ddf12247ba5c0cdc294ab6cc2ce1065105f2633a25c5",
    "same_byte_alias_only": false
  },
  {
    "revision": "revision-05",
    "before_utc": "2026-10-04T22:36:07.409463+00:00",
    "after_utc": "2026-10-04T22:36:07.414283+00:00",
    "receipt_sha256": "ae929c112433eccdea2c02f454272f43554a649321720e9cfe3c4dc603523413",
    "old_target_sha256": "7b05350f31fc936d0405b67de1c76b1f5ffc4632a2eb74e4caa7535ca92c0de7",
    "new_target_sha256": "e8a8281d870ce87d32af9339d355b05463e4501f7f0f81dc81ec60a804c2541f",
    "diff_sha256": "a76951c8be29786b78066635eeed8e128fb2a98a77c3e9a3d2b800375601e00c",
    "old_record_sha256": "25a7bbd067f1311d7c28017ee7bb6df88c03e2ee83b6d7a5e779683f2fed4f7f",
    "new_record_sha256": "a92a55238006dcdff4196f2bedd8fb2444bd068fe29d72fefc121e6c32c89add",
    "record_diff_sha256": "8be3e6363bf891479bb20d4470c38ca1fc1cf5c189e2e7be5f12ecfcd8355915",
    "same_byte_alias_only": false
  }
]
~~~

## 固定支持与先修边界

原作者 common133 清单 SHA256 ebbf4c6185da6d48c9cf22f437d4977e43ddbfb74b080eb660a5d4f50845f2b2，125 TERM +8 controls；既有133项身份、顺序、角色和分类保持，公开投影仅移除60个私有定位值。候选只追加 S127–S129 三个真实发布、独立完整回读的 TERM：common136、128 TERM、8 controls，加本课 own3 后139。原作者、common133、首稿、全部旧新record与审校均原样保留，后续公共record才绑定真实已发布own3。

~~~json
[
  {
    "sha256": "decf3c883928a917d07e47adec3e3f7a99ff80f27e09a5c51bac3377fa6688b7",
    "git_blob": "21b805ec6073e4c78f2c25b5a9a7be3388158b79",
    "bytes": 2588,
    "mode": "100644",
    "commit": "c3525f2eafeb8c5f65f383b20739c2e7733287f9",
    "path": "i18n/zh/.curated/stages/S127-self-supervised-vision/TERMINOLOGY.md",
    "role": "reference_stage_terminology",
    "stage_id": "S127-self-supervised-vision",
    "support_only_not_course_completion": true,
    "publication_receipt_sha256": "673f0ad49d4d127126ca3d9e2fae96895696b209b12217e9b4026924099f4678"
  },
  {
    "sha256": "e01b63129526b00477b3a1c1cb5e96f95fc3cd1d1a76362189507a54554d1b50",
    "git_blob": "a9b2e34252fd0b7f40d613d717683463c081fdda",
    "bytes": 3672,
    "mode": "100644",
    "commit": "5eac8a8b2425d5e822e019eac73d644bbbf38786",
    "path": "i18n/zh/.curated/stages/S128-speech-recognition-asr/TERMINOLOGY.md",
    "role": "reference_stage_terminology",
    "stage_id": "S128-speech-recognition-asr",
    "support_only_not_course_completion": true,
    "publication_receipt_sha256": "8aa7d15abff8748b16ba978aa4af0387442c911415c2ab742fd6f0de64397dfb"
  },
  {
    "sha256": "eacd0d355830b22c0a3a270787186c1301b01f20111019837f9bd269f4c298be",
    "git_blob": "8bfaddde342b8911b511233a428240b65ce1296f",
    "bytes": 2736,
    "mode": "100644",
    "commit": "0a7c8004c2d975e8187b5c811bd866c9e2232f35",
    "path": "i18n/zh/.curated/stages/S129-workbench-for-real-repos/TERMINOLOGY.md",
    "role": "reference_stage_terminology",
    "stage_id": "S129-workbench-for-real-repos",
    "support_only_not_course_completion": true,
    "publication_receipt_sha256": "22236cb96b5476f0c55d697b70d3770264f92e78625b2a5ddf77087e1a971f03"
  }
]
~~~

源先修原文：**Prerequisites:** Phase 6 · 04 (ASR), Phase 5 · 10 (Attention), Phase 7 · 05 (Full Transformer)

仅以固定英文及相关术语为翻译前提，不添加中文先修正式验收门槛。作者与审校者的亲读和固定既有英文全文复用按各自原报告保留；本轮仅装配支持候选，不新增语言二审或全文亲读声明。

冻结源准备 formal138/actual138，INDEX commit 4832660521df7d71a336615cb30ec59794a2db06，INDEX SHA256 1bc111580519ff8d68dce14547c373fd659d0320b4d5e0b5fc1fc87c4bf6223f，独立回执 SHA256 2d2284aa3eec2c4fb1f5aa89d9577a56d8a00647e7c89d61895fbe9e53685a0e。这是 2026-10-04T22:08:48.908492+00:00 源准备时的真实快照，未追刷当前计数；不覆盖本三课，也不借历史回归宣称其已通过。

## 作者源风险与有限提案

原源风险 SHA256 5dfdd86e02994d833b805f59ececff56ffbca9dd487bf86405ac944e32da8bab (4564 B)。以下原静态观察与历史 NOT_RUN 文字照录，原作者“strict 未执行”等若出现，仅反映该风险文件写作时点，不能覆盖后来的独立检查回执：

# S131 固定英文源风险（不是译错清单）

依据固定 commit 1bafaa88bb4668356791150bec3a6d7df38387eb 的本课英文包及三篇英文先修做静态分析；未联网核验模型规格、论文数值或 API 版本。下列源文断言在中文中保留，未暗中改正；本文不对正确性背书。

1. b0003、b0021、b0039 / SVG：680k 训练小时数、99 种语言、80 个 mel 频带、51,865 词表大小与 Large-v3 / Turbo 并列叙述，没有完整区分不同模型版本。Large-v3 参数和输入特征规格须另行按指定版本核验；不能由本译文断言各变体全部适用。
2. b0029、b0031 / main.py / SVG：英文把语言 token `<|en|>` 写成强制决定翻译还是转写，又把 `<|transcribe|>` / `<|translate|>` 后的用途按容易误配的顺序描述。main.py 则将 language 和 task 作为不同参数构造特殊 token。中文保留源文歧义，没有添加“分别”强行配对或改写任务语义。源将 `<|notimestamps|>` 称为跳过词级时间戳，时间戳 token 与强制对齐的区别也需核验。
3. b0035、b0087：`(log_mel - mean) / std` 及“统计量来自 Whisper 自身训练语料库”是源断言；其与 Whisper 实际预处理的关系未核验。不得据此悄悄改写代码、公式，或宣称更换 mel 实现必然产生近随机结果。
4. b0023、b0039、b0047、b0083、b0103：8× 延迟/速度、<1% WER、表内 A100 实时倍数、社区医疗/冰岛语收益、faster-whisper 最快及输出完全相同等均缺少本课可复现实验条件。表头“Latency”与实时速度倍数方向混用；具体 WER 数据也不能与不同数据划分、归一化或解码配置直接比较。百分数保留，没有改成百分点。
5. b0045、b0067 / main.py / SVG：微调流程写 q_proj/k_proj/v_proj，LoRA 示例只列 q_proj/v_proj；`generate_with_loss` 被称为回调但未提供实现或版本。显存降低 4×、WER 增加 <0.3、音频不足 10 小时必须冻结编码器都是未验证的经验断言。示例说 Turbo 约 3M 可训练参数，SVG 写 0.65M，main.py 的简式又假设编码器/解码器层数相等，且未独立计入解码器交叉注意力，不能视为真实 LoRA 参数统计。
6. main.py `chunk_schedule`：stride_s 实际被当作重叠长度，步进为 chunk_s - stride_s；对于长输入，若 stride_s >= chunk_s，会不前进或倒退且循环缺少边界防护。中文源码载荷不变，本次没有运行 main，也没有用病态输入实验。
7. main.py `encoder_frames`、`transformer_params` 和 Turbo 分支：帧数公式使用未填充的窗口计数，而打印文案同时声称 3000/1500；参数预算忽略/简化了一些结构，Turbo 分支以编码器块计数替代解码器块计数。示例只是近似预算，不能确认真实模型形状或参数量。
8. b0055–b0075、b0087、b0095：`pad=False`、`language="auto"`、WhisperX 参数与直接传文件名、PEFT task_type/模型兼容性、generate 返回注意力形状等需要按指定库版本核验。步骤 4 中 torch/features 没有在前文构造；单段 transcribe 示例也没有实际展示额外的对齐和说话人分离步骤。未把这些步骤说成已验证可运行。
9. b0095 / main.py：练习声称 main 对提示词“分词”，实际是拼接已写好的特殊 token 字符串；声称计算解码形状预算，而文件主要打印提示词、分块安排和粗略参数预算。包内没有 quiz.json、tests 或 Learning Objectives 章节。翻译不补造这些内容。
10. b0075、b0099 / SVG：注意力对角线被直接解释成词时间戳，SVG 又将时间戳与词级对齐等同；这不等于经过独立强制对齐的保证。SVG 中文字、尺寸、箭头和已有技术数字均逐字复制；尚未实际 GFM 检查或执行/渲染 SVG。

## NOT_RUN 与有界 CPU 提案

本次未运行课程 main、课程 import、测试、Whisper 模型、训练、音频下载/访问、API、GPU、网络或安装；未执行 SVG/figure/Mermaid。原 curated_translation 的纯本地记录检查和组装不属于课程运行。

如协调者之后需要额外安全分析，可以先审阅一个独立、有限、仅标准库的检查提案：静态 AST 检查函数体；只讨论有效且有界的 build_prompt 三个 LANG 键、encoder_frames 的固定正时长、chunk_schedule 在 total=600/chunk=30/overlap=5 的有限调度。该提案目前 NOT_RUN，不授权 import 原 main、模型执行或病态循环输入，也不以此验证实际 ASR/微调性能。


## 原独立审校保留的源边界

~~~json
[
  {
    "id": "SR01",
    "classification": "SOURCE_ONLY_NOT_TRANSLATION_DEFECT",
    "title": "模型版本规格混合",
    "segment_ids": [
      "06-05:b0003",
      "06-05:b0021",
      "06-05:b0039"
    ],
    "source_target_line_ranges": [
      {
        "segment_id": "06-05:b0003",
        "source": [
          3,
          3
        ],
        "target": [
          3,
          3
        ]
      },
      {
        "segment_id": "06-05:b0021",
        "source": [
          26,
          29
        ],
        "target": [
          26,
          29
        ]
      },
      {
        "segment_id": "06-05:b0039",
        "source": [
          51,
          59
        ],
        "target": [
          51,
          59
        ]
      }
    ],
    "additional_static_source_paths": [
      "phases/06-speech-and-audio/05-whisper-architecture-finetuning/assets/whisper.svg"
    ],
    "reason": "680k、99种语言、80mels和51865词表与Large-v3/Turbo并列而缺版本适用边界。译文忠实保留；未以外部资料替换。",
    "disposition": "保留固定源字节和译文对应；必要时另起源更正流程；本次不执行、不联网、不暗修。"
  },
  {
    "id": "SR02",
    "classification": "SOURCE_ONLY_NOT_TRANSLATION_DEFECT",
    "title": "language/task/timestamp token 语义",
    "segment_ids": [
      "06-05:b0029",
      "06-05:b0031"
    ],
    "source_target_line_ranges": [
      {
        "segment_id": "06-05:b0029",
        "source": [
          39,
          41
        ],
        "target": [
          39,
          41
        ]
      },
      {
        "segment_id": "06-05:b0031",
        "source": [
          43,
          43
        ],
        "target": [
          43,
          43
        ]
      }
    ],
    "additional_static_source_paths": [
      "phases/06-speech-and-audio/05-whisper-architecture-finetuning/code/main.py",
      "phases/06-speech-and-audio/05-whisper-architecture-finetuning/assets/whisper.svg"
    ],
    "reason": "英文将language标签与翻译/转写控制混同，transcribe/translate后的解释顺序易反配；main静态文本把language/task分开。notimestamps直接称词级时间戳也有边界。未暗修。",
    "disposition": "保留固定源字节和译文对应；必要时另起源更正流程；本次不执行、不联网、不暗修。"
  },
  {
    "id": "SR03",
    "classification": "SOURCE_ONLY_NOT_TRANSLATION_DEFECT",
    "title": "log-mel归一化来源与强因果",
    "segment_ids": [
      "06-05:b0035",
      "06-05:b0087"
    ],
    "source_target_line_ranges": [
      {
        "segment_id": "06-05:b0035",
        "source": [
          47,
          47
        ],
        "target": [
          47,
          47
        ]
      },
      {
        "segment_id": "06-05:b0087",
        "source": [
          158,
          161
        ],
        "target": [
          158,
          161
        ]
      }
    ],
    "additional_static_source_paths": [],
    "reason": "均值/标准差公式和训练语料统计来源是固定源断言；librosa替换导致近随机输出未给条件。保护公式/API，不将源问题算译错。",
    "disposition": "保留固定源字节和译文对应；必要时另起源更正流程；本次不执行、不联网、不暗修。"
  },
  {
    "id": "SR04",
    "classification": "SOURCE_ONLY_NOT_TRANSLATION_DEFECT",
    "title": "性能、延迟及WER比较口径",
    "segment_ids": [
      "06-05:b0023",
      "06-05:b0039",
      "06-05:b0047",
      "06-05:b0083",
      "06-05:b0103"
    ],
    "source_target_line_ranges": [
      {
        "segment_id": "06-05:b0023",
        "source": [
          31,
          31
        ],
        "target": [
          31,
          31
        ]
      },
      {
        "segment_id": "06-05:b0039",
        "source": [
          51,
          59
        ],
        "target": [
          51,
          59
        ]
      },
      {
        "segment_id": "06-05:b0047",
        "source": [
          71,
          71
        ],
        "target": [
          71,
          71
        ]
      },
      {
        "segment_id": "06-05:b0083",
        "source": [
          154,
          154
        ],
        "target": [
          154,
          154
        ]
      },
      {
        "segment_id": "06-05:b0103",
        "source": [
          187,
          191
        ],
        "target": [
          187,
          191
        ]
      }
    ],
    "additional_static_source_paths": [],
    "reason": "8×/<1%、A100表Latency与实时倍数混用、社区WER、最快/完全相同缺测量条件。新增S2仅修中文倍率，不认证源数值。",
    "disposition": "保留固定源字节和译文对应；必要时另起源更正流程；本次不执行、不联网、不暗修。"
  },
  {
    "id": "SR05",
    "classification": "SOURCE_ONLY_NOT_TRANSLATION_DEFECT",
    "title": "LoRA模块、参数量及微调经验",
    "segment_ids": [
      "06-05:b0045",
      "06-05:b0067",
      "06-05:b0099"
    ],
    "source_target_line_ranges": [
      {
        "segment_id": "06-05:b0045",
        "source": [
          65,
          69
        ],
        "target": [
          65,
          69
        ]
      },
      {
        "segment_id": "06-05:b0067",
        "source": [
          111,
          122
        ],
        "target": [
          111,
          122
        ]
      },
      {
        "segment_id": "06-05:b0099",
        "source": [
          175,
          183
        ],
        "target": [
          175,
          183
        ]
      }
    ],
    "additional_static_source_paths": [
      "phases/06-speech-and-audio/05-whisper-architecture-finetuning/code/main.py",
      "phases/06-speech-and-audio/05-whisper-architecture-finetuning/assets/whisper.svg"
    ],
    "reason": "正文q/k/v而代码q/v，代码约3M与SVG0.65M冲突；main层数和交叉注意力统计简化。4×显存、<0.3WER、<10小时冻结规则仍为未验证源经验。",
    "disposition": "保留固定源字节和译文对应；必要时另起源更正流程；本次不执行、不联网、不暗修。"
  },
  {
    "id": "SR06",
    "classification": "SOURCE_ONLY_NOT_TRANSLATION_DEFECT",
    "title": "分块循环边界",
    "segment_ids": [],
    "source_target_line_ranges": [],
    "additional_static_source_paths": [
      "phases/06-speech-and-audio/05-whisper-architecture-finetuning/code/main.py"
    ],
    "reason": "stride_s实为重叠；step=chunk_s-stride_s，在长输入且stride_s>=chunk_s时可能不前进。仅静态阅读，无病态输入执行。",
    "disposition": "保留固定源字节和译文对应；必要时另起源更正流程；本次不执行、不联网、不暗修。"
  },
  {
    "id": "SR07",
    "classification": "SOURCE_ONLY_NOT_TRANSLATION_DEFECT",
    "title": "帧数与Transformer预算近似",
    "segment_ids": [],
    "source_target_line_ranges": [],
    "additional_static_source_paths": [
      "phases/06-speech-and-audio/05-whisper-architecture-finetuning/code/main.py"
    ],
    "reason": "encoder_frames未填充计数与打印3000/1500关系未交代；参数预算简化，Turbo分支将enc作为dec。不是翻译改写的范围。",
    "disposition": "保留固定源字节和译文对应；必要时另起源更正流程；本次不执行、不联网、不暗修。"
  },
  {
    "id": "SR08",
    "classification": "SOURCE_ONLY_NOT_TRANSLATION_DEFECT",
    "title": "库版本/API/缺上下文",
    "segment_ids": [
      "06-05:b0045",
      "06-05:b0055",
      "06-05:b0057",
      "06-05:b0061",
      "06-05:b0067",
      "06-05:b0073",
      "06-05:b0075",
      "06-05:b0087",
      "06-05:b0095"
    ],
    "source_target_line_ranges": [
      {
        "segment_id": "06-05:b0045",
        "source": [
          65,
          69
        ],
        "target": [
          65,
          69
        ]
      },
      {
        "segment_id": "06-05:b0055",
        "source": [
          81,
          94
        ],
        "target": [
          81,
          94
        ]
      },
      {
        "segment_id": "06-05:b0057",
        "source": [
          96,
          96
        ],
        "target": [
          96,
          96
        ]
      },
      {
        "segment_id": "06-05:b0061",
        "source": [
          100,
          105
        ],
        "target": [
          100,
          105
        ]
      },
      {
        "segment_id": "06-05:b0067",
        "source": [
          111,
          122
        ],
        "target": [
          111,
          122
        ]
      },
      {
        "segment_id": "06-05:b0073",
        "source": [
          128,
          137
        ],
        "target": [
          128,
          137
        ]
      },
      {
        "segment_id": "06-05:b0075",
        "source": [
          139,
          139
        ],
        "target": [
          139,
          139
        ]
      },
      {
        "segment_id": "06-05:b0087",
        "source": [
          158,
          161
        ],
        "target": [
          158,
          161
        ]
      },
      {
        "segment_id": "06-05:b0095",
        "source": [
          169,
          171
        ],
        "target": [
          169,
          171
        ]
      }
    ],
    "additional_static_source_paths": [],
    "reason": "generate_with_loss、pad=False、language=\"auto\"、WhisperX入参、PEFT兼容性、generate注意力结构都未核版本；Step4的torch/features未构造。没有模型或API运行。",
    "disposition": "保留固定源字节和译文对应；必要时另起源更正流程；本次不执行、不联网、不暗修。"
  },
  {
    "id": "SR09",
    "classification": "SOURCE_ONLY_NOT_TRANSLATION_DEFECT",
    "title": "练习描述与实际课程包",
    "segment_ids": [
      "06-05:b0095"
    ],
    "source_target_line_ranges": [
      {
        "segment_id": "06-05:b0095",
        "source": [
          169,
          171
        ],
        "target": [
          169,
          171
        ]
      }
    ],
    "additional_static_source_paths": [
      "phases/06-speech-and-audio/05-whisper-architecture-finetuning/code/main.py"
    ],
    "reason": "main拼接特殊token字符串而非真正分词，主要提示词/分块/粗参数预算；包无quiz/tests/Learning Objectives。保持源正文，不补造。",
    "disposition": "保留固定源字节和译文对应；必要时另起源更正流程；本次不执行、不联网、不暗修。"
  },
  {
    "id": "SR10",
    "classification": "SOURCE_ONLY_NOT_TRANSLATION_DEFECT",
    "title": "注意力与词级时间戳/强制对齐",
    "segment_ids": [
      "06-05:b0075",
      "06-05:b0099"
    ],
    "source_target_line_ranges": [
      {
        "segment_id": "06-05:b0075",
        "source": [
          139,
          139
        ],
        "target": [
          139,
          139
        ]
      },
      {
        "segment_id": "06-05:b0099",
        "source": [
          175,
          183
        ],
        "target": [
          175,
          183
        ]
      }
    ],
    "additional_static_source_paths": [
      "phases/06-speech-and-audio/05-whisper-architecture-finetuning/assets/whisper.svg"
    ],
    "reason": "注意力对角线及timestamp token不能仅凭源文字等同完整强制对齐保证；SVG将时间戳与词级对齐混用。原SVG逐字复制且未渲染。",
    "disposition": "保留固定源字节和译文对应；必要时另起源更正流程；本次不执行、不联网、不暗修。"
  }
]
~~~

固定源准备风险（未暗改源）：

~~~json
[
  {
    "where": "docs/en.md architecture/prompt/normalization; assets/whisper.svg",
    "finding": "Mel count/vocab/training corpus are presented across Whisper variants without full distinction; language versus task tokens, word timestamps and normalization statements require source-risk handling. Preserve fixed source values/claims; this preparation has not verified external model specs or APIs."
  },
  {
    "where": "code/main.py chunk_schedule/encoder_frames/parameter helpers",
    "finding": "stride_s means overlap although namedstride; stride_s>=chunk_s can fail to advance for long inputs, no input guards. encoder_frames uses unpadded framing while prose reports fixed3000/1500. Turbo decoder accounting replaces decoder with encoder-block count; LoRA formula assumes equal encoder/decoder layer counts and omits cross-attention distinctions."
  },
  {
    "where": "docs/en.md code/exercises; package",
    "finding": "Main prints prompt strings/chunk schedules/approximatebudgets, not real tokenization, ASR or fine-tuning. Source LoRA numbers differ across snippet/main/SVG; API flags/normalization/performance claims are unverified. Protected SVG later needs actual GFM check; no quiz/tests/learning-objectives section. No audio access/download/install/inference authorized."
  }
]
~~~

CPU 提案准确原证据 SOURCE-RISKS.md，SHA256 5dfdd86e02994d833b805f59ececff56ffbca9dd487bf86405ac944e32da8bab，4564 B；状态 NOT_RUN。

原 SVG 精确复制证据（仅静态字节保护，不是渲染通过）：

~~~json
[
  {
    "source_path": "phases/06-speech-and-audio/05-whisper-architecture-finetuning/assets/whisper.svg",
    "target_path": "i18n/zh/phases/06-speech-and-audio/05-whisper-architecture-finetuning/assets/whisper.svg",
    "source_commit": "1bafaa88bb4668356791150bec3a6d7df38387eb",
    "source_blob": "e7aa02bb29d58d9b62080f6587cdce10129c16e9",
    "sha256": "506ab49ee0f6166891cba1198e28fbfe4d1f0b1d889614eef655fab2fe7ed3c3",
    "bytes": 5576,
    "copied_unchanged": true,
    "relative_SVG_in_body": true,
    "executed_or_rendered": false
  }
]
~~~

本轮仅本地支持候选装配。课程main/import/tests、CPU/GPU/model、API/network/install/service、strict、GFM、离线重放及累计回归均未运行；没有远端、INDEX或queue改动。所有源风险和后续发布关卡仍按真实证据分别保留。
