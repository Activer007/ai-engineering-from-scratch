# S107-multilingual-nlp English-first 支持范围

状态：本地check-only own3候选，未安装、未发布，不增加正式课程数。当前独立技术/中文语言PASS只绑定以下版本，不代替支持安装、真实GFM、远端最终字节核验及适用批次回归。

## 固定英文与唯一目标

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Source tree: `3d90647a3449a7b228a6b6025ed2b333ef99e81c`
- Lesson: 05-18
- Canonical docs H1: Multilingual NLP
- Source: `phases/05-nlp-foundations-to-advanced/18-multilingual-nlp/docs/en.md`
- Source Git blob: `97957e66c01d5a86574a0b5c3f29f1b1a652a0ad`
- Source SHA256: `343fc51cb223c67fcf46906beb0ade26c859c437a03196285d44a74e088e720a`
- Target: `i18n/zh/phases/05-nlp-foundations-to-advanced/18-multilingual-nlp/docs/zh.md`
- Eventual record: `i18n/zh/.curated/lessons/05-18/translation.json`
- Original core blocks: 101
- English prerequisite line: **Prerequisites:** Phase 5 · 04 (GloVe, FastText, Subword), Phase 5 · 11 (Machine Translation)
- Actual first write UTC: 2026-10-04T14:07:08.911837+00:00 through 2026-10-04T14:07:08.911996+00:00
- First-write receipt SHA256: `4cdb2a7a275c8fb8b205a81bfb30d70dfc886e5460647ce01a3029642f6253a7`
- Original complete first draft: 15126 bytes, SHA256 `0a7a89e55b12485da7213038a2b385763ce7bb5732bfe5fb9444d1782cbddc56`
- Original translation record: 48548 bytes, SHA256 `c602a9fc01fd967efc7a6e916483ef84aa670c2d6cf2ef401b5c8cc2740d19b3`
- Current reviewed target: 15148 bytes, SHA256 `2a9a4d09f8dbf89703d9f98a0bbb4cc4ba4b22645ea8bba1ceeb820ce556c389`
- Current draft record SHA256: `361089b812fa5c05169f5fceb0cb471b96a1212958a4fc4cb3e182cad63ff503`
- Independent language review SHA256: `6f42b55a0d42e46074da22858cb0e4393df31581a9183a9267525649a6d5047c`
- Existing local strict receipt SHA256: `681b5fe5af5958527f6bf2d3aee6066575a64738a66f20d186c939ad04d30bf0`

首写以原回执和原字节为准，不用mtime重建，不倒推为当时独审或own3已通过。本课源文件见DEPENDENCIES.source_files；先修固定英文已定位，无先修中文formal门禁。

## 真实修订绑定

- Revision 001: 2026-10-04T14:08:55.548054+00:00 through 2026-10-04T14:08:55.548299+00:00; target `0a7a89e55b12485da7213038a2b385763ce7bb5732bfe5fb9444d1782cbddc56` → `2fec8fc3629a4a95c5438261006490eeaf4bff131f1b8be02fa0c063396c5de9`; receipt SHA256 `ded087c548bdad84bbe74b01ce50bd1f1667a4831d5be4e05c58c651886e4497`; diff SHA256 `0f79456e5d171a51d5030d7507a6da12780416179b45d210447e87500264180e`
- Revision 002: 2026-10-04T14:09:55.080928+00:00 through 2026-10-04T14:09:55.081365+00:00; target `2fec8fc3629a4a95c5438261006490eeaf4bff131f1b8be02fa0c063396c5de9` → `2a9a4d09f8dbf89703d9f98a0bbb4cc4ba4b22645ea8bba1ceeb820ce556c389`; receipt SHA256 `8188faa1bc6ebb687bfe2a1a99d61dc7faf1697b129f54f449aa386f05133b7b`; diff SHA256 `ee93a5499f4bdac0c5c3ff92e79e5a1ea23be3f6d0dc62140698835996c49d67`

修订首尾快照及原差异均保留，只用技术事实和hash作公开绑定；不替换首写或初始record，不把后续版本当作首次版本。独立审校针对最终target/record，未要求新的翻译修订。

## 固定支持与当前溯源

共同准备清单SHA256 `aef5293c38284a7c281852d115973b8e1eb24c4b2a4787226bf578714b723e13`。files/support_pins为有记录的公开投影，保留common109原顺序、公共身份与历史role/classification，并非原内部对象逐字段完全相等；去除S97–S102条目的12个私有路径定位值，保留其receipt SHA256。reference_glossary_pins为101 TERM，另8 controls；own3只含本阶段DEPENDENCIES.json、SCOPE.md、TERMINOLOGY.md，总112。正文、record、兄弟阶段及图资产均不算own3。旧已核Git身份复用，不重写历史类别或首写时点。

当前冻结as-of为正式批次结果独立回读真实时间2026-10-04T14:39:28.193462+00:00：正式已审草稿117，INDEX commit `03379392933fa99905d1ba604dfb14c174060eb6`、SHA256 `98f0af00d276f873998de9313e8fd14c8553fc4e27a9dce473dcb1f8358532aa`；独立回读SHA256 `428e243e351cdfc5e8d655b232b779e5d58c41898f1fe9b7d4e0b96463bf53bf`。actual117于2026-10-04T14:25:30.110274+00:00至2026-10-04T14:25:40.159393+00:00真实执行，新覆盖S98/S99/S102，结果SHA256 `382c6ca8bf3cfe5eade9c2d0309848adc319e9c519ffe8ea1d4e649cd275083b`，正式增量0；不覆盖S106/S107/S108。本课所属批次尚未运行，不继承历史PASS。book5/6缺xelatex.fmt、站点空标题ID及CI/移动端/交互/发布等限制保留。

保留record schema_version=1、DEPENDENCIES version=1及原f9 core/S07/S19精确控制。own3 hash由外部manifest固定，无自引用，不新增builder/checker/audit框架或重分类表。原33 fixture只复用既有固定身份，不读取其旧中文正文或执行回归。

## 已有证据与实际限制

- 零样本跨语言迁移指没有目标语言任务训练标签，不是没有多语言预训练文本；源表中的无目标标签评估不能代替测量准确率所需的带标签评估集。few-shot在本课是目标语言监督微调，不是上下文提示示例。
- 共享子词必为同一语素、语义天然对齐、将NLLB与MLM叙述并列均是源概括，未在翻译中改写模型分类或证明普遍成立。
- 100-500例达到英语基线准确率的95-98%是相对比例，不是绝对准确率或百分点；模型覆盖、2026选型和qWALS论述均为未实测的固定源信息。qWALS与LANGRANK（ACL2019）分开；Aya-23的覆盖/能力与所引Aya论文版本须另核。
- 受保护微调示例没有显式展示padding或数据整理器策略，变长批处理未证实可执行；较高学习率必致仅英语、默认超参数普遍安全等断言不作背书。
- fertility为平均每词token数，script为文字系统，Unicode normalization为文本规范化。3-5x、变体失败、容量被挤占和不能靠更多数据补救均未实测；字节级回退/OOV覆盖不自动保证更少token或更强语言能力。
- main只对11种语言的word_order/script/family作三特征相等性比较和合成评分；不是qWALS或LANGRANK复现，不是分类性能测量。min(0.95,0.45+0.45*sim)在sim≤1时最多0.90；排名排除目标自身并保持同分输入次序。
- 文档示例需要预训练下载及transformers/sentence_transformers/datasets，并包含Trainer微调；这些库不在仓库允许依赖内，未安装或执行。没有code/tests；源quiz8题（2pre/3check/3post），且docs缺Learning Objectives，未暗补。
- 实际相对链接SVG与固定源字节一致，单列为正文资产，不属于own3或common109；图中英文/印地语及数量主张原样。n5-crosslingual-bridge另为自定义figure；均未进行真实页面可读性验收。
- 有限CPU提案只在另获GO后最多5秒提取LANGUAGE_FEATURES及三个纯函数的狭窄AST子集，检查对称性、范围、自排除、同分顺序与合成公式；本轮AST实验/main/tests均NOT_RUN，不触发模型、下载、微调、安装、GPU或输出文件。

## 核验与发布边界

本准备仅核新候选JSON/字节/hash、当前作者/首写/真实修订绑定、本三课17个源文件及6个先修英文的既有身份与当前字节；复用101 TERM校准及已核common身份，不重新解析所有历史commit:path。S85–S96历史commit:path在原准备对象库缺失的限制保留，未fetch、未补造。固定源准备清单SHA256 `366f8db5752f3a40784a05d22380aa212096e5dd164c2b40d11f6e97286a1a66`。

没有全源扫描、课程执行/import、main/tests/CPU实验/模型/训练/GPU、安装/下载、实际GFM/site/mobile/PDF/CI或全库回归。只生成候选，不写作者、英文源、原支持、INDEX、queue或远端。publication pending/null是冻结时点的状态；后续发布须另有真实commit及独立完整字节回读。语言PASS和静态核对不代表本课已正式登记、运行或批次通过。
