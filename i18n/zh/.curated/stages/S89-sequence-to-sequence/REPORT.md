# S89 / 05-09：序列到序列模型

固定正文提交：0d947156fb142029b7f1e15639aa7ee84d17efec；支持提交：7e67c26e2a7459319a30645374a69ae551bd70f7。原文提交：1bafaa88bb4668356791150bec3a6d7df38387eb。草稿 PR：https://github.com/Activer007/ai-engineering-from-scratch/pull/95。

本封装只追加 review.json 的 actual_GitHub_GFM 与 candidate_single_course_actual108 两个字段，并新增本阶段 TASKS.json、VALIDATION.json、REPORT.md，共四文件。原 review 的 48 个顶层字段、全部值和最终闭括号前的原字节前缀保留；author_self_review、101 块完整双审（51 内容块、50 分隔块）、217 行、源问题和历史运行均未删除或重新嵌套。原 review 305019 字节，新 review 337243 字节。中文、translation.json、三份支持文件及原 source/code/core 均不修改。

reference_glossary_pins 实际为 86 份术语文件；common support 94 项含这 86 份及 8 份原控制/检查器，own support 另有 3 份。不是 91 条规则，也不声称语义通读全部词表。独立远端六文件证据 SHA256 ad475142e670719b84dba616e1bacabe50bbead0df8b16682964efe38a7210e9，含 12 次完整 base64 读取、固定/当时当前分支六文件与新 Git 字节核验；原 5423 文件、60,903,817 字节及 LICENSE 原样保留。正文提交仅在支持父提交上新增本课三文件。

完整技术与中文独审保留作者 12 条及独审 13 条源问题。原文缺 Learning Objectives，quiz 实为 8 题（2/3/3）。main 的固定随机嵌入、衰减 context 与 target/noise 评分不是 GRU 训练或 token 复制准确率；文档演示百分比不冒充实测。figure 载荷 lstm-gates 与未链接 seq2seq.svg 各自保留；正文提示词和输出 artifact 的不同措辞不被同步。默认 CPU BOS、每批每步共享 teacher-forcing 抽样、greedy 同步 all-EOS 停止的局限不被修复或背书。BART 基座模型的指令英译法输出未经验证；未下载权重，未执行 PyTorch、BLEU、训练或练习。源断言按原强度译出，不把绝对表述冒充普适实证。

既有修订保留：b0061 仅补 text 围栏标签，载荷及 closing 不变；b0093 的基座模型（base model）术语修订已完整独立重读。首次 1305 字节部分稿未另存不可变快照，只留同期时间/哈希/大小；后来 12189 字节的首次完整目标快照确实保存，二者不可混称。

历史课程运行仅原 stdlib main 的 5 长度×100 次=500 次瓶颈玩具仿真，退出 0，观察值 89/83/69/53/51。它不是 GRU 复制训练、教材 98/91/62/23% 的测量，亦非本封装新跑的课程测试。原 review 的 site_parser=NOT_PERFORMED 原样保留；新发生的站点解析限制另记于本次 actual108，绝不改写历史。

固定 GitHub GFM 主报告 SHA256 136727c14d346221da9b67991b91fa839fe59998d16a47907bbcedab1d6e19c4，独立像素报告 SHA256 88d435ddc5e9e86e9206b1d79c7a881f423109ee067a33ddc9391508384574e4。36 项捕获清单逐项字节核验，独立复审实看全部 14 个原始 JPEG 文件；初始图与 viewport00 同 SHA，实际 13 个唯一像素状态。101 段记录完整重构目标；8 围栏源载荷相同，DOM 仅去至多一个末尾 LF 后相等；16 标题、22 段落、4 列表、7×3 表全部 21 单元格、17 inline code、4 外链标签/href 核对。仅移除明确 Markdown 语法并折叠空白后全文相等，两个 AX emphasis 范围明确，未宽泛删除星号。

11 个主视口 Y=0/502/1004/1506/2008/2510/3012/3514/4016/4518/4824 连续覆盖正文 348–5500.1875。实图高度 747；滚动后扣顶部 110，独审又加严为顶部 120/底部 737，仍无缝覆盖。以真实逐张像素和跨页内容佐证，不把 DOM 坐标当实看。提示词原生横滚左右同 rect：宽 1639、视口 968，左0、右671、重叠297，覆盖全部长行行尾并恢复0。其余7围栏无水平溢出。

lstm-gates 实际为 fenced literal，article 无图片/iframe，不宣称 SVG 渲染、未新增 asset。长图只作补充：提示词右端被裁、sticky 栏遮练习；主视口和 prompt-right 才补齐。JPEG1165×747 与 CSS1180×757/visual1165×757 差异根因未建立，不宣称已标定的像素变换。初始 symbols AX 与后来 Close no-match 保留，不声称关闭成功；未改图或 DOM。外链落地页未访问。未宣称手机、站点浏览器、所有原生交互、PDF 或 CI 全过。

实际108仅在正式107索引 0a1d387aec90759759d1bbb07bb4cd61c1f114a8（SHA256 7233acb6aeb253ae9812c7bc38a28bdf719d64f0fb4a7d4237eae02c5a20e8c2）上加入05-09；正式107已含14-50。排除旧待验收09-01/10-05/10-06，以及 S88/S91/S92/S93。19 组真实命令和原始日志，执行 2026-10-04T09:57:02.182071+00:00 至 2026-10-04T09:57:17.602016+00:00；run-id 不替代实际时间。原33/S07 24/S19 50全通过；原 strict 直接106，仅保留 S07 b0213 与 S19 b0245 两项既有精确例外，无新增。两个新目录各108篇 Markdown 字节一致，13个 SVG 各两份独立复制，三项仓库审计退出0。前后输入绑定一致，原不可变 Git 输入重读；旧回归不替代本轮。报告 SHA256 f4f1294de1ae3637293ed5a5cf63ab7aa5ee215e4bbef23b22f0005256046e85。

回归进程退出1，all_pass=false。book 本次5/6通过、1失败、0跳过、0预期失败；缺 xelatex.fmt，有自动 mktexfmt 只读失败诊断，没有安装或手工修配置/缓存，没有整本 PDF 通过。原站点解析器虽退出0，仍有10个空中文标题ID、0重复ID，结果 BLOCKED_SOURCE_RENDERER。GitHub 正文可读不等于课程网站通过。封装只读取这次唯一执行的证据，不重跑 runtime/回归。

正文 head 的 statuses 与 PR 触发 workflow 首分页均为空；不是 CI pass，不是未来 final head 检查。当前正式计数仍107，增量0；本地 emit 后原 strict 完整副本检查、final9 读回、final head CI、PR正文读回和单课正式108索引仍 pending，分别需要后续授权。没有未知提交号、不合并、不发布、不推进其他课程。
