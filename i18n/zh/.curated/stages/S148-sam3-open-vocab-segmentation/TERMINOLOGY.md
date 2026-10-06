# S148 SAM 3 and open-vocabulary segmentation terminology support candidate

Fixed English: 1bafaa88bb4668356791150bec3a6d7df38387eb, lesson 04-24. Short lexical support only, not Chinese lesson prose. Common152 = 144 TERM + 8 unchanged controls; own3 adds three, prospective total 155. The coordinator owns DEPENDENCIES.json. Publication, independent readback, installation, future author calibration and first write remain pending.

## Calibrated lexical choices

| English | Proposed Chinese presentation | Inheritance and semantic boundary |
|---|---|---|
| open-vocabulary / closed-vocabulary | 开放词表 / 封闭词表 | S130; S122 matched row agrees. Candidate visual concept classes, not tokenizer vocabulary size. |
| open-vocabulary segmentation | 开放词表分割（open-vocabulary segmentation） | S130 open-vocabulary + S97/S100 segmentation. Broader task label; do not silently turn all uses into semantic-only segmentation. |
| semantic / instance / panoptic segmentation | 语义分割 / 实例分割 / 全景分割 | S97/S100. Per-class pixels, distinct object instances, and joint coverage remain different. |
| mask / segmentation mask / binary mask | 掩码 / 分割掩码 / 二值掩码 | S100/S124; a spatial object-region representation, not an attention mask or image-patch masking operation. |
| Promptable Concept Segmentation / PCS | 可提示概念分割（Promptable Concept Segmentation，PCS） | New task-specific compound. A concept prompt selects matching instances; not arbitrary instruction reasoning or guaranteed perfect recall. |
| concept / concept prompt | 概念 / 概念提示词（concept prompt） | Core prompt with new visual-concept scope. Preserve actual quoted/inline model inputs. |
| noun phrase / image exemplar | 名词短语 / 图像示例（image exemplar） | New scoped lexical choices. Exemplar is a visual concept example, not a whole training corpus or an automatically identical output. |
| visual prompt / text prompt / text-prompted | 视觉提示 / 文本提示词 / 由文本提示词驱动的 | Core/S130. Points/boxes and textual concepts have distinct roles; use natural syntax without renaming API arguments. |
| text-image grounding | 文本—图像对应定位（text-image grounding） | New visual-context mapping. Relating a text description to image objects/regions; not S144 external-evidence grounding or an electrical ground. |
| object / instance / instance ID | 目标 / 实例 / 实例 ID | S94/S100/S139. Spatial instance identity is not automatically a persistent cross-frame or globally unique merged-query ID. |
| detector / detection head / mask decoder | 检测器 / 检测头 / 掩码解码器 | S94/S100. Whole component, prediction module, and mask-producing decoder stay distinct. |
| presence head | 存在性预测头（presence head） | New term. Whether the queried concept is present, distinct from region localisation and S94 generic anchor objectness. |
| localisation / false positive / absent concept | 定位 / 误报 / 未出现的概念 | S94 localisation; S144 false positive contextualized to an unwanted visual match. Do not confuse with missed objects. |
| shared backbone / ViT | 共享主干网络 / 视觉 Transformer（ViT） | ADDENDUM/S118/S139. Preserve ViT and architecture names; shared does not mean all detector/tracker heads share weights. |
| frozen model / frozen weights | 冻结的模型 / 冻结的权重 | ADDENDUM/S100/S143. Parameters held fixed in context, not absence of video memory state. |
| memory-based tracker / memory bank | 基于记忆的跟踪器 / 记忆库 | New video-tracking scope. Stored per-instance/frame features, not computer RAM or a language-agent autobiographical memory. |
| decoupled detector-tracker / decouple | 解耦的检测器—跟踪器 / 解耦 | New compound; image detection and temporal tracking roles remain separate. Not two unrelated model families. |
| Object Multiplex / shared memory / per-instance queries | Object Multiplex / 共享记忆 / 每个实例各自的查询 | Keep update name. Model tracking memory, not OS shared-memory IPC; do not silently replace source simplification with bucket details. |
| cascade / error accumulation | 级联 / 误差累积 | Serial detector-to-segmenter stages; not a proof every downstream error strictly increases. |
| pipeline / backend / interface / data contract | 管线 / 后端 / 接口 / 数据契约 | S124. A common adapter can normalize outputs; terminology does not make incompatible native fields identical. |
| bounding box / label / score / threshold | 边界框 / 标签 / 分数 / 阈值 | S94/S100. Score is not necessarily calibrated probability; keep xyxy and class/concept identifiers exact. |
| post-processing / preprocessing / NMS | 后处理 / 预处理 / 非极大值抑制（NMS） | ADDENDUM/S124/S94. Distinct stages; do not claim NMS is implemented by the stub. |
| run-length encoding / RLE | 游程编码（run-length encoding，RLE） | S124. Local value-count encoding; no implied compatibility with standard COCO RLE or fixed payload-size guarantee. |
| deterministic stub | 确定性桩实现（deterministic stub） | New implementation-context mapping; fixed synthetic detections, not a loaded or validated SAM model. |
| forward pass / batch / inference | 前向传播 / 批处理 / 推理 | S94/S139/S121. One concept/image path versus multi-query batching and temporal tracking stay separate. |
| sparse point prompting / shallow mask aggregation | 稀疏点提示 / 浅层掩码聚合 | New SAM-MI terms. Sparse means fewer selected points; shallow denotes aggregation level, not a weaker quality guarantee. |
| decoupled mask injection / SAM-MI | 解耦掩码注入 / SAM-MI | Keep method name; distinguish from security prompt injection. Source method description caveat stays separate. |
| compositional concept / concept complexity | 组合式概念 / 概念复杂度 | Modifiers/relations compose the queried concept; not only concept count or long sentence length. |
| latency / throughput / real-time / edge | 延迟 / 吞吐量 / 实时 / 边缘端 | Core/S121. Edge is deployment location, not an image boundary; real-time depends on measured workload/hardware. |
| precision / FP16 / INT8 / p95 | 精度 / FP16 / INT8 / p95 | Numerical precision, not classification precision. p95 retains percentile meaning per S121; identifiers unchanged. |
| benchmark / human performance / ablation | 基准测试 / 人类表现 / 消融实验 | S143/S144. Reported benchmark-relative results, not local measurements or a universal human-accuracy percentage. |
| fine-tuning / zero-shot / IoU | 微调 / 零样本 / 交并比（IoU） | Core/S130/S94. Zero-shot is not untrained; mask overlap differs from box overlap. |
| gated checkpoint / access request / license | 受访问限制的模型检查点 / 访问申请 / 许可 | S130 checkpoint and S145 license context. Access approval and legal permission are separate; no legal clearance supplied. |
| SAM / SAM 2 / SAM 3 / SAM 3.1 / Grounded SAM 2 / SAM3-I | Preserve source model names | SAM 2 itself is distinct from a Grounded SAM 2 detector cascade; SAM3-I is distinct from SAM-MI. Preserve every source variant's spelling. |

## Calibration and preservation

All 144 common152 terminology payloads were checked against commit/path, SHA-256, Git blob and byte count. Full semantic reading covered core TERMINOLOGY.md, S94/S97/S100/S118/S121/S124/S130/S139 and newly appended S143/S144/S145. ADDENDUM lines 1-42 covered first-use/common headings and relevant backbone/postprocessing/VLM rules; the S122 open/closed-vocabulary row was read at line 13. Other pinned glossaries were searched for named relevant terms, not fully reread. Common149 identity/order is unchanged. Historical lifecycle labels in immutable supports are not current status evidence. S97 terminology is usable without asserting acceptance of its blocked Chinese lesson.

Use the core first-body-occurrence Chinese plus English/acronym rule. Later appearances may use the calibrated Chinese. Preserve source names and acronyms including Meta, Hugging Face, transformers, Ultralytics, Grounding DINO, DINO-X, Florence-2, YOLO-World, SAM-MI, SAM3-I, SA-CO, PCS, CLIP, ViT, CVAT, PyTorch, NumPy, API, GPU, HF, RLE and IoU. Do not introduce an absent acronym expansion or rename a protected model ID.

Keep Type/Languages/Prerequisites/Time keys and Use + Build/Python values. Natural-language prerequisite descriptions and minutes may be translated. Common headings remain 学习目标、要解决的问题、核心概念、动手实现、实际使用、交付成果、练习、关键术语、延伸阅读; preserve source ordering and Step numbers, and add no absent sections.

Protect all seven fenced payloads, Mermaid, cv3-open-vocab marker, inline code, identifiers, shape/coordinate notation, numbers, dates, percentages, multiplication signs, paths and URL targets. No bare body fence needs a tag. Natural-language quantities follow the core/addendum exact-equivalence rules; preserve 4 million, 270K, 50x, 75-80%, 96%, ~1.6× and source-specific comparisons without rounding or turning them into local results.

Source API mistakes, helper differences, repeated instance IDs, custom RLE limits, missing tests, quiz shape, licensing claims, benchmark scope and diagram behavior remain caveats in SCOPE.md/source-readiness.json. No term choice repairs the English or code. No Chinese lesson body, author proposal/calibration receipt, record or review is created here. Own3 and all subsequent author/review/page/regression/publication gates remain pending.
