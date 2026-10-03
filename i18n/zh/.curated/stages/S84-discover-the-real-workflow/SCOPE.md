# S84 Discover the Real Workflow: English-first scope

Status: author has completed source/support preparation only. Chinese lesson authoring is gated on a separate coordinator GO after support publication and activation readback. No target, translation record, review, acceptance, or runtime result is claimed here.

## Fixed source and boundaries

- Lesson: `14-48`, **Discover the Workflow People Actually Perform**; Chinese title decision: **发现人们实际执行的工作流**.
- Fixed English commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`.
- English document: `phases/14-agent-engineering/48-discover-the-real-workflow/docs/en.md`.
- Source SHA256: `8ee8e7fa91e4ed6674f286de9cbdf05e1c2b141c61af1585c46c54a4b512f34b`.
- Eventual target: `i18n/zh/phases/14-agent-engineering/48-discover-the-real-workflow/docs/zh.md`.
- Exact prerequisite: Phase 14 lesson 47 (`14-47`). Keep `Learn + Build`, `Python (stdlib)`, and `~70` unchanged; metadata field names stay English, and the natural-language time unit may become 分钟.
- Translate all explanatory prose, the hook, objectives, table content, evidence ladder, four discovery concerns, workflow variants, build instructions, five exercises, reading annotations, and the retained-artifact explanation. Preserve the original section order and granularity; do not add missing curriculum sections.
- Protect all code fences and their language tags, Mermaid source/labels/edges, command lines, inline paths, URLs, numbers, mathematical content, identifiers, prompt text, and output payloads. The English lesson has one Mermaid fence and one bash fence; neither is translated.
- Do not edit English, code, tests, quiz, checked-in outputs, global index/claims/queue, another lesson, or immutable dependency pins. No commit, push, fetch, remote operation, package installation, or network runtime is in the author's present scope.

## Sources actually read

All five files below were read in full and compared byte-for-byte with the fixed English commit. Repository `AGENTS.md` and this stage's initial support contract were also read in full.

| Source file | SHA256 |
|---|---|
| `phases/14-agent-engineering/48-discover-the-real-workflow/docs/en.md` | `8ee8e7fa91e4ed6674f286de9cbdf05e1c2b141c61af1585c46c54a4b512f34b` |
| `phases/14-agent-engineering/48-discover-the-real-workflow/code/main.py` | `7a5ca870a97c539d511c363e87755de83a7c77e5b79863d64143bc447c0ba307` |
| `phases/14-agent-engineering/48-discover-the-real-workflow/code/tests/test_main.py` | `712ad3637525a4fad4784a51f1fbf9acd7cd1a0e096bd10c316fb6afb3f2da34` |
| `phases/14-agent-engineering/48-discover-the-real-workflow/quiz.json` | `2e38f941155fb559d3dd81f15d6049fd0c2a6a30c78436097b3be9b75f777f94` |
| `phases/14-agent-engineering/48-discover-the-real-workflow/outputs/workflow-evidence.json` | `f741744a503bafc83fe022e8c21f822734e60fb5361d5fa44029163191169798` |

## Accepted-support boundary

- `DEPENDENCIES.json` remains byte-identical: 87 immutable support pins, comprising the original 83 plus accepted final S73/S77/S80/S81 terminology. Each local file has been checked against its pinned SHA256 and exact committed bytes without fetching.
- This fixed support snapshot was prepared at the actual99 baseline (`944b854e93c748695d847d6882d7029385d72501`, index SHA256 `a60f714388f3e64e4feb10e664ab3e8cda6e18593e3486bbe7e9a54664062e44`). The coordinator's current accepted count is 100; that later count does not change these pins. S78 is not backfilled.
- The three original33 regression fixtures are separate from the 87 support files. Their bytes were checked against `f9b5e9cbe4012f54483794f920c0d87b06a7573d` and the coordinator's fixed hashes. They are test fixtures only, not translation references.
- Accepted glossary content is consulted for terminology only. No old Chinese lesson prose, other author draft, cached translation, or upstream452/457 content is used.
- Context-sensitive decisions follow the core/addendum and S81's accepted `outcome`, `output`, `on-call engineer`, `incident commander`, `runbook`, and `artifact` choices. This stage's glossary records new workflow-discovery senses rather than globally replacing overloaded terms.

## Source limitations to preserve and disclose

These findings are from static reading, not executed test results. Do not silently repair the lesson or strengthen its claims in Chinese.

1. `audit([])` has no ordering issue because both order lists are empty; its evidence ratio is `0` and status is `needs-evidence`, with an empty `issues` list. The code does not emit an explicit empty-workflow diagnostic.
2. A step with an empty evidence tuple produces `step N has no evidence`; missing evidence must not be described as validated or complete.
3. Ordering is exact list equality with `list(range(1, len(steps) + 1))`. Duplicate orders, gaps, a start other than one, and reversed contiguous orders fail the same generic check. It does not reorder steps or distinguish those causes in separate messages.
4. Confidence is checked with `not 0 <= item.confidence <= 1`. Values below zero, above one, infinities, and float NaN fail that comparison; the implementation has no explicit finite/type validator, and nonnumeric values can raise `TypeError`. It does not clamp, repair, or calibrate confidence. Confidence is not used to weight evidence.
5. `grounded` requires no collected issues and at least one direct item globally. It does not require direct evidence on every step. In the shipped three-step example, the approval step has only a `direct=False` runbook item yet the overall status is `grounded`.
6. `direct_evidence_ratio` counts direct evidence items over all evidence items, rounded to two decimal places. It is not a step-coverage ratio, a confidence-weighted score, or proof that every workflow branch is observed. The checked-in example is `0.67`.
7. The prose ladder says its first two categories directly prove current behavior, but the example marks its runbook evidence `direct=False`. The program accepts a supplied Boolean instead of deriving evidence strength from the category; retain both the prose and payload without inventing a reconciliation.
8. The discovery table asks for actor, trigger, action, input, output, friction, authority, and evidence. The example dataclass has only order, actor, action, evidence, and friction; it does not enforce all eight discovery fields, causal correctness, source authenticity, or an authority boundary.
9. Exception paths and multiple variants are exercises. The shipped linear audit has no explicit branch/variant structure and does not validate the suggested missing-deployment-record exception. Do not claim that feature is implemented.
10. The six original tests cover the example status, missing step evidence, a non-one order, reversed ordering, one confidence overflow, and friction extraction. They do not cover the empty list, duplicates, gaps as a distinct case, lower-bound confidence, NaN, or per-step direct-evidence coverage. Later supplemental checks must be labeled separately from the original suite.

## Safe runtime gate after GO

No lesson code was executed during preparation. After separate authorization, copy the entire lesson directory, including its existing `outputs/`, into a fresh temporary directory. Verify the copied source hashes, then run only the copied original main program and the copied six-test suite, with bytecode disabled and a 15-second bound. Use stdlib and offline synthetic data only. `main.py` derives the output location from `__file__`, so changing the process working directory alone does not protect the source/worktree output. Never execute the lesson directly in the source/worktree. Compare source and support hashes again afterwards; any supplemental static or runtime checks must preserve the original implementation and remain explicitly distinct.

Real Chinese authoring, deterministic assembly, independent bilingual review, independent runtime replay, validators, and actual GFM rendering remain future gates.
