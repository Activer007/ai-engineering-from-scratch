# S13 交付报告：降维

2026-10-02。只做 01/10 降维，保持 PCA、方差解释、t-SNE/UMAP、核 PCA 与重构的完整主题。阶段结束快照：**35/523 已审课程草稿，488 未开始，发布/合并均为 0**。README 不计入课程分母；实时进度只在 PR #7 的 [单一总索引](https://github.com/Activer007/ai-engineering-from-scratch/blob/zh/stage-01-tool-foundations/i18n/zh/.curated/ROLLOUT-INDEX.json) 维护。

## 新译与双审

- 来源固定 `1bafaa88bb4668356791150bec3a6d7df38387eb`，EN-first，不读旧中文/cache/历史机器翻译 PR
- 源 SHA-256：`13f508adaa0599b3db8d18ad77c9b20b501cf6864dd242ad884a48412e41bcfc`
- 最终中文 SHA-256：`1944260ad1e635f2ba4fd353fb16455982d989a3e82bc1fed3c04e65f105b9ee`
- 独立审校完整覆盖 374 行、169 块、72 候选，先 EN/ZH 技术对照，再完整纯中文通读，必修项 0；逐块双 pass/hash 齐全
- 13 围栏载荷原样，5 裸围栏仅补 text；数字/API/公式/图/链接保护，无新增 strict 例外
- 术语区分中心化/标准化、方差/任务信息、特征向量/投影、核函数/系统内核、t-SNE 邻域困惑度/语言模型评估困惑度

## 实际 GFM 与验证

在 dot 云端 Chrome 查看 [不可变正文提交](https://github.com/Activer007/ai-engineering-from-scratch/blob/05e21b0c369b3d4f989987da79e6f24f1e43a177/i18n/zh/phases/01-math-foundations/10-dimensionality-reduction/docs/zh.md)，DOM 和截图确认 24 标题、4 表（4/3/3/3 列，含表头 7/4/6/10 行）、13 strong、0 意外 em，中文链接可定位。RBF 双范数竖线、负号/平方、两个裸乘号正确显示，无需额外转义；PCA Mermaid 两节点、全部换行文字及旋转箭头完整可读。`pca-axes` 只显示为代码，不算原站交互图验收。

原 strict 本课通过；组合为 **34 课原 strict + S07 一处精确已审纯符号表例外**。33 项原控制、24 项 S07 守卫、35 课两份受控重放字节一致、523 课与 67 认证课/12 评测/505 题审计、README 计数及空白检查均通过。旧 S07 原 strict 仍有已记录误报，不冒称无例外全部通过。

## 运行范围

先完整读 canonical，再仅导入未改模块并调用 `demo_kernel_pca`、`demo_reconstruction_error`、`demo_synthetic` 三个离线 NumPy 函数；正文前两个 NumPy 载荷也运行，均 exit 0。全部六个正文 Python 载荷 AST 通过。16 个数值断言覆盖 PCA 形状、中心化、协方差、标准正交、特征值/方差比、重构、SVD 子空间与核投影。未执行会调用 `fetch_openml` 的 main，未下载 MNIST，未安装或运行非 allowlist 的 sklearn/UMAP，也未验证 t-SNE/UMAP 或分类器基准。

五组有限边界证据已记录：保留约 99% 方差仍可完全丢失某个分类目标的信息；元素均方误差与丢弃样本协方差特征值之和相差 `(n-1)/(n*d)`；核 PCA 的 `u/sqrt(lambda)` 是系数，训练投影是 `sqrt(lambda)*u`，源码与源说明步骤需区分；单特征/常量/越界 k 缺输入保护；合成示例不能冒称真实数据或下游准确率验收。

## 未过门槛与记录

14 组源风险按行/块单列，包含先修标题不一致、维数/距离泛化、方差与信息、核投影缩放、重构归一化、算法复杂度/全局结构、用测试集选 k 和输入边界。只做翻译必要核实，未扩展源文纠错研究或暗改技术意义。

原网站解析仍有 14 个中文空锚点和重复 pca；真实站点/移动端/交互图、CI 和用户发布验收未通过。Actions 保持禁用，空 workflow/status 不是 CI 成功。只本 fork draft，不合并、不部署、不上游写入。

SCOPE/TERMINOLOGY/DEPENDENCIES 固定范围、术语与 19 项只读依赖，TASKS/VALIDATION 绑定交付 hash 与门槛。只新增 S13/01-10 命名空间，不覆盖旧阶段台账。下一阶段接 01/12 张量操作；01/11 SVD 已在试点完成，不重复翻译。张量课 344 行、67 候选、15 围栏，需单独验证形状、步幅/内存和 einsum，保持完整单课。
