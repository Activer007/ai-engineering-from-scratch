# S162 anti-spoofing and audio watermarking terminology proposal

Fixed English `1bafaa88bb4668356791150bec3a6d7df38387eb`; lesson 06-16. Source-only lexical proposal by the assigned lane author, before lesson prose. Common164 is locally verified against its exact manifest; publication, independent readback, installation and coordinator calibration acceptance remain pending. This document is not an assertion of a passed author gate.

Core first-use rules retain relevant English/acronyms with a short Chinese explanation. Metadata keys and Type/Languages values remain English. Existing headings follow ADDENDUM only where present; Pitfalls follows S75 常见陷阱. Token, if needed, first appears as token（词元）. Source code, comments, math, numbers, units, model names, paths, links, SVG and figure payloads stay exact; prose natural-language time units may be equivalently translated with mapping recorded.

| English | Proposed Chinese | Inheritance / boundary |
|---|---|---|
| anti-spoofing / deepfake detection | 反欺骗 / 深度伪造检测 | S75/S137 反欺骗; detection is not speaker verification. |
| audio watermarking / watermark | 音频水印嵌入 / 水印 | S137 水印; process may use 音频水印技术 where broader than embedding. |
| authenticated provenance / provenance manifest | 经认证的来源信息 / 来源信息清单 | Core provenance 来源信息; signature authenticates the assertion, not the depicted event. |
| cryptographic signing / signed metadata | 密码学签名 / 经签名的元数据 | Core 签名; do not conflate with watermark or content hash. |
| countermeasure / CM | 反欺骗措施（CM） | Scoped standalone real-versus-synthetic classifier; not any security mitigation. |
| spoofing-robust ASV / SASV | 抗欺骗自动说话人验证（SASV） | S75 说话人验证; integrated biometric and spoof detection. |
| speaker recognition / verification | 说话人识别 / 说话人验证 | Exact S75 distinction. |
| voice cloning / voice conversion | 声音克隆 / 声音转换 | Exact S137; not interchangeable with speech recognition. |
| EER / FAR / FRR | 等错误率（EER）/ 错误接受率（FAR）/ 错误拒绝率（FRR） | Exact S75; discrete sweep and score polarity defects remain separate. |
| payload / bit accuracy / Bit Recovery Accuracy | 载荷 / 比特准确率 / 比特恢复准确率 | S137 base terms; recovery is fraction of payload bits, not probability of watermark presence. |
| utterance / audio clip / frame / sample | 话语 / 音频片段 / 帧 / 采样点 | S75/core; sample resolution is not frame rate. |
| sample rate / bitrate | 采样率 / 比特率 | S152; protect source kHz and bits/sec quantities. |
| imperceptible / inaudible / localized | 不可感知的 / 不可听见的 / 可定位的 | AudioSeal localization means detecting temporal presence; not interface localization. |
| spectral features / spectral rolloff | 频谱特征 / 频谱滚降点 | Scoped audio term; code returns a frequency-bin index, not an amplitude rolloff slope. |
| graph attention / backbone / focal loss | 图注意力 / 主干网络 / 焦点损失 | S75 backbone, S40 focal loss; graph is relational graph, not a chart. |
| SSL / TTS / SOTA | 自监督学习（SSL）/ 文本转语音（TTS）/ 当前最佳水平（SOTA） | S75 and speech conventions; historical claim strength retained without endorsement. |
| pitch shift / speed shift / temporal manipulation | 音高变换 / 变速 / 时间维度操纵 | Pitch versus playback speed and reversal stay distinct. |
| SNR / EQ / augmentation | 信噪比（SNR）/ 均衡处理（EQ）/ 数据增强 | S137 SNR; not accuracy or confidence. |
| Mixture-of-Experts / FiLM | 混合专家模型（MoE）/ FiLM | S151 exact MoE; retain Mixture-of-Experts at first explanation. FiLM name protected; explain feature-wise modulation if source context requires. |
| liveness challenge / replay attack | 活体检测挑战 / 重放攻击 | Challenge is an anti-replay step, not proof against real-time cloning. |
| calibration / held-out set / OOD | 校准 / 留出集 / 分布外（OOD） | S75 held-out and channel context; source unmeasured performance stays unverified. |
| consent / audit log / retention policy | 授权同意 / 审计日志 / 保留策略 | S137 consent; no legal compliance certification. |
| re-encode / strip metadata / fallback | 重新编码 / 剥离元数据 / 回退方案 | S153 fallback; no implication that stripping defeats every possible provenance recovery method. |
| ASVspoof 5 / AudioSeal / WavMark / WaveVerify / AASIST / RawNet2 / NeXt-TDNN / C2PA | ASVspoof 5 / AudioSeal / WavMark / WaveVerify / AASIST / RawNet2 / NeXt-TDNN / C2PA | Exact protected names and versions; Audobox source spelling also preserved. |

Selected inheritance was semantically read: core whole file, ADDENDUM lines 1–35, complete S75/S137/S152 terminology, S151 line47 (MoE), S40 line16 (focal loss), and S153 line73 (fallback). Exact pin objects and ranges are in DEPENDENCIES.json. All164 common identities were locally checked, not all semantically reread. No global replacement or Chinese lesson body has been made. Independent reconciliation and later installed167 gate remain pending.
