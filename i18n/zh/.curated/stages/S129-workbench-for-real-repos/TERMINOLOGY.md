# S129-workbench-for-real-repos 术语约定

固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；本地 own3 候选，未安装、未发布。原作者术语提案证据 SHA256 `8bb7cbdbad10acb88476ea37733a0b5b78c88d9941b3ba477e101448e6bf2ea4`；当前源语境与实际修订边界如下。原 common130 保持，本候选仅追加已独核 S124–S126 TERM 为 common133。

固定源为14-41；沿 core/addendum 与已安装common130的语境校准，不覆盖任何共享术语文件，不创建own3或伪造pin。

| English | 本课中文 | 依据与边界 |
|---|---|---|
| workbench / surface | 工作台 / 组成要素 | 核心及补充表；七种持久工程组成要素，不是UI表面 |
| prompt-only / workbench-guided | 仅用提示词 / 工作台引导 | 本课两条管线的对照条件，不暗示已真实运行 |
| pipeline | 管线 | 沿S57/S72/S101等；本课是按序读写组成要素，不是流水线并行 |
| verification gate / acceptance command | 验证关卡 / 验收命令 | 沿S111/S117/S120，非神经网络门控 |
| scope contract / scope creep | 范围契约 / 范围蔓延 | 沿S120/S104；契约不等于实际权限隔离 |
| feedback runner / reviewer / handoff packet | 反馈运行器 / 审查者 / 交接包 | 沿S117/S123/S84/S102；本脚本未实现这些运行环节 |
| fixture / happy path | 测试样例 / 正常路径 | 沿补充表、S84；源样例并不实现负向校验 |
| harness / evaluation harness | 运行框架 / 评测框架 | 核心补充表；generic agent harness为运行框架，Ship It及benchmark表为评测框架 |
| false negative | 假阴性 | 本课借用该词并立即按源文解释“仅用提示词更快”的任务，不当作分类漏报数据 |
| typed error envelope | 带类型信息的错误封装 | 本课新语境提案；不补造源不存在的具体schema |
| time-to-first-meaningful-edit | 首次实质性编辑耗时 | 本课练习提案，未宣称计时器已实现 |
| before/after report / workbench benchmark | 前后对比报告 / 工作台基准测试 | 保留比较含义；无真实测量的源限制另列 |
| rank | 排名 | 当前为榜单名次，不能沿矩阵/LoRA语境译作秩 |

正文首现解释workbench、surface、prompt、pipeline、agent、happy path、scope contract、feedback runner、verification gate、reviewer、handoff、fixture、LLM、harness、false negative、evaluation harness。已有受保护路径、字段、产品名和图载荷不译。

R03 进一步明确最后一条延伸阅读的 evaluation harness 为评测框架，并恢复“同一个评测框架接入评测驱动开发”的方向；generic agent harness 仍为运行框架。原作者提案与旧交接状态不改。
