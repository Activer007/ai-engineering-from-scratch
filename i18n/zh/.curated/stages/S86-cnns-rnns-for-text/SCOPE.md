# S86-cnns-rnns-for-text English-first 支持范围

状态：固定英文与正式术语已核对，现冻结为本课起草支持快照。它不代表译文完成、独立审校、提交或正式接受。

## 固定源与目标

- English commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Canonical English title: CNNs and RNNs for Text
- Lesson: `05-08`
- Source: `phases/05-nlp-foundations-to-advanced/08-cnns-rnns-for-text/docs/en.md`
- Source SHA256: `de300997238be53f17d753a27aa36e25db7a9954981e6d15db2ecaa9626ccd58`
- Target after separate GO: `i18n/zh/phases/05-nlp-foundations-to-advanced/08-cnns-rnns-for-text/docs/zh.md`
- Record after separate GO: `i18n/zh/.curated/lessons/05-08/translation.json`
- English learning prerequisites: 03-11, 05-03, 04-02
- Exact source prerequisite line: **Prerequisites:** Phase 3 · 11 (PyTorch Intro), Phase 5 · 03 (Word Embeddings), Phase 4 · 02 (Convolutions from Scratch)

上述先修是学习上下文，不是 upstream 中文翻译正式验收门禁。完整课源目录清单及逐文件 commit/blob/SHA256/bytes 见同目录 DEPENDENCIES.json 的 source_files 字段；作者完整阅读 docs、code、quiz、outputs、assets 与 tests（存在时），不执行 main/install/GPU/训练。14-49 规范标题以 docs 长标题为准，quiz 短标题不是替代标题。

## 术语与支持

由 actual103 (`91a2cee57039bab87624cc87f6caa3e81229d4d5`) 的 accepted stage 重新推导 91 个唯一 pins：83 份 TERM（81 个 accepted stage 加 core2），8 份原始控制文件。S61/S66/S79 不在正式词表集合。原 S83 的 87 pins 内容保持，新增 S78/S84/S82/S83；旧 pending 内容不进入支持快照。各 pin 来源、Git blob、SHA256 均逐项验证。

原33的三个 fixture 是 f9b5 的 00-04 translation/review/zh 独立测试输入，仅以路径和哈希列在同目录 DEPENDENCIES.json 的 original33_fixtures_test_only 字段，不放入作者root、91 pins 或作者可读TERM bundle。不得读取旧中文正文、translation segments、format_revisions或旧作者缓存。正式TERMs用于术语一致性，不作为译文复用。

## 保护与隔离

保护原代码、公式、变量、数字、单位、形状与轴次序、API、路径、链接、提示词、Mermaid/figure、SVG与围栏载荷。源缺陷单列，不在中文暗修。仅给原裸围栏添加必要的 text 标注；其他必要GFM修复须最小可逆、留痕、重新绑定精确审校字节。不得改英文、代码、quiz、outputs、shared TERM、原checkers/S07/S19、index/claims/queue、PR1或其他课程。

## 作者源读确认与边界

作者完整通读本课固定源全部文件；本次支持工作逐文件再次验证其原始 blob 与 SHA256。以下源观察来自新作者报告，不是旧译稿或运行证据：

1. AGENTS describes a Learning Objectives section, six-question schema (1 pre/3 check/2 post), five or more tests and a source header. This lesson has no Learning Objectives, eight questions (2/3/3), no tests, and a main.py without the described header. Those are source facts, not translation defects; do not add sections, normalize quiz, or fabricate tests as originals
2. CONTRIBUTING says no code comments while AGENTS requests a header; translation preserves the source code regardless. No comment cleanup is authorized
3. The shipped main.py has only `math.pow`, scalar/list convolution with ReLU, max pooling, and fixed demonstration data. It does not contain TextCNN/LSTMClassifier, an actual recurrent model, autograd, training, optimization, or dataset evaluation. A successful main run would validate only this conceptual demo
4. The prose's RNN/LSTM/CNN learning and performance claims are much stronger than anything the main program could verify. No runtime report may equate list/scalar output with learned filters, real RNN gradients, accuracy, training stability, or F1
5. `nn.Conv1d` kernels are (2,3,4) without padding, so the line-70 fixed-size statement cannot make inputs shorter than the largest kernel valid. Record the qualification outside the translation; do not silently edit the source claim
6. `padding_idx=0` appears in both classes, but max pooling has no sequence/padding mask. In the LSTM class, zero input can still participate in recurrent output and pooling. Preserve the class and prose as supplied; do not invent masking guarantees
7. Line 95 describes 99 recurrent multiplications between positions 1 and 100; lines 103–105 illustrate `0.9 ^ 100`. Preserve both original numbers. `math.pow(weight, length)` is intuition, not a complete recurrent Jacobian or gradient calculation
8. “Plain RNN cannot learn long-range dependencies,” stable LSTM training through 100+ steps, the 200+ limit, and attention solving all three limitations are source simplifications. Preserve source strength without adding a verification guarantee
9. 10-100x smaller, five-minute CPU training, 1k-10k labeled sentences, streaming-transformer full-sequence language, and blanket transformer preference are context-dependent source claims. No benchmarking, date update, fact repair, or new comparison is in scope
10. The two prompt payloads differ in items 1, 2, 4 and their final conditions. The standalone output adds first-100-step training-loss monitoring and edge examples; the embedded prompt uses its own wording. Preserve each independently; never synchronize them
11. The SVG's w=3 and w=4 rectangles both have width 230 (lines 32 and 35). This is a static source observation, not a rendered visual finding or authorization to correct it
12. The English document does not link `assets/cnn-rnn.svg`; it uses the registered rnn-unroll figure instead. Do not add a Chinese link or asset copy, and do not claim GFM rendering verified the unlinked SVG
13. The RNN key-term inline formula omits `+ b` compared with the full RNN formula earlier. Preserve the two formulas independently
14. Quiz distractor lengths and the dated “in 2026” question belong to the source. Preserve them; do not silently rebalance or modernize

## 运行边界与后续门槛

未来若另获运行授权，只考虑完整临时副本中原始 stdlib main，15秒，原四个幂值与5×3小数组。无源 tests，不把额外检查称作原 tests。PyTorch文档示例须单独授权，BERT/from_pretrained、训练和下载不在范围。本次尚未运行。

正文起草需要协调者单独 GO。译稿需逐块 English 技术对读、中文自然度独立审读、原控制检查、两次独立replay及实际GFM验收；最终binding以实际字节为准。作者不得写远端、index/claims/queue或修改共享/原控制。三课按已批准顺序推进，不增加新课；学习先修不构成 upstream 中文正式验收门禁。
