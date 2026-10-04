# S115-3d-vision-nerf 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；规范题名：3D Vision — Point Clouds & NeRFs。

本地check-only own3候选，未安装、未发布、不增加正式课程数。复用既有107 TERM校准与当前独立技术/中文审校；common115=107 TERM+8 controls，own3另计，未来总118。无单独Markdown提案；表格忠实整理既有107表校准中的contextual_decisions，未补造作者提案或新的校准时间。

| English | 本课译法及界定 | 来源类别 |
|---|---|---|
| MLP | 多层感知机（MLP），S08/S69/S72 | 既有术语沿用 |
| CNN | 卷积神经网络（CNN），S69/S77/S85 | 既有术语沿用 |
| tensor | 张量，S14/S69 | 既有术语沿用 |
| pooling / max pool | 池化 / 最大池化，S83/S85 | 既有术语沿用 |
| forward / backward pass | 前向传播 / 反向传播，S08/S32/S69 | 既有术语沿用 |
| positional encoding | 位置编码，S21 | 既有术语沿用 |
| Fourier features | Fourier 特征（傅里叶特征），沿 S21 专名策略 | 既有术语沿用 |
| pipeline | 管线，S57/S72/S77 | 既有术语沿用 |
| anti-aliasing | 抗混叠，S21/S30 | 既有术语沿用 |
| epoch | 轮（epoch），S43/S69/S85 | 既有术语沿用 |
| prompt / skill | 提示词（prompt）/ 技能，core/S88/S100 | 既有术语沿用 |
| ground truth | 真实值，S40/S94 | 既有术语沿用 |
| normalization / centring | 归一化 / 中心化，数值缩放语境，区别文本规范化 | 既有术语沿用 |
| point cloud | 点云（point cloud） | 本课术语 |
| mesh / voxel | 网格 / 体素 | 本课术语 |
| signed distance field / SDF | 有符号距离场 / SDF | 本课术语 |
| neural radiance field / NeRF | 神经辐射场 / NeRF | 本课术语 |
| permutation invariance | 置换不变性 | 本课术语 |
| symmetric function | 对称函数 | 本课术语 |
| ray casting | 光线投射 | 本课术语 |
| volumetric rendering | 体渲染 | 本课术语 |
| volumetric field | 体积场 | 本课术语 |
| 3D Gaussian splatting | 保留方法名称，首次说明高斯泼溅；3D Gaussians 为 3D 高斯体 | 本课术语 |
| structure-from-motion | 运动恢复结构 | 本课术语 |
| posed images | 带有相机位姿信息的图像 | 本课术语 |
| transmittance / opacity | 透射率 / 不透明度 | 本课术语 |
| hash-grid encoding | 哈希网格编码 | 本课术语 |
| novel view / view synthesis | 新视角 / 视角合成 | 本课术语 |
| registration | 配准 | 本课术语 |
| normal | 法线，不是正态分布 | 当前语境消歧 |
| surface | 几何表面，不是工作台组成要素 | 当前语境消歧 |
| head | 网络输出头，不是依存分析的中心词 | 当前语境消歧 |
| view | 渲染视角，不是张量共享内存视图 | 当前语境消歧 |
| trace | 跟踪计算，不是矩阵的迹 | 当前语境消歧 |
| density | 体密度，不是概率密度的点概率 | 当前语境消歧 |
| dense | 稠密张量，不是 dense 层的全连接 | 当前语境消歧 |
| bias | 频谱/低频偏向，不是加性偏置或泛化误差分解 | 当前语境消歧 |
| direction | 光线/视线方向，不是指标比较方向 | 当前语境消歧 |

## 沿用和保护

核心及补充表优先，只按本课语境使用术语；保留代码、专名、API、模型ID、路径、URL、公式、数字和图载荷。英文没有的内容不补造，源矛盾或宽泛主张在SCOPE单列，不静默改写技术含义。通用标题沿既有九项约定，不据此补造源文缺失章节。

固定英文与术语足以起稿，先修中文正式验收不是门禁。语言审校、真实GFM、运行、远端回读和批次回归分别记录；本候选不把翻译PASS当作运行或安全验证。
