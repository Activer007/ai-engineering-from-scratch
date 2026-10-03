# S67-anomaly-detection 翻译与验证报告

本课固定英语源为 `1bafaa88bb4668356791150bec3a6d7df38387eb`。作者完成全文技术对照及单独中文通读，另一位审校者完成独立双读；全部 257 块及作者对应块保持原哈希绑定，没有重写或删减原审校结论。源技术风险完整保留在 VALIDATION.json，未在译文中静默修复。

- [自有 fork 草稿 PR #73](https://github.com/Activer007/ai-engineering-from-scratch/pull/73)
- [已实际浏览的固定正文](https://github.com/Activer007/ai-engineering-from-scratch/blob/64b15abbd9dd95939a6c212be9d0ff467e4fcc73/i18n/zh/phases/02-ml-fundamentals/16-anomaly-detection/docs/zh.md)
- 英文 SHA256：`fd2418cd6ece3eb747a71ab926fe1b05f2c1c0e4fb07fafd8506081354a99106`
- 中文 SHA256：`eab087939acd2555dbe977d01cee283e133ae5590c55b7fc440f2ccde70be724`
- 固定支持依赖：74 项；支持文件不计为课程

## 已验范围与真实限制

GitHub GFM 正文和适用图表已按真实截图验收。首图一次同页重载后恢复。第二图使用原生展开、缩放和滚动读取全部下层标签。完整真实整页图与主要分段截图在后续两次浏览器 API 超时前已保存；超时后仅检查已有整页图的可追溯裁图。失败及过渡截图不作完整性证据，未绕行其他 URL、tab 或 raw 下载。

课程 figure 仍为 GitHub 代码占位，不代表站点交互通过。仅验证已保存的真实视觉证据，不把 DOM 存在或未成功截图当成图可读证明；没有重复 raw 下载或绕过被拒路线。

原规模五个固定 NumPy 合成演示已运行；有限诊断只刻画源边界行为。未运行 sklearn/LOF/One-Class SVM/自编码器生产实验、外部数据或 GPU。

候选联合报告包含 90 课，其中 88 课直接通过原 strict，其余仅使用现有 S07/S19 精确哈希适配，无新增例外。原控制 33 项、适配防护 24/50 项通过；90 篇 Markdown 在两个全新目录精确重放一致，11 个 SVG 单独复制并逐字节核对。book 测试 5/6 通过，另 1 项因缺少 xelatex.fmt 环境阻塞；不声称 PDF 成功或完整图书视觉验收。

## 仍未通过的门禁

原课程站解析器锚点验收失败：本批四课共 63 个空标题 ID、2 组重复非空 ID；含待验 S69 的五课观察共 77 个空 ID、3 组重复。本课空 ID 24 个、重复组 2 组。ASCII-only slugify 问题未修改。移动端、课程交互、托管 CI、PDF 和用户发布验收都不能由本地校验替代。

本次证据准备时正式为 86/523，90 为本地候选；最终数以单一索引精确读回为准。本脚本不改索引。S61/10-05、S66/10-06、S69/03-11 均待验并排除；S69 新提交三链接已复验修复；源未转义的星号导致公式乘号显示缺失，完整 GFM 待验；torch 缺失，运行跳过。新 head 展开图也未单独验收。支持 commit 不是课程完成数。

最终证据提交、精确 head 的 CI 和总索引读回由协调者另行处理，避免证据自引用。仅 own-fork Draft，不合并、不部署、不对上游发 PR。原代码、图、英文、中文、translation.json 与原双读块均不变。
