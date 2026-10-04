# S121-real-time-edge 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 1bafaa88bb4668356791150bec3a6d7df38387eb；规范题名：Real-Time Vision — Edge Deployment。

本地支持候选，未安装或发布，不增加正式课程数。冻结 common127=119 TERM+8 controls；own3另计，未来总130。完整沿用原HANDOFF术语取舍10条；首稿与R01分别绑定，旧独审REQUEST_CHANGES不改成新稿PASS。

- edge / on-device inference：边缘端 / 设备端推理，沿 S86；不是图像边缘。latency / throughput：延迟 / 吞吐量，沿核心
- backbone：主干网络，沿 ADDENDUM、S85、S91；不用骨干网络
- logits：保留 logits，首现解释未经归一化的分数，沿 ADDENDUM/S88；不译为概率
- eager：即时执行，沿 S69/S72；kernel dispatch/execution：计算内核调度/执行，沿 S14/S72/S83，区别卷积权重核
- depthwise convolution：逐通道卷积，沿 S83；PTQ、QAT、FP32、INT8、ONNX、TensorRT、Core ML、TFLite、模型 ID、路径、API、图内文原样
- warmup：运行时预热，不套学习率预热；percentile：百分位数，沿 S17；accuracy：准确率，区别数值精度和分类精确率
- PTQ：训练后量化；QAT：量化感知训练；calibration set：校准集，指测激活范围，不等同准确率评估/概率校准
- pruning / distillation：剪枝 / 蒸馏；量化、结构化剪枝和教师学生蒸馏不互相混用
- `90-accuracy` 无源单位，只译“准确率为90”，绝不补 `%`；`< 1%` 与 `0.1-1 percentage points` 分别保留为百分比和百分点
- 自然语言 millijoules 保留英文单位并解释毫焦耳；其余数字、单位、负号、链路、表格预算和文件 suffix 未改

## 沿用和保护

核心与补充表优先，固定英文和相关术语足以起稿，先修中文正式验收不是额外门槛。保留代码、API、路径、URL、数字、数学与图载荷。源风险见SCOPE，语言PASS不等于运行、呈现、回归或发布通过。
