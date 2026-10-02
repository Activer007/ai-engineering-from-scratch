# S18 交付报告：采样方法

2026-10-02。阶段完成快照 **40/523 已审课程草稿，3课已开始收尾，480课未开始**，发布/合并均0，README另计。实时数以 PR7 [单一总索引](https://github.com/Activer007/ai-engineering-from-scratch/blob/zh/stage-01-tool-foundations/i18n/zh/.curated/ROLLOUT-INDEX.json) 为准。

## 来源和双审

固定英语 `1bafaa88bb4668356791150bec3a6d7df38387eb`，source SHA-256 `387bb3952f9a86f59c898179ec88597a8e9719e662ecab1b6b93bd6a977c2616`；最终 target SHA-256 `7572cf2bbd12c8e3170177b4ee2146e60fa59e253f499feaeebb39c7b5a79909`。English-first独立新译，303块/118候选全文技术对照及另外一次中文通读，全部逐块source/target hash绑定，未解决必改项0。23项固定依赖实字节匹配。代码、公式、API、参数、链接和数值原样；34围栏仅22个裸围栏补text。分布语境抽样、LLM解码采样；独立审纠正3处解码动词并复核最终字节。

## 实际 GFM 与最小修复

[最终固定内容](https://github.com/Activer007/ai-engineering-from-scratch/blob/7faf263219a27ba8c465a65c3bbe625f6ed4da48/i18n/zh/phases/01-math-foundations/16-sampling-methods/docs/zh.md) 在 dot 云端Chrome实际查看。34标题、完整19×3术语表、25 strong、0意外em；温度/Top-k/Top-p、全部5练习、术语表和5参考资料可读。原figure代码标识符不是站点交互验收。

首次GFM发现练习4的 `8*x - 8*y` 被误识别为一个em，隐藏两个乘号。仅添加两个反斜杠；独立审确认可逆恢复此前全文已审hash `198b3b288e39010a0b84d3624907db4c5c1370e3e8b5a12c8247730ebb5cbd18`，无其他字节改动，公式含义等价。重新渲染已实际看到两个乘号，em从1降至0；原strict仍直接通过，没有新例外。

## 有限离线执行

作者完整阅读748行canonical后，用外部45秒上限及 python -S 原样运行，exit0；没有修改迭代次数，未加载可选matplotlib，8个有限核验通过。10个标准库正文定义块执行通过；缺少的sample_from_probs未注入，定义成功不等于所有函数可直接调用。1个混合SciPy块因超出allowlist整块未执行。无安装、联网、外部模型调用或数据下载。审校者另跑最终strict/33控制/双重放，不冒称重跑canonical。

## 来源边界

10组独立源风险另列：逆CDF端点、拒绝抽样包络界/接受率、重要性抽样方差、Monte Carlo误差前提、MH遍历与细致平衡、Gibbs/分层抽样绝对化、temperature零值、top-p边界、Gumbel代码把logits作概率及缺失helper等。源技术事实与代码未暗修。源parser仍有15空中文锚点。

## 控制与调度

组合39课原strict + S07一处精确已审符号表例外，共40课双重放逐字节一致；原33控制、S07的24守卫、523课/67认证课/12评测/505题审计和README计数通过，英文、源码、核心控制未改。网站/移动端/交互图、CI及用户发布验收仍未过；Actions禁用，空状态不是CI成功。全部仅fork draft。

根据最新要求，S19/S20/S21完成已有作者及必要独立审后，额外两条作者线退出；不增加新并行claim，之后仅一路顺序翻译并串行安排独立审。
