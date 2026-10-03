# S77 图像基础术语增量 v1.0

2026-10-03。联用核心、补充表及83项固定支持，尤其S14张量操作、S69 PyTorch、S30音频采样术语。唯一课文来源为固定英文04-01。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| image / pixel / channel | 图像 / 像素（pixel）/ 通道（channel） | 像素为光强采样值；通道为并列空间网格 |
| tensor / shape / dtype | 张量（tensor）/ 形状（shape）/ 数据类型（dtype） | 沿S14/S69，API与元组保持原样 |
| pipeline / preprocessing | 管线（pipeline）/ 预处理 | 视觉处理管线，不混同流水线并行 |
| spatial sampling / intensity quantization | 空间采样 / 强度量化 | 网格密度与强度离散精度分开 |
| aliasing / resampling | 混叠 / 重采样 | 沿S30，像素网格与音频网格按语境区分 |
| demosaicing | 去马赛克（demosaicing） | 从彩色滤镜阵列重建各位置RGB，不指遮挡打码 |
| HWC / CHW / NCHW | HWC / CHW / NCHW | 首现解释高度、宽度、通道；N为批次，轴顺序原样 |
| channels-first / channels-last | 通道优先 / 通道后置 | 沿S14；逻辑轴顺序不暗等同物理连续布局 |
| normalize / standardize | 归一化 / 标准化 | 本课分别指除以255及按通道减均值除标准差，不互换 |
| RGB / BGR / HSV / YCbCr | RGB / BGR / HSV / YCbCr | 专名保留；RGB红绿蓝、HSV色相饱和度明度；色彩空间首现解释 |
| grayscale / luminance / chroma | 灰度 / 亮度 / 色度 | BT.601系数及源约定不改，物理亮度与编码亮度差异另列源风险 |
| aspect ratio / center crop / pad | 宽高比 / 中心裁剪 / 填充 | 缩放后裁剪、保宽高比填充、直接拉伸分开 |
| interpolation / endpoint-aligned | 插值 / 端点对齐 | NumPy与框架align_corners=False坐标不静默统一 |
| nearest neighbor / bilinear / bicubic | 最近邻 / 双线性 / 双三次 | 插值方法；Catmull-Rom、Lanczos原名保留 |
| convolution kernel / contiguous plane | 卷积核 / 连续平面 | 不与操作系统内核混淆；转置后连续性源简化另列 |
| roughness / round trip | 粗糙度 / 往返变换 | 指代码给出的局部差分指标及预处理逆过程 |
| CNN / OCR / HDR | 卷积神经网络（CNN）/ 光学字符识别（OCR）/ 高动态范围（HDR） | 首现可括注，缩写不改 |

通用章节使用补充表的九种译法。自然语言minutes→分钟；one/two/three/four/ten等量词等值译汉字，所有阿拉伯数字、范围、公式、路径、URL、代码标识符及保护围栏逐字保留。源文经验比例和普遍性断言不表示已核实；源技术问题另列。
