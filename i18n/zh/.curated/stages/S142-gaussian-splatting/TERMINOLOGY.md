# S142 Gaussian Splatting terminology candidate

Preauthor support candidate only. Source planning read seven relevant pinned references; subsequent independent calibration verified and searched all 138 terminology files in candidate common146 and identified S07/S13/S16/S17 inheritance refinements below. These short lexical mappings are support, not Chinese lesson prose. Formal154 binding, own3 publication, independent exact-byte readback and installation remain pending. This is not the future author’s own proposal or calibration receipt.

| English | Proposed Chinese presentation | Status / basis | Context boundary |
|---|---|---|---|
| 3D Gaussian Splatting / 3DGS | 保留方法名称，首次说明高斯泼溅；3DGS 原样 | inherited; S115 | Method name; do not switch to an uncalibrated translation such as 高斯溅射. |
| 3D Gaussian / Gaussian blob | 3D 高斯体 / 高斯体 | inherited_context; S115 | A geometric primitive, not a normalized probability distribution or pixel. |
| point cloud / neural radiance field / NeRF | 点云 / 神经辐射场 / NeRF | inherited; S115 | Explicit point set versus learned radiance field. |
| volumetric rendering / transmittance / opacity | 体渲染 / 透射率 / 不透明度 | inherited; S115 | Opacity is not transparency; cumulative transmittance differs from one alpha. |
| structure-from-motion / SfM | 运动恢复结构（SfM） | inherited_context; S115 | Keep SfM; camera pose is position plus orientation, not body-pose keypoints. |
| novel view / view-dependent colour | 新视角 / 随视角变化的颜色 | inherited_context; S115 | Rendering viewpoint, not a shared-memory tensor view; the colour phrase is contextual proposal. |
| tensor / shape / broadcasting / einsum | 张量 / 形状 / 广播 / einsum（爱因斯坦求和） | inherited; S14 | Preserve all (G,H,W,...) tuples and index strings. |
| mean squared error / ground truth | 均方误差（MSE）/ 真实值 | inherited; S40 | Do not turn training MSE into proved reconstruction quality. |
| Gaussian / variance / standard deviation | 高斯 / 方差 / 标准差 | inherited_context; S09 | Probability distribution terms only where appropriate; unnormalized Gaussian kernel is not automatically a PDF. |
| logits / sigmoid / Adam | logits / sigmoid / Adam | inherited; core,S09,S40 | Activation and optimizer names stay unchanged; logits are not output probabilities. |
| diffusion model / Gaussian noise | 扩散模型 / 高斯噪声 | inherited; S106 | Optional prerequisite terms only, not the splatting mechanism. |
| quantisation / schema / pipeline | 量化 / schema（结构定义）/ 管线 | inherited; core,S115 | Keep schema identifiers, formats and API names verbatim. |
| rasterisation / rasteriser | 光栅化 / 光栅化器 | new_proposal; new proposal | Image formation by splatting projected primitives; not ray marching. |
| ray marching | 光线步进 | new_proposal; new proposal | Distinct from inherited ray casting 光线投射. |
| covariance / covariance matrix | 协方差 / 协方差矩阵 | inherited; S13/S16/S17 | Shape/orientation matrix; Sigma is not scalar standard deviation. |
| anisotropic / isotropic | 各向异性 / 各向同性 | new_proposal; new proposal | Directional scale differences; preserve actual source usage. |
| unit quaternion | 单位四元数 | new_proposal; new proposal | Four stored components represent rotation with a unit constraint, not four independent orientation degrees of freedom. |
| log-scale / scale | 对数尺度 / 尺度 | new_proposal; new proposal | Parameter log_scale differs from exp(log_scale) and covariance scale squared. |
| spherical harmonics / SH coefficients / degree | 球谐函数 / 球谐系数 / 阶数 | new_proposal; new proposal | Degree L includes degrees0..L, totaling(L+1)^2 basis functions per colour channel; do not confuse16 and48. |
| alpha compositing / front-to-back / back-to-front | alpha 合成 / 从前向后 / 从后向前 | new_proposal; new proposal | Preserve opposite order descriptions as source inconsistency, not interchangeable words. |
| camera intrinsics / extrinsics | 相机内参 / 相机外参 | new_proposal; new proposal | Distinguish screen, camera and world coordinates; intrinsics are not pose. |
| Jacobian / perspective projection / footprint | Jacobian 矩阵（雅可比矩阵）/ 透视投影 / 覆盖区域 | Jacobian inherited from S07; other two are new lexical proposals | Do not repair the source’s evaluation-point ambiguity in prose. |
| tile / depth-sort | 图块 / 按深度排序 | new_proposal; new proposal | 16x16 screen-space regions; not texture files or a learned continuous depth update. |
| densification / clone / split / prune | 致密化 / 克隆 / 拆分 / 剪枝 | 剪枝 inherited from S23/S24/S52/S121 with Gaussian-primitive contextual extension; others are new lexical proposals | Adds or removes geometric Gaussian primitives; not generic neuron pruning or model quantization. |
| floaters | 漂浮伪影 | new_proposal; new proposal | Unwanted disconnected reconstruction primitives, not floating-point numbers. |
| specular highlight / Lambertian shading | 镜面高光 / Lambertian 着色（朗伯着色） | new_proposal; new proposal | View dependence and approximation limits remain as source; no physically guaranteed reflectance recovery. |
| explicit / implicit representation | 显式 / 隐式表示 | new_proposal; new proposal | Scene parameterization, not explicit/implicit numerical integrators. |

Core first-use rules govern. Preserve all source code, formulae, numerical values, dimensions, paths, URLs, names and figure payloads. Translate only eligible prose; do not silently repair source defects. Final own3 publication/readback, installation and authoring remain pending.
