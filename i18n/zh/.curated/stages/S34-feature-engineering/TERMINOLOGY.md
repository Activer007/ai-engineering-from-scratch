# S34 特征工程术语增量 v1.0

2026-10-02。联用核心/补充与S05–S33固定词表，43项依赖见DEPENDENCIES.json；TF-IDF与同批S36统一。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| feature engineering / selection / interaction | 特征工程 / 特征选择 / 特征交互 | 工程转换表示、选择子集、交互组合分开，selection不是降维投影 |
| scaling / standardization / normalization | 缩放 / 标准化 / 归一化 | 沿S25，z-score与min-max、单位范数、Unicode规范化不同 |
| min-max scaling / z-score | 最小-最大缩放 / z-score | 区间端点/均值方差定义保留，常量特征例外另列 |
| binning / bin | 分箱 / 箱 | 连续特征离散化，区别频域频点、采样与统计直方图用途 |
| log transform / polynomial features | 对数变换 / 多项式特征 | 原实现log(v+1)，不能暗改成log(v)；degree接口实际范围单列 |
| categorical feature / cardinality | 类别特征 / 基数 | 基数指不同类别数，沿S23，非数学基数无限集语境 |
| one-hot / dummy variable | one-hot（独热）/ 哑变量 | 沿S28，drop-first与每类别一列区别按源保护 |
| label / target encoding | 标签编码 / 目标编码 | 类别整数映射与目标统计映射分开；标签不等于目标泄漏 |
| target leakage / data leakage | 目标泄漏 / 数据泄漏 | 目标编码自身、测试统计、未来时序信息等不同来源分别定位 |
| count vectorizer / TF-IDF | 计数向量化器 / TF-IDF（词频-逆文档频率） | count与归一化TF分开；IDF文档频率、语料规模、平滑及L2默认处理保留 |
| imputation / mean / median / mode | 填补 / 均值 / 中位数 / 众数 | 与数据生成或插值不混；None与NaN范围按实现 |
| missing indicator / forward/backward fill | 缺失指示列 / 前向/后向填充 | 指示缺失本身；backfill未来信息风险另列 |
| filter / wrapper / embedded methods | 过滤式 / 包裹式 / 嵌入式方法 | 源将Lasso归wrapper仍忠实译出，类别问题单列 |
| recursive feature elimination / RFE | 递归特征消除 / RFE | 迭代删特征，不是递归求导或树剪枝 |
| variance threshold / mutual information | 方差阈值 / 互信息 | 沿S12/S17，单位敏感与自然对数nats，单变量MI不能代表交互信号 |
| robust scaling / interquartile range / leave-one-out | 稳健缩放 / 四分位距 / 留一 | 保留练习条件，不能声称保证完全消除泄漏或过拟合 |
