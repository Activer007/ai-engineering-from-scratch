# S38 Flamingo 译文审校交付报告

2026-10-02 统一终验补记：本课及累计 63 课联合严格检查、两次逐字节重放通过（原 strict 61 课，既有 S07/S19 各一精确适配；没有新增例外）。原回归 33、两适配防护 24/50、仓库数量审计全部通过。快照 63/523 已审草稿、0 课进行中、460 课未开始。下文作者交接时的聚合 pending 已由本补记关闭；最终证据提交后的远端全字节及 CI 查询在 PR 说明与 PR #7 单一索引读回记录，避免自引用提交。final_acceptance=false 专指用户发布/完整网站验收，未合并或发布。

2026-10-02。本阶段完成语言审校和指定提交的实际 GitHub GFM 复验；此文件待协调者回填终验。`final_acceptance=false`，不是课程网站、移动端、CI 或发布验收。

## 固定范围与绑定

- 课程：12/04 Flamingo and Gated Cross-Attention for Few-Shot VLMs
- 固定英文提交：`1bafaa88bb4668356791150bec3a6d7df38387eb`
- 英文 SHA-256：`ee025c471f27b129edbaa5930c75688306a349f57658b4d4bcf4059cd9919b8f`
- 最终中文 SHA-256：`a8310b5383faa97bc63ccf52e1eb9ec7d34486c3256fd8fe16f5a0f86847ed57`
- 支持提交：`2a3e7a3fc9246418700423d948ac4cc0b10bd9c6`
- 初始内容提交：`37fa88e9b8b84ce016a69768542eaa25bdaffae6`；显示修复提交：`e074b72a1c4b3cee2ecb8e559536143737b08e08`
- 固定依赖 46 项，逐项核对工作区字节、Git pin 与 SHA-256；清单见 [DEPENDENCIES.json](DEPENDENCIES.json)，阶段术语见 [TERMINOLOGY.md](TERMINOLOGY.md)
- 只覆盖本课与其审核记录；未改固定英文、源代码、通用检查器或其他课程

## 作者与独立审校

作者从固定英文独立新译，未用旧中文、旧 PR 或旧缓存。作者完整英中技术自查后另遍通读中文；独立审员不读作者 QA，再完成全文英中对照与单独中文通读。覆盖 111 块，其中 53 个可译块、3 个保护围栏、18 个标题、2 张表、5 个练习和6项参考。

完整读取固定英文 12/03 BLIP-2 Q-Former 与 19/61 Cross-Attention Fusion，用于核对 Q/K/V 来源、每图潜向量数、序列维度、文本因果掩码、图像位置限制、冻结权重与梯度传播。作者另对原 Flamingo、Idefics2、OpenFlamingo 论文作有限定点核查，用于识别源风险；独立审员没有把这些外部核查冒称为自己的执行结果。源事实问题保留译文并单列。

`thousands of TPUv4` → `数千个 TPUv4` 的量级等值映射已明确记录并独立复核；没有编造精确数量。

## 实际执行范围

- 作者和独立审员均完整预读 175 行 canonical `main.py` 后，在外置超时下原样运行其3个 demo，未减少迭代或输入规模
- 作者11项有限 stdlib 检查：形状、Q/K/V、门控恒等及正负贡献、标量导数、最近图像掩码、空输入边界
- 独立审员10项有限检查：另加随机潜向量非持久、固定算子梯度通路、未接入mask、非有限/尺寸输入、练习给定数值的算术边界
- 原控制回归33项通过；单课严格检查与独立最终双新目录字节重放通过
- 本次没有安装依赖、下载模型/图像/权重/数据、调用外部模型 API，也没有执行 outputs 提示词
- PyTorch练习、真实 Flamingo/OpenFlamingo 训练、检查点推理、视频处理和few-shot效果均未运行；有限数值例不能证明真实模型能力

## 实际 GFM：先失败，再修复复验

本阶段作者亲自使用 dot 云浏览器检查了 GitHub Preview、渲染后 DOM 和截图；这里没有声称由协调者亲自浏览，也没有用离线 parser 代替 GFM。

1. [初始提交的实际页面](https://github.com/Activer007/ai-engineering-from-scratch/blob/37fa88e9b8b84ce016a69768542eaa25bdaffae6/i18n/zh/phases/12-multimodal-ai/04-flamingo-gated-cross-attention/docs/zh.md)：b0047 的三个未围栏图像占位符被显示为空 img/link，文本不可见，因此该次 GFM 未通过
2. 仅在该块 `<image A>`、`<image B>`、`<image C>` 的开尖括号前各增加一个反斜杠，共3个 ASCII 字节；其余110块、字词、公式和围栏不变。逆还原精确得到旧中文 SHA-256 `731e122789563d3d0224618e93bbda752f7f8ca0b7f12d4f772fcd4486e2b11d`。原 validate 通过；公共 review 在重绑前按预期保持 REVIEW_STALE，未绕过控制；独立审员复核差量后由协调者重绑
3. [修复后的实际页面](https://github.com/Activer007/ai-engineering-from-scratch/blob/e074b72a1c4b3cee2ecb8e559536143737b08e08/i18n/zh/phases/12-multimodal-ai/04-flamingo-gated-cross-attention/docs/zh.md)：三个图像标签全部字面可见，空 img 和空 href 均为0。复看首屏、修复段、两表及长残差公式、参考列表截图，确认18标题、表格9×3/11×3（含表头）、4个 strong、2个原有 em、3个围栏、6条参考；无未解析粗体、意外强调或观察到的表格截断。`cross-attention-fusion` 是可见普通代码标识，并非本次验证过的交互图；Mermaid为0

## 独立审员的15项源风险摘要

1. 首创、完全同构、Gemini谱系与选型等强概括不等于本次已核实事实；模型版本设置需区分。
2. Q-Former查询来自桥接模块，Flamingo新增交叉注意力查询来自文本；32/64 token本身不能证明单图/多图或少样本能力。
3. 每图固定K不等于整条提示词总视觉形状固定；视频T*64、编码器、层数和宽度不能由toy验证。
4. toy每次重新随机生成潜向量，没有持久学习参数、latent自注意力/FFN、多头或位置编码。
5. 零门控输出恒等不等于gate梯度为零；冻结权重不等于截断中间梯度，toy没有训练。
6. 非零残差项可抵消或翻转文本表示；文本性能下降不能唯一归因为门控打开过快。
7. 输入标记/掩码仍需约定；伪代码x_after_llm_block与x_after不一致，不能视为完整可执行程序。
8. i < i_t与最近前置图像定义及canonical行为冲突；单图视觉全可见与多图位置掩码不可混用。
9. mask仅为text×images表，未展开latent/head/batch轴，也未接入cross_attention。
10. 空输入、NaN和形状不符可使零门控失败；有限合法输入恒等不能泛化到任意输入。
11. 图文数据4.4B与表格1.3B冲突；数据类型和数量单位须分开，数值均未改写。
12. 模型名与9B/1.4B/64M参数分项可能混用；练习算术不是真实模型规格或硬件成本验证。
13. 目标三组示例与围栏两组完整示例有别；bird无真实生成，few-shot推理无更新不代表新增模块无需训练。
14. 固定fusion上下文的缓存、多头、LayerNorm和FFN不属于本课toy；该上下文只读未执行。
15. 论文节号、模型/数据和练习未由独立审员外查或运行；网站空锚点、移动端与交互未通过。

## 待完成与验收边界

- 聚合检查/聚合双目录重放：pending，由协调者完成
- 最终远端全部提交文件的逐字节读回：pending；浏览器视觉通过不能替代字节核验
- 托管 CI 查询：pending；本地检查通过不等于托管 CI 通过
- 原站离线 parser 仍有13个纯中文标题空锚点；真实课程站点、移动端和交互：未通过
- 发布、合并与部署：未批准；`final_acceptance=false`
