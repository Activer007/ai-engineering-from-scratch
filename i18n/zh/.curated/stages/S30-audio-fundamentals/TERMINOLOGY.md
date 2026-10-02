# S30 音频基础术语增量 v1.0

2026-10-02。主协调已确认。联用核心与补充、S21 Fourier、试点 06/02 及截至 S27 的固定词表。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| waveform | 波形（waveform） | 音频时域信号；浮点范围与单声道假设依源保留 |
| sample / sampling rate | 采样点或采样值 / 采样率 | 音频采样，不套用分布抽样 |
| Fourier transform / DFT / FFT | Fourier 变换（傅里叶变换）/ 离散 Fourier 变换（DFT）/ 快速 Fourier 变换（FFT） | 沿 S21；源对 FFT 长度限制另列风险 |
| magnitude / amplitude / phase | 模 / 幅度 / 相位 | 复系数的模与信号幅度不无条件等同，源归一化遗漏单列 |
| frequency bin | 频点（frequency bin） | 沿 S21，索引与 Hz 区分；API 中 bin 原样 |
| spectrogram / mel | 频谱图 / mel（梅尔频率尺度） | 沿 06/02，保留 mel 不强改专名 |
| frame / hop / window | 帧 / 帧移 / 窗 | 帧长不等于帧移；Hann 与 Hamming 保留原名 |
| STFT | 短时 Fourier 变换（STFT） | 分帧加窗随时间的变换 |
| aliasing / anti-aliasing | 混叠 / 抗混叠 | 高频折叠与低通滤波，频率边界条件单列 |
| downsampling / resampling / decimation | 降采样 / 重采样 / 抽取 | 本课朴素抽取为每三个采样点取一个，不等同带低通的完整重采样 |
| bit depth / PCM | 位深 / PCM（脉冲编码调制） | int16 范围、float32 精度与默认读出 dtype 源问题不暗修 |
| vocoder | 声码器（vocoder） | TTS 声码器训练，具体模型采样率保持源断言 |
| brick-wall low-pass filter | 砖墙式低通滤波器（brick-wall low-pass filter） | 首处说明为截止处陡峭的滤波形状，不附加物理可实现保证 |
| ASR / TTS / WER | 自动语音识别 / 文本转语音 / 词错误率 | 缩写保留，首处解释 |
| DSP / ADC / DAC | 数字信号处理 / 模数转换器 / 数模转换器 | 缩写保留，ADC 与 DAC 不互换 |

Whisper-Large-v4、Parakeet、SeamlessM4T v2、Kokoro、F5-TTS、xTTS v2、VALL-E 2、NaturalSpeech 3 与库名、API、参考书名/作者/URL 原样保留，不代表核验其时效或可用性。
