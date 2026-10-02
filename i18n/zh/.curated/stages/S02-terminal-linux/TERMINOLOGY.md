# S02 终端与 Linux 术语增量 v1.0

2026-10-02。来源：固定英文00/10与00/11。继承核心术语、试点附表及S01工具基础术语，按本课语境细化。API、命令、flags、路径、变量名、信号编号、快捷键、数值和代码载荷保持英文原样；首次正文可给中英解释。

| EN | 推荐呈现 | 语境 / 边界 |
|---|---|---|
| terminal | 终端（terminal） | 命令交互界面；不等同于解释命令的Shell |
| shell | Shell（命令解释器） | bash/zsh等；元数据语言及命令不译 |
| pipe / piping | 管道（pipe）/ 管道连接 | 将输出作为下一命令输入；保护 `\|` 的原始Markdown记法 |
| redirection / redirect | 重定向 | 输入输出目的地；不混淆网页跳转 |
| stdin / stdout / stderr | 标准输入 / 标准输出 / 标准错误 | 可括注原缩写；标识符内原样 |
| process | 进程（process） | 正在运行的程序实例；不译成流程 |
| PID | PID（进程ID） | 进程标识；数字原样 |
| background / foreground | 后台 / 前台 | Shell作业控制位置 |
| job | 作业（job） | Shell管理的任务；不可机械套用于课程作业 |
| signal / hangup | 信号 / 挂断信号 | 进程控制语境；SIGHUP等标识符原样 |
| kill / terminate | 终止 | 技术动作按源力度区分；不擅自把SIGTERM描述成一定能终止 |
| tmux session | tmux会话 | 与pane/终端窗口区分 |
| pane | 窗格（pane） | tmux窗口中的区域 |
| detach / reattach | 分离 / 重新连接 | tmux会话；不同于删除会话 |
| alias | 别名（alias） | Shell命令简写；不译别名标识符 |
| port forwarding | 端口转发 | SSH流量转发；命令端口号和绑定地址保持 |
| permission | 权限 | 文件访问位；不同于所有权 |
| owner / group / others | 所有者 / 所属组 / 其他用户 | 文件权限的三类对象；不把others当作整个文件组 |
| root directory / root user | 根目录 / root用户 | `/`目录与超级用户分别说明，不能混为同一对象 |
| executable / binary | 可执行的、可执行文件 / 二进制程序 | 按形容词或文件语境选择；实际文件名原样 |
| daemon | 守护进程（daemon） | systemd服务的后台程序 |
| kernel | 操作系统内核（kernel） | Linux/WSL语境；不同于S01的Jupyter代码执行内核 |
| case-sensitive / case-insensitive | 区分大小写 / 不区分大小写 | 文件系统属性；源文对OS的概括另列风险 |
| GPU passthrough | GPU直通 | WSL提供的GPU访问能力；不擅自扩展为所有功能均可用 |
| OOM | OOM（内存不足） | 源文未限定时不收窄为仅GPU显存不足 |
| filesystem / mount | 文件系统 / 挂载 | 路径与挂载点原样 |

源文所示sudo、chmod、rm、kill、SSH、安装和传输只作为教学文本翻译，不是执行授权。发现事实或安全前提缺口时保留原意、记入逐课审核，不在中文中无记录地替换命令。
