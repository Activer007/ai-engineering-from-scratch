# S57 机器学习管线术语增量

继承66项固定依赖，首次按上下文解释，不替换API、标识符或载荷。通用标题沿核心补充表；保留源强调边界空格。

| English | 中文或保留形式 | 语境/边界 |
|---|---|---|
| ML pipeline / pipeline | 机器学习管线 / 管线 | 有序预处理和估计器对象，不是数据并行或流水线并行 |
| transformer / estimator | 转换器 / 估计器 | sklearn对象，不是Transformer模型架构 |
| imputation / scaling / encoding | 填补 / 缩放 / 编码 | 缺失值、数值尺度和类别表示分别处理，沿S34 |
| numeric / categorical features | 数值特征 / 类别特征 | 不是任意数字列都应按连续数值缩放 |
| one-hot encoding | one-hot（独热）编码 | 与序数编码不同，沿既有one-hot术语 |
| data leakage | 数据泄漏 | 测试集/未来信息进入训练；源绝对化保证不暗修 |
| fit / transform / predict | 拟合 / 转换 / 预测 | 自然语言可译，API与代码名称保持原样 |
| train/serve skew | 训练与服务偏差 | 训练/推理处理不一致，不等同类别偏斜 |
| experiment tracking | 实验跟踪 | 记录配置、数据、指标和产物，不等于自动完整复现 |
| model registry | 模型注册表 | 模型版本元数据目录，沿registry既有用法 |
| staging / production / archived | 预发布 / 生产 / 已归档 | 源阶段标签和字符串代码保留，产品现状风险另列 |
| serialization / artifact | 序列化 / 产物 | 可交付对象；不承诺跨版本兼容或不可信加载安全 |
| reproducibility | 可复现性 | 相同代码/数据/配置重现；种子不是跨硬件完全确定性保证 |
| ColumnTransformer / Pipeline / MLflow / DVC | 保留原名 | 组件、产品和API，不自造译名 |
