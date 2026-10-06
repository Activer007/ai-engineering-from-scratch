# S139-keypoint-pose terminology support

Fixed English 1bafaa88bb4668356791150bec3a6d7df38387eb. Preauthor support candidate only. Common145 =137 terminology files +8 controls; own3 publication/readback/installation is pending. Exact complete common pins and source/prerequisite identities are in DEPENDENCIES.json. All author proposal/calibration, first-write, capture, record, strict and independent language-review evidence remains pending/null.

## Source-grounded term preparation

These short glossary entries refine the source-only proposal using the exact existing core and relevant stage terminology. They are not Chinese lesson prose. Existing terminology is not overwritten. The complete 137-file terminology set is pinned for consistency; this preparation does not claim a fresh full reread of all historical terminology. Targeted calibration read core TERMINOLOGY.md, ADDENDUM heading/first-use and relevant backbone/postprocess rules, S09/S40/S83/S85/S88/S94/S100, and the separately published S97 reference.

| English | Proposed Chinese | Semantic boundary / prior terminology |
|---|---|---|
| keypoint / keypoint detection | 关键点 / 关键点检测 | Ordered landmark identity; not an arbitrary salient pixel. |
| pose / pose estimation | 姿态 / 姿态估计 | This lesson's ordered keypoint set for one instance; do not expand it to every rigid-body 6D-pose representation. |
| landmark / joint / limb | 标志点 / 关节 / 肢段 | Landmark need not be an anatomical joint; limb/connection denotes an edge between keypoints. |
| top-down / bottom-up | 自顶向下 / 自底向上 | Person detect/crop then estimate versus all-keypoint prediction then instance association; not image-axis direction. |
| heatmap / heatmap regression | 热图 / 热图回归 | One H x W output per keypoint; raw heatmap values are not automatically calibrated probabilities. |
| Gaussian heatmap target | 高斯热图目标 | The source uses an unnormalized Gaussian-shaped target; do not call it a normalized probability density.; basis: S09-probability-foundations |
| argmax | argmax（最大值对应的索引） | Keep source lower-case spelling; do not confuse index with maximum value or soft-argmax.; basis: S88-image-classification |
| sub-pixel localisation / refinement | 亚像素定位 / 亚像素细化 | Coordinate refinement, not image super-resolution; raw, sign and quadratic methods remain distinct. |
| first-difference offset / quadratic fit | 一阶差分偏移量 / 二次拟合 | Do not insert sign or replace the protected source formula. |
| Part Affinity Field / PAF | 部件亲和场（Part Affinity Field，PAF） | Two-channel directed unit-vector field for a connection; distinguish a vector field from a scalar heatmap. |
| association / grouping / instance | 关联 / 分组 / 实例 | Assignment to a person/object instance; not class grouping or tracking identity across time.; basis: S100-instance-segmentation-mask-rcnn |
| line integral / unit vector | 线积分 / 单位向量 | PAF score along candidate connection; preserve summation approximation and direction. |
| Percentage of Correct Keypoints / PCK | 关键点正确率（PCK） | Keep metric name and abbreviation; no threshold/normalization formula is supplied by this source. |
| Object Keypoint Similarity / OKS | 目标关键点相似度（OKS） | Distinct from box IoU, although used analogously for matching; do not invent absent scale/visibility terms. |
| bounding box / IoU / mAP | 边界框 / 交并比 / 平均精确率均值 | Preserve AP versus mAP and mAP@OKS literals; no Bayesian MAP or pixel accuracy.; basis: S94-object-detection-yolo |
| feature map / backbone / stride | 特征图 / 主干网络 / 步幅 | Spatial features and sampling step, not tensor memory-stride units.; basis: S83-convolutions-from-scratch, S85-cnns-lenet-to-resnet |
| upsampling / transposed convolution | 上采样 / 转置卷积 | S97 is supplementary published terminology reference; no claim of Chinese lesson acceptance.; basis: S97-semantic-segmentation-unet, S100-instance-segmentation-mask-rcnn |
| mean squared error / ground truth | 均方误差（MSE）/ 真实值 | Loss versus evaluation; reference landmarks versus predictions.; basis: S40-loss-functions |
| image / camera / world coordinates | 图像坐标 / 相机坐标 / 世界坐标 | Distinct frames; single-view lifting does not by itself establish metric absolute depth. |
| 2D-to-3D lifting | 二维到三维提升 | Preserve 2D/3D tokens and source pipeline; not spatial upsampling. |
| latency / throughput / pipeline | 延迟 / 吞吐量 / 管线 | Per-frame cost, unit-time processed volume and processing stages remain distinct.; basis: core, S88-image-classification |

## First use, inheritance and protection

- Follow the core first-use rule: explain translatable technical terms with Chinese and the source English/acronym at their first body occurrence; later use the agreed term. Headings may be concise. Preserve source capitalization rather than changing argmax into a different operation.
- Inherit feature map as 特征图, backbone as 主干网络, stride as 步幅, downsampling as 降采样, forward pass as 前向传播, skip connection as 跳跃连接, ground truth as 真实值, and MSE as 均方误差（MSE）. The keypoint model's source wording U-Net-style does not add absent skip connections.
- Inherit S94/S100's 边界框, 交并比, 平均精确率 and 平均精确率均值. Classification precision is 精确率; coordinate/sub-pixel precision is 定位精度 or 亚像素精度. Do not interchange these meanings or change mAP@OKS literals. Source PCK/OKS definitions are not expanded with absent formulas.
- Inherit S97/S100's 上采样 and 转置卷积. S97 is the published reference pin at bfc72c4478e6f5281dd698097cbc5f1a90937179, SHA256 5eda3951e1e0f874862691337a9f8575be0d4e509d8bf0537a14d0a9ca6b8b57. Its Chinese lesson acceptance is not asserted.
- Keep keypoint identity/order, (x, y) output versus [y, x] indexing, and N/K/H/W axis meanings distinct. A landmark can be an object feature rather than an anatomical joint. Association connects keypoints to an instance without implying temporal tracking.
- Keep unnormalized Gaussian-shaped targets, calibrated probabilities and raw heatmap peak scores distinct. Preserve raw first-difference, sign-based quarter-pixel and quadratic-fit methods as different source surfaces; terminology must not repair the source algorithm.
- Keep image, camera and world coordinate frames distinct. Preserve 2D/3D source tokens even when explaining 二维/三维. Heatmap-grid output is not automatically mapped through crop/stride transforms to the original image, and single-view relative lifting does not prove absolute depth.
- Nine common headings follow the frozen ADDENDUM: 学习目标、要解决的问题、核心概念、动手实现、实际使用、交付成果、练习、关键术语、延伸阅读. Do not add missing source sections. Preserve Step labels/numbers and metadata keys Type/Languages/Prerequisites/Time; Build and Python remain unchanged. Natural-language prerequisite labels and minutes may be translated faithfully.
- Preserve numbers, units, shape tuples, mathematical expressions, identifiers, URLs, paths, fenced code, Mermaid and figure payloads. Any equivalent natural-language quantity translation or minimal GFM formatting adjustment must be recorded at the actual authoring stage. Citation titles/authors remain searchable; unverified product/version claims stay source claims.

Protected names include COCO, HRNet, ViTPose, OpenPose, HigherHRNet, MediaPipe Pose, MMPose, YOLOv8-pose, HumanDPT, PoseAnything, VideoPose3D, PyMAF, MHFormer, MotionBERT, SMPL, SMPL-X, DARK, EPnP, PoseCNN, DeepIM, PyTorch and NumPy; preserve every other source identifier too. No model availability, benchmark ranking or runtime claim is independently validated here.

Future author input and review chronology remains null; actual publication is recorded outside this prepublication snapshot. Common support and reference vocabulary do not establish course completion, source correctness or permission to begin a Chinese body before own3 readback and installation.
