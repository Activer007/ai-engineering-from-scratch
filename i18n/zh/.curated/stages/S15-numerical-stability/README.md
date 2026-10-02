# S15-numerical-stability 交付报告：数值稳定性

2026-10-02。独立并行作者负责01-13，另一位作者在冻结后完成全文技术对照和独立中文通读；没有把作者自审当成独立审。阶段完成快照为 **37/523 已审课程草稿，3课进行中，483课未开始**，剩余未审486，发布/合并均为0，README另计。实时状态仅在PR7的 [总索引](https://github.com/Activer007/ai-engineering-from-scratch/blob/zh/stage-01-tool-foundations/i18n/zh/.curated/ROLLOUT-INDEX.json) 串行更新。

## 来源、审校与保护

固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`，source SHA-256 `1f803ae9c3db1ab75678a37007833c86479ef7810778c396201e3c5d91e731c6`；target SHA-256 `af30f3c9410de0ba9cec5aaca00b31cd717de19e62792fd9ac963324eb7f2b75`。完整607行/297块/117候选双审通过，必改项0；协调者重算全部独立逐块source/target hash一致。禁止旧中文/cache/历史机器翻译稿复用；32围栏载荷、公式/API/数值/链接/结构保持，仅裸围栏补text。词表增量与21项固定依赖已核验，不覆盖旧表。

## 实际 GFM

在dot云端Chrome查看 [固定内容提交](https://github.com/Activer007/ai-engineering-from-scratch/blob/60096e817e204bed7f50b05fe330ca677ff99c92/i18n/zh/phases/01-math-foundations/13-numerical-stability/docs/zh.md)，DOM与截图核验31标题、1完整表、18 strong、0意外em；中文链接、公式/单位及全部表格可读，无需新增语法修复。原figure只显示代码标识符，不代表网站交互验收。

单张表为3列、含表头16行。重点查看IEEE位字段与dtype范围、机器epsilon练习的源等号方向、softmax/log-sum-exp、梯度裁剪、全部5练习和术语表。并行术语对齐将batch normalization统一为“批量归一化”，该修改在冻结和独立双审之前完成。

## 有限执行与来源边界

作者完整读719行canonical后，离线执行14个标准库教学演示，exit0；故意错误梯度例子会打印FAIL，这是预期教学输出，不是所有梯度都正确的证明。作者与独立审校者分别执行9个原Python片段，明确检测片段需x=1.0及按序共享定义，不声称每段独立可运行。10个有限断言覆盖稳定softmax/log-sum-exp/CE、梯度、裁剪和Welford方差。

16组独立源风险单列：IEEE/有效数与次正规数、float32与Python float差别、上溢/下溢阈值、Python异常和NaN/Inf、epsilon练习、稳定式边界、梯度检查、AMP/bfloat16转换、LayerNorm式子与RMS概括等。源canonical在极大共同偏移上的CE消去与正文更稳定版本有差别；没有擅改源码。原站parser有18个空中文锚点和重复nan-inf。

## 组合验证与未过门槛

本课原strict通过；组合 **36课原strict + S07一处精确已审符号表例外**，原33项控制与S07的24项守卫通过，37课两次重放逐字节一致。S07原检查器仍保留既有误报，不说全部旧strict无例外通过。523课及67认证课/12评测/505题审计、README计数、源/代码/控制未改与空白检查均通过。

真实网站/移动端/交互图、完整框架/GPU性能、CI和用户发布验收仍未过；Actions禁用，空workflow/status不是CI成功。无依赖安装、数据/模型下载或外部模型API。仅本fork draft，不merge/部署/上游写入；源问题只有限定位，不扩展为额外纠错研究。

## 并行衔接

S15/S16本轮各自新译并互审，单一协调者负责术语冲突、GFM、远端与索引。后续排他claim为S17=01/15统计、S18=01/16采样，继续各自独立作者与冻结互审；不得把进行中的课提前计入完成数。SCOPE/TERMINOLOGY/DEPENDENCIES、TASKS/VALIDATION和本课逐块审读共同绑定交付，不复制覆盖旧阶段台账。
