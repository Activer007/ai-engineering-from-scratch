# LLM API 负载测试：为什么 k6 和 Locust 会给出误导性结果

> 传统负载测试（load test）工具并非为流式响应、可变输出长度、token（词元）级指标或 GPU 饱和而设计。大多数团队会踩进两个陷阱。第一个是 GIL（全局解释器锁）陷阱：Locust 的 token 级测量在 Python GIL 下执行分词，高并发时会与请求生成争用执行机会；分词积压进而抬高报告中的 token 间延迟，此时瓶颈在客户端而非服务器。第二个是提示词单一化陷阱：循环发送完全相同的提示词（prompt），只测试了 token 分布中的一个点，而真实流量的长度和前缀匹配情况多种多样。LLMPerf 用 `--mean-input-tokens` + `--stddev-input-tokens` 解决这个问题。2026 年的工具分工：大语言模型（LLM）专用工具（GenAI-Perf、LLMPerf、LLM-Locust、guidellm）用于准确的 token 级测量；**k6 v2026.1.0** + **k6 Operator 1.0 GA (Sept 2025)** 支持流式测量，通过 TestRun/PrivateLoadZone CRD（自定义资源定义）提供 Kubernetes 原生分布式测试，最适合 CI/CD 门禁；用 Go 实现的 Vegeta 用于恒定速率饱和测试；Locust 2.43.3 只有配合 LLM-Locust 扩展才适合流式测试。负载模式包括稳态、渐增、突增（测试自动扩缩容）和长时间稳态运行（检测内存泄漏）。

**Type:** Build
**Languages:** Python (stdlib, toy realistic-prompt generator + latency collector)
**Prerequisites:** 阶段 17 · 08（推理指标）、阶段 17 · 03（GPU 自动扩缩容）
**Time:** ~75 分钟

## 学习目标

- 解释使通用负载测试工具对 LLM API（应用程序编程接口）给出误导性结果的两种反模式：GIL 陷阱和提示词单一化陷阱。
- 根据用途选择工具：LLMPerf（基准测试）、k6 + 流式扩展（CI 门禁）、guidellm（大规模合成测试）、GenAI-Perf（NVIDIA 参考工具）。
- 设计四种负载模式（稳态、渐增、突增、长时间稳态运行），并指出各自能发现的故障类型。
- 使用输入 token 数的均值和标准差构造接近真实情况的提示词分布，而不是固定长度。

## 要解决的问题

你用 k6 对 LLM 端点（endpoint）进行了 500 个并发用户的测试。服务撑住了，于是你上线了。然而到了生产环境，200 个真实用户就让服务崩溃：P99 TTFT（首 token 延迟）飙升，GPU 满载。

这里发生了两件事。首先，k6 发送了 500 条完全相同的提示词；请求合并和前缀缓存让系统看起来像是在处理 500 路并发解码，实际上只处理了一路。其次，k6 对流式响应 token 间延迟的追踪方式与人实际看到的节奏不同；它看到的是一条 HTTP 连接，而不是以不同时间间隔到达的 500 个 token。

LLM 负载测试需要专门的方法。

## 核心概念

### GIL 陷阱（Locust）

Locust 使用 Python，在客户端的 GIL 下执行分词。高并发时，分词器（tokenizer）的任务排在请求生成之后。报告中的 token 间延迟包含客户端分词积压造成的等待。你以为服务器慢，实际上慢的是测试框架。

解决办法：用 LLM-Locust 扩展将分词移到独立进程，或者使用编译型语言实现的测试框架（k6，或使用 tokenizers.rs 的 LLMPerf）。

### 提示词单一化陷阱

所有已知的负载测试工具都允许配置一条提示词。在循环 10,000 次的测试中，每次都发送同一条提示词。服务器每次看到的前缀相同，前缀缓存命中率接近 100%，吞吐量看起来很好。

解决办法：从提示词分布中采样。LLMPerf 使用 `--mean-input-tokens 500 --stddev-input-tokens 150`，使长度和内容都具有多样性。

### 四种负载模式

1. **稳态（steady-state）**：维持恒定 RPS（每秒请求数）运行 30-60 min。用于发现基线性能退化。
2. **渐增（ramp）**：将 RPS 从 0 线性增加到目标值，历时 15 min。用于发现容量临界点和预热异常。
3. **突增（spike）**：RPS 突然增至原来的 3-10x，持续 2 min 后恢复。用于发现自动扩缩容延迟、队列饱和及冷启动的影响。
4. **长时间稳态运行（soak）**：维持稳态运行 4-8 hours。用于发现内存泄漏、连接池漂移和可观测性系统的溢出。

### 2026 年的工具分工

**LLMPerf**（Anyscale）：用 Python 编写，但分词由 Rust 实现。支持按均值/标准差生成提示词，支持流式测量，是进行性能测试时的首选默认工具。

**NVIDIA GenAI-Perf**：NVIDIA 的参考工具。使用 Triton 客户端，指标覆盖全面。注意，它的 ITL（token 间延迟）不包含 TTFT，而 LLMPerf 的包含。因此，对同一台服务器，两种工具会给出不同的 TPOT（每个输出 token 的耗时）。

**LLM-Locust**（TrueFoundry）：解决 GIL 陷阱的 Locust 扩展。保留熟悉的 Locust DSL（领域专用语言），并加入流式指标。

**guidellm**：用于大规模合成基准测试。

**k6 v2026.1.0** + **k6 Operator 1.0 GA (Sept 2025)**：
- k6 本身用 Go 编译实现，没有 GIL，并增加了面向流式响应的指标。
- k6 Operator 使用 TestRun / PrivateLoadZone CRD 进行 Kubernetes 原生分布式测试。
- 最适合 CI/CD 门禁与 SLA（服务等级协议）测试。

**Vegeta**：用 Go 编写，比 k6 更简单。用于恒定速率的 HTTP 饱和测试。不专门针对 LLM，但适合网关/速率限制（rate limit）测试。

**原版 Locust 2.43.3**：用于 LLM 测试时存在 GIL 陷阱，需搭配 LLM-Locust 扩展。

### CI 中的 SLA 门禁

针对 PR 运行 k6，要求如下：

- 在基线 RPS 下，每次执行 30-50 次迭代。
- 门禁指标：P50/P95 TTFT、5xx < 5%、TPOT 低于阈值。
- 任一指标越界就让构建失败。

### 接近真实情况的提示词分布

如果有真实流量样本，就据此构造分布；否则可使用公开分布，例如用于聊天的 ShareGPT 提示词、用于代码的 HumanEval。将均值和标准差传给 LLMPerf。务必避免循环发送同一条提示词。

### 需要记住的数值

- k6 Operator 1.0 GA：September 2025。
- k6 v2026.1.0：面向流式响应的指标。
- 典型的 LLMPerf 测试：并发数为 X，发送 100-1000 个请求。
- 典型的 CI 门禁：每个 PR 执行 30-50 次迭代。
- 四种模式：稳态、渐增、突增、长时间稳态运行。

```figure
load-pattern-waves
```

## 实际使用

`code/main.py` 使用接近真实情况的提示词分布模拟负载测试，测量实际 TPOT，并演示提示词单一化陷阱。

## 交付成果

本课产出 `outputs/skill-load-test-plan.md`。它根据工作负载和 SLA 选择工具，并设计四种负载模式。

## 练习

1. 运行 `code/main.py`。对比单一提示词与接近真实情况的分布，差距在哪里？
2. 编写用于 CI 门禁的 k6 脚本：TTFT P95 < 800 ms，并发数为 100，运行时间为 5 minutes。
3. 长时间稳态测试显示，内存以 50 MB/hour 的速度增长。列出三种可能原因，以及可用于区分它们的观测手段。
4. 将负载从 10 RPS 突增到 100 RPS。如果已部署 Karpenter + vLLM production-stack（阶段 17 · 03 + 18），预期恢复时间是多少？
5. 对同一台服务器，GenAI-Perf 报告 TPOT=6ms，LLMPerf 报告 TPOT=11ms。请解释原因。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|------------------------|
| LLMPerf | “LLM 测试框架” | Anyscale 的基准测试工具，支持流式测量 |
| GenAI-Perf | “NVIDIA 工具” | NVIDIA 的参考测试框架 |
| LLM-Locust | “面向 LLM 的 Locust” | 解决 GIL 陷阱的 Locust 扩展 |
| guidellm | “合成基准测试” | 大规模合成测试工具 |
| k6 Operator | “K8s k6” | 基于 CRD 的分布式 k6 |
| GIL 陷阱 | “Python 客户端开销” | 分词积压抬高报告中的延迟 |
| 提示词单一化陷阱 | “单提示词假象” | 循环使用同一提示词导致缓存命中，抬高吞吐量 |
| 稳态 | “恒定负载” | RPS 保持不变，持续 N 分钟 |
| 渐增 | “线性上升” | 在一段时间内从 0 增至目标值 |
| 突增 | “突发测试” | 负载突然按倍数增加，然后恢复 |
| 长时间稳态运行 | “长时间测试” | 持续数小时以检测泄漏 |

## 延伸阅读

- [TianPan：LLM 应用负载测试](https://tianpan.co/blog/2026-03-19-load-testing-llm-applications)
- [PremAI：2026 年 LLM 负载测试](https://blog.premai.io/load-testing-llms-tools-metrics-realistic-traffic-simulation-2026/)
- [NVIDIA NIM：LLM 推理基准测试入门](https://docs.nvidia.com/nim/large-language-models/1.0.0/benchmarking.html)
- [TrueFoundry — LLM-Locust](https://www.truefoundry.com/blog/llm-locust-a-tool-for-benchmarking-llm-performance)
- [LLMPerf](https://github.com/ray-project/llmperf)
- [k6 Operator](https://github.com/grafana/k6-operator)
