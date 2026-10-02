# 线性方程组

> 求解 Ax = b 是数学中最古老的问题，至今仍支撑着神经网络的运行。

**Type:** Build
**Language:** Python
**Prerequisites:** 第 1 阶段，第 01 课（Linear Algebra Intuition）、第 02 课（Vectors & Matrices）、第 03 课（Matrix Transformations）
**Time:** ~120 分钟

## 学习目标

- 使用带部分选主元的高斯消元和回代求解 Ax = b
- 用 LU、QR 和 Cholesky 分解对矩阵进行因式分解，并说明各自的适用情形
- 推导最小二乘的正规方程，并说明它们与线性回归、Ridge 回归的联系
- 用条件数诊断病态方程组，并通过正则化使其求解更加稳定

## 要解决的问题

每次训练线性回归模型，你都在求解线性方程组（linear system）。每次进行最小二乘（least squares）拟合，你也在求解线性方程组。每当神经网络层计算 `y = Wx + b`，它就是在计算线性方程组的一侧。加入正则化（regularization）时，你在修改这个方程组。使用高斯过程时，你在分解矩阵。为了计算 Mahalanobis 距离而对协方差矩阵求逆时，你同样在求解线性方程组。

方程 Ax = b 无处不在。A 是由已知系数组成的矩阵，b 是由已知输出组成的向量，x 则是你要找的未知量向量。在线性回归中，A 是数据矩阵，b 是目标向量，x 是权重向量。整个模型可以归结为：找到 x，使 Ax 尽可能接近 b。

本课将从零实现求解这个方程的各种主要方法。你会理解为什么有些方法速度快，而另一些方法稳定；为什么有些方法只适用于系数矩阵为方阵的方程组，而另一些方法可以处理超定（overdetermined）方程组；以及为什么矩阵的条件数（condition number）决定了答案究竟有没有意义。

## 核心概念

### Ax = b 的几何意义

线性方程组可以从几何角度理解。每个方程定义一个超平面，解就是所有超平面相交的点（或点集）。

```text
2x + y = 5          Two lines in 2D.
x - y  = 1          They intersect at x=2, y=1.
```

```mermaid
graph LR
    A["2x + y = 5"] --- S["Solution: (2, 1)"]
    B["x - y = 1"] --- S
```

可能出现三种情况：

```mermaid
graph TD
    subgraph "One Solution"
        A1["Lines intersect at a single point"]
    end
    subgraph "No Solution"
        A2["Lines are parallel — no intersection"]
    end
    subgraph "Infinite Solutions"
        A3["Lines are identical — every point is a solution"]
    end
```

用矩阵来表述，“唯一解”意味着 A 可逆；“无解”意味着方程组不相容（inconsistent）；“无穷多解”意味着 A 有零空间。大多数机器学习（ML）问题属于“没有精确解”这一类，因为方程（数据点）的数量多于未知量（参数）的数量。这时就需要最小二乘。

### 列视角与行视角

Ax = b 可以从两个视角来理解。

**行视角。** A 的每一行定义一个方程，每个方程对应一个超平面，解就是它们共同的交点。

**列视角。** A 的每一列都是一个向量。问题就变成：A 的各列做怎样的线性组合，才能得到 b？

```text
A = | 2  1 |    b = | 5 |
    | 1 -1 |        | 1 |

Row picture: solve 2x + y = 5 and x - y = 1 simultaneously.

Column picture: find x1, x2 such that:
  x1 * [2, 1] + x2 * [1, -1] = [5, 1]
  2 * [2, 1] + 1 * [1, -1] = [4+1, 2-1] = [5, 1]   check.
```

列视角更为根本。如果 b 位于 A 的列空间中，方程组就有解；如果 b 不在其中，就要在列空间中找到距离 b 最近的点。这个最近的点就是最小二乘解。

### 高斯消元

高斯消元（Gaussian elimination）将 Ax = b 化为上三角方程组 Ux = c，再通过回代（back substitution）求解。这是最直接的方法。

算法如下：

```text
1. For each column k (the pivot column):
   a. Find the largest entry in column k at or below row k (partial pivoting).
   b. Swap that row with row k.
   c. For each row i below k:
      - Compute multiplier m = A[i][k] / A[k][k]
      - Subtract m times row k from row i.
2. Back substitute: solve from the last equation upward.
```

示例：

```text
Original:
| 2  1  1 | 8 |       R2 = R2 - (2)R1     | 2  1   1 |  8 |
| 4  3  3 |20 |  -->  R3 = R3 - (1)R1 --> | 0  1   1 |  4 |
| 2  3  1 |12 |                            | 0  2   0 |  4 |

                       R3 = R3 - (2)R2     | 2  1   1 |  8 |
                                       --> | 0  1   1 |  4 |
                                           | 0  0  -2 | -4 |

Back substitute:
  -2 * x3 = -4    -->  x3 = 2
  x2 + 2  = 4     -->  x2 = 2
  2*x1 + 2 + 2 = 8 --> x1 = 2
```

高斯消元需要 O(n^3) 次运算。对于一个 1000x1000 的方程组，这大约需要 billion（十亿）次浮点运算。虽然已经很快，但如果需要求解多个 A 相同的方程组，还有更好的方法。

### 部分选主元：为什么重要

不进行选主元操作，高斯消元可能失败，或者给出毫无意义的结果。如果主元为零，就会出现除以零；如果主元很小，就会放大舍入误差。

```text
Bad pivot:                       With partial pivoting:
| 0.001  1 | 1.001 |            Swap rows first:
| 1      1 | 2     |            | 1      1 | 2     |
                                 | 0.001  1 | 1.001 |
m = 1/0.001 = 1000              m = 0.001/1 = 0.001
R2 = R2 - 1000*R1               R2 = R2 - 0.001*R1
| 0.001  1     | 1.001   |      | 1      1     | 2     |
| 0     -999   | -999.0  |      | 0      0.999 | 0.999 |

x2 = 1.000 (correct)            x2 = 1.000 (correct)
x1 = (1.001 - 1)/0.001          x1 = (2 - 1)/1 = 1.000 (correct)
   = 0.001/0.001 = 1.000        Stable because the multiplier is small.
```

在精度有限的浮点运算中，不选主元的版本可能损失有效数字。部分选主元（partial pivoting）总是选择当前可用的最大主元，以尽量减小误差的放大。

### LU 分解

LU 分解将 A 分解为一个下三角矩阵 L 和一个上三角矩阵 U：A = LU。L 存储高斯消元中使用的乘数，U 则是消元后的矩阵。

```text
A = L @ U

| 2  1  1 |   | 1  0  0 |   | 2  1   1 |
| 4  3  3 | = | 2  1  0 | @ | 0  1   1 |
| 2  3  1 |   | 1  2  1 |   | 0  0  -2 |
```

为什么要做分解，而不只是消元？因为一旦得到 L 和 U，对于任意新的 b，求解 Ax = b 都只需要 O(n^2) 的计算量：

```text
Ax = b
LUx = b
Let y = Ux:
  Ly = b    (forward substitution, O(n^2))
  Ux = y    (back substitution, O(n^2))
```

O(n^3) 的计算代价只需在分解时付出一次，之后每次求解的代价都是 O(n^2)。如果需要求解 1000 个 A 相同、b 向量不同的方程组，LU 可以让总计算量缩减 1000/3 倍。

加入部分选主元后，得到的是 PA = LU，其中 P 是记录行交换的置换矩阵。

### QR 分解

QR 分解将 A 分解为一个正交矩阵 Q 和一个上三角矩阵 R：A = QR。

正交矩阵满足 Q^T Q = I，它的各列是标准正交向量。乘以 Q 会保持长度和夹角不变。

```text
A = Q @ R

Q has orthonormal columns: Q^T Q = I
R is upper triangular

To solve Ax = b:
  QRx = b
  Rx = Q^T b    (just multiply by Q^T, no inversion needed)
  Back substitute to get x.
```

在求解最小二乘问题时，QR 在数值上比 LU 更稳定。Gram-Schmidt 正交化逐列构造 Q：

```text
Given columns a1, a2, ... of A:

q1 = a1 / ||a1||

q2 = a2 - (a2 . q1) * q1        (subtract projection onto q1)
q2 = q2 / ||q2||                (normalize)

q3 = a3 - (a3 . q1) * q1 - (a3 . q2) * q2
q3 = q3 / ||q3||

R[i][j] = qi . aj    for i <= j
```

每一步都会去掉沿所有已有 q 向量方向的分量，只留下新的正交方向。

### Cholesky 分解

当 A 对称（A = A^T）且正定（所有特征值均为正）时，可以将它分解为 A = L L^T，其中 L 为下三角矩阵。这就是 Cholesky 分解。

```text
A = L @ L^T

| 4  2 |   | 2  0 |   | 2  1 |
| 2  5 | = | 1  2 | @ | 0  2 |

L[i][i] = sqrt(A[i][i] - sum(L[i][k]^2 for k < i))
L[i][j] = (A[i][j] - sum(L[i][k]*L[j][k] for k < j)) / L[j][j]    for i > j
```

Cholesky 的速度是 LU 的两倍，所需存储空间只有一半。它只适用于对称正定矩阵，但这类矩阵经常出现：

- 协方差矩阵是对称半正定的（正则化后为正定）。
- 高斯过程中的核矩阵是对称正定的。
- 凸函数在极小值点的 Hessian 矩阵（海森矩阵）是对称正定的。
- A^T A 总是对称半正定的。

在高斯过程中，先用 Cholesky 分解核矩阵 K，再求解 K alpha = y，得到预测均值。Cholesky 因子还可以给出计算边际似然所需的对数行列式：log det(K) = 2 * sum(log(diag(L)))。

### 最小二乘：当 Ax = b 没有精确解时

如果 A 的形状为 m x n，且 m > n（方程数多于未知量数），方程组就是超定的，不存在精确解。此时，转而最小化平方误差：

```text
minimize ||Ax - b||^2

This is the sum of squared residuals:
  sum((A[i,:] @ x - b[i])^2 for i in range(m))
```

使平方误差最小的解满足正规方程（normal equations）：

```text
A^T A x = A^T b
```

推导：展开 ||Ax - b||^2 = (Ax - b)^T (Ax - b) = x^T A^T A x - 2 x^T A^T b + b^T b。对 x 求梯度，并令其为零：2 A^T A x - 2 A^T b = 0。

```text
Original system (overdetermined, 4 equations, 2 unknowns):
| 1  1 |         | 3 |
| 1  2 | x     = | 5 |       No exact x satisfies all 4 equations.
| 1  3 |         | 6 |
| 1  4 |         | 8 |

Normal equations:
A^T A = | 4  10 |    A^T b = | 22 |
        | 10 30 |            | 63 |

Solve: x = [1.5, 1.7]

This is linear regression. x[0] is the intercept, x[1] is the slope.
```

### 正规方程 = 线性回归

两者之间是精确的对应关系。在线性回归中，数据矩阵 X 的每一行对应一个样本，每一列对应一个特征；目标向量 y 中，每个样本对应一个元素。权重向量 w 满足：

```text
X^T X w = X^T y
w = (X^T X)^(-1) X^T y
```

这就是线性回归的闭式解（closed-form solution）。每次调用 `sklearn.linear_model.LinearRegression.fit()`，都会计算这个解，或通过 QR、奇异值分解（SVD）得到等价的解。

在矩阵上加上正则化项 lambda * I，就得到 Ridge 回归：

```text
(X^T X + lambda * I) w = X^T y
w = (X^T X + lambda * I)^(-1) X^T y
```

正则化使矩阵的条件状况更好（更容易准确求逆），并通过将权重向零收缩来防止过拟合。当 lambda > 0 时，矩阵 X^T X + lambda * I 总是对称正定的，因此可以用 Cholesky 分解来求解。

### 伪逆（Moore-Penrose）

伪逆（pseudoinverse）A+ 将矩阵求逆推广到非方阵和奇异矩阵。对于任意矩阵 A：

```text
x = A+ b

where A+ = V Sigma+ U^T    (computed via SVD)
```

将每个非零奇异值取倒数，再将所得矩阵转置，就得到 Sigma+。如果 A = U Sigma V^T，那么 A+ = V Sigma+ U^T。

```text
A = U Sigma V^T        (SVD)

Sigma = | 5  0 |       Sigma+ = | 1/5  0  0 |
        | 0  2 |                | 0  1/2  0 |
        | 0  0 |

A+ = V Sigma+ U^T
```

伪逆给出范数最小的最小二乘解。根据方程组解的情况：
- 唯一解：A+ b 给出这个解。
- 无解：A+ b 给出最小二乘解。
- 无穷多解：A+ b 给出其中 ||x|| 最小的解。

NumPy 的 `np.linalg.lstsq` 和 `np.linalg.pinv` 内部都使用 SVD。

### 条件数

条件数衡量解对输入微小变化的敏感程度。对于矩阵 A，条件数为：

```text
kappa(A) = ||A|| * ||A^(-1)|| = sigma_max / sigma_min
```

其中，sigma_max 和 sigma_min 分别是最大和最小奇异值。

```text
Well-conditioned (kappa ~ 1):        Ill-conditioned (kappa ~ 10^15):
Small change in b -->                Small change in b -->
small change in x                    huge change in x

| 2  0 |   kappa = 2/1 = 2          | 1   1          |   kappa ~ 10^15
| 0  1 |   safe to solve            | 1   1+10^(-15) |   solution is garbage
```

经验法则：
- kappa < 100：可以放心求解，解是准确的。
- kappa ~ 10^k：浮点运算大约会损失 k 位精度。
- kappa ~ 10^16（对于 float64）：解没有意义，矩阵在数值上已经是奇异的。

在 ML 中，特征近乎共线时就会出现病态（ill-conditioned）问题。正则化（加上 lambda * I）会将条件数从 sigma_max / sigma_min 改善为 (sigma_max + lambda) / (sigma_min + lambda)。

### 迭代方法：共轭梯度

对于规模极大的稀疏方程组（未知量达到 millions，即数百万），LU 或 Cholesky 这样的直接法代价过高。迭代方法通过多次迭代不断改进初始估计，来逼近解。

当 A 对称正定时，共轭梯度（conjugate gradient，CG）可以求解 Ax = b。在精确算术下，它最多经过 n 次迭代就能找到精确解；但如果 A 的特征值聚集在一起，通常会更快收敛。

```text
Algorithm sketch:
  x0 = initial guess (often zero)
  r0 = b - A x0           (residual)
  p0 = r0                 (search direction)

  For k = 0, 1, 2, ...:
    alpha = (rk . rk) / (pk . A pk)
    x_{k+1} = xk + alpha * pk
    r_{k+1} = rk - alpha * A pk
    beta = (r_{k+1} . r_{k+1}) / (rk . rk)
    p_{k+1} = r_{k+1} + beta * pk
    if ||r_{k+1}|| < tolerance: stop
```

CG 用于：
- 大规模优化（Newton-CG 方法）
- 求解偏微分方程（PDE）离散化后得到的方程组
- 核矩阵过大、难以分解的核方法
- 为其他迭代求解器进行预条件化（preconditioning）

收敛速度取决于条件数。条件状况更好的方程组收敛更快，这也是正则化有帮助的另一个原因。

### 总览：何时使用哪种方法

| 方法 | 要求 | 代价 | 适用场景 |
|--------|-------------|------|----------|
| 高斯消元 | A 为非奇异方阵 | O(n^3) | 对系数矩阵为方阵的方程组进行一次性求解 |
| LU 分解 | A 为非奇异方阵 | 分解 O(n^3) + 求解 O(n^2) | 多次求解 A 相同的方程组 |
| QR 分解 | 任意 A（m >= n） | O(mn^2) | 最小二乘，数值稳定 |
| Cholesky | A 对称正定 | O(n^3/3) | 协方差矩阵、高斯过程、Ridge 回归 |
| 正规方程 | 超定（m > n） | O(mn^2 + n^3) | 线性回归（n 较小） |
| SVD / 伪逆 | 任意 A | O(mn^2) | 秩亏方程组、最小范数解 |
| 共轭梯度 | A 对称正定且稀疏 | O(n * k * nnz) | 大型稀疏方程组，k = 迭代次数 |

### 与 ML 的联系

本课的每一种方法都出现在生产环境中的 ML 应用里：

**线性回归。** 闭式解通过求解正规方程 X^T X w = X^T y 得到。可以使用 Cholesky（n 较小时）、QR（重视数值稳定性时）或 SVD（矩阵可能秩亏时）来求解。

**Ridge 回归。** 在 X^T X 上加上 lambda * I。正则化后的方程组 (X^T X + lambda * I) w = X^T y 总能通过 Cholesky 分解求解，因为当 lambda > 0 时，X^T X + lambda * I 是对称正定的。

**高斯过程。** 求预测均值需要求解 K alpha = y，其中 K 是核矩阵。对 K 做 Cholesky 分解是标准方法。对数边际似然的计算会用到 log det(K) = 2 sum(log(diag(L)))。

**神经网络初始化。** 正交初始化通过 QR 分解构造列向量标准正交的权重矩阵。这可以防止深层网络中的信号坍缩。

**预条件化。** 大规模优化器使用不完全 Cholesky 分解或不完全 LU 分解，作为共轭梯度求解器的预条件器。

**特征工程。** X^T X 的条件数可以告诉你特征是否共线。如果 kappa 很大，就去掉一些特征或加入正则化。

```figure
linear-system-conditioning
```

## 动手实现

### 第 1 步：带部分选主元的高斯消元

```python
import numpy as np

def gaussian_elimination(A, b):
    n = len(b)
    Ab = np.hstack([A.astype(float), b.reshape(-1, 1).astype(float)])

    for k in range(n):
        max_row = k + np.argmax(np.abs(Ab[k:, k]))
        Ab[[k, max_row]] = Ab[[max_row, k]]

        if abs(Ab[k, k]) < 1e-12:
            raise ValueError(f"Matrix is singular or nearly singular at pivot {k}")

        for i in range(k + 1, n):
            m = Ab[i, k] / Ab[k, k]
            Ab[i, k:] -= m * Ab[k, k:]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - Ab[i, i+1:n] @ x[i+1:n]) / Ab[i, i]

    return x
```

### 第 2 步：LU 分解

```python
def lu_decompose(A):
    n = A.shape[0]
    L = np.eye(n)
    U = A.astype(float).copy()
    P = np.eye(n)

    for k in range(n):
        max_row = k + np.argmax(np.abs(U[k:, k]))
        if max_row != k:
            U[[k, max_row]] = U[[max_row, k]]
            P[[k, max_row]] = P[[max_row, k]]
            if k > 0:
                L[[k, max_row], :k] = L[[max_row, k], :k]

        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]

    return P, L, U

def lu_solve(P, L, U, b):
    n = len(b)
    Pb = P @ b.astype(float)

    y = np.zeros(n)
    for i in range(n):
        y[i] = Pb[i] - L[i, :i] @ y[:i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - U[i, i+1:] @ x[i+1:]) / U[i, i]

    return x
```

### 第 3 步：Cholesky 分解

```python
def cholesky(A):
    n = A.shape[0]
    L = np.zeros_like(A, dtype=float)

    for i in range(n):
        for j in range(i + 1):
            s = A[i, j] - L[i, :j] @ L[j, :j]
            if i == j:
                if s <= 0:
                    raise ValueError("Matrix is not positive definite")
                L[i, j] = np.sqrt(s)
            else:
                L[i, j] = s / L[j, j]

    return L
```

### 第 4 步：通过正规方程求解最小二乘

```python
def least_squares_normal(A, b):
    AtA = A.T @ A
    Atb = A.T @ b
    return gaussian_elimination(AtA, Atb)

def ridge_regression(A, b, lam):
    n = A.shape[1]
    AtA = A.T @ A + lam * np.eye(n)
    Atb = A.T @ b
    L = cholesky(AtA)
    y = np.zeros(n)
    for i in range(n):
        y[i] = (Atb[i] - L[i, :i] @ y[:i]) / L[i, i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - L.T[i, i+1:] @ x[i+1:]) / L.T[i, i]
    return x
```

### 第 5 步：条件数

```python
def condition_number(A):
    U, S, Vt = np.linalg.svd(A)
    return S[0] / S[-1]
```

## 实际使用

把这些组件组合起来，在真实数据上进行线性回归和 Ridge 回归：

```python
np.random.seed(42)
X_raw = np.random.randn(100, 3)
w_true = np.array([2.0, -1.0, 0.5])
y = X_raw @ w_true + np.random.randn(100) * 0.1

X = np.column_stack([np.ones(100), X_raw])

w_ols = least_squares_normal(X, y)
print(f"OLS weights (ours):    {w_ols}")

w_np = np.linalg.lstsq(X, y, rcond=None)[0]
print(f"OLS weights (numpy):   {w_np}")
print(f"Max difference: {np.max(np.abs(w_ols - w_np)):.2e}")

w_ridge = ridge_regression(X, y, lam=1.0)
print(f"Ridge weights (ours):  {w_ridge}")

from sklearn.linear_model import Ridge
ridge_sk = Ridge(alpha=1.0, fit_intercept=False)
ridge_sk.fit(X, y)
print(f"Ridge weights (sklearn): {ridge_sk.coef_}")
```

## 交付成果

本课将产出：
- `code/linear_systems.py`，包含从零实现的高斯消元、LU 分解、Cholesky 分解、最小二乘和 Ridge 回归
- 一个可运行的演示，展示正规方程与 sklearn 的 LinearRegression 得到相同的权重

## 练习

1. 分别使用自己实现的高斯消元、LU 求解器和 `np.linalg.solve`，求解方程组 `[[1,2,3],[4,5,6],[7,8,10]] x = [6, 15, 27]`。验证三种方法在浮点容差范围内给出相同答案。

2. 生成一个 50x5 的随机矩阵 X，以及目标 y = X @ w_true + noise。分别用正规方程、QR（通过 `np.linalg.qr`）、SVD（通过 `np.linalg.svd`）和 `np.linalg.lstsq` 求解 w，比较这四个解。测量 X^T X 的条件数，并解释它如何影响你对各方法的信任程度。

3. 让两列几乎完全相同，构造一个近乎奇异的矩阵（例如，第 2 列 = 第 1 列 + 1e-10 * noise）。计算它的条件数。分别在不使用正则化和使用正则化（加上 0.01 * I）的情况下求解 Ax = b。比较解与残差（residual），解释正则化为什么有帮助。

4. 为一个 100x100 的随机对称正定矩阵实现共轭梯度算法。统计它收敛到容差 1e-8 所需的迭代次数，并与理论上限 n 次迭代比较。

5. 在大小为 10、50、200、500 的对称正定矩阵上，测量自己实现的 Cholesky 求解器、LU 求解器和 `np.linalg.solve` 的运行时间。将结果绘图，验证 Cholesky 的速度大约是 LU 的 2x（两倍）。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|----------------------|
| 线性方程组 | “求 x” | 一组线性方程 Ax = b。求 x 就是找到一个输入，使它经过变换 A 后产生输出 b。 |
| 高斯消元 | “做行消元” | 通过行操作，系统地把对角线下方的元素变为零，得到可用回代求解的上三角方程组。O(n^3)。 |
| 部分选主元 | “交换行以提高稳定性” | 在第 k 列消元前，将该列中绝对值最大的元素所在行交换到主元位置，防止除以很小的数。 |
| LU 分解 | “分解成三角矩阵” | 写成 A = LU，其中 L 为下三角矩阵（存储乘数），U 为上三角矩阵（消元后的矩阵）。把 O(n^3) 的代价分摊到多次求解中。 |
| QR 分解 | “正交分解” | 写成 A = QR，其中 Q 的各列标准正交，R 为上三角矩阵。求解最小二乘时比 LU 更稳定。 |
| Cholesky 分解 | “矩阵的平方根” | 对于对称正定矩阵 A，写成 A = LL^T。代价为 LU 的一半，用于协方差矩阵、核矩阵和 Ridge 回归。 |
| 最小二乘 | “没有精确解时的最佳拟合” | 当方程组超定（方程数多于未知量数）时，最小化残差平方和 \|\|Ax - b\|\|^2。 |
| 正规方程 | “微积分的捷径” | A^T A x = A^T b。令 \|\|Ax - b\|\|^2 的梯度为零。这正是线性回归的闭式解。 |
| 伪逆 | “非方阵也能求逆” | 通过 SVD 得到 A+ = V Sigma+ U^T。无论矩阵是方阵还是矩形矩阵、奇异还是非奇异，都能给出最小范数的最小二乘解。 |
| 条件数 | “这个答案有多可信” | kappa = sigma_max / sigma_min。衡量对输入扰动的敏感程度，大约损失 log10(kappa) 位精度。 |
| Ridge 回归 | “正则化的最小二乘” | 求解 (X^T X + lambda I) w = X^T y。加上 lambda I 可以改善条件状况，并将权重向零收缩，防止过拟合。 |
| 共轭梯度 | “为大矩阵迭代求解 Ax=b” | 用于对称正定方程组的迭代求解器，最多 n 步收敛。当分解代价过高时，适合用来求解大型稀疏方程组。 |
| 超定方程组 | “数据比参数多” | 在 m-by-n 方程组中，m > n。不存在精确解，最小二乘寻找最佳近似。这涵盖了每一个回归问题。 |
| 回代 | “从下往上求解” | 给定上三角方程组，先解最后一个方程，再向上逐步代入。O(n^2)。 |
| 前代 | “从上往下求解” | 给定下三角方程组，先解第一个方程，再向下逐步代入。O(n^2)。用于 LU 求解中的 L 这一步。 |

## 延伸阅读

- [MIT 18.06: Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)（Gilbert Strang）—— 讲解线性方程组与矩阵分解的权威课程
- [Numerical Linear Algebra](https://people.maths.ox.ac.uk/trefethen/text.html)（Trefethen & Bau）—— 理解数值稳定性、条件状况以及算法为何失效的标准参考书
- [Matrix Computations](https://www.press.jhu.edu/books/title/10678/matrix-computations)（Golub & Van Loan）—— 囊括各种矩阵算法的百科全书式参考书
- [3Blue1Brown: Inverse Matrices](https://www.3blue1brown.com/lessons/inverse-matrices) —— 直观理解求解 Ax = b 的几何意义
