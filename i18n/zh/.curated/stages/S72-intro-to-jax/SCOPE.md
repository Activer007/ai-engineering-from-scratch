# S72 / 03-12 JAX 入门翻译范围

2026-10-03。实际 index90 commit `04a043f315ae09acb512f2a2f80e0ab23faa1ec9`、SHA256 `b3f4732c2bb65af334ed90cbf5131c3782d56b2234c6120f3a68ae34d181778a` 已由协调双读回并明确激活。唯一英文源为 `1bafaa88bb4668356791150bec3a6d7df38387eb` 的 `phases/03-deep-learning-core/12-intro-to-jax/docs/en.md`；目标为对应 `i18n/zh/.../docs/zh.md`。已完整阅读509行英文和179行 `code/jax_intro.py`。

显式前置为阶段03第01–10课及NumPy基础。已接受术语依次由S27/S29/S32/S35/S40/S43/S48/S53/S58/S63提供，另联用S08自动微分及S14张量操作；不把视觉待验的S69当作已接受依赖。78条精确依赖由不可变DEPENDENCIES.json绑定，工作文件SHA256及Git源字节已验证；不修改旧词表或锁定记录。实际已接受集合为90；本课完成前不增加计数。

全文新译，不读取既有中文课文、缓存或上游PR452/457。保留全部围栏/figure载荷、行内代码、公式、数值、URL、路径、标识符和元数据不可变值。通用章节沿核心补充表；自然时间单位译分钟，billion保留并解释，倍数保留原数值。两条延伸阅读裸URL后保持ASCII空格。普通正文乘号若发现渲染风险，先提议并获明确许可，不暗改保护内容。

执行边界：JAX、jaxlib、Optax、sklearn、Flax、Equinox、Orbax不安装、不导入、不执行。禁止MNIST、fetch_openml、网络下载、GPU、多设备、默认训练与JIT基准。仅静态源码/AST检查，或独立编写并明确标注非JAX的有限NumPy数学夹具；不将数学夹具称为框架验证。尤其记录异步计时同步不一致、无同步预热、未验证加速/准确率、key复用和丢弃余数等源风险，不改源码。

原strict、原33controls、两次全新精确字节重放、78pins复核和完整251块双读为本地门禁。独立同行技术/中文双读由另一个审校者完成。作者不写review.json、不提交或发布；协调唯一远端写者。真实GitHub GFM、完整可见内容/链接、课程站点锚点/移动端/figure交互、托管CI及整书PDF均单列；本地解析不能替代视觉。缺xelatex.fmt仍为已知PDF阻塞，不安装修复。
