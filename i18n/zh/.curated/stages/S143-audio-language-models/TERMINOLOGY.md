# S143-audio-language-models terminology support candidate

Fixed English: `1bafaa88bb4668356791150bec3a6d7df38387eb`. Source-only preauthor support, prepared 2026-10-06 UTC. Short lexical mappings below are candidates, not Chinese lesson prose. Own3 publication, independent exact-byte readback and installation remain pending. This is not the future author's proposal/calibration receipt, first write, review or completed lesson.

## Calibration basis

The 149-entry common dependency candidate preserves the exact identity and order of common146 and appends final accepted S140/S141/S142 terminology. Candidate JSON SHA-256: `fca197eed922125d52d3360ea93dee99b9993e992ab262c07c5573394b4c855b`. All 141 terminology payloads were verified against pinned SHA-256, Git blob and byte counts; the eight controls were not loaded or run by this support worker. Full semantic reading is claimed only for core TERMINOLOGY and S30/S75/S128/S131/S140/S141/S142, plus the indicated ADDENDUM rules/rows and relevant matched rows in other pinned glossaries. Historical candidate-status text in an immutable glossary is not a new publication or acceptance claim.

| English | Proposed short Chinese presentation | Calibration | Context boundary |
|---|---|---|---|
| audio-language model / LALM / ALM | 音频语言模型（LALM / ALM） | new lexical proposal | Keep both source abbreviations; joint speech/sound/music understanding differs from ASR-only transcription. |
| speech / environmental sound / music | 语音 / 环境声音 / 音乐 | contextual proposal; S30 audio vocabulary | Speech is linguistic audio; sound need not be speech; music is a separate benchmark axis. |
| ASR / transcription / transcript | 自动语音识别（ASR）/ 转写 / 转写文本 | inherited; S30/S128/S131/S137 | Recognition task, action and resulting text are distinct; transcription is not cross-language translation. |
| audio encoder / LLM decoder / speech decoder | 音频编码器 / 大语言模型解码器 / 语音解码器 | inherited context; core/S128/S131 | Audio-to-feature encoder, text-generating LLM and optional speech-producing decoder have different roles. |
| projector / projection head / adapter | 投影器 / 投影头 / 适配器 | inherited; ADDENDUM | The audio feature-to-LLM embedding bridge; not optical projection, a complete audio encoder or a guarantee of information preservation. |
| MLP / linear layer / embedding space | 多层感知机（MLP）/ 线性层 / 嵌入空间 | inherited; S08/core/S136 | Model dimensions and activation functions stay exact; the demo and doc projector architectures differ. |
| backbone / frozen backbone / freeze | 主干网络 / 冻结的主干网络 / 冻结 | inherited; ADDENDUM/S75 | Weights are held fixed in the stated training stage; this is not a universal claim about runtime state or all later stages. |
| audio token / text token / interleaved | 音频 token / 文本 token / 交错排列的 | core token rule with contextual proposal | Keep token and explain its local unit. Audio features need not be discrete codec tokens or text words; the toy concatenates modalities instead of genuinely alternating them. |
| fine-tuning / full fine-tuning / LoRA | 微调 / 全量微调 / LoRA（低秩适配） | inherited; core/S131 | Keep the stage, trainable components and optional/full distinction; do not invent a training run. |
| instruction-following / audio QA / semantic reasoning | 指令遵循 / 音频问答 / 语义推理 | contextual lexical proposal | Task behavior and benchmark categories, not a claim that the toy reasons or follows instructions. |
| audio captioning / captioning pairs | 音频描述生成 / 描述生成数据对 | contextual extension of S112 captioning | Audio-to-description task, distinct from verbatim ASR transcriptions or timed subtitles. |
| pretext task | 前置任务（pretext task） | inherited; S127 | Pretraining objective task, not a course prerequisite. Here the source identifies ASR pairs for projector training. |
| multi-audio / mixed / long-audio | 多音频 / 混合类别 / 长音频 | new contextual proposal | Multiple-clip comparisons, mixed content/category and duration are distinct; do not collapse them into multimodal. |
| long-audio retrieval / clip | 长音频检索 / 音频片段 | contextual extension of S112/S137 | Locating semantic content within longer audio; clip is a segment, not gradient clipping. |
| voice-in / voice-out / output modality | 语音输入 / 语音输出 / 输出模态 | new contextual proposal | Preserve text-only versus text + speech. Source speech-native wording does not prove an internal architecture. |
| diarization / speaker attribution / speaker turn | 说话人分离（diarization）/ 说话人归属 / 说话轮次 | inherited S75/S131 plus contextual lexical entries | Who spoke when; not waveform source separation, voice cloning or automatically reliable identity verification. |
| voice activity detection / VAD-gate | 语音活动检测（VAD）/ 用 VAD 把关 | inherited S75/S128/S131 with contextual phrasing | Detect speech presence before inference; preserve the source recommendation without claiming silence never carries task information. |
| hallucination / long-audio degradation | 幻觉 / 长音频性能退化 | inherited S131 plus contextual phrase | Unsupported generated content and changing task performance; no new universal causal explanation or threshold. |
| streaming reasoning / offline batch inference | 流式推理 / 离线批量推理 | inherited S128 streaming context; lexical extension | Audio processing mode, not only API response streaming. The source prevalence claim stays dated. |
| exact match / embedding similarity / LLM judge | 完全匹配 / 嵌入相似度 / 大语言模型评判器 | inherited S101/core with contextual lexical extension | S143 toy comparison is raw equality; do not import S101 answer normalization. Keep the three evaluator mechanisms separate. |
| benchmark subset / category / random chance | 基准测试子集 / 类别 / 随机猜测水平 | new contextual proposal | A subset is not the full suite. Random baseline depends on the stated four-option setting and is not verified statistical significance. |
| open weights / closed model / proprietary | 开放权重 / 闭源模型 / 专有 | inherited S110 with source-context extension | Open weights is not synonymous with open source or commercial permission. API access is not a license grant. |
| compliance audit / required disclosure / guardrails | 合规审查 / 必要披露 / 安全护栏 | S140/core with contextual lexical extension | Call-center review and safeguards; these mappings do not certify regulatory compliance or authorize recording transmission. |
| fine-grained / chord-level / key change | 细粒度 / 和弦层面 / 转调 | contextual proposal; S140 music vocabulary | Musical resolution and tonality; key change here is not an authentication-key replacement. |
| B-section / chaptering / benchmark cherry-picking | B 段 / 章节划分 / 挑选有利基准结果 | new contextual proposal | Musical form, podcast/meeting navigation and selective reporting are different concepts; retain source B and model identifiers. |

## First use and protected material

Core first-use rules govern: explain technical acronyms at first body occurrence where needed, retain source spelling and later agreed terminology. Keep LALM/ALM/LLM/MLP/ASR/QA/VAD/RAG/API/SOTA and every model, dataset, evaluator, paper title, author, year, URL, code identifier and path exact. LALM is the source label; do not invent a longer acronym expansion absent from the source. CLAP/AF-CLAP/Q-Former/Whisper/BEATs/WavLM/Qwen/Gemma/Llama/GPT-4o/Audio Flamingo/LongAudioBench/MMAU/MMAU-Pro remain names, not generic translated objects.

Metadata keys Type, Languages, Prerequisites and Time stay English; Learn and Python stay unchanged. Ordinary prerequisite labels and metadata ~45 minutes may be rendered with the agreed terms and ~45 分钟. Keep the source's 12-03 label rather than silently replacing it with the actual prerequisite H1. Headings follow the ADDENDUM: 要解决的问题、核心概念、动手实现、实际使用、交付成果、练习、关键术语、延伸阅读; Pitfalls follows S75 as 常见陷阱. Do not add absent Learning Objectives.

Protect all three Python fence payloads, the figure identifier v4-alm-tokens, SVG bytes, inline code, numerical values, approximation marks, signs, percentages, units and table structure. No untagged source fences require a new text tag. Keep 1800, 10k, 47 GB, 1280, 4096, 1-3, 2-layer, >10-minute thresholds and source model-version numerals exact; natural-language time/count units may be mapped equivalently without adding or replacing source numeric tokens. Missing-value em dashes in benchmark cells are missing values, not zeroes. Preserve percentage versus percentage-point meaning.

Source claims about 2026 winners, licenses, universal architectures, silence hallucinations, near-random scores, speech-native internals and deployment safety remain fixed-source caveats. Term calibration is not external factual verification, code repair, runtime acceptance or legal advice. The output skill's <30% and >40% gates must not be harmonized. No lesson commands, tests, model/API calls, installs, data downloads or remote writes were performed.
