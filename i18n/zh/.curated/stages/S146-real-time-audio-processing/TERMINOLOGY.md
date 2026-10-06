# S146 Real-Time Audio Processing terminology support candidate

Fixed English: `1bafaa88bb4668356791150bec3a6d7df38387eb`, lesson `06-11`. Local source-only support. These are short lexical choices, not Chinese lesson prose, an author's proposal/calibration receipt, a first write or an independent lesson review. Parent owns DEPENDENCIES.json. Own3 publication, independent byte readback and installation are pending.

## Calibration basis

Common152 has SHA-256 `adb98cb4c54c97f8485605d3d90e10fbe80209705ffcae1545170c1c10c39beb`: 144 terminology files plus eight immutable controls, retaining the exact common149 prefix and appending accepted S143/S144/S145 terminology. All 144 terminology file SHA-256/Git-blob/byte identities were checked through the receipt's local payload locations.

Full semantic reads covered core TERMINOLOGY.md, the complete TERMINOLOGY-ADDENDUM.md, S17/S30/S75/S121/S128/S131/S134/S137/S138 and new S143/S144/S145. The other 130 glossary files were only searched for ring/jitter buffers, barge-in, full duplex, echo cancellation, SPSC, hot path, thread contention, silence hang-over and TTFA. No full semantic reread of all common support is claimed. Frozen glossary headers can describe older lifecycle states; they are not current publication evidence. No prior Chinese lesson body, translation record, review or original33 fixture was used.

## Source-grounded lexical choices

| English | Proposed Chinese presentation | Inheritance and semantic boundary |
|---|---|---|
| real-time audio processing | 实时音频处理 | New scoped compound using S30 audio vocabulary; real-time refers to meeting a time budget, not merely running quickly once. |
| pipeline / batch pipeline / cascaded pipeline | 管线 / 批处理管线 / 级联管线 | 管线 follows S75/S128; distinguish separate connected stages from a native end-to-end speech model. |
| streaming / streaming ASR / streaming TTS | 流式处理 / 流式自动语音识别 / 流式文本转语音 | S128/S131/S143 context; not mechanically 流式输出 when the text refers to audio arriving or internal processing. |
| ASR / STT / TTS | 自动语音识别（ASR）/ 语音转文本（STT）/ 文本转语音（TTS） | ASR/TTS follow S30/S128/S134. Keep distinct source labels; ASR and STT describe the recognition task without asserting identical APIs. |
| VAD / VAD gate / silence gate | 语音活动检测（VAD）/ VAD 门控 / 静音门控 | S75/S128/S131/S143. A speech-presence decision gates later work; an energy threshold is not a semantic speech classifier. |
| frame / chunk / window | 帧 / 音频块 / 窗 | Frame/window follow ADDENDUM/S30; audio chunk is not RAG text chunking. Do not make frame length, hop and model lookahead synonymous. |
| sample / sample rate / sample-rate conversion | 采样点（或采样值）/ 采样率 / 采样率转换 | S30; use point for counts and value for amplitudes. Preserve 320 samples at 16 kHz versus 20 ms. |
| resampling / aliasing / low-pass filter | 重采样 / 混叠 / 低通滤波器 | S30. Not distribution resampling or display aliasing. Do not turn a zero-latency source claim into a validated guarantee. |
| ring buffer / circular buffer / circular queue | 环形缓冲区 / 环形缓冲区 / 循环队列 | New scoped mapping; preserves the source distinction between storage layout and FIFO access policy. No automatic zero-allocation/lock-free guarantee. |
| capacity / buffer level / buffering latency | 容量 / 缓冲区占用量 / 缓冲延迟 | New scoped entries. Capacity is the limit; level is current occupancy; neither is an end-to-end measured latency. |
| FIFO / SPSC / lock-free | 先进先出（FIFO）/ 单生产者单消费者（SPSC）/ 无锁 | FIFO follows S138. Explain SPSC at first body use; a Python deque snippet is not evidence of a full lock-free real-time design. |
| producer thread / consumer thread | 生产者线程 / 消费者线程 | New concurrency context. Do not confuse producer with content creator or consumer with end user. |
| jitter / jitter buffer / out-of-order packets | 抖动 / 抖动缓冲区 / 乱序数据包 | Network arrival-time variation and queue smoothing; not random augmentation jitter, acoustic noise or a proven zero-delay mechanism. |
| hot path / thread contention | 关键处理路径（hot path）/ 线程争用 | Audio-path extension of S138 关键响应路径. Refers to timing-sensitive frequently executed work, not a filesystem path. |
| GIL / audio callback / C callback | GIL（全局解释器锁）/ 音频回调 / C 回调 | GIL follows ADDENDUM. Callback names do not demonstrate thread-safety or scheduling priority. |
| pinning threads / thread priority | 线程绑核 / 线程优先级 | Distinct mechanisms: source heading and explanation conflate them. Preserve that distinction without silently repairing the recommendation. |
| latency budget / latency floor / end-to-end latency | 延迟预算 / 延迟下限 / 端到端延迟 | Core 延迟. Do not substitute throughput or completed-response time for first-output timing. |
| first-token latency / first chunk / TTFA | 首 token 延迟 / 首个音频块 / 首段音频延迟（TTFA） | Core first-token rule; TTFA appears in implementation/output context. Keep the measured endpoint and source acronym exact. |
| P50 / P95 / P99 / percentile | P50 / P95 / P99 / 百分位数 | S17/S121. Explain where needed; preserve source casing, and do not equate P95 with a mean or a guaranteed maximum. |
| throughput / real-time factor / headroom | 吞吐量 / 实时因子 / 性能余量 | Core throughput plus scoped DSP context. Rust defines wall/budget and budget/p99 separately; do not invert their meanings. |
| partial transcript / partial results / lookahead | 部分转写文本 / 部分结果 / 前瞻 | S128/S131/S143. Partial text may still change; lookahead uses future audio and is not a completed transcript or model training lookahead. |
| utterance / final user utterance / turn-taking | 话语 / 用户最终话语 / 话轮交替 | 话语 follows S75. Preserve endpoint/finality context; final is not a last-ever conversation turn. |
| interruption / barge-in / interruptible generation | 打断 / 插话打断（barge-in）/ 可打断的生成 | New scoped mapping. User speaks during assistant speech; distinguish detection, generation cancellation and playback cancellation. |
| cancel / discard remaining output / playback | 取消 / 丢弃剩余输出 / 播放 | New scoped actions; task cancellation alone does not prove provider work or queued audio was stopped. Code cancel() stays English. |
| full duplex | 全双工（full duplex） | Simultaneous communication in both directions; do not replace with alternate-turn conversation or assume every cascade supports it. |
| transport / WebRTC Opus transport / bitrate | 传输层 / WebRTC Opus 传输 / 比特率 | Protocol and codec names remain literal. Preserve 48 kHz, 8–128 kbps and 20 ms rather than claiming these are their only valid settings. |
| echo cancellation / AEC / feedback path | 回声消除 / 声学回声消除（AEC）/ 声学反馈路径 | Speaker-to-microphone signal path; not model feedback or answer self-refinement from S144. AEC3 remains a name. |
| TTS priming / warm-up / dummy run | TTS 预热 / 运行时预热 / 试运行 | Runtime sense follows S121. Not learning-rate warm-up, training or a run carried out by this preparation. |
| passthrough loop / glass-to-glass latency | 直通环路 / 端到端实测延迟（glass-to-glass latency） | Audio echo-test context; retain the source phrase at first occurrence, rather than inventing a video-only definition or a measured result. |
| RMS / dBFS / gain / FIR | 均方根（RMS）/ 满刻度分贝（dBFS）/ 增益 / 有限冲激响应（FIR） | Static implementation context only. Amplitude, squared energy and speech probability use different scales. Source code names/formulae stay exact. |
| vocoder artifacts / glitches / pops | 声码器伪影 / 音频故障 / 爆音 | 声码器 follows S30/S134. Artifacts here are unwanted signal effects, not reusable deliverables. |
| silence hang-over / min speech duration | 静音延续等待时长 / 最短语音时长 | Output-skill context. Distinguish waiting after speech from how much speech is needed before accepting an utterance. |
| observability / false-positive interruption / drop-call rate | 可观测性 / 误触发打断 / 掉话率 | Observability follows S144; output metrics remain separate from WER and latency. |
| voice cloning / PII / guardrails | 声音克隆 / 个人身份信息（PII）/ 安全护栏 | S134/S137, ADDENDUM and core. A lexical choice is not consent, effective redaction or a compliance certification. |
| LLM / token / model / API / prompt injection | 大语言模型（LLM）/ token（词元）/ 模型 / API（应用程序编程接口）/ 提示词注入 | Core. Keep source API/product identifiers and explain acronyms at first eligible body occurrence. |

## First use, protected surfaces and source boundaries

Follow core first-use explanations and contextual choices rather than global substitution. Metadata keys Type, Languages, Prerequisites and Time remain English; Build and Python remain unchanged even though Rust exists in the package. ~75 minutes may be rendered ~75 分钟. Natural-language time/count units may be translated equivalently without changing source numeric tokens; ms, s, Hz, kHz, kbps, percentages, inequalities, approximate marks and model-version numerals stay exact.

Common headings follow ADDENDUM: 要解决的问题、核心概念、动手实现、实际使用、交付成果、练习、关键术语、延伸阅读. Pitfalls follows S75 as 常见陷阱; Common gotchas can use 常见注意事项 to preserve the two separate source sections. Preserve Step numbering and section order. The source has no Learning Objectives section; do not invent one.

Keep all five Python fence payloads, figure marker nyquist-aliasing, embedded ../assets/real-time.svg path, SVG bytes, inline-code spans, API names and URLs unchanged. There are no bare source fences requiring text tags. Preserve RingBuffer, Dialog, asyncio, audio_stream, transcribe_streaming, llm_then_tts, speaker.write, peerconnection.stop(), torch.hub.load, soxr_hq and protected output paths even where source correctness caveats apply.

Keep all actual source proper names, including Moshi, Kyutai, GPT-4o-realtime, Silero VAD 4.0, webrtcvad, Parakeet-CTC-0.6B, NeMo, Whisper-Streaming, Macháček, WebRTC, Opus, LiveKit, Daily.co, Pion, sounddevice, PortAudio, PolyPhase, Kokoro, AEC3, Groq, Cerebras, vLLM-streaming, ElevenLabs Turbo v2.5, OpenAI Realtime API and aiortc. Output/code-only names remain contextual inputs and are not newly added lesson prose.

SCOPE.md records fixed-source mismatches: timing boundaries, demo/package gaps, placeholder APIs, cancellation/track confusion, model-frame assumptions, zero-latency resampling, output filename and unvalidated vendor/privacy assertions. Preserve source meaning rather than silently correcting these through translation. Common152+own3 is eventual support total 155, not a reviewed-course count. No authoring, runtime, model/API call, installation, GFM acceptance, remote publication or regression result is asserted here.
