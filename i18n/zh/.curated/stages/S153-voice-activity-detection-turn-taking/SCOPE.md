# S153-voice-activity-detection-turn-taking source-only scope candidate

Fixed English `1bafaa88bb4668356791150bec3a6d7df38387eb`; source [phases/06-speech-and-audio/14-voice-activity-detection-turn-taking/docs/en.md](https://github.com/Activer007/ai-engineering-from-scratch/blob/1bafaa88bb4668356791150bec3a6d7df38387eb/phases/06-speech-and-audio/14-voice-activity-detection-turn-taking/docs/en.md). Git blob `121a1c1ecdc69b4f312407cf4b89f647e6017c22`, SHA-256 `ba520338d01743a41fd7f4343a64af318241ce7e72e752afe8a98773e5f876fb`.

Status: COMPLETE LOCAL OWN3 CANDIDATE, pending independent review, serial remote support publication/readback and installation. Common158 = 150 terminology files + 8 immutable controls; own3 gives161 prospective supports. No author assignment, Chinese lesson prose, course execution or formal/pending count increment.

## English-first coverage

Complete target package: 5 files. Direct prerequisites: 06-11, 06-12, with 5 English docs/main files fully read. Detailed fixed pins and semantic line ranges are in DEPENDENCIES.json. Only direct prerequisite closure is claimed; preceding Chinese acceptance is not an author gate.

Fresh author tree has exactly5411 fixed non-i18n files from the Git archive, with all bytes, Git blobs, Git modes and POSIX modes verified. All12 baseline i18n files excluded. No supports, Chinese bodies, records, reviews or original33 fixtures installed. Common lexical identity verification does not claim semantic rereading of all158 supports.

Source scanner join and identity assembly are lossless. English self-comparison is not Chinese strict acceptance. Bare-fence eligibility: none. The only eligible later label normalization is the unchanged original bare-to-text rule; record it before first capture and protect payload bytes.

Preserve every code/math/number/metadata/API/model/identifier/path/URL/Mermaid/figure/SVG surface. Source caveats remain outside Chinese prose; do not modernize or silently repair them.

## Source caveats

### VAD-DECISION-LEVELS

docs/en.md:12-18,30-37,160-168; code/main.py:28-63. Per-frame speech presence, utterance onset, and semantic completion are distinct. The implementation provides two heuristic speech inputs and a silence timer; it has no text/intonation/semantic end-of-turn model. Do not convert a silence timer into semantic understanding or treat a cough frame error as a turn-start error.

### VAD-FAKE-SILERO

code/main.py:14-36,93-112,128-129. fake_silero_vad ignores prev_state and threshold. For a transient with RMS > 0.05 it still returns 0.55, above the caller’s >= 0.5 speech cutoff. The transient condition only blocks the 0.92 branch. Both synthetic speech and cough can therefore remain active; printed statements that this rejects cough or demonstrates Silero superiority are not supported by the algorithm. No deterministic event trace or model quality measurement was run.

### VAD-STATE-ACCUMULATION

docs/en.md:92-113; code/main.py:39-63,70-78. While idle, speech_ms is not cleared when silence follows a short positive burst. Multiple disjoint bursts can accumulate to min_speech_ms and a cough can contribute to a later onset. With 20 ms updates, 250 ms is first reached at 260 ms. Once speaking, the default 500 ms end threshold needs 25 silent frames. No end-of-stream finalization exists if the stream stops before silence completes.

### VAD-DEMO-NOT-CASCADE

code/main.py:88-103; docs/en.md:24-30,154. The two VAD heuristics are evaluated in parallel on every frame and feed separate timers, not an energy-prefilter → Silero → semantic-detector cascade. The one 20 ms cough is shorter than the shared 250 ms onset threshold, so a frame-level false activation need not cause any extra START in either lane. Printed many-false-positives captions cannot prove a turn-event improvement.

### VAD-PRE-ROLL-NOT-IMPLEMENTED

code/main.py:40-46; docs/en.md:37,73-86,145; assets/vad-turn-taking.svg:48. pre_roll_ms is stored and never used; no audio buffer is maintained by TurnDetector. get_speech_timestamps speech_pad_ms expands offline segment boundaries rather than implementing a real-time pre-trigger rolling buffer. Do not imply the runnable package prevents first-word clipping.

### VAD-DOC-MAIN-DIVERGENCE

docs/en.md:100-113; code/main.py:48-63. The doc skeleton increments silence_ms even in idle and leaves it nonzero on END; main increments it only while speaking and clears it on END. Both preserve pending speech across idle gaps. These are distinct source implementations; do not silently unify them.

### VAD-FRAME-CONTRACT

docs/en.md:12,28,74-86; site/figures-speech2.js:167; ../11-real-time-audio-processing/docs/en.md:30,84-88. 20 ms transport frames contain 320 samples at 16 kHz, but current checked Silero processing windows are 512 samples (32 ms). Whole-waveform get_speech_timestamps handles its own windows; direct per-frame model invocation needs compatible buffering/version handling. Source prose combines transport cadence, inference compute time and model window size.

### VAD-DEFAULTS-VS-OVERRIDES

docs/en.md:32-37,78-84; outputs/skill-vad-tuner.md:13,24. The heading says defaults, but 500 ms silence and 300 ms padding are explicit lesson settings, whereas current raw Silero utility defaults are 100 ms and 30 ms. Output ranges 200–300/400–800/250–500 and doc ranges 250/500–800/300–500 are workload suggestions, not one identical API default.

### VAD-LATENCY-BOUNDARY

docs/en.md:39-43,166; assets/vad-turn-taking.svg:52-56; code/main.py:131. 500/4 = 125 ms describes residual buffered-STT processing after end detection in the Kyutai example. It excludes hangover, network, LLM and TTS. A 500 ms timer followed sequentially by 125 ms flush is already about 625 ms before those other stages. The source calls this sub-200 ms end-to-end and equates transcript timing with VAD timing; these are unsupported boundary collapses.

### VAD-FLUSH-PSEUDOCODE

docs/en.md:118-125; outputs/skill-vad-tuner.md:15,26. send_audio/send_flush/recv_transcript are generic stt_client placeholders, not a tested shared vendor API. timeout_ms=150 is not a latency guarantee. Resending an already delivered buffer could duplicate audio depending on client contract. Source’s all-Whisper-streaming rejection is broader than the examined implementations; no universal wrapper claim was verified.

### VAD-BENCHMARK-CONTEXT

docs/en.md:28,45-54,168; code/main.py:115-124; assets/vad-turn-taking.svg:31-34,42. The 50.0/87.7/98.9 figures match a vendor benchmark under specific corpus/noise settings. Version, threshold protocol and hardware are absent from the lesson table. The latency column mixes 30 ms frame/window duration with ~1 ms compute time. No source corroboration was established for pyannote 95% @ 5% FPR or ~10 ms, the exact Silero 1M parameter count, or the SVG 5–10% false-interrupt reduction.

### VAD-IVR-CONSTRAINT-CONFLICT

outputs/skill-vad-tuner.md:20-27. Example asks for < 500 ms turn detection but selects 600 ms silence hangover. Its 400→150 ms claimed turn-end saving is not reconciled with that timer. Threshold 0.4 is justified by high noise floor without calibration; lowering a speech-probability threshold normally trades fewer misses for more false positives. Preserve example rather than making it appear to satisfy its own latency requirement.

### VAD-FAIL-OPEN-GUARD

outputs/skill-vad-tuner.md:16,27. Treating everything as speech when VAD fails can prevent end detection, grow buffering, increase downstream work and transmit/retain more audio. It cannot restore an unreachable STT service. Cobra is described by its owner as on-device, so generic VAD-service outage language is deployment-dependent. Fail-open is a source tradeoff, not a proven privacy/compliance guard.

### VAD-SOURCE-RECOMMENDATIONS

docs/en.md:18,54,127-146; outputs/skill-vad-tuner.md:12,18,23. Open-source default, compliance upgrade, accuracy leader, never energy-only and refuse Whisper are categorical source recommendations, not universally demonstrated engineering rules. Threshold/timeout choice depends on task, noise, language and user behavior. Do not silently strengthen, soften or endorse them.

### VAD-NUMERICS-AND-INPUTS

docs/en.md:64-68,74-77; code/main.py:14-36,93-103. RMS-to-dBFS assumes normalized amplitudes referenced to full scale 1.0. Empty chunks divide by zero and fake_silero also calls max/min. Gaussian toy samples are not clipped to physical PCM range. Main logs i*20 after processing a frame, so timestamps are frame-start labels rather than frame-end decision time; they are not measured latency. docs uses > 0.5 prose while caller uses >= 0.5.

### VAD-LESSON-CONTRACT

AGENTS.md:58-122,207-214; docs/en.md:1-177; code/main.py:1-8; notebook/.gitkeep. No Learning Objectives, quiz.json, tests or runnable notebook exist in the five-file package; main header does not cite the docs path/spec and exceeds the nominal 4–6-line header. The example prints output instead of asserting tests. These are fixed-source repository-contract deviations, not generated omissions.

### VAD-DEPENDENCY-ALLOWLIST

AGENTS.md:66-78; docs/en.md:74,155-156. Real-model snippets/exercises reference silero-vad and sentence-transformers outside AGENTS dependency allowlist. The energy snippet lacks an import math in its standalone fence and Silero snippet assumes torch/waveform_16k. No installation, import or model download was performed.

### PREREQ-11-SCOPE

phases/06-speech-and-audio/11-real-time-audio-processing/docs/en.md:6,22,51-53,84-99,122,152,173; phases/06-speech-and-audio/11-real-time-audio-processing/code/main.py:50-89; phases/06-speech-and-audio/11-real-time-audio-processing/code/main.rs:21-24,149-154. Metadata lists Python despite main.rs. Budget rows sum to 400 ms but are not measurements; Python simulates 1.9 s rather than the exercise’s fake 10-second stream and has no ring buffer, live streaming or cancellation. Rust is only gain/FIR DSP; its nine taps sum to 1.0, but fast DSP cannot prove VAD/STT/LLM/TTS fit a 20 ms slot. The figure ID nyquist-aliasing is not a voice-pipeline mechanism. Raw Silero 20 ms calls and transcribe_streaming are version-sensitive. The Silero Apache 2.0 reading label conflicts with current owner MIT statement. No prerequisite repairs or performance acceptance.

### PREREQ-12-CAPTURE

phases/06-speech-and-audio/12-voice-assistant-pipeline/docs/en.md:77-92; phases/06-speech-and-audio/12-voice-assistant-pipeline/code/main.py:78-93. pre is appended before the first trigger; copying that buffer then appending the current chunk again duplicates the first positive frame. The doc returns b"".join on chunks originating as NumPy arrays unless encoded separately; the expected sample-byte format is not made explicit. The main simulation extends float lists and uses 400 ms trailing silence, whereas overview says 500 ms. No full Silero integration or minimum 250 ms speech gate exists.

### PREREQ-12-SIMULATOR

phases/06-speech-and-audio/12-voice-assistant-pipeline/docs/en.md:22,95-132,136,146; phases/06-speech-and-audio/12-voice-assistant-pipeline/code/main.py:37-66,98-137. The model and tool functions are sleeps/stubs; no mic hardware, concurrent streaming, cancellation, replay suppression, meaningful tool-result reinsertion or real timer scheduling is implemented. t_llm is captured before tool dispatch, so the LLM + tool total omits tool time. Speech capture runs faster than real time; model timings are artificial. The 30-day retention sentence and no-injection-success target are source claims, not a universal compliance or security guarantee. Known 06-12 SVG hold is not inspected or resolved in this lane.

## English prerequisite with separate hold

06-12 fixed English docs/main are available and read. S149 remains an unregistered source-SVG visual hold; no repair, Chinese acceptance, new index row or prerequisite-SVG pass is claimed. It does not block this English-first author preparation.

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
