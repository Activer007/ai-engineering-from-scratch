# S13 范围：降维

2026-10-02。只做 01/10 Dimensionality Reduction，固定英文 `1bafaa88bb4668356791150bec3a6d7df38387eb`。先修线性代数、矩阵变换与概率已审，SVD试点也已审；源先修栏把03称为Eigenvalues & Eigenvectors，与目录实际Matrix Transformations标题不同，此来源问题保留。

374 行、169 块、72 正文/符号候选、24 标题、4 表、13 围栏（6 Python、5 裸说明/公式、1 Mermaid、1 figure），约 1710 正文英文词。保留 PCA→解释方差→t-SNE/UMAP→kernel PCA→重构的完整单课，不扩展到后续张量主题。

从固定 EN 独立新译，不读旧中文/cache/历史PR；完整独立技术对照加另一遍中文通读、逐块来源/目标hash、载荷与结构保护、原strict与控制、双重放、基线审计、实际GitHubGFM、远端字节为门槛。仅 S13 和01-10增量记录，总索引仅PR7串行CAS；S07例外不得扩大。

源距离/体积/样本数泛化、方差与信息混同、kernel PCA投影缩放、MSE与特征值归一化、算法速度/全局结构/分离保证、输入和数值边界直接定位单列；只做翻译所必需的核实，不扩展源文纠错研究。

先完整读程序，仅运行已安装allowlist NumPy的本地合成示例和有限断言；不得运行含fetch_openml的main或MNIST联网路径，也不运行不在allowlist的sklearn/UMAP、不安装包或下载数据。source canonical导入后只显式调用安全离线函数。原站/移动端/交互图、CI、源修正和发布合并单列，Actions保持禁用，只本fork draft。
