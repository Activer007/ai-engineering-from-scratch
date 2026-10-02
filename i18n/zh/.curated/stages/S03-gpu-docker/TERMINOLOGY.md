# S03 GPU与Docker术语增量 v1.0

2026-10-02。固定英文00/03与00/07的语境；联用核心、试点及S01/S02术语。产品名、型号、硬件缩写、代码、字段、flags、路径、镜像tag、平台架构和数值/单位保持原样，首次可译正文用中文解释。

| EN | 推荐呈现 | 语境 / 不可混淆项 |
|---|---|---|
| GPU / CPU | GPU（图形处理器）/ CPU（中央处理器） | 缩写保留；不把并行执行泛化为任何任务都更快 |
| CUDA / cuDNN / MPS | 保留原名，按上下文解释 | 不把CUDA误作驱动版本；MPS为Apple GPU后端 |
| VRAM | VRAM（显存） | GPU内存，不等同系统RAM |
| fp16 / fp32 | fp16（半精度）/ fp32（单精度） | 数字与类型标识保留；容量估算适用范围另列源问题 |
| Tensor Core | Tensor Core（张量核心） | GPU特定矩阵硬件单元，非一般CPU核心 |
| benchmark / speedup | 基准测试 / 加速比 | 实测结果需给条件，不把源示例当本次测量 |
| cloud instance | 云实例 | 计算实例；不等于本次已租用云资源 |
| image | 镜像（image） | Docker镜像，非图片；镜像tag原样 |
| base image | 基础镜像 | Dockerfile FROM的起点 |
| container | 容器（container） | 与镜像、进程、虚拟机分别说明 |
| host | 宿主机（host） | 容器所运行的机器环境；不同于AI技能宿主 |
| layer | 镜像层（layer） | 文件系统/构建层；不套用神经网络层 |
| registry | 镜像仓库服务（registry） | 存放分发镜像的服务；可简称镜像仓库，不同于MCP Registry |
| volume | 卷（volume） | Docker存储对象；与绑定挂载不同；源文混用处单列 |
| bind mount | 绑定挂载 | 宿主路径直接映射入容器；默认可写性不隐去 |
| mount | 挂载 | 数据访问映射；方向/源目的地/冒号/尾斜杠保持 |
| build / run | 构建 / 运行 | 生成镜像与启动容器是不同步骤 |
| tag | 标签（tag） | 镜像版本标识；不擅自改成digest固定或最新版本 |
| Docker Compose | Docker Compose | 多服务配置工具，不把YAML解析当部署通过 |
| emulation / native | 仿真 / 原生 | Apple Silicon运行x86_64镜像的语境 |
| runtime / devel | 运行时 / 开发环境 | 自然语言说明；CUDA镜像tag中的原词不译 |
| reproducibility | 可复现性 | 容器与依赖条件下重现；源码未完整锁定时不新增绝对保证 |
| inference / serving | 推理 / 推理服务 | 模型计算与服务化部署分别说明 |
| quantization | 量化 | 参数表示精度；不等于剪枝或所有内存均等比例减少 |

围栏payload（包括原文英文说明卡）、Mermaid/figure保持源字节，裸围栏只补text。价格、免费额度、速度/容量保证、平台支持与权限/网络风险记录到review，不静默更改原文，也不执行其操作。
