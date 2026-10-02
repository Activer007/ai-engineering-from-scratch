# S02：终端与 Linux 交付记录

2026-10-02。00/10 Terminal & Shell 与00/11 Linux for AI 均完成从英文独立新译、全文技术对照、独立中文通读与实际GitHub GFM桌面检查，提交到本fork [draft PR #8](https://github.com/Activer007/ai-engineering-from-scratch/pull/8)。累计 **22/523** 课已审新译草稿，剩 **501** 课未启动；README不计入课程数，合并/发布/用户验收没有完成。

## 交付与检查

| 课程 | 翻译提交 | 全部块 / 可译块 | 保护围栏 | GFM |
|---|---|---:|---:|---|
| 00/10 终端与Shell | `cdeb324507e3f02bb09235f0988791c1929956be` | 113 / 44 | 13 | 实际桌面通过 |
| 00/11 AI工作中的Linux | `efaf8bb8115c802996476f4f00fe727413c48655` | 137 / 50 | 19 | 实际桌面通过 |

- 两课全部250块、94个可译块审查完成，无必修翻译问题；不是抽样检查
- 32个围栏载荷逐字保持，包含英文代码注释、Mermaid/figure与Linux速查卡；速查卡仅为裸围栏补 `text`，不会把受保护英文载荷冒称为中文正文
- 36个标题、5张表和逐块数字、路径、flags、快捷键、行内代码、元数据通过保护检查
- GitHub实页核对了两课中文锚点、Mermaid、表格与代码；两处转义管道正确显示为字面 `|`，没有将表格拆列；Linux比较表8行均为3列
- 2/2本阶段严格记录检查；只读组合既有试点和S01后 **22/22** 严格检查、**33** 控制回归和两次全22课重放通过
- 基线审计523课0问题；认证67课、12评估、505题0问题；README计数与空白检查通过
- 27个bash围栏与shell_aliases.sh通过 `env -u BASH_ENV bash --noprofile --norc -n` 静态语法检查；这不是功能测试，未执行任何围栏载荷或别名

## 术语与源风险

[S02术语表](TERMINOLOGY.md)明确区分终端与Shell、进程与作业、前后台、挂断信号、tmux分离/重连、所有者/所属组/其他用户、root用户与根目录、Linux操作系统内核与Jupyter内核。核心和之前阶段术语保持只读。

源文问题保持独立，不在译文中擅自更正：

- `echo $SHELL`不能可靠识别当前执行的Shell；受控只读探针在Bash内仍得到预设的`SHELL=/bin/sh`
- “三种重定向”实际列五行；`grep | wc -l`数匹配行，不数一行里的全部出现次数
- 后台进程、终端关闭、nohup与终止命令的说明有前提省略；广泛pkill、相对source路径、xargs文件名以及邮件通知示例另有适用性风险
- 权限问题不能一概用chmod/sudo解决；tmp清理、远程GUI、文件系统大小写与平台工具差异也存在配置例外
- rsync示例未加`--partial`，不能保证保留中断文件继续传输；[官方手册](https://download.samba.org/pub/rsync/rsync.1)的默认行为已核验
- WSL使用Windows侧NVIDIA驱动的方向正确，但开发编译另需toolkit，不能把所有环境/版本都视作已验证；见[NVIDIA官方指导](https://docs.nvidia.com/cuda/wsl-user-guide/)

没有运行安装器、sudo/chmod/chown、删除、终止进程、tmux、SSH、传输、mail、GPU/云端或Shell配置改动；这些教学命令的出现不构成执行许可。

## 尚未通过的发布面

原站离线解析仍分别产生7和13个空中文标题锚点。真实网站浏览器、移动端、交互figure和用户发布验收未通过。fork Actions仍禁用，托管CI未运行；空检查列表不能当作CI通过。保留draft，不合并、不部署、不向上游写入。

## 复验与记录边界

[TASKS.json](TASKS.json)只增加这两课；[VALIDATION.json](VALIDATION.json)分开记录通过/未通过/未运行；[DEPENDENCIES.json](DEPENDENCIES.json)列出P1控制/术语及S01术语的固定提交与hash。本PR只含S02课程和当前阶段记录，不覆盖旧台账，也不导入其他未合并课程。

在隔离工作树中按DEPENDENCIES.json提取精确支持文件并核验hash后，可以运行 `curated_translation.py check` 和两次仓库外 `render` 比较。单独S02内容树检查2课；22课结果来自额外只读组合树。原33回归包含P1专用夹具，复跑该套测试时须在单独测试树提供固定P1课文及作者/审核记录，不能把夹具提交到本PR。所有这些检查均不要求远端合并。

更大的领域路线与下一阶段约束见[SCOPE.md](SCOPE.md)及其链接的v1.2计划。源技术修正、额外权限/费用和合并部署仍需相应决定，常规已授权新译可继续小批推进。
