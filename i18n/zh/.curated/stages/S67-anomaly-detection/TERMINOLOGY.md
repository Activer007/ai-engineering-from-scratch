# S67 异常检测术语增量 v1.0

联用核心、补充及 DEPENDENCIES.json 的 74 项固定依赖。来源：固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb 的 02-16。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| anomaly detection / anomaly / outlier | 异常检测 / 异常 / 离群点 | 沿 S22/S28/S31；偏离常态不自动证明业务危害，源概括单列 |
| point / contextual / collective anomaly | 点异常 / 上下文异常 / 集体异常 | 单点、条件背景、序列整体三者分开；五次与连续五十次依源 |
| Z-score | Z-score（标准分数） | 以标准差衡量距均值远近；符号和代码保持 |
| interquartile range / IQR | 四分位距 / IQR | Q3 - Q1；首现 四分位距（IQR），不是四分位数 |
| Isolation Forest / isolation tree | 孤立森林 / 孤立树 | 首现 孤立森林（Isolation Forest）；算法名代码原样 |
| local outlier factor / LOF | 局部离群因子 / LOF | 首现 局部离群因子（LOF）；局部可达密度与普通计数密度分开 |
| local reachability density / masking effect | 局部可达密度 / 掩蔽效应 | 不把距离本身说成密度；密集区异常可能被掩蔽 |
| contamination | 异常比例 | 本课异常占比语境，区别测试集污染；参数标识符原样 |
| semi-supervised / weakly supervised | 半监督 / 弱监督 | 忠实保留本课局部定义，弱监督仅评估的过窄说法单列 |
| precision / recall / accuracy / false positive | 精确率 / 召回率 / 准确率 / 假阳性 | 沿 S28/S39；业务 alert 语境 false alarm 为误报 |
| AUROC / AUPRC / Precision@k | ROC 曲线下面积 / 精确率-召回率曲线下面积 / Precision@k | 缩写保留，首次解释；不是 AP 或准确率 |
| distribution shift / threshold drift / alert fatigue | 分布偏移 / 阈值漂移 / 告警疲劳 | 与梯度漂移无关；业务损失举例非承诺 |
| autoencoder / reconstruction error / ensemble | 自编码器 / 重构误差 / 集成 | 沿既有术语；源检测效果的保证式措辞保留且单列风险 |
| anomaly detection pipeline | 异常检测管线 | 沿 S57 管线，不改作生产部署通过 |
