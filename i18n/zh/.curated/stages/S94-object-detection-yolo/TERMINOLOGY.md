# S94-object-detection-yolo 术语增量 v1.0

日期：2026-10-04 UTC。固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；规范题名：Object Detection — YOLO from Scratch。

这是完整固定92份词表校准后的本地check-only候选，尚未安装或发布，不构成中文审校或正式接受。原术语提案无需强制改词；以下词义只用于本课语境。正式基线107；87正式TERM=85 accepted stage+core2，active-reviewed5=S88/S89/S91/S92/S93，总92；8原controls另计，100common+本课own3=103。S95原样SVG另计。原支持日期、旧状态叙述与字节保留，不据此否定S90现已正式接受。

| English | Proposed Chinese | Boundary |
|---|---|---|
| object detection | 目标检测（object detection） | Predict labelled boxes, distinct from whole-image classification |
| bounding box / box | 边界框 / 框 | In prose, 检测框 for a detector prediction when needed; same geometry |
| dense prediction | 密集预测（dense prediction） | A prediction at each spatial location |
| anchor / anchor box | 锚框（anchor）/ 锚框 | A prior width-height shape; not S40 triplet-loss 锚样本 or S74 textual 锚定 |
| box prior | 框先验 | Predetermined shape, not a probability score |
| grid cell / grid stride | 网格单元 / 网格步幅 | Stride follows S83 步幅; pixels per spatial cell, not tensor memory stride |
| ground-truth box / ground truth | 真实框（ground-truth box）/ 真实值 | Annotated reference box, not model prediction; follows S40 semantic role |
| objectness / objectness score | 目标存在性（objectness）/ 目标存在性分数 | Per-cell/per-anchor signal; do not conflate with postprocess product score |
| box regression / regression head | 边界框回归 / 回归头 | Predict continuous geometry, distinguish from classification |
| detection head | 检测头 | Last prediction module, distinct from full detector or main backbone |
| Intersection-over-Union / IoU | 交并比（Intersection-over-Union，IoU） | Intersection area divided by union area; both prediction/GT matching and prediction/prediction NMS |
| non-maximum suppression / NMS | 非极大值抑制（non-maximum suppression，NMS） | Greedy suppression above threshold; no averaging/merging guarantee |
| FPN | 特征金字塔网络（FPN） | Multi-resolution feature levels |
| true positive | 真阳性（true positive） | Matching success according to source IoU threshold; not numerical positivity |
| precision / recall / accuracy | 精确率 / 召回率 / 准确率 | S28/S39/S88; first occurrence explains metric terms, preserve tokens precision@0.5 and mAP variants |
| average precision / AP | 平均精确率（AP） | S39 definition; do not silently repair source PR-area simplification |
| mean average precision / mAP | 平均精确率均值（mAP） | Average over classes, and over IoU thresholds in source COCO context; not Bayesian MAP |
| MSE / focal loss / quality focal loss | 均方误差（MSE）/ 焦点损失（focal loss）/ 质量焦点损失（quality focal loss） | S40 focal loss; keep CIoU/DIoU names, do not conflate losses with AP metrics |
| localisation / multi-scale inference | 定位 / 多尺度推理 | Geometry quality / combine predictions at distinct input resolutions |
| task-aligned matching / dynamic k | 任务对齐匹配 / dynamic k | Preserve source version claims separately without endorsing them |
| confidence threshold / coverage statistics | 置信度阈值 / 覆盖统计量 | Thresholded postprocess score versus shape prior coverage |

## 沿用和消歧

沿用：feature map→特征图；backbone→主干网络；receptive field→感受野；forward pass→前向传播；pipeline→管线；epoch→轮（epoch）；prompt→提示词（prompt）；logits→logits（未经归一化的分数）。anchor不套S40锚样本或S74锚定。平均精确率与跨类别的平均精确率均值区分，grid stride不套内存布局单位。

## 保护规则

核心及补充表优先，首次正文说明中英对应，API、模型ID、语言代码、公式、数值单位、路径、链接、代码与图载荷保持。九个通用章节沿补充表，英文无的章节不补造。自然语言数量变化必须等值逐块记录。源技术疑问单列，不能静默改写。

参考词表只用于术语一致性，未复用旧中文课程正文/segments/format_revisions。必要阅读docs/i18n.md已暴露其中既有中文质量示例；未引用或复用该示例措辞。支持、作者草稿及局部测试均不增加正式完成数。

publication pending/null只记录冻结时尚未绑定发布提交；冻结后不自指当前文件commit。实际发布须由后续record/外部远端回读绑定，不能删除历史或编造SHA。
