# S28 交付报告：逻辑回归

2026-10-02。本阶段完成快照 **50/523 已审课程草稿、2课收尾中、471课未开始**；README另计，发布/合并0。实时总数只更新在PR7 [单一索引](https://github.com/Activer007/ai-engineering-from-scratch/blob/zh/stage-01-tool-foundations/i18n/zh/.curated/ROLLOUT-INDEX.json)。

## 来源与全文双审

固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`，源SHA-256 `28c89a0c75029f41edaaa3aae7428a8a5b30479765ec4c1afdf4853917c25954`，最终target SHA-256 `a3a8f977134302bf98dcad08ebf3f0c6e7073e638fc7a723d7c715cf774f59f3`。526行/156块/60可译块从EN独立新译；另一审员完整技术对照后，对最终中文另遍全文通读，所有块hash绑定，零剩余必改。37固定依赖核验，未用旧中文、cache或历史上游PR稿。

独立审提出并闭环两处首现术语：逻辑回归（logistic regression）、one-vs-rest（一对其余）和multinomial（多项式）。精确率/准确率、召回率/灵敏度、one-hot、二元/类别交叉熵按语境统一；20围栏载荷全部不变，10裸围栏仅补text。

## 实际 GitHub GFM 与最小修复

云端Chrome查看 [固定内容提交](https://github.com/Activer007/ai-engineering-from-scratch/blob/37862c903bf23a108fc772aa087402d6fbd49fd2/i18n/zh/phases/02-ml-fundamentals/03-logistic-regression/docs/zh.md)：23标题、3×3混淆矩阵与13×3术语表、11strong、0em/0残留粗体标记，2幅Mermaid逐框读取并截图显示。F1表内显示完整的 `2*P*R / (P+R)`。

固定英文GFM将F1表的两个裸乘号误读为强调。作者冻结前仅在b0156插入两个反斜杠，独立审确认可逆且数学等价；其后两处首现术语是另一独立差量。证据链：原稿bda47b…→两转义aed18f…→两术语修订最终a3a8f9…。不声称从最终稿单独去掉两转义即可回到最初稿。通用strict未放宽，原始英语未改。

## 有限运行

完整读325行Python与385行Julia源码后，Python原程序以python -S按原1000步等规模执行，exit0；源码尝试可选sklearn导入后走其原ImportError回退，没有载入sklearn或执行安装建议。六个stdlib正文段按原上下文顺序执行，作者16有限断言通过；独立审另分别执行英中六段，stdout完全相同，BCE梯度有限差分最大误差约4.90e-11。样例准确率只是有限证据，不代表泛化质量。sklearn正文整段与Julia均未运行，Julia未安装；无下载、安装或模型API调用。

## 来源边界与未过门槛

17组源问题单列，包括MSE非凸与“局部极小值”混用、sigmoid浮点端点、可分数据无有限最优权重、线性分界与阈值、梯度缩放、F1不等于平衡准确率、测试集阈值调优泄漏、零分母约定、zip截断/形状边界等。忠实保留原源文与代码，不暗改技术结论。

组合 **48课原strict + S07精确符号表例外 + S19精确两行竖线适配**，50课两次重放逐字节一致；原33、S07的24、S19的50控制及523课/67认证课/12评测/505题审计和README计数通过。原站点14个空中文ID与重复sigmoid仍在，实际应用站点/移动/交互和用户发布验收未过。Actions未启用，CI未运行，空状态不是CI成功。最终远端字节/PR元数据/CI状态在本证据提交后检查，记入PR完成说明及单一索引。仅本fork draft，无merge、部署或上游写入。
