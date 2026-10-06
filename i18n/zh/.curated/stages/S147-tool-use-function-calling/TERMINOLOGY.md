# S147 Tool Use and Function Calling terminology support candidate

Fixed English: `1bafaa88bb4668356791150bec3a6d7df38387eb`, lesson 14-06. Short lexical support only, prepared from complete fixed English/source reading. No Chinese lesson prose, author proposal or first-write chronology is supplied. Own3 publication, independent readback and installation remain pending; the coordinator supplies DEPENDENCIES.json.

## Calibration basis

common152 candidate SHA-256: `adb98cb4c54c97f8485605d3d90e10fbe80209705ffcae1545170c1c10c39beb`. Preparation receipt SHA-256: `4d8b3ece2ce2abb6455304075636495184be45bad78d9da5844955b666e8e447`. Common149 identity/order is preserved and accepted S143/S144/S145 terminology appended. Common152 has 144 terminology files plus 8 immutable controls; future own3 adds 3 for a lane total of 155. No support installation or control modification occurred.

Full semantic readings: core TERMINOLOGY.md and TERMINOLOGY-ADDENDUM.md; S22/S40/S45/S116/S132/S135/S138; and all new S143/S144/S145 terminology. Relevant rows of S74/S95/S101/S113/S127/S131 were read as targeted calibration. All 144 terminology payloads were byte-verified against SHA-256, Git blob and size, but unselected files are identity-only, not fully semantically reread. Exact read pins and line ranges are in source-readiness.json. Historical candidate/pending labels inside frozen accepted support do not change their externally verified roles.

## Source-grounded lexical choices

| English | Proposed Chinese presentation | Inheritance and semantic boundary |
|---|---|---|
| tool use / function calling | 工具使用 / 函数调用（function calling） | New scoped distinction. Tool use is the wider activity; function calling is structured call emission/invocation. Do not infer that a provider executed the client tool or that emitted arguments are already validated. |
| tool call / tool result / observation | 工具调用 / 工具结果 / 观察结果 | S132/S144. A call is a request, a result is execution output, and the observation is what enters model context. Output is not automatically trusted evidence. |
| tool registry / tool registration / tool catalog | 工具注册表（tool registry）/ 工具注册 / 工具目录 | Core registry and S132/S135. Registry maps names to definitions/executors; catalog is the model-facing listing. Keep ToolRegistry and all fields exact. |
| tool schema / JSON Schema / schema validation | 工具 schema / JSON Schema / schema 校验 | Core schema（结构定义）first-use explanation; S135 schema 校验. JSON Schema is the specification name, not a visual diagram or an assertion that the toy implements every keyword. |
| tool description / function signature | 工具描述 / 函数签名 | New context-specific lexical entries. Description guides selection; signature describes callable shape. Signature here is not a cryptographic signature. |
| argument / parameter / required field | 实参 / 参数 / 必填字段 | Use 实参 for supplied call values and 参数 for declared input slots; 参数类型转换 remains the natural compound for argument coercion. Preserve argument/field identifiers and required. |
| type coercion / argument coercion | 类型强制转换 / 参数类型转换 | Narrow, unambiguous representation conversion in this source. Do not imply accepting ambiguous inputs, rounding fractions, silently swallowing errors, or identical Python/TypeScript conversion rules. |
| int-as-string / float-as-string | 以字符串表示的整数 / 以字符串表示的浮点数 | Data representation versus numeric value. Quoted examples, types and error messages remain exact. Output-skill and exercise policies differ; do not harmonize them. |
| enum validation / format validation | 枚举值校验 / 格式校验 | Declared finite value set versus date/email/URL formatting. Format validation is discussed but absent from this implementation. |
| validator / executor / dispatch | 校验器 / 执行器 / 分派 | Executor and dispatch follow S135. 校验 here is schema/argument checking, distinct from S144 answer verifier 核验器 and authentication 身份验证. |
| parallel tool calls / parallel dispatch | 并行工具调用 / 并行分派 | S135 parallel vocabulary. Multiple call objects in one model turn do not establish concurrent host execution; both source demo dispatchers are sequential. |
| independent / sequential / correlation ID | 相互独立 / 顺序执行 / 关联 ID（correlation ID） | Independence is dependency compatibility, not merely different names. ID correlates a call with its result; it is not authorization, model token or a statistical correlation coefficient. |
| tool_use_id / tool_result | tool_use_id / tool_result | Exact Anthropic-style fields. Explain ID/result role around protected code, never translate keys or substitute OpenAI field names in the source. |
| structured observation / error observation | 结构化观察结果 / 错误观察结果 | S132/S144 observation vocabulary. The toy wraps plain error strings in metadata; do not invent machine-validated structured error JSON. |
| sandboxing / sandbox boundary | 沙箱隔离（sandboxing）/ 沙箱边界 | New scoped lexical proposal. A declared policy or narrow tool interface is not evidence of enforced process/network/resource isolation. |
| read/write surface / network access / memory cap | 读写访问范围 / 网络访问 / 内存上限 | New security/resource context. Surface is access scope, not the ADDENDUM workbench-components sense. Memory cap is RAM/resource limiting, not the agent's contextual memory. |
| timeout / circuit breaker | 超时限制 / 熔断器（circuit breaker） | Per-call execution limit versus temporary refusal after repeated failures. Neither is implemented by the stored timeout fields; retain 60s and 3 exactly. |
| no-op / refusal / confirmation gate | 空操作（no-op）/ 拒绝 / 确认关卡 | A no-op tool is still a tool call, distinct from emitting no call. Refusal in this context means declining an unsuitable tool; destructive-action confirmation is output-skill context. |
| Toolformer / self-supervised tool annotation | Toolformer / 自监督工具调用标注 | S22/S127 自监督 plus new compound. Preserve method name; annotations are training-corpus call insertions, not human comments or a claim of zero human demonstrations. |
| training signal / pretraining corpus / filtered corpus | 训练信号 / 预训练语料库 / 筛选后的语料库 | S45 pretraining vocabulary. Filtering examples and fine-tuning weights differ from dispatch-time argument checks. |
| next-token loss / fine-tuning | 下一 token 预测损失 / 微调（fine-tuning） | Core token（词元）, S22/S45 next-token and S40 loss. Do not equate a token with a word or silently replace source shorthand with the paper's fuller weighted-loss formula. |
| BFCL / Berkeley Function Calling Leaderboard | BFCL / Berkeley 函数调用排行榜 | Preserve BFCL and the original full proper name when protected or first introduced. Benchmark score weights are not dataset shares, current model pass rates or local test results. |
| Agentic / Multi-Turn / Live / Non-Live / Hallucination | 智能体类 / 多轮类 / Live（真实用户提示词类）/ Non-Live（合成测试用例类）/ 幻觉类 | New scoped BFCL category labels. Live is user-contributed prompt provenance, not livestreaming or necessarily live execution. Preserve source capitalization and percentages; source category simplifications are separate caveats. |
| state-based evaluation / API state / AST | 基于状态的评测 / API 状态 / 抽象语法树（AST） | New lexical context. Compare resulting state with call syntax; not model hidden state. Preserve AST and distinguish evaluation from training validation. |
| hallucination detection / wrong-tool-picked failure | 幻觉检测 / 选错工具的失败 | S74/S95/S101/S132/S144 hallucination. Here unsuitable/nonexistent tool calls; no safety guarantee or measured #1 ranking is inferred. |
| dynamic decision-making / long-horizon tool chaining | 动态决策 / 长时程工具调用链 | S135 long-horizon context. Horizon concerns many dependent steps, not necessarily long wall-clock duration. Keep 20+ and 40 steps as source claims. |
| memory / partial observability / trajectory | 记忆 / 部分可观测性 / 轨迹 | S138 memory and S135 trajectory; partial observability concerns incomplete environment information, not merely missing logs. Distinguish memory from the RAM cap above. |
| runtime / production-shape / production agent | 运行时（runtime）/ 具备生产系统形态 / 生产环境中的智能体 | S132 runtime. Shape describes an interface pattern and does not certify production readiness, sandbox safety or actual provider integration. |
| provider / translation layer / tool adapter | 提供商 / 转换层 / 工具适配器 | Core SDK/API and ADDENDUM adapter. Translation layer converts provider schemas/protocols here, not human-language translation. |
| description-quality check / observability / span | 描述质量检查 / 可观测性 / 追踪跨度（span） | S132/S144 span vocabulary. Output skill requests these features; no OpenTelemetry span was emitted or installed. |
| pass rate / benchmark / mini-eval | 通过率 / 基准测试 / 小型评测 | Evaluation vocabulary with scoped lexical additions. Exercise requests are not completed experiments; preserve denominators and category scope. |

## First use and protected content

Core first-use rules apply: retain relevant English/acronyms with short Chinese explanations at the first body occurrence, then use calibrated terms consistently. Explain API（应用程序编程接口）, SDK（软件开发工具包）, token（词元）and schema（结构定义）when first used as eligible prose. Preserve Toolformer, BFCL V4, Schick, Patil, NeurIPS, ICML, Anthropic, OpenAI, Gemini, Bedrock, Vercel AI SDK, LangChain, Pydantic, Zod, JSON Schema and all actual product/paper/model names. Preserve QA and AST with context; do not invent algorithm acronyms or rename provider fields.

Keep metadata keys Type/Languages/Prerequisites/Time and Build/Python unchanged. ~60 minutes may become ~60 分钟. Preserve the exact source Phase 13 · 01 number despite its title mismatch with 13-02. Common headings remain 学习目标、要解决的问题、核心概念、动手实现、实际使用、交付成果、练习、关键术语、延伸阅读, preserving order and adding no absent sections.

All inline identifiers, code payloads, paths, URLs, numbers, percentages, signs, quoted data values and table structure remain exact. Preserve the tool-routing figure payload and all SVG bytes. Only the two bare fences may receive the existing reversible text label during later authoring. Source code includes both Python and TypeScript but metadata remains as written. New observations, corrections, safety instructions or translator notes must not be inserted into the Chinese body without separate scope approval.

The fixed-source caveats in SCOPE.md remain separate from lexical choices: sequential dispatch, unused timeout fields, missing sandboxing/format validation, schema-subset and numeric edge cases, demo-count mismatch, prerequisite/forward-pointer mismatches, provider dialect differences and overstated benchmark/scaling claims. Terminology preparation is not factual endorsement, runtime validation or future author calibration.
