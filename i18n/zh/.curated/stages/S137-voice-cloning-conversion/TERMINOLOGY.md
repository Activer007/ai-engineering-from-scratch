# S137-voice-cloning-conversion terminology support

Fixed English 1bafaa88bb4668356791150bec3a6d7df38387eb. Preauthor support candidate only. Common142 =134 TERM +8 controls; own3 pending publication. Newly available S132 TERM is appended from its independent fixed-commit readback; English prerequisites remain unchanged. No author proposal, calibration, first write, capture, record, strict or independent language review is claimed.

| English | Proposed Chinese | Semantic boundary / prior terminology |
|---|---|---|
| voice cloning / voice conversion | 声音克隆 / 声音转换 | 声音克隆沿 S134；文本生成与保留源话语内容的转换分开 |
| speaker identity / content / prosody | 说话人身份 / 内容 / 韵律 | 韵律沿 S134，不与音色或文本内容等同 |
| speaker embedding / encoder | 说话人嵌入 / 说话人编码器 | 沿 S75；不把任意混合向量说成真实声纹识别结果 |
| zero-shot / few-shot cloning | 零样本 / 少样本声音克隆 | 零样本指无需目标说话人专属训练，不是未经预训练 |
| speaker adaptation / fine-tuning | 说话人适配 / 微调 | 保留参数更新与条件输入的区别 |
| recognition-synthesis / resynthesis | 识别—合成 / 重合成 | 先提取内容再合成目标声音 |
| disentanglement / latent bottleneck | 解耦 / 潜在空间瓶颈 | 分离内容与说话人因素，不保证真实彻底独立 |
| PPG / phonetic posteriorgram | PPG（音素后验概率图） | 逐帧语音内容表征，区别声谱幅度图 |
| neural codec / codec token | 神经音频编解码器 / 编解码器 token | 沿 token（词元），不套普通文本分词 |
| reference clip / reference transcript | 参考音频片段 / 参考转写文本 | 片段沿 S134；转写沿 S131 |
| SECS / WER / CER | 说话人嵌入余弦相似度 / 词错误率 / 字符错误率 | 沿 S134/S131/S133；保留缩写且粒度不混用 |
| watermark / payload / bit accuracy | 水印 / 载荷 / 比特准确率 | 音频嵌入数据，不当作签名真实性或授权证明 |
| consent gate / verifiable consent record | 授权同意检查 / 可验证的授权同意记录 | 保留具体授权目的和范围；示例不是已完成法律合规 |
| tamper-evident / revocation | 可显露篡改 / 撤销授权 | 显露篡改不等同不可篡改 |
| anti-spoofing / EER | 反欺骗 / 等错误率（EER） | 沿 S75；低 EER 不证明不会欺骗 |
| reverberation / close-mic / language leakage | 混响 / 近距离拾音 / 语言泄漏 | 语言泄漏按源指口音残留，不套信息泄露 |
| SNR / timbre / cross-lingual | 信噪比（SNR）/ 音色 / 跨语言 | 音色沿 S134；保持与韵律、可懂度的边界 |

Preserve code, inline code, numbers, mathematical expressions, identifiers, URLs, paths, Mermaid/SVG and figure payloads. Fixed-source discrepancies are recorded separately rather than silently repaired. Real later author changes must retain this frozen snapshot and their actual chronology.

Support-only revision 2026-10-05T08:40:00.217783+00:00: append S132 TERM; original preparation and all terminology rows retained. Previous common141 candidate SHA256: 360d4644897ff3489ab35fdf39dc8811ee8bd01fcede81d7025312e920840cf4.
