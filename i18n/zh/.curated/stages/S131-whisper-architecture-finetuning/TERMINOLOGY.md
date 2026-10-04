# S131-whisper-architecture-finetuning 术语约定

固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；本地 own3 候选，未安装、未发布。原术语提案 SHA256 d120e6a2e95417ca7a03307167e68c05b7bd3ed489af0dfee8d3d0e7522a92fc；首写前校准 SHA256 45236c0d52d59cecf3fc262a1f7e2b96773a8a5153067a658b0a7d4f3cef31bb。原 common133 不变，本候选追加已独核 S127–S129 TERM 为 common136。

| English | 本课中文 | 语境和沿用 |
|---|---|---|
| Whisper — Architecture & Fine-Tuning | Whisper：架构与微调 | 源 H1；模型名保留 |
| encoder-decoder / self-attention / cross-attention | 编码器—解码器 / 自注意力 / 交叉注意力 | 核心、ADDENDUM、S89/S92 |
| ASR / WER | 自动语音识别（ASR）/ 词错误率（WER） | S30/S75；不把 WER 当准确率 |
| log-mel / mel / spectrogram | log-mel（经对数压缩的 mel 特征）/ mel（梅尔频率尺度）/ 频谱图 | 核心、ADDENDUM、S30/S75/S125；不是 MFCC |
| hop / stride / zero-padding | 帧移 / 步幅 / 零填充 | S30；main 的 stride_s 实为重叠长度，源风险单列 |
| domain shift | 领域偏移（domain shift） | S125；区别漂移、语言切换 |
| transcription / translation | 转写 / 翻译 | 输出语音原语言文本与跨语言转换分别表达；原 token 描述错误不暗修 |
| prompt / token / BPE / tokenizer | 提示词（prompt）/ token（词元）/ BPE（字节对编码）/ 分词器（tokenizer） | 核心首现解释；保护所有特殊 token |
| timestamp / word-level timestamp / forced alignment | 时间戳 / 词级时间戳 / 强制对齐 | 本课音频时间位置与对齐；不宣称 attention 天然等于完整词级时间戳 |
| fine-tuning / full fine-tuning / LoRA | 微调（fine-tuning）/ 全量微调 / LoRA（低秩适配） | 核心、S91；原百分比/数字不转换 |
| VAD / diarization | 语音活动检测（VAD）/ 说话人分离（diarization） | S75；diarization 指谁在何时说话，不是声源波形拆分 |
| chunked long-form / streaming | 长音频分块处理 / 流式处理 | S89 流式语境；原模型窗口限制原样 |
| hallucination / held-out / epoch | 幻觉（hallucination）/ 留出数据 / 轮（epoch） | S74/S89/S91；未假称进行实际训练评估 |

自然语言单位映射：second / sec → 秒；hours → 小时；minute / minutes → 分钟；layers / dim / heads → 层 / 维 / 注意力头。September → 九月（首稿误用了数字 9，使原检查失败；真实修订见 revision-01）。k、M、B 保留并解释为千、百万、十亿；ms 和 s 等源符号单位保留。英文自然数量 one / multiple 按语义译成一 / 多种；不增加数字 token。引用题名、模型/库/API/路径、inline-code 和围栏内容原样。

当前 R05 以延迟／显存“缩减倍率”和速度“为原来的 X×”明确最终倍率，原8×、4×和全部代码不变。原提案与原完整 CHANGES_REQUESTED 保留；四处实际修订见独立增量 SHA256 04c0e1e331e562bcba5db058a475f701bf0f39fd8341db5809b9b7a436173b2e。
