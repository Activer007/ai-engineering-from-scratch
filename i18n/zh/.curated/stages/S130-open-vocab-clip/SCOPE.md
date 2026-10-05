# S130-open-vocab-clip English-first 支持范围

状态：本地 own3 候选，未安装、未发布，不增加正式课程数。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；原控制 f9b5e9cbe4012f54483794f920c0d87b06a7573d。

## 当前正文与独立审校身份

- Lesson: 04-18
- Current target SHA256: 7188a3caf7cfbacde3d690c1a3fd9f74026bbbe95cf040d592fccc5c32766237 (10663 B)
- Current draft record SHA256: 9188dba9b3428d67831708fa733bc893439f3bf70d320f8866d49fef9dd7c73b (48417 B)
- Historical author handoff SHA256: 9694e2c113404d0ea8cb50422a1c99518d5b9b273c4ea34cd42189402aa84032
- Current handoff SHA256: 9694e2c113404d0ea8cb50422a1c99518d5b9b273c4ea34cd42189402aa84032
- Original full independent review SHA256: 8f7b40f9e8430574b09447c691caa8da1259268effe31ba22ea1523bf0c90539
- Current incremental closure SHA256: not applicable; full review binds current bytes
- First complete body SHA256: e5962163208ed9dcd6d3aa5ebeffe7ce05e0f36f1f2e9f91e301ee044cd0ad51
- First-capture record SHA256: 0925bb1ba00a35dfe27707a7f910fe316f5938615fac62b328f64d2d28be598c
- First successful capture record SHA256: 0925bb1ba00a35dfe27707a7f910fe316f5938615fac62b328f64d2d28be598c
- Historical exact-byte local strict evidence SHA256: 5cdc38efe5d0d6d7c02dedf0c48ae8c858fe0d530cad6954e4d700f07b57f1c8; not rerun

First complete body and first capture succeeded. R01 changes record provenance date only, with identical body and empty body diff; R02 changes three prose passages. Two true revision events, one body revision, one metadata-only event. Current complete111-block independent review binds final R02 body/record.

真实审校先后与各自原身份：

~~~json
[
  {
    "sha256": "8f7b40f9e8430574b09447c691caa8da1259268effe31ba22ea1523bf0c90539",
    "bytes": 167646,
    "status": "PASS_TRANSLATION_WITH_SOURCE_RISKS_OPEN"
  }
]
~~~

真实修订身份与时间（同字节快照不增加修订数）：

~~~json
[
  {
    "revision": "R01",
    "before_utc": "2026-10-04T22:19:57.677283+00:00",
    "after_utc": "2026-10-04T22:19:57.705108+00:00",
    "receipt_sha256": "7baae7d12dd899e10aecd77a5c785797696eaf02cc913b6923bc33608883670e",
    "old_target_sha256": "e5962163208ed9dcd6d3aa5ebeffe7ce05e0f36f1f2e9f91e301ee044cd0ad51",
    "new_target_sha256": "e5962163208ed9dcd6d3aa5ebeffe7ce05e0f36f1f2e9f91e301ee044cd0ad51",
    "diff_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "old_record_sha256": "0925bb1ba00a35dfe27707a7f910fe316f5938615fac62b328f64d2d28be598c",
    "new_record_sha256": "8e67a2be5564ed0bbe17fff0a80d8b8f82b6de259cf70745e38e887ad7672892",
    "record_diff_sha256": "7d3b39769b820b8c62dbbaaa84cf1c3f58a1b9193584117c9bcaaeed88af92db",
    "same_byte_alias_only": false
  },
  {
    "revision": "R02",
    "before_utc": "2026-10-04T22:21:21.382576+00:00",
    "after_utc": "2026-10-04T22:21:21.423414+00:00",
    "receipt_sha256": "5cdc38efe5d0d6d7c02dedf0c48ae8c858fe0d530cad6954e4d700f07b57f1c8",
    "old_target_sha256": "e5962163208ed9dcd6d3aa5ebeffe7ce05e0f36f1f2e9f91e301ee044cd0ad51",
    "new_target_sha256": "7188a3caf7cfbacde3d690c1a3fd9f74026bbbe95cf040d592fccc5c32766237",
    "diff_sha256": "b00fab2035949c7e66d96bcc2f7ce9910d977cf7f10f3e819ab73f99bf58295a",
    "old_record_sha256": "8e67a2be5564ed0bbe17fff0a80d8b8f82b6de259cf70745e38e887ad7672892",
    "new_record_sha256": "9188dba9b3428d67831708fa733bc893439f3bf70d320f8866d49fef9dd7c73b",
    "record_diff_sha256": "9f21fff9883a22022962f7dbfaae38482fe4717a328f69e3896e283942c66156",
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

源先修原文：**Prerequisites:** Phase 4 Lesson 14 (ViT), Phase 4 Lesson 17 (Self-Supervised)

仅以固定英文及相关术语为翻译前提，不添加中文先修正式验收门槛。作者与审校者的亲读和固定既有英文全文复用按各自原报告保留；本轮仅装配支持候选，不新增语言二审或全文亲读声明。

冻结源准备 formal138/actual138，INDEX commit 4832660521df7d71a336615cb30ec59794a2db06，INDEX SHA256 1bc111580519ff8d68dce14547c373fd659d0320b4d5e0b5fc1fc87c4bf6223f，独立回执 SHA256 2d2284aa3eec2c4fb1f5aa89d9577a56d8a00647e7c89d61895fbe9e53685a0e。这是 2026-10-04T22:08:48.908492+00:00 源准备时的真实快照，未追刷当前计数；不覆盖本三课，也不借历史回归宣称其已通过。

## 作者源风险与有限提案

原源风险 SHA256 99a5677a1d30dd4eb16ce8d3e20534f4870dbdbfdfc9bd3161b07968411bfb9a (4032 B)。以下原静态观察与历史 NOT_RUN 文字照录，原作者“strict 未执行”等若出现，仅反映该风险文件写作时点，不能覆盖后来的独立检查回执：

# S130 固定英文源风险与执行边界

状态：静态源观察，未外查最新模型规格，未执行课程代码；不改英文或忠实中文正文。以下风险不是译文检查器例外。

固定英文 commit：1bafaa88bb4668356791150bec3a6d7df38387eb。

1. docs/en.md:23、80–89 将现代视觉系统、SAM、DALL-E 3、所有视觉语言任务都归为 CLIP 式联合嵌入或距离计算，语气非常绝对；架构族和版本间的区别没有在源文中说明。这些属于待专业事实核实的源断言，本稿保持原来的范围、因果和语气。
2. docs/en.md:31–32、41 将 CLIP-L/14 的共同投影嵌入维度写为 1024；具体编码器宽度与投影输出维度可能被混同。Mermaid 和数字原样保留；这里没有联网核验，也没有把记忆中的其他模型尺寸写入译文。
3. docs/en.md:55、112、121、关键术语表将温度、logit_scale 并列描述。数学式使用除以 tau；代码先对内部对数参数取 exp，再作为乘数。逆温度和其对数参数不能直接与 tau 当成同一个量。源代码保留，译文不暗改表格定义。
4. docs/en.md 合理性检查及 code/main.py:47–52 期望随机初始化损失接近 log(8)。随机但非均匀的缩放 logits 不保证这个值；这里没有产生实测损失，亦不把“应接近”升级为已验证。代码对学习中的缩放因子没有上界保护。
5. code/main.py:55–84 用 5 个潜在原型生成训练和测试特征，测试图像仍来自这些类别；class_text 直接使用同一组原型。打印 zero-shot accuracy 不足以证明未见自然语言类别迁移。批次内同类实例被当成非对角线负样本，任务假设与自然语言图像对不同。
6. docs/en.md:66、78、Use It 与 Exercises 中的 SigLIP 优势、2026 默认选择、80 模板和 CIFAR-10 85-90% 等是未复现的源断言。源百分比仍为百分比，未改为百分点；没有声称达到准确率或召回率。
7. outputs/skill-image-text-retriever.md:23、44–52 允许 SigLIP 模型 ID，但模板固定使用 CLIPModel/CLIPProcessor；“any CLIP checkpoint”能力也未经核验。IVF 分支:81–85 没有明确传入内积度量，而正文承诺归一化向量的余弦检索。未验证外部依赖版本或构造函数默认值。
8. 检索模板:57–65 没有空目录或图像解码失败防护；:92–100 没有建索引前查询、非法 k 或返回补齐索引的防护。IVF 最少 4 个中心与少量图像的训练兼容性也未处理。批量内处理和文件资源清理未示范。
9. 输出模板提出“少于100k最简单最快”等规模经验与提示词模板大小写/上级类别的一般化断言，没有本课证据。它们只作为完整源包理解背景；本任务仅翻译 docs 正文，不改输出文件。
10. quiz.json 有 5 题（2 pre、3 post），没有 lesson/title 字段或 check 阶段，与根规范的 6 题模式不符；本课没有测试文件。quiz 对零样本分类检索方向及所有SOTA VLM的解释也含未证实的概括。未调整题库或运行任何课程审计来掩盖这些差异。
11. docs 中两个无标签围栏已仅加 text 语言标签，载荷不变；Mermaid 和 figure 的英文图载荷不变。没有相对 SVG 资源，不需复制 assets。GFM、站点交互图、移动端和PDF均未渲染。

## NOT_RUN 与有限 CPU 提案

课程 main、课程 import、课程 tests、Torch/OpenCLIP/FAISS 模型执行、CPU/GPU 训练与推理、下载、联网/API、安装全部 NOT_RUN。未调用课程代码、未加载模型，也未尝试安装缺失依赖。

若后续单独授权，可考虑一个有限、离线、标准库的 2×2 手工相似度矩阵演示：只比较固定小矩阵在 tau=1 和 tau=0.5 下的行列交叉熵，限制固定两组输入、无循环训练、无课程 import、无模型/图像文件读取、无第三方依赖及网络。此项仅是 NOT_RUN 提案，不是本次验证，也不能验证 CLIP 性能或课程主程序。


## 原独立审校保留的源边界

~~~json
[
  {
    "id": "SRC01",
    "category": "FIXED_ENGLISH_SOURCE_RISK_NOT_TRANSLATION_DEFECT",
    "title": "CLIP投影维度与编码器宽度",
    "locations": [
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          29,
          41
        ]
      }
    ],
    "related_segments": [
      "04-18:b0023",
      "04-18:b0025"
    ],
    "observation": "ViT-L/14 的共同投影嵌入写为1024，疑似与编码器隐藏宽度混同；不能因另一课程写ViT-L宽度1024而推定CLIP投影也为1024。此审没有联网核验具体模型配置。",
    "required_source_followup": "在另行授权的英文事实修订中核对指定CLIP checkpoint配置及论文架构表；获准后再同步数字与图。忠实中文和Mermaid均不私改。",
    "status": "OPEN",
    "translation_change_requested": false,
    "publication_boundary": "不得据语言审校PASS宣称技术事实、可运行指导或教学发布已通过"
  },
  {
    "id": "SRC02",
    "category": "FIXED_ENGLISH_SOURCE_RISK_NOT_TRANSLATION_DEFECT",
    "title": "模型族及任务范围过度泛化",
    "locations": [
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          23,
          23
        ]
      },
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          80,
          99
        ]
      },
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          220,
          220
        ]
      }
    ],
    "related_segments": [
      "04-18:b0017",
      "04-18:b0053",
      "04-18:b0055",
      "04-18:b0063",
      "04-18:b0107"
    ],
    "observation": "every modern vision system、SAM、DALL-E 3、Grounding DINO、全部VLM与视觉语言任务的概括未区分具体模型版本、CLIP式对齐与实际架构；“每项任务都成为距离计算”并不足以描述生成和密集预测。正文“Real CLIP is ViT + transformer”也未区分CLIP图像编码器变体。",
    "required_source_followup": "按具体模型版本分别核对主干、文本塔与生成/检测/分割机制，再修英文范围；本次只记录源风险，不把中文的全称语气归罪译者。",
    "status": "OPEN",
    "translation_change_requested": false,
    "publication_boundary": "不得据语言审校PASS宣称技术事实、可运行指导或教学发布已通过"
  },
  {
    "id": "SRC03",
    "category": "FIXED_ENGLISH_SOURCE_RISK_NOT_TRANSLATION_DEFECT",
    "title": "温度、逆温度与对数参数混称",
    "locations": [
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          48,
          55
        ]
      },
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          112,
          120
        ]
      },
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          127,
          134
        ]
      },
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          215,
          215
        ]
      }
    ],
    "related_segments": [
      "04-18:b0031",
      "04-18:b0033",
      "04-18:b0065",
      "04-18:b0067",
      "04-18:b0071",
      "04-18:b0073",
      "04-18:b0107"
    ],
    "observation": "伪代码以tau为除数，模型内部参数取exp后作为乘数；tau、逆温度、其对数并非同一个标量。术语表把Temperature / logit_scale与tau并列，会混淆参数角色。",
    "required_source_followup": "另行修订英文以分清tau、内部logit_scale及exp(logit_scale)；不得在此次译文表格中擅自修正源定义。",
    "status": "OPEN",
    "translation_change_requested": false,
    "publication_boundary": "不得据语言审校PASS宣称技术事实、可运行指导或教学发布已通过"
  },
  {
    "id": "SRC04",
    "category": "FIXED_ENGLISH_SOURCE_RISK_NOT_TRANSLATION_DEFECT",
    "title": "随机损失不保证接近log(N)",
    "locations": [
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          156,
          167
        ]
      },
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/code/main.py",
        "lines": [
          47,
          52
        ]
      }
    ],
    "related_segments": [
      "04-18:b0083",
      "04-18:b0085"
    ],
    "observation": "log(N)是均匀预测交叉熵基线；随机初始化加缩放并不保证每行/列logits接近相等。没有执行模型，不能宣称固定seed实测应等于或接近2.08。",
    "required_source_followup": "英文需说明均匀或近均匀预测条件，并在另行获准运行后报告真实测量；本次不运行Torch、不改数字。",
    "status": "OPEN",
    "translation_change_requested": false,
    "publication_boundary": "不得据语言审校PASS宣称技术事实、可运行指导或教学发布已通过"
  },
  {
    "id": "SRC05",
    "category": "FIXED_ENGLISH_SOURCE_RISK_NOT_TRANSLATION_DEFECT",
    "title": "合成同类原型评估称zero-shot",
    "locations": [
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/code/main.py",
        "lines": [
          55,
          84
        ]
      },
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          99,
          99
        ]
      },
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          152,
          152
        ]
      }
    ],
    "related_segments": [
      "04-18:b0063",
      "04-18:b0079"
    ],
    "observation": "训练和测试均用同一5类proto；class_text直接来自proto，不是自然语言文本编码。held-out images仅留出实例，不能证明未见类零样本迁移或真实开放词表能力。同类批次样本又被非对角负样本损失推开。",
    "required_source_followup": "英文中区分玩具跨模态对齐/同类原型匹配与真实零样本迁移；任务与标题修订需另行授权。不得把源码打印zero-shot accuracy当验收结果。",
    "status": "OPEN",
    "translation_change_requested": false,
    "publication_boundary": "不得据语言审校PASS宣称技术事实、可运行指导或教学发布已通过"
  },
  {
    "id": "SRC06",
    "category": "FIXED_ENGLISH_SOURCE_RISK_NOT_TRANSLATION_DEFECT",
    "title": "性能、年代与默认选择未复现",
    "locations": [
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          66,
          78
        ]
      },
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          171,
          207
        ]
      },
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          217,
          219
        ]
      }
    ],
    "related_segments": [
      "04-18:b0041",
      "04-18:b0049",
      "04-18:b0089",
      "04-18:b0093",
      "04-18:b0103",
      "04-18:b0107"
    ],
    "observation": "SigLIP优势、OpenCLIP社区默认、新项目首选、80模板增益与85-90%依赖模型版本、数据、提示词及评估配置，未在本次复现或进行2026时效调查。1-3%源单位不可擅改百分点。",
    "required_source_followup": "另行补充实验配置和来源核验；当前只可称忠实翻译，不能承诺准确率或时下首选。",
    "status": "OPEN",
    "translation_change_requested": false,
    "publication_boundary": "不得据语言审校PASS宣称技术事实、可运行指导或教学发布已通过"
  },
  {
    "id": "SRC07",
    "category": "FIXED_ENGLISH_SOURCE_RISK_NOT_TRANSLATION_DEFECT",
    "title": "检索输出的模型与索引契约",
    "locations": [
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/outputs/skill-image-text-retriever.md",
        "lines": [
          23,
          52
        ]
      },
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/outputs/skill-image-text-retriever.md",
        "lines": [
          81,
          89
        ]
      }
    ],
    "related_segments": [
      "04-18:b0099"
    ],
    "observation": "输入示例允许SigLIP，模板却固定CLIPModel/CLIPProcessor；any checkpoint缺少兼容性路由。IVF构造没有显式传入内积metric，与文字承诺余弦检索存在需核验的契约风险；未查询依赖版本默认值。",
    "required_source_followup": "在单独实现修订中使用正确模型/processor并明确每种索引metric和模型支持范围；保持本次输出源码不动。",
    "status": "OPEN",
    "translation_change_requested": false,
    "publication_boundary": "不得据语言审校PASS宣称技术事实、可运行指导或教学发布已通过"
  },
  {
    "id": "SRC08",
    "category": "FIXED_ENGLISH_SOURCE_RISK_NOT_TRANSLATION_DEFECT",
    "title": "检索边界及规模断言",
    "locations": [
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/outputs/skill-image-text-retriever.md",
        "lines": [
          57,
          100
        ]
      },
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/outputs/skill-image-text-retriever.md",
        "lines": [
          116,
          120
        ]
      }
    ],
    "related_segments": [],
    "observation": "空目录将np.concatenate空列表；少图像IVF至少4中心、建索引前查询、非法k/补齐索引和坏图像没有显式处理。按图像规模宣称索引最快没有本课实验证据。",
    "required_source_followup": "单独处理边界验证、资源关闭及性能基准；本次不得安装FAISS或执行模板。",
    "status": "OPEN",
    "translation_change_requested": false,
    "publication_boundary": "不得据语言审校PASS宣称技术事实、可运行指导或教学发布已通过"
  },
  {
    "id": "SRC09",
    "category": "FIXED_ENGLISH_SOURCE_RISK_NOT_TRANSLATION_DEFECT",
    "title": "题库与课程结构缺口",
    "locations": [
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/quiz.json",
        "lines": [
          1,
          39
        ]
      }
    ],
    "related_segments": [],
    "observation": "题库静态为5题（2pre/3post），无check及lesson/title字段，与根课程契约不同；固定课程树无tests。第一题说明把给图像与类别文本比较称为text-to-image，方向用词与输入查询语义不一致；VLM桥接的普遍化仍待事实审查。",
    "required_source_followup": "作为英文课程问题另行修题库/规范，不运行课程tests或审计来伪装已经通过；翻译范围仅docs。",
    "status": "OPEN",
    "translation_change_requested": false,
    "publication_boundary": "不得据语言审校PASS宣称技术事实、可运行指导或教学发布已通过"
  },
  {
    "id": "SRC10",
    "category": "FIXED_ENGLISH_SOURCE_RISK_NOT_TRANSLATION_DEFECT",
    "title": "首句同一点与损失简化",
    "locations": [
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          3,
          3
        ]
      },
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          61,
          66
        ]
      },
      {
        "path": "phases/04-computer-vision/18-open-vocab-clip/docs/en.md",
        "lines": [
          214,
          214
        ]
      }
    ],
    "related_segments": [
      "04-18:b0003",
      "04-18:b0039",
      "04-18:b0041",
      "04-18:b0107"
    ],
    "observation": "same point是理想化直觉，对比学习目标实际提高匹配相似度；SigLIP伪公式省略实现细节；no labels touched应理解为无任务专属标签训练，而不是网络图文预训练完全不含标签概念。译文保留这些源简化。",
    "required_source_followup": "教学发布时在英文源明确直觉与实现/评估范围，必要时说明零样本相对于目标任务；本次不追加原文没有的技术断言。",
    "status": "OPEN",
    "translation_change_requested": false,
    "publication_boundary": "不得据语言审校PASS宣称技术事实、可运行指导或教学发布已通过"
  }
]
~~~

固定源准备风险（未暗改源）：

~~~json
[
  {
    "where": "docs/en.md two towers/use cases; main.py",
    "finding": "CLIP variant projection dimensions, SAM/DALL-E/VLM family and dated performance claims are unverified source assertions. Synthetic main trains on five latent prototypes then evaluates the same prototype classes; its printed zero-shot label does not demonstrate transfer to unseen natural-language classes."
  },
  {
    "where": "docs/en.md random-loss claim; main.py loss/temperature",
    "finding": "Random initialized scaled nonuniform logits need not yield exactly log(N). Learnable exponentiated logit scale is unbounded; duplicate class examples become batch negatives. Preserve tau versus inverse scale and no measured loss/accuracy claims."
  },
  {
    "where": "outputs/skill-image-text-retriever.md; package",
    "finding": "Template promises arbitraryCLIP/SigLIP and cosine indexing but hardcodes CLIP classes and does not explicitly set IVF metric. Empty image folder, failed image decode, invalid/padded search indices and pre-build query are not guarded. Third-party model downloads/FAISS not run. Quiz5(2pre/3post), no lesson/title fields or tests; figures/fences protected."
  }
]
~~~

CPU 提案准确原证据 SOURCE-RISKS.md，SHA256 99a5677a1d30dd4eb16ce8d3e20534f4870dbdbfdfc9bd3161b07968411bfb9a，4032 B；状态 NOT_RUN。

本轮仅本地支持候选装配。课程main/import/tests、CPU/GPU/model、API/network/install/service、strict、GFM、离线重放及累计回归均未运行；没有远端、INDEX或queue改动。所有源风险和后续发布关卡仍按真实证据分别保留。
