# S132-the-agent-loop English-first 支持范围

状态：本地 own3 候选，未安装、未发布，不增加正式课程数。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；原控制 f9b5e9cbe4012f54483794f920c0d87b06a7573d。

## 当前正文与独立审校身份

- Lesson: 14-01
- Current target SHA256: 2714b6a499dabb11d7746010953c3128cf107ec1ecc45eb0a80c2300c0fb38bb (10175 B)
- Current draft record SHA256: 534757197912632dd045b1c32de57a43cf39e6ab977df7f2882c380ea6e1864d (39937 B)
- Historical author handoff SHA256: 0dced85031bdfe0edcd35a3f4feb58e59dc1925c49e89c0af96c7b5320fecbc7
- Current handoff SHA256: 9720bac08b9e56d57d9cac8cd4f001c6199c2ed27fbafdfeaf5bdc89481005f8
- Original full independent review SHA256: 6f1c51fee196c50b7f133affc87f64b18eba68a54b4e069a6172a8d562fcfbc6
- Current incremental closure SHA256: 310300cec219a8619558f1f0ee350d5c3681a668f6fca6a425521d2170857dde
- First complete body SHA256: 6a555bb3996f106f8910efc20330f74cadffe56045ac5a6a7628e0819cc48ae2
- First-capture record SHA256: 72b92b53f388b3f819625e7ecb39609f884fbf29a75c130f1e39a0a87b861667
- First successful capture record SHA256: 72b92b53f388b3f819625e7ecb39609f884fbf29a75c130f1e39a0a87b861667
- Historical exact-byte local strict evidence SHA256: 15d14644e25df7aa723a4d07269801dd9947582d26e16abbdb441c84609bfa36; not rerun

FIRST-BODY null record is the real pre-capture state; FIRST-CAPTURE later succeeds and its first record is preserved. R01 body/provenance changes precede original full87-block review. Initial PASS_WITH_NONBLOCKING_S2 was an incorrect disposition, retained separately; corrected full review requires S2 revision. R02 adds only first-occurrence 工具注册表（tool registry） at b0009; independent delta PASS closes S2 while86 blocks and all older reports remain bound to actual bytes. Source SVG is copied unchanged but body has no relative SVG link; figure agent-loop is not proof that the SVG renders.

真实审校先后与各自原身份：

~~~json
[
  {
    "sha256": "1d3abcc7da41cefd9c114e04f5c81e56abd1dcbb88e5dd9348e9805ce5112fc3",
    "bytes": 108237,
    "status": "PASS_WITH_NONBLOCKING_S2"
  },
  {
    "sha256": "6f1c51fee196c50b7f133affc87f64b18eba68a54b4e069a6172a8d562fcfbc6",
    "bytes": 109760,
    "status": "REVISION_REQUIRED_S2"
  },
  {
    "sha256": "310300cec219a8619558f1f0ee350d5c3681a668f6fca6a425521d2170857dde",
    "bytes": 5984,
    "status": "PASS"
  }
]
~~~

真实修订身份与时间（同字节快照不增加修订数）：

~~~json
[
  {
    "revision": "revision-01",
    "before_utc": "2026-10-04T22:22:08.831410+00:00",
    "after_utc": "2026-10-04T22:22:08.841823+00:00",
    "receipt_sha256": "35a5062bb8bd3615ddbdd980b90189d77fd6e3914494e38572ef26fac0600db0",
    "old_target_sha256": "6a555bb3996f106f8910efc20330f74cadffe56045ac5a6a7628e0819cc48ae2",
    "new_target_sha256": "61b8f5625a172ae5a12e0287e6d571fa531a0c93da2cfb8c7a3e402efffa9945",
    "diff_sha256": "c500e3b749ece0906650e531f6c297d7b0e217d65a331cfcb138d47baa62957c",
    "old_record_sha256": "72b92b53f388b3f819625e7ecb39609f884fbf29a75c130f1e39a0a87b861667",
    "new_record_sha256": "92ceaea4a40704d33a03f8b9400dcbf79ff62c5d7d963c003a29369db6e4b9ce",
    "record_diff_sha256": "b1e9180e689ac04643d48dd9b9e525484ca157da9e9680c83e89a3ef9fb0b6e9",
    "same_byte_alias_only": false
  },
  {
    "revision": "revision-02",
    "before_utc": "2026-10-04T22:37:41.564325+00:00",
    "after_utc": "2026-10-04T22:37:41.567490+00:00",
    "receipt_sha256": "8308732b658e223b0d5bddef31d26876fc19b878f326604c56d19a79571dff74",
    "old_target_sha256": "61b8f5625a172ae5a12e0287e6d571fa531a0c93da2cfb8c7a3e402efffa9945",
    "new_target_sha256": "2714b6a499dabb11d7746010953c3128cf107ec1ecc45eb0a80c2300c0fb38bb",
    "diff_sha256": "3fa0bd37fee7de248043cc84dc2c43326cf8d82a11a3c11d34d836429bc8c6e0",
    "old_record_sha256": "92ceaea4a40704d33a03f8b9400dcbf79ff62c5d7d963c003a29369db6e4b9ce",
    "new_record_sha256": "534757197912632dd045b1c32de57a43cf39e6ab977df7f2882c380ea6e1864d",
    "record_diff_sha256": "9d997ab2650d297a77fed3123c24bb51afaac547658da885accae30620d82588",
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

源先修原文：**Prerequisites:** Phase 11 (LLM Engineering), Phase 13 (Tools and Protocols)

仅以固定英文及相关术语为翻译前提，不添加中文先修正式验收门槛。作者与审校者的亲读和固定既有英文全文复用按各自原报告保留；本轮仅装配支持候选，不新增语言二审或全文亲读声明。

冻结源准备 formal138/actual138，INDEX commit 4832660521df7d71a336615cb30ec59794a2db06，INDEX SHA256 1bc111580519ff8d68dce14547c373fd659d0320b4d5e0b5fc1fc87c4bf6223f，独立回执 SHA256 2d2284aa3eec2c4fb1f5aa89d9577a56d8a00647e7c89d61895fbe9e53685a0e。这是 2026-10-04T22:08:48.908492+00:00 源准备时的真实快照，未追刷当前计数；不覆盖本三课，也不借历史回归宣称其已通过。

## 作者源风险与有限提案

原源风险 SHA256 e50a2102afa0b0aa88321936f2871a3854a1fdc7dce2de9ad342d6a7245b6cfc (2304 B)。以下原静态观察与历史 NOT_RUN 文字照录，原作者“strict 未执行”等若出现，仅反映该风险文件写作时点，不能覆盖后来的独立检查回执：

# S132 固定英文源风险，非译文修正

仅静态读包，不代表运行、外部核实或验收。

1. docs/en.md 的 Languages 仅列 Python (stdlib)，源包同时含 Python、TypeScript main。忠实保留元数据，不改实现。
2. 文中把 ToolRegistry 描述为有输入校验；Python 实际仅查工具名并捕捉调用异常，没有 JSON Schema 校验。ToyLLM 按固定脚本推进且不使用 history/观察结果决定下一步，最终答案硬编码。文中 while loop 与实现有界 for 也存在差别。
3. 五要素列出多种停止条件，但示例只实现显式 finish 与轮次预算耗尽；没有 token 预算、无工具调用停止、护栏停止、并行关联器或提供商类型结构。轮次预算不能中断一次耗时工具调用。
4. Python eval 与 TypeScript Function 对字符做 allowlist，但没有表达式复杂度/耗时界限；不能据此宣称真实沙箱。SVG 的 registry is the sandbox boundary、validated on dispatch、no-tool-calls stop 和 OTel span 描述超出示例证明范围。
5. 源对 2026 所有框架/智能体普遍采用 ReAct、40–400 步普遍性、2025–2026 native reasoning/跨提供商加密透传、Letta API 迁移和提供商关联 ID 要求的断言均未外部核实；保留原意，不悄悄软化或补正确性结论。
6. 原论文 ALFWorld +34 / WebShop +10 与 Hotpot QA 描述仅按源翻译，未查论文测量口径，不虚构本地结果。原绝对提升措辞保留为百分点。
7. outputs/skill-agent-loop.md 将 Lesson 09 称为 permissions + sandboxing，来源准备记录指出实际 14-09 是 Hybrid Memory；不在翻译正文或源输出中修复。
8. quiz.json 共 7 问（2 pre / 3 check / 2 post），与 repo 合同要求 6 问不同；无 tests 目录。source docs 两个无标签围栏只在译文补 text，内容不动。
9. docs 的 figure 为 agent-loop，并没有相对 SVG 链接。react-loop.svg 作为原包资产按允许复制到中文同相对 assets 目录，字节/hash 不变；不伪称正文存在 SVG 链接，不为它新增 manifest 中相对链接绑定，不声称已可视化审查。

课程 main/import/tests、CPU/GPU/model、API/network/install、strict、GFM/SVG rendering、regression 均未执行。源风险不作为 strict 例外。


## 原独立审校保留的源边界

~~~json
[
  {
    "id": "SRC-01",
    "classification": "confirmed_static_source_mismatch",
    "references": [
      "docs/en.md:6",
      "code/main.py",
      "code/main.ts"
    ],
    "issue": "Languages 只写 Python (stdlib)，固定源包另含 TypeScript main。忠实翻译原元数据，不自行增加语言。"
  },
  {
    "id": "SRC-02",
    "classification": "confirmed_static_source_mismatch",
    "references": [
      "docs/en.md:79-82",
      "code/main.py:34-53",
      "code/main.py:89-94",
      "code/main.py:104-121",
      "code/main.py:139-157"
    ],
    "issue": "Build It 描述的输入校验、ToyLLM 输出逐行轨迹、while 循环与工具命名和实现有差异：调度只查询工具名并捕获调用异常，没有 JSON Schema 校验；ToyLLM 返回固定字典、忽略 history；实现为 for；实际工具注册名为 kv_get/kv_set，而文中为 kv_store.get/kv_store.set。"
  },
  {
    "id": "SRC-03",
    "classification": "confirmed_static_capability_limit",
    "references": [
      "docs/en.md:55-59",
      "docs/en.md:90",
      "code/main.py:89-94",
      "code/main.py:104-121",
      "code/main.py:146-157",
      "code/main.ts:93-137"
    ],
    "issue": "脚本策略和最终答案硬编码，不能证明观察后重新推理或错误纠正。实际停止仅 finish 与轮次耗尽，没有无工具调用、token 上限、护栏、并行关联或真实提供商协议；次数上限不打断单次耗时工具。production-shaped 不应被验收解读为生产可用。"
  },
  {
    "id": "SRC-04",
    "classification": "confirmed_static_safety_limit",
    "references": [
      "code/main.py:56-63",
      "code/main.ts:52-69",
      "assets/react-loop.svg:35-36",
      "assets/react-loop.svg:67-88"
    ],
    "issue": "字符 allowlist 后仍使用 eval/Function，未设表达式复杂度或时间上限，不构成真实进程隔离。SVG 中 registry sandbox boundary、validated on dispatch、无调用停止和 OTel span 文案超出示例所证明能力。未运行攻击样例或执行模型/代码。"
  },
  {
    "id": "SRC-05",
    "classification": "unverified_external_or_overbroad_source_claim",
    "references": [
      "docs/en.md:3",
      "docs/en.md:47",
      "docs/en.md:53-69",
      "docs/en.md:94",
      "docs/en.md:114",
      "docs/en.md:124-126"
    ],
    "issue": "所有智能体/框架都基于 ReAct、恰好五要素、2026 40–400 步普遍性、Responses/Letta 迁移、跨提供商加密透传和各提供商关联 ID 要求均为源文断言。本审仅判断翻译忠实，不声称外部事实已核实。"
  },
  {
    "id": "SRC-06",
    "classification": "unverified_measurement_scope",
    "references": [
      "docs/en.md:37-43"
    ],
    "issue": "ALFWorld +34/WebShop +10 与 Hotpot QA 结果按源翻译；未访问论文核实基线、成功率与百分点口径，不把引用转成此地实验结果。"
  },
  {
    "id": "SRC-07",
    "classification": "source_package_contract_mismatch",
    "references": [
      "quiz.json",
      "AGENTS.md:quiz.json schema",
      "phases/14-agent-engineering/01-the-agent-loop fixed git tree"
    ],
    "issue": "固定包 7 问（2 pre/3 check/2 post），不是 AGENTS 合同的 6 问；包内无 tests 文件。没有因翻译修改 quiz 或补造测试通过。"
  },
  {
    "id": "SRC-08",
    "classification": "source_reference_warning_not_reverified",
    "references": [
      "outputs/skill-agent-loop.md:Refusal rules",
      "evidence-sha256:e50a2102afa0b0aa88321936f2871a3854a1fdc7dce2de9ad342d6a7245b6cfc:7"
    ],
    "issue": "输出技能将 Lesson 09 称为 permissions + sandboxing，作者风险记录指出实际为 Hybrid Memory；本审读完源技能并确认该引用原样，未扩展读取整阶段来独立判定目标课题名。该警告保留作者出处，不假称独立核实目标。"
  },
  {
    "id": "SRC-09",
    "classification": "source_figure_delivery_boundary",
    "references": [
      "docs/en.md:71-73",
      "assets/react-loop.svg"
    ],
    "issue": "正文只有 figure/agent-loop，完全没有相对 SVG 链接。SVG 副本与源字节一致只证明复制保真；不造链接、不新增相对链接 manifest 绑定、不声称 GitHub GFM 已显示该 SVG。"
  }
]
~~~

固定源准备风险（未暗改源）：

~~~json
[
  {
    "where": "docs/en.md metadata/Build; code/main.py and main.ts",
    "finding": "Languages says Python(stdlib) while Python and TypeScript mains are both present. Pythonregistry has no JSONSchema validation, catches call exceptions only; ToyLLM advances a fixedscript and ignores observations, withhardcoded finalanswer. Statedinput validation andproduction-shaped equivalence are not full capabilities."
  },
  {
    "where": "calculator in both mains; AgentLoop stop paths; SVG",
    "finding": "Allowlisted arithmetic eval/Function still has no expression complexity/time limit; turnbudget doesnot interrupt oneexpensive tool. Only explicitfinish/maxturns implemented, no tokenbudget/no-tool-call/guardrailstop, parallelcorrelator ortypedprovider schema. Registry is not demonstrated sandbox isolation despite SVG label."
  },
  {
    "where": "docs/en.md references; outputs/skill-agent-loop.md; quiz",
    "finding": "Native/encryptedreasoning interoperability, framework universality and2026 stepcounts are unverified. Skill pointsLesson09 atpermissions althoughactual14-09 isHybridMemory; do notrepair inline. Quiz7(2pre/3check/2post), no tests. ProtectedSVG andfigure awaitvisualreview; no providerAPIcall orrealtrace generated."
  }
]
~~~

CPU 提案准确原证据 CPU-NOT-RUN-PROPOSAL.md，SHA256 3a156699844d975c0e149dbb268c212318d12a8cc230f081832138e4fdeb00cd，1448 B；状态 NOT_RUN。

# 可选 CPU 验证提案：NOT_RUN

本课作者没有运行或导入任何课程 main、测试、模型或 API。以下仅为独立审阅后、另获授权时的有限方案，不是执行记录。

- 对象：固定英文 `phases/14-agent-engineering/01-the-agent-loop/code/main.py`，SHA-256 `5fc9514531f6c088b593da55a99877887d8aa96cc0acbb63376fe1787230e534`
- 目的：仅确认现有固定演示脚本在离线条件下能否结束，并记录真实 stdout、stderr、退出码；不把它解释为自适应推理、生产可用性或安全沙箱证明
- 范围：一个 Python 标准库进程，单次，固定脚本和内置算术输入，不接受外来表达式；工作目录为临时隔离目录，不连接网络、不提供凭据、不安装包、不下载模型、不调用 GPU
- 上限建议：墙钟 5 秒、CPU 1 秒、内存 256 MiB、输出 1 MiB；只有现成隔离执行器能够强制这些边界时才运行，不为验证而改系统安全设置
- 观察项：工具调用顺序、5 次 action、最终固定答案 138.0、正常退出或明确资源终止。这些数值来自静态脚本阅读，是待核预期，未宣称实测
- 不扩大：不执行 TypeScript npx；包中没有 tests，不杜撰测试结果；不运行教学练习中的真实 Responses API，不验证跨提供商加密互通
- 停止条件：一次进程终止或任何边界不可保证即停止，保留真实结果，不反复跑同一字节

原 SVG 精确复制证据（仅静态字节保护，不是渲染通过）：

~~~json
[
  {
    "source_path": "phases/14-agent-engineering/01-the-agent-loop/assets/react-loop.svg",
    "target_path": "i18n/zh/phases/14-agent-engineering/01-the-agent-loop/assets/react-loop.svg",
    "source_commit": "1bafaa88bb4668356791150bec3a6d7df38387eb",
    "source_blob": "bf487a145d380ae6915668987de6f973a189900e",
    "sha256": "2822281cc241cbc1098947c3d63732b6bf1f0a751dbe90d27d168480f3d3f9d8",
    "bytes": 4907,
    "copied_unchanged": true,
    "relative_SVG_in_body": false,
    "executed_or_rendered": false,
    "figure_payload": "agent-loop",
    "not_added_to_relative_link_asset_manifest": true
  }
]
~~~

本轮仅本地支持候选装配。课程main/import/tests、CPU/GPU/model、API/network/install/service、strict、GFM、离线重放及累计回归均未运行；没有远端、INDEX或queue改动。所有源风险和后续发布关卡仍按真实证据分别保留。
