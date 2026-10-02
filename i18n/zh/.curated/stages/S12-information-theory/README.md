# S12 交付报告：信息论

2026-10-02。本阶段只做 01/09，接续已审的概率基础，保留从熵到交叉熵/KL、互信息、标签平滑与困惑度的完整主题。阶段完成快照为 **34/523 已审课程草稿，489 课尚未开始，发布和合并均为 0**，README 不计入课程分母。实时状态仅由 PR #7 分支的 [ROLLOUT-INDEX](https://github.com/Activer007/ai-engineering-from-scratch/blob/zh/stage-01-tool-foundations/i18n/zh/.curated/ROLLOUT-INDEX.json) 维护。

## 新译和完整双审

英文固定 `1bafaa88bb4668356791150bec3a6d7df38387eb`，不复用旧中文、cache 或历史 PR 草稿。源 SHA-256 为 `56e2b277862358e636e71058ac13e9cd31366d39105702aa91570844e1e38953`；最终中文为 `63ebd666171e03710bc9403be20e65e431a5f22a14f8871f6f053fb3b72901be`。

作者之外完成全部 471 行、225 块、87 候选的 EN/ZH 技术对照，再独立通读全部中文；必修问题为 0，没有以抽样替代全文。每块审读记录绑定来源与目标 hash，重点复核 P/Q、条件方向、bits/nats、熵/交叉熵/KL、MI、软目标、似然归约与困惑度。

26 围栏载荷原样，18 裸围栏仅补 `text`；公式、代码/API、图、数字、链接和表格结构保护。4 处中文 strong 后保留源空格；本课无需新增乘号或表格竖线修复，也没有新增 strict 例外。术语增量把矩阵/概率/信息语境与之前数学术语联用，保留 logits、softmax、token、KL 等专名/API 的适当英文。

## 真实 GFM 与运行边界

在 dot 云端 Chrome 检查 [不可变内容提交](https://github.com/Activer007/ai-engineering-from-scratch/blob/aae3697060756718d39a58fa5d284a1d0979ba74/i18n/zh/phases/01-math-foundations/09-information-theory/docs/zh.md)：26 标题、2 张完整表（4/3 列，含表头 4/11 行）、8 个 strong、0 个意外 em；中文链接、条件竖线、单位换算、指数底、0.025/0.925 软目标与似然公式均可读。六节点熵关系 Mermaid 经滚动、一次缩小和 reset 后分视图检查全部节点/连线。`entropy-kl` 只作为代码显示，不代表原网站交互图验收。

先完整阅读程序，再隔离运行未改的标准库 canonical 和正文 5 个标准库载荷，以及 1 个已安装 allowlist NumPy 载荷，均 exit 0；6 个 Python 载荷均 AST 通过。18 个标准库与 6 个 NumPy 数值断言通过，涵盖熵、CE/KL、MI、链式关系、单位、硬标签/平滑目标与困惑度。没有安装包、下载数据、调用模型或跑语言模型 benchmark；PyTorch/TensorFlow 的完整行为未验收。

6 组来源边界与 2 项 NumPy 支持域观察均单列：

- `P=Q` 时 CE 可以为正，而额外 KL 为 0；“浪费的信息”不能无条件等同 CE 总量
- 独立公平 bit 的 XOR 中，各单特征 MI 为 0，联合 MI 为 1 bit；低单变量 MI 并不等于无用噪声
- 二类词表、真类概率 0.001 可产生约 1000 的困惑度；它不是词表大小上界
- 源教学函数未完整校验概率域、归一化、形状和对数底；`zip` 可静默截断
- `[-1000,0]` 真类 0 的数学 NLL 约为 1000，源 softmax 后再 log 却可能下溢到 `log(0)` 并报错
- 正 P 配零 Q 的 CE/KL 为无穷；NumPy 负 Q 可为 NaN；自定义 perplexity 的非 e 参数统一走以 2 为底路径

这些有限例子不验证普遍校准改善、特征选择完备性或跨 tokenizer 困惑度可比性；离散熵结论也不能直接移用于微分熵。

## 控制与未过门槛

本课原 strict 通过。只读合成共 **33 课原 strict + S07 一处精确已审数学符号表例外**；原 33 项控制和 S07 24 项守卫通过；34 课两次受控重放逐字节一致。S07 原检查器仍保留既有误报，不声称全部旧 strict 无例外。基线审计为 523 课零问题、67 认证课/12 测验/505 题零问题，README 数量与空白检查通过。

15 组独立源问题含定位与原论文/官方 API 依据，见本课 review：CE/KL 混用、离散/连续熵边界、MI 交互与估计、相关系数/分箱复杂度、标签平滑与校准、uniform 项记号、CE/NLL 单位和归约、困惑度解释和未指定基准、下溢、输入域、压缩条件、决策树准则和零损失极限。它们作为源问题保留，不擅改译文或保护代码。

原网站离线解析有 19 个中文空锚点；真实网站/移动端/交互图仍未验收。2026-10-02 04:51 UTC 实际 GitHub Actions 页仍显示本 fork workflows 禁用，未启用；空 workflow/status 不能当 CI 成功。只提交本 fork draft，未合并、未发布、未做上游写入。

## 增量记录与下一范围

SCOPE/TERMINOLOGY/DEPENDENCIES 为范围、术语和 18 项只读依赖；TASKS 绑定来源、目标与审校 hash，VALIDATION 区分已过/未过。新记录只在 S12 和 01-09 命名空间，旧阶段台账不被覆盖，总索引串行 CAS。

下一阶段只做 01/10 降维，374 行、72 候选、13 围栏、约 1710 正文英文词；线性代数、矩阵变换、概率及试点 SVD 已审。保留 PCA→方差解释→t-SNE/UMAP→kernel PCA→重构的主题完整性，源风险和联网/不在 allowlist 的 sklearn/UMAP 路径另列；不把源技术更正或网站未过项混入新译范围。
