# S04 数据管理术语增量 v1.0

2026-10-02。固定英文00/09；联用核心、试点和S01–S03术语。库名、字段、文件扩展名、API、dataset ID/config/revision、命令、路径、数值与单位保留；首次可译正文可加简短中文解释。

| EN | 推荐呈现 | 语境 / 边界 |
|---|---|---|
| dataset | 数据集（dataset） | 与数据库、单条记录区分；`Dataset`类名保持 |
| split / dataset split | 划分 / 数据集划分 | 命名子集；不混淆字符串split方法 |
| train / validation / test | 训练集 / 验证集 / 测试集 | 三者角色不能交换；代码键`train`/`val`/`test`原样 |
| seed / random seed | 随机种子（seed） | 不是完整可复现性保证；版本与输入条件另列源问题 |
| streaming | 流式读取（streaming） | 数据逐步迭代，不套用LLM“流式输出” |
| IterableDataset | `IterableDataset`（可迭代数据集） | 类名原样，解释只在代码外 |
| row / column | 行 / 列 | 样本记录与特征字段；不可互换 |
| columnar | 列式 | 文件/内存布局；非“列查询”专属含义 |
| format conversion | 格式转换 | 不改变数据本身的任务语义 |
| CSV / JSON / Parquet / Arrow | 保留格式名 | 中文说明性质；不擅自改API/文件扩展名 |
| JSON Lines / JSONL | JSON Lines / JSONL（逐行JSON） | `.json`扩展名不保证整个文件是一个JSON数组；源代码默认行为单列 |
| zero-copy | 零拷贝（zero-copy） | Arrow语境，不泛化为所有操作从不复制 |
| cache | 缓存（cache） | 已取数据的本地副本；命中不等于零I/O或永久可用 |
| fingerprint | 指纹（fingerprint） | 数据摘要标识；本课工具仅取样，不代表全数据唯一内容hash |
| checkpoint | 检查点 | 模型状态文件；不译模型ID或扩展名 |
| revision | 修订版本 / 版本 | Hub版本或提交语境；API参数名原样 |
| Git LFS | Git LFS（Git大文件存储扩展） | 仓库内保留指针，大文件另存；收费/额度按源照录并单列 |
| pointer | 指针 | LFS/DVC的引用记录，非内存地址 |
| DVC | DVC（数据版本控制） | 工具名保留；不把本地缓存等同已推送远端 |
| remote storage / backend | 远程存储 / 存储后端 | S3/GCS品牌、URI与bucket原样 |
| version control | 版本控制 | 管理数据/模型版本；不暗示本次执行Git/DVC写入 |
| data pipeline | 数据处理流水线 | 数据加载/转换/划分流程 |

源文典型80/10/10、代码70/10/20和练习70/15/15分别保留，不能为“统一”而改数。围栏载荷、字段/路径和元数据键（本课为单数Language）原样保护。下载、云端、LFS/DVC写入与凭据操作未获执行授权。
