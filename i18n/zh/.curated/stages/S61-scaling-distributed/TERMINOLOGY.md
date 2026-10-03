# S61 分布式扩展术语增量 v1.0

2026-10-03。联用核心术语、补充表及S03/S43/S45已固定术语；来源仅固定英文10-05。保留源数值/单位、公式、代码、链接、图负载与事实局限。通用章节依补充表。

| EN | 推荐呈现 | 语境与边界 |
|---|---|---|
| distributed training | 分布式训练（distributed training） | 多设备协同；CPU模拟不等于真实多GPU训练 |
| data / tensor / pipeline parallelism | 数据并行 / 张量并行 / 流水线并行 | 首次正文中英；分别分数据、矩阵、层组，不能混同 |
| shard / sharding | 分片 / 分片处理 | 局部数据或模型状态；非等长分片均值的源问题另列 |
| FSDP | 完全分片数据并行（FSDP） | Fully Sharded Data Parallel，保留缩写 |
| DDP | 分布式数据并行（DDP） | PyTorch名称；目标提及不等于交付真实实现 |
| all-reduce | 全归约（all-reduce） | 集合通信求和或平均；ring为环形 |
| all-gather | 全收集（all-gather） | 各设备得到完整拼接数据 |
| reduce-scatter | 归约散发（reduce-scatter） | 归约并将不同块分给不同设备 |
| pipeline bubble / micro-batch | 流水线气泡 / 微批次 | 等待导致空闲；源气泡公式与模拟差异另列 |
| optimizer states / master weights | 优化器状态 / 主权重 | Adam一、二阶矩与FP32主副本分开核算；源遗漏不修正文 |
| activation checkpointing | 激活检查点 | 反向时重算激活；不等于模型检查点或减小模型状态 |
| mixed precision / loss scaling | 混合精度 / 损失缩放 | 溢出/下溢语境；不保证所有内存减半 |
| column-parallel / row-parallel | 列并行 / 行并行 | 输出维分割后拼接，输入维分割后求和 |
| Mixture of Experts | 混合专家（Mixture of Experts） | 活跃参数与总存储参数不同 |
| offload | 卸载 | GPU状态移至CPU RAM或NVMe；非删除 |
| first / second moment | 一阶矩 / 二阶矩 | 源另称running variance处照译滚动方差并登记问题 |

token首次解释为token（词元）；GB/MB/TB、FP16/BF16/FP32、NVLink、InfiniBand、NCCL、ZeRO、DeepSpeed、Megatron-LM、GPipe、PipeDream均保留。自然语言million/billion保留源英文单位并解释百万/十亿，M/B/K原样；英文文字数量以等值中文表达。~120 minutes译~120 分钟。成本/硬件/吞吐数值只保留源陈述，不作为本次实测或当前报价。
