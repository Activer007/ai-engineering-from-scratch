# S144 Self-Refine and CRITIC source-only scope candidate

Fixed English commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`. Lesson: `14-05`, `phases/14-agent-engineering/05-self-refine-and-critic`. Local support preparation only. This candidate adds **0 reviewed drafts**. It contains no Chinese lesson body. The coordinator owns DEPENDENCIES.json, formal157/common149 bindings, author trees and every remote write.

## Scope and fixed inputs

Future translation target: `i18n/zh/phases/14-agent-engineering/05-self-refine-and-critic/docs/zh.md`. Translate eligible prose of `docs/en.md` from the fixed English only. Read the whole six-file package, including the empty placeholder, and complete direct prerequisite English documents and all their main implementations. Code, quiz, shipped output skill and notebook placeholder are contextual inputs, not additional translation targets.

| Source package file | Bytes | Git blob | SHA-256 | Read coverage |
|---|---:|---|---|---|
| `phases/14-agent-engineering/05-self-refine-and-critic/assets/refine-loop.svg` | 4607 | `edf23a4b0388e10895ab87d22b426dee037bd4f2` | `c4356e5061c054023e652a250e0a73b5304993f814a204b66b4a29805ce468a8` | full |
| `phases/14-agent-engineering/05-self-refine-and-critic/code/main.py` | 4103 | `499fa5868be8f6bc52612ef305a65d2bb5177150` | `83180d9695228d693d7033c2e2a592f21104fb3c363c2bd9456808fd8a5013c4` | full |
| `phases/14-agent-engineering/05-self-refine-and-critic/docs/en.md` | 8504 | `e3dcbcbddf3c26e5b373b281449a34b073123bbf` | `9c7f53947f9886f431c8f1a5d51f4f1c97af01ff68887f33275dbd64892f93e3` | full |
| `phases/14-agent-engineering/05-self-refine-and-critic/notebook/.gitkeep` | 0 | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | empty_file_verified |
| `phases/14-agent-engineering/05-self-refine-and-critic/outputs/skill-refine-loop.md` | 2578 | `c662046c84f8eb11aed127bfd620a24047d1d8e8` | `d47d64c82222c13ecadfdafd5d1a4b9ad25aa3870dce032fb3513538bbc1ce36` | full |
| `phases/14-agent-engineering/05-self-refine-and-critic/quiz.json` | 3570 | `e3af6cdf2c6047dee9c9ffe523fa1c154d5465fa` | `dd9aa876c06faf3ef085217904188c71c253825332c71f81624ff8792dbb94dc` | full |

| Direct prerequisite context | Bytes | Git blob | SHA-256 | Read coverage |
|---|---:|---|---|---|
| `phases/14-agent-engineering/01-the-agent-loop/docs/en.md` | 9089 | `ebc7eb641819a5eaf93d92e00e86c633b426b3db` | `5f40298b9c1cbabd41a85ede8679c80c55b9a6c9ed92ac661ecd1f9aba18b83e` | full |
| `phases/14-agent-engineering/01-the-agent-loop/code/main.py` | 5651 | `bf3dc0181be003aa6bedb1302e668a161165e01a` | `5fc9514531f6c088b593da55a99877887d8aa96cc0acbb63376fe1787230e534` | full |
| `phases/14-agent-engineering/01-the-agent-loop/code/main.ts` | 5947 | `9a9f5f3efc36e16bd69add723bc406264f13b26d` | `b1a8da96193cb83da568e45f90d57214aed1ac5f57627fd3f94c15aa0dd1b9bc` | full |
| `phases/14-agent-engineering/03-reflexion-verbal-rl/docs/en.md` | 8403 | `7aa94b1dc349bdb8aa5ea52103dd268b722ec5e9` | `9afabebcab9e1ce6d6ab3b2b0ceabd8b0aa308b25a73b8d6510fc2f2739f9b36` | full |
| `phases/14-agent-engineering/03-reflexion-verbal-rl/code/main.py` | 3651 | `e1ad5e43a1bfd41ab51d89734d3652cfe2d4c592` | `6e3e0c338bcdecf5410de0a0194dec48fe41d9514e49432799c701472b725d1e` | full |

| Repository guidance | Bytes | Git blob | SHA-256 | Read coverage |
|---|---:|---|---|---|
| `AGENTS.md` | 13617 | `3be7cf810ba6879a068d6da4756a399eab129740` | `24a1cb3e111107b1a3d922f550776e7573396bc9d0b651b33b1e2cc1d7e1bcc2` | full |
| `CONTRIBUTING.md` | 4933 | `3a561b62567ad298277adcebfbd65853e3e7ccf0` | `fd1d4f0b904f6ec83b2ad1c0290fe537dcc4ebfd3f1bf1d88148dd383059c166` | full |
| `docs/i18n.md` | 14861 | `5eea45dea0c125705ed158db3f0c731b4ef68ace` | `5d0e89958e6c90c3f4f65d8f0369800d350b4a3ceaf51275e2c41f23c6f4aa56` | full |

Local rollout guidance v1.3 was read in full: SHA-256 `8aa60a30dd31a7ae579a064a28bedeb324727d8f4d0fa2b26c111fac9b6fb397`, 12613 bytes. Its operative instructions supersede its historical v1.2 scheduling/count examples. Generic repository run/install/push commands were read, never executed. The historical machine-translation workflow in docs/i18n.md does not authorize using old Chinese, running NLLB, enabling CI or changing this curated workflow.

## Source structure and protected surfaces

The English document has 144 lines, 16 headings, 1067 approximate prose words, 3 fenced blocks, one three-column/eight-row key-term table, and four external reference links. The planning word count removes fences and inline code and is not model-token measurement.

- Bare fences are at lines 31-39 and 104-106. Only the existing permitted reversible `text` tag may be added later; payloads stay exact. The run command remains text and is not executed.
- Preserve the `figure` fence at lines 86-88 and payload `self-refine`. No formula block, inline math or Mermaid block appears in this body. Preserve numeric gains, dates, max-iteration comparisons, OR/AND expressions, identifiers, citation names, path and URL targets.
- Static asset `phases/14-agent-engineering/05-self-refine-and-critic/assets/refine-loop.svg` is not embedded in the source body. Future copy target is `i18n/zh/phases/14-agent-engineering/05-self-refine-and-critic/assets/refine-loop.svg`, retaining source blob `edf23a4b0388e10895ab87d22b426dee037bd4f2`, SHA-256 `c4356e5061c054023e652a250e0a73b5304993f814a204b66b4a29805ce468a8`, 4607 bytes. Later asset/double-replay inventories must include it; do not inject an image link or translate SVG labels.
- Website context `site/figures-agents2.js` has blob `22f8dde632f44b3c4f4f9faa904acdd516ff76c8`, SHA-256 `bdb342cf800e6d21566bdc7cfd2eda761a5ef1a0dd09bcaf06669a537d419879`, 29340 bytes. Only lines 1-22, 130-230 and 430-450 were read, including the complete selfRefine function and registration. The widget draws a synthetic quality curve `94 - 42 * Math.pow(0.62, k)`; it is not paper data, the toy-program result, or a rendering of the static SVG.
- Forward references in the shipped skill to Lessons 09/12/16/23/30 are not newly declared learning prerequisites. This task does not translate them or execute their commands.

## Source caveats for faithful translation and later review

### R01: stop policy mismatch

Location: `docs/en.md:23,31-39,58-65,74,100,137; outputs/skill-refine-loop.md:17; code/main.py:78-88; assets/refine-loop.svg`.

The prose combines verifier success OR (self-eval acceptance AND at least 2 iterations) OR budget exhaustion. The toy chooses exactly one verifier, exits on its first True, and otherwise stops at max_iters. The key-term row compresses the logic to verifier passes OR no feedback AND iteration cap, omitting the separate budget OR. The skill calls its OR expression a conjunction. Preserve each source expression; do not normalize them into one alleged implemented policy.

### R02: scripted demo claim mismatch

Location: `docs/en.md:108; code/main.py:28-56,78-88,119-120`.

Static inspection shows self-feedback flags the initial Paris/Germany error, but returns a critique without germany or everest, the only keywords generate uses to change output. It therefore repeats the first output to the cap. CRITIC critiques contain those tokens and statically lead to repair then acceptance on iteration 3. This is a scripted critique/refiner interface mismatch, not a measured LLM failing to notice its own factual error. No demo was executed.

### R03: history and role mismatch

Location: `docs/en.md:41,96-100,135; code/main.py:28-48,51,74-75`.

The list retains all attempts but generate uses only history[-1]; refine ignores its prev and critique arguments, and topic is unused. The documented feedback component is implemented as feedback_self. No model or prompt execution exists. Preserve identifiers and full-history claims as source text, with this caveat kept separate.

### R04: verifier coverage and boundary

Location: `docs/en.md:92; code/main.py:13-17,59-71`.

verify_external repeats two substring co-occurrence checks inside a loop; computed key is unused, and the listed Sun/Earth error is never checked. It is not a general reference lookup. It allows exactly 60 characters despite under 60 prose, counts lines starting with a hyphen rather than requiring exactly three total lines, permits extra non-bullet lines, and counts the full line including the prefix. feedback_self checks neither bullet count nor length. Do not imply comprehensive factual or format verification.

### R05: result and budget semantics

Location: `code/main.py:78-88; docs/en.md:120; outputs/skill-refine-loop.md:15-29`.

The code returns Attempt records with freeform critique strings and a bool; the skill requests structured JSON violations/suggested_fixes. After the last failed verification, the loop computes a refinement that is neither verified nor appended before returning history. The public parameter is max_iters, while the exercise says max_iterations=1. Iterations count verification attempts rather than a guaranteed number of completed useful improvements; nonpositive caps yield an empty history. No local CLI argument parser is provided.

### R06: paper headline boundary

Location: `docs/en.md:3,41,43,135`.

Keep +20, 7, GPT-4, dates and author names exact. The Self-Refine abstract describes approximately 20 percent absolute average improvement over task metrics; this is not a relative gain or a measured outcome here. The lesson strengthens history ablation into sharply/collapses language; the targeted reference check did not independently validate that exact magnitude. Do not silently soften or amplify it in translation.

### R07: critic paper abstraction

Location: `docs/en.md:47-56,123; outputs/skill-refine-loop.md:15-17`.

The paper describes LLM interaction with tools and natural-language critiques; the lesson abstracts this as replacing feedback with an external verifier, while the skill mandates structured JSON. These are not identical protocols. The lesson enumerates four example tool groups, then asks for three categories in CRITIC Section 3; keep the exercise wording and log the ambiguity. Without-tool CRITIC is an ablation, not proof of literal equivalence to every Self-Refine implementation.

### R08: sdk guardrail analogy

Location: `docs/en.md:78,112,124; assets/refine-loop.svg`.

Official output-guardrail documentation says a tripwire raises an exception and halts the run. Output checking is not itself a built-in generate/critique/refine retry loop. The source can retry wording must not become automatic retry; the SVG stronger enforce retries assertion stays an asset caveat. A pure function also is not the same thing as single-LLM Self-Refine. No SDK was installed or called.

### R09: dated or broad assertions

Location: `docs/en.md:3,23,56,65,74,82-84,112,121`.

Every framework, 2026 default, most guardrail stacks, the fixed 30% noise characterization, Gemini 2.5 Computer Use equivalence, and the recommendation for a smaller critic are source assertions, not validated universal current practice. Anthropic supports an evaluator-optimizer workflow with separate generation/evaluation calls, but the checked article passage does not establish the lesson claimed mandatory substantially different prompts. Preserve attribution and date; no silent factual update.

### R10: quiz contract

Location: `quiz.json; AGENTS.md:quiz.json schema`.

The package has 7 questions with 2 pre, 3 check, 2 post; root guidance calls for 6 with 1 pre, 3 check, 2 post. Quiz is read-only context here. Do not remove or relabel questions, translate the quiz, or claim root audit/course-test success.

### R11: output skill scope

Location: `outputs/skill-refine-loop.md`.

The reusable skill has its own JSON, tracing, sandbox, refusal and iteration-budget rules: default 4, reject >=10, and 3-4 as a heuristic. It mentions Lessons 09/12/16/23/30 as forward context. These are source content, not instructions to invoke tools, install packages, collect telemetry, or expand translation to those lessons.

### R12: figure and asset surface

Location: `docs/en.md:31,86-88,104; assets/refine-loop.svg; site/figures-agents2.js:140-177,440-450`.

Two bare fences may only gain the permitted reversible text tag during actual authoring. Preserve the self-refine figure payload. The static SVG is present but not embedded by the body and must remain byte-identical as a future support asset. The website widget uses a hard-coded geometric quality curve, not measurements or the SVG; GitHub GFM displays the figure fence as code rather than the live widget. Neither website nor mobile/PDF behavior has been tested.

### R13: prerequisite boundaries

Location: `phases/14-agent-engineering/01-the-agent-loop/docs/en.md and code/main.py/main.ts; phases/14-agent-engineering/03-reflexion-verbal-rl/docs/en.md and code/main.py`.

All direct prerequisite docs and main files were read. 14-01 metadata lists Python while both Python and TypeScript implementations exist. 14-03 describes TTL and an Evaluator.binary component while code has a length-capped FIFO list and binary_evaluator; its scripted Actor uses memory count, not reflection text. Keep the distinction between iterative revision of one output and fresh Reflexion attempts conditioned on memory; do not import unsupported implementation claims.

### R14: publication and runtime limits

Location: `rollout v1.3 and this preparation`.

Source/context/terminology readiness is not authoring, strict acceptance, independent language review, GFM inspection, remote readback, cumulative regression or publication. No course runtime/tests, installs, models/APIs, own3 installation, remote writes, CI changes, merge, deploy or count increase occurred. Historical approved support headers are not current lifecycle evidence.

## Targeted primary-source checks

The following read-only checks distinguish source assertions from validated facts; they do not amend the fixed English or introduce extra lesson prose. No full literature review or current cross-framework audit is claimed.

- [https://arxiv.org/abs/2303.17651](https://arxiv.org/abs/2303.17651): abstract and version metadata. Confirms one-model self-feedback/refinement, seven tasks, no additional training, and approximate absolute average improvement. Not local experimental evidence.
- [https://arxiv.org/html/2303.17651v2](https://arxiv.org/html/2303.17651v2): targeted history/ablation search only, not full-paper review. No claim that the exact strong history-collapse wording was fully verified.
- [https://arxiv.org/abs/2305.11738](https://arxiv.org/abs/2305.11738): abstract and version metadata. Confirms v4 date 2024-02-21 and tool-interactive evaluation plus revision.
- [https://arxiv.org/html/2305.11738v4](https://arxiv.org/html/2305.11738v4): targeted tool/ablation passages, not full-paper review. LLMs interact with tools; comparisons distinguish tool-free ablations and natural-language feedback. The local keyword detector is not a paper reproduction.
- [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents): evaluator-optimizer passage and page publication metadata. Describes separate generation and evaluation calls with iterative feedback. Does not by itself substantiate a universal 2026 default or the lesson prompt-difference attribution.
- [https://openai.github.io/openai-agents-python/guardrails/](https://openai.github.io/openai-agents-python/guardrails/): output guardrails and tripwires sections. Final-output validation raises an exception on a tripwire and stops agent execution; automatic refinement retries are not established by that behavior.

## Terminology calibration and next gates

Only immutable support terminology was used for lexical calibration. The coordinator common149 candidate has SHA-256 `fca197eed922125d52d3360ea93dee99b9993e992ab262c07c5573394b4c855b` and preserves the complete common146 array in exact order/identity before appending final accepted S140/S141/S142 pins. All 141 terminology files were byte-verified against their pins and searched for relevant rows. Full semantic reads covered core TERMINOLOGY.md, S132, S138, S140, S141 and S142. ADDENDUM preamble/first 42 lines were read for heading/first-use rules. This is not a claim of fresh full semantic review of every historical glossary; no historical lesson body, record or review was used. Inherited historical lifecycle prose in glossaries is not current status evidence.

The coordinator-provided baseline is formal157 at `a5510405156c888d8d6a657284f9fa1e8a03d27b`, index SHA-256 `374bf990d0288f740e9d8e371abbb140a9cf820ef3eb0b922b357f6d06910c88`; latest actually validated cumulative set is actual156 at `832e57d45c3f2947d8d86b9af1a7fcf4cc8afd1f`. This worker did not reverify those remote facts. The parent coordinates actual159 membership (S142 plus the next two accepted lessons). Source support readiness is not cumulative regression or a count increment.

Own3 publication, independent exact-byte readback and installation remain pending and are not performed here. The future author's own proposal/calibration, first-write/capture, target/record, original strict, independent full semantic review plus Chinese read-through, real GitHub GFM inspection, final changed-byte readback and batch regression remain separate truthful gates. No tests/models/APIs/installs, remote mutation, merge or deployment occurred. No generic checker exception or source-code fix is proposed.
