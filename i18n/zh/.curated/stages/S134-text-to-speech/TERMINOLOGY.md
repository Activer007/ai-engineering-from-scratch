# S134-text-to-speech 术语约定

固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb。正文起草前支持候选，依据完整本课英文、必要英文先修与 common136 校准。作者首写、capture、record、strict 和独审 pending；没有预填相关时间或 hash。

| English | 本课中文 | 依据与语义边界 |
|---|---|---|
| text-to-speech / TTS | 文本转语音（TTS） | 本课任务语境；也可在自然叙述中称语音合成 |
| text frontend / text normalizer | 文本前端 / 文本规范化器 | 日期、数字、缩写转读法；区别于数值归一化和网页前端 |
| phoneme / phonemize / phonemizer | 音素 / 转换为音素 / 音素转换器 | 本课语境；不等同拼写字符或音频采样点 |
| grapheme-to-phoneme / G2P | 字素到音素转换（G2P） | 区别字符书写形式与语音单位；不声称简单查表涵盖真实发音 |
| prosody / stress / timbre | 韵律 / 重音 / 音色 | 本课声学语境；韵律不是声调的同义词 |
| acoustic model / vocoder | 声学模型 / 声码器（vocoder） | 声码器沿 S30；前者预测声学表征，后者生成波形 |
| mel spectrogram / waveform | mel 频谱图 / 波形 | 沿音频课程；mel 首现解释梅尔频率尺度 |
| sequence-to-sequence / autoregressive / non-AR | 序列到序列 / 自回归 / 非自回归 | 序列到序列沿 S89；不得把非自回归等同没有序列依赖 |
| duration predictor / mel frame schedule | 时长预测器 / mel 帧时间安排 | 预测每音素占几帧；不是运行任务调度器 |
| flow matching / variational inference | 流匹配 / 变分推断 | 本课生成模型语境；源方法归类保留，不擅修架构 |
| voice cloning / reference clip | 声音克隆 / 参考音频片段 | 保留源应用含义；本次没有采集、合成或克隆 |
| MOS / CMOS | 平均意见得分（MOS）/ 比较平均意见得分（CMOS） | 主观评分与比较评价分别说明；不等同自动预测得分 |
| UTMOS / DNSMOS | UTMOS / DNSMOS | 保留指标名，说明为无需参考音频的神经评分预测器 |
| CER / SECS | 字符错误率（CER）/ 说话人嵌入余弦相似度（SECS） | CER 是可懂度代理，SECS 衡量说话人相似度；不扩大为全部声音质量 |
| out-of-vocabulary / OOV | 词表外（OOV） | 未知专名等输入，区别无声帧 |
| code-switched input / clipping / aliasing | 语码转换输入 / 削波 / 混叠 | 混合语言、振幅截断和采样频率伪影三者分开 |

沿用编码器、解码器、交叉注意力、隐藏状态、微调、管线等现有词。API、模型名、代码、公式、数字、URL、路径、SVG 与 figure 载荷保护。源对模型和效果的时效断言单列，不通过译文暗改。作者实际提出新词时，另保留真实支持增量。
