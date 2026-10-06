# S156-multi-object-tracking terminology candidate

Fixed English `1bafaa88bb4668356791150bec3a6d7df38387eb`, lesson04-27. Short lexical proposals only, not Chinese lesson prose or future-author calibration. Common158 SHA-256 `a4ed394c03650b70a6e48172186d37c5bc255dc887753c058be7a73bc5a78875` is finalized locally from independently accepted support/content/repair/final-TASKS/formal166 chains. Own3 publication/readback/installation and independent review remain pending.

Core and ADDENDUM first-body-use rules apply: explain relevant English/acronyms with Chinese context, retaining protected product/API/identifier names. token first use follows token（词元）. Common headings follow ADDENDUM only where present; metadata keys and language/type values stay unchanged. Natural-language time/count units may be translated equivalently, with exact numeric quantities preserved. No lexical choice silently repairs source facts.

| English | Proposed Chinese presentation | Context and boundary |
|---|---|---|
| multi-object tracking | 多目标跟踪 | MOT retains acronym; target identity over video frames. |
| tracking-by-detection | 基于检测的跟踪 | Detection followed by association; not all trackers. |
| association | 关联 | Cross-frame matching, distinct from language association. |
| track / track ID | 轨迹 / 轨迹 ID | Persistent tracker hypothesis; not one detected box. |
| trajectory | 运动轨迹 | Position sequence; retain track context. |
| Kalman filter | 卡尔曼滤波器 | Linear state/covariance estimator; not neural filter. |
| covariance | 协方差 | State uncertainty matrix. |
| constant-velocity model | 匀速模型 | Motion assumption only. |
| Hungarian algorithm | 匈牙利算法 | Keep source naming; implementation caveat separate. |
| cost matrix | 代价矩阵 | Tracks×detections assignment costs. |
| one-to-one assignment | 一对一指派 | At most one match per side. |
| occlusion | 遮挡 | Object visibility interruption. |
| ReID / re-identification | 重识别（ReID） | Appearance-based identity cue. |
| appearance feature | 外观特征 | Distinct from box geometry. |
| camera motion compensation | 相机运动补偿 | Global camera motion correction. |
| ID switch | ID 切换 | Predicted identity change; not global IDF1. |
| memory bank | 记忆库 | S148 video-feature memory. |
| shared memory | 共享记忆 | S148 model feature memory, not OS IPC. |
| per-instance query tokens | 每个实例各自的查询 token | S148 queries/core token first-use 词元. |
| bounding box / IoU | 边界框 / 交并比（IoU） | S94/S100 visual geometry. |
| ground truth | 真实值 | S94; ground-truth tracks are annotated reference trajectories. |
| false negative / false positive | 漏检 / 误检 | Detection metric context; retain FN/FP. |
| MOTA | 多目标跟踪准确率（MOTA） | Preserve formula; not general classification accuracy. |
| IDF1 | 身份 F1 分数（IDF1） | Identity precision/recall, not switch count alone. |
| HOTA | 高阶跟踪准确率（HOTA） | Detection/association/localization metric. |
| detection accuracy / association accuracy | 检测准确率 / 关联准确率 | Retain DetA/AssA, not numerical precision. |
| lifecycle / birth / death | 生命周期 / 新建 / 终止 | Track lifecycle, no biological metaphor needed. |
| ByteTrack / BoT-SORT / SORT / DeepSORT / StrongSORT / OC-SORT / SAM 2 / SAM 3.1 / Object Multiplex | Preserve source names | No renamed models or silent version changes. |

## Calibration coverage

All158 common payload identities verified; only the following lexical files/ranges were semantically read for this lane. Older frozen headers describe historical lifecycle states and cannot override accepted identity chains.

- i18n/zh/.curated/TERMINOLOGY-ADDENDUM.md: {"mode": "excerpt", "line_ranges": [[1, 42]]}.
- i18n/zh/.curated/TERMINOLOGY.md: {"mode": "full", "line_ranges": [[1, 82]]}.
- i18n/zh/.curated/stages/S94-object-detection-yolo/TERMINOLOGY.md: {"mode": "full", "line_ranges": [[1, 41]]}.
- i18n/zh/.curated/stages/S100-instance-segmentation-mask-rcnn/TERMINOLOGY.md: {"mode": "full", "line_ranges": [[1, 49]]}.
- i18n/zh/.curated/stages/S148-sam3-open-vocab-segmentation/TERMINOLOGY.md: {"mode": "full", "line_ranges": [[1, 54]]}.
- i18n/zh/.curated/stages/S151-vision-language-models/TERMINOLOGY.md: {"mode": "full", "line_ranges": [[1, 74]]}.

No older Chinese lesson body/record/review was supplied to this fresh tree. The future author must independently propose/calibrate terms before first body writing. SCOPE.md records complete source caveats. Mandatory future read-only CJK-bold risk scan and manual raw angle-tag Markdown review supplement original strict and actual GFM; they do not permit rewriting code or adding checker exceptions.
