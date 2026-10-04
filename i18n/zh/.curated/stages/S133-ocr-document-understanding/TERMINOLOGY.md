# S133-ocr-document-understanding 术语约定

固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`。这是正文起草前的支持候选，依据固定本课英文、必要英文先修与 common136 校准。正文、首写、capture、strict 和独立审校均 pending；没有作者提案或独审结果的预填记录。支持发布后的真实 commit 由外部回读证据绑定。

| English | 本课中文 | 依据与语义边界 |
|---|---|---|
| optical character recognition / OCR | 光学字符识别（OCR） | 沿 S77；从像素到字符，区别于字段语义抽取 |
| document understanding | 文档理解 | 本课源语境；从文档提取结构化信息 |
| layout parsing / reading order | 版面解析 / 阅读顺序 | 本课源语境；区域分类和排序，不等同识别字符 |
| text detection / recognition | 文本检测 / 文本识别 | 沿检测与识别任务区分；前者给框，后者给字符序列 |
| bounding box / quadrilateral | 边界框 / 四边形 | 沿视觉检测语境；不把四边形限定为轴对齐矩形 |
| CTC / Connectionist Temporal Classification | 连接时序分类（CTC） | 沿真实已公开 S128；首次保留英文全称，不能说需要逐字符对齐标签 |
| blank / collapse | 空白 token / 折叠、合并重复项 | 沿 S128；先合并连续重复项，再去空白，空白不等于空格 |
| marginalise over alignments | 对所有对齐关系进行边缘化 | 沿 S128；对有效路径求和，不是只选最优路径 |
| greedy decoding / beam search / beam width | 贪心解码 / 束搜索 / 束宽 | 沿 S128；不把束宽说成输出字符数 |
| log probabilities / logits | 对数概率 / logits | 两者区分；log-softmax 输出为对数概率 |
| CRNN / BiLSTM | 卷积循环神经网络（CRNN）/ 双向长短期记忆网络（BiLSTM） | 首现展开；保留模型缩写 |
| CER / WER | 字符错误率（CER）/ 词错误率（WER） | WER 沿 S128；字符和词的粒度不得交换 |
| key-value extraction / structured field | 键值抽取 / 结构化字段 | 本课任务语境；不改字面 JSON 键和值 |
| length normalisation | 长度归一化 | 本课源措辞；技能代码未实现这一点，单列源风险 |
| end-to-end / pipeline | 端到端 / 管线 | 沿视觉课程术语；多阶段管线与整体模型区分 |
| synthetic / held-out set | 合成 / 留出集 | 本课语境；没有真实训练或评测的声明 |

代码、行内代码、公式、数字、URL、路径、模型标识、Mermaid 与 figure 载荷原样保护。源的架构概括和效果断言不通过译文暗改。作者若提出术语修订，保留本候选及实际发布身份，再记录真实增量。
