# S163 Anthropic workflow patterns source-only scope

Fixed English: 1bafaa88bb4668356791150bec3a6d7df38387eb.
Source: phases/14-agent-engineering/12-anthropic-workflow-patterns/docs/en.md.
Source Git blob: fdd2bccd65849a4c6ac663805a25f82f28641af0.
Source SHA-256: 55c8edf5c8a62595d2db17d555b2ca3cddf12a8b8d8bdf0ff745b347000c0a57.

Status: local own3 source-only candidate. No Chinese lesson prose, translation record, capture, review, target QA, publication or installed-support claim. No remote write or course execution.

## Source and context coverage

A fresh git archive from the fixed source excludes all i18n. All5411 non-i18n source file Git blobs were verified. Complete target docs/en.md, code/main.py, output skill, quiz and SVG XML were read statically; empty notebook placeholder inventoried. Complete prerequisite14-01 English and conceptual context14-05/14-06/14-07 English were read; these context packages' other files were not fully semantically reviewed. workflowChain function and registry in site/figures-agents3.js were read. No transitive prerequisite DAG or full-glossary semantic read is claimed. Only14-01 is an explicit prerequisite;14-05 is a conceptual reference.

## Source caveats, kept separate from future translation

- The context-engineering paragraph explicitly names an earlier lesson06 before renumbering. Current14-06 is tool use;14-07 contains related virtual-context material. Exact intended compression lesson remains unresolved. Do not silently redirect or repair.
- Signature summaries differ from code: prompt_chain needs llm; parallel_vote needs llm and has no aggregator argument; orchestrator_workers needs synth. Preserve prose signature strings and actual code independently.
- parallel_vote uses a sequential list comprehension, not concurrent execution. Counter chooses the most frequent result; ties follow first encounter. n=0 fails at winner lookup. Conceptual sectioning/voting and claimed concurrency remain source descriptions, not tested implementation capabilities.
- orchestrator_workers uses deterministic Worker.handles predicates rather than an orchestrator LLM. Demo synthesis joins strings. ScriptedLLM is a deterministic mock, not a provider client.
- evaluator_optimizer can exhaust max_iter and return its last failing candidate; max_iter=0 leaves candidate unbound. The output skill requests fail-pass-through fallback but the demo does not declare a separate fallback. A bounded loop does not prove a passing result.
- Seven quiz questions (2pre/3check/2post) conflict with AGENTS six-question contract; no code/tests directory exists. No tests or sample code were run.
- Most-cited post, framework line counts, 200k context window and SDK/framework recommendations remain historical source claims, not externally revalidated current guidance or endorsement.
- workflow-patterns.svg is not embedded in en.md. Prior actual-source SVG preflight found33 readable labels,26 rectangles and all8 defined arrows. Missing conceptual connectors are source topology: routing only points to refund, parallelization has no connectors, orchestrator connects workerA only and feedback has no drawn return loop. No source repair, insertion, hold waiver or target acceptance follows.

## Protected surface and future gates

Preserve source code, formulas, numbers, metadata, names, paths, URLs, SVG bytes and workflow-chain figure payload. The existing bare-fence→text allowance may later be recorded; no new strict exception. Mandatory future checks include original strict, full independent bilingual review plus separate Chinese reading, read-only CJK-bold diagnostic with manual context adjudication, manual raw-angle Markdown review and actual fixed-target GitHub GFM coverage. Source SVG pixels do not establish targetGFM, website, mobile or PDF acceptance. No CI success is implied by zero checks.

Common164 contains156 terminology files and8 immutable controls, plus own3 gives167 required installed supports. Source assets/context and original33 fixtures are separate from this count; fixtures remain test-only and are not imported here. Exact164 pin objects/order are retained.39 historical original receipt gaps remain unresolved. No recovered public binding is asserted to recreate those originals.

Clean172 index commit61a301b1d2f5321f8bd03e25fda3ed76946d099a is independently read back: formal172, actual cumulative171. No newer cumulative run is claimed. Existing holds06-12,04-26,14-09,14-10,07-01 stay unchanged. v1.3 single-course and batch gates apply; coordinator owns serialized fork-only publication. Independent common/own3 review, publication, independent full readback, all167 installed supports, post-installation terminology calibration and explicit coordinator prose clearance must occur before first lesson prose write.
