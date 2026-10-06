# S147 Tool Use and Function Calling source-only scope candidate

Fixed English: `1bafaa88bb4668356791150bec3a6d7df38387eb`. Lesson `14-06`, `phases/14-agent-engineering/06-tool-use-and-function-calling`. Prepared from the fresh source-only tree. Local support only; **0 new reviewed drafts**. No Chinese lesson prose is included. The coordinator owns DEPENDENCIES.json and all author/publication steps.

## Fixed scope and exact source package

Future translation target: `i18n/zh/phases/14-agent-engineering/06-tool-use-and-function-calling/docs/zh.md`. Only eligible prose of this fixed English document is a future translation target. All seven package files were read statically, including complete Python/TypeScript, quiz, shipped skill, SVG XML and the verified empty placeholder. Code, quiz, output skill and notebook are context, not additional translation targets. No package manifest or tests are present.

| Path | Bytes | Git blob | SHA-256 | Read coverage |
|---|---:|---|---|---|
| `phases/14-agent-engineering/06-tool-use-and-function-calling/assets/tool-stack.svg` | 5452 | `352699f1099e7b8974aad22575a389a6706b545f` | `49f97dd3da28773e11a8494e81d9deb3d3ebc67cbfffe72836ef12494bb4f5b9` | full |
| `phases/14-agent-engineering/06-tool-use-and-function-calling/code/main.py` | 7030 | `50a710158900a1d037c6fc3a55c91852eb33b172` | `306cad1c9544979767563bca3b1a0ed218d8e3f757ce63707654cf70bbb5aa67` | full |
| `phases/14-agent-engineering/06-tool-use-and-function-calling/code/main.ts` | 8250 | `1fac4d0d3f1420687353ee989ea4193b0e36b2e4` | `fcf75dc4fd5483d79b6ee6983ec345aad5682be4b6fd22823331a73a879fcfcf` | full |
| `phases/14-agent-engineering/06-tool-use-and-function-calling/docs/en.md` | 8174 | `1f1e36a20f62f97635e2926ccc8439ec2f42dc6c` | `73cf8bf653c6148817147fd98b4fc780d9794ca3e9651605f6c8e3f242a14992` | full |
| `phases/14-agent-engineering/06-tool-use-and-function-calling/notebook/.gitkeep` | 0 | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | empty_file_verified |
| `phases/14-agent-engineering/06-tool-use-and-function-calling/outputs/skill-tool-registry.md` | 2783 | `0339ad2ce5ea5f96a8effdf6691047c670a7574e` | `a0ac6c7b967d94894c303f34bcc84e9bdd85f177ec35df3e71d6eb8550690da9` | full |
| `phases/14-agent-engineering/06-tool-use-and-function-calling/quiz.json` | 3660 | `8e34290b92367295ab8d20344f930f2a13ad9f76` | `d3deec25e2eab91a6a3fb4df75f216e685e43e6357a934980fca21c746072e83` | full |

## Prerequisites and implementation context

The source says `Phase 14 · 01 (Agent Loop), Phase 13 · 01 (Function Calling Deep Dive)`. The latter title belongs to 13-02, while numbered 13-01 is The Tool Interface. Both were read completely with all main implementations; preserve the source number/title instead of silently repairing it. Full English prerequisite reading permits later drafting without waiting for Chinese prerequisite acceptance. No complete transitive graph is claimed.

| Path | Bytes | Git blob | SHA-256 | Read coverage |
|---|---:|---|---|---|
| `phases/14-agent-engineering/01-the-agent-loop/docs/en.md` | 9089 | `ebc7eb641819a5eaf93d92e00e86c633b426b3db` | `5f40298b9c1cbabd41a85ede8679c80c55b9a6c9ed92ac661ecd1f9aba18b83e` | full |
| `phases/14-agent-engineering/01-the-agent-loop/code/main.py` | 5651 | `bf3dc0181be003aa6bedb1302e668a161165e01a` | `5fc9514531f6c088b593da55a99877887d8aa96cc0acbb63376fe1787230e534` | full |
| `phases/14-agent-engineering/01-the-agent-loop/code/main.ts` | 5947 | `9a9f5f3efc36e16bd69add723bc406264f13b26d` | `b1a8da96193cb83da568e45f90d57214aed1ac5f57627fd3f94c15aa0dd1b9bc` | full |
| `phases/13-tools-and-protocols/01-the-tool-interface/docs/en.md` | 12806 | `503ff561f2b74fadbeeabced064b8a1437cf14c4` | `03823fa620a739c438f4e907af32445f81cc3a26387b86d13ca90ff0d1f14533` | full |
| `phases/13-tools-and-protocols/01-the-tool-interface/code/main.py` | 7844 | `384f169b8a74a863942daa869535ef05ebaa1070` | `27692fffd3af4163972b8d7d7cb4e328c7f8178fb7889fe6e90eb428c82a056d` | full |
| `phases/13-tools-and-protocols/01-the-tool-interface/code/main.ts` | 8257 | `ea735ef777ddf1ea12a4874e4310b46ae23a86cd` | `213ef94bff3f576af804356b43afd683a8cc374421fb13adcb5a4de45bedb50d` | full |
| `phases/13-tools-and-protocols/02-function-calling-deep-dive/docs/en.md` | 11770 | `8ff9fd5c427174bad344135a102d8de851d0571f` | `4691bbc616aa41426d78eb1e3b77b8635de13cf451272e63fba79b59094a7e71` | full |
| `phases/13-tools-and-protocols/02-function-calling-deep-dive/code/main.py` | 8028 | `9356f00d3d1b776d3ca27118915f050f9c83ecae` | `aeaddcafc116b57f259106982d983c6c49274859ea23dedc182391aec1dacad2` | full |

## Other context and exact coverage

| Path | Bytes | Git blob | SHA-256 | Read coverage |
|---|---:|---|---|---|
| `AGENTS.md` | 13617 | `3be7cf810ba6879a068d6da4756a399eab129740` | `24a1cb3e111107b1a3d922f550776e7573396bc9d0b651b33b1e2cc1d7e1bcc2` | full |
| `CONTRIBUTING.md` | 4933 | `3a561b62567ad298277adcebfbd65853e3e7ccf0` | `fd1d4f0b904f6ec83b2ad1c0290fe537dcc4ebfd3f1bf1d88148dd383059c166` | full |
| `docs/i18n.md` | 14861 | `5eea45dea0c125705ed158db3f0c731b4ef68ace` | `5d0e89958e6c90c3f4f65d8f0369800d350b4a3ceaf51275e2c41f23c6f4aa56` | full |
| `README.md` | 110543 | `fa3bdfe6f7161c0e8176a288443c7e528b0fb9be` | `e65435a0190b0d5d88019b92838a387c1e142699178c3d8881c86de2283804d7` | selected_ranges |
| `ROADMAP.md` | 53970 | `2bfe92922350584f648109bd35997676bc059574` | `715bc5177f4eb6e0671a1497eff871a2048aab3f6706d732d3fc3ab53c29a419` | selected_ranges |
| `site/figures-agents-alignment.js` | 33834 | `9e8bd0a7d6689a738356704e6cc1299518244907` | `56916d4f58e4c5a3842bd9b0b70e417d33b2aa83def373e7a01cc97427351666` | selected_ranges |
| `site/lesson.html` | 249289 | `e0dab75fa0746e01a6618ff5b507975a70967334` | `03a79431a160d84c30793da3433d565b236db586ba53083b45b07e304d15757e` | selected_ranges |

Full AGENTS.md, CONTRIBUTING.md and docs/i18n.md guidance were read. docs/i18n.md contains an unrelated historical Chinese quality sample; it was visible as guidance and was not used as translation memory. No legacy Chinese lesson body, original33 fixture, translation record or review was read. README ranges 820–839/878–893 and ROADMAP 320–334/360–373 establish curriculum paths. Figure helper ranges 1–40/210–287/510–534 and renderer 2775–2783/4298–4335 are targeted static reads, not full-file semantic reads. Whole-file identities do not imply whole-file semantic coverage.

Rollout v1.3 is operative; the historical v1.2/S01 sections were read as history. Local guidance identity: SHA-256 `8aa60a30dd31a7ae579a064a28bedeb324727d8f4d0fa2b26c111fac9b6fb397`, computed Git blob `906bb056ea298cb8e7a517cb98252c881eccc90b`, 12613 bytes. Generic source runtime/PR instructions do not authorize them here.

## Static source format and diagram treatment

Immutable scanner SHA-256 `d89de5eec36e10edcc391330d973632e3ceedb33fe679de3503dab52a7f6ece8` was used only for lossless English block parsing. 97 blocks; 46 nonempty non-fence/non-display-math blocks; 1068 approximate English whitespace units (not tokens); 9 H2 and 6 H3 headings. Three fences: two bare and one figure. One three-column table has eight body rows. Exact block identities and line spans are in SOURCE-BLOCK-MAP.json. No source content-loss blocker was found.

The two bare fences may later receive only the existing reversible `text` label; payload bytes remain protected. `tool-routing` is the exact figure marker and must not be translated. The widget is registered at site/figures-agents-alignment.js:526, with the relevant implementation at 220–265. It uses fixed demonstration scores, not model measurements. The lesson renderer creates the figure host; the generated figure manifest is absent from this fixed tree and is not evidence. No live rendering inspected.

Future unchanged support asset: `i18n/zh/phases/14-agent-engineering/06-tool-use-and-function-calling/assets/tool-stack.svg` from `phases/14-agent-engineering/06-tool-use-and-function-calling/assets/tool-stack.svg`; 5452 bytes; Git blob `352699f1099e7b8974aad22575a389a6706b545f`; SHA-256 `49f97dd3da28773e11a8494e81d9deb3d3ebc67cbfffe72836ef12494bb4f5b9`; mode `100644`. It is not embedded by this English body. It has not been copied/installed. Required future separate asset manifest: `i18n/zh/.curated/lessons/14-06/supporting-assets.json`; it must bind this nonembedded SVG identity for cumulative replay and asset audit. The future content surfaces allowed here are the translated `docs/zh.md`, the byte-identical `assets/tool-stack.svg` copy, and that supporting-assets.json manifest; author record/evidence destinations remain coordinator-owned. Do not create either asset copy or manifest during this support preparation. Do not add an embed or translate SVG text. GitHub GFM, interactive website, mobile and PDF are separate future checks.

## Terminology calibration and common support

common152 candidate SHA-256 `adb98cb4c54c97f8485605d3d90e10fbe80209705ffcae1545170c1c10c39beb`; independent preparation receipt SHA-256 `4d8b3ece2ce2abb6455304075636495184be45bad78d9da5844955b666e8e447`. Exact common149 identity metadata and order preserved, with accepted S143/S144/S145 terminology appended. Common152 = 144 terminology + 8 immutable controls; with future own3 the lane total is 155. No common/control/own3 install occurred.

Both core glossaries and S22/S40/S45/S116/S132/S135/S138 plus all three new S143/S144/S145 glossaries were read fully. Targeted relevant rows from other pinned glossaries were searched and calibrated. All 144 terminology payloads matched SHA-256/Git blob/bytes; identity-only files are not claimed as semantically read. Per-file full versus targeted coverage and exact pins appear in source-readiness.json. Historical candidate/pending labels within frozen terms do not supersede external accepted identity evidence. This preparation is not the future author's proposal/calibration.

## Fixed-source correctness and runtime caveats

### R01 · prerequisite_number_title_conflict

Locations: docs/en.md:7; README.md:832-833; ROADMAP.md:328-329.

The exact source prerequisite says Phase 13 · 01 (Function Calling Deep Dive). Fixed 13-01 is The Tool Interface; the named deep dive is 13-02. Read and pin both complete English documents and all main implementations, alongside 14-01. Preserve source numbering and title; do not silently replace 01 with 02. No full transitive prerequisite DAG claimed.

### R02 · metadata_and_missing_tests

Locations: docs/en.md:6; code/main.py; code/main.ts; quiz.json; AGENTS.md.

Metadata says Python (stdlib), but both Python and TypeScript main files are shipped. The seven-file package contains no tests or package/dependency manifest. Quiz has 7 questions: 2 pre, 3 check, 2 post, versus the root 6-question contract. Preserve these inputs and mark tests absent; no audit, test pass, or language-metadata repair is claimed.

### R03 · parallelism_claim_not_implemented

Locations: docs/en.md:70-78,95,104; code/main.py:dispatch_many; code/main.ts:dispatchMany.

Both batch methods synchronously iterate (Python list comprehension; TypeScript map). They preserve supplied correlation IDs and input order but neither enforce unique IDs nor implement independent parallel execution. The demo contains five calls over three registered tools, including an invalid enum and an unknown tool, while prose describes three tools and one malformed call. There is no model or agent turn; calls are hard-coded.

### R04 · sandbox_timeout_not_implemented

Locations: docs/en.md:14,82,93,118; code/main.py:ToolDef/dispatch; code/main.ts:ToolDef/dispatch; assets/tool-stack.svg.

timeout_s=5.0 and timeoutMs are stored declarations and never enforced. No filesystem/network policy, memory cap, process isolation, circuit breaker or cancellation exists. Executors run directly in the host process. The SVG asserts enforced timeouts, circuit breaker, tracing and audit trail that neither implementation supplies. Do not turn production-shape into production-safe or implemented sandboxing.

### R05 · json_schema_subset_limits

Locations: docs/en.md:59-68,92; code/main.py:_coerce/validate; code/main.ts:coerce/validate.

Validators inspect top-level required fields, types, enums and numeric bounds. Array items and nested object properties are not recursively validated; format, pattern, lengths, unions, refs and other JSON Schema constraints are unsupported. Unknown fields are always rejected regardless of additionalProperties, and root type is not validated. Unknown schema types fall through. This is not a full JSON Schema validator or the date/email/URL parser promised in prose.

### R06 · coercion_and_numeric_edge_cases

Locations: code/main.py:_coerce/validate; code/main.ts:coerce/validate; docs/en.md:63,117; outputs/skill-tool-registry.md:17.

Python int(string) and TypeScript Number(string) differ: TypeScript can accept empty/whitespace strings as zero and integral decimal/exponent/hex forms rejected by Python int. Python numeric coercion accepts non-finite floats; TypeScript filters non-finite parsed numeric strings but accepts already-number NaN/Infinity for number. NaN bypasses ordinary min/max comparisons. Python excludes bool from numeric types. Coercion already exists despite exercise 2, while output-skill example says reject float-as-string. Do not silently unify these policies.

### R07 · exception_and_registry_boundary

Locations: code/main.py:register/dispatch/validate; code/main.ts:register/dispatch/validate.

Only executor invocation is inside try/catch. Malformed runtime args or malformed schemas can fail earlier; annotations do not validate external payloads. Duplicate tool names silently overwrite. Executor return annotations do not enforce string results at runtime. Structured ToolResult metadata contains free-form error strings, not a validated JSON error protocol. Preserve source never-raise wording but keep this caveat separate.

### R08 · toolformer_loss_and_scale_simplification

Locations: docs/en.md:3,12,27-31,127.

Toolformer paper Section 2 filters on a thresholded weighted future-token loss reduction versus no-call and call-without-result baselines; the lesson compresses that to next-token loss. Its self-supervision still starts from a handful of demonstrations per API. Section 4.4 reports similar small-model performance with/without tools and emergence near 775M in its setup; it does not establish a universal smaller-model harm or 2026-most-7B reliability rule. Preserve the fixed lesson claims without endorsing or correcting them.

### R09 · benchmark_weights_and_dated_claims

Locations: docs/en.md:3,33-45,108,128; quiz.json; assets/tool-stack.svg.

BFCL V4 release composition confirms 40/30/10/10/10 as score weights, not dataset proportions or pass rates. Format sensitivity and relevance are listed as non-scoring. Agentic scoring covers web search and memory; broader descriptions are shorthand. V3 state-transition checking coexists with AST-based checking across the suite. Single-turn solved/near-solved, 20+ step drift, 40 steps, 2026 de facto and description quality as #1 cause are fixed-source claims, not universal measurements or results from this toy.

### R10 · provider_shape_and_correlation_scope

Locations: docs/en.md:49-57,74-76,108; 13-02/docs/en.md and code/main.py.

The lesson uses Anthropic-style tool_use_id/tool_result as a generic explanation. OpenAI Responses uses call_id/function_call_output and a flat parameters definition; function.parameters is Chat Completions-style. Both providers support schema descriptions, but API dialect and strictness differ. 13-02 conflates Responses with Chat Completions and contains contradictory Anthropic strictness descriptions; no adapter/live-provider compatibility is demonstrated here. Preserve exact identifiers; do not rewrite the API examples to current syntax.

### R11 · forward_reference_and_output_scope

Locations: docs/en.md:82; outputs/skill-tool-registry.md.

Lesson 09 is called sandboxing/permissions, but fixed 14-09 is Hybrid Memory. Output references 17/21/23/30 are forward pointers, not additional direct prerequisites. The skill requests <=30-tool scoping, destructive-action confirmations, OTel spans, a dispatch graph and provider-ready catalogs; these are proposed deliverables, not shipped implementation features, evidence of security acceptance, or instructions to run tools in this preparation.

### R12 · figure_surface_and_asset

Locations: docs/en.md:84-86; site/figures-agents-alignment.js:220-265,526; site/lesson.html:4314-4315; assets/tool-stack.svg.

tool-routing widget uses four hard-coded query/similarity arrays, not a live model, embedding calculation or observed routing benchmark. It is distinct from the unembedded tool-stack.svg. Preserve figure payload and SVG bytes; no new image embed. The lesson renderer creates a figure host, whereas GitHub GFM shows the figure fence as code. No browser, GFM, website, mobile or PDF acceptance was performed.

### R13 · prerequisite_implementation_limits

Locations: 14-01 docs and main.py/main.ts; 13-01 docs and main.py/main.ts; 13-02 docs and main.py.

14-01 ToyLLM is scripted and ignores history; its calculator evaluates allowlisted expressions without resource isolation. 13-01 fake router returns after a tool result, validators do not implement advertised min/max, weather is stub data and time labels do not convert timezone; its would-confirm branch still executes. 13-02 has three parse functions rather than documented canonical_call, and schema conversion is partial (e.g. type arrays are not normalized into a Gemini nullable schema). These are static contextual caveats, not runtime findings.

### R14 · source_format_and_guidance_boundaries

Locations: docs/en.md:51,100; AGENTS.md; CONTRIBUTING.md; ROLLOUT-PLAN.md.

Two bare fences conflict with root tagged-fence guidance. Later authoring may apply only the existing reversible text-tag rule and must keep payloads exact. Source is losslessly scanned; no content-loss blocker found. Root audit/runtime recommendations and generic translation placement do not override the narrower source-only task or rollout v1.3. No source/control/checker edits or new exceptions.

### R15 · release_and_runtime_limits

Locations: this source support preparation.

Readiness and lexical candidates add zero reviewed drafts and are not an author proposal, first-write record, strict acceptance, independent language review, rendered-page inspection, remote byte readback, regression or publication. Formal160/actual159 and future actual162 membership are coordinator context, not executed here. Source and all common/control payloads remain unchanged; no support installs, model/GPU/provider API/download/package install/course command or test execution occurred.

## Narrow primary-reference checks

- https://arxiv.org/abs/2302.04761 — abstract and author/version metadata only. Confirms self-supervised tool use with a handful of API demonstrations; no local model reproduction.
- https://arxiv.org/html/2302.04761v1 — targeted Section 2 filtering and Section 4.4 scaling passages, not full-paper review. Thresholded weighted future-token loss criterion; smaller-model result is not the lesson broad harm claim.
- https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html — release introduction, scoring composition and methodology only. Confirms 40/30/10/10/10 scoring weights; format sensitivity is non-scoring; no leaderboard or agent was run.
- https://gorilla.cs.berkeley.edu/leaderboard.html — page introduction and methodology metadata only. A changing public benchmark, not proof of universal 2026 solved status. No current ranking reproduced.
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview — client tool schema/call/result overview and strict-tool-use pointer only. input_schema and tool_use/tool_result are Anthropic protocol fields; client execution remains application-owned.
- https://developers.openai.com/api/docs/guides/function-calling — targeted function-definition and result-correlation passages only. Responses uses flat parameters and call_id/function_call_output; no full API audit or request executed.

These checks bound source claims; they do not authorize new lesson prose, a translator note, a source correction or updated provider examples. Preserve the fixed source and keep caveats separate.

## Pending gates and count discipline

Coordinator context is formal160 / actual159. Next actual162 is S145 plus the next two accepted lessons; the third new lane enters a later wave. None of those regressions was executed by this worker. DEPENDENCIES.json remains coordinator-owned. Own3 publication, independent readback/installation, author assignment, actual first-write calibration, translation body/record, strict, independent full language review, real GFM inspection and final remote-byte acceptance remain pending. No increment, merge, deployment, website/PDF/mobile or CI claim is made.
