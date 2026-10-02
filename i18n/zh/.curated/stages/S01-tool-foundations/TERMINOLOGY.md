# S01 工具基础术语增量 v1.0

日期：2026-10-02。与固定核心 v1.0 及试点附表 v1.1 联用，不改写其既有含义。首次正文中按下表解释，后续可用中文；代码、命令、路径、品牌、字段、快捷键原样。引用语境均来自固定英文 S01 四课。

| EN | 推荐呈现 | 语境 / 不可混淆项 | 来源课 |
|---|---|---|---|
| development environment | 开发环境 | 包括工具链配置；不等同仅虚拟环境 | 00/01 |
| toolchain | 工具链（toolchain） | 完成开发工作的相互配合工具 | 00/01 |
| runtime | 运行时（runtime） | Python/Node/Rust/Julia语言执行层，不是运行耗时 | 00/01 |
| package manager | 包管理器（package manager） | 管理软件包的工具 | 00/01、00/06 |
| preflight | 环境预检（preflight） | 运行前核验；命令或文件名不译 | 00/01 |
| shell | Shell（命令解释器） | 命令交互层；不能译为操作系统内核 | 00/01、00/06 |
| repository / repo | 仓库 | Git 跟踪的项目及其历史 | 00/02 |
| fork | 分叉（fork） | 当前课指托管平台上的仓库副本；不同于编辑器课的产品派生版本 | 00/02 |
| branch | 分支（branch） | 同一仓库的工作线；不是 fork | 00/02 |
| commit | 提交（commit） | Git记录/动作；commit hash、命令及Conventional类型不译 | 00/02 |
| staging / stage | 暂存 | Git index语境；不是课程阶段 | 00/02 |
| merge | 合并（merge） | 合并Git历史；不暗示允许合并本项目PR | 00/02 |
| pull request / PR | 拉取请求（pull request，PR） | 协作审查机制；PR缩写与平台按钮保留 | 00/02 |
| diff | 差异（diff） | 文件或提交之间的变化 | 00/02、00/05 |
| dependency | 依赖项 | 项目需要的软件包；先修依赖按教学语境区分 | 00/06 |
| virtual environment | 虚拟环境（virtual environment） | Python包隔离；不是虚拟机 | 00/06 |
| dependency resolution | 依赖解析 | 为约束选择兼容版本；不是解析源代码语法 | 00/06 |
| lockfile | 锁文件（lockfile） | 记录解析后的依赖；具体文件名原样 | 00/06 |
| transitive dependency | 传递依赖项 | 依赖项自身需要的依赖 | 00/06 |
| pin (a version) | 锁定（版本） | 仅版本锁定语境；不同于Registry中的完整“锁定记录” | 00/06 |
| editable install | 可编辑安装 | 使用源码目录开发的安装模式；`-e`原样 | 00/06 |
| notebook | 笔记本（notebook） | Jupyter交互文档；不是笔记本电脑 | 00/05 |
| cell / code cell | 单元格 / 代码单元格 | 笔记本文档的执行或文本单元 | 00/05 |
| kernel | 内核（kernel） | 本课指后台执行单元格的Python进程；不同于操作系统内核/CUDA kernel | 00/05 |
| magic command | 魔法命令（magic command） | IPython的`%`/`%%`接口；不能改成普通Shell命令 | 00/05 |
| hidden state | 隐式状态（hidden state） | 乱序执行后内存变量与可见文档不一致；不是模型hidden state | 00/05 |
| memory leak | 内存泄漏 | 源文用语照译；累积引用/缓存是否严格为泄漏另记源问题 | 00/05 |
| inline (output/plot) | 在单元格中显示 | 不套用函数“内联”优化含义 | 00/05 |
| command mode / edit mode | 命令模式 / 编辑模式 | 笔记本UI两种键盘操作状态 | 00/05 |

不把安装步骤的存在当作执行授权；不因当前工具版本或源文错误静默改写原意。新增技术更正应进入逐课 source_issues。
