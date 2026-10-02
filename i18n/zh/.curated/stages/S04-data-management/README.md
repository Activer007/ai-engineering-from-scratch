# S04：数据管理交付记录

2026-10-02。00/09 Data Management已完成独立英文新译、完整技术对照、独立中文通读和真实GitHub GFM桌面检查，位于本fork [draft PR #10](https://github.com/Activer007/ai-engineering-from-scratch/pull/10)。翻译提交：`c4debc5cad215ee6098894c9fecb3f14e368804b`。

累计 **25/523** 课已审新译草稿，00阶段11/12。阶段结束时498课未启动；未来阶段开始后，以[单一总索引](https://github.com/Activer007/ai-engineering-from-scratch/blob/zh/stage-01-tool-foundations/i18n/zh/.curated/ROLLOUT-INDEX.json)的进行中/未启动区分为准。README不计入课程分母，未获合并/部署/发布批准。

## 质量与运行面

- 全258行、137块、55个可译块完整审校；无必修S0–S3译文问题
- 14个围栏载荷原样，仅裸gitignore围栏加text；单数Language、数字/单位、字段/路径、数据集ID/config和所有API保持
- 真实GFM检查18个标题、4张表（4/3/4/3列）、中文锚点、Mermaid、加粗边界、train/validation/test角色；原典型比例、代码比例与练习比例均未擅自统一
- 1/1本阶段strict通过；只读组合前批后 **25/25** strict、**33** 控制回归、两次全25课字节一致重放通过
- 基线审计523课0问题；认证67课、12评估、505题0问题；README计数与空白检查通过
- 5个bash围栏静态语法、6个Python围栏和data_utils.py AST通过；主流程含HF数据/模型下载，**未执行**，没有冒称完整运行成功

## 英文源问题单列

review.json记录9项带日期/来源的源风险，译文没有静默纠正：

- 典型说明80/10/10、实际代码70/10/20、练习70/15/15是不同位置的数字；示例需要解释差异
- 同一个seed还依赖输入数据/顺序/环境，示例没有锁revision；缓存命中也不等于零I/O或立即加载
- `Dataset.to_json`默认JSON Lines，`.json`扩展名并不使整个文件变成单个JSON数组，见[HF接口文档](https://huggingface.co/docs/datasets/en/package_reference/main_classes#datasets.Dataset.to_json)
- 源文Git LFS免费1 GB已不符合当前计划依赖的额度说明，见[GitHub官方计费说明](https://docs.github.com/en/billing/concepts/product-billing/git-lfs#free-use-of-git-lfs)；保留源值，不推断用户账户额度
- `dvc add`先进入本地缓存，远端另需配置与push，见[DVC add](https://doc.dvc.org/command-reference/add)和[DVC push](https://doc.dvc.org/command-reference/push)
- 流式内存恒定、格式速度/体积排行、Parquet最佳及约10GB本地/云端分界是需要条件的入门概括
- 工具脚本还下载模型config、写临时目录并读取缓存，不能当作纯离线校验

没有安装、下载数据/模型、执行LFS/DVC写入、配置或推送云存储、读取缓存内容或访问凭据。安全静态检查不代表联网库、数据版本、格式转换或性能实测通过。

## 开放门槛与记录

原站解析仍产生10个空中文标题锚点。真实网站/移动端/交互figure/托管CI/用户发布验收未通过，Actions保持禁用，所有工作留在本fork draft。

[TASKS.json](TASKS.json)、[VALIDATION.json](VALIDATION.json)、[TERMINOLOGY.md](TERMINOLOGY.md)只增加S04。[DEPENDENCIES.json](DEPENDENCIES.json)固定只读支持文件的提交与hash；本PR不复制旧课程或覆盖前批台账。总索引只在PR #7计划分支按最新blob SHA串行更新，按lesson_id去重，不相加各阶段累计数。

单独内容树检查1课；25课结果来自额外只读组合树。33回归另需固定P1测试夹具，不把它们提交本PR。00/12调试仍按basic PyTorch先修后置，后续可按数学基础依赖顺序继续。
