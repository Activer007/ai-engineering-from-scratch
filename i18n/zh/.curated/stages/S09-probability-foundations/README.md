# S09：概率与分布交付记录

2026-10-02。01/06 Probability and Distributions完成固定英文独立新译、作者外全文技术对照、最终中文独立通读及真实GitHub GFM检查，位于本fork [draft PR #15](https://github.com/Activer007/ai-engineering-from-scratch/pull/15)。内容检查提交 `5dedf524dcd69e184f19a361453a6b068ff6911c`。

累计 **31/523** 课已审新译草稿，本阶段结束时492课未开始。以[单一总索引](https://github.com/Activer007/ai-engineering-from-scratch/blob/zh/stage-01-tool-foundations/i18n/zh/.curated/ROLLOUT-INDEX.json)为实时准绳；README不计入课程分母，草稿不代表发布批准。

## 全文质量

- 458行、197块、72候选块完整双审；26标题、2表、27围栏保护，18个裸围栏仅补text标签
- 独立技术审纠正一处语气强化：EN for numerical stability不意味着保证所有输入稳定，中文唯一改为“以提高数值稳定性”；最终hash和唯一差异独立复核
- 正态密度表格公式的4个乘号做最小可逆GFM转义，数学内容未变；条件概率的竖线转义原样保留
- 真实GFM检查26标题、两表（4/3列）、10项strong、0意外em；正态公式4乘号完整，P(A|B)在同一单元格没有多列。联合表X天气为行、Y带伞为列，边际方向与数值完整
- 本课原strict通过，无例外。组合为30课原strict，加S07已批准的唯一纯符号表例外1课；33原控制与24例外防护回归通过，全31课两次组合重放字节一致
- 基线523课0问题，认证67课/12评估/505题0问题，README计数和空白检查通过

## 运行范围

完整阅读源程序后，用 `python -S` 执行原样隔离的 `probability.py`，stdlib计算/抽样部分exit0。全机虽已安装Matplotlib与SciPy，本批按AGENTS依赖allowlist主动不执行它们：stays stdlib-first for educational clarity。程序的“matplotlib not available”仅指该隔离执行模式，不代表全机未安装。

8个正文Python载荷均AST通过；前6个stdlib载荷原样按次序执行exit0。第7个可视化片段和第8个SciPy对照未执行；可视化片段含未定义sigma和Ellipsis占位，不能因AST成功声称可直接运行。canonical确实有完整绘图实现，只是本批没验证绘图分支。

14项数值断言加1项联合分布非独立判定通过，覆盖条件概率、PMF/PDF、期望方差、边际、softmax平移、交叉熵与固定随机输入抽样。控制注入RNG0用于边界复现，不代表默认随机种子自然遇到了该值。PyTorch未安装，练习的框架对照未做。未安装依赖、下载数据或改源代码，也未做完整统计/输入域验收。

## 13项源风险仍开放

review.json给出源位置、证据及处置。译文保持源义，不把技术纠正混进翻译：

- CLT对“任意分布”的表述缺少中心化、尺度标准化和分布/矩条件；概率公理只写了二事件有限可加性
- 条件概率分母非零前提、句子概率的条件链、所有预测/损失都作分布解释等概括需限定
- `exp(102)`对Python双精度有限，对float32则溢出；0.01的30次/50次方在双精度下均非零，不能无条件声称约30项就下溢
- 源 `log_softmax([1e16,1e16])` 实际返回[0,0]，重加巨大max再相减丢失log(2)，应有值是[-log(2),-log(2)]；这里仅记录，不修代码
- Box–Muller在注入u1=0时出现log(0)错误；类别采样r<=c边界可选中前置零质量类别；未归一化输入还可返回少于n个样本
- Bernoulli支持域、分布参数、矩存在性、softmax边界、交叉熵与负对数似然的标签条件、抽样/重参数化及可视化片段限制分别记录

正常示例成功或有限抽样不能证明CLT、消除这些源问题，或替代全面数值分析。源技术修正须另行决定。

## 未通过与协作

原网站解析器在本课产生18个空中文标题ID。实际网站、移动端、交互figure、Matplotlib/SciPy/PyTorch验收、托管CI与用户发布验收仍未通过。GFM中的gaussian-pdf只是代码标识。Actions保持禁用，本fork draft，不merge、部署或上游写入。

本阶段仅新增S09和01-06记录；依赖按DEPENDENCIES固定只读。组合验收保留S07例外的严格范围，不扩展到本课；总索引仍由PR #7规划分支串行CAS维护，按lesson_id去重。
