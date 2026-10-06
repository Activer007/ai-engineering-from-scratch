# S140-music-generation terminology support

Preauthor support candidate only. Short lexical entries are calibrated source support, not Chinese lesson prose. Own3 publication/readback/installation and all actual author proposal/calibration, first-write, capture, strict and independent review evidence remain pending/null.

Source basis: fixed English 06-09 and both prerequisite docs/main.py at 1bafaa88bb4668356791150bec3a6d7df38387eb. Calibration reads core TERMINOLOGY.md, ADDENDUM preamble/audio rows, and full S30/S80/S106/S109/S125/S134/S137 term files. Their local bytes match inherited immutable pins. Final common146/formal154 bindings await coordinator confirmation in DEPENDENCIES.json; no full reread of every historical term file or new remote verification is claimed. Explanations are in English to keep support preparation separate from lesson drafting.

| English | Proposed short Chinese term | Calibration and boundary |
|---|---|---|
| music generation | 音乐生成 | Lesson task, not a claim that the toy emits audio. |
| instrumental generation / instrumental | 器乐生成 / 器乐 | Distinguish from songs with vocals; do not automatically render as accompaniment. |
| song generation / vocals / lyrics | 歌曲生成 / 人声 / 歌词 | Keep the three objects separate; vocals here can mean singing rather than generic speech. |
| neural audio codec / codec | 神经音频编解码器 / 编解码器 | Reuse pinned S137; distinguish codec from S30/S134 vocoder. |
| vocoder | 声码器（vocoder） | Reuse pinned S30. Does not identify the architecture of closed models. |
| codec token / codebook | 编解码器 token / 码本 | Codec token reuses pinned S137. Keep token; here it is a discrete audio-code symbol, not a text word or authentication token. Codebook is a lesson-specific short lexical proposal. First-body explanation comes only after the writing gate. |
| token LM / autoregressive | token 语言模型 / 自回归 | Autoregressive reuses pinned S134. Preserve LM/AR abbreviations when present; the ACE-Step classification remains a source issue. |
| embedding | 嵌入（embedding） | Core convention; not feature-selection embedded method. |
| text conditioning / melody conditioning | 文本条件化 / 旋律条件化 | Reuse S106 text-conditioning pattern; lyric conditioning is a different conditioning source. |
| lyric-conditioned / conditioning input | 以歌词为条件 / 条件输入 | S109 grammatical distinction; not numerical matrix conditioning. |
| diffusion / latent diffusion | 扩散 / 潜在扩散 | Reuse S106/S109. Do not translate Stable Audio or Stable Diffusion brand names as generic words. |
| latent / latent space | 潜在表示 / 潜在空间 | S109 representation context; not the “latent disclosure” legal sense. |
| spectrogram / mel spectrogram | 频谱图 / mel 频谱图 | Core, addendum, S30. Preserve mel with its scale explanation when needed. |
| chromagram / chroma | 色度图 / 色度特征 | Music pitch-class context, not image color. Retain English at first occurrence; source gives 12 dimensions per frame. |
| FAD / Fréchet Audio Distance | 弗雷歇音频距离（FAD） | Proposed lexical rendering; preserve Fréchet name if used. Distribution distance, not per-clip fidelity or subjective listening score. |
| CLAP | CLAP | Keep model/metric name; short explanatory term: 音频—文本对比嵌入. Do not invent an acronym expansion absent from the source. |
| alignment | 对齐 | Prompt–audio semantic correspondence here, not forced phoneme alignment or value alignment. |
| musicality | 音乐性 | Human judgment axis; not equivalent to the FAD or CLAP scalar. |
| musicality artifacts / artifact | 音乐生成瑕疵 / 产物 | Audible defects versus shipped reusable deliverable. Core artifact convention requires context. |
| stems / stem separation | 分轨 / 分轨分离 | Separated instrument/vocal components, not the linguistic word-stem sense or the multi-channel stereo field. |
| inpainting | 局部重生成（inpainting） | Time-window audio editing. Do not reuse S106 “图像修复” or S109 “图像修补” mechanically. |
| bridge / loop | 桥段 / 循环片段 | Musical form/audio loop, not an API bridge or program loop. |
| crossfade | 交叉淡化 | Overlap affects duration; preserve the source arithmetic in the body and flag it separately. |
| timbre / tempo / BPM | 音色 / 速度 / BPM（每分钟拍数） | Tempo is musical pulse, not generation latency. Timbre follows pinned S134 and S137; preserve BPM spelling and case in protected material. |
| chord progression / voicing | 和弦进行 / 和弦配置 | Symbolic harmony and note arrangement; voicing is not speaker identity. |
| off-beat / vocal-phrase drift | 偏离节拍 / 人声乐句漂移 | Keep drift object-specific per core glossary. |
| mono / stereo / waveform | 单声道 / 立体声 / 波形 | S30 waveform convention. No claim about all open models follows from this mapping. |
| watermark / metadata / disclosure | 水印 / 元数据 / 披露 | S80 watermark/provenance boundary; technical marker does not establish legal sufficiency. |
| license / licensing / rightsholder | 许可证 / 许可授权 / 权利人 | Code, model weights, generated output and service terms are different objects. Preserve MIT, CC0, Apache-2.0 and source labels. |
| settlement / compliance | 和解 / 合规 | These words do not certify the amount, applicability or safe deployment. |

## Protected material and first-occurrence rules

Use core first-occurrence rules in future Chinese lesson writing only after own3 is genuinely published, independently read back and installed. At first body use, include the source English/acronym with the calibrated Chinese explanation; do not invent absent definitions or duplicate protected numeric tokens. Keep model names, versions, IDs, paper titles/authors, acronym case, API names, commands, filenames, URLs, code, figure payloads, SVG bytes, numerical values and units. Keep metadata keys Type, Languages, Prerequisites and Time in English; keep Build and Python unchanged.

The source-common headings use 要解决的问题、核心概念、动手实现、实际使用、交付成果、练习、关键术语、延伸阅读. Do not add the absent Learning Objectives section. Keep Step labels and numeric order.

Proposed metadata unit mapping: ~75 minutes -> ~75 分钟. Proposed month mapping, only where natural-language prose is translated: April -> 四月; Nov -> 十一月. Preserve source numerals and protected short labels such as Apr 2026 in tables or model names unless the actual approved preservation contract explicitly allows a mapped prose unit. No numeric or license correction is bundled into a term choice.

Do not force the core text-token definition onto neural-codec tokens, the image inpainting translation onto audio, or the neural latent representation translation onto legal disclosure. No new translation example sentences, section paragraphs, first-write hashes or review outcomes are supplied.


## Calibration provenance

Core rules have priority. S30 supplies waveform/spectrogram/mel/vocoder; S80 watermarks and provenance; S106 diffusion/time/text conditioning; S109 latent representation/conditioning grammar and the separation of visual artifacts from delivered artifacts; S125 log-mel/audio feature distinctions; S134 autoregressive/timbre/acoustic terminology; S137 neural audio codec/codec token/timbre. Only short glossary terms are inherited. Source inconsistencies and historical candidate headers do not authorize copying old lesson prose, changing source claims or declaring legal/runtime acceptance.
