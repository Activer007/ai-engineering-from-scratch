# S17 交付报告：机器学习统计学

2026-10-02。01/15 已独立新译并完成全文技术对照和另一次中文通读。阶段完成快照 **39/523 已审课程草稿、4课收尾中、480课未开始**，发布/合并为0，README另计。实时总数以 PR7 的 [单一索引](https://github.com/Activer007/ai-engineering-from-scratch/blob/zh/stage-01-tool-foundations/i18n/zh/.curated/ROLLOUT-INDEX.json) 为准。

## 来源与审校

English-first，固定源 `1bafaa88bb4668356791150bec3a6d7df38387eb`。源 SHA-256 `9770d8e715f37b25538f2c9b0e78de30b38d7c1ddccc81765b124880071e0561`，目标 SHA-256 `f102458a193c14a68143bc97af41d5de167461f2c8f9c1e55320fc9b46d381b8`。249块/91候选全部双审并逐块重算来源和译文 hash；必改项0。作者与独立审校分开，没有以自审替代独立审。没有读取旧中文/cache/上游机器翻译稿。

34围栏、公式、数值、API、链接和结构保持；33裸围栏仅补 text。源课没有Python围栏，也没有独立练习/延伸阅读章节；不得把文本公式当成已执行程序。bootstrap（自助法）、有放回重采样、置信区间、p值、统计功效和统计/实际显著性按语境统一；23项固定依赖实字节匹配。

## 实际 GFM

在 dot 云端 Chrome 查看 [固定内容提交](https://github.com/Activer007/ai-engineering-from-scratch/blob/599319df2b3998cba200217e3c15d58358b2608e/i18n/zh/phases/01-math-foundations/15-statistics-for-ml/docs/zh.md)：19标题，完整23×2术语表，49 strong、0意外em，0 Mermaid。截图检查假设检验、bootstrap、关键术语；公式代码块、中文锚点和表格可读，无需额外语法修复。源 figure 标识符仅作为代码块显示，不代表真实站点交互验收。

## 有限执行与源风险

作者完整阅读683行 canonical 后原样离线执行至最后 power simulation，exit0；12项有限断言通过。只用标准库 math/random，无安装、联网、模型调用或数据下载。独立审校另跑 strict、33控制、双重放，没有冒称重新执行 canonical。

14组独立源风险另列：p值/置信区间解释、相关与因果、检验和CLT前提、配对 bootstrap 文字与独立重采样实现不一致、交叉验证折依赖、多重比较、效应量、退化t检验及“无分布假设”等绝对化表述。译文保留原意，未修英语或代码事实。完整定位在本课 review.json；有限演示不能证明源统计结论普适正确。

## 控制与边界

本课原 strict 通过；组合38课原 strict + S07一处精确已审符号表例外，共39课两次重放字节一致。原33控制、S07的24守卫、523课/67认证课/12评测/505题审计和README计数通过，源文、代码与核心控制未改。

原应用站点仍有15个空中文锚点，真实网站/移动端/交互图、CI和用户发布验收未过；Actions禁用，空workflow/status不代表CI成功。全部仅fork draft。

## 调度收拢

按最新要求逐步改为单一路顺序翻译。只收尾已开始的S18/S19/S20/S21及其必要独立审，额外两条作者线完成本轮后退出，不再分配新课。后续仍保留独立技术审和中文全文审，不以减少并行降低质量。
