# S17 机器学习统计学术语增量 v1.0

2026-10-02。联用核心及S05–S16词表；重点区分样本/总体、统计量/参数、置信区间/可信区间和相关/因果。API、公式/条件方向、概率/数值/单位及围栏内容保留。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| descriptive statistics / statistic | 描述统计 / 统计量 | 数据摘要与样本函数，不把总体参数当样本统计量 |
| central tendency / spread | 集中趋势 / 离散程度 | 均值/中位数/众数与方差/标准差/IQR不同 |
| mean / median / mode | 均值 / 中位数 / 众数 | mode不是模式；左右偏关系保留源判断并单列限制 |
| percentile / quartile / IQR | 百分位数 / 四分位数 / 四分位距（IQR） | Q1/Q3及25/50/75的对应不交换，源有限样本定义约定另记 |
| sample / population | 样本 / 总体 | 样本量n与总体N、样本均值和总体均值分开 |
| Bessel's correction / unbiased | Bessel校正 / 无偏 | 方差分母n-1与n保持，有限方差/独立条件不能暗补进源 |
| Pearson / Spearman correlation | Pearson相关系数 / Spearman秩相关 | 线性与单调关联分开；秩不是矩阵rank；正态假设过度概括另记 |
| covariance / correlation matrix | 协方差矩阵 / 相关矩阵 | 原始单位协变与标准化关联不同；PCA术语沿用 |
| hypothesis testing | 假设检验 | 检验结果不是假设真假的后验概率 |
| null / alternative hypothesis | 零假设 / 备择假设 | H0/H1角色和拒绝/未拒绝方向不互换 |
| p-value / significance level | p值 / 显著性水平 | 沿用S10；条件是H0为真，不是H0的后验概率 |
| confidence interval / level | 置信区间 / 置信水平 | 沿用S10，与Bayes可信区间不同；重复采样覆盖率方向保持 |
| precision / accuracy | 估计精度 / 准确性 | 置信区间语境；分类precision译精确率，accuracy译准确率 |
| t-test / chi-squared test | t检验 / 卡方检验 | 检验分布与观测计数/频率分开；Welch专名保留 |
| paired / independent sample | 配对 / 独立样本 | 同一数据划分配对与各折独立不是同义，CV依赖问题单列 |
| observed / expected frequencies | 观测频数 / 期望频数 | 本例为计数，不误写成相对频率 |
| statistical / practical significance | 统计显著性 / 实际显著性 | 统计证据与实际价值区分；源绝对意义判断不强化 |
| effect size / Cohen's d | 效应量 / Cohen's d | 标准化差异和样本量、p值分开，符号/pooled_std保持 |
| multiple comparisons / Bonferroni | 多重比较 / Bonferroni校正 | alpha除以检验次数，不取倒数；依赖条件源问题单列 |
| bootstrap / resampling with replacement | bootstrap（自助法）/ 有放回重采样 | 估计统计量抽样分布；与后验抽样、无放回抽样分开 |
| parametric / non-parametric test | 参数检验 / 非参数检验 | 非参数不等于无假设，源表述保留并单列 |
| Wilcoxon signed-rank | Wilcoxon符号秩检验 | 不混成符号检验；独立/对称性等前提另记 |
| Type I / Type II error | I类错误 / II类错误 | 分别假阳性/假阴性，H0真时拒绝/假时未拒绝 |
| statistical power | 统计功效 | 正确拒绝错误H0的概率，1减II类错误率；非算力 |
| p-hacking / cherry-picking | p值操纵 / 挑选有利结果 | 数据驱动反复选择检验/指标，不等同预注册检验 |
| data leakage / hold out | 数据泄漏 / 留出 | 训练测试分离与未来信息泄漏；无实际用户健康数据参与 |

CLT沿用中心极限定理；bootstrap无假设、参数检验正态假设、交叉验证依赖、p值证明真实等源过度概括均保留在译文并单列来源风险。百分比不改为百分点。纯说明/公式围栏仅补text标签；中文加粗后的必要空格保持最小可逆并接受真实GFM检查。
