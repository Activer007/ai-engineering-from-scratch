# S51 情感分析：范围与边界

2026-10-02。本阶段仅独立新译 05/05 Sentiment Analysis，并记录可复核的审校证据；前置 05/02 与 02/14 已完成审校交付。

- 固定英文：`1bafaa88bb4668356791150bec3a6d7df38387eb`
- 源路径：`phases/05-nlp-foundations-to-advanced/05-sentiment-analysis/docs/en.md`
- 源 SHA256：`6c0d5587fd261631bbf70042e355315dd840b25ea237f8525e5970dd10f87534`，260 行
- 目标路径：`i18n/zh/phases/05-nlp-foundations-to-advanced/05-sentiment-analysis/docs/zh.md`
- 56 项固定控制与术语依赖见 `DEPENDENCIES.json`；逐项验证本地字节、固定 Git 字节与声明 SHA256 一致。manifest SHA256：`38fcca71f9ac69299a1e8a9a6d22f37e3cca3273d074499c2c54d39cbbdacb33`
- 作者仅写本课正文、作者记录与本阶段增量；独立审员另作全文英中技术对照和完整中文通读。公共 review、索引、远端提交及最终验收由协调者管理。

从固定英文逐段独立新译；不读取或复用历史中文、旧 PR 中文、翻译缓存。保留源代码、数据字符串、API、参数、路径、公式、数值、链接、figure 与产物提示词载荷；裸围栏只补 `text`。自然语言数量等值映射逐块记录。`sentiment-logits` 是 figure 标识，不能把 GitHub 代码占位显示作为真实网站交互验收。

重点区分情感正负类别与指标正类、否定范围与标点、多项式朴素 Bayes 条件独立与逻辑回归、宏平均/微平均/加权 F1、正文数字标签与 canonical 的 `+`/`-` 标签，以及 L2 惩罚系数。源事实或实现问题单列，不通过译文修正；特别核对示例仅实现正类 F1、NB/LR 能力断言、未验证的准确率提升和生产适用性断言。

所有待执行代码须完整预读；仅允许已安装的依赖白名单与标准库，设置外置 timeout。canonical 为 118 行 stdlib 情感分类演示；正文另有 NumPy 逻辑回归定义，二者实际执行范围分别记录。跳过 sklearn 示例，不安装库、不下载 IMDb/SST-2/Yelp 或模型、不调用外部模型 API、不执行产物提示词。必要的官方资料核查限于具体源风险。

使用未修改的 `scripts/curated_translation.py` capture/check/render；作者记录保持 draft，逐块绑定源与目标 hash。运行原 33 项回归、两个新建且位于工作树外的重放目录逐字节比较，以及三项仓库审计。实际执行结果由验收记录另载，本文不预先宣称通过。全课程网站、移动交互、托管 CI、合并和发布均需各自证据。
