# 决策树与随机森林

> 决策树（decision tree）就是一张流程图。但由许多决策树组成的森林，却是机器学习（ML）中最强大的工具之一。

**Type:** Build
**Language:** Python
**Prerequisites:** 阶段 1（课程 09 信息论、06 概率）
**Time:** ~90 分钟

## 学习目标

- 实现 Gini 不纯度、熵和信息增益的计算，找出决策树的最优划分
- 从零构建决策树分类器，并加入预剪枝控制（最大深度、最小样本数）
- 利用 bootstrap 抽样（自助抽样）和特征随机化构建随机森林（random forest），并解释它为什么能降低方差
- 比较 MDI 特征重要性与置换重要性，并识别 MDI 存在偏差的情况

## 要解决的问题

你手头有一份表格数据。每行是一个样本，每列是一个特征，还有一列是你想预测的目标。你可以直接拿神经网络来处理。但对于表格数据，树模型（决策树、随机森林、梯度提升树）的表现一直优于深度学习。在 Kaggle 的结构化数据竞赛中，占据主导地位的是 XGBoost 和 LightGBM，而不是 Transformer。

为什么？树模型无需预处理就能处理混合类型的特征（数值型和类别型），无需特征工程就能处理非线性关系。它们具有可解释性：查看树的结构，就能清楚看到模型为什么做出某个预测。而对许多树的结果取平均的随机森林，在中等规模的数据集上具有很强的抗过拟合能力。

本课使用递归划分从零构建决策树，再在此基础上构建随机森林。你将实现划分准则背后的数学计算（Gini 不纯度、熵、信息增益），并理解为什么把弱学习器组成集成（ensemble）后，就能得到强学习器。

## 核心概念

### 决策树做什么

决策树通过一连串是非问题，将特征空间划分成矩形区域。

```mermaid
graph TD
    A["Age < 30?"] -->|Yes| B["Income > 50k?"]
    A -->|No| C["Credit Score > 700?"]
    B -->|Yes| D["Approve"]
    B -->|No| E["Deny"]
    C -->|Yes| F["Approve"]
    C -->|No| G["Deny"]
```

每个内部节点都将一个特征与阈值进行比较。每个叶节点都给出一个预测。要对一个新数据点分类，就从根节点出发，沿着分支向下走，直到到达叶节点。

构建树时从上到下进行，在每个节点选择最能分开数据的特征和阈值。“最好”由划分准则来定义。

### 划分准则：衡量不纯度

每个节点都有一组样本。我们希望划分后得到的子节点尽可能“纯”，也就是说，每个子节点中的样本主要属于同一个类别。

**Gini 不纯度（Gini impurity）** 衡量的是：随机选取一个样本，再按照该节点的类别分布为它指定标签时，被错误分类的概率。

```text
Gini(S) = 1 - sum(p_k^2)

where p_k is the proportion of class k in set S.
```

对于纯节点（样本全属于同一类别），Gini = 0。对于类别比例为 50/50 的二分类划分，Gini = 0.5。数值越低越好。

```text
Example: 6 cats, 4 dogs

Gini = 1 - (0.6^2 + 0.4^2) = 1 - (0.36 + 0.16) = 0.48
```

**熵（entropy）** 衡量节点中的信息量（无序程度）。阶段 1 课程 09 已经介绍过。

```text
Entropy(S) = -sum(p_k * log2(p_k))
```

对于纯节点，entropy = 0。对于类别比例为 50/50 的二分类划分，entropy = 1.0。数值越低越好。

```text
Example: 6 cats, 4 dogs

Entropy = -(0.6 * log2(0.6) + 0.4 * log2(0.4))
        = -(0.6 * -0.737 + 0.4 * -1.322)
        = 0.442 + 0.529
        = 0.971 bits
```

**信息增益（information gain）** 是一次划分后不纯度（熵或 Gini）的减少量。

```text
IG(S, feature, threshold) = Impurity(S) - weighted_avg(Impurity(S_left), Impurity(S_right))

where the weights are the proportions of samples in each child.
```

每个节点采用的贪心算法是：尝试每个特征和每个可能的阈值，选择使信息增益最大的特征与阈值组合（feature, threshold）。

### 划分如何进行

假设当前节点的数据集有 n 个特征、m 个样本：

1. 对每个特征 j（j = 1 到 n）：
   - 按特征 j 对样本排序
   - 将相邻不同取值之间的每个中点都作为候选阈值
   - 计算每个阈值对应的信息增益
2. 选择信息增益最高的特征和阈值
3. 将数据划分到左侧（feature <= threshold）和右侧（feature > threshold）
4. 对每个子节点递归执行

这种贪心方法不能保证得到全局最优的树。寻找最优树是 NP-hard 问题。但贪心划分在实践中效果很好。

### 停止条件

如果没有停止条件，树会一直生长，直到每个叶节点都变纯（每个叶节点只有一个样本）。这样可以完美记住训练数据，泛化表现却很差。

**预剪枝（pre-pruning）** 在树完全长成之前停止生长：
- 最大深度：树达到设定深度时停止划分
- 每个叶节点的最小样本数：节点中的样本少于 k 个时停止
- 最小信息增益：最佳划分带来的不纯度改善小于阈值时停止
- 最大叶节点数：限制叶节点总数

**后剪枝（post-pruning）** 先让树完全长成，再进行修剪：
- 代价复杂度剪枝（scikit-learn 使用的方法）：加入与叶节点数成正比的惩罚。增大惩罚就能得到更小的树
- 错误率降低剪枝：如果移除一棵子树不会增加验证误差，就将其移除

预剪枝更简单、速度更快。后剪枝往往能得到更好的树，因为它不会过早阻止那些可能为后续有效划分创造条件的划分。

### 用于回归的决策树

对于回归任务，叶节点的预测值是其中目标值的均值。划分准则也会改变：

用 **方差减少量（variance reduction）** 代替信息增益：

```text
VR(S, feature, threshold) = Var(S) - weighted_avg(Var(S_left), Var(S_right))
```

选择让方差减少最多的划分。树将输入空间分成若干区域，并在每个区域内预测一个常数（均值）。

### 随机森林：集成的力量

单棵决策树的方差很高。数据中很小的变化，就可能产生完全不同的树。随机森林通过对许多树的结果取平均来解决这一问题。

```mermaid
graph TD
    D["Training Data"] --> B1["Bootstrap Sample 1"]
    D --> B2["Bootstrap Sample 2"]
    D --> B3["Bootstrap Sample 3"]
    D --> BN["Bootstrap Sample N"]
    B1 --> T1["Tree 1<br>(random feature subset)"]
    B2 --> T2["Tree 2<br>(random feature subset)"]
    B3 --> T3["Tree 3<br>(random feature subset)"]
    BN --> TN["Tree N<br>(random feature subset)"]
    T1 --> V["Aggregate Predictions<br>(majority vote or average)"]
    T2 --> V
    T3 --> V
    TN --> V
```

两种随机性来源让各棵树有所不同：

**Bagging（自助聚合，bootstrap aggregating）：** 每棵树都在一个 bootstrap 样本上训练，也就是从训练数据中有放回随机抽取的样本集。每个 bootstrap 样本中会出现约 63% 的原始样本（其余是可用于验证的袋外样本，即 out-of-bag samples）。

**特征随机化（feature randomization）：** 每次划分时，只考虑一个随机选取的特征子集。分类任务默认使用 sqrt(n_features)，回归任务使用 n_features/3。这可以防止所有树都按同一个占主导地位的特征划分。

关键在于：对许多相关性较低的树取平均，能够降低方差而不增加偏差。单棵树的表现可能平平，但集成后的模型很强。

### 特征重要性

随机森林自然能够给出特征重要性分数。最常用的方法是：

**平均不纯度减少量（Mean Decrease in Impurity，MDI）：** 对每个特征，将所有树中使用该特征的所有节点带来的不纯度减少量相加。在更靠前的划分中带来更大不纯度减少量的特征，更为重要。

```text
importance(feature_j) = sum over all nodes where feature_j is used:
    (n_samples_at_node / n_total_samples) * impurity_decrease
```

这种方法速度快（训练过程中就能计算），但会偏向高基数（cardinality，即不同取值的数量）的特征，以及具有许多可能划分点的特征。

另一种方法是 **置换重要性（permutation importance）**：打乱某个特征的取值，测量模型准确率下降了多少。这种方法更可靠，但也更慢。

### 树模型何时胜过神经网络

在表格数据上，决策树和随机森林的表现优于神经网络。原因有以下几项：

| 因素 | 树模型 | 神经网络 |
|--------|-------|----------------|
| 混合类型（数值型 + 类别型） | 原生支持 | 需要编码 |
| 小数据集（< 10k 行） | 效果好 | 过拟合 |
| 特征交互 | 通过划分发现 | 需要设计架构 |
| 可解释性 | 完全透明 | 黑盒 |
| 训练时间 | 几分钟 | 几小时 |
| 超参数敏感性 | 低 | 高 |

当数据具有空间或序列结构（图像、文本、音频）时，神经网络胜出。对于扁平的特征表，树模型是默认选择。

```figure
decision-tree-depth
```

## 动手实现

### 步骤 1：Gini 不纯度与熵

从零实现两种划分准则，并验证它们对哪些划分更好的判断一致。

```python
import math

def gini_impurity(labels):
    n = len(labels)
    if n == 0:
        return 0.0
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    return 1.0 - sum((c / n) ** 2 for c in counts.values())

def entropy(labels):
    n = len(labels)
    if n == 0:
        return 0.0
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    return -sum(
        (c / n) * math.log2(c / n) for c in counts.values() if c > 0
    )
```

### 步骤 2：寻找最佳划分

尝试每个特征和每个阈值，返回信息增益最高的那个。

```python
def information_gain(parent_labels, left_labels, right_labels, criterion="gini"):
    measure = gini_impurity if criterion == "gini" else entropy
    n = len(parent_labels)
    n_left = len(left_labels)
    n_right = len(right_labels)
    if n_left == 0 or n_right == 0:
        return 0.0
    parent_impurity = measure(parent_labels)
    child_impurity = (
        (n_left / n) * measure(left_labels) +
        (n_right / n) * measure(right_labels)
    )
    return parent_impurity - child_impurity
```

### 步骤 3：构建 DecisionTree 类

实现递归划分、预测和特征重要性跟踪。`_build` 是树的核心：节点变纯或达到预剪枝限制时，它就停止；否则，它会选取最佳划分，并对两个子节点递归处理。

```python
import random

class DecisionTree:
    def __init__(self, max_depth=None, min_samples_split=2,
                 min_samples_leaf=1, criterion="gini",
                 max_features=None):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.criterion = criterion
        self.max_features = max_features
        self.tree = None
        self.feature_importances_ = None

    def fit(self, X, y):
        self.n_features = len(X[0])
        self.feature_importances_ = [0.0] * self.n_features
        self.n_samples = len(X)
        self.tree = self._build(X, y, depth=0)
        total = sum(self.feature_importances_)
        if total > 0:
            self.feature_importances_ = [
                fi / total for fi in self.feature_importances_
            ]

    def predict(self, X):
        return [self._predict_one(x, self.tree) for x in X]

    def _build(self, X, y, depth):
        if len(set(y)) == 1:
            return {"leaf": True, "value": y[0]}

        if self.max_depth is not None and depth >= self.max_depth:
            return self._make_leaf(y)

        if len(y) < self.min_samples_split:
            return self._make_leaf(y)

        best_feature, best_threshold, best_gain = self._best_split(X, y)

        if best_feature is None or best_gain <= 0:
            return self._make_leaf(y)

        left_X, left_y, right_X, right_y = self._split_data(
            X, y, best_feature, best_threshold
        )

        if len(left_y) < self.min_samples_leaf or len(right_y) < self.min_samples_leaf:
            return self._make_leaf(y)

        weight = len(y) / self.n_samples
        self.feature_importances_[best_feature] += weight * best_gain

        return {
            "leaf": False,
            "feature": best_feature,
            "threshold": best_threshold,
            "left": self._build(left_X, left_y, depth + 1),
            "right": self._build(right_X, right_y, depth + 1),
        }

    def _make_leaf(self, y):
        counts = {}
        for label in y:
            counts[label] = counts.get(label, 0) + 1
        return {"leaf": True, "value": max(counts, key=counts.get)}

    def _best_split(self, X, y):
        best_feature = None
        best_threshold = None
        best_gain = -1.0

        if self.max_features == "sqrt":
            k = max(1, int(math.sqrt(self.n_features)))
            feature_indices = random.sample(range(self.n_features), k)
        elif isinstance(self.max_features, int):
            if self.max_features < 1:
                raise ValueError("max_features must be at least 1 when given as an integer")
            k = min(self.max_features, self.n_features)
            feature_indices = random.sample(range(self.n_features), k)
        else:
            feature_indices = list(range(self.n_features))

        for feature_idx in feature_indices:
            values = sorted(set(X[i][feature_idx] for i in range(len(X))))
            if len(values) <= 1:
                continue

            for i in range(len(values) - 1):
                threshold = (values[i] + values[i + 1]) / 2.0
                left_y = [y[j] for j in range(len(X)) if X[j][feature_idx] <= threshold]
                right_y = [y[j] for j in range(len(X)) if X[j][feature_idx] > threshold]

                if len(left_y) < self.min_samples_leaf or len(right_y) < self.min_samples_leaf:
                    continue

                gain = information_gain(y, left_y, right_y, self.criterion)
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature_idx
                    best_threshold = threshold

        return best_feature, best_threshold, best_gain

    def _split_data(self, X, y, feature, threshold):
        left_X, left_y, right_X, right_y = [], [], [], []
        for i in range(len(X)):
            if X[i][feature] <= threshold:
                left_X.append(X[i])
                left_y.append(y[i])
            else:
                right_X.append(X[i])
                right_y.append(y[i])
        return left_X, left_y, right_X, right_y

    def _predict_one(self, x, node):
        if node["leaf"]:
            return node["value"]
        if x[node["feature"]] <= node["threshold"]:
            return self._predict_one(x, node["left"])
        return self._predict_one(x, node["right"])
```

### 步骤 4：构建 RandomForest 类

实现 bootstrap 抽样、特征随机化和多数投票。

```python
class RandomForest:
    def __init__(self, n_trees=100, max_depth=None,
                 min_samples_split=2, max_features="sqrt",
                 criterion="gini"):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_features = max_features
        self.criterion = criterion
        self.trees = []

    def fit(self, X, y):
        n = len(X)
        for _ in range(self.n_trees):
            indices = [random.randint(0, n - 1) for _ in range(n)]
            X_boot = [X[i] for i in indices]
            y_boot = [y[i] for i in indices]
            tree = DecisionTree(
                max_depth=self.max_depth,
                min_samples_split=self.min_samples_split,
                max_features=self.max_features,
                criterion=self.criterion,
            )
            tree.fit(X_boot, y_boot)
            self.trees.append(tree)

    def predict(self, X):
        all_preds = [tree.predict(X) for tree in self.trees]
        predictions = []
        for i in range(len(X)):
            votes = {}
            for preds in all_preds:
                v = preds[i]
                votes[v] = votes.get(v, 0) + 1
            predictions.append(max(votes, key=votes.get))
        return predictions
```

完整实现及全部辅助方法见 `code/trees.py`。

## 实际使用

使用 scikit-learn，训练随机森林只需三行：

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
print(f"Accuracy: {rf.score(X_test, y_test):.4f}")
print(f"Feature importances: {rf.feature_importances_}")
```

在实践中，梯度提升树（gradient boosted trees，如 XGBoost、LightGBM、CatBoost）往往比随机森林更强，因为它们按顺序构建树，每棵树都会修正前面那些树的错误。不过，随机森林更不容易配错，几乎不需要超参数调优。

## 交付成果

本课产出 `outputs/prompt-tree-interpreter.md`，这是一份面向业务相关人员解释决策树划分的提示词（prompt）。向它提供训练好的树的结构（深度、特征、划分阈值、准确率），它就会将模型转化成通俗的规则，对特征重要性排序，指出过拟合或数据泄漏，并建议后续步骤。需要向不读代码的人解释树模型时，都可以使用它。

## 练习

1. 在一个有 3 个类别的 2D 数据集上训练单棵决策树。手动追踪划分过程，画出矩形决策边界。比较 max_depth=2 与 max_depth=10 时的边界。

2. 为回归树实现基于方差减少量的划分。生成 200 个满足 y = sin(x) + noise 的数据点，并拟合你的回归树。将树的分段常数预测与真实曲线画在一起比较。

3. 分别构建包含 1、5、10、50 和 200 棵树的随机森林。绘制训练准确率和测试准确率随树的数量变化的曲线。观察测试准确率达到平台期，但不会下降的现象（随机森林能够抵抗过拟合）。

4. 在 5 个不同的数据集上比较 Gini 不纯度与熵这两种划分准则。测量准确率和树深度。在大多数情况下，它们会产生几乎相同的结果。解释原因。

5. 实现置换重要性。在一个特征为高基数随机噪声的数据集上，将它与 MDI 重要性进行比较。MDI 会把这个噪声特征排得很高，而置换重要性不会。

## 关键术语

| 术语 | 通常的说法 | 实际含义 |
|------|----------------|----------------------|
| 决策树 | “用来预测的流程图” | 通过学习一连串 if/else 划分，将特征空间分成矩形区域的模型 |
| Gini 不纯度 | “节点有多混杂” | 节点处随机样本被误分类的概率。0 = 纯，0.5 = 二分类的最大不纯度 |
| 熵 | “节点中的无序程度” | 节点中的信息量。0 = 纯，1.0 = 二分类的最大不确定性。源自信息论 |
| 信息增益 | “一次划分有多好” | 划分后的不纯度减少量。选择划分的贪心准则 |
| 预剪枝 | “让树早点停下” | 通过设置最大深度、最小样本数或最小增益阈值，提前停止树的生长 |
| 后剪枝 | “长成之后再修剪” | 先让树完全长成，再移除不能改善验证表现的子树 |
| Bagging | “在随机子集上训练” | 自助聚合。每个模型都在有放回抽取的不同随机样本集上训练 |
| 随机森林 | “一群树” | 决策树的集成；每棵树在一个 bootstrap 样本上训练，每次划分时使用随机特征子集 |
| 特征重要性（MDI） | “哪些特征重要” | 每个特征贡献的不纯度减少总量，在所有树和节点上求和 |
| 置换重要性 | “打乱后再检查” | 随机打乱某个特征的取值后，准确率的下降量。对于噪声特征，比 MDI 更可靠 |
| 方差减少量 | “回归版的信息增益” | 回归树中与信息增益对应的量。选择使目标方差减少最多的划分 |
| bootstrap 样本 | “允许重复的随机样本” | 从原始数据集中有放回随机抽取的样本集。大小相同，但存在重复样本 |

## 延伸阅读

- [Breiman：Random Forests（2001）](https://link.springer.com/article/10.1023/A:1010933404324) - 随机森林的原始论文
- [Grinsztajn 等：Why do tree-based models still outperform deep learning on tabular data?（2022）](https://arxiv.org/abs/2207.08815) - 对表格任务中树模型与神经网络的严谨比较
- [scikit-learn 决策树文档](https://scikit-learn.org/stable/modules/tree.html) - 含可视化工具的实用指南
- [XGBoost: A Scalable Tree Boosting System（Chen & Guestrin，2016）](https://arxiv.org/abs/1603.02754) - 在 Kaggle 上占据主导地位的梯度提升论文
