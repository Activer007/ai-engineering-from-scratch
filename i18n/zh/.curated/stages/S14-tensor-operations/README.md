# S14 交付报告：张量操作

2026-10-02。只做01/12；01/11 SVD已试点完成，没有重译。阶段完成快照为 **36/523 已审课程草稿，2课并行进行，485课尚未开始**（剩余未审487），README另计，发布/合并均为0。实时进度以 PR #7 的 [单一索引](https://github.com/Activer007/ai-engineering-from-scratch/blob/zh/stage-01-tool-foundations/i18n/zh/.curated/ROLLOUT-INDEX.json) 为准。

## 新译与双审

源固定 `1bafaa88bb4668356791150bec3a6d7df38387eb`，EN-first，不读旧中文/cache/历史机器翻译稿。源 SHA-256：`98beea9409bda9831f924611911ce5218d012444740a5a8a800f9c7823aaf632`；最终中文：`0e2ef0704cfd6cdebdc170d697b361314c1f5490df0903b0e90f488c795c7b82`。

作者之外完成344行/163块/67候选全文技术对照，再完整纯中文通读，0项必修。逐块hash和两次覆盖记录完整。15围栏载荷原样，唯一裸围栏仅补text；形状、轴、数值/API、公式/图/链接保护。术语重点区分张量阶/矩阵秩、步幅单位、视图/副本、归约/降维、einsum缩并和注意力头的轴语义。

## 真实 GFM

dot云端Chrome查看 [不可变正文提交](https://github.com/Activer007/ai-engineering-from-scratch/blob/8971baa40aa50ba94ce1f29ada63083cc1d79673/i18n/zh/phases/01-math-foundations/12-tensor-operations/docs/zh.md)，确认25标题、3表（各3列，含表头7/7/11行）、16 strong、0意外em、中文链接有效。4个Mermaid的阶数/形状、Vision/NLP/Attention/Weights、C/F布局与einsum节点边均实际可读；阶数图缩小一次显露完整B,C,H,W。所有表、提示词路径、einsum表达式与习题标签检查通过，无需新增语法修复。`tensor-broadcast`仅作为代码显示，不代表网站交互验收。

## 有限运行及控制

完整阅读775行canonical后，导入未改模块，仅调用9个安全离线函数，exit0；跳过大数组`demo_ai_tensor_shapes`及main，不声称大内存/性能验证。正文2–7的6个载荷在NumPy和完整canonical Tensor类上下文中运行，exit0；全部9载荷AST通过。第1个是缺方法/导入的类片段，第8个缺K/V/softmax/W_o，第9个需要未安装的PyTorch，均不冒称独立程序可执行。完整canonical注意力演示另已运行。

18个有限数值/形状断言涵盖阶数、步幅、reshape/transpose/permute、sum/squeeze/unsqueeze、逐元素运算、广播、einsum、注意力分数/归一化/加权和及拆头合头。5组边界显示scratch reshape/transpose复制数据而NumPy转置共享、stride按元素/字节不同、二维`transpose(0,1)`为恒等、尾部偏置无需显式unsqueeze，以及scratch接口/正文片段不具备完整框架语义。

本课原strict通过。只读组合 **35课原strict + S07一处精确已审数学符号表例外**；原33控制与S07的24守卫通过，36课两次受控重放逐字节一致。S07旧检查器仍有既有误报，不夸称全部旧strict无例外通过。523课、67认证课/12评测/505题审计、README计数及空白检查通过。

## 未过门槛与并行协调

13项源风险按行定位：内存布局/视图概括、stride单位、广播unsqueeze、表内transpose、attention片段缺上下文、多维K.T、简化归一化、缩并/形状及scratch接口边界等。它们不作为擅改源或代码的理由。只做必要验证，没有扩大研究。

原站解析仍有15个中文空锚点；真实网站/移动端/交互图、PyTorch/GPU、CI和用户发布验收未过。Actions禁用，空workflow/status不是CI成功。只fork draft，未merge、部署或上游写入。

按并行安排，S15只claim01/13数值稳定，S16只claim01/14范数距离，各自隔离工作树独立新译、冻结后互换完整技术与中文审校，不跨改对方正文；主线不重复这两课。术语冲突、实际GFM、远端提交及总索引由单一协调者串行处理。SCOPE/TERMINOLOGY/DEPENDENCIES固定本阶段与20项只读依赖，TASKS/VALIDATION记录hash与门槛；旧阶段账本不被覆盖。
