# S153-voice-activity-detection-turn-taking terminology candidate

Fixed English `1bafaa88bb4668356791150bec3a6d7df38387eb`, lesson06-14. Short lexical proposals only, not Chinese lesson prose or future-author calibration. Common158 SHA-256 `a4ed394c03650b70a6e48172186d37c5bc255dc887753c058be7a73bc5a78875` is finalized locally from independently accepted support/content/repair/final-TASKS/formal166 chains. Own3 publication/readback/installation and independent review remain pending.

Core and ADDENDUM first-body-use rules apply: explain relevant English/acronyms with Chinese context, retaining protected product/API/identifier names. token first use follows token（词元）. Common headings follow ADDENDUM only where present; metadata keys and language/type values stay unchanged. Natural-language time/count units may be translated equivalently, with exact numeric quantities preserved. No lexical choice silently repairs source facts.

| English | Proposed Chinese presentation | Context and boundary |
|---|---|---|
| voice activity detection | 语音活动检测 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| VAD | 语音活动检测（VAD） | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| turn-taking | 话轮交替 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| turn detection | 话轮检测 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| turn detector | 话轮检测器 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| turn-end | 话轮结束 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| end-pointing | 端点检测 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| semantic endpointing | 语义端点检测 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| semantic endpoint | 语义端点 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| onset detection | 起始检测 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| utterance | 话语 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| voice agent | 语音智能体 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| voice assistant | 语音助手 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| three-tier VAD cascade | 三级 VAD 级联 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| energy gate | 能量门控 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| energy threshold | 能量阈值 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| energy-only VAD | 仅基于能量的 VAD | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| frame | 帧 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| chunk | 音频块 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| waveform | 波形 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| sample | 采样点 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| sampling rate | 采样率 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| RMS | 均方根（RMS） | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| dBFS | 满刻度分贝（dBFS） | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| threshold | 阈值 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| probability | 概率 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| minimum speech duration | 最短语音时长 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| silence hangover | 静音延续等待时长 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| pre-roll | 预留音频 | Audio retained before speech onset, distinct from offline output segment padding. |
| pre-roll buffer | 预留音频缓冲区 | Audio retained before speech onset, distinct from offline output segment padding. |
| pre-speech buffer | 语音前缓冲区 | Audio retained before speech onset, distinct from offline output segment padding. |
| rolling buffer | 滚动缓冲区 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| look-ahead delay | 前瞻延迟 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| flush trick | 强制输出技巧（flush trick） | Drain already-buffered STT after end detection; not file-system flush or end-to-end125ms guarantee. |
| flush signal | 强制输出信号 | Drain already-buffered STT after end detection; not file-system flush or end-to-end125ms guarantee. |
| streaming STT | 流式语音转文本 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| STT | 语音转文本（STT） | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| transcript | 转写文本 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| state machine | 状态机 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| real time | 实时 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| end-to-end latency | 端到端延迟 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| first-word clip | 首词截断 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| false positive | 假阳性 | Statistical positive means classifying nonspeech as speech; distinguish false frame decisions from false whole-turn events. |
| false trigger | 误触发 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| true positive rate | 真阳性率 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| false positive rate | 假阳性率 | Statistical positive means classifying nonspeech as speech; distinguish false frame decisions from false whole-turn events. |
| TPR | 真阳性率（TPR） | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| FPR | 假阳性率（FPR） | Statistical positive means classifying nonspeech as speech; distinguish false frame decisions from false whole-turn events. |
| ROC point | ROC 曲线上的工作点 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| precision | 精确率 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| recall | 召回率 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| F1 | F1 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| transient | 瞬态信号 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| noise floor | 噪声底 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| crowd babble | 人群嘈杂声 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| intonation | 语调 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| linguistic context | 语言上下文 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| classifier | 分类器 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| diarization | 说话人分离 | S75/S131/S143: who spoke when, not separating mixed source waveforms. |
| on-device | 设备端 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| call center | 呼叫中心 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| IVR | 交互式语音应答（IVR） | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| fail-open | 失败时放行 | Source deployment tradeoff, not a privacy/compliance guarantee; do not confuse with fail closed. |
| audit log | 审计日志 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| fallback | 回退方案 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| workload | 工作负载 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| MLP | 多层感知机（MLP） | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| embedding | 嵌入 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| hand-labeled | 人工标注 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| silence | 静音 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| speech | 语音 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| inference latency | 推理延迟 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |
| buffering latency | 缓冲延迟 | Source-context lexical candidate; apply core first-use, preserve protected identifiers and source caveats. |

## Calibration coverage

All158 common payload identities verified; only the following lexical files/ranges were semantically read for this lane. Older frozen headers describe historical lifecycle states and cannot override accepted identity chains.

- i18n/zh/.curated/TERMINOLOGY-ADDENDUM.md: {"mode": "relevant excerpts after lexical search", "line_ranges": [[4, 6], [22, 29], [46, 56], [70, 72], [87, 89], [93, 104]]}.
- i18n/zh/.curated/TERMINOLOGY.md: {"mode": "full", "line_ranges": [[1, 82]], "empty_file_verified": false}.
- i18n/zh/.curated/stages/S30-audio-fundamentals/TERMINOLOGY.md: {"mode": "full terminology only", "line_ranges": [[1, 23]]}.
- i18n/zh/.curated/stages/S128-speech-recognition-asr/TERMINOLOGY.md: {"mode": "full terminology only", "line_ranges": [[1, 28]]}.
- i18n/zh/.curated/stages/S146-real-time-audio-processing/TERMINOLOGY.md: {"mode": "full terminology only", "line_ranges": [[1, 61]]}.
- i18n/zh/.curated/stages/S152-neural-audio-codecs/TERMINOLOGY.md: {"mode": "full", "line_ranges": [[1, 32]], "reader": "candidate coordinator"}.
- i18n/zh/.curated/stages/S75-speaker-recognition-verification/TERMINOLOGY.md: {"mode": "excerpt", "line_ranges": [[12, 12]], "reader": "candidate coordinator"}.
- i18n/zh/.curated/stages/S131-whisper-architecture-finetuning/TERMINOLOGY.md: {"mode": "excerpt", "line_ranges": [[17, 17]], "reader": "candidate coordinator"}.
- i18n/zh/.curated/stages/S143-audio-language-models/TERMINOLOGY.md: {"mode": "excerpt", "line_ranges": [[26, 26]], "reader": "candidate coordinator"}.

No older Chinese lesson body/record/review was supplied to this fresh tree. The future author must independently propose/calibrate terms before first body writing. SCOPE.md records complete source caveats. Mandatory future read-only CJK-bold risk scan and manual raw angle-tag Markdown review supplement original strict and actual GFM; they do not permit rewriting code or adding checker exceptions.
