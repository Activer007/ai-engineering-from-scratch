# English-first 中文术语规范 v1.0

本表仅用于 Activer007/ai-engineering-from-scratch 的 `zh-curated` 试点。英文源固定于 `1bafaa88bb4668356791150bec3a6d7df38387eb`。不使用已有中文课文、旧翻译缓存或其他中文 PR 作翻译记忆。

## 使用规则

- 先判断上下文，再选译法；不得跨文档机械全局替换多义词。
- 每课技术术语的首次正文出现遵循表内“首现规则”；可译术语通常采用“中文（English / acronym）”，API、SDK、token、schema、KV cache 等按表内推荐形式呈现。后续用表内约定；标题可简洁。
- 品牌、产品、模型 ID、命令、API 标识符、类名、参数、标志、路径、URL、公式、代码、数值和单位保持原样（元数据中的自然语言时间单位按下条规则处理）。代码块及 Mermaid/figure 内文不翻译；图的中文解释放正文，不能改可执行含义。
- 保留英文不等于省略解释：token、schema、SDK 等在正文首次出现时给出简短中文解释，避免硬译专名。
- 元数据键 `Type`、`Languages`、`Prerequisites`、`Time` 保持英文以兼容工具；类型值 `Learn`、`Build`、`Reference` 及语言名保持英文，普通前置条件和时间单位可译。
- 术语新增须写明语境与来源；确需偏离时记录在逐课 review.json。源文本可能存在事实问题，单独记录，不在翻译中悄悄修正。

| EN | ZH / 推荐呈现 | 保留英文 | 首现规则 | 定义与上下文 | 禁用译法 | 例外与来源 |
|---|---|---|---|---|---|---|
| API | API（应用程序编程接口） | 是 | 首次解释 | 程序之间调用能力的接口 | 把 API 当产品名或账户 | 00/04 英文 |
| API key | API 密钥 | API 保留 | 直接使用 | 识别账户并授权请求的密钥 | API 键、随意等同密码 | 00/04 |
| SDK | SDK（软件开发工具包） | 是 | 首次解释 | 提供调用接口的客户端工具包 | 开发包品牌的中文改名 | 00/04 |
| raw HTTP | 直接发送 HTTP 请求 | 否 | 首次注明“不使用 SDK” | 本课指不经提供商 SDK、直接构造并发送 HTTP 请求 | 原生 HTTP（易误解为协议变体） | 00/04 英文 |
| endpoint | 端点 | 可括注 | 端点（endpoint） | API 请求的目标地址 | 终端（指 endpoint） | 00/04 |
| request / response | 请求 / 响应 | 否 | 常规中文 | 网络交互消息 | 返回值（泛指完整 response） | 00/04 |
| request body / response body | 请求体 / 响应体 | 否 | 常规中文 | 消息正文 | 请求身体、响应身体 | 00/04 |
| authentication | 身份验证 | 否 | 可括注 | 确认请求者身份 | 授权（混为一谈） | 00/04 |
| authorization | 授权 | 否 | 常规中文 | 决定可执行哪些操作 | 身份验证（混为一谈） | 13/30 |
| rate limit | 速率限制 | 否 | 速率限制（rate limit） | 单位时间请求限制 | 速度极限 | 00/04 |
| token | token（词元） | 是 | 首次解释 | 模型处理/计费文本单位；不必等于单词 | 一律译成令牌、字 | 凭据上下文用“令牌”；00/04、10/01 |
| streaming | 流式输出 | 否 | 流式输出（streaming） | 逐步返回响应 | 直播 | 00/04 |
| LLM | 大语言模型（LLM） | 是 | 首次解释 | large language model | 大型语言模特 | 00/04 |
| agent | 智能体 | 可括注 | 智能体（agent） | 执行任务的智能系统 | 代理人 | 网络 proxy 不套用；README PR1 |
| reusable artifact | 可复用成果 | 否 | 常规中文 | 学习后可复用的文件/工具 | 人工制品 | README PR1 |
| artifact | 产物 | 视语境 | 构建产物等 | 可交付文件或工具 | 固定一律“工件” | 14/42 |
| prompt | 提示词 | 可括注 | 提示词（prompt） | 给模型的指令或输入 | 提示符（在 LLM 上下文） | shell prompt 可为提示符 |
| schema | schema（结构定义） | 是 | 首次解释 | 数据字段、类型和约束 | 图表、仅“格式”遗漏约束 | 19/70 |
| targets | `targets` | 是 | 解释为目标列表 | schema 中字段名 | 改字段为“目标” | 19/70 |
| model | 模型 | 标识符除外 | 常规中文 | 学习/推理模型 | 模特 | `GPTModel` 原样 |
| configuration | 配置 | 标识符除外 | 常规中文 | 参数集合 | 模型实体 | `GPTConfig` 原样；19/35 |
| feature selection | 特征选择 | 可括注 | 首次中英 | 选择输入特征子集 | 特征提取（混为一谈） | 02/18 |
| filter method | 过滤法 | 可括注 | 首次中英 | 不依赖预测模型的筛选 | 过滤器模型 | 02/18 |
| wrapper method | 包裹法 | 可括注 | 首次中英 | 用模型表现评价子集 | 打包法 | 02/18 |
| embedded method | 嵌入法 | 可括注 | 首次中英 | 在训练过程中选择特征 | 词嵌入法 | 02/18 |
| embedding | 嵌入 | 可括注 | 首次中英 | 向量表示或映射 | 嵌入法（混淆选择方法） | 按向量/层上下文补充 |
| singular value decomposition | 奇异值分解（SVD） | SVD | 首次中英 | 矩阵分解 | 奇怪值分解 | 01/11 |
| singular value / vector | 奇异值 / 奇异向量 | 否 | 常规中文 | SVD 的值及方向 | 特征值/向量（无条件替换） | 01/11 |
| complex number | 复数 | 否 | 首次可括注 | 有实部、虚部的数 | 复杂数字 | 01/19 |
| imaginary unit | 虚数单位 | 否 | 符号保留 | 满足 i²=-1 的单位 | 想象单位 | 01/19 |
| magnitude / phase | 模 / 相位 | 可括注 | 按上下文解释 | 复数的长度/角度 | 阶段（指相位） | 数值大小可译幅值；01/19 |
| spectrogram | 频谱图 | 可括注 | 首次中英 | 时间—频率能量表示 | 单纯频谱（漏时间轴） | 06/02 |
| mel / MFCC | mel / MFCC | 是 | mel 解释为梅尔频率尺度；MFCC 解释为梅尔频率倒谱系数 | mel 是频率尺度；MFCC 是音频特征系数 | 擅自改写缩写 | 06/02 |
| sample / sampling | 样本 / 采样 | 否 | 音频可用采样点 | 一次观测/取样过程 | 混同毫秒和采样数 | 06/02 |
| attention | 注意力 | 否 | 首次可括注 | 关联查询与键值的机制 | 关注度（一律替换） | 07/12 |
| KV cache | KV cache（键值缓存） | 是 | 首次解释 | 缓存已计算的键和值 | 缓存所有注意力结果 | 07/12 |
| FlashAttention | FlashAttention | 是 | 可补中文解释 | 专有算法/实现名称 | 闪电注意力等自造名 | 07/12 |
| tokenizer | 分词器 | 可括注 | 分词器（tokenizer） | 文本与 token ID 的映射 | 保证按词分割 | 10/01 |
| BPE | BPE（字节对编码） | 是 | 首次解释 | 合并频繁符号对 | 改写算法缩写 | 10/01 |
| fine-tuning | 微调 | 可括注 | 首次中英 | 继续训练调整模型 | 精调与微调混用 | 11/08 |
| LoRA / QLoRA | LoRA / QLoRA | 是 | 中文解释低秩适配/量化组合 | 算法名称 | 强行音译 | 11/08 |
| quantization | 量化 | 可括注 | 首次中英 | 降低数值表示精度 | 数量化 | 11/08 |
| block | 块 | 可括注 | 按对象解释 | 如 64 个权重一块 | 把块当单个权重 | 11/08 |
| guardrail | 安全护栏 | 可括注 | 安全护栏（guardrail） | 检查/限制模型输入输出行为 | 保证绝对安全 | 11/12 |
| prompt injection | 提示词注入 | 可括注 | 首次中英 | 非可信输入改变模型指令行为 | 普通提示词输入 | 11/12、13/30 |
| BLIP-2 / Q-Former | BLIP-2 / Q-Former | 是 | 中文说明其作用 | 视觉—语言桥接架构/模块 | 自造模型中文名 | 12/03 |
| registry | 注册表 | 可括注 | 首次中英 | 组件发布/发现的元数据目录 | 注册机构（无条件使用） | 13/30 |
| digest / signature | 摘要 / 签名 | 否 | 可括注 | digest 为内容摘要；signature 为用于验证真实性与完整性的数字签名；二者不可互换 | 摘要与签名互换 | 13/30 |
| provenance | 来源信息 | 可括注 | 首次中英 | 可追溯来源及构建证据 | 仅“名称” | 13/30 |
| drift | 漂移 | 可括注 | 说明变化对象 | 版本/内容/行为偏离基线 | 所有更新都是攻击 | 13/30 |
| fail closed | 失败即拒绝 | 是可括注 | 首次解释 | 验证失败就拒绝继续 | 失败后继续放行 | 13/30 |
| scaffold / workbench | 脚手架 / 工作台 | 标识符除外 | 首次中英 | 项目结构模板/开发工作区 | 翻译目录或产品名字 | 14/42 |
| latency / throughput | 延迟 / 吞吐量 | 否 | 首次可括注 | 耗时/单位时间处理量 | 两者互换 | 17/22 |
| load test | 负载测试 | 可括注 | 首次中英 | 压力负载下测量服务行为 | 负荷考试 | 17/22 |
| first-token latency | 首 token 延迟 | token | 首次解释 | 首个输出 token 到达的耗时 | 完整响应耗时 | 17/22 |
| capstone | 综合项目 | 可括注 | 首次可括注 | 综合运用已学技能的项目 | 顶石 | 19/35、19/70 |

## 不可强译的英文清单

- 品牌与产品：Anthropic、OpenAI、Google、Claude、Hugging Face、Python、TypeScript、Rust、Julia、PyTorch、NumPy、GitHub、VS Code、Cursor、MCP、Agent Skills
- 架构、算法与激活函数：Transformer、GPT、BERT、BLIP-2、Q-Former、LoRA、QLoRA、BPE、ReLU、GELU、softmax、Adam、FlashAttention
- 模型 ID 和别名：按源文逐字保留，包括 `claude-sonnet-5`；保留不代表已核实当前可用性
- 代码/协议：函数、类、属性、JSON key、HTTP 方法和头、环境变量、CLI 参数、路径、URL、错误字符串、fixture ID 全部原样
- 缩写：API、SDK、HTTP、JSON、URL、LLM、SVD、FFT、STFT、MFCC、GPU、CPU、RAM、KV、TTFT、TPOT、p50/p95/p99 保留并在需要时解释
- 数学：公式、变量名、上下标、正负号、矩阵维度、数值、单位原样；中文只解释其含义，不重新推导或悄悄订正

来源链接均以固定英文课程路径为准：`https://github.com/Activer007/ai-engineering-from-scratch/blob/1bafaa88bb4668356791150bec3a6d7df38387eb/phases/<phase>/<lesson>/docs/en.md`。README 术语仅取本 fork 新译 PR1 的已审术语，不读取旧课程中文。
