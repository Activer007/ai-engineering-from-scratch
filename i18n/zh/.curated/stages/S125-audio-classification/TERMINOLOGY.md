# S125-audio-classification 术语约定

固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；本地 own3 支持候选，未安装、未发布。以下完整保留作者术语提案的本课用法及保护边界，提案证据 SHA256 `ee9b80936b35d8d96a6312208ab91c9b7a13691e788d1db4fdf2be30fd04631f`。原作者 common127 已包含 S117 修订 TERM；本轮只追加 S121–S123 已独核固定 TERM 作为参考，当前 common130，不替换旧作者历史。

| EN | 本课采用 / 建议 | 语境与边界 |
|---|---|---|
| audio classification / language ID | 音频分类 / 语言识别 | 语言 ID 指所说语言的类别；en/es/ar 原样 |
| k-NN / labeled bank / majority vote | k 近邻（k-NN）/ 带标签的样本库 / 多数投票 | 对 top K 近邻投票；k、K 大小写按源上下文 |
| MFCC / mel / log-mel | MFCC（梅尔频率倒谱系数）/ mel（梅尔频率尺度）/ log-mel（经对数压缩的 mel 特征） | 沿核心、补充表、S30、S75；不把 mel 当 MFCC |
| spectrogram patch / patchify | 频谱图块 / 将频谱图切成块 | patch 为时频图上的块，不是软件补丁；16×16 不变 |
| Audio Spectrogram Transformer / AST | 音频频谱图 Transformer（AST） | AST 名称和模型标识保留；不用中文替换 API |
| class imbalance / domain shift / label noise | 类别不平衡 / 领域偏移 / 标签噪声 | 前两项沿 S22/S55/S68；干净与含噪音频分布不同 |
| multiclass exclusive / multiclass multi-label | 多类别、互斥标签 / 多类别、多标签 | 每段音频可有几类标签的区别；源 UrbanSound-style 归类不在翻译中修复 |
| mean average precision / mAP | 平均精确率均值（mAP） | 沿 S39/S94/S100；非准确率、数值精度或 Bayes MAP；源“跨类别和阈值”定义单列风险 |
| per-class recall / macro F1 / accuracy | 各类别召回率 / 宏平均 F1 / 准确率 | 沿 S28/S39/S51；macro F1 不因首现括注而重复 F1 数字 token |
| Mixup / SpecAugment | 保留原名，正文解释线性混合样本及标签 / 随机遮蔽时间段和频带 | 沿 S88 mixup；SpecAugment 的掩蔽以频谱图为对象 |
| frozen backbone / head | 冻结的主干网络 / 分类头 | 沿补充表、S75、S85；冻结主干和微调全模型不是同义词 |
| BCE / KWS / SOTA | 二元交叉熵 / 关键词检测 / 当前最佳水平 | 首现保留缩写并解释；不会据译名扩大源结论 |
| four-moment pooling | 对四种矩统计量进行池化 | 此处 mean/var/skew/kurtosis 是四种统计量，不是只计算第四阶矩 |

等值映射：~75 minutes → ~75 分钟；10-second → 10 秒；millions of hours → 数百万小时（明确记录的等值自然语言单位映射，未加精确数字）；1990s → 1990 年代。M、K、min 保留并给出中文释义；1-10%、1-2 mAP、1/4、80%+、95% 以及所有源数值不改。论文题名、引用作者、年份、模型/数据集名称、代码、内联代码、figure、SVG 载荷和链接目标全部保留。
