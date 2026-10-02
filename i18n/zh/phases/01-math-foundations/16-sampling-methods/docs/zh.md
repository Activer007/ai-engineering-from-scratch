# 采样方法

> 抽样是 AI 探索各种可能性的方式。

**Type:** Build
**Language:** Python
**Prerequisites:** 阶段 1，第 06-07 课（概率、Bayes 定理）
**Time:** ~120 分钟

## 学习目标

- 仅使用均匀随机数，从零实现逆 CDF 抽样、拒绝抽样和重要性抽样
- 构建用于语言模型 token 生成的温度采样、top-k 采样和 top-p（核）采样
- 解释重参数化技巧，以及它为何能让 VAE 中的反向传播穿过抽样操作
- 运行 Metropolis-Hastings MCMC，从未归一化的目标分布中抽样

## 要解决的问题

语言模型处理完你的提示词（prompt），输出一个包含 50,000 个 logits（未归一化分数）的向量，词表中的每个 token（词元）都对应一个分数。现在它必须选出一个，该怎么选？

如果总是选择概率最高的 token，每次回答都会一模一样，确定却乏味。如果完全均匀随机地选择，输出又会是一堆胡言乱语。答案介于这两个极端之间，而具体落在哪里，就由采样来控制。

抽样（sampling）并不限于文本生成。强化学习通过对轨迹抽样来估计策略梯度。VAE 从学习得到的分布中抽样，并让反向传播穿过随机性，以此学习潜在表示。扩散模型通过抽取噪声并迭代去噪来生成图像。Monte Carlo 方法用于估计没有闭式解的积分。MCMC 算法则探索无法穷举的高维后验分布。

每一个生成式 AI 系统都是抽样系统。抽样策略决定输出的质量、多样性和可控性。本课将从零构建各种主要的抽样方法，从均匀随机数出发，最终实现现代大语言模型（LLM）和生成模型背后的技术。

## 核心概念

### 为什么抽样很重要

在 AI 和机器学习中，抽样承担四种基本角色：

**生成。** 语言模型、扩散模型和 GAN 都通过抽样产生输出。抽样算法直接控制创造性、连贯性和多样性。温度、top-k 和核采样，都是工程师日常调节的参数。

**训练。** 随机梯度下降对小批量数据抽样；Dropout 随机选取要停用的神经元；数据增强随机选取变换。重要性抽样通过重新加权样本，降低强化学习（PPO、TRPO）中的梯度方差。

**估计。** ML 中的许多量没有闭式解，例如数据分布上的期望损失、能量模型的配分函数，以及贝叶斯推断中的证据。Monte Carlo 估计通过对样本取平均，近似这些量。

**探索。** MCMC 算法探索贝叶斯推断中的后验分布；演化策略抽取参数扰动；Thompson 抽样在多臂老虎机问题中平衡探索与利用。

核心挑战在于：你只能直接从简单分布（均匀分布、正态分布）中抽样。对于其他分布，需要一种方法，将简单分布的样本转换为目标分布的样本。

### 均匀随机抽样

所有抽样方法都从这里开始。均匀随机数生成器产生 [0, 1) 内的数值，长度相同的子区间具有相同的概率。

```text
U ~ Uniform(0, 1)

P(a <= U <= b) = b - a    for 0 <= a <= b <= 1

Properties:
  E[U] = 0.5
  Var(U) = 1/12
```

要从 n 个元素构成的离散集合中均匀抽样，生成 U 并返回 floor(n * U)。要从连续区间 [a, b] 中抽样，则计算 a + (b - a) * U。

关键认识是：一个均匀随机数所包含的随机性，恰好足以从任意分布中产生一个样本。诀窍在于找到合适的变换。

### 逆 CDF 方法（逆变换抽样）

累积分布函数（CDF）将数值映射为概率：

```text
F(x) = P(X <= x)

Properties:
  F is non-decreasing
  F(-inf) = 0
  F(+inf) = 1
  F maps the real line to [0, 1]
```

逆 CDF 将概率映射回数值。如果 U ~ Uniform(0, 1)，那么 X = F_inverse(U) 就服从目标分布。

```text
Algorithm:
  1. Generate u ~ Uniform(0, 1)
  2. Return F_inverse(u)

Why it works:
  P(X <= x) = P(F_inverse(U) <= x) = P(U <= F(x)) = F(x)
```

**指数分布示例：**

```text
PDF: f(x) = lambda * exp(-lambda * x),   x >= 0
CDF: F(x) = 1 - exp(-lambda * x)

Solve F(x) = u for x:
  u = 1 - exp(-lambda * x)
  exp(-lambda * x) = 1 - u
  x = -ln(1 - u) / lambda

Since (1 - U) and U have the same distribution:
  x = -ln(u) / lambda
```

当 F_inverse 可以写成闭式表达式时，这种方法非常有效。正态分布的逆 CDF 没有闭式表达式，因此我们使用其他方法，例如 Box-Muller 或数值近似。

**离散版本：** 对于离散分布，通过累加概率构建 CDF，生成 U，再找到累积和首次超过 U 的索引。第 06 课中的 `sample_categorical` 就是这样工作的。

### 拒绝抽样

如果无法求逆 CDF，但能计算目标概率密度函数（PDF），即使它还差一个常数因子，也可以使用拒绝抽样（rejection sampling）。

```text
Target distribution: p(x)  (can evaluate, possibly unnormalized)
Proposal distribution: q(x)  (can sample from)
Bound: M such that p(x) <= M * q(x) for all x

Algorithm:
  1. Sample x ~ q(x)
  2. Sample u ~ Uniform(0, 1)
  3. If u < p(x) / (M * q(x)), accept x
  4. Otherwise, reject and go to step 1

Acceptance rate = 1/M
```

界 M 越紧，接受率就越高。在低维（1-3）空间中，拒绝抽样表现良好；在高维空间中，大部分提议体积都会被拒绝，接受率会呈指数下降。这就是拒绝抽样中的维数灾难。

**示例：从截断正态分布中抽样。** 在截断区间上使用均匀提议分布（proposal distribution）。包络界 M 是该区间内正态 PDF 的最大值。

**示例：从半圆中抽样。** 在其外接矩形中均匀生成提议点。如果点落在半圆内，就接受它。Monte Carlo 就是这样计算 pi 的：接受率等于面积比 pi/4。

### 重要性抽样

有时你并不需要目标分布 p(x) 的样本，而是需要估计 p(x) 下的某个期望，手头却只有另一个分布 q(x) 的样本。

```text
Goal: estimate E_p[f(x)] = integral of f(x) * p(x) dx

Rewrite:
  E_p[f(x)] = integral of f(x) * (p(x)/q(x)) * q(x) dx
            = E_q[f(x) * w(x)]

where w(x) = p(x) / q(x)  are the importance weights.

Estimator:
  E_p[f(x)] ~ (1/N) * sum(f(x_i) * w(x_i))    where x_i ~ q(x)
```

这在强化学习中至关重要。在 PPO（Proximal Policy Optimization，近端策略优化）中，你使用旧策略 pi_old 收集轨迹，却希望优化新策略 pi_new。重要性权重为 pi_new(a|s) / pi_old(a|s)。PPO 会裁剪这些权重，防止新策略偏离旧策略太远。

重要性抽样估计量的方差取决于 q 与 p 有多相似。如果 q 与 p 差别很大，少量样本就会获得巨大的权重，主导估计结果。自归一化重要性抽样（self-normalized importance sampling）通过除以权重之和来缓解这一问题：

```text
E_p[f(x)] ~ sum(w_i * f(x_i)) / sum(w_i)
```

### Monte Carlo 估计

Monte Carlo（蒙特卡洛）估计通过对随机样本取平均来近似积分。大数定律保证其收敛。

```text
Goal: estimate I = integral of g(x) dx over domain D

Method:
  1. Sample x_1, ..., x_N uniformly from D
  2. I ~ (Volume of D / N) * sum(g(x_i))

Error: O(1 / sqrt(N))   regardless of dimension
```

误差收敛速率与维数无关。因此，在无法使用网格积分的高维空间中，Monte Carlo 方法占据主导地位。

**估计 pi：**

```text
Sample (x, y) uniformly from [-1, 1] x [-1, 1]
Count how many fall inside the unit circle: x^2 + y^2 <= 1
pi ~ 4 * (count inside) / (total count)
```

**估计期望：**

```text
E[f(X)] ~ (1/N) * sum(f(x_i))    where x_i ~ p(x)

The sample mean converges to the true expectation.
Variance of the estimator = Var(f(X)) / N
```

### 马尔可夫链蒙特卡洛（MCMC）：Metropolis-Hastings

MCMC 构造一条马尔可夫链（Markov chain），使其平稳分布为目标分布 p(x)。经过足够多步后，链上的样本就（近似）来自 p(x)。

```text
Target: p(x)  (known up to a normalizing constant)
Proposal: q(x'|x)  (how to propose the next state given the current state)

Metropolis-Hastings algorithm:
  1. Start at some x_0
  2. For t = 1, 2, ..., T:
     a. Propose x' ~ q(x'|x_t)
     b. Compute acceptance ratio:
        alpha = [p(x') * q(x_t|x')] / [p(x_t) * q(x'|x_t)]
     c. Accept with probability min(1, alpha):
        - If u < alpha (u ~ Uniform(0,1)): x_{t+1} = x'
        - Otherwise: x_{t+1} = x_t
  3. Discard first B samples (burn-in)
  4. Return remaining samples
```

对于对称提议分布（q(x'|x) = q(x|x')），这个比值简化为 p(x')/p(x)。这就是最初的 Metropolis 算法。

**原理。** 接受规则保证细致平衡（detailed balance）：处于 x 并转移到 x' 的概率，等于处于 x' 并转移到 x 的概率。细致平衡意味着 p(x) 是这条链的平稳分布。

**实践中的注意事项：**
- 预热期（burn-in）：丢弃链达到平衡之前的早期样本
- 抽稀（thinning）：每 k 个样本保留一个，以降低自相关
- 提议尺度：太小会使链移动缓慢（接受率高，但探索慢）；太大则会让大部分提议被拒绝（接受率低，停在原地）
- 高维空间中 Gaussian 提议分布的最优接受率约为 0.234

### Gibbs 抽样

Gibbs 抽样是面向多变量分布的一种特殊 MCMC 方法。它不会一次在所有维度上提议移动，而是每次从一个变量的条件分布中抽样，更新这个变量。

```text
Target: p(x_1, x_2, ..., x_d)

Algorithm:
  For each iteration t:
    Sample x_1^{t+1} ~ p(x_1 | x_2^t, x_3^t, ..., x_d^t)
    Sample x_2^{t+1} ~ p(x_2 | x_1^{t+1}, x_3^t, ..., x_d^t)
    ...
    Sample x_d^{t+1} ~ p(x_d | x_1^{t+1}, x_2^{t+1}, ..., x_{d-1}^{t+1})
```

Gibbs 抽样要求能够从每个条件分布 p(x_i | x_{-i}) 中抽样。对许多模型来说，这很直接：
- 贝叶斯网络：可根据图结构得到条件分布
- Gaussian 混合模型：条件分布为 Gaussian 分布
- Ising 模型：每个自旋的条件分布只依赖其邻居

接受率始终为 1（每个提议都被接受），因为从精确条件分布中抽样会自动满足细致平衡。

**局限。** 当变量之间高度相关时，Gibbs 抽样的混合速度很慢，因为每次只更新一个变量，无法沿对角线方向在分布中大幅移动。

### 温度采样（用于 LLM）

语言模型为词表中的各个 token 输出 logits z_1, ..., z_V。softmax 将其转换为概率。温度会在 softmax 之前对 logits 重新缩放：

```text
p_i = exp(z_i / T) / sum(exp(z_j / T))

T = 1.0: standard softmax (original distribution)
T -> 0:  argmax (deterministic, always picks highest logit)
T -> inf: uniform (all tokens equally likely)
T < 1.0: sharpens the distribution (more confident, less diverse)
T > 1.0: flattens the distribution (less confident, more diverse)
```

**原理。** 当 T < 1 时，将 logits 除以 T 会放大它们之间的差异。如果 z_1 = 2，z_2 = 1，除以 T = 0.5 后，就得到 z_1/T = 4 和 z_2/T = 2，差距因而变大。经过 softmax 后，logit 最高的 token 会获得大得多的概率份额。

**实际使用时：**
- T = 0.0：贪心解码，最适合事实性问答
- T = 0.3-0.7：略具创造性，适合代码生成
- T = 0.7-1.0：较为均衡，适合一般对话
- T = 1.0-1.5：创意写作、头脑风暴
- T > 1.5：随机性越来越强，很少有用

温度不会改变哪些 token 是可能的，只会改变分配给每个 token 的概率质量。

### Top-k 采样

Top-k 采样将候选集合限制为概率最高的 k 个 token，然后重新归一化，并从这个受限集合中采样。

```text
Algorithm:
  1. Compute softmax probabilities for all V tokens
  2. Sort tokens by probability (descending)
  3. Keep only the top k tokens
  4. Renormalize: p_i' = p_i / sum(p_j for j in top-k)
  5. Sample from the renormalized distribution

k = 1:  greedy decoding
k = V:  no filtering (standard sampling)
k = 40: typical setting, removes long tail of unlikely tokens
```

Top-k 防止模型选择词表概率分布长尾中那些极不可能的 token，例如拼写错误或无意义内容。问题在于，无论上下文如何，k 都是固定的。模型很有把握时（一个 token 的概率为 95%），k = 40 仍会允许另外 39 个选择；模型不确定时（概率分散在 1000 个 token 上），k = 40 又会排除一些合理选项。

### Top-p（核）采样

Top-p 采样会动态调整候选集合的大小。它保留的不是固定数量的 token，而是累积概率超过 p 的最小 token 集合。

```text
Algorithm:
  1. Compute softmax probabilities for all V tokens
  2. Sort tokens by probability (descending)
  3. Find smallest k such that sum of top-k probabilities >= p
  4. Keep only those k tokens
  5. Renormalize and sample

p = 0.9:  keeps tokens covering 90% of probability mass
p = 1.0:  no filtering
p = 0.1:  very restrictive, nearly greedy
```

模型很有把握时，核采样（nucleus sampling）只保留少量 token，可能只有 2-3 个；模型不确定时，则会保留很多，可能有 200 个。这种自适应行为，使核采样通常能生成比 top-k 更好的文本。

**常见组合：**
- 温度 0.7 + top-p 0.9：适合一般用途的设置
- 温度 0.0（贪心）：最适合确定性任务
- 温度 1.0 + top-k 50：Fan 等人（2018）原始论文中的设置

Top-k 和 top-p 可以组合使用。先应用 top-k，再对剩余集合应用 top-p。

### 重参数化技巧（用于 VAE）

变分自编码器（VAE）先将输入编码为潜在空间中的一个分布，再从这个分布抽样，最后将样本解码回来，以此进行学习。问题是：无法直接让反向传播穿过抽样操作。

```text
Standard sampling (not differentiable):
  z ~ N(mu, sigma^2)

  The randomness blocks gradient flow.
  d/d_mu [sample from N(mu, sigma^2)] = ???
```

重参数化技巧（reparameterization trick）将随机性与参数分离：

```text
Reparameterized sampling:
  epsilon ~ N(0, 1)          (fixed random noise, no parameters)
  z = mu + sigma * epsilon   (deterministic function of parameters)

  Now z is a deterministic, differentiable function of mu and sigma.
  d(z)/d(mu) = 1
  d(z)/d(sigma) = epsilon

  Gradients flow through mu and sigma.
```

这种方法之所以有效，是因为 N(mu, sigma^2) 与 mu + sigma * N(0, 1) 具有相同的分布。关键在于：把随机性移到一个不含参数的来源（epsilon），再把样本表示为参数的可微变换。

**在 VAE 训练循环中：**
1. 编码器为每个输入输出 mu 和 log(sigma^2)
2. 抽取 epsilon ~ N(0, 1)
3. 计算 z = mu + sigma * epsilon
4. 对 z 解码，重构输入
5. 依次通过步骤 4、3、2、1 进行反向传播（因为步骤 3 可微，所以能够做到）

没有重参数化技巧，VAE 就无法用标准反向传播训练。正是这一认识让 VAE 变得实用。

### Gumbel-Softmax（可微类别抽样）

重参数化技巧适用于连续分布（Gaussian 分布）。对于离散的类别分布，需要另一种方法。Gumbel-Softmax 提供了类别抽样的可微近似。

**Gumbel-Max 技巧（不可微）：**

```text
To sample from a categorical distribution with log-probabilities log(p_1), ..., log(p_k):
  1. Sample g_i ~ Gumbel(0, 1) for each category
     (g = -log(-log(u)), where u ~ Uniform(0, 1))
  2. Return argmax(log(p_i) + g_i)

This produces exact categorical samples.
```

**Gumbel-Softmax（可微近似）：**

```text
Replace the hard argmax with a soft softmax:
  y_i = exp((log(p_i) + g_i) / tau) / sum(exp((log(p_j) + g_j) / tau))

tau (temperature) controls the approximation:
  tau -> 0:  approaches a one-hot vector (hard categorical)
  tau -> inf: approaches uniform (1/k, 1/k, ..., 1/k)
  tau = 1.0: soft approximation
```

Gumbel-Softmax 给出离散样本的连续松弛。其输出是概率向量，也就是软 one-hot（独热）向量，而不是硬 one-hot 向量。梯度可以穿过 softmax。在训练的前向传播中，可以使用“直通”估计器（straight-through estimator）：前向传播使用硬 argmax，反向传播则使用软 Gumbel-Softmax 的梯度。

**应用场景：**
- VAE 中的离散潜变量
- 神经架构搜索（选择离散操作）
- 硬注意力机制
- 使用离散动作的强化学习

### 分层抽样

标准 Monte Carlo 抽样可能偶然在样本空间中留下空隙。分层抽样（stratified sampling）将空间划分为若干层，并从每一层中抽样，以此强制均匀覆盖。

```text
Standard Monte Carlo:
  Sample N points uniformly from [0, 1]
  Some regions may have clusters, others gaps

Stratified sampling:
  Divide [0, 1] into N equal strata: [0, 1/N), [1/N, 2/N), ..., [(N-1)/N, 1)
  Sample one point uniformly within each stratum
  x_i = (i + u_i) / N   where u_i ~ Uniform(0, 1),  i = 0, ..., N-1
```

与标准 Monte Carlo 相比，分层抽样的方差始终更低或相等：

```text
Var(stratified) <= Var(standard Monte Carlo)

The improvement is largest when f(x) varies smoothly.
For piecewise-constant functions, stratified sampling is exact.
```

**应用场景：**
- 数值积分（准 Monte Carlo）
- 训练数据划分（确保每一折中的类别均衡）
- 带分层的重要性抽样（结合两种技术）
- NeRF（Neural Radiance Fields，神经辐射场）沿相机射线使用分层抽样

### 与扩散模型的联系

扩散模型通过抽样过程生成图像。前向过程经过 T 步向图像添加 Gaussian 噪声，直到图像变成纯噪声。反向过程学习去噪，逐步恢复原始图像。

```text
Forward process (known):
  x_t = sqrt(alpha_t) * x_{t-1} + sqrt(1 - alpha_t) * epsilon
  where epsilon ~ N(0, I)

  After T steps: x_T ~ N(0, I)  (pure noise)

Reverse process (learned):
  x_{t-1} = (1/sqrt(alpha_t)) * (x_t - (1 - alpha_t)/sqrt(1 - alpha_bar_t) * epsilon_theta(x_t, t)) + sigma_t * z
  where z ~ N(0, I)

  Each denoising step is a sampling step.
```

它与本课方法的联系：
- 每个去噪步骤都使用重参数化技巧（抽取噪声，再进行确定性变换）
- 噪声调度 {alpha_t} 控制了一种温度退火过程
- 训练使用 Monte Carlo 估计来近似 ELBO（证据下界）
- 扩散模型中的祖先抽样（ancestral sampling）是一条马尔可夫链（每一步仅依赖当前状态）

整个图像生成过程就是迭代抽样：从噪声开始，每一步都以学习得到的去噪模型为条件，抽取一个噪声略少的版本。

```figure
monte-carlo-pi
```

## 动手实现

### 步骤 1：均匀抽样与逆 CDF 抽样

```python
import math
import random

def sample_uniform(a, b):
    return a + (b - a) * random.random()

def sample_exponential_inverse_cdf(lam):
    u = random.random()
    return -math.log(u) / lam
```

生成 10,000 个指数分布样本，验证均值为 1/lambda。

### 步骤 2：拒绝抽样

```python
def rejection_sample(target_pdf, proposal_sample, proposal_pdf, M):
    while True:
        x = proposal_sample()
        u = random.random()
        if u < target_pdf(x) / (M * proposal_pdf(x)):
            return x
```

使用拒绝抽样，从截断正态分布中抽取样本。对样本绘制直方图，验证其形状。

### 步骤 3：重要性抽样

```python
def importance_sampling_estimate(f, target_pdf, proposal_pdf, proposal_sample, n):
    total = 0
    for _ in range(n):
        x = proposal_sample()
        w = target_pdf(x) / proposal_pdf(x)
        total += f(x) * w
    return total / n
```

使用均匀提议分布估计正态分布下的 E[X^2]，并与已知答案（mu^2 + sigma^2）比较。

### 步骤 4：用 Monte Carlo 估计 pi

```python
def monte_carlo_pi(n):
    inside = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y <= 1:
            inside += 1
    return 4 * inside / n
```

### 步骤 5：Metropolis-Hastings MCMC

```python
def metropolis_hastings(target_log_pdf, proposal_sample, proposal_log_pdf, x0, n_samples, burn_in):
    samples = []
    x = x0
    for i in range(n_samples + burn_in):
        x_new = proposal_sample(x)
        log_alpha = (target_log_pdf(x_new) + proposal_log_pdf(x, x_new)
                     - target_log_pdf(x) - proposal_log_pdf(x_new, x))
        if math.log(random.random()) < log_alpha:
            x = x_new
        if i >= burn_in:
            samples.append(x)
    return samples
```

从双峰分布（两个 Gaussian 分布的混合）中抽样，并可视化这条链的轨迹。

### 步骤 6：Gibbs 抽样

```python
def gibbs_sampling_2d(conditional_x_given_y, conditional_y_given_x, x0, y0, n_samples, burn_in):
    x, y = x0, y0
    samples = []
    for i in range(n_samples + burn_in):
        x = conditional_x_given_y(y)
        y = conditional_y_given_x(x)
        if i >= burn_in:
            samples.append((x, y))
    return samples
```

### 步骤 7：温度采样

```python
def softmax(logits):
    max_l = max(logits)
    exps = [math.exp(z - max_l) for z in logits]
    total = sum(exps)
    return [e / total for e in exps]

def temperature_sample(logits, temperature):
    scaled = [z / temperature for z in logits]
    probs = softmax(scaled)
    return sample_from_probs(probs)
```

展示温度如何改变一组 token logits 对应的输出分布。

### 步骤 8：Top-k 与 top-p 采样

```python
def top_k_sample(logits, k):
    indexed = sorted(enumerate(logits), key=lambda x: -x[1])
    top = indexed[:k]
    top_logits = [l for _, l in top]
    probs = softmax(top_logits)
    idx = sample_from_probs(probs)
    return top[idx][0]

def top_p_sample(logits, p):
    probs = softmax(logits)
    indexed = sorted(enumerate(probs), key=lambda x: -x[1])
    cumsum = 0
    selected = []
    for token_idx, prob in indexed:
        cumsum += prob
        selected.append((token_idx, prob))
        if cumsum >= p:
            break
    sel_probs = [pr for _, pr in selected]
    total = sum(sel_probs)
    sel_probs = [pr / total for pr in sel_probs]
    idx = sample_from_probs(sel_probs)
    return selected[idx][0]
```

### 步骤 9：重参数化技巧

```python
def reparam_sample(mu, sigma):
    epsilon = random.gauss(0, 1)
    return mu + sigma * epsilon

def reparam_gradient(mu, sigma, epsilon):
    dz_dmu = 1.0
    dz_dsigma = epsilon
    return dz_dmu, dz_dsigma
```

展示梯度能够穿过重参数化后的样本，却无法穿过直接抽样。

### 步骤 10：Gumbel-Softmax

```python
def gumbel_sample():
    u = random.random()
    return -math.log(-math.log(u))

def gumbel_softmax(logits, temperature):
    gumbels = [math.log(p) + gumbel_sample() for p in logits]
    return softmax([g / temperature for g in gumbels])
```

展示随着温度降低，输出如何趋近 one-hot 向量。

包含所有可视化的完整实现见 `code/sampling.py`。

## 实际使用

使用 NumPy 和 SciPy 的生产版本如下：

```python
import numpy as np

rng = np.random.default_rng(42)

exponential_samples = rng.exponential(scale=2.0, size=10000)
print(f"Exponential mean: {exponential_samples.mean():.4f} (expected 2.0)")

from scipy import stats
normal = stats.norm(loc=0, scale=1)
print(f"CDF at 1.96: {normal.cdf(1.96):.4f}")
print(f"Inverse CDF at 0.975: {normal.ppf(0.975):.4f}")

logits = np.array([2.0, 1.0, 0.5, 0.1, -1.0])
temperature = 0.7
scaled = logits / temperature
probs = np.exp(scaled - scaled.max()) / np.exp(scaled - scaled.max()).sum()
token = rng.choice(len(logits), p=probs)
print(f"Sampled token index: {token}")
```

要进行大规模 MCMC，可使用专门的库：
- PyMC：使用 NUTS（自适应 HMC）进行完整的贝叶斯建模
- emcee：集成 MCMC 抽样器
- NumPyro/JAX：GPU 加速的 MCMC

你已经从零构建过这些方法，现在知道库函数调用背后在做什么了。

## 练习

1. 为 Cauchy 分布实现逆 CDF 抽样。CDF 为 F(x) = 0.5 + arctan(x)/pi。生成 10,000 个样本，将其直方图与真实 PDF 对照。观察重尾现象，即远离中心的极端值。

2. 使用 Uniform(0, 1) 提议分布，通过拒绝抽样生成 Beta(2, 5) 分布的样本。将接受样本的图与真实 Beta PDF 对照。理论接受率是多少？

3. 分别使用 1,000、10,000 和 100,000 个样本，用 Monte Carlo 估计 sin(x) 从 0 到 pi 的积分。比较各个样本量下的误差，验证误差按 O(1/sqrt(N)) 的速率变化。

4. 实现 Metropolis-Hastings，从一个 2D 分布中抽样，其 p(x, y) 正比于 exp(-(x^2 * y^2 + x^2 + y^2 - 8*x - 8*y) / 2)。绘制样本和链轨迹，并尝试不同的提议标准差。

5. 构建完整的文本生成演示：给定一个含 10 个单词及其 logits 的词表，分别使用 (a) 贪心、(b) temperature=0.7、(c) top-k=3、(d) top-p=0.9 生成长度为 20 个 token 的序列。比较 5 次运行中输出的多样性。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|----------------------|
| 抽样 | “抽取随机值” | 按概率分布生成数值，是所有生成式 AI 背后的机制 |
| 均匀分布 | “所有值等可能” | [a, b] 中每个值的概率密度均为 1/(b-a)，是所有抽样方法的起点 |
| 逆 CDF | “概率变换” | F_inverse(U) 将均匀分布样本转换为任意已知 CDF 分布的样本，精确且高效 |
| 拒绝抽样 | “提议并接受或拒绝” | 从简单的提议分布生成样本，以正比于目标分布与提议分布之比的概率接受；精确，但会浪费样本 |
| 重要性抽样 | “重新加权样本” | 用 q(x) 的样本估计 p(x) 下的期望，每个样本的权重为 p(x)/q(x)，是强化学习中 PPO 的核心 |
| Monte Carlo | “对随机样本取平均” | 用样本平均近似积分，无论维数多少，误差均为 O(1/sqrt(N)) |
| MCMC | “会收敛的随机游走” | 构造一条以目标分布为平稳分布的马尔可夫链；Metropolis-Hastings 是基础算法 |
| Metropolis-Hastings | “向高密度处总是接受，向低密度处有时接受” | 提议移动，根据密度比接受；细致平衡保证收敛到目标分布 |
| Gibbs 抽样 | “一次更新一个变量” | 固定其他变量，从条件分布更新每个变量，接受率为 100% |
| 温度 | “置信程度调节器” | 在 softmax 之前将 logits 除以 T。T<1 使分布更尖锐（更有把握），T>1 使分布更平坦（更多样） |
| Top-k 采样 | “保留最好的 k 个” | 除概率最高的 k 个 token 外，其余概率均归零，然后重新归一化并采样；候选集合大小固定 |
| 核采样（top-p） | “保留概率较高的” | 保留累积概率超过 p 的最小 token 集合，候选集合大小自适应 |
| 重参数化技巧 | “将随机性移到外面” | 写成 z = mu + sigma * epsilon，其中 epsilon ~ N(0,1)，使抽样可微，是 VAE 训练的关键 |
| Gumbel-Softmax | “软类别抽样” | 利用 Gumbel 噪声加带温度的 softmax，对类别抽样进行可微近似 |
| 分层抽样 | “强制覆盖” | 将样本空间划分为若干层，分别抽样；方差始终低于朴素 Monte Carlo |
| 预热期 | “热身阶段” | 在链达到平稳分布之前丢弃的早期 MCMC 样本 |
| 细致平衡 | “可逆性条件” | p(x) * T(x->y) = p(y) * T(y->x)，是 p 成为马尔可夫链平稳分布的充分条件 |
| 扩散抽样 | “迭代去噪” | 从噪声出发，应用学习得到的去噪步骤来生成数据；每一步都是一次条件抽样操作 |

## 延伸阅读

- [Holbrook（2023）：Metropolis-Hastings 算法](https://arxiv.org/abs/2304.07010) - MCMC 基础的详细教程
- [Jang、Gu、Poole（2017）：使用 Gumbel-Softmax 进行类别重参数化](https://arxiv.org/abs/1611.01144) - Gumbel-Softmax 原始论文
- [Holtzman 等（2020）：神经文本退化的奇特现象](https://arxiv.org/abs/1904.09751) - 核（top-p）采样论文
- [Kingma 与 Welling（2014）：自编码变分 Bayes](https://arxiv.org/abs/1312.6114) - 引入重参数化技巧的 VAE 论文
- [Ho、Jain、Abbeel（2020）：去噪扩散概率模型](https://arxiv.org/abs/2006.11239) - DDPM 将抽样与图像生成联系起来
