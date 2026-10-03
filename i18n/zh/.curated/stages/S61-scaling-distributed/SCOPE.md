# S61 范围与安全门槛

2026-10-03。独占课程10-05。英文源固定提交1bafaa88bb4668356791150bec3a6d7df38387eb，路径phases/10-llms-from-scratch/05-scaling-distributed/docs/en.md，SHA256 b9ae0ccea1f097aa7d3715f6578a007b167d065be32530ebb83dec516b2ca406。唯一正文目标为i18n/zh/phases/10-llms-from-scratch/05-scaling-distributed/docs/zh.md。572行，201语义块，10围栏（3 Mermaid、1 figure、6 Python），无引用SVG。

先修10-04已在协调者核验的78课闭环中；S45术语提供Mini GPT、梯度累积、激活与显存语境。S43优化器及S03 GPU术语已读。仅沿用术语，不读取旧中文课文、翻译缓存或PR452/457。保留固定英文技术问题，另列报告，绝不暗修正文。

DEPENDENCIES.json的66项控制/术语文件逐一核验工作区SHA256和固定Git字节，不改清单、不改校验器。

执行限离线CPU、stdlib/NumPy有限夹具，外部timeout和单线程BLAS。已完整预读main.py；默认8192×8192 float64权重约512MiB，禁止默认main入口和正文run_all_demos。允许小尺寸DP/TP及有限pipeline/内存/混精/通信成本算术；明确不能代表默认执行或真实集群。不得GPU、多进程分布式、PyTorch/DeepSpeed生产执行、云资源、网络、安装、下载或运行outputs提示词。

原strict、33控制、两新目录重放精确字节比较为本地门槛。实际GitHub GFM待协调者发布实读；课程网站、移动端、figure交互和托管CI均未通过。book PDF缺xelatex.fmt为已知环境阻塞，不安装软件修补。本作者只交付本地draft，不写独立review、不提交远端/PR/总索引。
