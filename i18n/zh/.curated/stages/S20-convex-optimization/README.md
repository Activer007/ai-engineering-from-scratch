# S20 交付报告：凸优化

2026-10-02。原图渲染待验项已解除，本课终验完成快照 **43/523 已审课程草稿、0课收尾中、480课未开始**，README另计，发布/合并0。实时状态仍以 PR7 [单一总索引](https://github.com/Activer007/ai-engineering-from-scratch/blob/zh/stage-01-tool-foundations/i18n/zh/.curated/ROLLOUT-INDEX.json) 为准。

## 来源与双审

固定英语 `1bafaa88bb4668356791150bec3a6d7df38387eb`，source SHA-256 `061158e46d86c18ffeb43b730c98c52994ae863629445f6431942a368cfdb952`，target SHA-256 `eedc57205b5fcacba6c3f9db7bfd803387331084b858de232b7b2958cfc38002`。555行/275块/115译块完整独立技术对照及另次中文通读，逐块hash全部匹配，必改项0。25项固定依赖已核验。23围栏载荷原样，仅12裸围栏补text；公式/API/数值/链接受保护，旧中文/cache/上游旧稿未复用。

## 真实 GFM：瞬态阻碍已闭环

首次内容提交a85c0254…中27标题、7表、41strong、0意外em正常，但“约束优化”图报render undefined；一次刷新和对照后仍曾失败，故没有提前计完成。冻结英文相同载荷可显示，不能将其断言为源语法错。

记录待验报告后，在 [固定报告提交](https://github.com/Activer007/ai-engineering-from-scratch/blob/a06cdad082921e0e6548ca137ca5df1f6d6ff26d/i18n/zh/phases/01-math-foundations/18-convex-optimization/docs/zh.md)，dot云端Chrome已实际显示四幅Mermaid并逐框读取全部节点/连接，错误数0，约束图截图清晰。目标正文hash和所有图载荷从冻结到此刻都未改，未用语义修改掩盖平台/页面瞬态。所有表仍完整，含表头依次4×2、4×3、9×3、5×3、5×3、6×4、17×2。

## 运行与源风险

作者完整读635行canonical后，以外部30秒限制原样离线运行9个标准库演示，exit0；4个原标准库实现片段及12项有限断言通过，SciPy/sklearn两段超出allowlist未跑。独立审另跑4片段与有限夹具，不冒称重跑canonical。没有安装或联网。

16组独立源风险另列：凸问题唯一性/收敛、Hessian半正定的可微前提、Newton尺度/步长、约束Lagrangian鞍点、KKT约束资格、强对偶和Slater条件、Fisher/Adam近似、支持向量退化边界等。源事实和代码未暗修，有限数值演示不证明所有定理前提。原站仍18空中文锚点。

## 组合控制和收拢

43课组合为 **41课原strict + S07精确符号表例外 + S19精确竖线适配**，全部两次重放字节一致；原33、S07的24、S19的50控制及523课/67认证课/12评测/505题审计和README计数通过。英文/源码/通用控制未变。

真实应用网站/移动端/交互图、CI、用户发布验收仍未过；Actions禁用，空workflow/status不是CI成功。仅fork draft，无merge、部署、上游写入、安装或模型数据请求。额外两条作者线和必要审员已退出；后续仅一路顺序翻译，仍安排独立审。
