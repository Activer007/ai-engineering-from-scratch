# S87-map-assumptions-and-risk English-first 支持范围

状态：固定英文与正式术语已核对，现冻结为本课起草支持快照。它不代表译文完成、独立审校、提交或正式接受。

## 固定源与目标

- English commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Canonical English title: Map Assumptions and Resolve the Riskiest One First
- Lesson: `14-49`
- Source: `phases/14-agent-engineering/49-map-assumptions-and-risk/docs/en.md`
- Source SHA256: `7c8381be49ff8b9c8b4e9f8100c338936d993f68cbcd9e988e4f0831ff33ab43`
- Target after separate GO: `i18n/zh/phases/14-agent-engineering/49-map-assumptions-and-risk/docs/zh.md`
- Record after separate GO: `i18n/zh/.curated/lessons/14-49/translation.json`
- English learning prerequisites: 14-48
- Exact source prerequisite line: **Prerequisites:** Phase 14 lesson 48

上述先修是学习上下文，不是 upstream 中文翻译正式验收门禁。完整课源目录清单及逐文件 commit/blob/SHA256/bytes 见同目录 DEPENDENCIES.json 的 source_files 字段；作者完整阅读 docs、code、quiz、outputs、assets 与 tests（存在时），不执行 main/install/GPU/训练。14-49 规范标题以 docs 长标题为准，quiz 短标题不是替代标题。

## 术语与支持

由 actual103 (`91a2cee57039bab87624cc87f6caa3e81229d4d5`) 的 accepted stage 重新推导 91 个唯一 pins：83 份 TERM（81 个 accepted stage 加 core2），8 份原始控制文件。S61/S66/S79 不在正式词表集合。原 S83 的 87 pins 内容保持，新增 S78/S84/S82/S83；旧 pending 内容不进入支持快照。各 pin 来源、Git blob、SHA256 均逐项验证。

原33的三个 fixture 是 f9b5 的 00-04 translation/review/zh 独立测试输入，仅以路径和哈希列在同目录 DEPENDENCIES.json 的 original33_fixtures_test_only 字段，不放入作者root、91 pins 或作者可读TERM bundle。不得读取旧中文正文、translation segments、format_revisions或旧作者缓存。正式TERMs用于术语一致性，不作为译文复用。

## 保护与隔离

保护原代码、公式、变量、数字、单位、形状与轴次序、API、路径、链接、提示词、Mermaid/figure、SVG与围栏载荷。源缺陷单列，不在中文暗修。仅给原裸围栏添加必要的 text 标注；其他必要GFM修复须最小可逆、留痕、重新绑定精确审校字节。不得改英文、代码、quiz、outputs、shared TERM、原checkers/S07/S19、index/claims/queue、PR1或其他课程。

## 作者源读确认与边界

作者完整通读本课固定源全部文件；本次支持工作逐文件再次验证其原始 blob 与 SHA256。以下源观察来自新作者报告，不是旧译稿或运行证据：

1. **Title discrepancy:** documentation uses “Map Assumptions and Resolve the Riskiest One First”; `quiz.json` uses “Map Assumptions and Risk”. The canonical translation title must follow the documentation. Report the source discrepancy; do not change the quiz.
2. **Scoring:** `risk_score` computes `impact * uncertainty + irreversibility`. The three shipped example scores are 27, 25, and 9 in ranked order. Source documentation expressly says the formula is not universal.
3. **Membership is not strict integer type validation:** `value not in range(1, 6)` checks membership. The error string says “integers”, but booleans and integral floats have Python numeric equality behavior that requires characterization; do not rewrite the source contract as a strict `int` type guard.
4. **Tested is an evidence-presence label:** `prioritize` assigns `tested` for truthy evidence and `open` otherwise. This does not evaluate credibility, sufficiency, relevance, a passing threshold, or whether the claim is true. The shipped statuses are `open`, `open`, `tested`.
5. **Sorting and next-selection differ on ties:** `prioritize` sorts by `(-risk_score(item), item.statement)`. `next_experiment` first filters out truthy-evidence items, then uses `max` by risk score; equally scored open candidates retain first-input selection. It is inaccurate to promise matching alphabetical tie breaks in both functions.
6. **Scope of main:** `main` writes and prints the ranked JSON. It does not call or print `next_experiment`; that selector is exercised by the tests. The doc's “lab selects” statement refers to the available lab functionality, not an extra printed main result.
7. **File location:** `main` resolves `outputs/assumption-map.json` from `Path(__file__).resolve().parents[1]`. Changing the shell working directory alone cannot isolate its write. Running requires a complete temporary lesson copy with an existing `outputs/` directory.
8. **No external operational action:** the sample `test` text includes incident replay, interviews, and an approval workflow before automation. These are stored strings. Running the lesson neither executes experiments nor triggers remediation, production changes, real interviews, permission grants, or tool calls.
9. **Decision discipline:** “pass, fail, and ambiguous evidence” must retain all three outcomes. Decisive evidence should mean evidence that changes a decision, not evidence that automatically confirms the proposed feature.
10. **Safety and authority:** preserve the contrast between read-only replay and production integration, temporary adapter and data migration, and human-approved recommendation and automatic action. Do not replace unsafe authority with a narrower unsupported claim about administrator privileges.
11. **Class distinctions:** value, usability, feasibility, viability, and safety are separate. In particular, feasibility concerns available data/constraints; viability concerns sustaining cost, ownership, and operations.
12. **Downstream artifact:** keep the literal output path unchanged. The next lesson consumes the assumption map to choose a smallest slice producing decisive evidence; this is an instructional dependency, not proof that a subsequent build has already happened.

## 运行边界与后续门槛

未来若另获运行授权，只考虑完整临时副本中原始 stdlib main 与原5项tests，分别15秒。main按 __file__ 写 outputs，必须复制完整课程而非只改变cwd。附加表征至多20个假设，须单列授权和结果，不暗修bool/float、evidence truthiness或tie-break行为。本次尚未运行。

正文起草需要协调者单独 GO。译稿需逐块 English 技术对读、中文自然度独立审读、原控制检查、两次独立replay及实际GFM验收；最终binding以实际字节为准。作者不得写远端、index/claims/queue或修改共享/原控制。三课按已批准顺序推进，不增加新课；学习先修不构成 upstream 中文正式验收门禁。
