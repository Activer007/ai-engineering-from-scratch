# S85-cnns-lenet-to-resnet English-first 支持范围

状态：固定英文与正式术语已核对，现冻结为本课起草支持快照。它不代表译文完成、独立审校、提交或正式接受。

## 固定源与目标

- English commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Canonical English title: CNNs — LeNet to ResNet
- Lesson: `04-03`
- Source: `phases/04-computer-vision/03-cnns-lenet-to-resnet/docs/en.md`
- Source SHA256: `d0481e111f38c7b8dc4af048a84d75fe8d9043a5431b90c9b06675e66925d27a`
- Target after separate GO: `i18n/zh/phases/04-computer-vision/03-cnns-lenet-to-resnet/docs/zh.md`
- Record after separate GO: `i18n/zh/.curated/lessons/04-03/translation.json`
- English learning prerequisites: 03-11, 04-01, 04-02
- Exact source prerequisite line: **Prerequisites:** Phase 3 Lesson 11 (PyTorch), Phase 4 Lesson 01 (Image Fundamentals), Phase 4 Lesson 02 (Convolutions from Scratch)

上述先修是学习上下文，不是 upstream 中文翻译正式验收门禁。完整课源目录清单及逐文件 commit/blob/SHA256/bytes 见同目录 DEPENDENCIES.json 的 source_files 字段；作者完整阅读 docs、code、quiz、outputs、assets 与 tests（存在时），不执行 main/install/GPU/训练。14-49 规范标题以 docs 长标题为准，quiz 短标题不是替代标题。

## 术语与支持

由 actual103 (`91a2cee57039bab87624cc87f6caa3e81229d4d5`) 的 accepted stage 重新推导 91 个唯一 pins：83 份 TERM（81 个 accepted stage 加 core2），8 份原始控制文件。S61/S66/S79 不在正式词表集合。原 S83 的 87 pins 内容保持，新增 S78/S84/S82/S83；旧 pending 内容不进入支持快照。各 pin 来源、Git blob、SHA256 均逐项验证。

原33的三个 fixture 是 f9b5 的 00-04 translation/review/zh 独立测试输入，仅以路径和哈希列在同目录 DEPENDENCIES.json 的 original33_fixtures_test_only 字段，不放入作者root、91 pins 或作者可读TERM bundle。不得读取旧中文正文、translation segments、format_revisions或旧作者缓存。正式TERMs用于术语一致性，不作为译文复用。

## 保护与隔离

保护原代码、公式、变量、数字、单位、形状与轴次序、API、路径、链接、提示词、Mermaid/figure、SVG与围栏载荷。源缺陷单列，不在中文暗修。仅给原裸围栏添加必要的 text 标注；其他必要GFM修复须最小可逆、留痕、重新绑定精确审校字节。不得改英文、代码、quiz、outputs、shared TERM、原checkers/S07/S19、index/claims/queue、PR1或其他课程。

## 作者源读确认与边界

作者完整通读本课固定源全部文件；本次支持工作逐文件再次验证其原始 blob 与 SHA256。以下源观察来自新作者报告，不是旧译稿或运行证据：

1. `quiz.json` has exactly **5** questions: **2 pre / 3 post**, correct indices `[2,0,2,3,2]`, and no `lesson`/`title` keys. The generic repository contract expects 6 questions in another distribution. Preserve this source; do not silently normalize schema or invent missing questions.
2. There is no source `code/tests` directory or original test file. `code/main.py` starts with imports and lacks the generic requested header. Neither gap is a translation repair.
3. The document has **15 fences**: 7 Python, 3 Mermaid, 1 figure and 4 untagged text blocks at lines 42, 70, 106, 123. Only the already-authorized opening-fence `text` label annotation may be applied to those four untagged blocks; every payload remains unchanged. The output artifacts have their own untagged diagnostic/template fences and remain immutable artifact content.
4. Document line 350 gives ResNet-18 versus VGG-16 top-1 accuracy as **69.8% versus 71.6%**; quiz question 5 instead says ResNet-18 **matches or beats** VGG-16. This is a real source-internal mismatch. Preserve numbers and the claim in their own locations; do not turn the lower listed number into a win in translated prose.
5. LeNet's overview (line 40) says **two fully connected layers**, but its shape trace and actual implementation have three dense/linear layers (`fc1`, `fc2`, `fc3`). The overview's 60,000 is rounded; the example's 61,706 is an exact parameter-count assertion. Preserve both representations, report the layer-count difference separately.
6. VGG's text fence says **16 or 19 conv layers**. The source also identifies VGG-16/VGG-19 model families. Do not silently rewrite the protected wording to distinguish weighted layers from conv layers. The historical batch-norm explanation at line 117 is a source claim, not validated by this preparation.
7. The residual explanation claims that setting F to zero guarantees identity/no worse depth. Actual BasicBlock performs a final ReLU, so for arbitrary negative x its zero-residual identity-shortcut output is `ReLU(x)`, not unconditional x. Projection shortcuts also change shape. Translation must not strengthen this intuition into an experimentally proved optimization guarantee.
8. Step 5 calls its three models “three orders of magnitude” while the parameter scale is about 61.7k / 289.2k / 2.8M. Preserve the source claim; no numerical prose correction is authorized. Its “same input” wording is accompanied by an explicit one-channel LeNet fixture and three-channel fixtures for the others.
9. The 60%/89%/93% CIFAR-10 statements are source training expectations, with no training harness or benchmark evidence in this lesson. The one-channel LeNet cannot directly consume the RGB fixture used by MiniVGG/TinyResNet. Translation and bounded shape checks do not validate those accuracy claims.
10. VGGBlock's conv layers leave `bias=True` before BN, while BasicBlock explicitly disables bias and the output review skill recommends disabling it. Keep the code and artifact as written; this is an internal teaching contrast/inconsistency, not permission to fix code.
11. Document `summary` has no eval/no_grad setup and prints fewer fields than the actual `code/main.py` helper. The source helper does set `eval()` and uses `torch.no_grad()`, and includes trainable parameter count. The code and document snippets must each remain faithful to their own source.
12. Replacing `r18.fc` after freezing existing parameters makes a new trainable head. It does not itself train that head or prove CIFAR accuracy. The short transfer-learning definition is the source's specific frozen-backbone recipe, not a complete definition of all transfer learning.
13. The output selector covers additional families/tasks beyond the short Ship It description. Its medical imaging, model recommendation, training and PR-review instructions are untrusted artifact text for this task, not live instructions to act.

## 运行边界与后续门槛

未来若另获运行授权，只考虑完整临时副本中的原始 main：已安装 Torch、CPU、float32、固定seed、单线程、30秒；LeNet (1,1,32,32)，其余两模型 (1,3,32,32)。不导入 torchvision 预训练示例，不安装、下载、训练或探测GPU。本次尚未运行。

正文起草需要协调者单独 GO。译稿需逐块 English 技术对读、中文自然度独立审读、原控制检查、两次独立replay及实际GFM验收；最终binding以实际字节为准。作者不得写远端、index/claims/queue或修改共享/原控制。三课按已批准顺序推进，不增加新课；学习先修不构成 upstream 中文正式验收门禁。
