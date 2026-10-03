# S64-embedding-models-deep-dive 翻译与验证报告

本课从固定英文独立新译。作者与非作者分别完成全文技术对照和完整中文通读，全部 105 块与最终哈希绑定，无未解决的翻译必改项。源技术问题与翻译质量分开记录；代码、公式、数字和图载荷保持源意。

- [fork 草稿 PR #70](https://github.com/Activer007/ai-engineering-from-scratch/pull/70)
- [实际浏览的固定正文](https://github.com/Activer007/ai-engineering-from-scratch/blob/10af2b412b44b708200c2745a5ea9a7c80b896c4/i18n/zh/phases/05-nlp-foundations-to-advanced/22-embedding-models-deep-dive/docs/zh.md)
- 英文提交：`1bafaa88bb4668356791150bec3a6d7df38387eb`；源 SHA256：`bfb5483ccac7e580a5256434b2a7e4ea749c30999fabc4aead4a95189e8c96b0`
- 中文 SHA256：`65881f601e369332be41c08908d9d45ea87579e8005a1db30e8331816b10a2c2`；固定支持依赖70项

## 已验证范围

实际 GitHub GFM 已检查全文与适用的图表、强调、代码和公式。实际观察范围与限制：Referenced SVG labels readable without intrinsic clipping; long protected skill fence inspected using native horizontal scroll. Source dimensional/storage arithmetic remains a semantic caveat. Custom figure remains code fallback.

自定义 figure 围栏仍为 GitHub 代码占位，不代表课程互动图通过。源问题保留，具体见 VALIDATION.json。

候选86课联合验证中，84课直接通过原 strict；另两课仅用原 S07/S19 精确哈希适配，无新例外。原33项回归、24/50项适配防护通过。86篇 Markdown 在两个新目录逐字节重放一致；9个 SVG 独立复制核对，不假称由 Markdown 渲染器产生。课程、认证与数量审计通过。图书测试5/6通过，PDF项因缺少 xelatex.fmt 的环境限制未通过，不代表整书视觉验收通过。

原站解析器在本次四门可验收课程中生成62个空标题 ID，并在 S63 的 module 形成一个重复非空 ID 组。另行保留的 S66 观察多出15个空 ID 与重复 sft，五课机械观察共77个空 ID、两组重复；S66 未计入本次验收。本课空 ID 为 10 个，重复 ID 为 []。原 ASCII-only slugify 会删除中文并把部分混合标题折叠为同一 ID；渲染器未改，课程站点锚点验收未通过。

运行固定小语料 stdlib 演示及有限夹具；哈希教学向量不是真实 Matryoshka 训练模型。未运行模型下载、MTEB、API或生产嵌入库。

## 待完成验收

支持和正文远端字节已核对。最终证据提交读回、精确 head 的 CI 与总数写入 PR 正文及唯一索引，避免自引用。候选86课排除待视觉验收的 S61/10-05 与 S66/10-06。S61第三张3D源图仍有遮挡标签；S66源图的 (pre-trained) 与 (after SFT) 被各组首节点遮挡，中英文同提交均存在。只有最终索引读回后才采用86已审 +2进行中 +435未开始 =523的计数，尚未计为已审的共437课。

完整课程网站、移动端、互动、托管 CI 和用户发布验收未由这些证据证明通过；空 CI 查询不算成功。有限夹具不证明源算法全部正确，不替代生产库、模型、GPU或外部系统验证。仅 fork 草稿，未合并、未部署、未发布。
