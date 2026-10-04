# S126-multi-session-handoff 术语约定

固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`；本地 own3 支持候选，未安装、未发布。以下完整保留作者术语提案的本课用法及保护边界，提案证据 SHA256 `60713b9b706ec2955acf9290e79fb4c415ab27bb42e0f5303e33462d8c702b85`。原作者 common127 已包含 S117 修订 TERM；本轮只追加 S121–S123 已独核固定 TERM 作为参考，当前 common130，不替换旧作者历史。

| English | 本稿译法 | 边界 |
|---|---|---|
| multi-session handoff / handoff packet | 跨会话交接 / 交接包（handoff packet） | 延续S84/S102/S111交接；文件产物不是网络packet |
| next action / verdict pointer | 下一步行动 / 判定结果指针 | 标识符保持；后者指验证和审查报告路径 |
| feedback trim / feedback log | 反馈裁剪 / 反馈日志 | 保留最后K条与全部非零退出记录，不能推定上限 |
| compaction | 上下文压缩（compaction） | 会话上下文压缩，非文件压缩；handoff与compaction的区别完整保留 |
| clean state / dirty tree | 干净状态 / 未清理的工作树 | 工程清理状态；不意味着代码已执行检查 |
| working tree / branch / orphan branch | 工作树 / 分支（branch）/ 孤儿分支 | 工作树沿S111，branch沿S01；HEAD字面量保留 |
| receipt | 凭证 | 本课指报告路径的可追溯依据，不是付款收据 |
| runtime / hook / idempotent | 运行时（runtime）/ 钩子（hook）/ 幂等性（idempotent） | 沿S117、S73/S82和核心补充表 |
| schema / LLM / SDK | schema（结构定义）/ 大语言模型（LLM）/ SDK（软件开发工具包） | 首现解释，产品完整名和标识符保留 |
| verification gate | 验证关卡 | 沿S111/S120及修正后S117；本课正文没有完整术语自然语言出现，不补造，仅供技术风险和后续协同沿用 |

章节名沿补充表九项规范。API路径、产品与品牌、状态枚举、代码/图载荷、URL和数字保持。原文技术矛盾另列SOURCE-RISKS，不在术语统一中偷改事实。
