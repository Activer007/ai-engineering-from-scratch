# S130-open-vocab-clip 术语约定

固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；本地 own3 候选，未安装、未发布。原术语提案 SHA256 ccb4670e0890bd752b93ca21212bf38a66575d53272993c5e05cf9cde5cf1f3d；首写前校准 SHA256 bb9735ed66df45ccc3075b31b3a0a303725882f24d1580173b42541a172ff7cc。原 common133 不变，本候选追加已独核 S127–S129 TERM 为 common136。

| English | 建议译法 | 边界 |
|---|---|---|
| open-vocabulary / closed-vocabulary | 开放词表 / 封闭词表 | 分类候选类别的开放程度，不是分词器词表大小 |
| two-tower / dual encoder | 双塔 / 双编码器 | 两个独立编码器，末端映射到共同维度；沿S59双编码器概念 |
| image-caption pair | （图像，图像描述）对 | caption是描述图像的文本，不是代码注释或图表题名 |
| zero-shot transfer | 零样本迁移 | 无任务专属训练，不是没有预训练；零样本分类沿S113 |
| joint embedding | 联合嵌入 | 沿核心嵌入，强调共享表示空间 |
| prompt template | 提示词模板 | 模板内真实英文模型输入保持原样，提示词沿核心 |
| text-conditioned detection / segmentation | 以文本为条件的检测 / 分割 | 条件输入，不等同识别图像中的文字 |
| per-pair loss | 逐对计算的损失 | 相对于批次级归一化，保留源方法描述 |
| temperature / logit_scale | 温度 / logit_scale | tau、内部对数参数及exp后的乘数有区别；代码标识符原样；源并列表格风险另列 |
| projection head | 投影头 | 沿ADDENDUM，不能机械套用分类语境的线性分类头 |

继续沿用：余弦相似度、L2归一化、模型检查点、对比损失、多层感知机、API、视觉语言模型、大语言模型、top-1准确率、recall@5（召回率）。详见首写前 evidence-sha256:bb9735ed66df45ccc3075b31b3a0a303725882f24d1580173b42541a172ff7cc 与125表检索证据。
