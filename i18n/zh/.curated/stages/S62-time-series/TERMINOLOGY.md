# S62 时间序列术语增量

继承70项固定支持；通用章节标题沿核心增补表。API、标识符、公式、单位和图代码不译。记录源问题不等于修改译文。

| English | 中文或保留形式 | 语境与边界 |
|---|---|---|
| time series / forecasting | 时间序列 / 预测 | 按时间排列的观测与未来预测，不擅自承诺可预测性 |
| stationarity | 平稳性 | 指统计性质随时间不变；源文混用弱平稳、单位根检验和经验检查另列 |
| trend / seasonality / residual | 趋势 / 季节性 / 残差 | 源分解三分量，周期性不一定限于季节 |
| differencing / first-order / second-order | 差分 / 一阶 / 二阶 | 连续值相减，不混为微分或原序列导数 |
| i.i.d. | 独立同分布（i.i.d.） | 独立与同分布为不同要求 |
| autocorrelation / ACF | 自相关 / 自相关函数（ACF） | 相关不代表因果或独立，原估计器有限样本问题另列 |
| partial autocorrelation / PACF | 偏自相关 / 偏自相关函数（PACF） | 移除更短滞后的间接影响 |
| lag / lag features | 滞后 / 滞后特征 | t-k历史值，未来和当前目标不能误作已知特征 |
| rolling / expanding statistics | 滚动统计量 / 扩展窗口统计量 | 固定窗口与累计历史区分 |
| walk-forward validation | 滚动前向验证（walk-forward validation） | 训练时间早于验证；仅有时间切分不保证所有处理无泄漏 |
| expanding window / sliding window | 扩展窗口 / 滑动窗口 | 全历史递增与固定长度向前移动 |
| horizon / recursive / direct / multi-output | 预测步长 / 递归 / 直接 / 多输出 | 一步、固定起点多步与滚动一步区分 |
| ARIMA | 自回归差分移动平均（ARIMA） | AR为自回归，I为差分，MA用过去误差；不与滑动均值基线混同 |
| ADF | 增广Dickey-Fuller（ADF）检验 | 原假设与平稳性结论的适用限定另列 |
| MAE / RMSE / MAPE | 平均绝对误差 / 均方根误差 / 平均绝对百分比误差 | 首现展开缩写；零目标、尺度及单位保持源文 |
| persistence / seasonal naive | 持续性 / 季节性朴素法 | 最近值与上一周期对应位置基线 |
| regime change / structural break | 状态转变 / 结构突变 | 数据生成行为变化，不作金融领域建议 |

元数据Build/Python与键保留；~90 minutes译~90分钟，Lessons01-09保留范围。数字、百分比、窗口大小及代码特征名严格逐块保护；纯自然语言three/two等按原义译中文。源强调边界空格保持，避免中文标点附近粗体失效。
