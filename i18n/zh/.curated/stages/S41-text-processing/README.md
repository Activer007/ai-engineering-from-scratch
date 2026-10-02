# S41 文本处理：阶段审校证据

2026-10-02 统一终验补记：本课及累计 61 课联合严格检查、两次逐字节重放通过（原 strict 59 课，既有 S07/S19 各一精确适配；没有新增例外）。原回归 33、两适配防护 24/50、仓库数量审计全部通过。快照 61/523 已审草稿、2 课进行中、460 课未开始。下文作者交接时的聚合 pending 已由本补记关闭；最终证据提交后的远端全字节及 CI 查询在 PR 说明与 PR #7 单一索引读回记录，避免自引用提交。final_acceptance=false 专指用户发布/完整网站验收，未合并或发布。

本阶段仅包含 05/01 Text Processing — Tokenization, Stemming, Lemmatization。完整作者技术自查、另遍中文通读、独立全文双审和实际 GitHub GFM 检查已完成，无剩余翻译必改项。聚合重放、最终远端字节读回和 CI 查询待协调者回填；`final_acceptance=false`。这份草案不增加课程完成总数，也不代表网站、移动端、交互图、CI、合并或发布已经通过。

## 固定输入与范围

- 英文基线：`1bafaa88bb4668356791150bec3a6d7df38387eb`
- 英文路径：`phases/05-nlp-foundations-to-advanced/01-text-processing/docs/en.md`
- 英文 SHA256：`d7070af33a9656a02ce6dcf42966d6c8c401035df0f8fa244ec37c12ca4d210b`
- 中文路径：`i18n/zh/phases/05-nlp-foundations-to-advanced/01-text-processing/docs/zh.md`
- 中文 SHA256：`89701f8f92bd19c968fca3273dac02bdd695f64520749dab602aa66362414f2a`
- PR：#47；support commit：`18ae7009527dfdd77f52088e48fbcd7151c2913d`；content commit：`29de4163c7ed6f7ee00653a21fb69e7c8dd5c841`

源文与译文均 257 行，共 119 个无损块、48 个候选块，其中 46 块包含译文，2 块为原样保留的 NLTK、spaCy 专名标题。17 个标题、12 个围栏、2 张表、5 项术语、3 个练习与 3 项参考完整保留。源文没有 Learning Objectives 段，译文未擅自增补。

[公开逐块审核记录](../../lessons/05-01/review.json)绑定全部 119 块的源与目标哈希。[VALIDATION.json](VALIDATION.json)记录本草案的证据与限制；[DEPENDENCIES.json](DEPENDENCIES.json)列出 46 项固定依赖；[TERMINOLOGY.md](TERMINOLOGY.md)记录本阶段术语。

## 翻译与独立审校

作者从固定英文独立新译，完成全文英中技术对照，再单独通读全部中文。另一位作者完成独立全文英中对照，并另次连续通读最终 257 行中文；审核时未读取作者自审报告或作者 translation 记录，未跨改正文。独立结论为 `PASS_TRANSLATION`，公开记录中各严重度的未解决翻译问题均为 0。

译文区分分词、词干提取和词形还原；lemma 统一为“词典原形”，避免与 token（词元）混同；morphology 用“词形学”，POS tagging 用“词性标注”。Porter、WordNet、Penn Treebank、NLTK、spaCy、tokenizers、transformers、en_core_web_sm、全部 API、词项示例、英文论文标题和链接保留。

普通英文数量 three/five 在 8 个块中分别等值译为“三／五”，详见结构化映射；约 `~45` 分钟、版本 `2.x/3.x`、`20` 个测试句等源数值与限定保持。没有新增数值适配规则。

## 保护与机械检查

12 个围栏载荷逐字节不变：9 个 Python 围栏（4 个定义段、3 个 REPL 段、2 个外部库例）、1 个输出文本段、1 个 figure 标识段和 1 个 Markdown 提示词段。b0085 仅将裸围栏标注为 `text`，没有改输出。没有新增 GFM 修复。

作者已运行原 strict、原 33 项回归，并在两个新目录重放出完全一致的冻结 Markdown。独立审明确核过原 strict、全部载荷与 46 项本地文件及固定 Git 对象的哈希。独立初审报告原未单列这些运行，审员于 11:52:40–41 UTC 实际补跑完整原 CLI check、33 项回归及两个全新目录重放并全部通过；这是初审后的真实补验，不冒称发生于原全文审校时。

核心 render 的重放范围是 Markdown。本课没有相对图片链接；源树中另有未引用 SVG，未把它当作本课已加载图片，也未复制或声称其视觉通过。

## 实际执行的范围

作者完整预读固定的 81 行 `code/main.py`（SHA256 `1c3fc4efa436eeb61bb4c1cf9326150bb94d3451765941c03e3a9845991d7ed7`），用外部 30 秒 timeout、`python3 -I -S -B` 原样运行。原句 `The cats were running at 3pm.` 和硬编码演示 POS 标注器未改，进程退出 0：token 为 `The/cats/were/running/at/3/pm/.`，词干为 `the/cat/were/running/at/3/pm/.`，词典原形为 `the/cat/be/run/at/3/pm/.`。此 POS 标注器是演示词表，不是训练完成的语言模型。

作者另运行 b0037、b0049、b0059、b0067 四个原始标准库定义；b0041、b0051、b0061 三段 REPL 共 6 个原例通过。8 组有限核验覆盖原 REPL、ASCII/Unicode 和标点边界、步骤 1a、查表、大小写/POS 回退、默认 NOUN 与演示 POS 的差别、tagger 输出对齐缺失，以及正文定义与 canonical 的有限输入一致性。其中复现了源局限，例如 `this -> thi`、`hopping -> hopp`、`making -> mak`、大写回退差异与 3 个 token 只返回 1 个 lemma。核验通过指行为得到复现，不表示这些输出符合完整语言学规则。

独立审员只在完整预读后执行同课四个标准库定义，以外部 60 秒 timeout 完成 8 项独立有限断言。审员没有运行 canonical、作者 QA、把 REPL 文本作为脚本、外部 NLP 库或大语料基准。作者与审员的运行范围分开计，不宣称“全部教程端到端执行成功”。

NLTK 下载、spaCy 的 `en_core_web_sm` 加载、tokenizers/transformers、语料和模型下载、安装、网络调用均未执行。受保护 Markdown 提示词只是课程文本，没有作为指令执行；三个练习也没有据此声称完成。

## 独立审列出的 8 组源风险

1. 按任务或语言把词、子词、字符粒度直接分类是简化规则，不是普遍定理。
2. 正则主体仅覆盖 ASCII 字母与直撇号，所谓“标点”分支也会产生非 ASCII 字符 token；独立观察到 `café -> caf, é` 和 `don’t -> don, ’, t`。
3. 源称 Porter 步骤 1b 会把 `poni` 修正为 `pony`，但其练习所述 `ed/ing` 处理无法支持这项断言；保留源文，未暗改算法。
4. 查表与后缀回退的大小写处理不同，且没有完整双辅音规则；独立例 `hopping -> hopp`、`jumping -> jump`、`JUMPING -> jumping`。
5. 源将 spaCy morphologizer 列作词形还原选项；精确组件职责需另核，译文保留 API 专名并作词形标注组件释义。
6. 无 tagger 时流水线把所有内容默认标为 NOUN，`running` 因而不还原；中文完整保留这一局限。
7. NLTK 资源和 spaCy 模型是外部依赖，超出本次允许的执行范围；没有下载或执行后的成功证据。
8. 库的速度、准确率、组件替换难易、spaCy 2.x/3.x 缩约示例和“最常见失效原因”等为尚未单独验证的源概括，译文保留原限定。

以上是源风险，不是剩余翻译缺陷。作者另有更细的有限检查边界；本阶段公开汇总沿独立审的 8 组分类，不宣称已证明生产可用或跨版本兼容。

## 亲自完成的 GitHub GFM 检查

2026-10-02，本课作者在自己的 dot 云 Chrome 新标签只读查看[固定内容页面](https://github.com/Activer007/ai-engineering-from-scratch/blob/29de4163c7ed6f7ee00653a21fb69e7c8dd5c841/i18n/zh/phases/05-nlp-foundations-to-advanced/01-text-processing/docs/zh.md)，读取实际 DOM，并查看首屏、两张表、正则与 REPL、核心概念和 figure 占位共五幅截图。未把这次作者浏览归为独立审员的视觉检查。

- 17 个标题（含 NLTK、spaCy 两个专名标题）完整；两表含表头分别为 4×2 和 6×3，全部单元格读取且截图无截断
- 12 个 strong 正确显示；em 为 0、意外强调为 0、正文残留 `**` 为 0
- 12 个 pre 代码块均可读；正则、REPL 输入输出和内联箭头示例保持代码角色；本课没有显示型数学公式
- Mermaid、iframe、图片均为 0；`figure` 的 `edit-distance` 在 GitHub 中实际显示为代码标识占位，未渲染交互图
- 无须修改正文或格式，冻结 SHA256 保持不变

这项通过仅覆盖实际 GitHub Markdown 展示。源码站点 parser 检查仍得到 11 个空 heading ID（`BLOCKED_SOURCE_RENDERER`），不能代替真实站点验收。实际课程网站、移动端、交互 edit-distance 图、CI 与发布均未通过本草案验收。聚合重放、最终远端字节和 CI 查询由协调者继续回填；最终验收保持 `false`。
