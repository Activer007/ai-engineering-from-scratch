# S16 范数与距离术语增量 v1.0

2026-10-02。联用核心、补充及 S05–S14 词表；主协调确认本增量无冲突。度量、距离、范数的源边界忠实保留，不能用译法暗修数学问题。专业名字、API、数值和公式保留。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| norm / magnitude | 范数（norm）/ 模长 | 范数函数与其在向量上的值区分，任意距离未必范数诱导 |
| metric / distance | 度量（metric）/ 距离 | 原文泛用 distance 时不暗改成满足全部公理的度量 |
| L1 / Manhattan | L1 / Manhattan 距离 | 绝对值求和；专名保留 |
| L2 / Euclidean | L2 / 欧氏距离（Euclidean distance） | 平方和开根，与平方 L2 及均方误差区别 |
| Lp / L-infinity / Chebyshev | Lp / L-infinity / Chebyshev 距离 | 保留 p、无穷与所有符号；p 的定义域不足单列 |
| unit ball / constraint region | 单位球 / 约束区域 | 源把球面称单位球的错误单列，不静默改为球面 |
| cosine similarity / distance | 余弦相似度 / 余弦距离 | 相似度 -1 到 +1，与 1 减相似度区别；零向量/非度量问题单列 |
| dot product | 点积 | 未归一化点积携带模长，不能暗中假设其为正 |
| Mahalanobis distance | Mahalanobis 距离 | 利用协方差结构，S 的可逆/正定前提不足单列 |
| whitening / covariance matrix | 白化（whitening）/ 协方差矩阵 | 去相关和归一化语境，不与任意 L2 单位向量归一化等同 |
| Jaccard similarity | Jaccard 相似度 | 交集大小除以并集大小；两个空集约定由代码决定 |
| edit / Levenshtein distance | 编辑距离（edit distance）/ Levenshtein 距离 | 单字符插入、删除、替换最少次数；替换非字符交换 |
| intersection over union | 交并比（Intersection over Union） | 分割集合重叠，不能变成概率分布的交叉熵 |
| mean-seeking / mode-seeking | 均值寻求 / 众数寻求 | mode 按统计语境为众数；源启发式概括不加强为定理 |
| Wasserstein / Earth Mover's Distance | Wasserstein 距离 / 推土距离 | 依本课 W_1 语境；不能将所有阶数/代价无条件等同 |
| cumulative distribution function / CDF | 累积分布函数（CDF） | 离散示例按源等距分箱，不增改实际 bin 间距 |
| optimal transport / probability mass | 最优传输 / 概率质量 | 概率质量不是物理质量；搬土为源类比 |
| absolute homogeneity / triangle inequality | 绝对齐次性 / 三角不等式 | 范数公理，与向量值的正定性和距离公理区别 |
| approximate nearest neighbor / ANN | 近似最近邻（ANN） | ANN 在这里不是人工神经网络；近似不等于精确最近邻 |
| HNSW | HNSW（分层可导航小世界） | Hierarchical Navigable Small World；算法缩写保留 |
| LSH / MinHash / IVF | LSH / MinHash / IVF | 专名与代码保留；局部敏感哈希不强译缩写 |
| LASSO / Lasso / Ridge / Elastic Net | LASSO / Lasso / Ridge / Elastic Net | 按源拼写保留；正则化与归一化、权重衰减不混同 |
| MAE / MSE | 平均绝对误差（MAE）/ 均方误差（MSE） | 平均与总和、距离与距离平方区别 |
| outlier / robustness / sparsity | 离群值 / 鲁棒性 / 稀疏性 | 具体源条件不足单列，不保证对任意污染模型有效 |

各围栏内容（包括英文解释表格）原样保护，只给裸围栏补 text。中文正文补足源有的说明，不新增证明或算法研究。GFM 若需要最小空格/转义修复，单列可逆差异并重新绑定 hash。billion 与 bits 保留并括注中文释义，产品及算法名不强译。
