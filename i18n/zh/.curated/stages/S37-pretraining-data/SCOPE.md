# S37：预训练数据处理流水线

2026-10-02。初始 43 项只读依赖已核验；协调者追加 S34–36 词表后，最终 46 项再次逐 Git/hash 核验，manifest SHA256 为 `8b81c7570923d1cc4ea580864cc83e1320c6bc9bcb88b4ad02f9f9a4e4e757f8`。独占作者范围为 10/03；英文先行，从固定英文逐段独立新译。正文不复用历史中文、旧翻译缓存或旧上游 PR 452/457。前置课 10/01–02 已由协调者确认完成；本阶段无需读取它们的中文。

- 固定源提交：`1bafaa88bb4668356791150bec3a6d7df38387eb`
- 固定英文：`phases/10-llms-from-scratch/03-data-pipelines/docs/en.md`
- 英文 SHA256：`75ed5890977f72a36387b7cbea1db9b67a90ca4ba784223ec2f69e4b8cd37a44`
- 中文目标：`i18n/zh/phases/10-llms-from-scratch/03-data-pipelines/docs/zh.md`
- 作者记录：`i18n/zh/.curated/lessons/10-03/translation.json`，保持 `draft`
- 仅写本课中文、作者记录、本阶段范围/术语与作者 QA；不写公共 review、通用控制或总索引
- 不改英文、源码、quiz、产出提示词或站点；不 push、不操作远端、不合并、不启用 Actions
- 451 行、169 个无损块；11 个围栏包括 6 个 Python、3 个 Mermaid、1 个 figure 和 1 个数学说明围栏。所有载荷原样；唯一裸围栏仅补 `text`
- 元数据键、Type/Languages 值、代码、标识符、API、路径、URL、模型/数据集名、公式和数字原样。自然数量单位的等值译法列于本阶段术语文件

## 作者检查与运行边界

作者先完成完整 EN/ZH 技术对照，再另行完整中文通读；独立审核由其他作者完成，作者不代写独立批准。逐块 hash、检查范围、源码已预读和实跑证据见作者报告与 `qa/`。

执行前完整读取原控制脚本、原测试、离线解析脚本及其实际提取的站点函数、原课程 main.py 和所有嵌入 Python 片段。原 main.py 为纯标准库，内部生成 15 篇小文档，默认 100 次 BPE 合并；不含联网或文件写入。未改规模，在外部 60 秒 timeout 下完整执行。22 项边界测试只用小型本地夹具，执行原 main 的函数及前五个预读片段；它们不是全规模生产验证。原测试目录不存在，不能将本阶段测试冒称原课程自带测试。

HuggingFace 示例需 `datasets`/`transformers`（非依赖 allowlist）以及外部语料/模型访问，不执行、不安装、不下载。没有执行产出提示词、Wikipedia 训练练习、API 请求、GPU 训练、TB 级吞吐测试或完整大语料基准。没有声称模型/平台数字已获当前事实验证。

原 core 的 capture/check/render 与原 33 回归照常使用；重放仅检验外部两个新目录中的字节一致性。原站离线 parser 可暴露中文锚点限制，但不等于浏览器视觉检查、实际 GitHub GFM 或最终网站验收；这些由协调者单独处理。
