# S128-speech-recognition-asr 术语约定

固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；本地 own3 候选，未安装、未发布。原作者术语提案证据 SHA256 `a4d4ae1ea375ca000d80a7ea1e3cd81dc8b90a2557b198903e433f57810fc876`；当前源语境与实际修订边界如下。原 common130 保持，本候选仅追加已独核 S124–S126 TERM 为 common133。

固定源：06-04，1bafaa88bb4668356791150bec3a6d7df38387eb。作者于 2026-10-04 UTC 新译，完整静态阅读了本课全部五个源文件和三份直接英文先修。术语以安装的 common130（122 TERM＋8 controls）为参考；其来源及逐项 SHA 已核对，校准证据 SHA256 dceee45ecc768217a5afc193e16dd63dfb855066fc13eea96e470587ff8eea05。本文件不是支持发布记录或独立语义验收。

沿用：ASR→自动语音识别，WER→词错误率；token 首次解释为词元，后续保留 token；spectrogram→频谱图；mel→mel（梅尔频率尺度）；log-mel→经过对数压缩的 mel 特征；frame→帧；encoder/decoder→编码器/解码器；hidden state→隐藏状态；cross-attention→交叉注意力；beam search/beam width/greedy→束搜索/束宽/贪心；autoregressive→自回归；VAD→语音活动检测；pipeline→管线；fine-tune→微调。

| 英文 | 本课采用的中文 | 语义界限 |
|---|---|---|
| Connectionist Temporal Classification / CTC | 连接时序分类（CTC） | 保留英文全称，首次展开；不得将逐帧分类当成已知帧字符对齐 |
| Recurrent Neural Network Transducer / RNN-T | 循环神经网络转导器（RNN-T） | 保留英文全称；不是 Transformer 的翻译 |
| blank / null / no-emit | 空白 token / 空值／不输出 | 表示当前帧不输出；不等于空格、静音或填充 token |
| predictor / joiner | 预测网络 / 联合网络 | 前者嵌入 token 历史，后者结合该状态与编码器帧；不是两个词互换 |
| alignment / collapse | 对齐关系 / 折叠、合并重复项 | CTC 先合并连续重复项，再去空白；不可反序 |
| conditional independence / dependence | 条件独立 / 条件依赖 | 原文的简化假设强度保留；不把 logits 当概率 |
| streamable / streaming | 支持流式处理 / 流式 | 音频在线处理，不能机械使用通用 API 语境的“流式输出” |
| lookahead | 前瞻 | 编码器访问未来音频帧；与优化器前瞻位置区分 |
| shallow fusion / LM fusion | 浅融合 / LM 融合 | 外部语言模型参与解码；对数概率加权原义保持 |
| prefix tree | 前缀树 | 不声称当前示例已正确实现完整 prefix CTC |
| loss lattice | 损失格网 | 3D 原形保留并解释为三维，不擅自改损失实现 |
| carryover state | 跨块保留的状态 | 音频块之间承接，不是重新独立初始化 |
| language ID / LID | 语种识别 / LID | 不是账号 ID，也不翻译 language="en" 参数 |
| marginal over alignments | 对所有对齐关系进行边缘化 | 保留求和涵盖所有有效对齐的概念，不改成择优单路径 |

数字与单位等值映射：元数据 ~45 minutes→~45 分钟；10-second→10 秒；30-second→30 秒；three/two→三/两；first 100 utterances→前 100 段话语；B/M 原形保留，表头解释十亿/百万；3D 原形保留，括注三维。16 kHz、200 ms、1200 ms、24 GB、~20×、<500 ms、范围 6-32 与 1.8–2.1%、百分比、模型数字、引用年份均保留。

源码式名称、代码、行内代码、公式、图载荷、文件路径、URL、引用题名和模型 ID 不翻译。源模型表与推荐是固定源的断言，不是作者联网核实后的选型建议。
