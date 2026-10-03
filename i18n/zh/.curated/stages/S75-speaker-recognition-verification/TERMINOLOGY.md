# S75 说话人识别与验证术语增量 v1.0

2026-10-03；固定英文 06-06。沿用核心、补充表与 78 项固定支持依赖；前置音频术语来自已接受 06-02 的核心/补充表，嵌入术语承接 S64。只读术语，不复用旧中文课文。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| speaker recognition / verification / identification | 说话人识别 / 说话人验证 / 说话人辨识 | recognition 为总称，verification 为 1:1，identification 为 1:N；不混同语音内容识别 |
| enrollment / enrollment bank / utterance | 注册 / 注册库 / 话语 | 计算参考嵌入；不是账户注册；utterance 是一次话语而非采样点 |
| open-set / closed-set | 开放集 / 闭集 | 测试可能含未注册说话人；源分类局限另列 |
| EER / False Accept Rate / False Reject Rate | 等错误率（EER）/ 错误接受率 / 错误拒绝率 | 保留源阈值交叉定义；离散近似与代码错误另列，不暗修 |
| embedding / cosine similarity / normalization | 嵌入（embedding）/ 余弦相似度 / 归一化 | 数学余弦与仅点积实现有别；L2 源形保留 |
| diarization / DER | 说话人分离（diarization）/ 说话人分离错误率（DER） | 指谁在何时说话的时间标注，不是把混合波形拆成独立声源 |
| VAD / segmentation / clustering | 语音活动检测（VAD）/ 分段 / 聚类 | pipeline → 管线；agglomerative → 凝聚；spectral → 谱 |
| MFCC / mel / frame / hop | MFCC（梅尔频率倒谱系数）/ mel（梅尔频率尺度）/ 帧 / 帧移 | 承接已审音频术语；不改 featurize_mfcc 等标识符 |
| AAM-softmax / angular margin | 加性角度间隔 softmax（AAM-softmax）/ 角度间隔 | 代码和 cos(θ + m)、m、s 的保护形式原样 |
| PLDA / score normalization / cohort | 概率线性判别分析（PLDA）/ 分数归一化 / 参照组 | 冒认者参照组；不把概率似然比说成额外点积 |
| backbone / pooling / squeeze-excitation | 主干网络 / 池化 / 压缩与激励 | TDNN、ECAPA-TDNN、WavLM、模型 ID 原样 |
| channel mismatch / held-out dev set / anti-spoofing | 信道不匹配 / 留出开发集 / 反欺骗 | 声学信道与神经网络通道注意力分开 |

首现解释 ASR（自动语音识别）、SSL（自监督学习）、SOTA（当前最佳水平）、KWS（关键词检测）。通用标题沿补充表；Pitfalls → 常见陷阱。引用题名、品牌、代码注释、figure 与 SVG 原文保持。RT 保留并解释实时速度倍数，M 保留并解释百万；d 保留并解释维。数值和单位保留源形；metadata ~45 minutes → ~45 分钟，5–30 seconds → 5–30 秒，3 seconds → 3 秒，英文 one/three/first → 一/三/第一等按义等值，不把百分比改为百分点。强调闭合后保留空格，URL 使用原链接目标；不暗改源默认试验对数、数据集人数、排行榜或 EER 算法。
