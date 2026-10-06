# S143-audio-language-models source-only scope candidate

Prepared 2026-10-06 UTC under rollout v1.3. This candidate adds 0 reviewed lessons. No Chinese lesson body, translation record or language review is created. The coordinator retains DEPENDENCIES.json, common149, author-tree construction and the sole remote writer. Own3 publication/readback/installation and every later authoring or acceptance gate remain pending.

## Fixed identity and future deliverable

- Stage: `S143-audio-language-models`; lesson: `06-10`.
- Canonical source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`.
- Source: `phases/06-speech-and-audio/10-audio-language-models/docs/en.md`.
- Future target: `i18n/zh/phases/06-speech-and-audio/10-audio-language-models/docs/zh.md`.
- Future protected asset: `i18n/zh/phases/06-speech-and-audio/10-audio-language-models/assets/alm-architecture.svg`, byte-identical to the source asset below.
- Future record namespace: `i18n/zh/.curated/lessons/06-10/`; future record/review hashes are null.
- Support files in scope: SCOPE.md and TERMINOLOGY.md candidates only. DEPENDENCIES.json is owned by the coordinator, not supplied here.
- Coordinator-supplied accepted baseline: formal157 commit `a5510405156c888d8d6a657284f9fa1e8a03d27b`, index SHA-256 `374bf990d0288f740e9d8e371abbb140a9cf820ef3eb0b922b357f6d06910c88`; latest executed cumulative set actual156 commit `832e57d45c3f2947d8d86b9af1a7fcf4cc8afd1f`. This support worker does not revalidate either. Pending actual159 contains accepted S142 plus the next two accepted courses; S143 becomes one of those only after its own acceptance. Preparation is not inclusion or a passing batch result.

## Complete lesson-package inventory

All five files were read statically in full; the placeholder is verified empty. No lesson tests or quiz exist at the fixed tree. No missing-file pass, runtime check or newly produced learning artifact is claimed.

| Fixed source path | Bytes | Git blob | SHA-256 |
|---|---:|---|---|
| `phases/06-speech-and-audio/10-audio-language-models/assets/alm-architecture.svg` | 4257 | `d9c6392cfc7c417c6d2323b6cab87150dcaf9221` | `ef7f3cc86c43b11eb4fa53b08b12439ee531da406b06320ddeb0ca37e54e7f39` |
| `phases/06-speech-and-audio/10-audio-language-models/code/main.py` | 3204 | `5421eb95eca980a554eaa6dc44928eee9677829c` | `b486ddc9c2331df4b295090514d9d94819942f0911c107abb3723092b4d4a8d6` |
| `phases/06-speech-and-audio/10-audio-language-models/docs/en.md` | 9463 | `420e367eb91741d07697081df476984e7f544891` | `a32837dad7c1099f98828124d16ed2bc97576711bfbaea7f503127db3f6d4c84` |
| `phases/06-speech-and-audio/10-audio-language-models/notebook/.gitkeep` | 0 | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `phases/06-speech-and-audio/10-audio-language-models/outputs/skill-alm-picker.md` | 2274 | `e4cffa3fad73736a47490d2adeedf124238e0446` | `3b07ad13dec12cfe0e17384f05a557aa7c77a85a96bb7e2e5a8e89207a5e4bd2` |

## Direct English prerequisite context

All six files below were read completely, including code, not merely headers or summaries. No prerequisite Chinese lesson body, record or review was used. English context suffices for preparation; prerequisite Chinese acceptance is not a drafting dependency.

| Fixed source path | Bytes | Git blob | SHA-256 |
|---|---:|---|---|
| `phases/06-speech-and-audio/04-speech-recognition-asr/docs/en.md` | 9550 | `ad8ffd95c66b2efcc41bd3a77ff93b1864a49e3f` | `8636c6f5f698e085af96b807aff2733d606e41728a174fe1b80e31508c02f721` |
| `phases/06-speech-and-audio/04-speech-recognition-asr/code/main.py` | 4937 | `b52efd53886462d3055bf110ef78130b033971c0` | `6e5bd81c7ded72910f676beef40e9631ac10645ad3c5ef4fbb5b618b9e7e20c0` |
| `phases/12-multimodal-ai/03-blip2-qformer-bridge/docs/en.md` | 11438 | `8dc13ac9ee1fb4e64f999e7d57947e55e7654be4` | `8849ac3172d4edecb50891b890d4a3080f6efd1a7af17ea6c79c86b410a63c28` |
| `phases/12-multimodal-ai/03-blip2-qformer-bridge/code/main.py` | 6012 | `c9b17e04468e51187fea887a88fb90f0608b8748` | `ac83d0eb4ddbed35c7bcfef3c3556e1a32ea83ac73c76411acbafdc709a80ae0` |
| `phases/07-transformers-deep-dive/10-audio-transformers-whisper/docs/en.md` | 9900 | `e1ce2144668b19f9d72d1f1f368bd241439e4abb` | `f996b553ee4abba0d68ac4368a41ffecdffc5c91639060ffe99fa83fd84d80eb` |
| `phases/07-transformers-deep-dive/10-audio-transformers-whisper/code/main.py` | 3657 | `e97b50c289e9bfebb9f5321bdf6b73786ede2f1a` | `5d096b5a4feb079dc5b3d8318f5ff01c96309919d70a60286c22b44dfbd108c6` |

The metadata label Vision-Language Models resolves by its explicit Phase 12 · 03 identity to BLIP-2/Q-Former. It supplies frozen-backbone, bridge, projection and token-budget context. 06-04 supplies ASR/transcription and decoding/evaluation distinctions. 07-10 supplies audio features, encoder-decoder and task-token context. Their temporal claims and implementation/prose discrepancies are not corrected or endorsed here. No transitive prerequisite closure or full repository semantic read is claimed.

## Governance and protected structure

Root AGENTS.md, CONTRIBUTING.md and docs/i18n.md were read from the fixed source. The rollout v1.3 overrides the older batching/production rules for curated translation and prohibits copying machine-translation caches. Contributor guidance says translate content rather than code; the curated core metadata/structure contract applies. Neither main, upstream, certification files, README, ROADMAP, generated site files nor the machine-translation branch are write targets. Commands printed in guidance and lesson material were not executed. Canonical docs/i18n.md includes multilingual illustration text; it was treated only as contributor guidance, not term memory or material for a Chinese lesson.

| Fixed guidance path | Bytes | Git blob | SHA-256 |
|---|---:|---|---|
| `AGENTS.md` | 13617 | `3be7cf810ba6879a068d6da4756a399eab129740` | `24a1cb3e111107b1a3d922f550776e7573396bc9d0b651b33b1e2cc1d7e1bcc2` |
| `CONTRIBUTING.md` | 4933 | `3a561b62567ad298277adcebfbd65853e3e7ccf0` | `fd1d4f0b904f6ec83b2ad1c0290fe537dcc4ebfd3f1bf1d88148dd383059c166` |
| `docs/i18n.md` | 14861 | `5eea45dea0c125705ed158db3f0c731b4ef68ace` | `5d0e89958e6c90c3f4f65d8f0369800d350b4a3ceaf51275e2c41f23c6f4aa56` |

- The source body has 191 lines, 18 headings, four tables (column counts 5, 6, 2, 3), three Python fences and one figure fence; no bare fence or Mermaid payload. These are static inventory counts, not the shared strict check.
- Preserve the figure payload `v4-alm-tokens` and the linked SVG. The fixed site registration is in `site/figures-visaudio4.js`; the relevant function was read statically. No browser, GFM, mobile, site or PDF acceptance has occurred.
- Preserve all code, formulas/inline code, identifiers, filenames, paths, URL targets, numerical tokens, signs, percentages, table dimensions, heading hierarchy and source block order. Translate eligible prose freshly after the writing gate.
- Retain citations, model/version/license strings and source-reported dates. No source correction, new protected-content exception or checker relaxation is bundled into terminology.

## Immutable terminology calibration

Common149 candidate SHA-256: `fca197eed922125d52d3360ea93dee99b9993e992ab262c07c5573394b4c855b`. The exact prior 146 identities/order remain unchanged. All 141 term payloads (138 inherited plus accepted S140/S141/S142) match pinned Git blobs, SHA-256 and byte counts. Full glossary reading and relevant-row reading are differentiated in the source-readiness manifest; this is not a false claim of complete semantic rereading of 141 files. The eight immutable control files are not run or reread in this support pass. No original33 fixture or old Chinese body/translation/review is consulted. Final accepted terminology pin identities for the three appendages come from the coordinator's common149, rather than historical support commit headers.

## Source-risk register

### R01: prerequisite label resolution

The fixed metadata calls 12-03 Vision-Language Models; the actual direct path is 03-blip2-qformer-bridge and its H1 is From CLIP to BLIP-2 — Q-Former as Modality Bridge. Read that complete English doc and main.py. Preserve the fixed metadata wording during translation rather than silently renaming the source.

### R02: time-sensitive model, benchmark and availability claims

2026 model maps, rankings, benchmark sizes, architecture/backbone assignments, named winners, live leaderboard references and open/closed parity are fixed-source assertions. Approximate marks, missing-value dashes, task categories, model versions and dates must remain unchanged. No current ranking, API availability or reproduced score is verified here.

### R03: license and deployment caveat

Apache-2.0 and NVIDIA non-commercial are source labels; code, weights, base-model restrictions, outputs and service terms are different licensing objects. This pass does not validate license scope or approve deployment. Call-center compliance examples and RAG are instructional, not legal/compliance certification.

### R04: blanket architecture/training template

Every 2026 LALM is an overbroad source assertion, not independently established universality. Distinguish frozen stage-1 encoder/LLM from trainable projector; source prose allows full/LoRA stage-2 fine-tuning, while SVG explicitly says LoRA on encoder + LLM. Optional speech decoder is not the ordinary text decoder.

### R05: multi-audio random-baseline rhetoric

Four-option random choice is 25%; preserve each literal source result including ~20%, ~22%, 21.2%, 26.5% and 22-26%. The source wording barely above random includes values below 25%; do not silently repair or strengthen it. Multi-audio comparisons differ from mixed speech/sound/music within one clip.

### R06: long-audio and silence generalizations

The >10-minute degradation, offline-batch prevalence, speaker-attribution failure and Whisper-encoder hallucination inheritance are source claims; no general threshold or causal proof is verified. Diarization identifies who spoke when and does not separate waveforms. VAD may remove silence relevant to the motivating joint-context example; record this task-dependent tension rather than resolve it in translation.

### R07: non-runnable framework sketches and resource cost

Framework examples include load_wav and call_model without definitions and version-dependent model/processor APIs. transformers and datasets are beyond the root educational dependency allowlist; the projector snippet imports torch.nn. Model download, ~47 GB data.zip, NV-Embed-v2 and LLM judging are not authorized or executed. No source-code/API repair is made.

### R08: official scorer boundary

The heading mentions MMAU / LongAudioBench, but the snippet loads MMAU-Pro only. Preserve the explicit warning: exact string-match MCQ sanity-check accuracy is not comparable to published MMAU-Pro; the stated official evaluator uses embedding similarity, LLM judging and regex, plus model_output and category fields. Do not add answer normalization, claim LongAudioBench scoring exists, or run the evaluator.

### R09: toy implementation scope

main.py creates Gaussian fake features, a single dense 1280-to-4096 projection with ReLU, takes only eight frames, substitutes range IDs for real audio embeddings, concatenates AUDIO entries before TEXT entries and returns a count-based canned answer. The doc snippet has two Linear layers and GELU. Neither the word interleave nor the toy permits claiming neural inference, training, semantic reasoning, audio generation or benchmark execution.

### R10: source artifact/contract gaps

The five-file fixed lesson has no quiz.json or code/tests and notebook/.gitkeep is empty. Record absence, not tests passed or tests failed. Preserve the figure block v4-alm-tokens, three Python fences and SVG byte-for-byte. The output skill is context, not a command to enforce new policies or a newly translated deliverable.

### R11: output skill thresholds and deployment advice

The source skill has different gates: reject multi-audio below 30% and refuse shipping without verified >40%; it also requires upstream diarization for >10-minute audio. Preserve the distinction rather than harmonize thresholds. Its bank-call audit example, API route, per-speaker sending and confidence logging do not authorize transmission of recordings, user data, API calls or deployment.

### R12: prerequisite source inconsistencies

06-04 simplified beam search lacks blank-intervene state and is not full prefix CTC; its implementation says so. 12-03 prose describes 256 patches/32 queries/512 outputs but code constants are 64/8/24; its ~100M and 188M counts, training claims, 50x statement and 1 FPS/60-frame exercise are not repaired. 07-10 prose large-layer counts conflict with its 32-layer table; mel-bin/version geometry, both-convolutions stride wording and stand-in framing energy are not verified Whisper computation. These are context caveats, not blockers on source-faithful S143 support.

### R13: GFM and website acceptance boundaries

Static SVG and registered browser figure use English labels and protected payloads. Reading the JavaScript registration does not prove a rendered animation, accessible figure, GitHub GFM page, mobile view, website, PDF or CI result. All such S143 acceptance gates remain pending.

### R14: parity and terminology strength

Source hook matches must not become identical benchmark results: the source table retains 52.2% versus 52.5%, while main.py says 0.3 points. Open weights must not be strengthened to open-source licensing. Voice-in/voice-out without text detour is a source characterization, not a verified claim about every named internal architecture.

## Execution and acceptance boundaries

This pass only reads fixed English/Git metadata and permitted immutable terminology, hashes local bytes, and writes the two local support candidates plus a source-readiness inventory. It does not install own3, create an author tree, translate lesson prose, write translation.json/review.json, publish Git objects, change refs/PRs, execute repository/course tests, call models/APIs, train/fine-tune, download audio/data/weights, install software, send recordings or modify shared control code.

Before any lesson authoring, own3 support must actually be published by the authorized remote writer, independently read back byte-for-byte, and installed with its immutable dependencies. The later author must supply their own complete source/context reading, terminology proposal/calibration, first-write chronology and target/record evidence. The candidate's short glossary is not a substitute. Independent complete technical/Chinese review, original strict plus necessary link/structure checks, necessary real GitHub GFM inspection, independent final remote-byte verification and minimal registration are later gates. New lesson registration must state the applicable batch is pending until actually run. Original 33/24/50 controls, exact existing S07/S19 exceptions, dual replay and asset/repository audit remain unchanged. CI zero checks means not run. Merge, deployment, upstream, mobile/site/PDF claims and new permissions remain outside scope.

Coordinator review can freeze these support candidates; this file does not represent that review, remote publication or source-fact endorsement. Source/runtime caveats are recorded separately and do not block unrelated lessons.
