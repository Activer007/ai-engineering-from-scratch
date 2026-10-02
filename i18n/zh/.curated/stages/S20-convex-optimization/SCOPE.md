# S20 范围：凸优化

2026-10-02。只做01/18 Convex Optimization。固定英文commit `1bafaa88bb4668356791150bec3a6d7df38387eb`、SHA256 `061158e46d86c18ffeb43b730c98c52994ae863629445f6431942a368cfdb952`。555行、275块、115可译块、23围栏。先修01/04及01/08已审；S19线性方程组和S21 Fourier由其他线负责，不覆盖。只读控制/术语25项见DEPENDENCIES.json。

固定英文从零新译，不读取旧中文/旧缓存/旧PR；代码、公式、数值/维度/条件方向、API、路径/链接、Mermaid/figure载荷和结构保护。裸围栏只补text。完整作者EN↔ZH技术自查后另一次全文中文通读，逐块source/target哈希；作者记录仅draft，随后与S21独立交换全文双审。原strict、33控制回归、两次离线重放、站点离线parser与hash依赖校验不替代真实GFM/网站验收。

先完整读取635行canonical程序再用外部timeout安全离线运行。stdlib math/random，正文前4段stdlib实现可用明示上下文验证；SciPy/sklearn示例保留但跳过，不安装CVXPY/SciPy/matplotlib或其他依赖，不联网/下载/模型调用。凸/严格凸、存在性/唯一性、步长/收敛、强对偶/KKT、Fisher/Adam等源风险仅必要定位和有限验证，不修源或扩大研究。

主协调唯一拥有共享索引、远端整合、draft PR及真实GFM。作者不push/merge/启用Actions。课程源/程序不变；网站中文锚点/移动端/交互figure、托管CI、最终合并/发布仍不宣称通过。
