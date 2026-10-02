# S20 凸优化术语增量 v1.0

2026-10-02。联用核心及S05–S18词表。凸/严格凸、局部/全局极小值、存在性/唯一性及平稳/最优性分别处理，不用译文为源补上未声明的数学条件。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| convex / non-convex / concave | 凸 / 非凸 / 凹 | 普通凸不等于严格凸或强凸；凹也不等于所有非凸 |
| convex set / convex function | 凸集 / 凸函数 | 集合线段与函数图像线段判据分开，定义域凸性条件保留 |
| halfspace / intersection / union | 半空间 / 交集 / 并集 | 任意交保持凸，不得误改为任意并保持凸 |
| local / global minimum | 局部 / 全局极小值 | 沿用S07/S11，点或函数值按语境补“点”以说明 |
| feasible region / constraint | 可行域 / 约束 | 可行不代表最优，等式/不等式方向原样 |
| positive semidefinite / definite | 半正定 / 正定 | 沿用S07/S13，零特征值允许；源必要条件不能强化 |
| Newton's method | Newton法（牛顿法） | 逆Hessian与梯度次序保留；步长及局部收敛条件另记 |
| quadratic convergence / approximation | 二次收敛 / 二次近似 | 误差收敛阶与二次模型分开，不泛称二阶精度 |
| condition number | 条件数（condition number） | 本课SPD Hessian最大/最小特征值比；一般矩阵条件数定义更广 |
| Lagrange multiplier / Lagrangian | Lagrange乘子 / Lagrange函数 | 专名英文保留，lambda是乘子不是学习率；不可暗改为单纯无约束极小化 |
| Karush-Kuhn-Tucker / KKT | Karush-Kuhn-Tucker（KKT）条件 | 原缩写/人名保持；约束资格条件不足单列 |
| stationarity / feasibility | 驻点条件 / 可行性 | 一阶导数为零不同于已证明极小值，原始/对偶角色保持 |
| active constraint | 活跃约束（active constraint） | g_i=0的边界约束；乘子>0蕴含活跃但反向不总成立 |
| complementary slackness | 互补松弛（complementary slackness） | lambda_i*g_i=0，二者可都为零，不能译成严格二选一 |
| primal / dual / duality | 原始问题 / 对偶问题 / 对偶性 | 原始最小化、对偶最大化及下界方向不可反转 |
| strong duality / Slater's condition | 强对偶 / Slater条件 | 最优值相等需相应条件，普通凸性不单独保证 |
| kernel trick / support vector | 核技巧 / 支持向量 | 数学核不是系统/GPU内核，SVM对偶和active源简化另记 |
| L-BFGS / Fisher information | L-BFGS / Fisher信息 | 沿用S07/S11，Hessian与梯度二阶矩不混同；源错误仍保持 |
| natural gradient / Hessian-free | 自然梯度 / 无Hessian优化 | 不显式形成Hessian不代表不使用曲率；矩阵向量积原样 |
| conjugate gradient / Kronecker product | 共轭梯度 / Kronecker积 | 算法和矩阵运算，不是贝叶斯共轭先验 |
| overparameterization | 过参数化（overparameterization） | 源定义参数多于训练样本；不保证任意损失几何更好 |
| sharp / flat minima | 尖锐 / 平坦极小值 | 沿用S11；与泛化关系依参数化，源概括单列 |

Adam二阶矩、Fisher期望Hessian的符号、K-FAC复杂度、GD/Newton收敛与唯一解保证等按英文忠实保留并单列source风险，不静默纠正。million等量级原文保留并可附中文说明，百分比/数值/公式/API/链接/代码与Mermaid/figure载荷保护。
