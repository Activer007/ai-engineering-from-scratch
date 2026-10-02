# S33 交付报告：从零构建分词器

本课已完成完整作者自查和独立技术、中文双审，无必须修改的翻译问题。协调者已在 dot 云浏览器实际检查指定内容 commit 的 GitHub GFM 和 Mermaid。标准库回退确实丢失 CJK 文本，canonical 运行虽退出 0，却打印 `Round-trip: FAIL`；不得将翻译审校通过或有限核验通过写成生产级、无损分词全部通过。

2026-10-02，聚合验证已完成。本阶段快照 **55/523 已审课程草稿、0课收尾中、468课未开始**；README另计，发布/合并0，实时总数由PR7单一索引维护。用户发布验收未过。

## 来源、范围和版本

- 课程：10/02 Building a Tokenizer from Scratch；唯一显式前置 10/01 已审，只使用固定词表，不借旧中文课文作草稿。
- English commit：`1bafaa88bb4668356791150bec3a6d7df38387eb`。
- English 路径：`phases/10-llms-from-scratch/02-building-a-tokenizer/docs/en.md`。
- English SHA256：`3e2af805d324028b1c673be3bebad6f17dc74ca2ffa0f1f050aa2d5d56d61da1`。
- 中文路径：`i18n/zh/phases/10-llms-from-scratch/02-building-a-tokenizer/docs/zh.md`。
- 中文 SHA256：`a7585d89f9d36d460a61428c8f33a34c222d6858358b87ea72871a1ddf464d7e`。
- 仓库：Activer007/ai-engineering-from-scratch；PR #38。
- content commit：`c9b2dcb245712c67611a3f5a8b770272cc627029`。
- support commit：`18d91e8419e56df8fe0ebf37b8b5ca31dba92be0`。
- 447 行、175 块、73 可译块、23 标题、3 表、3 练习、5 参考。
- 15 围栏：10 Python、1 Mermaid、1 figure、3 原裸围栏仅添加 text 标签。代码、图载荷、公式、数值、特殊 token 拼写、路径和链接均保持。
- 40 项支持与术语依赖逐项绑定固定 commit 和 hash；术语经协调者确认，Unicode/NFKC 使用“规范化”，与数值归一化区分。

本轮未发生新的 GFM 修复，冻结正文未变。上述远端 commit 信息及 GFM 观察由协调者提供，本草案作者未另行浏览或宣称完成最终远端全部字节核验。

## 双审与本地控制

作者完整逐段对照固定 English 与中文，随后另作完整中文通读。独立审员未读取作者自审结论、未改作者工作树，独立完成全部 175 块/73 译块的英中对照和另一次纯中文通读，核对全部 15 围栏、3 表、3 练习和 5 参考，结论为 `PASS_TRANSLATION_WITH_SOURCE_ISSUES`，无必改项。

作者与独立审员分别通过原 strict、原 33 项控制回归及两次输出目录重放。各重放 Markdown 与冻结正文逐字一致。独立审员另核 40 项依赖。逐块 source/target hash 保留在本课记录及独立审证据中；这些检查不代表生产分词器行为、实际课程站点或 CI 已通过。

## 作者运行范围

作者完整预读 `code/main.py` 的 258 行后，用以下受限模式原样运行整个文件：`timeout 30s python3 -I -S -B phases/10-llms-from-scratch/02-building-a-tokenizer/code/main.py`。

`-I -S` 隔离环境路径并禁用 site packages，原来的 `import regex` 失败后进入源码已有的标准库 re 回退；原 `import tiktoken` 也失败，比较演示走源码已有的跳过分支。没有加载第三方代码，没有安装、网络、模型调用、编码文件或外部语料下载。源码算法、原示例语料和 50 次合并设置未改；日志中的安装提示只是源程序输出，没有执行。

canonical 退出码为 0，词表大小为 310，四个特殊 token 的 ID 为 306–309。ASCII、emoji 和示例特殊标记往返可以成功，但输入“你好世界 Hello World”被解码为“ Hello World”，打印 `Round-trip: FAIL`。因此退出成功不能证明无损或生产可用。

作者另完整预读并按顺序执行 8 个正文代码段：b0099、b0103、b0111、b0117、b0125、b0131、b0137、b0143，使用同样的隔离 stdlib 路径；原正文 50 次合并示例保留。8 组有限核验如下，部分核验专门确认源失败边界：

1. 有效多语言字符串的原始 UTF-8 helper 往返及字节数：5、6、4、15。
2. 原 re 回退静默丢弃 CJK 和下划线；`the cat` 首片段没有凭空增加空格。
3. NFKC 将 `ﬁＡ` 变为 `fiA`，与原始字符串不相同；NFD/NFKD 连字行为不同。
4. 非重叠左到右合并及有限 ASCII BPE 训练往返：`abab ab` 为 7 字节、3 token。
5. 最长优先特殊标记匹配；普通用户字面文本中的注册标记也会变成特殊 ID。
6. 规范化先于特殊标记匹配，注册 `Ａ` 后输入被规范化为 `A`，未命中注册 ID。
7. 未知 ID 被静默跳过，无效 UTF-8 字节被替换为替换字符。
8. 重复 train 覆盖已有 pair 到 ID 的映射，同时保留旧词表项。

## 独立运行范围

独立审员完整预读同样的 8 个正文段，以 `python3 -I -S` 运行原标准库回退，没有读取或运行 canonical。作者 canonical 结果不能算作独立审员的运行结果。独立审员的 13 组有限核验为：

1. UTF-8 字节数，包括补充区汉字 U+20000 为 4 字节。
2. 有效 byte helper 往返及无效字节 255 的有损替换。
3. 正则表达式不会凭空增加首部空格。
4. 原回退遗漏 CJK、é 和下划线，emoji 片段仍保留。
5. 原完整正文示例中的 CJK 编码为空，而 ASCII/emoji 示例可往返。
6. NFD 与 NFKD/NFKC 对兼容字符的差异。
7. NFKC 导致原文本往返不再为恒等映射。
8. 注册特殊标记保留其精确固定 ID，正文 BOS/EOS 为 306/307。
9. 重叠特殊标记先匹配最长者。
10. apply_merge 按从左到右、非重叠方式合并。
11. 重复训练分配新 ID 并留下旧词表项。
12. decode 静默跳过未知 ID。
13. 仅核算假定吞吐的耗时：约 173.611 天与 1.736 天；没有速度基准测试。

双方都未加载 regex、tiktoken、transformers；b0153/b0155 未执行，未调用 from_pretrained、模型 API 或交付提示词。未完成与真实 GPT/Llama/Mistral 分词器的生产对比、外部聊天模板验收或外部引用时效核验。

## 14 组独立源风险

以下是独立审员的分组，不与作者的 13 组相加为缺陷总数。所有源事实/代码问题仅记录，正文没有暗修：

1. 生产级与固定五阶段流程的泛化，以及大规模语料/词表断言。
2. 任意字节覆盖能力与本课 Python 字符串/NFKC/UTF-8 接口并不相同。
3. 源声称的 GPT-2 可打印字节映射没有在示例中实现或核实。
4. 汉字不都为 3 字节，用户感知 emoji 不必等同单一码点。
5. ASCII 回退静默丢失 CJK、非 ASCII 字母与下划线。
6. 源的前导空格示例及注释与实际正则结果不符。
7. Llama 各代、SentencePiece 配置及特殊 token 的跨版本概括与内部不一致。
8. 流程图在 BPE 后放特殊 token，而 encode 在 BPE 前拆分；训练、规范化、字面控制标记和重复/空标记还有边界。
9. NFKC 分解/组合定义写反，且规范化不保留原始表示。
10. 重复 BPE 训练可能重分配同一 pair 的 ID；教学接口不包含完整生产能力。
11. 未知 ID 跳过、无效 UTF-8 替换及逐 token 单独显示的解码边界。
12. 速度、词表大小、压缩率和 fertility 的语料/配置依赖；耗时算术不是性能测量。
13. 非 allowlist 外部库、资源、模型下载、练习和引用的未执行范围。
14. 15 围栏保护、3 个裸围栏补 text、特殊标记表及实际渲染边界；weight-tying figure 保留，未重画或验证交互。

## 实际 GFM 与站点边界

协调者在 dot 云浏览器对 immutable content commit `c9b2dcb245712c67611a3f5a8b770272cc627029` 实际观察：23 标题、3 表（含表头分别为 6×3、9×3、9×3）、7 个 strong、0 em、0 未解析粗体。1 幅 Mermaid pipeline 的完整节点已逐一读取并截图。没有新增 GFM 修复，正文 hash 保持不变。此项来源是协调者浏览器观察，本草案作者未声称独立浏览。

离线课程站点 parser 生成 38303 字节 HTML，包含 3 表、13 普通代码块、1 figure、1 Mermaid；15 个中文标题得到空 ID、无重复非空 ID，结果为 `BLOCKED_SOURCE_RENDERER`。这是源 renderer 的已知限制，不等于真实课程站点、移动布局或交互验收通过；GitHub 的 Mermaid 显示通过也不等于 weight-tying figure 交互通过。

## 协调者联合验收与未过门槛

组合 **53课原strict + S07精确符号表例外 + S19精确两行竖线适配**，55课两次输出逐字节一致。原33/S07的24/S19的50控制及523课/67认证课/12评测/505题审计、README/book计数通过。核心只重放Markdown，清单绑定SVG另经hash验证复制到两个输出并参与整体字节比较。

最终证据提交后的远端字节、PR元数据及CI查询记录在PR完成说明和单一索引，避免自引用。完整实际网站/移动/交互、托管CI及用户发布验收均未过；Actions未启用，空状态不是CI成功，没有虚构失败run。仅本fork draft，无merge/部署/上游写入。
