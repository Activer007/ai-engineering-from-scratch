# S106-image-generation-diffusion English-first 支持范围

状态：本地check-only own3候选，未安装、未发布，不增加正式课程数。当前独立技术/中文语言PASS只绑定以下版本，不代替支持安装、真实GFM、远端最终字节核验及适用批次回归。

## 固定英文与唯一目标

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Source tree: `3d90647a3449a7b228a6b6025ed2b333ef99e81c`
- Lesson: 04-10
- Canonical docs H1: Image Generation — Diffusion Models
- Source: `phases/04-computer-vision/10-image-generation-diffusion/docs/en.md`
- Source Git blob: `6803d21892319333fc9ac6b5c81044995ac06721`
- Source SHA256: `596c04cae482ef2dd4aae5b11e7452c9fa9bfe74a44047286ed296a5ea5634cd`
- Target: `i18n/zh/phases/04-computer-vision/10-image-generation-diffusion/docs/zh.md`
- Eventual record: `i18n/zh/.curated/lessons/04-10/translation.json`
- Original core blocks: 141
- English prerequisite line: **Prerequisites:** Phase 4 Lesson 07 (U-Net), Phase 1 Lesson 06 (Probability), Phase 3 Lesson 06 (Optimizers)
- Actual first write UTC: 2026-10-04T14:04:26.812125+00:00 through 2026-10-04T14:04:26.813324+00:00
- First-write receipt SHA256: `b5423347fca10a3a93fb0a40b9d14a1bb623da7c5cf6fb22ab64d7faa29bdea6`
- Original complete first draft: 15468 bytes, SHA256 `8dc7f15fec7cd14bda61bf089366362bab4983d72363576fa3cbb6f3ce6e72d8`
- Original translation record: 64507 bytes, SHA256 `876af9175b305ae3bc77450d60ac95ae5dd157a66bc27b81df43bfb6c9b3eb55`
- Current reviewed target: 15489 bytes, SHA256 `42fdd683bd2fb376bcd005284b749d2890690b256749b3433cab279e014256b0`
- Current draft record SHA256: `876af9175b305ae3bc77450d60ac95ae5dd157a66bc27b81df43bfb6c9b3eb55`
- Independent language review SHA256: `bdcb96c134b9bdf81248d61ff3b86a1c68b389e1a96e7b84564edba62486b2ae`
- Existing local strict receipt SHA256: `0609b26f7b27e9e9769e4a582650053f165efb9ba893cb27e2616e6b54187a37`

首写以原回执和原字节为准，不用mtime重建，不倒推为当时独审或own3已通过。本课源文件见DEPENDENCIES.source_files；先修固定英文已定位，无先修中文formal门禁。

## 真实修订绑定

- Revision v2: 2026-10-04T14:06:14.600231+00:00 through 2026-10-04T14:06:14.600637+00:00; target `8dc7f15fec7cd14bda61bf089366362bab4983d72363576fa3cbb6f3ce6e72d8` → `204e5c5f8490d196d507ca021843769335c28e6efa726108649fdd37304006ba`; receipt SHA256 `07b04d065eef45fbca090abd6f588e713f2007a22871829364c7761220a481a8`; diff SHA256 `54d4e0ee586fc2ffc5cd3a7d8a6fdcf4e37365cec450dacbd38f3b0bcba52e0f`
- Revision v3: 2026-10-04T14:08:06.889128+00:00 through 2026-10-04T14:08:06.889551+00:00; target `204e5c5f8490d196d507ca021843769335c28e6efa726108649fdd37304006ba` → `42fdd683bd2fb376bcd005284b749d2890690b256749b3433cab279e014256b0`; receipt SHA256 `c9700c0000bbdddb96105e0b681f8f1d5d4444eba8cdc71cc143dfcd252a86c8`; diff SHA256 `7d9d4df5ed096d8e1384b2091d7ad58a326dee664ff82ef6a9ec92ac414ab4b6`

修订首尾快照及原差异均保留，只用技术事实和hash作公开绑定；不替换首写或初始record，不把后续版本当作首次版本。独立审校针对最终target/record，未要求新的翻译修订。

## 固定支持与当前溯源

共同准备清单SHA256 `aef5293c38284a7c281852d115973b8e1eb24c4b2a4787226bf578714b723e13`。files/support_pins为有记录的公开投影，保留common109原顺序、公共身份与历史role/classification，并非原内部对象逐字段完全相等；去除S97–S102条目的12个私有路径定位值，保留其receipt SHA256。reference_glossary_pins为101 TERM，另8 controls；own3只含本阶段DEPENDENCIES.json、SCOPE.md、TERMINOLOGY.md，总112。正文、record、兄弟阶段及图资产均不算own3。旧已核Git身份复用，不重写历史类别或首写时点。

当前冻结as-of为正式批次结果独立回读真实时间2026-10-04T14:39:28.193462+00:00：正式已审草稿117，INDEX commit `03379392933fa99905d1ba604dfb14c174060eb6`、SHA256 `98f0af00d276f873998de9313e8fd14c8553fc4e27a9dce473dcb1f8358532aa`；独立回读SHA256 `428e243e351cdfc5e8d655b232b779e5d58c41898f1fe9b7d4e0b96463bf53bf`。actual117于2026-10-04T14:25:30.110274+00:00至2026-10-04T14:25:40.159393+00:00真实执行，新覆盖S98/S99/S102，结果SHA256 `382c6ca8bf3cfe5eade9c2d0309848adc319e9c519ffe8ea1d4e649cd275083b`，正式增量0；不覆盖S106/S107/S108。本课所属批次尚未运行，不继承历史PASS。book5/6缺xelatex.fmt、站点空标题ID及CI/移动端/交互/发布等限制保留。

保留record schema_version=1、DEPENDENCIES version=1及原f9 core/S07/S19精确控制。own3 hash由外部manifest固定，无自引用，不新增builder/checker/audit框架或重分类表。原33 fixture只复用既有固定身份，不读取其旧中文正文或执行回归。

## 已有证据与实际限制

- 数学正文的1..T与代码数组的0..T-1没有显式映射；练习t=1000若直接索引长度1000的调度会越界。正文数值保持，不在翻译中暗修。
- 两份DDIM网格都止于索引0；文档a_prev=1的负索引分支不可达，终点仍保留alpha_bar[0]，并未显式走到干净时刻。eta=0仅在初始噪声给定时确定，不保证未设种子的多次调用相同。
- 文档与main在q_sample设备迁移、奇数维时间嵌入、TinyUNet base=32/16、DDPM函数名、DDIM标量转换与根号clamp上存在差异；正文的各层时间条件描述与示例仅在瓶颈注入的范围不同。
- 逆向条件分布闭式、eta=1恢复DDPM、50步接近1000步、DDIM/ODE、无坍塌或振荡、所有可控图像模型及生产系统等是固定源断言，未由本次翻译核验。v-parameterisation归属与模型性能需另核。
- sampler-picker的latency_budget为秒，steps*unet_forward_ms为毫秒，比较前缺少换算；ControlNet/Euler限制和普遍质量推荐不作为已验证规则。alpha_bar为信号功率保留系数，幅度系数是其平方根。
- 源quiz仅5题（2pre/3post），缺check及lesson/title；没有code/tests。源课包约定缺口单列，未改英文或quiz。
- 首写对4个原裸围栏补text标签，块25/33/55/71的载荷不变；Mermaid、自定义figure、公式/表及DDPM长行尚需真实页面检查。无SVG资产。
- main会导入numpy/torch，可能自动选CUDA，训练TinyUNet并执行DDPM/DDIM；本轮没有import或运行。有限CPU提案仅为另获GO后最多5秒的stdlib八步标量调度/系数核对，不运行main、模型、训练、采样、tests或GPU，不能据此验证实现或图像质量。

## 核验与发布边界

本准备仅核新候选JSON/字节/hash、当前作者/首写/真实修订绑定、本三课17个源文件及6个先修英文的既有身份与当前字节；复用101 TERM校准及已核common身份，不重新解析所有历史commit:path。S85–S96历史commit:path在原准备对象库缺失的限制保留，未fetch、未补造。固定源准备清单SHA256 `366f8db5752f3a40784a05d22380aa212096e5dd164c2b40d11f6e97286a1a66`。

没有全源扫描、课程执行/import、main/tests/CPU实验/模型/训练/GPU、安装/下载、实际GFM/site/mobile/PDF/CI或全库回归。只生成候选，不写作者、英文源、原支持、INDEX、queue或远端。publication pending/null是冻结时点的状态；后续发布须另有真实commit及独立完整字节回读。语言PASS和静态核对不代表本课已正式登记、运行或批次通过。
