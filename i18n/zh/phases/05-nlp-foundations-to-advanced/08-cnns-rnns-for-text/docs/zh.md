# 用于文本处理的 CNN 和 RNN

> 卷积学习连续 n 元片段（n-gram），循环机制保留记忆。两者都已被注意力机制取代，但在硬件受限的场景中仍有用武之地。

**Type:** Build
**Languages:** Python
**Prerequisites:** 阶段 3 · 11（PyTorch 入门）、阶段 5 · 03（词嵌入）、阶段 4 · 02（从零实现卷积）
**Time:** ~75 分钟

## 要解决的问题

TF-IDF（词频-逆文档频率）和 Word2Vec 生成的是忽略词序的扁平向量。基于这些向量的分类器无法区分 `dog bites man` 和 `man bites dog`。有时，关键信息就藏在词序中。

在 Transformer 出现之前，两类架构填补了这一空白。

**用于文本的卷积神经网络（TextCNN）。** 在词嵌入（word embedding）序列上应用 1D（一维）卷积。宽度为 3 的滤波器（filter）就是一个可学习的三元片段（trigram）检测器：它覆盖三个词，输出一个分数。组合不同宽度（2, 3, 4, 5）的滤波器，就能检测多种尺度的模式。再通过最大池化得到固定大小的表示。结构扁平，可并行，速度快。

**循环神经网络（RNN, LSTM, GRU）。** 每次处理一个 token（词元），同时维护一个隐藏状态（hidden state），把信息传递到后续时刻。它们按顺序计算，能保留记忆，也能处理不同长度的输入。从 2014 到 2017 年，这类网络主导了序列建模，随后注意力机制登场。

本课将实现这两类架构，再指出推动注意力机制出现的局限。

## 核心概念

**TextCNN** （Kim, 2014）。先将 token 映射为嵌入。宽度为 `k` 的 1D 卷积让滤波器沿连续 `k` 元片段的嵌入滑动，生成特征图。对特征图做全局最大池化，选出最强的激活值。把多种滤波器宽度对应的最大池化结果拼接起来，再送入分类头。

为什么有效？滤波器就是可学习的 n-gram。最大池化具有位置不变性，因此，无论 "not good" 出现在评论开头还是中间，都会触发同一个特征。使用三种滤波器宽度，每种配 100 个滤波器，就能得到 300 个学得的 n-gram 检测器。训练可以并行进行，没有跨时间步的串行依赖。

**RNN。** 在每个时间步 `t`，隐藏状态为 `h_t = f(W * x_t + U * h_{t-1} + b)`。不同时间步共享 `W`、`U`、`b`。时刻 `T` 的隐藏状态概括了此前的整个输入前缀。做分类时，对 `h_1 ... h_T` 进行池化（取最大值、取平均值或取最后一个状态）。

普通 RNN 存在梯度消失问题。**LSTM** 加入了门，决定遗忘什么、存储什么、输出什么，使梯度在长序列中保持稳定。**GRU** 将 LSTM 简化为两个门，以更少的参数取得相近的表现。

**双向 RNN** 分别让一个 RNN 正向运行、另一个反向运行，再拼接它们的隐藏状态。每个 token 的表示都能利用左侧和右侧的上下文。这对标注任务至关重要。

```figure
rnn-unroll
```

## 动手实现

### 第 1 步：用 PyTorch 实现 TextCNN

```python
import torch
import torch.nn as nn
import torch.nn.functional as F


class TextCNN(nn.Module):
    def __init__(self, vocab_size, embed_dim, n_classes, filter_widths=(2, 3, 4), n_filters=64, dropout=0.3):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.convs = nn.ModuleList([
            nn.Conv1d(embed_dim, n_filters, kernel_size=k)
            for k in filter_widths
        ])
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(n_filters * len(filter_widths), n_classes)

    def forward(self, token_ids):
        x = self.embed(token_ids).transpose(1, 2)
        pooled = []
        for conv in self.convs:
            c = F.relu(conv(x))
            p = F.max_pool1d(c, c.size(2)).squeeze(2)
            pooled.append(p)
        h = torch.cat(pooled, dim=1)
        return self.fc(self.dropout(h))
```

`transpose(1, 2)` 将 `[batch, seq_len, embed_dim]` 的形状变为 `[batch, embed_dim, seq_len]`，因为 `nn.Conv1d` 把中间的轴视为通道轴。不论输入长度如何，池化输出的大小都是固定的。

### 第 2 步：LSTM 分类器

```python
class LSTMClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, n_classes, bidirectional=True, dropout=0.3):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True, bidirectional=bidirectional)
        factor = 2 if bidirectional else 1
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(hidden_dim * factor, n_classes)

    def forward(self, token_ids):
        x = self.embed(token_ids)
        out, _ = self.lstm(x)
        pooled = out.max(dim=1).values
        return self.fc(self.dropout(pooled))
```

沿序列做最大池化，而不是末状态池化。用于分类时，最大池化通常优于直接取最后一个隐藏状态，因为长序列末尾的信息往往会主导最后的状态。

### 第 3 步：梯度消失演示（建立直觉）

没有门控的普通 RNN 无法学习长距离依赖。考虑一个简单任务：预测 token `A` 是否在序列的任意位置出现过。如果 `A` 位于位置 1，而序列长 100 个 token，损失的梯度在反向传播时，就必须连续乘以循环权重 99 次。如果权重小于 1，梯度就会消失；如果大于 1，梯度就会爆炸。

```python
def vanishing_gradient_sim(seq_len, recurrent_weight=0.9):
    import math
    return math.pow(recurrent_weight, seq_len)


# At weight=0.9 over 100 steps:
#   0.9 ^ 100 ≈ 2.7e-5
# The gradient from step 100 to step 1 is effectively zero.
```

LSTM 通过贯穿网络的 **细胞状态（cell state）** 解决这个问题，这条路径只进行加性相互作用（遗忘门会以乘法缩放它，但梯度仍能沿着这条“高速公路”传播）。GRU 用更少的参数实现了类似的机制。两者都能在 100+ 步的序列上保持训练稳定。

### 第 4 步：为什么这仍然不够

即使使用 LSTM，仍然存在三个问题。

1. **串行计算瓶颈。** 在长度为 1000 的序列上训练 RNN，需要执行 1000 个串行的前向传播/反向传播步骤，无法沿时间维度并行。
2. **编码器-解码器架构中的固定大小上下文向量。** 解码器只能看到编码器最后的隐藏状态，整个输入都压缩在其中。输入较长时，细节会丢失。第 09 课会直接讨论这个问题。
3. **长距离依赖的准确率上限。** LSTM 的表现优于普通 RNN，但仍难以跨越 200+ 步传递特定信息。

注意力机制解决了这三个问题。Transformer 彻底去掉了循环机制。第 10 课将介绍这一转折。

## 实际使用

PyTorch 的 `nn.LSTM`、`nn.GRU` 和 `nn.Conv1d` 都可用于生产环境，训练代码采用常规写法即可。

Hugging Face 提供了可接入输入层的预训练嵌入：

```python
from transformers import AutoModel

encoder = AutoModel.from_pretrained("bert-base-uncased")
for param in encoder.parameters():
    param.requires_grad = False


class BertCNN(nn.Module):
    def __init__(self, n_classes, filter_widths=(2, 3, 4), n_filters=64):
        super().__init__()
        self.encoder = encoder
        self.convs = nn.ModuleList([nn.Conv1d(768, n_filters, kernel_size=k) for k in filter_widths])
        self.fc = nn.Linear(n_filters * len(filter_widths), n_classes)

    def forward(self, input_ids, attention_mask):
        with torch.no_grad():
            out = self.encoder(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state
        x = out.transpose(1, 2)
        pooled = [F.max_pool1d(F.relu(conv(x)), kernel_size=conv(x).size(2)).squeeze(2) for conv in self.convs]
        return self.fc(torch.cat(pooled, dim=1))
```

按约束条件选择适用场景：

- **边缘端 / 设备端推理。** 配合 GloVe 嵌入的 TextCNN，其模型体积比 Transformer 小 10-100x。如果部署目标是手机，就用这套组合。
- **流式 / 在线分类。** RNN 每次处理一个 token；Transformer 则需要完整序列。对于实时到来的文本，LSTM 仍然占优。
- **用小模型建立基线。** 在新任务上快速迭代，用 CPU 在 5 分钟内训练一个 TextCNN。
- **数据有限时的序列标注。** 对于只有 1k-10k 个已标注句子的数据集，BiLSTM-CRF（第 06 课）仍是可用于生产环境的命名实体识别（NER）架构。

其他情况都交给 Transformer。

## 交付成果

保存为 `outputs/prompt-text-encoder-picker.md`：

```markdown
---
name: text-encoder-picker
description: Pick a text encoder architecture for a given constraint set.
phase: 5
lesson: 08
---

Given constraints (task, data volume, latency budget, deploy target, compute budget), output:

1. Encoder architecture: TextCNN, BiLSTM, BiLSTM-CRF, transformer fine-tune, or "use a pretrained transformer as a frozen encoder + small head".
2. Embedding input: random init, GloVe / fastText frozen, or contextualized transformer embeddings.
3. Training recipe in 5 lines: optimizer, learning rate, batch size, epochs, regularization.
4. One monitoring signal. For RNN/CNN models: attention mechanism absence means they miss long-range deps; check per-length accuracy. For transformers: fine-tuning collapse if LR too high; check train loss.

Refuse to recommend fine-tuning a transformer when data is under ~500 labeled examples without showing that a TextCNN / BiLSTM baseline has plateaued. Flag edge deployment as needing architecture-before-everything.
```

## 练习

1. **简单。** 在一个 3 类的玩具数据集上训练 TextCNN（数据由你自行构造）。验证在平均 F1 上，滤波器宽度（2, 3, 4）的组合优于单一宽度（3）。
2. **中等。** 为 LSTM 分类器实现最大池化、平均池化和末状态池化。在小数据集上比较它们，记录哪种池化表现最好，并推测原因。
3. **困难。** 构建一个 BiLSTM-CRF NER 标注器（结合第 06 课和本课）。在 CoNLL-2003 上训练，与第 06 课仅使用 CRF 的基线以及经过微调的 BERT 比较。报告训练时间、内存占用和 F1。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|-----------------|-----------------------|
| TextCNN | 用于文本的 CNN | 在词嵌入上组合多组 1D 卷积，再做全局最大池化。Kim（2014）。 |
| RNN | 循环网络 | 每个时间步都更新隐藏状态：`h_t = f(W x_t + U h_{t-1})`。 |
| LSTM | 带门控的 RNN | 加入输入门 / 遗忘门 / 输出门，以及一个细胞状态。能在长序列上稳定训练。 |
| GRU | 更简单的 LSTM | 使用两个门而非三个门。准确率相近，参数更少。 |
| 双向 | 两个方向 | 将正向与反向 RNN 的结果拼接起来。每个 token 都能利用两侧的上下文。 |
| 梯度消失 | 训练信号消失 | 在普通 RNN 中，反复乘以 <1 的权重，会使早期时间步的梯度几乎为零。 |

## 延伸阅读

- [Kim, Y. (2014). Convolutional Neural Networks for Sentence Classification](https://arxiv.org/abs/1408.5882) — TextCNN 论文，共八页，容易读懂。
- [Hochreiter, S. and Schmidhuber, J. (1997). Long Short-Term Memory](https://www.bioinf.jku.at/publications/older/2604.pdf) — LSTM 论文，讲解出乎意料地清晰。
- [Olah, C. (2015). Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) — 这篇文章的图解让所有人都能理解 LSTM。
