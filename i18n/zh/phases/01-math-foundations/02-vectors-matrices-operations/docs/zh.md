# 向量、矩阵与运算

> 每个神经网络本质上都是矩阵乘法，再加上一些额外步骤。

**Type:** Build
**Languages:** Python, Julia
**Prerequisites:** 第 1 阶段，第 01 课（线性代数直觉）
**Time:** ~60 分钟

## 学习目标

- 构建一个 Matrix 类，支持逐元素（element-wise）运算、矩阵乘法（matrix multiplication）、转置（transpose）、行列式（determinant）和求逆矩阵（inverse）
- 区分逐元素乘法与矩阵乘法，并解释各自的适用场景
- 仅使用从零实现的 Matrix 类，实现一个神经网络全连接层（dense layer），其计算为 `relu(W @ x + b)`
- 解释广播（broadcasting）规则，以及神经网络框架如何实现偏置（bias）相加

## 要解决的问题

你想构建一个神经网络。阅读代码时，你看到了这样一行：

```text
output = activation(weights @ input + bias)
```

其中的 `@` 表示矩阵乘法。`weights` 是一个矩阵（matrix），`input` 是一个向量（vector）。如果你不知道这些运算的作用，这行代码就像魔法一样；如果你理解了，就会发现它用三次运算完成了一层的整个前向传播（forward pass）。

模型处理的每张图像都是一个像素值矩阵。每个词嵌入（word embedding）都是一个向量。每个神经网络的每一层都是一种矩阵变换。不熟练掌握矩阵运算，就无法构建 AI 系统，正如不理解变量就无法编写代码一样。

本课将带你从零开始，熟练掌握这些运算。

## 核心概念

### 向量：有序的数值列表

向量是一个有方向和模（magnitude）的数值列表。在 AI 中，向量用于表示数据点、特征或参数。

```text
v = [3, 4]        -- a 2D vector
w = [1, 0, -2]    -- a 3D vector
```

2D 向量 `[3, 4]` 指向平面上坐标为 (3, 4) 的位置。它的长度（模）为 5（即 3-4-5 三角形）。

### 矩阵：数值网格

矩阵是一个由行和列组成的 2D 网格。一个 m x n 矩阵有 m 行、n 列。

```text
A = | 1  2  3 |     -- 2x3 matrix (2 rows, 3 columns)
    | 4  5  6 |
```

在神经网络中，权重矩阵将输入向量变换为输出向量。一层若有 784 个输入和 128 个输出，就需要使用一个 128x784 的权重矩阵。

### 为什么形状很重要

矩阵乘法有一条严格的规则：`(m x n) @ (n x p) = (m x p)`。内侧维度（dimension）必须匹配。

```text
(128 x 784) @ (784 x 1) = (128 x 1)
  weights       input       output

Inner dimensions: 784 = 784  -- valid
```

如果你在 PyTorch 中遇到形状（shape）不匹配的错误，原因就在这里。

### 运算概览

| 运算 | 作用 | 在神经网络中的用途 |
|-----------|-------------|-------------------|
| 加法 | 逐元素相加 | 为输出加上偏置 |
| 标量（scalar）乘法 | 缩放每个元素 | 学习率 * 梯度 |
| 矩阵乘法 | 对向量进行变换 | 层的前向传播 |
| 转置 | 交换行和列 | 反向传播（backpropagation） |
| 行列式 | 用一个数概括矩阵 | 检查可逆性 |
| 逆矩阵 | 撤销变换 | 求解线性方程组 |
| 单位矩阵（identity matrix） | 不改变输入的矩阵 | 初始化、残差连接（residual connection） |

### 逐元素乘法与矩阵乘法

初学者经常混淆这两种运算。

逐元素乘法：将对应位置的元素相乘。两个矩阵的形状必须相同。

```text
| 1  2 |   | 5  6 |   | 5  12 |
| 3  4 | * | 7  8 | = | 21 32 |
```

矩阵乘法：计算行与列的点积（dot product）。内侧维度必须匹配。

```text
| 1  2 |   | 5  6 |   | 1*5+2*7  1*6+2*8 |   | 19  22 |
| 3  4 | @ | 7  8 | = | 3*5+4*7  3*6+4*8 | = | 43  50 |
```

运算不同，结果不同，规则也不同。

### 广播

将偏置向量加到输出矩阵上时，两者的形状并不相同。广播会将较小的数组扩展到匹配的形状。

```text
| 1  2  3 |   +   [10, 20, 30]
| 4  5  6 |

Broadcasting stretches the vector across rows:

| 1  2  3 |   | 10  20  30 |   | 11  22  33 |
| 4  5  6 | + | 10  20  30 | = | 14  25  36 |
```

现代框架都会自动完成这一步。理解广播，就不会在形状看似不对、代码却能运行时感到困惑。

```figure
vector-projection
```

## 动手实现

### 第 1 步：Vector 类

```python
class Vector:
    def __init__(self, data):
        self.data = list(data)
        self.size = len(self.data)

    def __repr__(self):
        return f"Vector({self.data})"

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.data, other.data)])

    def __mul__(self, scalar):
        return Vector([x * scalar for x in self.data])

    def dot(self, other):
        return sum(a * b for a, b in zip(self.data, other.data))

    def magnitude(self):
        return sum(x ** 2 for x in self.data) ** 0.5
```

### 第 2 步：实现核心运算的 Matrix 类

```python
class Matrix:
    def __init__(self, data):
        self.data = [list(row) for row in data]
        self.rows = len(self.data)
        self.cols = len(self.data[0])
        self.shape = (self.rows, self.cols)

    def __repr__(self):
        rows_str = "\n  ".join(str(row) for row in self.data)
        return f"Matrix({self.shape}):\n  {rows_str}"

    def __add__(self, other):
        return Matrix([
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def __sub__(self, other):
        return Matrix([
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def scalar_multiply(self, scalar):
        return Matrix([
            [self.data[i][j] * scalar for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def element_wise_multiply(self, other):
        return Matrix([
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def matmul(self, other):
        return Matrix([
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ])

    def transpose(self):
        return Matrix([
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ])

    def determinant(self):
        if self.shape == (1, 1):
            return self.data[0][0]
        if self.shape == (2, 2):
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        det = 0
        for j in range(self.cols):
            minor = Matrix([
                [self.data[i][k] for k in range(self.cols) if k != j]
                for i in range(1, self.rows)
            ])
            det += ((-1) ** j) * self.data[0][j] * minor.determinant()
        return det

    def inverse_2x2(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular, no inverse exists")
        return Matrix([
            [self.data[1][1] / det, -self.data[0][1] / det],
            [-self.data[1][0] / det, self.data[0][0] / det]
        ])

    @staticmethod
    def identity(n):
        return Matrix([
            [1 if i == j else 0 for j in range(n)]
            for i in range(n)
        ])
```

### 第 3 步：查看运行效果

```python
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

print("A + B =", (A + B).data)
print("A @ B =", A.matmul(B).data)
print("A^T =", A.transpose().data)
print("det(A) =", A.determinant())
print("A^-1 =", A.inverse_2x2().data)

I = Matrix.identity(2)
print("A @ A^-1 =", A.matmul(A.inverse_2x2()).data)
```

### 第 4 步：与神经网络联系起来

```python
import random

inputs = Matrix([[0.5], [0.8], [0.2]])
weights = Matrix([
    [random.uniform(-1, 1) for _ in range(3)]
    for _ in range(2)
])
bias = Matrix([[0.1], [0.1]])

def relu_matrix(m):
    return Matrix([[max(0, val) for val in row] for row in m.data])

pre_activation = weights.matmul(inputs) + bias
output = relu_matrix(pre_activation)

print(f"Input shape: {inputs.shape}")
print(f"Weight shape: {weights.shape}")
print(f"Output shape: {output.shape}")
print(f"Output: {output.data}")
```

这就是一个全连接层：`output = relu(W @ x + b)`。每个神经网络中的每个全连接层所做的都是这件事。

## 实际使用

NumPy 能用更少的代码完成上述所有运算，而且速度快几个数量级。

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("A + B =\n", A + B)
print("A * B (element-wise) =\n", A * B)
print("A @ B (matrix multiply) =\n", A @ B)
print("A^T =\n", A.T)
print("det(A) =", np.linalg.det(A))
print("A^-1 =\n", np.linalg.inv(A))
print("I =\n", np.eye(2))

inputs = np.random.randn(3, 1)
weights = np.random.randn(2, 3)
bias = np.array([[0.1], [0.1]])
output = np.maximum(0, weights @ inputs + bias)

print(f"\nNeural network layer: {weights.shape} @ {inputs.shape} = {output.shape}")
print(f"Output:\n{output}")
```

Python 中的 `@` 运算符会调用 `__matmul__`。NumPy 使用以 C 和 Fortran 编写、经过优化的 BLAS 例程来实现它。数学运算相同，速度却是原来的 100x。

NumPy 中的广播：

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
bias = np.array([10, 20, 30])
print(matrix + bias)
```

NumPy 会自动将 1D 偏置向量广播到这两行。所有神经网络框架都是这样实现偏置相加的。

## 交付成果

本课将产出一份提示词（prompt），用于通过几何直觉讲解矩阵运算。参见 `outputs/prompt-matrix-operations.md`。

这里实现的 Matrix 类，是我们将在第 3 阶段第 10 课构建的迷你神经网络框架的基础。

## 练习

1. **验证逆矩阵。** 计算乘积 `A @ A.inverse_2x2()`，确认得到单位矩阵。用三个不同的 2x2 矩阵尝试一下。行列式为零时会发生什么？

2. **实现 3x3 矩阵的求逆。** 扩展 Matrix 类，使用伴随矩阵法（adjugate method）计算 3x3 矩阵的逆矩阵。将结果与 NumPy 的 `np.linalg.inv` 对照测试。

3. **构建一个两层网络。** 仅使用你的 Matrix 类（不使用 NumPy），创建一个两层神经网络：输入 (3) -> 隐藏层 (4) -> 输出 (2)。随机初始化权重，执行一次前向传播，并验证所有形状都正确。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|----------------------|
| 向量 | “一个箭头” | 有序的数值列表。在 AI 中，表示高维空间中的一个点。 |
| 矩阵 | “一张数值表” | 一种线性变换（linear transformation），将向量从一个空间映射到另一个空间。 |
| 矩阵乘法 | “把数字乘起来就行” | 计算第一个矩阵的每一行与第二个矩阵的每一列之间的点积。顺序很重要。 |
| 转置 | “翻转一下” | 交换行与列，将 m x n 矩阵变为 n x m 矩阵。在反向传播中至关重要。 |
| 行列式 | “从矩阵算出的某个数” | 衡量矩阵将面积（2D）或体积（3D）缩放了多少。为零意味着该变换压缩掉了一个维度。 |
| 逆矩阵 | “撤销矩阵的作用” | 能够逆转原变换的矩阵。只有行列式非零时才存在。 |
| 单位矩阵 | “无聊的矩阵” | 相当于矩阵运算中的乘以 1。用于残差连接（ResNets）。 |
| 广播 | “神奇的形状修复” | 沿缺失的维度重复，将较小的数组扩展到与较大数组匹配。 |
| 逐元素 | “普通乘法” | 将对应位置的元素相乘。两个数组的形状必须相同（或满足广播条件）。 |

## 延伸阅读

- [3Blue1Brown：线性代数的本质](https://www.3blue1brown.com/topics/linear-algebra) - 为本课涉及的每种运算建立视觉直觉
- [NumPy 广播文档](https://numpy.org/doc/stable/user/basics.broadcasting.html) - NumPy 遵循的精确规则
- [Stanford CS229 线性代数回顾](http://cs229.stanford.edu/section/cs229-linalg.pdf) - 面向 ML 的线性代数简明参考资料
