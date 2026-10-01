# 中文独立重译试点

本目录记录 16 课风险试点的任务、术语与审核证据。所有课程从固定英文独立重译，未读取或复用历史课程中文、旧 PR 中文或旧翻译缓存。`zh-curated` 基线直接来自 fork/main；历史 `translations` 分支不动。README 新译在独立 draft PR #1，不在这里重复或合并。

## 范围与交付

- 唯一写入仓库：`Activer007/ai-engineering-from-scratch`
- 固定英文：`1bafaa88bb4668356791150bec3a6d7df38387eb`
- 所有课程 PR 的 base：本 fork 的 `zh-curated`；head 也必须是本 fork
- 每课独立 Conventional commit（标题不超过 72 字符）；工具/术语独立支持提交
- 每批 draft PR；不合并、不部署、不启用 Actions，不运行全库付费翻译
- 源课程和程序保持不变；代码、标识符、链接、公式与数值受保护
- 课程路径：`i18n/zh/phases/<phase>/<lesson>/docs/zh.md`
- 作者记录：`lessons/NN-MM/translation.json`，含稳定块 ID、类型、标题上下文和 source hash；`review.json` 绑定已审 target hash
- `TERMINOLOGY.md` 是本试点术语与英文保留清单；`TASKS.json` 是可执行台账

## 分批顺序

| 批次 | 课程 | 目的 |
|---|---|---|
| P1 | 00/04 | 单课闭环，冻结术语与安全检查 |
| P2 | 01/19、12/03、19/70 | 按实施计划完成初选四课，覆盖数学、表格和 schema |
| P3 | 01/11、02/18、06/02 | 数学与特征：维度、否定、采样和系数 |
| P4 | 07/12、10/01、11/08、11/12、19/35 | 模型实现：缓存、分词、量化、安全护栏、类与配置 |
| P5 | 00/08、13/30、14/42、17/22 | 工具与生产：快捷键、协议安全、跨文件产物、性能 |

批次之间不依赖未经批准的课程合并；共享控制文件在 P1 PR 中提出，其他批次只提交自己的课程及审核记录。合并由仓库所有者决定。

## 本地命令

```bash
python3 scripts/test_curated_translation.py
python3 scripts/curated_translation.py check
node scripts/check_curated_render.js i18n/zh/phases/00-setup-and-tooling/04-apis-and-keys/docs/zh.md
python3 scripts/curated_translation.py render --output-dir /tmp/curated-run-a
python3 scripts/curated_translation.py render --output-dir /tmp/curated-run-b
diff -rq /tmp/curated-run-a /tmp/curated-run-b
python3 scripts/audit_lessons.py
python3 scripts/audit_certifications.py
python3 scripts/check_readme_counts.py
```

先对每课英文与候选中文完整技术审校，再完整中文审校。初次录入使用 `capture --lesson phases/<phase>/<lesson>`；它拒绝重录已有作者记录。后续修订须明确修改作者记录和对应课文、更新 hash 并重新审校，不能把旧审核自动继承给新内容。

`check` 为只读，验证固定源、内容 hash、术语版本、结构及受保护 token；不会联系任何模型。`render` 仅在仓库外离线重放作者记录，拒绝覆盖不同内容，重复输出应字节相同。它不是自动翻译模型，也不是发布器。新的 `.curated` 记录不会读写旧 `.cache`，没有自动英文回退。

`drift` 只输出保守的变更候选，不自动改写课文。完全相同的唯一块可保留 ID 并标为移动；重复块标为不确定。修改/新增/删除必须人工确认。文件改名目前只有 helper 夹具验证，尚未实现跨路径自动发现；不声称完整增量同步系统已完成。

数字与行内代码按每个源文块的多重集合核对；块内为中文语序所作的重排必须经人工逐项确认，不能借此交换语义角色。检查器区分 factor-of-10 等词语连接号与负号，并补充真实 CLI 重放/防覆盖回归。

自动检查无法判断所有语义、自然语言单位换算或术语歧义，不能替代逐课双审。模型精确版本、采样参数和 token 用量不由当前运行时提供，记录为 unavailable，不虚构成本或质量分。

## 验收状态与真实限制

`language-reviewed` 只代表翻译双审状态，不代表用户批准、网站验收或发布。

- GitHub GFM：逐课在本 fork 的实际文件页面检查，结果写入 review
- 原站 renderer：可以离线执行其解析函数；此检查不是浏览器视觉验证
- 真实网站：当前环境的本地浏览器与云浏览器预览路线均不可用，保持 **未通过/环境阻塞**，不因此将草稿标为最终验收
- 原站兼容性：`site/lesson.html` 的英文-only `slugify` 会为纯中文标题产生空锚点；英文节标题专用样式也不识别中文。应在单独的站点适配工作中修复并真实复验
- 继承的 Actions 在 fork 中未启用；本地检查通过不等于托管 CI 通过
- API 示例不执行，不传递密钥，不产生外部模型 API 费用；可运行的离线测试另记
- 发现英文源事实问题时保留忠实译文并单列风险；未经核实不能当作当前产品说明

## 试点完成摘要

16/16 课已提交为本 fork 内的5个draft PR，并完成实际GitHub桌面检查；仍未通过最终网站/发布验收。当前结果、所有PR链接和后续建议见 [PILOT-REPORT.md](PILOT-REPORT.md)，严格控制回归为33项。

重放只输出zh.md，并不打包SVG或站点资源；原SVG在仓库内作固定源/目标双向校验。

最后更新：2026-10-01
