# S144 Self-Refine and CRITIC terminology support candidate

Fixed English: 1bafaa88bb4668356791150bec3a6d7df38387eb. Short lexical support only; no Chinese lesson prose or future author chronology. The coordinator supplies DEPENDENCIES.json and owns common149/formal157 bindings. Own3 publication, independent byte readback and installation remain pending.

## Source-grounded lexical choices

| English | Proposed Chinese presentation | Inheritance and semantic boundary |
|---|---|---|
| Self-Refine | Self-Refine | Preserve the method name. A short explanatory label may be 自我改进; do not rename the paper or conflate this output-revision loop with fresh Reflexion trials. |
| CRITIC | CRITIC | Preserve uppercase method name. Its tool-interactive critique differs from a general critic role; do not translate the acronym as 批评家. |
| iterative output improvement / iterative refinement | 输出迭代改进 / 迭代改进 | Revision of successive answers, not parameter fine-tuning, a convergence proof or image/coordinate refinement. New context-specific lexical proposal. |
| generate / feedback / refine | 生成 / 反馈 / 改进 | Three roles; keep protected function labels and code payloads in English. S117/S138 feedback vocabulary. |
| generator / feedback provider / refiner | 生成器 / 反馈提供者 / 改进器 | Source role names; neither a model-count guarantee beyond the actual source nor names of imported classes. |
| evaluator-optimizer / Evaluator / Optimizer | 评估器—优化器 / 评估器 / 优化器 | Evaluator follows S138/S141. Optimizer revises text here, unlike Adam updating parameters; keep source capitalization in names/identifiers. |
| critique / critic / self-critique | 评议 / 评议器 / 自我评议 | A diagnosis of an answer's faults, not merely a scalar grade. Preserve CRITIC as the method name. New scoped lexical proposal. |
| verifier / verification / verify step | 核验器 / 核验 / 核验步骤 | An answer-checking component; inherits S138 核验 in tool-grounded verification. Not login authentication or an automatic proof of truth. |
| external verifier / tool-grounded verification | 外部核验器 / 以工具结果为依据的核验 | S138 exact phrase. External refers to evidence outside model self-evaluation; the local toy is a hard-coded check, not an external service call. |
| grounding / grounded critique | 以外部信息为依据 / 以外部信息为依据的评议 | Use the actual evidence source when named. S104/S138 grounding vocabulary; tool output can still be wrong. |
| self-verification / self-evaluation / self-rated | 自我核验 / 自我评估 / 自行评分 | S138/S141 self-evaluation. Separate a model's judgment from tool-backed evidence and deterministic checking. |
| output guardrail / guardrail loop | 输出安全护栏 / 安全护栏循环 | Core/S132 安全护栏（guardrail）. An output tripwire is not itself an automatic refinement retry; keep this source caveat outside translated prose. |
| tripwire / trip / output rejection | 触发机制 / 触发 / 拒绝输出 | Preserve OutputGuardrailTripwireTriggered and output_guardrails. Triggering is not proof that retrying occurred. |
| refine history / prior outputs and critiques | 改进历史 / 先前输出与评议 | Historical attempts in the prompt; not training data, weight updates or a claim that the toy actually consumes all history. |
| stop condition / stop policy | 停止条件 / 停止策略 | S132. Preserve each original OR/AND formula and separate budget exhaustion from successful verification. Do not reconcile the source's conflicting versions silently. |
| iteration / iteration budget / max-iteration cap | 迭代 / 迭代预算 / 迭代次数上限 | Counted loop attempts; not training epoch, wall-clock time or token budget. max_iters and max_iterations remain distinct identifiers. |
| convergence / over-refinement | 收敛 / 过度改进 | A source-level success/plateau description, not a mathematical convergence guarantee or evidence of monotonic improvement. |
| rubber-stamp loop / self-agreement failure | 机械认可循环 / 自我附和失效 | A critic uncritically accepting the generator's answer. Avoid a literal stationery interpretation; new scoped lexical proposal. |
| hallucination / factual error / reference data | 幻觉（hallucination）/ 事实错误 / 参考数据 | S74/S95/S101/S132 hallucination. A reference list is not a comprehensive knowledge base. |
| false positive / noisy verifier | 误报 / 有噪声的核验器 | A failure flagged for an acceptable output in this context; do not reverse with a missed error. The 30% is the source exercise assumption. |
| absolute improvement / relative improvement | 绝对提升 / 相对提升 | Preserve +20 and the source units exactly; do not convert an absolute performance change to a relative percentage or a locally measured result. |
| ablation / history ablation | 消融实验 / 移除历史的消融实验 | Comparison after removing a component. The exact paper claim remains subject to source caveats; no experiment was rerun. |
| code interpreter / test runner / type checker / linter | 代码解释器 / 测试运行器 / 类型检查器 / 静态检查工具 | Distinct validation tools. Listed examples do not grant permission to execute them. |
| structured critique / violations / suggested fixes | 结构化评议 / 违规项 / 建议修复项 | Preserve JSON keys violations[] and suggested_fixes[] and pass/fail. The code emits strings and a bool, not this proposed schema. |
| pure function / stub verifier / scripted producer | 纯函数 / 桩核验器 / 脚本化生成器 | Program properties and demonstrator components, not evidence of actual model/tool interaction. |
| agent / agent loop / observation | 智能体（agent）/ 智能体循环 / 观察结果 | Core/S132. Retain the distinction between an observation and trusted ground truth. |
| Reflexion / reflection / episodic memory | Reflexion / 反思 / 情景记忆 | S138/S141. Reflexion is a proper name; do not reuse geometric reflection or conversational paraphrase senses. |
| LLM / prompt / token / SDK | 大语言模型（LLM）/ 提示词（prompt）/ token（词元）/ SDK（软件开发工具包） | Core first-use rules; code tokens and API/product names stay unchanged. |
| latency / human review / observability | 延迟 / 人工审查 / 可观测性 | Core/S132 context. The source's 1-3 passes is a recommendation, not a measured optimum or executed escalation. |
| OpenTelemetry GenAI span / trajectory | OpenTelemetry GenAI 追踪跨度（span）/ 轨迹 | S132 span and S135/S138 trajectory. Shipped skill context only; no tracing or telemetry was installed or sent. |

## Inheritance, first use and protected material

Byte checks matched all 141 terminology files from common149, including the unchanged common146 prefix plus final accepted S140/S141/S142. Full semantic readings covered core TERMINOLOGY.md, S132, S138 and the three appended term files; relevant rows across the remaining pinned set were searched. ADDENDUM first-use and common-heading rules were read. This is lexical calibration, not full semantic rereading of all historical support, and not the future author's own proposal/calibration receipt. Glossary historical headers do not assert current completion.

Use Chinese plus source English/acronym at the first body occurrence of eligible technical terms, following the core. Subsequent occurrences may use the calibrated Chinese. Preserve Self-Refine, CRITIC, Reflexion, ReAct, Anthropic, OpenAI Agents SDK, LangGraph, Gemini 2.5 Computer Use, GPT-4, Madaan, Gou, NeurIPS, paper identifiers and all other actual source names. Do not invent acronym expansions.

Keep metadata keys Type/Languages/Prerequisites/Time and the Build/Python labels. Faithful natural-language prerequisite descriptions and minutes may be translated. Shared headings follow the ADDENDUM: 学习目标、要解决的问题、核心概念、动手实现、实际使用、交付成果、练习、关键术语、延伸阅读. Do not add absent sections.

Protect every code payload, inline identifier, number, operator, source path and URL, SVG byte and the exact self-refine figure identifier. Only the already permitted reversible text tags may be added later to the two bare fences. The unembedded SVG remains a separately inventoried future byte-identical asset; no new image embed is proposed.

No source fix, automatic retry behavior, universal 2026 claim, structured-output implementation, true full-history consumption, model benchmark result or mathematical convergence guarantee is supplied by a terminology choice. Source caveats remain in SCOPE.md and source-readiness.json. Own3 and every author/review/publication gate remain pending; no checker exception, runtime, model/API call or install is authorized by this file.
