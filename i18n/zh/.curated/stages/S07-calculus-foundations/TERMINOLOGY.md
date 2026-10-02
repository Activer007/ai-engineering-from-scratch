# S07 微积分基础术语增量 v1.0

2026-10-02。联用核心、试点、S05/S06数学词表；仅补01/04语境，不覆盖既有定义。首现可给中英对应；所有API、公式、下标/维度、数字、单位和围栏载荷保护。单数Language元数据保持。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| calculus / derivative | 微积分 / 导数（derivative） | 导数是变化率；数值微分与解析求导分开 |
| differentiation / differential | 微分（求导）/ 微分 | 根据过程或微分量语境判断，不混成积分 |
| analytical / numerical derivative | 解析导数 / 数值导数 | 前者由解析规则得到；后者为有限差分近似 |
| partial derivative | 偏导数（partial derivative） | 明确对谁求导，其他变量保持不变 |
| gradient | 梯度（gradient） | 标量输出对输入的偏导数组成向量；不同于Jacobian或优化更新量 |
| gradient descent | 梯度下降 | 从参数中减去学习率乘梯度，负号/更新前后变量不能错位 |
| tangent / slope / curvature | 切线 / 斜率 / 曲率 | 各有数学角色；Hessian为二阶局部信息，不统一叫斜率 |
| central difference / finite difference | 中心差分 / 有限差分 | 分母2h与正负扰动保留；不要把数值近似称精确导数 |
| steepest ascent / descent | 最速上升 / 下降 | 源文未限定范数/步长时不擅自增补定理条件 |
| chain rule | 链式法则（chain rule） | 路径上乘积与多路径贡献求和区别必须保留 |
| backpropagation | 反向传播 | 计算图从输出到输入，不与参数更新混为一谈 |
| automatic differentiation / autodiff | 自动微分 | 不等于符号微分或数值差分；exact的源概括另记 |
| reverse-mode | 反向模式 | 与反向传播关联；不同于求逆矩阵 |
| Hessian matrix | Hessian矩阵（海森矩阵） | 二阶偏导矩阵，专名保留；H[i][j]对象/混合偏导顺序原样 |
| Jacobian matrix | Jacobian矩阵（雅可比矩阵） | R^n到R^m为m×n；反传使用转置，不能交换行列 |
| critical / stationary point | 临界点 / 驻点 | 本课明确gradient=0；不能漏掉这个限定再断言极值 |
| positive definite / negative definite / indefinite | 正定 / 负定 / 不定 | 与半正定/半负定分开，特征值正负条件原样 |
| local / global minimum | 局部 / 全局极小值 | 函数值或点按语境表达；原局部排除全局的简化需单列 |
| saddle point | 鞍点（saddle point） | 非极大/极小的驻点语境 |
| Newton's method | Newton法（牛顿法） | 逆Hessian与梯度相乘；收敛/极小值前提不足不静默纠正 |
| Taylor series / approximation | Taylor级数（泰勒级数）/ Taylor近似 | 无限级数与有限阶多项式区别；原光滑/解析概括单列 |
| first-order / second-order | 一阶 / 二阶 | 导数阶数/近似阶数/优化信息按语境保留 |
| integral / expectation | 积分 / 期望 | 积分变量、区间、密度加权保持 |
| probability density | 概率密度 | 不是离散概率；连续积分与离散和区分 |
| KL divergence | KL散度 | 保留p与q顺序，不称对称距离 |
| normalization constant | 归一化常数 | 概率分布积分/求和归一化，不套用向量单位范数 |
| marginal likelihood / ELBO | 边际似然 / 证据下界（ELBO） | 两者相关但不等同；缩写原样 |
| Fisher information matrix | Fisher信息矩阵 | 与一般Hessian不同；源“statistical Hessian”类比需单列 |
| L-BFGS / Adam / momentum | L-BFGS / Adam / 动量 | 优化器名保留；Adam二阶矩不等于二阶导数或方差 |
| learning rate / step size | 学习率 / 步长 | 与梯度、有限差分扰动h明确区分 |
| weight / bias | 权重 / 偏置 | 对w、b求导对象与聚合平均保持 |

原文数值、单位和量级表达保持；必要可附中文释义，时间元数据可自然翻译。图/代码/公式载荷原样，裸围栏仅补text。正文裸乘号若破坏GFM，仅做可逆语法转义并记录，不能修正公式或技术意义。原始源风险留在审校记录，最终技术更正须另行决定。
