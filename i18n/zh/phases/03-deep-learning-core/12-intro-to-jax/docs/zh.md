# JAX 入门

> PyTorch 修改张量。TensorFlow 构建计算图。JAX 编译纯函数。最后这一点，会改变你思考深度学习的方式。

**Type:** Build
**Languages:** Python
**Prerequisites:** 阶段 03 第 01-10 课、NumPy 基础
**Time:** ~90 分钟

## 学习目标

- 使用 JAX 的函数式 API（应用程序编程接口，jax.numpy、jax.grad、jax.jit、jax.vmap）编写纯函数形式的神经网络代码
- 解释 PyTorch 的即时修改方式与 JAX 的函数式编译模型之间的关键设计差异
- 运用 jit 编译和 vmap 向量化，相比朴素 Python 实现加速训练循环
- 在 JAX 中训练一个简单网络，并将其显式状态管理与 PyTorch 的面向对象方式进行对比

## 要解决的问题

你已经知道如何用 PyTorch 构建神经网络：定义一个 `nn.Module`，调用 `.backward()`，再让优化器执行更新。这套方法行得通，有数百万人在使用。

但 PyTorch 有一个刻在骨子里的约束：它在 Python 中以即时方式逐个跟踪运算。每次 `tensor + tensor` 都会单独启动一个计算内核。每个训练步骤都会重新解释同样的 Python 代码。通常这没问题，但当你需要在 2,048 个 TPU 上训练一个具有 540 billion（十亿）个参数的模型时，开销就会变得难以承受。

Google DeepMind 用 JAX 训练 Gemini。Anthropic 曾用 JAX 训练 Claude。这些绝非小规模任务，而是地球上规模最大的神经网络训练任务。它们选择 JAX，是因为 JAX 将训练循环视为可编译的程序，而不是一连串 Python 调用。

JAX 就是拥有三项超能力的 NumPy：自动微分、编译到 XLA 的即时编译（JIT），以及自动向量化。你编写一个处理单个样本的函数，JAX 就能给你一个处理整个批次、计算梯度、编译成机器码并跨多个设备运行的函数，而无需修改原函数。

## 核心概念

### JAX 的设计理念

JAX 是一个函数式框架。没有类，没有可变状态，也没有 `.backward()` 方法。它采用的是：

| PyTorch | JAX |
|---------|-----|
| 带有状态的 `nn.Module` 类 | 纯函数（pure function）：`f(params, x) -> y` |
| `loss.backward()` | `jax.grad(loss_fn)(params, x, y)` |
| 即时执行 | 通过 XLA 进行 JIT 编译 |
| `for x in batch:` 手动循环 | `jax.vmap(f)` 自动向量化 |
| `DataParallel` / `FSDP` | `jax.pmap(f)` 自动并行化 |
| 可变的 `model.parameters()` | 由数组组成的不可变 pytree（嵌套树结构） |

这不是编程风格偏好，而是编译器的约束。JIT 编译要求纯函数：相同输入始终产生相同输出，并且没有副作用。正是这一限制，让 100 倍加速成为可能。

### jax.numpy：熟悉的接口

JAX 在加速器上重新实现了 NumPy API：

```python
import jax.numpy as jnp

a = jnp.array([1.0, 2.0, 3.0])
b = jnp.array([4.0, 5.0, 6.0])
c = jnp.dot(a, b)
```

函数名相同，广播规则相同，切片语义也相同。但数组位于 GPU/TPU 上，而且每次运算都能被编译器跟踪。

一个关键区别是：JAX 数组不可变。不能使用 `a[0] = 5`，而要写成 `a = a.at[0].set(5)`。你可能会觉得别扭一周，然后便豁然开朗：正是不可变性，让 `grad`、`jit` 和 `vmap` 这样的变换能够组合使用。

### jax.grad：函数式自动微分

PyTorch 将梯度附着在张量上（`.grad`），JAX 则将梯度附着在函数上。

```python
import jax

def f(x):
    return x ** 2

df = jax.grad(f)
df(3.0)
```

`jax.grad` 接收一个函数，返回一个计算梯度的新函数。无需调用 `.backward()`，也不会在张量上存储计算图。梯度就是另一个函数，你可以调用它、组合它，或者对它进行 JIT 编译。

这种方式可以任意组合：

```python
d2f = jax.grad(jax.grad(f))
d2f(3.0)
```

二阶导数、三阶导数、Jacobian（雅可比矩阵）、Hessian（海森矩阵），都通过组合 `grad` 得到。PyTorch 也能做到（`torch.autograd.functional.hessian`），但那是后来附加的能力。在 JAX 中，这就是基础。

约束在于：`grad` 只适用于纯函数。函数内部不能有 print 语句，因为它们会在跟踪期间运行，而不是在执行期间运行。不能修改外部状态，也不能在没有显式密钥管理的情况下生成随机数。

### jit：编译到 XLA

```python
@jax.jit
def train_step(params, x, y):
    loss = loss_fn(params, x, y)
    return loss

fast_step = jax.jit(train_step)
```

第一次调用时，JAX 会跟踪函数：记录将发生哪些运算，而不执行这些运算。随后，它把跟踪结果交给 XLA（加速线性代数，Accelerated Linear Algebra），这是 Google 为 TPU 和 GPU 开发的编译器。XLA 会融合运算、消除冗余的内存复制，并生成优化后的机器码。

后续调用会完全跳过 Python。编译后的代码在加速器上以 C++ 的速度运行。

JIT 适用的场景：
- 训练步骤：相同计算重复数千次
- 推理：相同模型处理不同输入
- 任何使用形状相近的输入、被调用不止一次的函数

JIT 不利的场景：
- Python 控制流依赖具体值的函数，例如 `if x > 0`，其中 x 是被跟踪的数组
- 一次性计算：编译开销超过运行时间
- 调试：跟踪过程掩盖了实际执行过程

控制流限制确实存在。`jax.lax.cond` 替代 `if/else`，`jax.lax.scan` 替代 `for` 循环。这些并非可选项，而是编译所需付出的代价。

### vmap：自动向量化

你先编写一个处理单个样本的函数：

```python
def predict(params, x):
    return jnp.dot(params['w'], x) + params['b']
```

`vmap` 将它提升为处理整个批次的函数：

```python
batch_predict = jax.vmap(predict, in_axes=(None, 0))
```

`in_axes=(None, 0)` 的意思是：不沿 `params` 分批，因为参数是共享的；沿 `x` 的轴 0 分批。无需手写 `for` 循环，无需重塑形状，也无需在各处传递批次维度。JAX 会确定批次维度，并将整个计算向量化。

这不是语法糖。`vmap` 会生成融合后的向量化代码，运行速度比 Python 循环快 10-100 倍。而且，它能与 `jit` 和 `grad` 组合：

```python
per_example_grads = jax.vmap(jax.grad(loss_fn), in_axes=(None, 0, 0))
```

一行代码就能得到逐样本梯度。在 PyTorch 中，如果不借助变通手段，这几乎不可能实现。

### pmap：跨设备数据并行

```python
parallel_step = jax.pmap(train_step, axis_name='devices')
```

`pmap` 将函数复制到所有可用设备（GPU/TPU）上，并拆分批次。在函数内部，`jax.lax.pmean` 和 `jax.lax.psum` 用于跨设备同步梯度。

Google 使用 `pmap` 及其后继者 `shard_map`，在数千颗 TPU v5e 芯片上训练 Gemini。编程模式就是：写好单设备版本，用 `pmap` 包装，完成。

### Pytrees：通用数据结构

JAX 操作的是“pytrees”，即列表、元组、字典和数组的嵌套组合。你的模型参数就是一个 pytree：

```python
params = {
    'layer1': {'w': jnp.zeros((784, 256)), 'b': jnp.zeros(256)},
    'layer2': {'w': jnp.zeros((256, 128)), 'b': jnp.zeros(128)},
    'layer3': {'w': jnp.zeros((128, 10)),  'b': jnp.zeros(10)},
}
```

每种 JAX 变换，包括 `grad`、`jit` 和 `vmap`，都知道如何遍历 pytree。`jax.tree.map(f, tree)` 会将 `f` 应用于每个叶节点。优化器就是这样一次更新全部参数的：

```python
params = jax.tree.map(lambda p, g: p - lr * g, params, grads)
```

没有 `.parameters()` 方法，也没有参数注册。树结构本身就是模型。

### 函数式与面向对象

PyTorch 将状态存储在对象内部：

```python
class Model(nn.Module):
    def __init__(self):
        self.linear = nn.Linear(784, 10)

    def forward(self, x):
        return self.linear(x)
```

JAX 则使用具有显式状态的纯函数：

```python
def predict(params, x):
    return jnp.dot(x, params['w']) + params['b']
```

参数被传入函数，不存储任何内容，也不修改任何内容。这使每个函数都可以测试、组合和编译，也意味着你要自己管理参数，或者使用 Flax、Equinox 这样的库。

### JAX 生态系统

JAX 提供基本组件，库则让它们更易用：

| 库 | 作用 | 风格 |
|---------|------|-------|
| **Flax** (Google) | 神经网络层 | 带显式状态的 `nn.Module` |
| **Equinox** (Patrick Kidger) | 神经网络层 | 基于 pytree，符合 Python 风格 |
| **Optax** (DeepMind) | 优化器 + 学习率调度 | 可组合的梯度变换 |
| **Orbax** (Google) | 检查点保存与恢复 | 保存/恢复 pytree |
| **CLU** (Google) | 指标 + 日志记录 | 训练循环工具 |

Optax 是标准的优化器库。它将梯度变换（Adam、随机梯度下降 SGD、裁剪）与参数更新分离，让组合变得十分简单：

```python
optimizer = optax.chain(
    optax.clip_by_global_norm(1.0),
    optax.adam(learning_rate=1e-3),
)
```

### 何时使用 JAX，何时使用 PyTorch

| 因素 | JAX | PyTorch |
|--------|-----|---------|
| TPU 支持 | 一等支持（两者都由 Google 构建） | 社区维护（torch_xla） |
| GPU 支持 | 良好（通过 XLA 使用 CUDA） | 同类最佳（原生 CUDA） |
| 调试 | 困难（跟踪 + 编译） | 容易（即时执行、逐行运行） |
| 生态系统 | 侧重研究（Flax、Equinox） | 庞大（HuggingFace、torchvision 等） |
| 招聘 | 小众（Google/DeepMind/Anthropic） | 主流（各处都有） |
| 大规模训练 | 更优（XLA、pmap、mesh） | 良好（FSDP、DeepSpeed） |
| 原型开发速度 | 较慢（函数式方式的额外负担） | 较快（修改后即可继续） |
| 生产推理 | TensorFlow Serving, Vertex AI | TorchServe, Triton, ONNX |
| 使用者 | DeepMind (Gemini), Anthropic (Claude) | Meta (Llama), OpenAI (GPT), Stability AI |

坦率地说，除非有使用 JAX 的特定理由，否则就用 PyTorch。这些理由包括：能够使用 TPU、需要逐样本梯度、进行超大规模多设备训练，或者在 Google/DeepMind/Anthropic 工作。

### JAX 中的随机数

JAX 没有全局随机状态。每个随机操作都需要显式的伪随机数生成器（PRNG）密钥：

```python
key = jax.random.PRNGKey(42)
key1, key2 = jax.random.split(key)
w = jax.random.normal(key1, shape=(784, 256))
```

起初这会让人觉得麻烦，但它保证了跨设备、跨编译的可复现性，而 PyTorch 的 `torch.manual_seed` 无法在多 GPU 环境中保证这一点。

```figure
batchnorm-effect
```

## 动手实现

### 步骤 1：环境准备与数据

我们将使用 JAX 和 Optax，在 MNIST 上训练一个 3 层多层感知机（MLP）。它有 784 个输入，两个隐藏层分别含 256 和 128 个神经元，输出分为 10 个类别。

```python
import jax
import jax.numpy as jnp
from jax import random
import optax

def get_mnist_data():
    from sklearn.datasets import fetch_openml
    mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
    X = mnist.data.astype('float32') / 255.0
    y = mnist.target.astype('int')
    X_train, X_test = X[:60000], X[60000:]
    y_train, y_test = y[:60000], y[60000:]
    return X_train, y_train, X_test, y_test
```

### 步骤 2：初始化参数

没有类，只有一个返回 pytree 的函数：

```python
def init_params(key):
    k1, k2, k3 = random.split(key, 3)
    scale1 = jnp.sqrt(2.0 / 784)
    scale2 = jnp.sqrt(2.0 / 256)
    scale3 = jnp.sqrt(2.0 / 128)
    params = {
        'layer1': {
            'w': scale1 * random.normal(k1, (784, 256)),
            'b': jnp.zeros(256),
        },
        'layer2': {
            'w': scale2 * random.normal(k2, (256, 128)),
            'b': jnp.zeros(128),
        },
        'layer3': {
            'w': scale3 * random.normal(k3, (128, 10)),
            'b': jnp.zeros(10),
        },
    }
    return params
```

手动完成 He 初始化。从一个随机种子拆分出三个 PRNG 密钥。每个权重都是嵌套字典中的不可变数组。

### 步骤 3：前向传播

```python
def forward(params, x):
    x = jnp.dot(x, params['layer1']['w']) + params['layer1']['b']
    x = jax.nn.relu(x)
    x = jnp.dot(x, params['layer2']['w']) + params['layer2']['b']
    x = jax.nn.relu(x)
    x = jnp.dot(x, params['layer3']['w']) + params['layer3']['b']
    return x

def loss_fn(params, x, y):
    logits = forward(params, x)
    one_hot = jax.nn.one_hot(y, 10)
    return -jnp.mean(jnp.sum(jax.nn.log_softmax(logits) * one_hot, axis=-1))
```

这些都是纯函数：输入参数，输出预测。没有 `self`，也没有存储的状态。`loss_fn` 从零计算交叉熵，即 softmax、取对数、求均值并取负。

### 步骤 4：经 JIT 编译的训练步骤

```python
@jax.jit
def train_step(params, opt_state, x, y):
    loss, grads = jax.value_and_grad(loss_fn)(params, x, y)
    updates, opt_state = optimizer.update(grads, opt_state, params)
    params = optax.apply_updates(params, updates)
    return params, opt_state, loss

@jax.jit
def accuracy(params, x, y):
    logits = forward(params, x)
    preds = jnp.argmax(logits, axis=-1)
    return jnp.mean(preds == y)
```

`jax.value_and_grad` 在一次处理中同时返回损失值和梯度。`@jax.jit` 装饰器将这两个函数编译到 XLA。第一次调用之后，每个训练步骤都不再经过 Python。

### 步骤 5：训练循环

```python
optimizer = optax.adam(learning_rate=1e-3)

X_train, y_train, X_test, y_test = get_mnist_data()
X_train, X_test = jnp.array(X_train), jnp.array(X_test)
y_train, y_test = jnp.array(y_train), jnp.array(y_test)

key = random.PRNGKey(0)
params = init_params(key)
opt_state = optimizer.init(params)

batch_size = 128
n_epochs = 10

for epoch in range(n_epochs):
    key, subkey = random.split(key)
    perm = random.permutation(subkey, len(X_train))
    X_shuffled = X_train[perm]
    y_shuffled = y_train[perm]

    epoch_loss = 0.0
    n_batches = len(X_train) // batch_size
    for i in range(n_batches):
        start = i * batch_size
        xb = X_shuffled[start:start + batch_size]
        yb = y_shuffled[start:start + batch_size]
        params, opt_state, loss = train_step(params, opt_state, xb, yb)
        epoch_loss += loss

    train_acc = accuracy(params, X_train[:5000], y_train[:5000])
    test_acc = accuracy(params, X_test, y_test)
    print(f"Epoch {epoch + 1:2d} | Loss: {epoch_loss / n_batches:.4f} | "
          f"Train Acc: {train_acc:.4f} | Test Acc: {test_acc:.4f}")
```

训练 10 轮，测试准确率为 ~97%。第一轮很慢，因为需要 JIT 编译。第 2-10 轮则很快。

注意这里省去了什么：没有 `.zero_grad()`，没有 `.backward()`，也没有 `.step()`。整个更新就是一次组合函数调用。计算梯度、用 Adam 变换梯度、将其应用于参数，这些全都在 `train_step` 内部完成。

## 实际使用

### Flax：Google 的标准选择

Flax 是最常用的 JAX 神经网络库。它重新引入了 `nn.Module`，但采用显式状态管理：

```python
import flax.linen as nn

class MLP(nn.Module):
    @nn.compact
    def __call__(self, x):
        x = nn.Dense(256)(x)
        x = nn.relu(x)
        x = nn.Dense(128)(x)
        x = nn.relu(x)
        x = nn.Dense(10)(x)
        return x

model = MLP()
params = model.init(jax.random.PRNGKey(0), jnp.ones((1, 784)))
logits = model.apply(params, x_batch)
```

结构与 PyTorch 相同，但 `params` 与模型分离。`model.init()` 创建参数，`model.apply(params, x)` 执行前向传播。模型对象没有状态。

### Equinox：符合 Python 风格的替代方案

Equinox（由 Patrick Kidger 开发）将模型表示为 pytree：

```python
import equinox as eqx

model = eqx.nn.MLP(
    in_size=784, out_size=10, width_size=256, depth=2,
    activation=jax.nn.relu, key=jax.random.PRNGKey(0)
)
logits = model(x)
```

模型本身就是一个 pytree，无需 `.apply()`。参数就是模型的叶节点。这更接近 JAX 的思维方式。

### Optax：可组合的优化器

Optax 将梯度变换与更新解耦：

```python
schedule = optax.warmup_cosine_decay_schedule(
    init_value=0.0, peak_value=1e-3,
    warmup_steps=1000, decay_steps=50000
)

optimizer = optax.chain(
    optax.clip_by_global_norm(1.0),
    optax.adamw(learning_rate=schedule, weight_decay=0.01),
)
```

梯度裁剪、学习率预热、权重衰减，全都组合成一条变换链。每个变换接收梯度、修改它们，再传递给下一个变换。无需一个包揽所有功能的优化器类。

## 交付成果

**安装：**

```bash
pip install jax jaxlib optax flax
```

启用 GPU 支持：

```bash
pip install jax[cuda12]
```

用于 TPU（Google Cloud）：

```bash
pip install jax[tpu] -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
```

**性能注意事项：**

- 第一次 JIT 调用很慢，因为要编译。做基准测试前先预热。
- 避免在 JIT 内部用 Python 循环遍历 JAX 数组，应使用 `jax.lax.scan` 或 `jax.lax.fori_loop`。
- `jax.debug.print()` 可以在 JIT 内部工作，普通的 `print()` 则不行。
- 使用 `jax.profiler` 或 TensorBoard 做性能分析。XLA 编译可能会掩盖瓶颈。
- JAX 默认预分配 75% 的 GPU 内存。将 `XLA_PYTHON_CLIENT_PREALLOCATE=false` 设好即可禁用。

**检查点保存与恢复：**

```python
import orbax.checkpoint as ocp
checkpointer = ocp.PyTreeCheckpointer()
checkpointer.save('/tmp/model', params)
restored = checkpointer.restore('/tmp/model')
```

**本课产出：**
- `outputs/prompt-jax-optimizer.md`：用于选择合适 JAX 优化器配置的提示词
- `outputs/skill-jax-patterns.md`：涵盖 JAX 函数式模式的技能

## 练习

1. 给 MLP 添加 Dropout（随机失活）。在 JAX 中，Dropout 需要 PRNG 密钥：让密钥贯穿前向传播，并为每个 Dropout 层拆分密钥。比较使用与不使用 Dropout 时的测试准确率。

2. 使用 `jax.vmap` 为一个包含 32 张 MNIST 图像的批次计算逐样本梯度。计算每个样本的梯度范数。哪些样本的梯度最大？为什么？

3. 将手写的前向函数替换为通用的 `mlp_forward(params, x)`，使其支持任意层数。使用 `jax.tree.leaves` 自动确定网络深度。

4. 对比使用与不使用 `@jax.jit` 时的训练步骤性能。分别测量 100 步的耗时。在你的硬件上能加速多少？第一次调用的编译开销是多少？

5. 通过组合 `optax.chain(optax.clip_by_global_norm(1.0), optax.adam(1e-3))` 实现梯度裁剪。分别在使用与不使用裁剪时训练，绘制训练过程中的梯度范数曲线来观察效果。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|----------------------|
| XLA | “让 JAX 变快的东西” | 加速线性代数（Accelerated Linear Algebra），一种将运算融合、从计算图生成优化后的 GPU/TPU 计算内核的编译器 |
| JIT | “即时编译” | JAX 在首次调用时跟踪函数，编译到 XLA，然后在后续调用中运行编译后的版本 |
| 纯函数 | “没有副作用” | 输出只依赖输入的函数，没有全局状态、没有修改操作，也没有不带显式密钥的随机性 |
| vmap | “自动分批” | 将处理单个样本的函数变换为处理整个批次的函数，无需重写 |
| pmap | “自动并行化” | 将函数复制到多个设备上，并拆分输入批次 |
| Pytree | “数组的嵌套字典” | JAX 能够遍历和变换的、由列表、元组、字典和数组组成的任意嵌套结构 |
| 跟踪 | “记录计算” | JAX 用抽象值执行函数来构建计算图，而不计算实际结果 |
| 函数式自动微分 | “函数的 grad” | 通过变换函数计算导数，而不是给张量附加梯度存储 |
| Optax | “JAX 的优化器库” | 可组合的梯度变换库，将 Adam、SGD、裁剪、调度串联起来 |
| Flax | “JAX 的 nn.Module” | Google 为 JAX 提供的神经网络库，添加层抽象，同时保持状态显式 |

## 延伸阅读

- JAX 文档：https://jax.readthedocs.io/ —— 官方文档，包含优秀的 grad、jit 和 vmap 教程
- "JAX: composable transformations of Python+NumPy programs" (Bradbury 等人，2018)：解释设计理念的原始论文
- Flax 文档：https://flax.readthedocs.io/ —— Google 的 JAX 神经网络库
- Patrick Kidger，"Equinox: neural networks in JAX via callable PyTrees and filtered transformations" (2021)：符合 Python 风格的 Flax 替代方案
- DeepMind，"Optax: composable gradient transformation and optimisation"：标准优化器库
- "You Don't Know JAX" (Colin Raffel, 2020)：由 T5 作者之一撰写的实用指南，介绍 JAX 的常见陷阱和模式
