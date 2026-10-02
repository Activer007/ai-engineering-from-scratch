# S26 支持向量机术语增量 v1.0

2026-10-02。联用核心、补充及 S05–S24 固定词表。沿用核技巧、支持向量、范数、原始/对偶问题、Lagrange 与 KKT。

| EN | 推荐呈现 | 语境与保护 |
|---|---|---|
| support vector machine / SVM | 支持向量机（SVM） | 算法名称；SVC/LinearSVC/LinearSVM API 原样 |
| maximum margin / margin width | 最大间隔 / 间隔宽度 | 不混同概率边缘分布；源半宽与全宽混用单列 |
| hard / soft margin | 硬间隔 / 软间隔 | 约束必须满足与允许松弛的区别 |
| support vector | 支持向量 | 沿用 S20；软间隔中不只间隔边界点，源简化另记 |
| hyperplane / decision boundary | 超平面 / 决策边界 | w与b、点到平面距离、分类符号保护 |
| slack variable | 松弛变量 | xi_i 与误分类不是同一概念，间隔内正确点也可违反约束 |
| hinge loss / logistic loss | 合页损失（hinge loss）/ logistic 损失 | 分段线性与光滑损失不同；边界不可微条件只列源风险 |
| primal / dual formulation | 原始形式 / 对偶形式 | 沿用 S20 原始/对偶问题；求最小与求最大方向不互换 |
| convex quadratic program / QP | 凸二次规划（QP） | 凸不泛推唯一性，源假设分开记录 |
| linear / polynomial / RBF kernel | 线性核 / 多项式核 / 径向基函数（RBF）核 | 沿用 S13；数学核不同于系统或计算内核 |
| kernel-induced feature space | 核诱导的特征空间 | 隐式映射与直接求核值不同，参数有效性依条件 |
| support vector regression / SVR | 支持向量回归（SVR） | epsilon 管与两侧松弛变量保持 |
| epsilon-insensitive loss / tube | epsilon 不敏感损失 / epsilon 管 | 不敏感范围与总管宽区别只列源风险 |
| one-class SVM | 单类 SVM | 异常检测语境，不改成二类分类 |
| sparse solution | 稀疏解 | 此处主要对偶系数贡献稀疏，不等同原始权重稀疏 |

C 与 lambda 的关系依损失求和/均值归一化；hinge 极点梯度、全/半间隔、SVR 管宽、支持向量识别与线性模型预测存储等源问题按原文保留并单列。所有公式、符号、数值、代码和图载荷不变。
