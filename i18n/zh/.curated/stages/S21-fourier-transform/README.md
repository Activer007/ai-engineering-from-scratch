# S21-fourier-transform 交付报告：Fourier 变换

2026-10-02。阶段完成快照 **42/523 已审课程草稿、1课收尾中、480课未开始**；S20的一幅GitHub图尚待验收，不提前计入全部通过数。README另计，发布/合并均0。实时状态以PR7的 [单一总索引](https://github.com/Activer007/ai-engineering-from-scratch/blob/zh/stage-01-tool-foundations/i18n/zh/.curated/ROLLOUT-INDEX.json) 为准。

## 独立翻译与双审

固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`，源 SHA-256 `88d32836b77ed732bc2e2610451d4ea5509c1b20b9bb96dddc2dd3cd0bc47cff`，最终译文 SHA-256 `8ed5894393b29e8e9ff3d74768b1bbb15dcef55b21b8fa1bfffe2a98dd965c84`。English-first新译，不复用旧中文/cache/上游旧PR。完整465行/237块/97候选逐段技术对照，再另次中文全文通读，所有逐块来源/译文hash重算一致，未解决必改项0。22围栏载荷、公式、API、数字、链接和结构受到保护。

在dot云端Chrome实际检查 [最终内容提交](https://github.com/Activer007/ai-engineering-from-scratch/blob/b4be997888def33cf63f8b8b48e3d7a068e6eb31/i18n/zh/phases/01-math-foundations/20-fourier-transform/docs/zh.md)，28标题/3表/19 strong/0意外em，2幅Mermaid实际显示。原figure代码标识符并不等于真实网站交互验收。

## GFM乘号最小修复

初次真实渲染出现8个意外em，吞掉旋转因子、DFT性质表和术语表中的16个乘号。只在b0063/b0121/b0233分别插入2/12/2反斜杠，严格逆变换还原此前全文已审hash；另外234块及全部22围栏逐字节未动。原审校者做独立差量复核并绑定全部237块，随后原strict和两次重放通过。最终实际页面0意外em，线性/时移/频移与复指数乘号完整。

三表含表头为5×5、8×3、17×2。首次有1个GitHub图渲染错误；一次刷新后两图实际显示，逐框读取FFT和卷积定理的所有节点与连接标签。幅度/模/相位、信号采样/分布抽样、DFT/FFT及频点/Hz按语境区分；25项固定依赖无冲突。

## 有限运行与源边界

作者完整读581行canonical后，以外部30秒限制原样离线运行exit0，生成物只写外部QA目录。8项有限核验与1个原NumPy正文片段通过；3段SciPy示例超出allowlist未执行，没有安装。独立审校者另作有限标准库公式运算，并未重跑canonical，来源清楚区分。

12组独立源风险保留：正弦幅度/未归一化系数、偶数N/Nyquist约定、FFT长度与占位Complex类、频谱分辨率/补零、Hamming端点不为0、卷积与CNN互相关、STFT能量、混叠相位、空输入和长度1窗函数等。英文/代码未暗修。原网站17个空中文ID，以及dft/fourier两个重复ID。

## 组合控制与未过门槛

组合 **40课原strict + S07精确符号表例外 + S19精确两行竖线适配**，共42课两次重放逐字节一致。原33控制、S07的24守卫、S19的50守卫、523课/67认证课/12评测/505题审计和README计数通过，英文/源码/通用控制未改。

真实应用网站/移动端/交互图、CI、用户发布验收仍未过；Actions禁用，空workflow/status不是CI成功。零安装/联网模型调用/数据下载。仅fork draft，不merge、部署或上游写入。源风险的单列不是课程事实已正确的证明。

额外作者线已完成当前课及必要交叉审后退出；按最新要求不再领取新并行课，后续仅一路顺序作者并串行安排独立审。
