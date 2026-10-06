# S157-streaming-speech-to-speech-moshi-hibiki source-only scope candidate

Fixed English `1bafaa88bb4668356791150bec3a6d7df38387eb`; [phases/06-speech-and-audio/15-streaming-speech-to-speech-moshi-hibiki/docs/en.md](https://github.com/Activer007/ai-engineering-from-scratch/blob/1bafaa88bb4668356791150bec3a6d7df38387eb/phases/06-speech-and-audio/15-streaming-speech-to-speech-moshi-hibiki/docs/en.md). Source Git blob `30b4c5c2fe0d9c35d5af044d0f9fd0f5270f42a4`, SHA-256 `e21cb5cde8e5c2f46a027328b5d1eee69ad8231661d78f8b6509803a6dde3802`.

Status: complete local source-only own3 candidate after explicit clean169. Common161 accepted-chain preparation is finalized locally; independent final common/own3 review, serial remote publication, independent full readback and installation remain pending. No author assignment or Chinese lesson prose.

## Coverage

Complete target package: 4files. Direct prerequisites: 06-13, 06-11, 07-05, full packages read (all source languages, outputs, quizzes, SVG XML and empty placeholders). DEPENDENCIES contains exact source identities and coverage. No transitive-DAG claim. All5411 fixed non-i18n baseline files retain bytes, Git modes and physical0664/0775;12baseline i18n excluded. No Chinese body/record/review/fixture import. Required i18n policy contained an unrelated historic Chinese sample; not used as translation memory.

Original scanner source join/assemble is lossless. Source self-comparison is not Chinese strict acceptance. Bare fence locations and payload identities are recorded; only unchanged bare-source→text-target label allowance may later apply. No source/code/formula/asset repair or extra checker exception.

## Source caveats

### S2S-CITATION

docs/en.md Further Reading. The Hibiki-Zero link arXiv:2602.12345 resolves to an unrelated axion-physics paper. The current relevant Hibiki-Zero paper is2602.11072. Keep the frozen URL and attribution unchanged in translation; correct neither silently.

Primary checks: [arxiv.org](https://arxiv.org/abs/2602.12345), [arxiv.org](https://arxiv.org/abs/2602.11072).

### S2S-LATENCY-AND-ARCHITECTURE

docs/en.md Concept; assets/moshi-hibiki.svg; code/main.py takeaways. Official Moshi confirms7B temporal backbone,12.5Hz Mimi,160ms theoretical and as-low-as200ms practical L4 latency. Its paper specifies6 depth layers; source says2. SVG says200ms theoretical while docs/code say160. Inference consumes user audio while generating model audio/text; the SVG predicts-all-three wording requires training/inference context. Timing figures are not measurements from this task.

Primary checks: [github.com](https://github.com/kyutai-labs/moshi), [arxiv.org](https://arxiv.org/html/2410.00037v2).

### S2S-LANGUAGE-LICENSE

docs/en.md Hibiki and performance table; outputs/skill-duplex-pipeline.md. Released Hibiki is FR→EN, not the source table’s FR↔EN. Hibiki-Zero repository/model card lists FR/ES/PT/DE→EN; its current paper evaluates five X-to-English tasks and adaptation with less than1000h. Release coverage and benchmark coverage differ. The Hibiki-Zero weight card is CC BY-NC-SA4.0, unlike source CC-BY4.0; Moshi/Hibiki original model weights and their code have distinct licenses. Source French-first Moshi and universal any-language commercial peer claims are not established by these checks.

Primary checks: [github.com](https://github.com/kyutai-labs/hibiki), [github.com](https://github.com/kyutai-labs/hibiki-zero), [huggingface.co](https://huggingface.co/kyutai/hibiki-zero-3b-pytorch-bf16), [arxiv.org](https://arxiv.org/abs/2602.11072).

### S2S-WEBSOCKET-PLACEHOLDERS

docs/en.md Build It Steps1–2. encode_audio_mimi/decode_audio_mimi are absent from the checked current client_utils.py; several mic/serialize/play helpers are undefined source pseudocode. Current server transports tagged Opus bytes and separate text events, and runs Mimi server-side. It does not expose the lesson’s raw-Mimi-token WebSocket contract. Preserve code exactly and record it as conceptual, unexecuted and version-sensitive.

Primary checks: [github.com](https://github.com/kyutai-labs/moshi/blob/main/moshi/moshi/client_utils.py), [github.com](https://github.com/kyutai-labs/moshi/blob/main/moshi/moshi/server.py).

### S2S-SCALING-ARITHMETIC

outputs/skill-duplex-pipeline.md Scale; docs broader stack. 10k DAU×10% concurrency is1000 simultaneous sessions. At4–6 sessions/GPU, this implies approximately167–250 GPUs, not1500. Output refuses more than4 concurrent sessions yet recommends4–6. Source64 sessions at3× on L40S is not attributed to a model; checked Hibiki-Zero card describes3× on H100 instead, so it cannot validate that source row.

Primary checks: [huggingface.co](https://huggingface.co/kyutai/hibiki-zero-3b-pytorch-bf16).

### S2S-SIMULATION-BOUNDARIES

code/main.py. The stdlib demo prebuilds25 synthetic80ms frames and processes them serially, with artificial2ms/3ms sleeps. No streaming I/O, neural codec, transformer, interruption detector, inter-codebook conditioning or spoken turn-taking is implemented. depth_transformer ignores text/content except stream lengths; output tokens are random integers. Its per-frame timer excludes network/audio-capture/playout and is not end-to-end conversational latency. The encoded print entity &lt; remains protected.

### S2S-PRODUCT-CLAIM-SCOPE

docs/en.md Sesame/Use It/Pitfalls; outputs skill. Sesame CSM is context-conditioned speech generation with a Llama backbone and Mimi decoder, distinct from native full-duplex dialogue. The checked released generator uses32 Mimi codebooks. Source200ms TTFA, best-on-market, enterprise/pipeline-only and sub250ms universal prohibitions are not hardware-independent guarantees. No current commercial model latency or universal language benchmark was established.

Primary checks: [github.com](https://github.com/SesameAILabs/csm), [github.com](https://github.com/SesameAILabs/csm/blob/main/generator.py).

### S2S-SOURCE-CONTRACT

target package and AGENTS.md. Four target files only: docs, main.py, SVG and output. No quiz, tests or notebook exist; no Learning Objectives section exists. Dependencies websockets/moshi are outside AGENTS allowlist. Exercises require model download/GPU/audio that must not run. Missing source surfaces are not translation omissions.

### S2S-PREREQUISITE-BOUNDARIES

06-13,06-11,07-05 complete fixed packages. 06-13 toy is scalar RVQ and does not validate its codec-quality/rate claims; its output86Hz×8×10 calculation is not5504.06-11 metadata omits actual Rust, names a nonexistent shipped output path and its Python/Rust demos cannot prove voice-pipeline deadlines.07-05 metadata omits Julia; Python emits hidden states rather than promised vocab logits and lacks embeddings/position/final head. Its block-count arithmetic and unconditional stability claims are source caveats.06-12 pipeline is a body-context reference, not an explicit prerequisite; S149 held source is unchanged.

## Publication and future-author gates

Retain fixed English, protected code/math/numbers/metadata/paths/API/model names/URLs/Mermaid/figure/SVG unchanged. Independent complete bilingual review and separate Chinese read, original strict, read-only CJK-bold diagnostic plus manual context adjudication, and manual raw-angle Markdown review are mandatory before body publication. Actual fixed-target GitHub GFM must cover every table, formula, code fence, long line and figure; local source PNG is not targetGFM/site/mobile/PDF. Prior exact-source SVG browser evidence can be reused only at identical hashes.

Common161 now binds accepted S153/S154/S156 support→content→final TASKS→formal169 independent chains and the explicit coordinator clean169 checkpoint. Every old158 pin object, metadata field and ordering remains unchanged. Common161 consists of153 TERM files and8 unchanged controls; own3 gives164 future supports. Independent final common/own3 review, sole-writer serialized fork-only publication, full independent readback and164-support installation proof must precede any fresh author. Future author provides own proposal/calibration and truthful first-write chronology. No remote writes or course code/import/tests/models/GPU/API/audio/video/download/install/training here.

Clean169 is verified at index commit3c2f11e6c6ae1e3b75192e774c29e36fb7ec1f56, with formal169 and actually executed cumulative168. Actual168 covers S151/S153/S154, not S156. S156 final evidence head00182576b6544dcc0f86a784a357fa404065dd6c begins future actual171; the next two individually accepted lessons fill that cohort in acceptance order, and the remaining next lane begins future174. No future regression is claimed. Seven historic pending rows and unregistered S149/S155/S158/S160 holds are unchanged. Stage reservations follow the established audio/agent/vision frontier, not a global DAG.

## Final local support identities

Common161 SHA-256 `9e3da64b335de21fb20e4d56a7cb2036797fb79d9d4449991b50e8d3b9c1faeb`. Clean169 checkpoint SHA-256 `09db563c2bcf8c6bc2ce48aed61592af85b686fac962876128719b26ae43c317`. Exact source/TERM/readback chains are bound in DEPENDENCIES.json. Prior R01/R02 candidates and failed helper drafts remain preserved. The immutable public own3 snapshot keeps publication/readback/install/author fields null until those events occur in separate receipts.
