# S124-vision-pipeline-capstone English-first 支持范围

状态：本地 own3 候选，未安装、未发布、不增加正式课程数。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；原控制 `f9b5e9cbe4012f54483794f920c0d87b06a7573d`。

## 当前作者与独立审校身份

- Lesson: 04-16
- Target SHA256: a2bca65f436e398a9532106afab8e2f77de395d7d755cd7e56dee7df5442546b (15947 B)
- Original author record SHA256: ac042f153411b17873b419a76e286afb1d07f88cf9f003f2c4ba9aa831d228ae (90259 B), status=draft
- Author handoff SHA256: dbd4a7335f45f878c8e67c8ba53a542de780dcc5704034bdd7a0e3510d2cf27a
- Original independent review SHA256: 9b0a5f710c302522fb44067a542589259bc600b4bd93ed2cb5ad34af74bc7494; companion SHA256: 8f8986591557947de4ae049119bb844b425f8a0b5a94ebb6756357bfc518f170
- First complete body SHA256: 6c5e0c93db4540929a14df22463947ec85e08cf9ddf697de77283af1bc6bc580
- First-body record SHA256: b111d4fcf9b1427a1c32eb2dd7158308273b8d27382ac3cf658ee3547f482a03
- Original local strict evidence SHA256: 5ae2d569bebf2c9f378e8d96d4ea728241b5c4969b84061ad9583ab6910d6163; cached evidence only, not rerun

109块完整独审；审校者亲读04-01、04-08、04-15及04-06定向段落，其余先修复用固定准备阅读证据。

Preflight 2026-10-04T20:50:22.248358+00:00; first body written 2026-10-04T20:52:46.563933+00:00, with no separately recorded before-write time. First original capture succeeded; first record snapshot 2026-10-04T20:52:58.260161+00:00. One real body/record revision 2026-10-04T20:54:28.359095+00:00 to 2026-10-04T20:54:28.374029+00:00, including2 wording blocks and explicit date/TERM metadata. No before-write timestamp invented.

首次capture成功，首record真实存在；一次正文/record修订完整保留。15门英文先修固定身份复用，作者与审校者亲读范围各按原证据，不声称重读15全文。

真实修订身份与时间（同字节快照不计额外修订）：

```json
[
  {
    "revision": "01",
    "before_utc": "2026-10-04T20:54:28.359095+00:00",
    "after_utc": "2026-10-04T20:54:28.374029+00:00",
    "receipt_sha256": "8e0bc0a9e1929a8b9eb2c757072c5618ca2d62648304269775ecc6d870679d46",
    "old_target_sha256": "6c5e0c93db4540929a14df22463947ec85e08cf9ddf697de77283af1bc6bc580",
    "new_target_sha256": "a2bca65f436e398a9532106afab8e2f77de395d7d755cd7e56dee7df5442546b",
    "diff_sha256": "38df0b0162ca15a4a7fdcd03a9ed45ab5f417064ec33be052ea78d039a44e22e",
    "old_record_sha256": "b111d4fcf9b1427a1c32eb2dd7158308273b8d27382ac3cf658ee3547f482a03",
    "new_record_sha256": "ac042f153411b17873b419a76e286afb1d07f88cf9f003f2c4ba9aa831d228ae",
    "record_diff_sha256": "fbcf2d9447d363986a1cd7f1aed914d357546928ace0efb08d8f81f7883a3ab5",
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

源先修原文：Phase 4 Lessons 01-15

固定英文先修身份来自已读准备材料；读取范围按作者和独审原证据分别保留，不冒称本次重新全文审读。 只依据固定英文与相关术语即可翻译，不增加中文先修正式验收要求。

冻结源准备时 formal134，INDEX commit 57e6fdd85d87ba64726514e4c4433d3a1d9dca44 / SHA256 7659fc93786f56524138d8525e646f2a2cdb92a0569fef7ac9b98fce357d1673，独立回执 SHA256 7ca593614e44ebe780dd30120dfc3122868f90d3188484041a32511aed8abaff。actual132 运行 2026-10-04T19:24:29.438439+00:00 至 2026-10-04T19:24:41.076837+00:00 / RESULTS SHA256 d307d12f3aec999a804086e8588efe9bb69a04868dcc32b2d9061eec2a4f95fd，不覆盖本3课；不是当前实时计数。旧book5/6与site空锚点/重复项限制保持，不借历史批次声明本课发布通过。

## 作者源风险与有限提案

来源SHA256 6201b16664a58a66603e5fe92325bc009932b2b9c78ce61d0313cf9a42e5a823；CPU提案实际来源SHA256 2e013a15219ae2e3c65f2fdff6a91f2a5b959f60a858fb9181dcdf414e80435a。以下技术事实与提案完整保留；NOT_RUN，提案不等于执行结果。

{
  "created_utc": "2026-10-04T20:57:31.779013+00:00",
  "source_commit": "1bafaa88bb4668356791150bec3a6d7df38387eb",
  "method": "Complete static source package read and targeted prerequisite context; no course execution or external validation",
  "status": "SOURCE_LIMITATIONS_NOT_TRANSLATION_CORRECTIONS",
  "risks": [
    {
      "id": "SR01",
      "location": "phases/04-computer-vision/16-vision-pipeline-capstone/docs/en.md:50-68,106-124; code/main.py:10-28; quiz.json:first question",
      "title": "坐标语义未被schema验证",
      "finding": "四个float组成的元组不能区分中心宽高与xyxy；没有坐标格式标记或语义验证器。分类索引、类别映射、框有限值/顺序等也未被完整约束。原文与quiz关于Pydantic立即识别该错配、每个边界均保证有效的断言没有由所示schema实现。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    },
    {
      "id": "SR02",
      "location": "phases/04-computer-vision/16-vision-pipeline-capstone/docs/en.md:54-57,110,179-211,333; code/main.py:14,110-148",
      "title": "掩码契约不统一且未输出实际掩码",
      "finding": "概念草图mask为Optional[list[list[int]]]并标注RLE，正式schema则为mask_rle:Optional[str]。管线未读取detector返回的masks，也未编码填充mask_rle。练习要求新增字段而示例已有空字段；JSON小于1MB的要求没有编码格式、分辨率或内容边界证明。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    },
    {
      "id": "SR03",
      "location": "phases/04-computer-vision/16-vision-pipeline-capstone/docs/en.md:129-266; code/main.py:31-76,128,193-210",
      "title": "正文生产模型与随课main桩实现不一致",
      "finding": "正文使用预训练Mask R-CNN和ConvNeXt-Tiny、224×224裁剪、min_crop=32，支持PIL并演示FastAPI；main使用固定检测结果的StubDetector与随机初始化StubClassifier，裁剪64×64、min_crop=16，接受ndarray/Tensor且没有FastAPI app。随课main不能直接满足uvicorn main:app。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    },
    {
      "id": "SR04",
      "location": "phases/04-computer-vision/16-vision-pipeline-capstone/docs/en.md:146-155,189-195,226-229; code/main.py:78-90; prerequisite04-01 Step4 and04-08 Step3",
      "title": "预处理及权重来源需要区分",
      "finding": "正文只除以255，没有分类器所需的独立ImageNet标准化变换；数组路径未验证dtype/范围/通道布局，main Tensor路径直接float也未检查范围。英文注释统称ImageNet-pretrained weights，而先修明确Mask R-CNN权重用于COCO检测；两模型类别映射不能混为一谈。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    },
    {
      "id": "SR05",
      "location": "phases/04-computer-vision/16-vision-pipeline-capstone/docs/en.md:178-206,288-294; code/main.py:110-141",
      "title": "裁剪范围、对齐及索引检查不完整",
      "finding": "将所有坐标下限截为0，只对x2/y2做上限截断，没有保证x1/y1上限、框顺序或有效面积；过小/倒序框可能仍以Detection返回。zip会静默截断不等长结果。正文class_names索引无边界检查；main只防上界，未处理负索引语义。min_crop是经验筛选阈值，不是所示插值/分类器证明过的绝对最小输入要求。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    },
    {
      "id": "SR06",
      "location": "phases/04-computer-vision/16-vision-pipeline-capstone/docs/en.md:80-88,218,243-266; code/main.py:94-149",
      "title": "完整失败处理和日志的承诺未兑现",
      "finding": "空检测与过小裁剪虽有分支，但没有具名失败码或日志；上传错误仅返回自由文本detail，没有统一命名错误schema。模型加载、分类超时、推理异常、错误响应等未构成完整已测路径。每个接口都有类型/每条失败路径已处理的断言过强。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    },
    {
      "id": "SR07",
      "location": "phases/04-computer-vision/16-vision-pipeline-capstone/docs/en.md:255-266,319",
      "title": "服务资源和并发边界未定义",
      "finding": "上传文件整体读入，未指定体积/像素数限制、超时、并发预算或恶意内容防护；async端点直接执行同步pipe.run。批量URL端点仅是建议，若实现还需独立处理URL访问范围等风险。这里没有运行服务或传输数据。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    },
    {
      "id": "SR08",
      "location": "phases/04-computer-vision/16-vision-pipeline-capstone/docs/en.md:275-309; code/main.py:152-190",
      "title": "基准范围与GPU计时不足",
      "finding": "classify阶段计时包含裁剪与插值；total从已生成ndarray开始，不含真实图像解码、HTTP、完整schema/响应序列化。正文没有GPU同步，异步执行可能使分阶段归因失真；main仅在device恰为cuda时同步。少量采样的p95按下标选取，不是统计置信保证。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    },
    {
      "id": "SR09",
      "location": "phases/04-computer-vision/16-vision-pipeline-capstone/docs/en.md:14,72-78,309; quiz.json:second question",
      "title": "性能概括不是实测保证",
      "finding": "预处理通常最大、GPU检测占70-90%、后处理GPU便宜CPU昂贵等均依赖模型、输入和设备；本课给出的CPU例子反而检测300-500ms远大于预处理~3ms。没有硬件/版本/输入配置支持这些典型数字；随机桩不能验证生产模型延迟。原数字原样保留。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    },
    {
      "id": "SR10",
      "location": "phases/04-computer-vision/16-vision-pipeline-capstone/docs/en.md:92,315-321,334; code/main.py",
      "title": "生产扩展与微批处理尚未实现",
      "finding": "跨请求微批处理、模型版本/权重hash、trace ID、分类器超时回退、NSFW/PII过滤、batch endpoint和health check是设计要求或练习，不在main中。吞吐量成倍提升或仅增加窗口延迟不是已验证结果；torchserve/Triton/BentoML能力和维护现状未作当前联网核验。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    },
    {
      "id": "SR11",
      "location": "AGENTS.md:Dependencies; docs/en.md:103,135,223-244,268; code/main.py:1-7",
      "title": "依赖、版本与执行限制",
      "finding": "pydantic、torchvision、PIL、FastAPI、uvicorn不在根AGENTS白名单；model_dump/model_dump_json要求相应Pydantic API版本，但未锁版本；weights=DEFAULT可能触发下载。uvicorn绑定0.0.0.0属于服务暴露。全部仅保留源文本，未安装/导入/下载/运行。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    },
    {
      "id": "SR12",
      "location": "quiz.json; code/main.py:1-7; source directory inventory",
      "title": "课程契约已有缺口",
      "finding": "quiz只有5题，阶段为2pre/3post，缺少lesson/title，部分正确选项明显更长；无code/tests。main头部也没有根AGENTS要求的说明/来源注释。译文不补造题目、测试或源代码。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    },
    {
      "id": "SR13",
      "location": "phases/04-computer-vision/16-vision-pipeline-capstone/outputs/prompt-vision-service-shape-reviewer.md:15; docs/en.md:157-159; prerequisite04-08",
      "title": "交付提示词把模型输入形状过度统一",
      "finding": "提示词统一检查NCHW，但正文检测器使用list[CHW tensor]，分类器才stack成NCHW；该准则需模型相关解释。提示词还要求发现第一处就停止，不能把其输出当作完整生产审计。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    },
    {
      "id": "SR14",
      "location": "phases/04-computer-vision/16-vision-pipeline-capstone/outputs/skill-pipeline-budget-planner.md:28-38,70-75",
      "title": "预算技能为未验证启发式",
      "finding": "默认分配为15+55+5+5+15+<1+4，总和小于100%，未解释剩余；先试Pillow-SIMD/NVJPEG、超目标30%就换模型、超预算10%判X等是启发式。原输出仅静态阅读，没有采用其安装或模型优化指令。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    },
    {
      "id": "SR15",
      "location": "phases/04-computer-vision/16-vision-pipeline-capstone/docs/en.md:29-46; figure v4-vision-pipeline",
      "title": "图与阶段计数边界未明示",
      "finding": "Mermaid包含请求和响应共八个节点；正文称七阶段、两个模型加五个其他阶段，可理解为不计入口请求，但未明示统计边界。figure注册键保持原样，不在本地GFM渲染，不把代码围栏保存视为互动图已验收。",
      "translation_disposition": "Preserve fixed English claims/code/numbers; no silent technical repair and no strict exception."
    }
  ],
  "scope_note": "Author source-risk inventory, not an exhaustive security audit or runtime verdict. Earlier source-only preparation risks all retained and expanded.",
  "location_verified_utc": "2026-10-04T20:59:45.122958+00:00"
}

# 有限离线 CPU 验证提案：NOT_RUN

当前授权只允许翻译、静态阅读及原翻译控制工具。没有运行、导入或测试本课代码，没有加载任何模型，没有 GPU/API/网络/服务/下载/安装操作。本提案不是执行记录，也不是运行授权。

若以后另获明确许可，可在依赖已存在、网络关闭的独立环境中做一次有限 smoke test：

- 只选择随课本地 StubDetector / StubClassifier 路径，不涉及 torchvision、预训练权重、PIL 上传或 FastAPI 服务
- CPU 单线程、固定随机种子、单张 64×64 RGB 合成图、一次管线调用；跳过 main() 与 benchmark()，设置进程硬超时与内存上限
- 检查有限数值、box/scores/labels 数量及索引对应、空检测、过小裁剪跳过但保留检测结果，以及 JSON 序列化
- 单独构造四元组坐标语义互换、越界/倒序框、分类索引越界等输入，记录实际接受或拒绝结果；不得预设 Pydantic 能自动识别坐标格式
- 结果只代表离线桩接口 smoke test，不能验证生产模型准确率、文中 CPU/GPU 延迟、HTTP、批处理或安全过滤
- 缺依赖即停止，不安装；发现网络、GPU或服务启动路径即停止，不改用其他路径规避限制

当前状态：NOT_RUN。没有把可运行建议计作验证。


## 独立源边界

```json
{
  "classification": "SOURCE_ONLY_NOT_TRANSLATION_FINDINGS",
  "author_inventory": {
    "path": "private-locator-sha256:68a286b21a357a0587eb9d06e5bc823348a81e1cbc170dd49e9404a6c5d4cb6e",
    "sha256": "6201b16664a58a66603e5fe92325bc009932b2b9c78ce61d0313cf9a42e5a823",
    "count": 15
  },
  "independent_dispositions": [
    {
      "id": "SR01",
      "assessment": "确认",
      "independent_note": "正式schema只有四float类型和score/class_id局部范围约束；b0033与quiz的坐标错配即报错断言无法从此推出。译文完整忠实，既非译错也非生产正确性通过。"
    },
    {
      "id": "SR02",
      "assessment": "确认",
      "independent_note": "草图mask列表与正式mask_rle字符串不一致；run不读取masks、不进行RLE。练习为新增mask字段但既有schema已留空字段，1MB上限仍待真实内容验证。"
    },
    {
      "id": "SR03",
      "assessment": "确认",
      "independent_note": "doc用真实DEFAULT模型、224裁剪/min_crop32/PIL/FastAPI；main为固定三检测和随机分类线性头、64裁剪/min_crop16/ndarray或Tensor。main未定义app，不能把其演示当作doc服务实现。"
    },
    {
      "id": "SR04",
      "assessment": "确认",
      "independent_note": "04-01明确除255与mean/std不同；本课crop直接喂分类器，无后者。04-08明确COCO检测背景/标签；统一ImageNet注释不能等同两模型类别语义。"
    },
    {
      "id": "SR05",
      "assessment": "确认",
      "independent_note": "仅所有坐标下界与x2/y2上界限制，未全验框；zip静默截断、class_names索引不足、min_crop阈值未证明为绝对架构最低值。未改源阈值或实现。"
    },
    {
      "id": "SR06",
      "assessment": "确认",
      "independent_note": "代码仅局部空检测/小crop和上传错误分支，没有各失败具名码/日志/分类超时等全路径保证；b0067源强断言未因翻译而被改写。"
    },
    {
      "id": "SR07",
      "assessment": "确认",
      "independent_note": "FastAPI上传整体读入且同步推理在async端点，未给资源、超时及并发边界；URL列表批端点仍是扩展提议。无服务或数据传输发生。"
    },
    {
      "id": "SR08",
      "assessment": "确认",
      "independent_note": "doc计时classify含crop/resize，total从ndarray开始且未含HTTP/真实解码/完整响应；doc无cuda同步，main只有device字面cuda检查。04-15再次说明同步与目标设备的重要性。"
    },
    {
      "id": "SR09",
      "assessment": "确认",
      "independent_note": "预处理通常最大和CPU典型检测300–500ms而预处理~3ms之间存在依赖场景/表述矛盾；没有设备配置和实测依据。所有数字按源保留。"
    },
    {
      "id": "SR10",
      "assessment": "确认并补充源歧义",
      "independent_note": "微批、trace/版本、timeout fallback、过滤、batch/health均不在main。练习“5 concurrent requests per second”同时使用并发数与速率术语，未给独立并发上限/到达模型；译文保留该歧义，不能静默改为只有5QPS或只有并发5。"
    },
    {
      "id": "SR11",
      "assessment": "确认",
      "independent_note": "当前根AGENTS允许列表不包括Pydantic/torchvision/PIL/FastAPI/uvicorn；DEFAULT可能下载，model_dump接口有版本约束，0.0.0.0监听是源命令。未安装/导入/联网核验。"
    },
    {
      "id": "SR12",
      "assessment": "确认",
      "independent_note": "quiz只有5题且2pre/3post、无lesson/title；目录无tests，main无要求的说明头。这些课程包缺口与本次zh正文译质分开。"
    },
    {
      "id": "SR13",
      "assessment": "确认",
      "independent_note": "输出prompt要求NCHW不适用于本例detector的list[CHW]契约，classifier才stack到NCHW；其first-issue即停止规则不是全面审查。文件仅读不执行。"
    },
    {
      "id": "SR14",
      "assessment": "确认",
      "independent_note": "预算表除schema外合计99%，schema<1%使总额不到100%；30%/10%阈值及优先工具选择是启发式。产物不存在已运行/兑现预算证据。"
    },
    {
      "id": "SR15",
      "assessment": "确认",
      "independent_note": "图含REQ和RESP共8节点，文称7阶段/2+5可由排除请求入口解释但未明示；figure键字节保存不等于实际交互图验收。"
    }
  ],
  "source_technical_errors_do_not_become_translation_edits": true
}
```

源准备发现（仅读、未代改源）：

```json
[
  {
    "location": "docs/en.md:68; code/main.py:Detection",
    "finding": "Typed four-float boxes do not distinguish cx/cy/w/h from x1/y1/x2/y2; source claim that Pydantic catches that mismatch is not implemented by the shown schema."
  },
  {
    "location": "docs/en.md Build steps2–5; code/main.py",
    "finding": "Docs build a pretrained Mask R-CNN/ConvNeXt and FastAPI service; main is a random stub detector/classifier demonstration, resizes64 vs224 and min_crop16 vs32. No FastAPI app is defined by main, so documented uvicorn main:app does not name the shipped app."
  },
  {
    "location": "docs/en.md preprocessing/crops/failures/benchmark",
    "finding": "Input normalization for pretrained classifier, complete box bounds/order, zero-area values, structured named error/log paths, upload limits/timeouts, model loading and GPU timing are not fully covered. Benchmark classify includes crop work and does not cover decode/HTTP/schema; main stub timings cannot verify documented performance figures."
  },
  {
    "location": "AGENTS dependency allowlist; docs/en.md imports; quiz.json",
    "finding": "pydantic/torchvision/PIL/FastAPI/uvicorn are outside the stated allowlist, model weights can download, service binds0.0.0.0; source package has no tests and quiz has5 questions (2pre/3post), missing lesson/title. Record these source limits without changing translation."
  }
]
```

课程 main/import/tests、模型/CPU/GPU、API/网络/安装/服务/签名均 NOT_RUN；本轮不重跑原strict、离线重放、GFM、控制或累计回归。已有局部strict和独审仅按其真实输入哈希复用；own3仍未安装，后续页面、远端内容和适用批次尚待处理。
