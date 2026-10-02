# 数值稳定性

> 浮点数这种抽象并不能完全掩盖底层细节。训练时，它会在你毫无防备的情况下让你栽跟头。

**Type:** Build
**Language:** Python
**Prerequisites:** 阶段 1，第 01-04 课
**Time:** ~120 分钟

## 学习目标

- 用减去最大值的技巧，实现数值稳定的 softmax 和 log-sum-exp
- 识别浮点计算中的上溢（overflow）、下溢（underflow）和灾难性消去（catastrophic cancellation）
- 用中心有限差分计算数值梯度，以此验证解析梯度
- 解释训练时为何更倾向于使用 bfloat16 而非 float16，以及损失缩放（loss scaling）如何防止梯度下溢

## 要解决的问题

模型训练了三个小时，损失突然变成 NaN。你加了一条打印语句。第 9,000 步时，logits（未归一化分数）还正常；到第 9,001 步，它们就变成了 `inf`。到了第 9,002 步，每个梯度都是 `nan`，训练彻底停摆。

或者，模型顺利训练完了，准确率却比论文声称的低 2%。你逐一排查：架构一致，超参数一致，数据也一致。问题在于，论文用了 float32，而你用了 float16，却没有做适当的缩放。三十二位的累积舍入误差，悄悄蚕食了准确率。

又或者，你从零实现了交叉熵损失。logits 较小时它运行正常，一旦 logits 超过 100，就返回 `inf`。这是 softmax 发生了上溢，因为 `exp(100)` 超出了 float32 的表示范围。每个机器学习（ML）框架都会用一个两行代码的技巧处理这种情况，而你此前根本不知道有这个技巧。

数值稳定性不只是理论上的问题。它决定了一次训练是成功完成，还是悄无声息地失败。你最终会发现，每一个严重的 ML bug，追根溯源都与浮点数有关。

## 核心概念

### IEEE 754：计算机如何存储实数

计算机遵循 IEEE 754 标准，以浮点数（floating point）的形式存储实数。一个浮点数由三部分组成：符号位（sign bit）、指数（exponent）和尾数（mantissa，也称 significand）。

```text
Float32 layout (32 bits total):
[1 sign] [8 exponent] [23 mantissa]

Value = (-1)^sign * 2^(exponent - 127) * 1.mantissa
```

尾数决定精度，也就是能保留多少位有效数字。指数决定范围，也就是能表示多大或多小的数。

```text
Format     Bits   Exponent  Mantissa  Decimal digits  Range (approx)
float64    64     11        52        ~15-16          +/- 1.8e308
float32    32     8         23        ~7-8            +/- 3.4e38
float16    16     5         10        ~3-4            +/- 65,504
bfloat16   16     8         7         ~2-3            +/- 3.4e38
```

float32 大约提供 7 位十进制有效数字的精度。也就是说，它能区分 1.0000001 和 1.0000002，却不能区分 1.00000001 和 1.00000002。超过 7 位之后，剩下的都是舍入噪声。

float16 大约只有 3 位有效数字，能表示的最大数是 65,504。对 ML 来说，这个上限小得令人不安，因为 logits、梯度和激活值经常会超过它。

bfloat16 是 Google 针对 float16 表示范围不足给出的方案。它的指数与 float32 一样占 8 位，因此范围也一样，上限可达 3.4e38；但尾数只有 7 位，精度低于 float16。训练神经网络时，表示范围比精度更重要，所以 bfloat16 通常更占优势。

### 为什么 0.1 + 0.2 != 0.3

二进制浮点数无法精确表示 0.1。在以 2 为底的数制中，它是一个循环小数：

```text
0.1 in binary = 0.0001100110011001100110011... (repeating forever)
```

Float32 将它截断为 23 位尾数，存储的值约为 0.100000001490116。同样，0.2 存储的值约为 0.200000002980232。两者之和是 0.300000004470348，而不是 0.3。

```text
In Python:
>>> 0.1 + 0.2
0.30000000000000004

>>> 0.1 + 0.2 == 0.3
False
```

这对 ML 很重要，因为：

1. 像 `if loss < threshold` 这样的损失比较，可能得出错误结果
2. 大量小数值的累加，例如数千步中的梯度更新，会偏离真实的总和
3. 如果用 `==` 比较浮点数，校验和检查与可复现性测试就可能失败

解决办法：永远不要用 `==` 比较浮点数。应使用 `abs(a - b) < epsilon` 或 `math.isclose()`。

### 灾难性消去

两个非常接近的浮点数相减时，有效数字会相互抵消，剩下的舍入噪声便成了结果的高位数字。

```text
a = 1.0000001    (stored as 1.00000011920929 in float32)
b = 1.0000000    (stored as 1.00000000000000 in float32)

True difference:  0.0000001
Computed:         0.00000011920929

Relative error: 19.2%
```

仅仅做了一次减法，相对误差就达到 19%。在 ML 中，以下操作都会遇到这种情况：

- 计算均值很大的数据的方差：当 E[x] 很大时，使用 `E[x^2] - E[x]^2`
- 将非常接近的对数概率相减
- 用过小的 epsilon 计算有限差分梯度

解决办法：改写公式，避免让两个很大且非常接近的数相减。计算方差时，使用 Welford 算法，或先将数据中心化；处理对数概率时，则始终在对数域中计算。

### 上溢与下溢

结果大到无法表示时，就会发生上溢。结果太小，也就是比最小可表示正数更接近零时，则会发生下溢。

```text
Float32 boundaries:
  Maximum:  3.4028235e+38
  Minimum positive (normal): 1.175e-38
  Minimum positive (denorm): 1.401e-45
  Overflow:  anything > 3.4e38 becomes inf
  Underflow: anything < 1.4e-45 becomes 0.0
```

在 ML 中，`exp()` 函数是上溢的主要来源：

```text
exp(88.7)  = 3.40e+38   (barely fits in float32)
exp(89.0)  = inf         (overflow)
exp(-87.3) = 1.18e-38   (barely above underflow)
exp(-104)  = 0.0         (underflow to zero)
```

`log()` 函数则会在另一个方向上出问题：

```text
log(0.0)   = -inf
log(-1.0)  = nan
log(1e-45) = -103.3      (fine)
log(1e-46) = -inf        (input underflowed to 0, then log(0) = -inf)
```

在 ML 中，softmax、sigmoid 和概率计算都会用到 `exp()`。交叉熵、对数似然和 KL 散度中则会用到 `log()`。如果没有合适的技巧，`log(exp(x))` 这样的组合就像一片雷区。

### log-sum-exp 技巧

直接计算 `log(sum(exp(x_i)))` 在数值上很危险。只要有一个 `x_i` 很大，`exp(x_i)` 就会上溢。如果所有 `x_i` 都是绝对值很大的负数，那么每个 `exp(x_i)` 都会下溢为零，而 `log(0)` 就是 `-inf`。

技巧是：先减去最大值，再计算指数。

```text
log(sum(exp(x_i))) = max(x) + log(sum(exp(x_i - max(x))))
```

它之所以有效，是因为减去 `max(x)` 后，最大的指数运算结果为 `exp(0) = 1`，不可能发生上溢。求和的项中至少有一项为 1，因此总和至少为 1，而 `log(1) = 0`，所以也不可能下溢到 `-inf`。

证明如下：

```text
log(sum(exp(x_i)))
= log(sum(exp(x_i - c + c)))                    (add and subtract c)
= log(sum(exp(x_i - c) * exp(c)))               (exp(a+b) = exp(a)*exp(b))
= log(exp(c) * sum(exp(x_i - c)))               (factor out exp(c))
= c + log(sum(exp(x_i - c)))                    (log(a*b) = log(a) + log(b))
```

令 `c = max(x)`，就能消除上溢。

这个技巧在 ML 中随处可见：
- softmax 归一化
- 交叉熵损失计算
- 序列模型中的对数概率求和
- 混合高斯模型
- 变分推断

### 为什么 softmax 需要减去最大值

softmax 将 logits 转换为概率：

```text
softmax(x_i) = exp(x_i) / sum(exp(x_j))
```

不用这个技巧时，[100, 101, 102] 这样的 logits 会导致上溢：

```text
exp(100) = 2.69e43
exp(101) = 7.31e43
exp(102) = 1.99e44
sum      = 2.99e44

These overflow float32 (max ~3.4e38)? No, 2.69e43 < 3.4e38? Actually:
exp(88.7) is already at the float32 limit.
exp(100) = inf in float32.
```

使用这个技巧，减去 max(x) = 102：

```text
exp(100 - 102) = exp(-2) = 0.135
exp(101 - 102) = exp(-1) = 0.368
exp(102 - 102) = exp(0)  = 1.000
sum = 1.503

softmax = [0.090, 0.245, 0.665]
```

概率完全相同，计算也变得安全。这不是性能优化，而是保证正确性所必需的。

### NaN 和 Inf：检测与预防

`nan`（Not a Number，非数）和 `inf`（infinity，无穷大）会像病毒一样在计算中传播。梯度更新中只要有一个 `nan`，权重就会变成 `nan`，之后的每个输出也都会是 `nan`。只需一步，训练就会停摆。

`inf` 是如何出现的：
- 对很大的正数计算 `exp()`
- 除以零：`1.0 / 0.0`
- 使用 `float32` 累加时发生上溢

`nan` 是如何出现的：
- `0.0 / 0.0`
- `inf - inf`
- `inf * 0`
- 对负数计算 `sqrt()`
- 对负数计算 `log()`
- 任何涉及已有 `nan` 的算术运算

检测方法：

```python
import math

math.isnan(x)       # True if x is nan
math.isinf(x)       # True if x is +inf or -inf
math.isfinite(x)    # True if x is neither nan nor inf
```

预防策略：

1. 将 `exp()` 的输入限制在指定区间：`exp(clamp(x, -80, 80))`
2. 在分母中加上 epsilon：`x / (y + 1e-8)`
3. 在 `log()` 内部加上 epsilon：`log(x + 1e-8)`
4. 使用数值稳定的实现，例如 log-sum-exp 和稳定版 softmax
5. 通过梯度裁剪防止权重爆炸
6. 调试时，在每次前向传播后检查是否出现 `nan`/`inf`

### 数值梯度检查

通过反向传播计算解析梯度的实现可能有 bug。数值梯度检查（gradient checking）会用有限差分计算梯度，再以此验证解析梯度。

中心差分公式如下：

```text
df/dx ~= (f(x + h) - f(x - h)) / (2h)
```

它的精度为 O(h^2)，远好于只有 O(h) 精度的前向差分 `(f(x+h) - f(x)) / h`。

选择 h 时，取值过大会导致近似不准确；取值过小，灾难性消去又会破坏结果。常见的取值范围是 `h = 1e-5` 到 `1e-7`。

检查方法：计算解析梯度与数值梯度之间的相对差异。

```text
relative_error = |grad_analytical - grad_numerical| / max(|grad_analytical|, |grad_numerical|, 1e-8)
```

经验判断标准：
- relative_error < 1e-7：非常理想，梯度正确
- relative_error < 1e-5：可以接受，梯度很可能正确
- relative_error > 1e-3：存在问题
- relative_error > 1：梯度完全错误

实现新的层或损失函数时，务必检查梯度。PyTorch 为此提供了 `torch.autograd.gradcheck()`。

### 混合精度训练

现代 GPU 配备了专用硬件 Tensor Cores，进行 float16 矩阵乘法时，速度可达 float32 的 2-8 倍。混合精度训练（mixed precision training）利用的就是这一点：

```text
1. Maintain float32 master copy of weights
2. Forward pass in float16 (fast)
3. Compute loss in float32 (prevents overflow)
4. Backward pass in float16 (fast)
5. Scale gradients to float32
6. Update float32 master weights
```

纯 float16 训练的问题在于，梯度往往很小，为 1e-8 或更小。Float16 会将低于 ~6e-8 的值全部下溢为零。所有梯度更新都变成零后，模型就不再学习了。

解决办法是损失缩放：

```text
1. Multiply loss by a large scale factor (e.g., 1024)
2. Backward pass computes gradients of (loss * 1024)
3. All gradients are 1024x larger (pushed above float16 underflow)
4. Divide gradients by 1024 before updating weights
5. Net effect: same update, but no underflow
```

动态损失缩放会自动调整缩放因子。先从一个较大的值（65536）开始。如果梯度上溢到 `inf`，就将缩放因子减半；如果经过 N 步都没有上溢，就将它加倍。

### bfloat16 与 float16：为什么训练时 bfloat16 更占优势

```text
float16:   [1 sign] [5 exponent]  [10 mantissa]
bfloat16:  [1 sign] [8 exponent]  [7 mantissa]
```

float16 的精度更高，尾数有 10 位，而另一种格式只有 7 位；但它的范围有限，最大值约为 ~65,504。bfloat16 的精度较低，但范围与 float32 相同，最大值约为 ~3.4e38。

对于神经网络训练：

- 训练过程中出现数值突增时，激活值和 logits 经常超过 65,504。float16 会上溢，而 bfloat16 可以处理这些值
- float16 需要损失缩放，而 bfloat16 通常不需要，因为它的表示范围涵盖了梯度大小的各个量级
- bfloat16 就是将 float32 简单截断：去掉尾数最低的 16 位。转换非常简单，而且指数部分没有损失

推理时，数值有界，精度更重要，因此更倾向于使用 float16；训练时，范围更重要，因此更倾向于使用 bfloat16。这也是 TPU 和现代 NVIDIA GPU（A100、H100）原生支持 bfloat16 的原因。

### 梯度裁剪

梯度经过许多层后呈指数增长，就会发生梯度爆炸，这在循环神经网络（RNN）、深层网络和 Transformer 中很常见。一个很大的梯度，就可能在一步更新中破坏所有权重。

裁剪有两种方式：

**按值裁剪（clip by value）：** 分别将每个梯度元素限制在指定区间。

```text
grad = clamp(grad, -max_val, max_val)
```

这种方式很简单，但可能改变梯度向量的方向。

**按范数裁剪（clip by norm）：** 缩放整个梯度向量，使其范数不超过阈值。

```text
if ||grad|| > max_norm:
    grad = grad * (max_norm / ||grad||)
```

这种方式可以保持梯度方向不变。`torch.nn.utils.clip_grad_norm_()` 做的就是这件事，它也是标准选择。

常用值如下：Transformer 使用 `max_norm=1.0`，强化学习（RL）使用 `max_norm=0.5`，较简单的网络使用 `max_norm=5.0`。

梯度裁剪不是权宜之计，而是一种安全机制。没有它，一个异常批次就可能产生足够大的梯度，毁掉数周的训练成果。

### 归一化层也能稳定数值

批量归一化（batch normalization）、层归一化（layer normalization）和 RMS 归一化（均方根归一化）通常被介绍为帮助训练收敛的正则化手段。它们也能稳定数值。

不做归一化时，激活值经过各层后可能呈指数增长或衰减：

```text
Layer 1: values in [0, 1]
Layer 5: values in [0, 100]
Layer 10: values in [0, 10,000]
Layer 50: values in [0, inf]
```

归一化会在每一层重新对激活值进行中心化和缩放：

```text
LayerNorm(x) = (x - mean(x)) / (std(x) + epsilon) * gamma + beta
```

当所有激活值都相同时，`epsilon`（通常为 1e-5）可以防止除以零。通过学习得到的参数 `gamma` 和 `beta`，网络可以恢复所需的任意尺度。

这使数值在整个网络中都保持在安全范围内，既能防止前向传播中的上溢，也能防止反向传播中的梯度爆炸。

### 常见的 ML 数值 bug

**问题：训练几个轮次（epoch）后，损失变成 NaN。**
原因：logits 增长过大，导致 softmax 上溢；或者学习率过高，权重发散。
解决办法：使用稳定版 softmax，也就是先减去最大值；降低学习率，并加入梯度裁剪。

**问题：损失停留在 log(num_classes)。**
原因：模型输出的概率接近均匀分布。这通常意味着梯度正在消失，或者模型根本没有学习。
解决办法：检查数据标签是否正确，验证损失函数，并检查是否有失活的 ReLU。

**问题：验证准确率比预期低 1-3%。**
原因：使用了混合精度，却没有进行适当的损失缩放。梯度下溢会悄悄将较小的更新归零。
解决办法：启用动态损失缩放，或者改用 bfloat16。

**问题：某些层的梯度范数为 0.0。**
原因：ReLU 神经元失活，即所有输入都为负；或者发生了 float16 下溢。
解决办法：使用 LeakyReLU 或 GELU，采用梯度缩放，并检查权重初始化。

**问题：模型在一块 GPU 上运行正常，换一块 GPU 却得到不同结果。**
原因：浮点数累加顺序不确定。GPU 的并行归约在不同硬件上按不同顺序求和，而浮点加法不满足结合律。
解决办法：接受较小的差异（1e-6），或者设置 `torch.use_deterministic_algorithms(True)`，并接受速度下降。

**问题：计算损失时，`exp()` 返回 `inf`。**
原因：没有使用减去最大值的技巧，就把原始 logits 传给了 `exp()`。
解决办法：使用 `torch.nn.functional.log_softmax()`，它在内部实现了 log-sum-exp。

**问题：从 float32 切换到 float16 后，训练开始发散。**
原因：float16 无法表示大小低于 6e-8 的梯度，或高于 65,504 的激活值。
解决办法：使用带损失缩放的混合精度（AMP），或者改用 bfloat16。

```figure
logsumexp-stability
```

## 动手实现

### 步骤 1：展示浮点精度的限制

```python
print("=== Floating Point Precision ===")
print(f"0.1 + 0.2 = {0.1 + 0.2}")
print(f"0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}")
print(f"Difference: {(0.1 + 0.2) - 0.3:.2e}")
```

### 步骤 2：实现朴素版与稳定版 softmax

```python
import math

def softmax_naive(logits):
    exps = [math.exp(z) for z in logits]
    total = sum(exps)
    return [e / total for e in exps]

def softmax_stable(logits):
    max_logit = max(logits)
    exps = [math.exp(z - max_logit) for z in logits]
    total = sum(exps)
    return [e / total for e in exps]

safe_logits = [2.0, 1.0, 0.1]
print(f"Naive:  {softmax_naive(safe_logits)}")
print(f"Stable: {softmax_stable(safe_logits)}")

dangerous_logits = [100.0, 101.0, 102.0]
print(f"Stable: {softmax_stable(dangerous_logits)}")
# softmax_naive(dangerous_logits) would return [nan, nan, nan]
```

### 步骤 3：实现稳定版 log-sum-exp

```python
def logsumexp_naive(values):
    return math.log(sum(math.exp(v) for v in values))

def logsumexp_stable(values):
    c = max(values)
    return c + math.log(sum(math.exp(v - c) for v in values))

safe = [1.0, 2.0, 3.0]
print(f"Naive:  {logsumexp_naive(safe):.6f}")
print(f"Stable: {logsumexp_stable(safe):.6f}")

large = [500.0, 501.0, 502.0]
print(f"Stable: {logsumexp_stable(large):.6f}")
# logsumexp_naive(large) returns inf
```

### 步骤 4：实现稳定版交叉熵

```python
def cross_entropy_naive(true_class, logits):
    probs = softmax_naive(logits)
    return -math.log(probs[true_class])

def cross_entropy_stable(true_class, logits):
    max_logit = max(logits)
    shifted = [z - max_logit for z in logits]
    log_sum_exp = math.log(sum(math.exp(s) for s in shifted))
    log_prob = shifted[true_class] - log_sum_exp
    return -log_prob

logits = [2.0, 5.0, 1.0]
true_class = 1
print(f"Naive:  {cross_entropy_naive(true_class, logits):.6f}")
print(f"Stable: {cross_entropy_stable(true_class, logits):.6f}")
```

### 步骤 5：检查梯度

```python
def numerical_gradient(f, x, h=1e-5):
    grad = []
    for i in range(len(x)):
        x_plus = x[:]
        x_minus = x[:]
        x_plus[i] += h
        x_minus[i] -= h
        grad.append((f(x_plus) - f(x_minus)) / (2 * h))
    return grad

def check_gradient(analytical, numerical, tolerance=1e-5):
    for i, (a, n) in enumerate(zip(analytical, numerical)):
        denom = max(abs(a), abs(n), 1e-8)
        rel_error = abs(a - n) / denom
        status = "OK" if rel_error < tolerance else "FAIL"
        print(f"  param {i}: analytical={a:.8f} numerical={n:.8f} "
              f"rel_error={rel_error:.2e} [{status}]")

def f(params):
    x, y = params
    return x**2 + 3*x*y + y**3

def f_grad(params):
    x, y = params
    return [2*x + 3*y, 3*x + 3*y**2]

point = [2.0, 1.0]
analytical = f_grad(point)
numerical = numerical_gradient(f, point)
check_gradient(analytical, numerical)
```

## 实际使用

### 混合精度模拟

```python
import struct

def float32_to_float16_round(x):
    packed = struct.pack('f', x)
    f32 = struct.unpack('f', packed)[0]
    packed16 = struct.pack('e', f32)
    return struct.unpack('e', packed16)[0]

def simulate_bfloat16(x):
    packed = struct.pack('f', x)
    as_int = int.from_bytes(packed, 'little')
    truncated = as_int & 0xFFFF0000
    repacked = truncated.to_bytes(4, 'little')
    return struct.unpack('f', repacked)[0]
```

### 梯度裁剪

```python
def clip_by_norm(gradients, max_norm):
    total_norm = math.sqrt(sum(g**2 for g in gradients))
    if total_norm > max_norm:
        scale = max_norm / total_norm
        return [g * scale for g in gradients]
    return gradients

grads = [10.0, 20.0, 30.0]
clipped = clip_by_norm(grads, max_norm=5.0)
print(f"Original norm: {math.sqrt(sum(g**2 for g in grads)):.2f}")
print(f"Clipped norm:  {math.sqrt(sum(g**2 for g in clipped)):.2f}")
print(f"Direction preserved: {[c/clipped[0] for c in clipped]} == {[g/grads[0] for g in grads]}")
```

### NaN/Inf 检测

```python
def check_tensor(name, values):
    has_nan = any(math.isnan(v) for v in values)
    has_inf = any(math.isinf(v) for v in values)
    if has_nan or has_inf:
        print(f"WARNING {name}: nan={has_nan} inf={has_inf}")
        return False
    return True

check_tensor("good", [1.0, 2.0, 3.0])
check_tensor("bad",  [1.0, float('nan'), 3.0])
check_tensor("ugly", [1.0, float('inf'), 3.0])
```

完整实现及所有边界情况的演示见 `code/numerical.py`。

## 交付成果

本课产出：
- `code/numerical.py`，包含稳定版 softmax、log-sum-exp、交叉熵、梯度检查和混合精度模拟
- `outputs/prompt-numerical-debugger.md`，用于诊断训练中的 NaN/Inf 及数值问题

这些数值稳定的实现还会在阶段 3 构建训练循环时，以及阶段 4 实现注意力机制时再次用到。

## 练习

1. **灾难性消去。** 用 float32 和朴素公式 `E[x^2] - E[x]^2` 计算 [1000000.0, 1000001.0, 1000002.0] 的方差。然后用 Welford 在线算法计算。以真实方差（0.6667）为基准，比较两者的误差。

2. **寻找精度极限。** 在 Python 中，找到满足 `1.0 + x == 1.0` 的最小正 float32 数 `x`。这就是机器 epsilon（machine epsilon）。验证它是否与 `numpy.finfo(numpy.float32).eps` 一致。

3. **log-sum-exp 的边界情况。** 用以下输入测试你的 `logsumexp_stable` 函数：(a) 所有值都相等；(b) 一个值远大于其余值；(c) 所有值都是绝对值很大的负数（-1000）。验证它能在朴素版失败的情况下给出正确结果。

4. **检查神经网络层的梯度。** 实现一个线性层 `y = Wx + b` 及其解析反向传播过程。用 `numerical_gradient` 验证 3x2 权重矩阵的梯度是否正确。

5. **损失缩放实验。** 模拟 float16 训练：生成范围为 [1e-9, 1e-3] 的随机梯度，将其转换为 float16，测量变成零的比例。然后进行损失缩放，也就是乘以 1024，再转换为 float16、缩放回去，并再次测量零值比例。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|----------------------|
| IEEE 754 | “浮点数标准” | 定义二进制浮点格式、舍入规则及特殊值（inf、nan）的国际标准。每种现代 CPU 和 GPU 都实现了它。 |
| 机器 epsilon | “精度极限” | 对于给定的浮点格式，使 1.0 + e != 1.0 成立的最小值 e。float32 中约为 1.19e-7。 |
| 灾难性消去 | “减法导致精度丢失” | 两个非常接近的浮点数相减时，有效数字相互抵消，舍入噪声主导了结果。 |
| 上溢 | “数太大了” | 结果超出可表示的最大值，变成 inf。exp(89) 会在 float32 中上溢。 |
| 下溢 | “数太小了” | 结果比最小可表示正数更接近零，变成 0.0。exp(-104) 会在 float32 中下溢。 |
| log-sum-exp 技巧 | “先减去最大值” | 通过提取公因子 exp(max(x)) 来计算 log(sum(exp(x)))，避免上溢和下溢。用于 softmax、交叉熵和对数概率运算。 |
| 稳定版 softmax | “不会数值爆炸的 softmax” | 计算指数前先减去 max(logits)。数值结果相同，不可能发生上溢。 |
| 梯度检查 | “验证反向传播” | 将反向传播得到的解析梯度与有限差分得到的数值梯度进行比较，以发现实现中的 bug。 |
| 混合精度 | “Float16 前向传播，float32 反向传播” | 对速度要求高的运算使用较低精度浮点数，对数值敏感的运算使用较高精度浮点数。典型加速幅度为 2-3 倍。 |
| 损失缩放 | “防止梯度下溢” | 反向传播前将损失乘以较大的常数，使梯度保持在 float16 的表示范围内；更新权重前，再除以同一个常数。 |
| bfloat16 | “Brain floating point” | Google 的 16 位格式，指数有 8 位，因此范围与 float32 相同；尾数有 7 位，因此精度低于 float16。训练时优先选用。 |
| 梯度裁剪 | “限制梯度范数” | 缩放梯度向量，使其范数不超过阈值。防止梯度爆炸破坏权重。 |
| NaN | “非数” | 未定义运算（0/0、inf-inf、sqrt(-1)）产生的特殊浮点值，会传播到后续所有算术运算中。 |
| Inf | “无穷大” | 上溢或除以零产生的特殊浮点值。它们的某些组合运算会产生 NaN，例如 inf - inf、inf * 0。 |
| 数值梯度 | “暴力求导” | 计算 f(x+h) 和 f(x-h)，将两者之差除以 2h，以此近似导数。虽然慢，但用于验证很可靠。 |

## 延伸阅读

- [What Every Computer Scientist Should Know About Floating-Point Arithmetic（Goldberg 1991）](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html) -- 权威参考资料，内容密集但完整
- [Mixed Precision Training（Micikevicius 等，2018）](https://arxiv.org/abs/1710.03740) -- NVIDIA 提出为 float16 训练采用损失缩放的论文
- [AMP：自动混合精度（PyTorch 文档）](https://pytorch.org/docs/stable/amp.html) -- PyTorch 混合精度实用指南
- [bfloat16 格式（Google Cloud TPU 文档）](https://cloud.google.com/tpu/docs/bfloat16) -- Google 为何给 TPU 选择这种格式
- [Kahan 求和（Wikipedia）](https://en.wikipedia.org/wiki/Kahan_summation_algorithm) -- 减少浮点求和舍入误差的算法
