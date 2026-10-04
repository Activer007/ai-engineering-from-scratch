# 卷积神经网络：从 LeNet 到 ResNet：翻译与验证报告

[自有 fork 草稿 PR #91](https://github.com/Activer007/ai-engineering-from-scratch/pull/91)；[固定中文正文](https://github.com/Activer007/ai-engineering-from-scratch/blob/1a364d8283c864eccac467bb32a850a0d0779eef/i18n/zh/phases/04-computer-vision/03-cnns-lenet-to-resnet/docs/zh.md)。

固定英文源：1bafaa88bb4668356791150bec3a6d7df38387eb
中文 SHA256：89965d5854263f138c8cbde8e17b48369cd5df4f8833c3a8880e2ebc3f004f3d
正文 commit：1a364d8283c864eccac467bb32a850a0d0779eef
正文直接 parent：61fe6c0c99760c04d503ccfa207440088d1b4d79
支持 commit：d67680e64746efb697d508df50fa37f1c3a12d7f
历史 review SHA256：825f7fc40983ba7d8bdf84199838fa1a0ce8614d9040da12b68d136774298774（485262 bytes）
本候选 review SHA256：aa8320a25b5c0b7020d80aa78d927715130d52b6d7ccb409d84b99c8648c9ea9（528889 bytes）
新 GFM 报告 SHA256：4400e4377fc8481ca7a9d7057e14ae26c1c9cebd5757f394bee800ed120594a4
独立像素复审 SHA256：43183002e95245482aeb601a066a559eac9114945ef24122101f9b230d1f40d2
本课实际单课106回归 SHA256：746a39b9a76b3e54a5b07ddf1480936b83de3b956d70232d1f1f32f532b4a629
实际报告窗口：2026-10-04T06:53:43.437604+00:00 至 2026-10-04T06:53:56.994864+00:00
19组命令实际窗口：2026-10-04T06:53:43.438511+00:00 至 2026-10-04T06:53:52.837887+00:00
正式105索引 SHA256：7018901024e464b56ccd36f26e2098c7c346ab498b7c1fd8418938a5d461931e
本地封装时间：2026-10-04T07:24:26.763626+00:00

完整作者及独立技术对照、中文通读保留：161 块中包含 23 标题、35 段落、6 列表、1 引言、1 表格、15 保护围栏及80分隔块；5份课程源文件共737行，正文393行。旧 review 的全部字段、历史日期、historical_base_review、format_only_revision、historical_gfm_before_format_revision 原样保留；仅追加新目标 GFM 与本课实际回归摘要。没有再嵌套一份整 review 或索引。99项保护绑定不变；旧reference_glossary_pins字段实际91条，其中83份术语/增补文件、8份原控制与检查器文件，不能将91条全称术语；support dependency另为91项。5423份原source和三份support不变。

第75行、04-03:b0047 的唯一正文修订，是在三个原有星号前各插入一个 ASCII 反斜杠；160个其他块、15围栏payload、80分隔块不动。已经独立完整重读英文和新旧中文、逐块复核并另跑strict及两个新目录重放。旧英文与旧中文 GFM 都曾将算式渲染为 29C^2 = 18C^2 vs 25*C^2；这个失败及旧行号勘误完整保留。新中文实际像素与DOM均完整显示 2*9*C^2 = 18C^2 vs 25*C^2，三乘号均在，无多余反斜杠、无强调吞号。本轮没有重新截取英文页面，不能把旧source证据写成新英文验收。

修订后独立复审实看全部27张新JPEG，校验主清单61项，18张重叠视口覆盖全文，三张默认Mermaid图均完整可读。timeline四年份、家族和说明，Inception 7节点9边，residual 5节点5边均可辨；浅色背景上的timeline白字偏弱且小，不是正式对比度认证。新head原生timeline一次Zoom out仍裁掉标题上沿，Reset后标题完全位于iframe上方；本轮未重测Pan，不冒称全交互通过。pooling在GFM仍为literal代码。长图含空白Mermaid区域和穿过术语表的sticky栏，不能单独证明图表完整。视口JPEG1165×747，CSS inner1180×757、visual1165×757，差异原因未建立；保守覆盖无空档且超过正文底边。

原环境没有Torch。source_main及补充特征验证在依赖预检即SKIP，没有导入Torch、实例化模型、训练、GPU探测、下载或安装；课程也没有原测试目录。LeNet5 61,706、MiniVGG 289,194、TinyResNet 2,797,610是依据固定模块声明的静态整数推导，零残差负输入仍经过ReLU也是静态代数，不是runtime pass。原教材中的两层全连接叙述与三层实现、VGG层数/BN历史说法、无条件恒等直觉、三个数量级、CIFAR准确率预期及69.8%/71.6%与quiz表述差异均未静默修正，不背书为新实验证据。

实际回归严格为已正式验收105课加且仅加04-03，共106；S87和S86已经是正式基线的一部分，其旧实际104/105不能替代本课实际106。原strict直接104课，只保留S07/S19两项既有精确边界，不增例外。原33/S07 24/S19 50控制、两个全新目录各106篇Markdown字节相等、13个SVG各两份独立复制及3项仓库审计的真实结果见VALIDATION。S61/S66/S79仍排除，本地封装不增正式计数。

本课原站点解析器仍有12个空标题ID，进程退出0不等于站点通过。book本次实际观察：5/6通过、1失败、0跳过、0预期失败；xelatex.fmt缺失=true，自动mktexfmt诊断=true。这些字段来自本课新实际日志，不沿用旧课结果；未安装、修配置或宣称整本PDF通过。

当前正文head的原始带args查询返回statuses[]与workflow_runs[]；workflow接口只有PR触发首分页，不能推断全库没有运行。这不等于CI通过，也不是未来finalhead检查。四文件只为本地证据候选；最终9文件读回、finalhead CI、PR正文与正式单课索引另行闭环。正式计数仍105，不合并、不发布课程、不向上游提交。
