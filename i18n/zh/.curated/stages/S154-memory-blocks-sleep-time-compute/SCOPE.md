# S154-memory-blocks-sleep-time-compute source-only scope candidate

Fixed English `1bafaa88bb4668356791150bec3a6d7df38387eb`; source [phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/docs/en.md](https://github.com/Activer007/ai-engineering-from-scratch/blob/1bafaa88bb4668356791150bec3a6d7df38387eb/phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/docs/en.md). Git blob `64e3268d0a35b8acb42a01d73a2b23ea453db741`, SHA-256 `c9d406091f226f33e6b8336bd887d12e7a8cdbe769b257a6c6bda4988eff6f3b`.

Status: COMPLETE LOCAL OWN3 CANDIDATE, pending independent review, serial remote support publication/readback and installation. Common158 = 150 terminology files + 8 immutable controls; own3 gives161 prospective supports. No author assignment, Chinese lesson prose, course execution or formal/pending count increment.

## English-first coverage

Complete target package: 6 files. Direct prerequisites: 14-07, with 2 English docs/main files fully read. Detailed fixed pins and semantic line ranges are in DEPENDENCIES.json. Only direct prerequisite closure is claimed; preceding Chinese acceptance is not an author gate.

Fresh author tree has exactly5411 fixed non-i18n files from the Git archive, with all bytes, Git blobs, Git modes and POSIX modes verified. All12 baseline i18n files excluded. No supports, Chinese bodies, records, reviews or original33 fixtures installed. Common lexical identity verification does not claim semantic rereading of all158 supports.

Source scanner join and identity assembly are lossless. English self-comparison is not Chinese strict acceptance. Bare-fence eligibility: block67 lines92-94. The only eligible later label normalization is the unchanged original bare-to-text rule; record it before first capture and protect payload bytes.

Preserve every code/math/number/metadata/API/model/identifier/path/URL/Mermaid/figure/SVG surface. Source caveats remain outside Chinese prose; do not modernize or silently repair them.

## Source caveats

### MEMORY-DEMO-NOT-ASYNC-PERSISTENT

phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/code/main.py:50-72,82-104,174-244; phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/docs/en.md:3,55-65,83-96. All stores and histories are process-local. There is no database, file persistence, Recall store, transcript pagination, model inference, background task, thread, asyncio or concurrent scheduler. main calls four primary.turn methods then one synchronous sleep.run. The response is a string echo, not reasoning from rendered blocks. No latency measurement supports the absolute no-latency-cost claim.

### MEMORY-DEMO-NO-CONSOLIDATION-TRIGGER

phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/docs/en.md:88,96; phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/code/main.py:46-47,146-149,179-224. Prose promises three turns and a summarizing pass, but the code has four turns. Static literal arithmetic gives human=72 characters versus trigger int(180*0.8)=144; task=119 versus 176; persona=0 versus 128. Therefore the supplied pass does not call _summarize; it only invalidates the explicitly named archival record. Both city strings remain in core. Values were derived from inert literals, without executing the course.

### MEMORY-SCHEMA-AND-CRUD-GAP

phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/docs/en.md:46,50-53,85-86; phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/code/main.py:14-72. Block lacks the documented id. It has version/history instead. BlockStore implements create/get/labels/render, no delete and no near_limit helper on the store itself. Existing label creation silently replaces the block. Updates live on Block; no exported block_read or block_summarize tools match the prose surface. Letta-shaped does not mean an API-compatible implementation.

### MEMORY-CAP-AND-HISTORY-NOT-GUARDS

phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/code/main.py:23-47,54-57; phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/docs/en.md:73-74,112-113. append, replace and rewrite never enforce limit or reject invalid limits. near_limit only reports character length. String replace replaces every matching occurrence, not a structured field. Version/history retain prior strings but have no persistence, source citation, visible diffs, optimistic concurrency, locks or review policy. History can grow without bound.

### MEMORY-SUMMARIZER-LOSS

phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/code/main.py:160-171. _summarize is a period-splitting prefix picker, not semantic summarization or deduplication. It stops at the first overlong sentence; if that is first it returns just a period. Later sentences can be dropped irrespective of importance, contradictions or citation preservation.

### MEMORY-INVALIDATION-AND-SAFETY

phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/code/main.py:75-104,140-157; phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/outputs/skill-memory-blocks.md:14-31. Archival has no vector/KV/graph backend, retrieval score, timestamps, provenance or learned contradiction detector. A caller-supplied substring matches records case-insensitively and flips valid=False. Invalidation preserves text but does not establish which claim is true. Persona/Safety review, poisoning protection, learned_context writes and token-overlap dedup are requested goals/exercises, not implemented defenses.

### MEMORY-OUTPUT-CONTRACT-CONFLICT

phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/outputs/skill-memory-blocks.md:18,23; phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/code/main.py:115-127. The artifact asks the primary to issue raw writes but rejects every synchronous memory operation except direct lookup. Raw writes in the demo occur synchronously before the response. The prompt also demands persistence while the bundled toy is in-memory. Preserve this internal distinction; do not treat the artifact as a fulfilled implementation.

### MEMORY-TIERS-HISTORY-ANALOGIES

phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/docs/en.md:25,31-37,41,69,101-102. The two-versus-three-tier history is an explanatory grouping, not proof that recall and archival were absent from MemGPT. Human/Persona naming and typed refer to named structured string blocks, not necessarily a strongly typed semantic schema. Agent SDK skill loading is an analogy rather than identical always-in-context core memory. No generic API migration guarantee follows from matching field names.

### MEMORY-SOURCE-CONTRACT-DEVIATIONS

phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/quiz.json:1-90; phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/docs/en.md:92-94; phases/14-agent-engineering/08-memory-blocks-sleep-time-compute/code/main.py:1-6. Quiz contains seven questions (2 pre, 3 check, 2 post), not six; no tests directory exists; the code header lacks the required lesson/spec path. Run fence is untagged. These are fixed-source AGENTS deviations, not a reason to add tests, retag source or change validators.

### MEMORY-DIRECT-PREREQUISITE

phases/14-agent-engineering/07-memory-virtual-context-memgpt/docs/en.md:31-69,83-107; phases/14-agent-engineering/07-memory-virtual-context-memgpt/code/main.py:22-118,127-138. MemGPT prerequisite is a scripted in-memory OS analogy. MainContext evicts messages, never summarizes; Archival search is Jaccard token-set overlap rather than BM25. Citation fields default to s0/0 because MemoryTools.insert does not pass the turn; core is unbounded; getattr dispatch is not an allowlisted production tool router. Broad all-production-systems and provider product claims were read but not comprehensively revalidated.

## Required later gates

- Read-only CJK-bold adjacency risk diagnostic using unchanged prior packaging/check_bold_adjacency.py, followed by manual context review, before any future body publication. Risk scan never replaces original strict or GFM.
- Manual raw angle-tag Markdown review outside protected code, especially literal model/control tags and comparisons; no automatic global replacement, no new checker exception.
- Original local strict and source-target protected payload/structure checks, independent complete EN-to-ZH semantic review and separate full Chinese read.
- Actual fixed-target GitHub GFM inspection of every table, code, math, long line, Mermaid/figure and exact SVG; source local PNG is not GFM/site/mobile/PDF acceptance.
- One independent final remote byte/readback gate and separately scoped actual cumulative regression after accepted lessons.

Only the coordinator may write remotely, fork-only, with at least60seconds between publication groups. No support installation before independent immutable byte/tree/ref readback. Fresh author then supplies own actual terminology proposal/calibration and first-write chronology. Frozen support pending/null states are historical snapshots, not fabricated future commits.

## Baseline and held sources

Verified formal166 at `34efa23be08970d25291d057b108949ddceef7e2`; actual165 PASS remains separately scoped. S151/04-25 is the first member of future actual168. The next two accepted active courses complete that cohort in acceptance order; the remaining new course starts a later cohort. Preparation cannot infer future acceptance or actual168 execution. S149/06-12 remains held. S155/04-26 remains reserved and held for source-table content loss incompatible with original strict; approved active replacement is S156/04-27. Neither hold changes historical seven blocker rows. Source-only S155 files prepared before hold are retained inactive.

Common158 SHA-256 `a4ed394c03650b70a6e48172186d37c5bc255dc887753c058be7a73bc5a78875` retains exact prior155 objects/metadata/order and appends only accepted S150/S152/S151 terminology, including format-repair descendant proofs. Required repository i18n documentation exposed an unrelated old Chinese sample; it is not translation memory.

## Current official-source caveats carried into this support

### MEMORY-V1-DATE-REASONING

The official Letta V1 owner post is dated October14,2025, while fixed source calls the rewrite2026. Native reasoning/direct assistant output is supported, but encrypted reasoning cannot be mutated or transferred across different models. Handling provider-specific reasoning state does not establish cross-provider portability or access to all raw internal thoughts. Current Anthropic thinking blocks may expose a summary rather than the entire internal process. Preserve the source date and wording; do not promise portability or raw-thought visibility. Keep this source discrepancy outside Chinese prose; no silent correction. Primary references: https://www.letta.com/blog/letta-v1-agent/ and https://platform.claude.com/docs/en/build-with-claude/extended-thinking ; checked2026-10-06.

### MEMORY-CURRENT-API-ROLE-CAVEATS

Current owner memory-block APIs use client.blocks/client.agents.blocks; block_* names in lesson are pedagogical, not certified SDK methods. Whole-value writes use last-write-wins behavior. Letta April21,2025 sleep-time design does not give the primary agent core-editing tools, unlike this toy raw-core-write design. Asynchronous offloading does not prove zero total compute or response-latency impact. Preserve source interfaces and design, do not modernize. Primary references: https://docs.letta.com/v1-sdk/memory/memory-blocks and https://www.letta.com/blog/sleep-time-compute/ ; checked2026-10-06.

