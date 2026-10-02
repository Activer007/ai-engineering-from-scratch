# S21 Fourier 变换术语增量 v1.0

2026-10-02。联用核心、补充及 S05–S18 词表；沿用 01/19 复数的模、相位、相量，不重译复数课。专名保留 English，频率单位和公式原样。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| Fourier transform / DFT / FFT | Fourier 变换（傅里叶变换）/ 离散 Fourier 变换（DFT）/ 快速 Fourier 变换（FFT） | DFT 是变换，FFT 是快速算法；不能把任意 FFT 长度限制为二次幂 |
| time / frequency / space domain | 时域 / 频域 / 空域 | 时间索引、频率索引与图像空间维度不同 |
| sample / sampling rate | 采样点或采样值 / 采样率 | 信号语境用采样；不是 S18 分布抽样或 S17 样本量的无条件替代 |
| amplitude / magnitude / phase | 幅度 / 模 / 相位 | 信号幅度、未归一化复系数的模、相角分开；phase 课程阶段语境不同 |
| phasor / complex sinusoid | 相量 / 复正弦波 | 沿用复数课；旋转指数与实信号的正弦波幅度不等同 |
| frequency bin | 频点（frequency bin） | 离散频率位置，k 索引不等于物理 Hz；负频索引需源约定 |
| DC component / Nyquist frequency | 直流分量（DC）/ Nyquist 频率 | DC 是零频，Nyquist fs/2；N/2 索引的偶数条件不足单列 |
| forward / inverse transform | 正向 / 逆变换 | 指数正负号与 1/N 保持，不能混为矩阵转置 |
| twiddle factor / butterfly | 旋转因子（twiddle factor）/ 蝶形运算 | FFT 合并子变换，指数符号与奇偶支路不变 |
| power / magnitude / phase spectrum | 功率谱 / 幅度谱 / 相位谱 | \|X\|^2、\|X\| 与 angle(X) 不混同；源归一化/功率与能量混用另列 |
| convolution / pointwise multiplication | 卷积 / 逐点相乘 | 星号依源语境表示卷积或普通乘法，不全局替换 |
| circular / linear convolution | 循环卷积 / 线性卷积 | 首尾回绕与补零长度 N+M-1 区别 |
| windowing / spectral leakage | 加窗 / 频谱泄漏 | 加权渐变与周期边界，Hamming 非零端点等源简化另记 |
| main lobe / side lobe | 主瓣 / 旁瓣 | 宽度与电平不同，负 dB 数字/符号原样 |
| Hann / Hamming / Blackman | Hann / Hamming / Blackman | 窗函数专名不改写，不把 Hann 误为 Hanning |
| Parseval's theorem | Parseval 定理 | 能量等式的 1/N 缩放不可漏 |
| positional encoding / receptive field | 位置编码 / 感受野 | Transformer 编码频带与 CNN 卷积核空间覆盖语境不同 |
| STFT / spectrogram | 短时 Fourier 变换（STFT）/ 频谱图 | 时间窗位置与频率两个轴保持，幅度与功率图因定义而异 |
| chirp / mel | 啁啾信号（chirp）/ mel（梅尔频率尺度） | 源定义为频率随时间升高，广义上下扫频条件不暗加 |
| aliasing / anti-aliasing | 混叠 / 抗混叠 | 采样前低通，频率折叠与正弦相位/正负号区分 |
| zero-padding / resolution | 补零 / 分辨率 | 频点密度增加不等于真实频率辨别能力增加 |

Cooley-Tukey、FNet、Whisper、DeepSpeech、Gaussian、Transformer、NumPy/numpy、SciPy、API 名及论文作者保留。自然量级 million/trillion 保留并解释；2D 保留并可括注二维。GFM 裸乘号/中文加粗/表格竖线只允许最小可逆语法修复，任何变更重新绑定 source/target 审核。源缺条件与错误不得在翻译中悄改。
