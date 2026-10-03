# S54-glove-fasttext-subword 翻译与验证报告

本课从固定英文独立新译，作者与非作者分别完成全文技术对照及完整中文通读；全部块与最终 hash 绑定，没有未解决的翻译必改项。没有复用旧中文、缓存或上游草稿。代码、公式、标识符、路径、数量和图载荷受保护，源技术问题保持原意并单独列出。

- [fork 草稿 PR #60](https://github.com/Activer007/ai-engineering-from-scratch/pull/60)
- [实际浏览的固定正文](https://github.com/Activer007/ai-engineering-from-scratch/blob/7433f3d5b6fa72641e306d1b7544af4d7ce2933b/i18n/zh/phases/05-nlp-foundations-to-advanced/04-glove-fasttext-subword/docs/zh.md)
- 英文提交：`1bafaa88bb4668356791150bec3a6d7df38387eb`；源 SHA256：`b92cf9d14b8729b4a378b0b4f468f4d957f6600c15d876b091d8dec54d8d3e47`
- 中文 SHA256：`98bb3acff92780f0aa487cef062f000b016ece28c0d063bf20c6353a927b7ba9`
- 本课逐块审校 93 块；独审列出 16 组源问题；固定支持依赖 61 项

## 已验证范围

实际 GitHub GFM 标题、完整表格、强调、代码、公式和适用 Mermaid/SVG 已检查，无须改译文格式。自定义 figure 围栏在 GitHub 仅为代码占位，不能称为原站互动图通过。S52 首张 Mermaid 初次托管加载错误，一次刷新后四图均正常；正文未修改。

本次联合 78 课验证为 76 课原 strict 直接通过，以及仅 S07/S19 既有精确 hash 适配；原控制未放宽，无新增例外。原 33 项回归与 24/50 项适配防护通过。全部 78 篇 Markdown 在两个新目录重放并逐字节核对；5 个 SVG 另行复制、核对，未假称由 Markdown 渲染器生成。课程、认证与 README/图书数量审计通过。额外图书渲染测试 6 项中 5 项通过，PDF 项受 XeLaTeX format/缓存环境限制，单独列为未通过；不以此冒称整书验证通过。

本课支持与正文提交的远端全部文件已 fetch 并逐字节核对。最终证据提交后的全部文件读回和精确 head 的 CI 查询结果，另写 PR 正文及唯一总索引，避免证据自引用。正式总数只以该索引最终读回为准。

## 执行与未通过边界

实际运行、有限夹具、跳过项目和各源问题详见 VALIDATION.json；有限检查不等于完整模型、库、下载或生产实验验证。S52 未运行默认 479 次搜索和 3 次重训，也未运行 Optuna。S53 原 canonical 原规模运行成功；S54/S55/S56 小型原演示与有限验证的实际范围分别记录。

GitHub GFM、原站 parser、完整网站/移动端/交互、托管 CI 及用户发布验收是不同关卡。中文锚点或原站渲染器问题未因 GFM 通过而关闭。Actions 未启用；空 CI 查询不算通过。仅 fork 内 open draft，未合并、未部署、未发布，未向上游写入。
