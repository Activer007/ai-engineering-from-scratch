# S83 从零实现卷积术语增量 v1.0

2026-10-03 UTC。完整阅读固定英文 04-02 及全部 code/quiz/outputs 后制定；仅继承 `DEPENDENCIES.json` 的 87 项固定支持，其中 79 个术语文件已全文核对。特别沿用 S05 点积/矩阵运算、S14 张量与内存布局、S21 卷积/感受野、S27/S29 权重偏置、S35 非线性、S38 残差连接、S69 PyTorch 和 S77 图像基础。词表不修正源事实；后续须独立审校。

| English | 中文或保留形式 | 语境与保护 |
|---|---|---|
| convolution / cross-correlation | 卷积（convolution）/ 互相关（cross-correlation） | 卷积沿 S21；按源关键术语明确实际计算为互相关，不翻转源卷积核或改代码 |
| convolutional neural network / CNN | 卷积神经网络（CNN） | 沿 S69/S77；CNN 保留，不把模型家族断言扩为本次实测 |
| dense / fully connected layer | 全连接层（dense / fully connected layer） | 网络连接方式语境，不套用向量存储的“稠密”解释 |
| kernel / filter | 卷积核（kernel）/ 滤波器（filter） | 卷积核沿 S77；此处两者指滑动权重张量，不是 SVM 核函数、OS 内核或特征选择过滤法 |
| CUDA kernel / conv kernel | CUDA 计算内核 / 卷积计算内核 | 执行实现语境沿 S14/S72，区别于可学习权重张量 |
| translation equivariance | 平移等变性（translation equivariance） | 输入平移对应输出平移，不误译成平移不变性；边界/步幅限制另记源问题 |
| parameter sharing / shared weights | 参数共享（parameter sharing）/ 共享权重 | 各空间位置复用同一权重；不改成独立复制参数 |
| locality / sliding window | 局部性 / 滑动窗口 | 局部空间邻域，不是网络请求本地性或上下文长度 |
| input / output channel | 输入通道 / 输出通道 | 沿 S77 通道；C_in/C_out 与空间轴/批次轴不能交换 |
| feature map / feature extractor / feature detector | 特征图 / 特征提取器 / 特征检测器 | 空间激活网格、提取模块与检测模式按源角色区分，不等同特征选择 |
| stride / strided convolution | 步幅（stride）/ 带步幅的卷积 | 这里是卷积核滑动间隔；区别 S14 内存布局的步幅，不引入字节单位 |
| padding / zero padding | 填充（padding）/ 零填充 | 沿 S77 填充；不是 token 填充；源 P、边界模式与取整公式不改 |
| same / valid convolution | same 卷积 / valid 卷积 | 首次按源说明“保持尺寸”/“不填充”；same、valid 作为模式名称保留 |
| reflect / replicate / circular | 反射 / 复制边缘 / 循环填充 | 代码标识符 `reflect`、`replicate`、`circular` 原样；不互换各自边界行为 |
| downsample / pooling / max-pool | 降采样 / 池化 / 最大池化 | 降采样沿 S30；卷积步幅和独立池化层的实现不同 |
| receptive field / RF | 感受野（receptive field）/ RF | 沿 S21；原始输入中影响某激活值的区域，不是当前特征图尺寸 |
| im2col / col2im | im2col / col2im | 算法标识保留；首次解释 im2col 将局部窗口展开为列，col2im 为反向聚合相关操作，不能翻译函数名 |
| vectorised / vectorization | 向量化 / 向量化（vectorization） | 沿 S72；将运算交由数组/矩阵操作，不等于自动零拷贝或已验证加速 |
| matmul / GEMM | 矩阵乘法（matmul）/ GEMM（通用矩阵乘法） | 沿 S05 矩阵乘法；不改乘数方向或声称所有实现均采用相同算法 |
| flatten / reshape / patch | 展平 / 重塑形状 / 局部图像块 | reshape 沿 S14；局部图像块不译成软件补丁，代码 API 原样 |
| dot product / element-wise product | 点积 / 逐元素乘积 | 沿 S05；sum、乘法、矩阵乘法和转置对象分开 |
| weights / bias / parameter count | 权重 / 偏置 / 参数数量 | 沿 S27/S29；bias 不是统计偏差；是否计偏置按源公式保持 |
| activation / non-linearity | 激活值 / 非线性 | 沿 S27/S35；输出值与激活函数按语境区分，不暗补源未写出的层 |
| residual connection | 残差连接 | 沿 S38；相加所需形状匹配按源说明 |
| depthwise convolution / groups | 逐通道卷积（depthwise convolution）/ groups | groups 参数名保留；不误译为普通增加网络深度，不增改源参数计数 |
| pointwise convolution | 逐点卷积（pointwise convolution） | outputs 的通道混合语境；仅术语说明，保护提示词原文 |
| Sobel / edge / blur / sharpen | Sobel / 边缘 / 模糊 / 锐化 | Sobel 保留专名；sobel_x/sobel_y 和卷积核数字不改，轴和响应正负不能交换 |
| synthetic step image / sanity check | 合成阶跃图像 / 基本合理性检查 | 固定合成输入与简要检查，不夸大为完整正确性证明 |
| backward pass / autograd | 反向传播 / autograd（自动求导） | 沿 S08/S32/S69；计算梯度不是参数更新，API 原样 |
| floating-point accumulation order | 浮点累加顺序 | 沿 S15 数值稳定性；误差解释不等于任意输入均满足同一误差上界 |

通用章节沿固定补充表：学习目标、要解决的问题、核心概念、动手实现、实际使用、交付成果、练习、关键术语、延伸阅读。Step 1–6 标号保留。元数据键、Build、Python 保留；`~75 minutes` → `~75 分钟`。自然语言 one/two/three/four/five 等按原义等值译为一/两/三/四/五并在逐块记录登记；源阿拉伯数字与单位不换算。`150 million` 保留源数值和量级并可释为一亿五千万，`1e-5` 和所有形状/公式保持。

NumPy、numpy、PyTorch、torch、CUDA、cuDNN、JPEG、Photoshop、ImageNet、ResNet、ConvNeXt、MobileNet、VGG、AlexNet、Sobel、Winograd、FFT、GEMM、RGB、CPU/GPU、float32、nn.Conv2d、Conv2d、nn.Sequential、torch.autograd.grad 及所有 API/参数/路径原样。Gaussian blur 可呈现为 Gaussian 模糊（高斯模糊）；引用题名和人名保持可检索英文，介绍文字译中文。保留英文不免除首次正文的必要中文解释。

公式、代码、ASCII 说明、Mermaid/figure、提示词和 outputs 全部保护。原裸围栏仅增加 text；强调边界保留源空格，必要可逆 GFM 调整单独记录。源的 Sobel 预期、dtype/参数验证、形状取整、感受野数字与性能/普遍性断言如有问题，独立登记，不借术语静默修正。
