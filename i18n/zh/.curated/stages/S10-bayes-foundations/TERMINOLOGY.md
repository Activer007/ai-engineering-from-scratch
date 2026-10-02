# S10 Bayes定理术语增量 v1.0

2026-10-02。联用核心、增补、S09概率及先前数学词表；区分条件方向、参数与观测、概率质量/密度与似然、后验均值/众数。API/类/路径/数值单位和所有公式/代码载荷保护。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| Bayes' theorem | Bayes定理（贝叶斯定理） | Bayes专名保留，标题可简写Bayes定理 |
| prior / posterior | 先验 / 后验 | 观察证据前/后对参数或假设的分布，更新方向明确 |
| likelihood | 似然（likelihood） | 固定观测后关于参数的函数；不能与后验概率互换 |
| evidence / marginal likelihood | 证据 / 边际似然 | 归一化项P(data)，不是单个类别的似然 |
| normalizer | 归一化因子 | 使后验概率和/积分归一，不是向量单位化 |
| law of total probability | 全概率公式 | 互补假设各条件概率乘先验再相加，分母/补事件保持 |
| Naive Bayes | 朴素Bayes（Naive Bayes） | 依类条件独立，不是无条件独立；类名NaiveBayes原样 |
| Laplace smoothing | Laplace平滑（拉普拉斯平滑） | add-one为加一平滑；一般smoothing参数可非1，词项计数与文档频数区分 |
| MLE | 最大似然估计（MLE） | 最大化P(data\|parameters)，不使用参数先验 |
| MAP | 最大后验估计（MAP） | 最大化后验密度/质量，非后验均值；L1/L2对应需特定先验，源泛化单列 |
| Gaussian / Laplace prior | Gaussian先验（高斯先验）/ Laplace先验 | 与L2/L1的对应分别保持，不把任意“小参数先验”都当Gaussian |
| regularization / ridge | 正则化 / 岭回归 | 惩罚强度、负log尺度与似然条件不暗改 |
| frequentist / Bayesian | 频率学派 / 贝叶斯学派 | 统计框架，不把SGD算法本身定义为其中一种 |
| confidence / credible interval | 置信区间 / 可信区间 | 前者重复程序覆盖，后者给定模型/先验的后验区间，不能互换 |
| calibrated probability | 校准的概率 | 不等于分类准确率；Bayesian方法不自动保证模型校准 |
| false positive / false-positive rate | 假阳性（医疗）或误报 / 假阳性率 | 在真实阴性群体中的阳性比例，非所有阳性中错误所占比例 |
| sensitivity / specificity | 灵敏度 / 特异度 | 本课源把99%accuracy展开为检出率99%与误报率1%，按原分别保留 |
| base rate fallacy | 基率谬误（base rate fallacy） | 忽视先验患病率/类别基率，不与误报率混用 |
| spam / ham | 垃圾邮件 / 正常邮件 | 代码标签spam/ham与训练文本原样；ham不译成火腿 |
| tokenization / vocabulary | 分词 / 词表 | whitespace split与CountVectorizer默认规则差别单列，不声称两者完全相同 |
| conjugate prior | 共轭先验（conjugate prior） | 相对于特定似然；先验与后验同族，参数维数和积分限制源语境保留 |
| Beta-Binomial | Beta-Binomial（Beta-二项） | Beta参数a,b分别加成功/失败；均值a/(a+b)与众数不同 |
| Gamma / Dirichlet | Gamma分布 / Dirichlet分布 | 参数化rate/scale含义须分清，源未注明处另记，不改公式 |
| sequential / batch updating | 顺序更新 / 批量更新 | 相同模型及数据假设下的更新次序；不等同任意历史数据都可丢弃 |
| A/B testing / conversion rate | A/B测试 / 转化率 | 假设示例，不是实际产品上线指令；点击数与曝光数/未点击数不混用 |
| posterior probability P(B>A) | 后验概率P(B>A) | 两变体真实率的比较，不是p-value或保证收益 |
| p-value / optional stopping / peeking | p值 / 可选停止 / 中途查看 | 不能把Bayesian可选停止概括成频率误报率自动受控；源风险单列 |
| Monte Carlo / Thompson sampling | Monte Carlo（蒙特卡洛）/ Thompson抽样 | 专名保留，样本比例是有限模拟估计而非精确积分值 |

P(A\|B)等表格转义保持，不增列。代码样本里的lottery/free等特征词保持英文，必要中文解释只在自然语言，不能改训练文本。给定比例/索引/计数、0.95与0.05决策边界、100,000次抽样等原样。

中文加粗闭合标点后若接汉字需检查GFM空格，公式裸乘号可作最小可逆转义。真实GFM必须核表格列数、所有strong与乘号；修后重新独立hash绑定。源医疗情境是固定参数的教学例子，不做真实诊断；统计/代码缺陷记录不等于允许改源。
