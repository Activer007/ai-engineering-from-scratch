# S19 线性方程组术语增量 v1.0

2026-10-02。联用核心及S05–S16固定词表，重点区分方程组相容性、秩与形状、分解因子、残差与参数误差。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| linear system | 线性方程组 | Ax=b求解语境，不泛译线性系统软件 |
| row / column picture | 行视角 / 列视角 | 超平面交集与列向量线性组合不同 |
| consistent / inconsistent | 相容 / 不相容 | 是否有精确解，不等于超定/欠定 |
| overdetermined / underdetermined | 超定 / 欠定 | m与n大小关系，不保证是否有解或解是否唯一 |
| Gaussian elimination | 高斯消元（Gaussian elimination） | 与高斯分布抽样不同 |
| partial pivoting / pivot | 部分选主元 / 主元 | 取列内绝对值最大元素，API与行交换顺序保护 |
| upper / lower triangular | 上三角 / 下三角 | U/L角色与前代/回代一致 |
| forward / back substitution | 前代 / 回代 | 不是神经网络前向/反向传播 |
| LU / QR / Cholesky decomposition | LU / QR / Cholesky分解 | 名称保留；PA=LU与A=LU、LL^T与LL*按源区分 |
| permutation matrix | 置换矩阵 | P表示行交换，不是概率分布P |
| symmetric positive definite / semi-definite | 对称正定 / 对称半正定 | 零特征值与严格正值不同；源泛化单列 |
| orthogonal / orthonormal columns | 正交 / 标准正交列 | 方阵正交矩阵与矩形列标准正交不同 |
| Gram-Schmidt | Gram-Schmidt正交化 | 经典/修正版稳定性需分清，保留专名 |
| least squares / residual | 最小二乘 / 残差 | Ax-b观测空间残差与x参数误差不同 |
| normal equations | 正规方程（normal equations） | 不是正态分布方程；A^TA与A^Tb位置保护 |
| closed-form solution | 闭式解 | 可写表达式不等于推荐显式矩阵求逆 |
| pseudoinverse / Moore-Penrose | 伪逆 / Moore-Penrose伪逆 | SVD零/非零奇异值处理与最小范数条件按源保持 |
| condition number / ill-conditioned | 条件数 / 病态（ill-conditioned） | 问题敏感性不同算法稳定性；sigma比对应2范数条件数 |
| well-conditioned / effectively singular | 良态 / 数值上奇异 | 精确奇异与浮点阈值判定分别记录 |
| ridge regression / regularization | Ridge回归 / 正则化 | lambda I与方差特征值、截距是否惩罚按源，不保证泛化 |
| conjugate gradient / CG | 共轭梯度（CG） | SPD和精确算术n步条件不丢，非任意矩阵通用保证 |
| preconditioning / preconditioner | 预条件化 / 预条件器 | 与概率条件化、先修条件不同 |
| sparse / nnz | 稀疏 / nnz（非零元素数） | 复杂度符号与迭代次数k/n不可交换 |

公式、代码/图载荷、API、路径/链接、数值和原先修标题保护。源表范数竖线的GFM语法问题由协调者处理，源数值/理论错误不以译文默修。
