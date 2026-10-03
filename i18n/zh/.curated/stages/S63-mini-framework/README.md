# S63-mini-framework 翻译与验证报告

本课从固定英文独立新译。作者与非作者分别完成全文技术对照和完整中文通读，全部 155 块与最终哈希绑定，无未解决的翻译必改项。源技术问题与翻译质量分开记录；代码、公式、数字和图载荷保持源意。

- [fork 草稿 PR #69](https://github.com/Activer007/ai-engineering-from-scratch/pull/69)
- [实际浏览的固定正文](https://github.com/Activer007/ai-engineering-from-scratch/blob/411482c66d44a72310fa4ca09d0717b3b307da82/i18n/zh/phases/03-deep-learning-core/10-mini-framework/docs/zh.md)
- 英文提交：`1bafaa88bb4668356791150bec3a6d7df38387eb`；源 SHA256：`94d283931d471f9a757d50d4f12656d497b3cb78aacebeb7619a55e5c0e67325`
- 中文 SHA256：`588a0dae949020cd32755998db3311445527bfaa6ab94085399f4078ac2ad244`；固定支持依赖70项

## 已验证范围

实际 GitHub GFM 已检查全文与适用的图表、强调、代码和公式。实际观察范围与限制：Initial transient GitHub render error recovered after one reload. All diagram labels readable using native expanded/scroll/zoom/pan controls, including the first diagram lower labels. Initial viewport does not fit every label; final recovery evidence supersedes initial error screenshots. No intrinsic obscured label remains.

自定义 figure 围栏仍为 GitHub 代码占位，不代表课程互动图通过。源问题保留，具体见 VALIDATION.json。

候选86课联合验证中，84课直接通过原 strict；另两课仅用原 S07/S19 精确哈希适配，无新例外。原33项回归、24/50项适配防护通过。86篇 Markdown 在两个新目录逐字节重放一致；9个 SVG 独立复制核对，不假称由 Markdown 渲染器产生。课程、认证与数量审计通过。图书测试5/6通过，PDF项因缺少 xelatex.fmt 的环境限制未通过，不代表整书视觉验收通过。

原站解析器在本次四门可验收课程中生成62个空标题 ID，并在 S63 的 module 形成一个重复非空 ID 组。另行保留的 S66 观察多出15个空 ID 与重复 sft，五课机械观察共77个空 ID、两组重复；S66 未计入本次验收。本课空 ID 为 14 个，重复 ID 为 ["module"]。原 ASCII-only slugify 会删除中文并把部分混合标题折叠为同一 ID；渲染器未改，课程站点锚点验收未通过。

作者与独审均运行原500样本、三组100轮 stdlib 演示，并做独立有限诊断；演示未使用 BatchNorm，不能证明其导数正确或框架普遍有效。

## 待完成验收

支持和正文远端字节已核对。最终证据提交读回、精确 head 的 CI 与总数写入 PR 正文及唯一索引，避免自引用。候选86课排除待视觉验收的 S61/10-05 与 S66/10-06。S61第三张3D源图仍有遮挡标签；S66源图的 (pre-trained) 与 (after SFT) 被各组首节点遮挡，中英文同提交均存在。只有最终索引读回后才采用86已审 +2进行中 +435未开始 =523的计数，尚未计为已审的共437课。

完整课程网站、移动端、互动、托管 CI 和用户发布验收未由这些证据证明通过；空 CI 查询不算成功。有限夹具不证明源算法全部正确，不替代生产库、模型、GPU或外部系统验证。仅 fork 草稿，未合并、未部署、未发布。
