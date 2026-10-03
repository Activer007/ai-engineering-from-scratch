# 构建你自己的迷你框架

> 你已经实现了神经元、层、网络、反向传播、激活函数、损失函数、优化器、正则化、初始化和学习率（LR）调度。但它们都是独立的部件。现在，把它们连接起来，组成一个框架。不是 PyTorch，也不是 TensorFlow，而是你自己的框架。

**Type:** Build
**Languages:** Python
**Prerequisites:** 阶段 03 的全部课程（第 01-09 课）
**Time:** ~120 分钟

## 学习目标

- 构建一个完整的深度学习框架（~500 行），包含 Module（模块）、Linear、ReLU、Sigmoid、Dropout（随机失活）、BatchNorm（批量归一化）、Sequential（顺序容器）、损失函数、优化器和 DataLoader（数据加载器）
- 解释 Module 抽象（forward、backward、parameters），以及为什么需要切换 train/eval 模式
- 将所有组件接入一个可运行的训练循环，在圆形区域分类任务上训练一个 4 层网络
- 将框架中的每个组件对应到 PyTorch 中的等价组件（nn.Module、nn.Sequential、optim.Adam、DataLoader）

## 要解决的问题

你在十节课中实现的基础组件散落在不同文件里。这里有一个 `Value` 类，那里有一个训练循环，权重初始化在另一个文件中，学习率调度又在别处。要训练一个网络，你得从五节不同的课中复制粘贴，再手动把这些组件连接起来。

这正是框架要解决的问题。PyTorch 提供了 `nn.Module`、`nn.Sequential`、`optim.Adam`、`DataLoader`，以及把它们串起来的训练循环模式。TensorFlow 提供了 `keras.Layer`、`keras.Sequential`、`keras.optimizers.Adam`。这些并不神秘。它们是组织代码的模式，让你能够定义、训练和评估网络，而不必每次都重新搭建基础设施。

你将用 ~500 行 Python 实现同样的东西。不用 numpy，也不依赖任何外部库。这个框架能够定义任意前馈网络，用随机梯度下降（SGD）或 Adam 训练网络，对数据分批，应用随机失活和批量归一化，使用任意激活函数，并调度学习率。

完成之后，你就会确切理解在 PyTorch 中写下 `model = nn.Sequential(...)` 时发生了什么。你会明白为什么有 `model.train()` 和 `model.eval()`，为什么 `optimizer.zero_grad()` 要单独调用。你会理解这一切，因为这一切都是你亲手构建的。

## 核心概念

### Module 抽象

PyTorch 中的每一层都继承自 `nn.Module`。一个 Module 有三项职责：

1. **forward()** -- 根据输入计算输出
2. **parameters()** -- 返回所有可训练权重
3. **backward()** -- 计算梯度（PyTorch 中由自动微分 autograd 处理，而我们的框架显式实现）

Linear 层是 Module，ReLU 激活函数是 Module，随机失活层是 Module，批量归一化层也是 Module。它们都有相同的接口。

### Sequential 容器

`nn.Sequential` 将多个 Module 串联起来。前向传播时，数据先经过 Module 1，再经过 Module 2，接着经过 Module 3。反向传播时，则沿这条链逆序执行。容器本身也是 Module，具有 forward()、parameters() 和 backward()。这就是组合模式：由一系列 Module 组成的序列，本身也是一个 Module。

### 训练模式与评估模式

Dropout 在训练时随机将神经元置零，在评估时则让所有值原样通过。批量归一化在训练时使用批次统计量，在评估时则使用运行平均值。`train()` 和 `eval()` 方法用于切换这些行为。每个 Module 都有一个 `training` 标志。

### 优化器

优化器利用参数的梯度来更新参数。SGD：`param -= lr * grad`。Adam：维护动量和方差的估计值，然后进行更新。优化器并不了解网络架构，它看到的只有参数及其梯度组成的扁平列表。

### DataLoader

分批很重要，原因有两个。首先，对于规模较大的问题，内存无法容纳整个数据集。其次，小批量梯度下降会引入噪声，有助于逃离局部极小值。DataLoader 将数据分成批次，并且可以在各轮训练之间打乱顺序。

### 框架架构

```mermaid
graph TD
    subgraph "Modules"
        Linear["Linear<br/>W*x + b"]
        ReLU["ReLU<br/>max(0, x)"]
        Sigmoid["Sigmoid<br/>1/(1+e^-x)"]
        Dropout["Dropout<br/>random zero mask"]
        BatchNorm["BatchNorm<br/>normalize activations"]
    end

    subgraph "Containers"
        Sequential["Sequential<br/>chains modules"]
    end

    subgraph "Loss Functions"
        MSE["MSELoss<br/>(pred - target)^2"]
        BCE["BCELoss<br/>binary cross-entropy"]
    end

    subgraph "Optimizers"
        SGD["SGD<br/>param -= lr * grad"]
        Adam["Adam<br/>adaptive moments"]
    end

    subgraph "Data"
        DataLoader["DataLoader<br/>batching + shuffle"]
    end

    Sequential --> |"contains"| Linear
    Sequential --> |"contains"| ReLU
    Sequential --> |"forward/backward"| MSE
    SGD --> |"updates"| Sequential
    DataLoader --> |"feeds"| Sequential
```

### 训练循环

```mermaid
sequenceDiagram
    participant DL as DataLoader
    participant M as Model
    participant L as Loss
    participant O as Optimizer

    loop Each Epoch
        DL->>M: batch of inputs
        M->>M: forward pass (layer by layer)
        M->>L: predictions
        L->>L: compute loss
        L->>M: backward pass (gradients)
        M->>O: parameters + gradients
        O->>M: updated parameters
        O->>O: zero gradients
    end
```

### Module 层次结构

```mermaid
classDiagram
    class Module {
        +forward(x)
        +backward(grad)
        +parameters()
        +train()
        +eval()
    }

    class Linear {
        -weights
        -biases
        +forward(x)
        +backward(grad)
    }

    class ReLU {
        +forward(x)
        +backward(grad)
    }

    class Sequential {
        -modules[]
        +forward(x)
        +backward(grad)
        +parameters()
    }

    Module <|-- Linear
    Module <|-- ReLU
    Module <|-- Sequential
    Sequential *-- Module
```

```figure
gradient-clipping
```

## 动手实现

### 第 1 步：Module 基类

每一层都要实现的抽象接口。

```python
class Module:
    def __init__(self):
        self.training = True

    def forward(self, x):
        raise NotImplementedError

    def backward(self, grad):
        raise NotImplementedError

    def parameters(self):
        return []

    def train(self):
        self.training = True

    def eval(self):
        self.training = False
```

### 第 2 步：Linear 层

最基本的构建单元。它存储权重和偏置，在前向传播时计算 Wx + b，在反向传播时计算权重和输入的梯度。

```python
import math
import random


class Linear(Module):
    def __init__(self, fan_in, fan_out):
        super().__init__()
        std = math.sqrt(2.0 / fan_in)
        self.weights = [[random.gauss(0, std) for _ in range(fan_in)] for _ in range(fan_out)]
        self.biases = [0.0] * fan_out
        self.weight_grads = [[0.0] * fan_in for _ in range(fan_out)]
        self.bias_grads = [0.0] * fan_out
        self.fan_in = fan_in
        self.fan_out = fan_out
        self.input = None

    def forward(self, x):
        self.input = x
        output = []
        for i in range(self.fan_out):
            val = self.biases[i]
            for j in range(self.fan_in):
                val += self.weights[i][j] * x[j]
            output.append(val)
        return output

    def backward(self, grad):
        input_grad = [0.0] * self.fan_in
        for i in range(self.fan_out):
            self.bias_grads[i] += grad[i]
            for j in range(self.fan_in):
                self.weight_grads[i][j] += grad[i] * self.input[j]
                input_grad[j] += grad[i] * self.weights[i][j]
        return input_grad

    def parameters(self):
        params = []
        for i in range(self.fan_out):
            for j in range(self.fan_in):
                params.append((self.weights, i, j, self.weight_grads))
            params.append((self.biases, i, None, self.bias_grads))
        return params
```

### 第 3 步：激活模块

将 ReLU、Sigmoid 和 Tanh 实现为 Module。每个模块都会缓存反向传播所需的信息。

```python
class ReLU(Module):
    def __init__(self):
        super().__init__()
        self.mask = None

    def forward(self, x):
        self.mask = [1.0 if v > 0 else 0.0 for v in x]
        return [max(0.0, v) for v in x]

    def backward(self, grad):
        return [g * m for g, m in zip(grad, self.mask)]


class Sigmoid(Module):
    def __init__(self):
        super().__init__()
        self.output = None

    def forward(self, x):
        self.output = []
        for v in x:
            v = max(-500, min(500, v))
            self.output.append(1.0 / (1.0 + math.exp(-v)))
        return self.output

    def backward(self, grad):
        return [g * o * (1 - o) for g, o in zip(grad, self.output)]


class Tanh(Module):
    def __init__(self):
        super().__init__()
        self.output = None

    def forward(self, x):
        self.output = [math.tanh(v) for v in x]
        return self.output

    def backward(self, grad):
        return [g * (1 - o * o) for g, o in zip(grad, self.output)]
```

### 第 4 步：Dropout 模块

训练时随机将元素置零。将剩余元素乘以 1/(1-p)，使期望值保持不变。在评估时不做任何操作。

```python
class Dropout(Module):
    def __init__(self, p=0.5):
        super().__init__()
        self.p = p
        self.mask = None

    def forward(self, x):
        if not self.training:
            return x
        self.mask = [0.0 if random.random() < self.p else 1.0 / (1 - self.p) for _ in x]
        return [v * m for v, m in zip(x, self.mask)]

    def backward(self, grad):
        if self.mask is None:
            return grad
        return [g * m for g, m in zip(grad, self.mask)]
```

### 第 5 步：BatchNorm 模块

对批次中的每个特征分别归一化，使激活值的均值为零、方差为一。同时维护供评估模式使用的运行统计量。

```python
class BatchNorm(Module):
    def __init__(self, size, momentum=0.1, eps=1e-5):
        super().__init__()
        self.size = size
        self.gamma = [1.0] * size
        self.beta = [0.0] * size
        self.gamma_grads = [0.0] * size
        self.beta_grads = [0.0] * size
        self.running_mean = [0.0] * size
        self.running_var = [1.0] * size
        self.momentum = momentum
        self.eps = eps
        self.x_norm = None
        self.std_inv = None
        self.batch_input = None

    def forward_batch(self, batch):
        batch_size = len(batch)
        output_batch = []

        if self.training:
            mean = [0.0] * self.size
            for sample in batch:
                for j in range(self.size):
                    mean[j] += sample[j]
            mean = [m / batch_size for m in mean]

            var = [0.0] * self.size
            for sample in batch:
                for j in range(self.size):
                    var[j] += (sample[j] - mean[j]) ** 2
            var = [v / batch_size for v in var]

            self.std_inv = [1.0 / math.sqrt(v + self.eps) for v in var]

            self.x_norm = []
            self.batch_input = batch
            for sample in batch:
                normed = [(sample[j] - mean[j]) * self.std_inv[j] for j in range(self.size)]
                self.x_norm.append(normed)
                output = [self.gamma[j] * normed[j] + self.beta[j] for j in range(self.size)]
                output_batch.append(output)

            for j in range(self.size):
                self.running_mean[j] = (1 - self.momentum) * self.running_mean[j] + self.momentum * mean[j]
                self.running_var[j] = (1 - self.momentum) * self.running_var[j] + self.momentum * var[j]
        else:
            std_inv = [1.0 / math.sqrt(v + self.eps) for v in self.running_var]
            for sample in batch:
                normed = [(sample[j] - self.running_mean[j]) * std_inv[j] for j in range(self.size)]
                output = [self.gamma[j] * normed[j] + self.beta[j] for j in range(self.size)]
                output_batch.append(output)

        return output_batch

    def forward(self, x):
        result = self.forward_batch([x])
        return result[0]

    def backward(self, grad):
        if self.x_norm is None:
            return grad
        for j in range(self.size):
            self.gamma_grads[j] += self.x_norm[0][j] * grad[j]
            self.beta_grads[j] += grad[j]
        return [grad[j] * self.gamma[j] * self.std_inv[j] for j in range(self.size)]

    def parameters(self):
        params = []
        for j in range(self.size):
            params.append((self.gamma, j, None, self.gamma_grads))
            params.append((self.beta, j, None, self.beta_grads))
        return params
```

### 第 6 步：Sequential 容器

将各模块串联起来。前向传播从左向右进行，反向传播从右向左进行。

```python
class Sequential(Module):
    def __init__(self, *modules):
        super().__init__()
        self.modules = list(modules)

    def forward(self, x):
        for module in self.modules:
            x = module.forward(x)
        return x

    def backward(self, grad):
        for module in reversed(self.modules):
            grad = module.backward(grad)
        return grad

    def parameters(self):
        params = []
        for module in self.modules:
            params.extend(module.parameters())
        return params

    def train(self):
        self.training = True
        for module in self.modules:
            module.train()

    def eval(self):
        self.training = False
        for module in self.modules:
            module.eval()
```

### 第 7 步：损失函数

均方误差（MSE）和二元交叉熵。每个损失函数都会返回损失值，并提供一个返回梯度的 backward() 方法。

```python
class MSELoss:
    def __call__(self, predicted, target):
        self.predicted = predicted
        self.target = target
        n = len(predicted)
        self.loss = sum((p - t) ** 2 for p, t in zip(predicted, target)) / n
        return self.loss

    def backward(self):
        n = len(self.predicted)
        return [2 * (p - t) / n for p, t in zip(self.predicted, self.target)]


class BCELoss:
    def __call__(self, predicted, target):
        self.predicted = predicted
        self.target = target
        eps = 1e-7
        n = len(predicted)
        self.loss = 0
        for p, t in zip(predicted, target):
            p = max(eps, min(1 - eps, p))
            self.loss += -(t * math.log(p) + (1 - t) * math.log(1 - p))
        self.loss /= n
        return self.loss

    def backward(self):
        eps = 1e-7
        n = len(self.predicted)
        grads = []
        for p, t in zip(self.predicted, self.target):
            p = max(eps, min(1 - eps, p))
            grads.append((-t / p + (1 - t) / (1 - p)) / n)
        return grads
```

### 第 8 步：SGD 和 Adam 优化器

二者都接收一个参数列表，并利用梯度更新权重。

```python
class SGD:
    def __init__(self, parameters, lr=0.01):
        self.params = parameters
        self.lr = lr

    def step(self):
        for container, i, j, grad_container in self.params:
            if j is not None:
                container[i][j] -= self.lr * grad_container[i][j]
            else:
                container[i] -= self.lr * grad_container[i]

    def zero_grad(self):
        for container, i, j, grad_container in self.params:
            if j is not None:
                grad_container[i][j] = 0.0
            else:
                grad_container[i] = 0.0


class Adam:
    def __init__(self, parameters, lr=0.001, beta1=0.9, beta2=0.999, eps=1e-8):
        self.params = parameters
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = eps
        self.t = 0
        self.m = [0.0] * len(parameters)
        self.v = [0.0] * len(parameters)

    def step(self):
        self.t += 1
        for idx, (container, i, j, grad_container) in enumerate(self.params):
            if j is not None:
                g = grad_container[i][j]
            else:
                g = grad_container[i]

            self.m[idx] = self.beta1 * self.m[idx] + (1 - self.beta1) * g
            self.v[idx] = self.beta2 * self.v[idx] + (1 - self.beta2) * g * g

            m_hat = self.m[idx] / (1 - self.beta1 ** self.t)
            v_hat = self.v[idx] / (1 - self.beta2 ** self.t)

            update = self.lr * m_hat / (math.sqrt(v_hat) + self.eps)

            if j is not None:
                container[i][j] -= update
            else:
                container[i] -= update

    def zero_grad(self):
        for container, i, j, grad_container in self.params:
            if j is not None:
                grad_container[i][j] = 0.0
            else:
                grad_container[i] = 0.0
```

### 第 9 步：DataLoader

将数据分成批次，并可选择在每轮训练时打乱顺序。

```python
class DataLoader:
    def __init__(self, data, batch_size=32, shuffle=True):
        self.data = data
        self.batch_size = batch_size
        self.shuffle = shuffle

    def __iter__(self):
        indices = list(range(len(self.data)))
        if self.shuffle:
            random.shuffle(indices)
        for start in range(0, len(indices), self.batch_size):
            batch_indices = indices[start:start + self.batch_size]
            batch = [self.data[i] for i in batch_indices]
            inputs = [item[0] for item in batch]
            targets = [item[1] for item in batch]
            yield inputs, targets

    def __len__(self):
        return (len(self.data) + self.batch_size - 1) // self.batch_size
```

### 第 10 步：在圆形区域分类任务上训练一个 4 层网络

将所有组件连接起来。定义模型，选择损失函数和优化器，然后运行训练循环。

```python
def make_circle_data(n=500, seed=42):
    random.seed(seed)
    data = []
    for _ in range(n):
        x = random.uniform(-2, 2)
        y = random.uniform(-2, 2)
        label = 1.0 if x * x + y * y < 1.5 else 0.0
        data.append(([x, y], [label]))
    return data


def train():
    random.seed(42)

    model = Sequential(
        Linear(2, 16),
        ReLU(),
        Linear(16, 16),
        ReLU(),
        Linear(16, 8),
        ReLU(),
        Linear(8, 1),
        Sigmoid(),
    )

    criterion = BCELoss()
    optimizer = Adam(model.parameters(), lr=0.01)

    data = make_circle_data(500)
    split = int(len(data) * 0.8)
    train_data = data[:split]
    test_data = data[split:]

    loader = DataLoader(train_data, batch_size=16, shuffle=True)

    model.train()

    for epoch in range(100):
        total_loss = 0
        total_correct = 0
        total_samples = 0

        for batch_inputs, batch_targets in loader:
            batch_loss = 0
            for x, t in zip(batch_inputs, batch_targets):
                pred = model.forward(x)
                loss = criterion(pred, t)
                batch_loss += loss

                optimizer.zero_grad()
                grad = criterion.backward()
                model.backward(grad)
                optimizer.step()

                predicted_class = 1.0 if pred[0] >= 0.5 else 0.0
                if predicted_class == t[0]:
                    total_correct += 1
                total_samples += 1

            total_loss += batch_loss

        avg_loss = total_loss / total_samples
        accuracy = total_correct / total_samples * 100

        if epoch % 10 == 0 or epoch == 99:
            print(f"Epoch {epoch:3d} | Loss: {avg_loss:.6f} | Train Accuracy: {accuracy:.1f}%")

    model.eval()
    correct = 0
    for x, t in test_data:
        pred = model.forward(x)
        predicted_class = 1.0 if pred[0] >= 0.5 else 0.0
        if predicted_class == t[0]:
            correct += 1
    test_accuracy = correct / len(test_data) * 100
    print(f"\nTest Accuracy: {test_accuracy:.1f}% ({correct}/{len(test_data)})")

    return model, test_accuracy
```

## 实际使用

下面是与你刚才构建的框架相对应的 PyTorch 版本：

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

model = nn.Sequential(
    nn.Linear(2, 16),
    nn.ReLU(),
    nn.Linear(16, 16),
    nn.ReLU(),
    nn.Linear(16, 8),
    nn.ReLU(),
    nn.Linear(8, 1),
    nn.Sigmoid(),
)

criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(100):
    model.train()
    for inputs, targets in dataloader:
        optimizer.zero_grad()
        predictions = model(inputs)
        loss = criterion(predictions, targets)
        loss.backward()
        optimizer.step()

    model.eval()
    with torch.no_grad():
        test_predictions = model(test_inputs)
```

结构完全一致：`Sequential`、`Linear`、`ReLU`、`Sigmoid`、`BCELoss`、`Adam`、`zero_grad`、`backward`、`step`、`train`、`eval`。每个概念都能一一对应。区别在于，PyTorch 会自动处理自动微分（不需要在每个模块中实现 backward()），能够在 GPU 上运行，而且经过了多年的优化。但它们的基本骨架是相同的。

现在，当你看到 PyTorch 代码时，就能确切地知道每一行在做什么。获得这样的理解，正是本课的全部意义。

## 交付成果

本课将产出：
- `outputs/prompt-framework-architect.md` -- 一个利用框架抽象来设计神经网络架构的提示词（prompt）

## 练习

1. 添加一个用于多分类的 `SoftmaxCrossEntropyLoss` 类。对预测值应用 softmax，计算交叉熵损失，并处理二者合并后的反向传播。在一个 3 类螺旋数据集上测试它。

2. 在优化器中实现学习率调度：添加 `set_lr()` 方法，并接入第 09 课中的余弦调度。用预热（warmup）+ 余弦调度训练圆形区域分类器，并与恒定 LR 比较。

3. 为 Sequential 添加 `save()` 和 `load()` 方法，将所有权重序列化为 JSON 文件并重新加载。验证加载后的模型与原模型给出相同的预测。

4. 在 Adam 优化器中实现权重衰减（L2 正则化）。添加一个 `weight_decay` 参数，使权重在每一步都向零收缩。比较 decay=0 与 decay=0.01 时的训练表现。

5. 用真正的小批量梯度累积替换逐样本训练循环：累积一个批次中所有样本的梯度，再除以批次大小，然后执行一次优化器更新。测量这是否会改变收敛速度。

## 关键术语

| 术语 | 通俗说法 | 实际含义 |
|------|----------------|----------------------|
| Module | “一个层” | 框架中的基础抽象，即任何具有 forward()、backward() 和 parameters() 的对象 |
| Sequential | “按顺序堆叠各层” | 串联模块的容器，前向传播时依次应用各模块，反向传播时逆序应用 |
| 前向传播 | “运行网络” | 将输入按顺序传入各个模块，计算输出 |
| 反向传播 | “计算梯度” | 将损失梯度逆序传过各模块，从而计算参数梯度 |
| 参数 | “可训练的权重” | 网络中优化器能够更新的所有值，包括权重和偏置 |
| 优化器 | “更新权重的东西” | 利用梯度更新参数的算法，实现 SGD、Adam 或其他更新规则 |
| DataLoader | “提供数据的东西” | 将数据集拆成批次的迭代器，可以在各轮训练之间打乱顺序 |
| 训练模式 | “model.train()” | 启用随机失活等随机行为，以及使用批次统计量的批量归一化的标志 |
| 评估模式 | “model.eval()” | 禁用随机失活，并让批量归一化使用运行统计量的标志 |
| 梯度清零 | “清除梯度” | 在计算下一个批次的梯度之前，将所有参数梯度重置为零 |

## 延伸阅读

- Paszke 等，"PyTorch: An Imperative Style, High-Performance Deep Learning Library" (2019) -- 介绍 PyTorch 设计决策的论文
- Chollet，"Deep Learning with Python, Second Edition" (2021) -- 第 3 章介绍 Keras 内部机制，使用相同的模块/层抽象
- Johnson，"Tiny-DNN" (https://github.com/tiny-dnn/tiny-dnn) -- 一个仅含头文件的 C++ 深度学习框架，可用于理解框架内部机制
