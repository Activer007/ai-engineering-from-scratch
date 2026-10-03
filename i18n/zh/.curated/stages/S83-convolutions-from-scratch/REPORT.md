# 从零实现卷积：翻译与验证报告

[自有fork草稿PR #90](https://github.com/Activer007/ai-engineering-from-scratch/pull/90)；[固定中文正文](https://github.com/Activer007/ai-engineering-from-scratch/blob/7cd003da0acc4f7fc8392f15df4607198b664079/i18n/zh/phases/04-computer-vision/02-convolutions-from-scratch/docs/zh.md)。

固定英文源：1bafaa88bb4668356791150bec3a6d7df38387eb
中文SHA256：661d3a05d390f6b85ccbbeb20482f0027e2f6905fb2d9f149d090337948591ad
正文commit：7cd003da0acc4f7fc8392f15df4607198b664079
支持commit：868cbcbf36f31caa9ed52ac6ea514fddb9122b8a
原review SHA256：6950d21aa9ac07a2c8788dcc605b4235b38ae730a487b31d03a57eebd7e4cbc2
本候选review SHA256：c6ca7c12681d90599fdfbdc94d39ea62e6f961e2a01e9d83cb7eea6d574b5256
真实GFM报告SHA256：64627a7befd249d4b482b23d8811306c3b01723af9addfef7b53f3a5b75c9f9d
新单课累计回归SHA256：8ed3b826f4ac6084a9a50e25d212e14b4acf6605ecffac4cbb9007fcd2638352

作者与独立审校者各完成163块技术对照和单独中文通读，82个内容块、81个分隔块，逐块SHA与具体意见完整保留。87项冻结依赖、79项历史术语绑定和3份原33测试fixture未变，没有回填S78。target、record、source与3份support字节不变；review只追加两个新证据字段。

作者13项、独审14组补充验证仅覆盖原小尺寸NumPy CPU示例。原main只打印，exit0不等于断言测试；原课没有code/tests。没有执行文档8×3×224×224样例、GPU、训练、大型im2col或prompt输出。源问题包括floor遗漏、stride/padding/平移等变性的限定、naive固定float32与im2col dtype差异、Sobel实际非零列7/8/15、im2col测验乘法方向、输出感受野表应3/5/7、adaptive pool范围与参数计数限定。所有保护源码、公式、Mermaid、quiz与outputs原样保留，完整风险清单见review和VALIDATION。

历史独审有一次导入产生非源.pyc，原文件保留且hash锁定，并从全部发布白名单排除。不能声称整个作者目录从未变化；本构建器没有写作者目录。

真实固定commit GitHub GFM与独立像素审阅：23标题、17保护payload、2表、10强调、1斜体、44行内代码及4阅读链接。21个原JPEG/JFIF文件中20个验收，20-diagram2为过渡帧明确排除；21为第二图settled原生展开态。第二图inline下排裁切及控件覆盖是已披露限制，原生展开显示7节点6边；第一图3组3节点2边。没有改源码、DOM或CSS。02单行粘性工具栏过渡由相邻帧文字重叠补证，不能仅凭统一顶栏几何假设。像素1165×747与CSS1180×757分开；外部链接目的地、交互图、部署站和移动端未验收。

本次候选严格为正式102课加本课，合计103；原strict直接101课，S07/S19仅保留两处原精确适配，没有新例外。实际33/24/50控制、两个全新目录各103篇逐字节重放、13个SVG各两份独立复制及3项仓库审计通过。S61/S66/S79不纳入，本报告不增加正式计数。

课程站原解析器仍有16个空标题ID；14个普通代码块、1个figure、2个Mermaid源码和2个表已解析；不等于实际站点通过。正文head status/workflow真实查询均为空，不等于CI通过，也不代表未来finalhead已检查。book 实际重测5/6；xelatex.fmt缺失阻塞PDF；没有安装或配置修复。

这是仅4文件本地证据候选：review追加两字段，TASKS/VALIDATION/REPORT新增。最终9文件不可变/当前分支/Git读回、finalhead CI、最终PR正文与正式单课索引仍待协调者完成。不合并、不发布课程、不向上游提交。
