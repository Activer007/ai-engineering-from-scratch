# S04 范围：数据管理

2026-10-02。00/09 Data Management是独立完整主题，显式先修仅00/01；与已完成的Python环境、notebook、终端/云端工具直接衔接。单课约858个可译英文词、55个可译块/137个全块、14个围栏、18个标题、4张表，不为了凑课数与尚需PyTorch背景的00/12混批。

阶段开始时24/523课已审新译，00/09进入进行中。[统一进度索引](https://github.com/Activer007/ai-engineering-from-scratch/blob/zh/stage-01-tool-foundations/i18n/zh/.curated/ROLLOUT-INDEX.json)只在计划分支串行更新；本PR只新增00/09及S04记录，不覆盖索引、旧台账或其他课程。

固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`。从英文独立新译，不用历史中文/缓存/fallback。保持原文单数元数据键Language、train/val/test角色、source块/代码/字段/数值/单位/路径/版本/标识符；裸围栏只加text。正文典型80/10/10、代码70/10/20和练习70/15/15属于不同原文位置，不能为统一而悄悄改数。

完成门槛沿用v1.2：全文技术及独立中文双审，必修译文问题修复后最终hash复核；严格保护、来源/段落记录、双目录重放、基线审计、实际GitHub GFM桌面验收、逐课Conventional提交、本fork draft PR、远端字节核验。实际完成情况写到阶段台账，范围文件不预先计入完成率。

data_utils.py主流程会下载HF数据和模型文件，故不运行。仅进行源码阅读、Python AST及禁profile/清BASH_ENV的Shell `-n`检查；不安装、不下载数据/模型、不执行Git LFS/DVC写入或云存储推送、不访问缓存内容或凭据。种子/数据版本、JSON Lines、DVC本地/远端以及额度/尺寸/性能保证的源问题独立记录，不在中文中修正技术含义。

实际网站/移动端、托管CI、源技术纠错和用户发布验收继续单列未通过。共享依赖按DEPENDENCIES.json在隔离树只读组合，无需合并。普通新译可继续依赖顺序推进；合并、部署、权限/费用、凭据及改变英文技术意义仍另作决定。
