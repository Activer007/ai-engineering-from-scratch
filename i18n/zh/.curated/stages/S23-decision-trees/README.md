# S23-decision-trees 交付报告：决策树与随机森林

2026-10-02。完成快照 **45/523 已审课程草稿、3课已开始、475课未开始**。另两作者当前S26/S27在独立工作树进行，S25只是后续计划，不计入在途；README另计，发布/合并0。实时总数以PR7 [单一索引](https://github.com/Activer007/ai-engineering-from-scratch/blob/zh/stage-01-tool-foundations/i18n/zh/.curated/ROLLOUT-INDEX.json) 为准。

## 来源与双审

固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；source SHA-256 `012e6e8f09a1eda4f03ca395221e5aa30287a782b885a197d563ff79b5ca750c`，target SHA-256 `42857fb62aa5b27d7eac711107d580c80e627fa48c5c3497b0d985e83b204e92`。English-first独立新译，完整477行/179块/75译块技术对照和另次中文通读，所有块hash重算匹配，必改项0。作者与审员分开，不读取作者自审作为独立依据，不复用旧中文/cache/历史PR。围栏代码、图、公式、API、数值与路径保持。

## 实际 GFM

在dot云端Chrome检查 [固定最终内容](https://github.com/Activer007/ai-engineering-from-scratch/blob/135821dc16783c65f07ac34c7d96c9fd7c7d4bcf/i18n/zh/phases/02-ml-fundamentals/04-decision-trees/docs/zh.md)，22标题、2完整表、14 strong、0意外em、0未解析粗体标签；2幅Mermaid逐框内容实际显示。原figure标识符是保护代码块，不是实际站点交互验收。

两表含表头7×3、13×3；特征重要性的中文冒号和粗体标签实际正常，无需GFM修复。15围栏载荷未动，7裸围栏仅补text；32依赖核验。bootstrap/Bagging、Gini/熵、信息增益与MDI按既有词表统一。

作者654行标准库源码全读后原样执行8演示至SUMMARY，exit0；4个原正文定义块和16有限断言通过。独立审另执行4片段/8核验，并未重跑canonical。sklearn示例按allowlist跳过。14组独立源问题另列：类别输入原生支持的概括、纯叶与单样本混同、信息增益/复杂度条件、训练集上重要性偏差、森林树数增加并不保证测试准确率单调提升、正文重复fit追加树而canonical清空、XOR零增益提前停等。英文/源码未修。原站18空中文ID。

## 组合控制与边界

45课组合：**43课原strict + S07精确符号表例外 + S19精确两行竖线适配**，两次重放逐字节一致。原33、S07的24、S19的50控制及523课/67认证课/12评测/505题审计、README计数通过；英文/源码/通用控制未改。所有源问题只单列有限证据，不暗修、不扩大研究。

真实应用站点/移动端/交互图、CI及用户发布验收仍未过，Actions禁用，空状态不是CI成功。没有安装、模型API、模型/数据下载；仅fork draft，不merge/部署/上游写入。最新要求恢复3条排他作者线，已实际确认启动；协调者单写术语汇总、远端和总索引，当前批终验优先，待验不超过一轮。
