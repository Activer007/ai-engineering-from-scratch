# S05 线性代数基础术语增量 v1.0

2026-10-02。固定英文01/01、01/02的实数向量/矩阵语境；联用核心及试点数学词表，已有定义不覆盖。首现可给中英解释；公式、维度表达、索引、API/类、运算符和代码保持原样。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| scalar | 标量（scalar） | 单个数；不是缩放这个动作 |
| vector | 向量（vector） | 本课有序分量及几何方向；不能混同数据集样本行 |
| component / coordinate | 分量 / 坐标 | 按源文指对象的数值分量或基下坐标 |
| matrix / tensor | 矩阵（matrix）/ 张量（tensor） | 保留Matrix/Vector等类名；矩阵rank与张量维数不混用 |
| shape | 形状（shape） | 各轴大小的有序组，行×列顺序不变 |
| dimension / dimensionality | 维度 / 维数 | 数组轴/形状语境用维度；向量空间独立方向数量用维数；按上下文说明 |
| row / column | 行 / 列 | 行向量、列向量与行列数分别对应；不能为中文语序交换乘数角色 |
| dot product | 点积（dot product） | 本批实数欧氏向量运算；不可无条件替代复数共轭内积 |
| inner product | 内积 | 若源未使用此术语，不用它掩盖点积的具体定义 |
| matrix multiplication | 矩阵乘法 | 与逐元素乘法分开；乘法顺序/内外维度保持 |
| element-wise / Hadamard product | 逐元素 / Hadamard积 | 对应元素运算，非矩阵乘法；代码`*`/`@`原样 |
| transpose | 转置 | 转置作用的矩阵对象明确；不混为逆矩阵 |
| magnitude / norm | 模或大小 / 范数（norm） | magnitude此处为向量长度；避免与分量数/内存长度混淆 |
| normalization / unit vector | 归一化 / 单位向量 | 本课缩放至单位范数；不是统计标准化或改变方向 |
| cosine similarity | 余弦相似度 | 点积除以模长乘积；不把未归一化点积等同余弦 |
| linear independence | 线性无关 | 不存在非平凡零线性组合；不是统计独立 |
| linear combination | 线性组合 | 标量系数加权相加，符号/系数属于哪个向量不可交换 |
| span | 张成 / 张成空间 | 全部线性组合的集合；不同于模型注意力跨度 |
| basis | 基（basis） | 线性无关且张成目标空间的向量组 |
| rank | 秩（rank） | 独立列/行方向数；非张量轴数 |
| full rank / rank-deficient | 满秩 / 秩亏 | 对矩形矩阵需与其行列数的较小值比较；保留源限定 |
| projection | 投影（projection） | 明确“谁投到谁上”；分母对应被投向向量 |
| orthogonal / orthonormal | 正交 / 标准正交 | 后者还要求每个向量单位范数；两者不互换 |
| Gram-Schmidt process | Gram-Schmidt正交化 | 专名保持；减去投影再归一化，次序不变 |
| determinant | 行列式（determinant） | 标量值，不是矩阵本身；方阵条件按源保留 |
| inverse / singular | 逆矩阵 / 奇异 | 非奇异条件与数值近奇异不能混为一谈；源阈值原样 |
| identity matrix | 单位矩阵 | 区别单位向量 |
| broadcasting | 广播（broadcasting） | 兼容形状的逐元素扩展；不是矩阵乘法条件 |
| linear transformation | 线性变换 | 平移不自动属于线性变换；源文概括单列 |
| weight matrix / bias | 权重矩阵 / 偏置 | 行提取输出模式与输入特征的对应关系保持 |
| embedding | 嵌入 | 向量表示，不套用特征选择的嵌入法 |
| autodiff | 自动微分 | 不等于符号求导；框架标识符原样 |

新术语解释不能修正或强化源文结论。零向量、空矩阵、维度不匹配、数值容差与复杂度等代码前提分列source_issues，不擅自改源程序。GFM裸乘号如需转义，须仅加反斜杠、可逆还原并记录，数学符号内容不变。
