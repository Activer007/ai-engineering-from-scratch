# S121-real-time-edge English-first 支持范围

状态：本地 own3 候选，未安装、未发布、不增加正式课程数；S117 TERM 一次固定身份 overlay 已应用。

## 固定英文、作者字节与真实历史

- Source commit: 1bafaa88bb4668356791150bec3a6d7df38387eb
- Source tree: 3d90647a3449a7b228a6b6025ed2b333ef99e81c
- Lesson: 04-15
- Canonical H1: Real-Time Vision — Edge Deployment
- Source: phases/04-computer-vision/15-real-time-edge/docs/en.md
- Source blob: 8156e6d0f62bb0858833d2b96bf869d059443dcf
- Source SHA256: 67456ce0e428e1ffa31eacece531fc95a2eec306f375a994f21571109e76642e
- Target: i18n/zh/phases/04-computer-vision/15-real-time-edge/docs/zh.md
- Record: i18n/zh/.curated/lessons/04-15/translation.json
- Original core blocks: 125
- English prerequisites: **Prerequisites:** Phase 4 Lesson 04 (Image Classification), Phase 10 Lesson 11 (Quantization)
- Prewrite UTC: 2026-10-04T19:38:22.141087+00:00
- First target write before UTC: 2026-10-04T19:39:36.199704+00:00
- First complete target UTC: 2026-10-04T19:39:36.200272+00:00
- First draft: 14191 B / SHA256 b00fb85961b481350eb08a18b0f12ae8ebcd94fd046954c305c219000ead921b
- First-body record: 58109 B / SHA256 89d08ffe43a5c3f25ee213ae61e0bed91941b0a3957c33a8c98985b8803897f0
- Current target: 14194 B / SHA256 cabf2a70175b563d4519dfc9f7ea9965daaa99b234d8bf3c62cd144a84393a08
- Current record: 58112 B / SHA256 77765e30bcd9e00560be89874b6fcc7c311bf26e34384f60d5f96ce347cf7712
- Original HANDOFF SHA256: 2b80126b85520c9dea8eea27564a60df7b2385fd4dd8b1b7ae829a293f10aa77
- First-write evidence SHA256: c16497f96699fa712871a77f222445534ac972d7fae1760c34c8f3ae38b948fe
- Existing exact-current original strict stdout SHA256: dd750655d3587ab4c5c6619fe455f0938bb7ba0038bbb7a56f9935109c9d20f3

Prewrite 2026-10-04T19:38:22.141087+00:00; first body write 2026-10-04T19:39:36.199704+00:00 to 2026-10-04T19:39:36.200272+00:00. Original full review requested one S2 at b0043 and remains bound to original first body/record. Actual R01 at 2026-10-04T19:59:49.139915+00:00 to 2026-10-04T19:59:49.140312+00:00 changes only 计算量 to 计算开销 in one INT8 paragraph;124 blocks unchanged. Incremental independent PASS completed 2026-10-04T20:02:37.490Z; original review/handoff/self-review/strict not rebound.

首稿body/record原样冻结，R01只有一处技术词组与对应record段+target hash变更；真实前后全文、diff、时间、旧S2和增量闭环全部保留。

- R01: before UTC 2026-10-04T19:59:49.139915+00:00, after/event UTC 2026-10-04T19:59:49.140312+00:00; body b00fb85961b481350eb08a18b0f12ae8ebcd94fd046954c305c219000ead921b → cabf2a70175b563d4519dfc9f7ea9965daaa99b234d8bf3c62cd144a84393a08; record 89d08ffe43a5c3f25ee213ae61e0bed91941b0a3957c33a8c98985b8803897f0 → 77765e30bcd9e00560be89874b6fcc7c311bf26e34384f60d5f96ce347cf7712; receipt SHA256 8cd6decd8163afff6d5b90682e269db075dd94297349c8b7bb4ef686b269bab0; body diff SHA256 1149152d21b364af311b7bd39e65476df77d7fd31af1bb0867a51ced5ab9a99c; record diff SHA256 9e21634a6903b3691548b6d49192f1aea3e5affccfab41d704cd2de30d64c004

原完整125块英中对照及另次中文通读报告SHA256 908fbedea1693f6127f5f72c122be561c1f035cbf2bbbabce33d57a2ec4df13b、配套SHA256 39bf4995d7015eba6136d5c150a460650feee724848ccfef5f7b93f04068ca8e保持REQUEST_CHANGES_ONE_S2并绑定原稿。R01独立增量PASS报告SHA256 6170a40fd7452e7b7985fbf71b40abec967d355c1c2fffa6dbed453ce257b8be、配套SHA256 cc98e6a01cdc10a606946c80de297a2052d617b0a9e4dd9658407dd211f5cbe6闭合唯一S2，覆盖当前b0043及上下文；其余124块沿原完整审校。当前PASS不冒称重跑了整课全文审，全部15项原独审源边界保持。

原作者HANDOFF的待独审、formal131/actual129等为当时事实，原文件与所有首稿/修订/技术自审/中文自审保留，不倒填时间、不重绑旧审。相同字节快照不算新修订；未保存的diff/独立时间为null。

## 固定支持与候选术语overlay

原common127清单SHA256 ee9a55ea831a59135dda08ec77aed08f1bddc09f9b4375727427c510f61e73ac。files/support_pins保留127条、reference_glossary_pins保留119条原顺序及role/classification；仅下述S117 TERM固定身份作一次已核更正，其他身份不变。只删除48个私有locator值，receipt哈希仍保留。own3仅DEPENDENCIES/SCOPE/TERMINOLOGY，未来总130；正文/record/SVG不计入。S122唯一原SVG按固定源字节保护，其他两课无相对SVG。

已知S117工程verification gate术语由旧commit 89dd04954fa5fa6488bdcdbf33374526b7db7174、SHA256 0dcac84df319efb76a023bd986d43e4e6663af305d8dd792e8c98dc41a1d3b5b更正为真实commit ff4d56e72126e854321b5d95a7c43a8b57a485bf、SHA256 6631ae3d6b514d374a63bd21afa98eaedeb995e2aeed3e664e037e6de6ea0c85（3154 B，blob ba0f7c5096125388b0d1889df573b525cbcfc3b7），独立远端回执SHA256 936a39b19be99d9aad56d847bacac431ab240db04725c34ebea3a8e41253ca91。本轮已在3课本地候选DEP的files/support_pins/reference_glossary_pins应用这一真实固定pin，并更新support_set_sha256；原9份候选与manifest已完整留存为更正前快照。未来公共record按本次校准候选库存重绑，同时完整保留作者冻结common127及其历史，不将新pin倒填进旧审校。原作者稿、record、shared文件和旧common清单不改；角色分类和计数也不重分。

冻结已独核formal132：INDEX commit d4220b50bc6002d23a1fff1065a5374a9c5fff76、SHA256 e16f410a4f392a152a66137cb246cefacb9990afae64350cff15f63b2002d693，回执SHA256 eeff8c73b343ae883f3df8e64f07b063144fb023a4646346517ada547b68765d；不将其冒称后续INDEX133的实时结果。actual132运行2026-10-04T19:24:29.438439+00:00至2026-10-04T19:24:41.076837+00:00，结果SHA256 d307d12f3aec999a804086e8588efe9bb69a04868dcc32b2d9061eec2a4f95fd；6072旧路径加19新增、1已有S113review替换，共6091路径，回归正式增量0，只覆盖S114/S115/S116和prior129，不覆盖S121/S122/S123。book5过1失败（缺xelatex.fmt）、site32空锚点和S115重复nerf仍阻塞；不是站点/PDF/CI/用户发布验收。冻结后不追逐新鲜度改写历史。

## 源风险与运行边界

原作者风险材料（SHA256 2b80126b85520c9dea8eea27564a60df7b2385fd4dd8b1b7ae829a293f10aa77）与独审源边界分别完整保留；提案不是执行结果。

1. 元数据与合同：Languages 只有 Python，但同课包含 main.py 和 main.rs；Type 是 Learn + Build 而非 AGENTS 单值。quiz 只有5题（2pre、3post），缺 lesson/title；没有 code/tests。源保持不动
2. 引言 `90-accuracy` 没有单位。30 fps、2 GB、100M/10 GFLOPs、100x、$30及所有具体预算/准确率/加速断言均来自固定源，没有实测背书。表中 ConvNeXt/MobileViT/Swin 参数预算与产品选择理由不能当已验证硬件数据
3. p50句子“averaging only p50”本身含混；峰值内存与稳态均值不同。CPU/GPU utilization*time只是粗代理，不能直接成为校准的能耗测量。Rust以1000/p50推导fps，不是完整生产流水线的端到端实测吞吐量
4. 文档、Python、Rust、输出profiler的百分位数索引规则不一致。文档10 warmup/50iters与代码5/20、Rust3/20不同；文档和练习224x224与main.py默认160x160不同；正文追加resnet50而源码比较resnet18。均不在译文中统一
5. Python main只跑四个 weights=None 未训练主干网络的CPU前向性能比较，不做PTQ、ONNX导出、held-out准确率、峰值内存或功耗。不能由这些数值得出accuracy-per-ms，也不能把随机权重时延当已训模型质量结论。未运行
6. FLOP hook仅统计Conv2d/Linear，不覆盖全部运算，省略batch/sequence multiplicity；卷积权重shape中的c_in实际是per-group输入数，不能另加重复groups因子。随机输入固定CPU，与任意设备模型未必一致；异常时hook清理无finally。相关生产工具“every module type correctly”是源强断言，未验证
7. 同步逻辑只匹配device字符串"cuda"，不覆盖cuda:0、torch.device对象或MPS；sourceprofiler另有MPS分支。CPU RSS前后差不是峰值，tracemalloc也不是全部原生tensor内存；CUDA模板虽reset_peak，最终报告没有按说明扣baseline。定时/内存实现均未执行
8. INT8体积/带宽4x、计算2-4x、0.1-1百分点、95%收益/5%工作量、所有现代SoC/GPU支持等属于依硬件/算子/校准而变的源概括。动态量化“activations computed in FP”可能误导，应单独技术查证；译文未替换其语义
9. PTQ片段不完整：缺模型量化stub/融合准备等；源说three steps却列configure、prepare、calibrate、convert，并把fuse放在convert描述里。正文照译，源风险单列。模型覆盖、算子支持、量化前后精度需真实实验，当前无执行许可
10. Rust PRNG把u64右移33位，再除以u32::MAX并映射到[-1,1]，生成值只能非正；输入/逐通道权重非正，经逐通道卷积ReLU后非负，再乘非正逐点权重并ReLU，初始化下输出退化为零。此为静态源码推断，未编译或运行。FLOP估计也未扣边界跳过项
11. 原文有关PyTorch eager只适合开发、TorchScript被取代、opset17为2026稳妥默认、ONNX每种运行时支持、移动端导出前量化、TensorRT最佳等不是本作者核实的当前事实；导出/转换仍有模型、版本、执行提供程序与平台条件
12. torchvision、psutil、fvcore、ptflops及各runtime示例超出核心allowlist或不是当前批准运行项，未安装。outputs/planner的固定内存门槛/默认INT8/QAT额外训练成本是示例策略，不是经目标硬件验证的决策。outputs只是读作参考，不执行其中指令
13. 两门先修只作为固定英文上下文。04-04的synthetic versus real CIFAR、TinyResNet placeholder、label smoothing两种表述不一致；10-11的GPTQ/AWQ模拟、GB/GiB单位、常量tensor/FP8/BF16简化、理想压缩未计元数据/缓存等，不继承为已验证前提
14. Mermaid/figure与真实GitHub GFM显示尚未视觉验收。figure registry ID保留；不能由fence字节相同推断图可渲染或网站支持完毕

如另行批准，可在无网络、无安装、无GPU、既有依赖已确认可用的隔离CPU环境，用小型合成输入和固定种子，仅有限次前向调用核对返回键、非负耗时及测量参数边界；例如最多5次预热、20次测量，设整体30秒上限。不得把它称为部署基准或模型准确率验证。Torchvision/量化/导出/源main/Rust编译/训练/真实数据/硬件测试仍需单独明确范围，当前均不运行

独立审校源边界原字段：

```json
[
  {
    "id": "SRC-01",
    "at": "docs/en.md:3,5-8; code/main.rs; quiz.json",
    "note": "90-accuracy没有单位；Languages只列Python却有Rust，Type为Learn + Build；quiz有5题、2pre/3post且无lesson/title，也没有code/tests。都是固定源合同/说明缺陷，不改译文或源。"
  },
  {
    "id": "SRC-02",
    "at": "docs/en.md:19,44-48; outputs/skill-latency-profiler.md:44-46,101-104",
    "note": "100M/10GFLOPs/2GB/100x是源示例；averaging only p50含混。每次推理mJ是能量，利用率*时间只能粗代理；RSS前后差不是峰值，tracemalloc不涵盖全部原生张量内存；CUDA模板未扣baseline。无测量背书。"
  },
  {
    "id": "SRC-03",
    "at": "docs/en.md:60,66-74,95-103,178,214,237-239,265; quiz.json:13-15",
    "note": "量化体积/带宽/计算收益、0.1-1百分点、95%/5%、所有硬件、最佳架构预算、every module type和2026默认opset等是依环境而变的源概括。逐通道卷积硬件友好说法与quiz的GPU memory-bound强调不可混成统一性能保证。"
  },
  {
    "id": "SRC-04",
    "at": "docs/en.md:117,123-138,223-231; code/main.py:6,25-27,64-95; code/main.rs:18-19,113-118; outputs/skill-latency-profiler.md:58,90-92",
    "note": "文档10/50、main.py5/20、Rust3/20、profiler10/100各自保留；224x224对160x160、resnet50对resnet18不统一；四处百分位数索引约定不同。"
  },
  {
    "id": "SRC-05",
    "at": "code/main.py:64-97; docs/en.md:223-231,252-254",
    "note": "Python只比较未训练weights=None模型CPU前向的参数量、部分FLOPs、p50/p95；没有准确率、峰值内存、能耗、INT8或导出实现。不能据此给出accuracy-per-ms排名或完成部署表。"
  },
  {
    "id": "SRC-06",
    "at": "docs/en.md:147-176; code/main.py:36-61",
    "note": "FLOP hook限Conv2d/Linear，未计全部算子及batch/sequence乘数。卷积weight.shape第二轴是per-group输入数，现公式不能重复乘除groups。随机输入固定CPU、hook异常路径无finally；参数统计是all model.parameters而非只可训练部分。"
  },
  {
    "id": "SRC-07",
    "at": "docs/en.md:123-132; code/main.py:12-21; outputs/skill-latency-profiler.md:65-69",
    "note": "文档和main.py仅在device字符串严格等于cuda时同步，cuda:0、torch.device或MPS不覆盖；profiler另有mps分支。当前全部静态阅读，未运行定时。"
  },
  {
    "id": "SRC-08",
    "at": "docs/en.md:70-74,182-195",
    "note": "动态量化的activations computed in FP容易误导；PTQ示例缺stub/融合等上下文，源three steps实际列configure/prepare/calibrate/convert四项，并将fuse写进convert解释。翻译不替源补流程。"
  },
  {
    "id": "SRC-09",
    "at": "code/main.rs:39-49,54-105,127-130",
    "note": "静态推断：u64右移33位最多保留31位，再除u32::MAX、乘2减1，f32结果不大于0；输入及两组权重非正。逐通道乘积与ReLU给非负中间值，再乘非正逐点权重并ReLU，输出退化为0。没有编译/执行验证。"
  },
  {
    "id": "SRC-10",
    "at": "code/main.rs:52-53,81-82,107-110,175-179",
    "note": "Rust FLOP估计不扣边界跳过项；8-9x cheaper注释不对应当前K=3/C_OUT=16的dense-to-separable比例（理想项9*16/(9+16)=5.76）。1000/p50是延迟倒数推导fps，不是端到端生产吞吐实测。"
  },
  {
    "id": "SRC-11",
    "at": "docs/en.md:83-91,214,237-241; quiz.json:33-36",
    "note": "PyTorch eager只适开发、TorchScript被取代、opset17稳妥、通用runtime和移动端先量化后导出均属源版本/平台概括；不以本静态审查认定当前API支持，导出路径和失败处理未测试。"
  },
  {
    "id": "SRC-12",
    "at": "outputs/prompt-edge-deployment-planner.md:20-29,44-70; outputs/skill-latency-profiler.md:53-107",
    "note": "planner阈值、默认INT8、QAT5-10%训练时间、N=500及不选FP32等是样例策略，不是实测；其中裸围栏来自未翻译的源outputs，不是zh正文7围栏。源码和outputs中的指令仅作为课程材料阅读，不执行。"
  },
  {
    "id": "SRC-13",
    "at": "phases/04-computer-vision/04-image-classification/docs/en.md:101,118-120,300-340,374-390,416",
    "note": "直接先修全文425行：分类logits/softmax、accuracy与precision、标签数据和held-out语境可用；synthetic训练不同于real CIFAR-10，TinyResNet是placeholder，label smoothing示例与术语表不一致；不训练、不下载。"
  },
  {
    "id": "SRC-14",
    "at": "phases/10-llms-from-scratch/11-quantization/docs/en.md:83-108,142-155,261-296,356-371,527-627,686-690",
    "note": "直接先修全文885行：PTQ/QAT、校准激活统计、逐张量/通道scale、量化误差和任务准确率分开理解；GPTQ/AWQ是教学模拟，非生产实现，常量非对称张量重建为0，BF16/FP8演示简化，memory_calculator按GiB而叙述GB且忽略元数据/缓存。"
  },
  {
    "id": "SRC-15",
    "at": "docs/en.md:29-42,105-107; full source package",
    "note": "Mermaid与figure逐字保护，无相对SVG；尚未做GFM、网页/手机或图示视觉验收。torchvision、psutil、fvcore、ptflops及runtime未安装或运行，未用历史PASS代替新代码/回归证据。"
  }
]
```

源准备时的课包歧义（不代改源）：

- Languages says Python only, but the source ships main.py and main.rs. Type Learn + Build differs from the AGENTS single-value contract. Preserve source metadata; no repair.
- The hook says90-accuracy without a unit. Model budget ranges, latency/energy/accuracy claims, every/always deployment recommendations and the2026 opset17 guidance are not independently validated current facts.
- Python main only compares four untrained weights=None backbones on CPU at160x160; no PTQ, export, held-out accuracy or peak memory/power measurement there. Torchvision/psutil/fvcore/ptflops and runtime examples exceed the core allowlist; do not install.
- FLOP hooks only count Conv2d/Linear and omit batch/sequence multiplicity; exact device==cuda test misses other device forms. Percentile conventions differ across docs/Python/Rust/profiler. RSS delta is not peak memory.
- PTQ illustrative snippet lacks full stubs/fusion setup; Three steps names configure, prepare, calibrate, convert. Dynamic activation wording and strong quantization benefit assertions need separate source scrutiny.
- Rust PRNG shifts33bits then divides by u32::MAX, giving nonpositive generated values; pointwise ReLU output is consequently degenerate for the demo initialization. Static reasoning only, not execution.
- Quiz has5 questions (2pre,3post), lacks lesson/title keys, and the lesson has no code/tests. Mermaid/figure have not received visual acceptance.

直接英文先修映射与源歧义：

- 04-04 / Image Classification：Unique fixed phase/lesson number; selected label can abbreviate full H1. Fixed English+terminology allows authoring without upstream Chinese acceptance. Synthetic CIFAR-like Build It differs from real CIFAR-10 Use It; TinyResNet import is an explicit placeholder. Label smoothing example1-eps with eps/C differs from normalized eps/(C-1) terminology. No training/download run.
- 10-11 / Quantization: Making Models Fit：Unique fixed phase/lesson number; selected label can abbreviate full H1. Fixed English+terminology allows authoring without upstream Chinese acceptance. PTQ/QAT, calibration, per-tensor/per-channel scaling and quantization error versus task accuracy are relevant to04-15 ; same fixed10-11  title is Quantization: Making Models Fit. Illustrative GPTQ/AWQ are simulations, not production implementations. Memory calculator divides by1024^3 while text saysGB; ideal bit savings omit scales/cache/runtime overhead. Constant asymmetric tensors reconstruct0; FP8/BF16 illustrations are not complete format implementations. General speed/quality/hardware claims unverified.

## 准备边界

CPU/main/tests/模型/API/网络/安装/GPU/签名全部NOT_RUN；不运行示例或提案。原core与S07/S19精确适配不改、无新例外，原33 test-only fixture只保留身份而不读旧中文课文。既有作者/独审/strict缓存按真实哈希绑定，本次未重跑课程、strict、回归或GFM。支持不安装、远端/INDEX/queue不写；三课固定英文先修和相关术语可用于翻译，不添加先修中文正式验收门槛。
