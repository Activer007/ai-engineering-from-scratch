# S82 调试与性能剖析术语增量

2026-10-03。唯一课文来源为固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb` 的 `00-12`。联用核心、补充表与 87 项固定支持，重点承接 S69 的 PyTorch、S73 的神经网络调试、S15 的数值稳定性及 S32 的反向传播术语；不读取或复用旧中文课文。术语选择不修正英文技术结论。

| English | 中文或保留形式 | 语境与保护边界 |
|---|---|---|
| debugging / bug / silent bug | 调试 / 缺陷 / 静默缺陷（silent bug） | 沿 S73；程序无异常而结果错误，不译成安全漏洞 |
| profiling / profiler | 性能剖析（profiling）/ 性能剖析器（profiler） | 观察耗时或资源开销，与排查正确性的调试分开；题名采用“调试与性能剖析” |
| print debugging / logging | 打印调试 / 日志记录 | 临时打印与可配置日志分开；`debug_print`、`logging` 原样 |
| breakpoint / conditional debugging | 断点 / 条件调试 | 条件满足时暂停；`breakpoint()`、`pdb` 和调试命令不译 |
| stack trace / root cause | 调用栈信息（stack trace）/ 根本原因 | 异常调用链与性能调用统计不同，不将推测写成已证实诊断 |
| tensor / shape / dtype / device | 张量（tensor）/ 形状（shape）/ 数据类型（dtype）/ 设备（device） | 沿 S69；维度元组、类型和设备标识符保持源形 |
| shape mismatch / device mismatch | 形状不匹配 / 设备不匹配 | 轴尺寸与设备位置不同；`[batch, features]` 等表达式原样 |
| training loop / training dynamics | 训练循环 / 训练动态 | 程序循环与损失、激活值、梯度随训练的变化分开 |
| loss curve / loss spike / oscillation | 损失曲线 / 损失突增 / 振荡 | 沿 S58/S73；只保留源诊断语气，不额外保证某现象只有一种原因 |
| forward pass / backward pass | 前向传播 / 反向传播 | 沿 S32/S69；反向传播计算梯度，不等同优化器更新 |
| gradient norm / gradient distribution | 梯度范数 / 梯度分布 | 数值大小与直方图分布不同，不能当成权重分布 |
| vanishing / exploding gradients | 梯度消失 / 梯度爆炸 | 沿 S32/S73；不把权重直方图直接等同梯度的完整诊断证据 |
| gradient clipping / gradient checkpointing | 梯度裁剪 / 梯度检查点（gradient checkpointing） | 沿 S15/S32；后者重算中间激活，区别梯度检查和保存训练状态 |
| data leakage / temporal leakage | 数据泄漏 / 时间泄漏（temporal leakage） | 沿 S17/S73；后者在本课指用未来数据预测过去；不把高准确率本身当泄漏证明 |
| train / validation / test set | 训练集 / 验证集 / 测试集 | 沿 S04/S39；代码 `train`、`val`、`test` 标识不译 |
| data loading / preprocessing pipeline | 数据加载 / 预处理管线 | pipeline 沿 S57/S73 的管线用法，不译成流水线并行 |
| bottleneck / cumulative time | 瓶颈 / 累计耗时 | 资源瓶颈须按源对象；函数累计耗时与逐行耗时不同 |
| memory profiling / memory allocation | 内存剖析 / 内存分配 | CPU 内存与 GPU 显存分别说明，不承诺 `tracemalloc` 覆盖全部原生张量分配 |
| allocated / cached / reserved memory | 已分配内存 / 缓存内存 / 预留内存 | 按源各自措辞，不把活跃张量内存和分配器缓存静默合并；API 保持 |
| OOM / NaN / Inf | OOM（内存不足）/ NaN（非数）/ Inf（无穷大） | 沿 S02/S15；OOM 不默认只指 GPU，代码大小写原样 |
| mixed precision / numerical instability | 混合精度 / 数值不稳定 | 沿 S15/S69；精度方案与减小全部内存一半的源概括分开记录 |
| hook / handle / histogram | 钩子（hook）/ 句柄 / 直方图 | 前两项沿 S73；回调资源与可视化分布不同 |
| overfitting / learning rate / batch size | 过拟合 / 学习率 / 批量大小 | 沿 S22/S58/S69；训练损失、验证损失、每步样本数不可互换 |
| severity level / gutter / Variables pane / Debug Console | 严重级别 / 行号旁区域 / Variables 窗格 / Debug Console（调试控制台） | 日志等级与编辑器可见 UI；保留 UI 名称便于定位 |

保留 Python、PyTorch、TensorBoard、VS Code、DataLoader、RNN、CPU、GPU、CUDA、SGD、Adam，以及 `cProfile`、`line_profiler`、`memory_profiler`、`tracemalloc`、`debugpy`、`SummaryWriter`、`Timer`、所有 API、命令、路径、配置键和字符串。首次正文按语境解释英文术语，不强译产品或模块名。

通用标题采用：学习目标、要解决的问题、核心概念、动手实现、实际使用、交付成果、练习。英文没有的关键术语或延伸阅读章节不补造。`Part 1` 至 `Part 9` 的数字逐一保留。元数据 `~60 minutes` 等值译 `~60 分钟`；`8 hours` 译 `8 小时`；`3 AM` 译 `凌晨 3 点`，均不改数值或时段。正文 three/first/once 等自然语言数量按三/第一/一次等值处理；`$200`、`80%`、`60%`、`99%`、`10,000`、各步骤数字、公式、单位符号与围栏负载保持源形。强调闭合符后保留必要空格，图和输出提示词原字节保护。
