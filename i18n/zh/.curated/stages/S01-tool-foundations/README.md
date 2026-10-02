# S01：开发与实验工具基础交付记录

2026-10-02。已完成 **4/4 课已审草稿**，本 fork [draft PR #7](https://github.com/Activer007/ai-engineering-from-scratch/pull/7)。加上试点，累计 **20/523** 课独立新译，剩余 **503** 课未启动。这里的完成不代表已合并、用户验收或发布。

## 课程与提交

| 学习顺序 | 课程 | 独立翻译提交 |
|---|---|---|
| 1 | 00/01 开发环境 | `b77e15c09185fff22ce9f987d9a6021034b7c02c` |
| 2 | 00/02 Git 与协作 | `4a65c17e0a4b8917cf7c14b17360ef75effd00f3` |
| 3 | 00/06 Python 环境 | `08aaacd0e2080f0edee91db7614e1cec74c08427` |
| 4 | 00/05 Jupyter 笔记本 | `c08d05ac502b24cf4a239af24345d9dc1d5a8c2e` |

每课一个翻译提交；后续 GFM 证据也按单课提交。计划、术语和本阶段台账单独提交，未合入任何旧试点课程。英文固定于 `1bafaa88bb4668356791150bec3a6d7df38387eb`，没有读取/复用历史中文或缓存。

## 质量结果

- 184 个可译块全文 EN→ZH 技术审查与独立中文通读；470 个源块的稳定身份/顺序保持
- 53 个围栏载荷原样，65 个标题、9 张表格的结构核验通过；5 个 Mermaid 和4个站点 figure 标识符保持
- 修正技能 scope 的歧义为“技能安装范围”；恢复 `10-100x` 的源符号；Jupyter 三处粗体闭合标记后补空格，真实 GFM 已确认生效
- 核心/试点术语只读；[本阶段术语增量](TERMINOLOGY.md) 区分 Git fork、版本 pin、Jupyter kernel、Shell 和隐式状态，明确词项来源
- 当前四课严格记录检查全过；隔离组合旧试点后 **20/20** 严格检查、**33** 控制回归及两次全20课重放均通过
- 课程审计523课0问题；认证审计67课/12评估/505题0问题；README计数与空白检查通过
- 四课真实 GitHub GFM 桌面页面全部检查：中文标题锚点、表格列、代码/字段、图和格式修复；`figure` 仅显示原标识符，不冒称运行了站点交互图
- Python beginner 预检 exit0（2/2必需项）；notebook隔离演示 exit0并生成图；环境安装器仅做 `bash -n`，没有执行安装

## 源文问题和开放门槛

源问题与翻译问题分开。四课没有未解决的 S0/S1/S2 翻译问题，但固定英文仍有必须单独审议的技术/教学问题：

- 00/01 的 GPU 运算目标未由所示可用性检查完整实现；安装步骤存在先决条件省略，不同语言预检的要求也不同
- 00/02 的 pull/remote 图示是简化模型，点击 Fork 本身不会修改已有本地 origin
- 00/06 的 CUDA 双向不兼容断言、Conda/pip 绝对规则、锁文件跨机器保证过度；目录树还引用固定仓库中不存在的旧阶段名称
- 00/05 的 `!pip` 与内核环境可能不同，内存占用不必然等于泄漏；Colab 的固定90分钟/T4表述不能当作服务保证

相关官方核验链接与源块位置已写入逐课 review.json，包括 [NVIDIA 兼容性](https://docs.nvidia.com/deploy/cuda-compatibility/minor-version-compatibility.html)、[Conda 环境管理](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?highlight=prune)、[uv 锁文件](https://docs.astral.sh/uv/concepts/projects/layout/)、[IPython 魔法命令](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pip)和 [Colab FAQ](https://research.google.com/colaboratory/faq.html)。译文没有静默修正这些源问题，也未修改英文或课程代码。

原站解析器本次仍产生空中文标题锚点。真实网站、移动端和发布验收 **未通过**；本阶段没有重新运行实际网站浏览器，不能用 GFM 代替。fork Actions 页面确认继承工作流仍禁用，托管 CI **未运行**。未运行 Rust、可能触发安装的 TypeScript 检查、真实 Jupyter/Colab/GPU、安装器、提供商 API 或 Git 教程中的写入命令。

## 可复验的增量记录

- [TASKS.json](TASKS.json)：只记录本阶段四课及总进度口径；不覆盖试点根台账
- [VALIDATION.json](VALIDATION.json)：实际通过、未通过和未运行分开
- [DEPENDENCIES.json](DEPENDENCIES.json)：共享支持的固定提交及五个文件 hash；它们来自 PR #2，而不是本分支的隐式依赖
- [扩展计划 v1.2](../../ROLLOUT-PLAN.md)：下一批先修/篇幅/风险安排与门槛

复验应在独立工作树中进行：以本 PR 为内容树，从 `f9b5e9cbe4012f54483794f920c0d87b06a7573d` 提取 DEPENDENCIES.json 精确列出的五个只读支持文件，逐一核对 hash；不要导入其他中文。然后运行以下命令（全部为离线检查/重放）：

```bash
python3 scripts/test_curated_translation.py
python3 scripts/curated_translation.py check
python3 scripts/curated_translation.py render --output-dir /tmp/s01-review-a
python3 scripts/curated_translation.py render --output-dir /tmp/s01-review-b
diff -rq /tmp/s01-review-a /tmp/s01-review-b
python3 scripts/audit_lessons.py
python3 scripts/audit_certifications.py
python3 scripts/check_readme_counts.py
```

独立四课内容树的 check 是4课；20课结果来自额外只读组合的试点树，两者不可混称。现有33回归包含 P1 专用夹具；若要原样复跑完整回归，也须把固定P1课文/作者记录/审核记录作为测试夹具放入独立测试树，不能把它们提交到本PR。支持文件和测试夹具都不需要先远端合并。

下一个逻辑完整主题可为00/10终端与00/11 Linux；依照计划继续小批新译时无需因为本阶段结束重复申请常规翻译许可。新增费用、凭据/权限、改变英文技术含义、实际冲突或合并/部署仍应另作决定。本阶段没有进行这些动作。
