# 序列到序列模型

> 两个 RNN 搭档，试着充当翻译。它们遇到的瓶颈，正是注意力机制诞生的原因。

**Type:** Build
**Languages:** Python
**Prerequisites:** 第 5 阶段 · 08（用于文本处理的 CNN 和 RNN），第 3 阶段 · 11（PyTorch 入门）
**Time:** ~75 分钟

## 要解决的问题

分类任务把变长序列映射为一个标签。翻译任务则把变长序列映射为另一个变长序列。输入和输出各有自己的词表，甚至可能属于不同语言，长度也不一定相同。

序列到序列（seq2seq）架构（Sutskever, Vinyals, Le, 2014）用一种刻意保持简单的方案解决了这个问题：两个 RNN。一个读取源句子，生成固定大小的上下文向量；另一个读取这个向量，逐个生成目标句子的 token（词元）。用的还是你在第 08 课写过的代码，只是组合方式不同。

学习它有两个理由。首先，上下文向量的瓶颈是 NLP 中最有教学价值的失败案例。注意力和 Transformer 的种种优势，都可以由此引出。其次，这套训练方法，包括教师强制（teacher forcing）、计划采样（scheduled sampling）和推理时的束搜索（beam search），至今仍适用于所有现代生成系统，包括大语言模型（LLM）。

## 核心概念

**编码器（encoder）。** 读取源句子的 RNN。它最后的隐藏状态就是**上下文向量（context vector）**，即对整个输入的固定大小摘要。按说只需丢开源句子本身，信息一点也不会少。

**解码器（decoder）。** 另一个 RNN，用上下文向量初始化。每一步，它把上一步生成的 token 作为输入，输出目标词表上的概率分布。通过采样或 argmax 选出下一个 token，再把它送回解码器。如此反复，直到生成 `<EOS>` token 或达到最大长度。

**训练：** 在解码器的每个时间步计算交叉熵损失（cross-entropy loss），再沿序列求和。对两个网络都执行标准的随时间反向传播。

**教师强制。** 训练时，解码器在第 `t` 步接收的输入，是位置 `t-1` 上的*真实* token，而非解码器上一步的预测。这样能稳定训练；不用它，早期错误会不断累积，模型就学不会。推理时却只能使用模型自身的预测，因此训练与推理的数据分布总会有差异。这种差异称为**曝光偏差（exposure bias）**。

**瓶颈。** 编码器从源句子中学到的一切，都得挤进这一个上下文向量。长句会丢失细节，罕见词的信息会变得模糊。词序调整（chat noir 与 black cat 的差别）也只能靠记忆，无法通过计算完成。

注意力（第 10 课）解决这个问题的办法，是让解码器能够查看编码器的*每一个*隐藏状态，而不只是最后一个。核心思路就是这么简单。

```figure
lstm-gates
```

## 动手实现

### 第 1 步：编码器

```python
import torch
import torch.nn as nn


class Encoder(nn.Module):
    def __init__(self, src_vocab_size, embed_dim, hidden_dim):
        super().__init__()
        self.embed = nn.Embedding(src_vocab_size, embed_dim, padding_idx=0)
        self.gru = nn.GRU(embed_dim, hidden_dim, batch_first=True)

    def forward(self, src):
        e = self.embed(src)
        outputs, hidden = self.gru(e)
        return outputs, hidden
```

`outputs` 的形状是 `[batch, seq_len, hidden_dim]`，每个输入位置都有一个隐藏状态。`hidden` 的形状是 `[1, batch, hidden_dim]`，对应最后一个时间步。第 08 课讲的是“对 outputs 做池化，用于分类”。这里则保留最后的隐藏状态作为上下文向量，忽略各个时间步的输出。

### 第 2 步：解码器

```python
class Decoder(nn.Module):
    def __init__(self, tgt_vocab_size, embed_dim, hidden_dim):
        super().__init__()
        self.embed = nn.Embedding(tgt_vocab_size, embed_dim, padding_idx=0)
        self.gru = nn.GRU(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, tgt_vocab_size)

    def forward(self, token, hidden):
        e = self.embed(token)
        out, hidden = self.gru(e, hidden)
        logits = self.fc(out)
        return logits, hidden
```

每次调用解码器只处理一个时间步。输入是一批单个 token，以及当前隐藏状态；输出是下一个 token 在整个词表上的 logits（未经归一化的分数），以及更新后的隐藏状态。

### 第 3 步：使用教师强制的训练循环

```python
def train_batch(encoder, decoder, src, tgt, bos_id, optimizer, teacher_forcing_ratio=0.9):
    optimizer.zero_grad()
    _, hidden = encoder(src)
    batch_size, tgt_len = tgt.shape
    input_token = torch.full((batch_size, 1), bos_id, dtype=torch.long)
    loss = 0.0
    loss_fn = nn.CrossEntropyLoss(ignore_index=0)

    for t in range(tgt_len):
        logits, hidden = decoder(input_token, hidden)
        step_loss = loss_fn(logits.squeeze(1), tgt[:, t])
        loss += step_loss
        use_teacher = torch.rand(1).item() < teacher_forcing_ratio
        if use_teacher:
            input_token = tgt[:, t].unsqueeze(1)
        else:
            input_token = logits.argmax(dim=-1)

    loss.backward()
    optimizer.step()
    return loss.item() / tgt_len
```

有两个参数值得单独说明。`ignore_index=0` 表示不计算填充 token 的损失。`teacher_forcing_ratio` 表示每一步选择真实 token 而非模型预测作为输入的概率。开始时设为 1.0（完全使用教师强制），训练期间逐步退火至 ~0.5，以缩小曝光偏差造成的分布差异。

### 第 4 步：推理循环（贪心解码）

```python
@torch.no_grad()
def greedy_decode(encoder, decoder, src, bos_id, eos_id, max_len=50):
    _, hidden = encoder(src)
    batch_size = src.shape[0]
    input_token = torch.full((batch_size, 1), bos_id, dtype=torch.long)
    output_ids = []
    for _ in range(max_len):
        logits, hidden = decoder(input_token, hidden)
        next_token = logits.argmax(dim=-1)
        output_ids.append(next_token)
        input_token = next_token
        if (next_token == eos_id).all():
            break
    return torch.cat(output_ids, dim=1)
```

贪心解码（greedy decoding）在每一步都选择概率最高的 token。它可能越走越偏：一旦选定一个 token，就再也无法撤回。**束搜索**会保留得分最高的 `k` 个未完成序列，最后再从完整序列中选出得分最高的一个。常用束宽为 3-5。

### 第 5 步：展示瓶颈

用一个简单的复制任务训练模型：源序列为 `[a, b, c, d, e]`，目标序列也是 `[a, b, c, d, e]`。逐步增加序列长度，观察准确率。

```text
seq_len=5   copy accuracy: 98%
seq_len=10  copy accuracy: 91%
seq_len=20  copy accuracy: 62%
seq_len=40  copy accuracy: 23%
```

一个 GRU 隐藏状态无法无损地记住包含 40 个 token 的输入。编码器的每个时间步都含有信息，但解码器只能看到最后的状态。注意力直接解决了这个问题。

## 实际使用

PyTorch 有基于 `nn.Transformer` 和 `nn.LSTM` 的 seq2seq 模板。Hugging Face 的 `transformers` 库提供完整的编码器-解码器模型（BART、T5、mBART、NLLB），这些模型都在数十亿 token 上接受过训练。

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tok = AutoTokenizer.from_pretrained("facebook/bart-base")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-base")

src = tok("Translate this to French: Hello, how are you?", return_tensors="pt")
out = model.generate(**src, max_new_tokens=50, num_beams=4)
print(tok.decode(out[0], skip_special_tokens=True))
```

现代编码器-解码器放弃了 RNN，转而采用 Transformer。整体结构，也就是编码器、解码器、逐个生成 token，仍与 2014 年的 seq2seq 论文相同。变化的是各个模块内部的机制。

### 什么时候还会用基于 RNN 的 seq2seq

对于新项目，几乎不会。只有一些特定例外：

- 流式翻译：逐个读取输入 token，同时将内存使用控制在有限范围内。
- 设备端文本生成：Transformer 的内存开销高得无法承受。
- 教学：理解编码器-解码器的瓶颈，是理解 Transformer 为什么胜出的最快途径。

### 曝光偏差及其缓解方法

- **计划采样。** 训练期间逐步降低教师强制比例，让模型学会从自己的错误中恢复。
- **最小风险训练（minimum risk training）。** 用句子级 BLEU 分数代替 token 级交叉熵来训练，更贴近真正的目标。
- **强化学习微调（reinforcement learning fine-tuning）。** 用一个指标为序列生成器提供奖励。现代大语言模型的 RLHF 就会用到它。

这三种方法仍适用于基于 Transformer 的生成系统。

## 交付成果

保存为 `outputs/prompt-seq2seq-design.md`：

```markdown
---
name: seq2seq-design
description: Design a sequence-to-sequence pipeline for a given task.
phase: 5
lesson: 09
---

Given a task (translation, summarization, paraphrase, question rewrite), output:

1. Architecture. Pretrained transformer encoder-decoder (BART, T5, mBART, NLLB) is the default. RNN-based seq2seq only for specific constraints.
2. Starting checkpoint. Name it (`facebook/bart-base`, `google/flan-t5-base`, `facebook/nllb-200-distilled-600M`). Match the checkpoint to task and language coverage.
3. Decoding strategy. Greedy for deterministic output, beam search (width 4-5) for quality, sampling with temperature for diversity. One sentence justification.
4. One failure mode to verify before shipping. Exposure bias manifests as generation drift on longer outputs; sample 20 outputs at the 90th-percentile length and eyeball.

Refuse to recommend training a seq2seq from scratch for under a million parallel examples. Flag any pipeline that uses greedy decoding for user-facing content as fragile (greedy repeats and loops).
```

## 练习

1. **简单。** 实现简单的复制任务。用目标与源相同的输入-输出对训练 GRU seq2seq，测量序列长度为 5、10、20 时的准确率，复现这一瓶颈。
2. **中等。** 加入束宽为 3 的束搜索解码。在一个小型平行语料库上，与贪心解码比较 BLEU 分数。记录束搜索在哪些地方更好（通常是最后几个 token），又在哪些地方没有差别。
3. **困难。** 在包含 10k 对样本的改写数据集上微调 `facebook/bart-base`。使用留出的输入，比较微调模型与基座模型（base model）在束宽为 4 时的输出。报告 BLEU 分数，并挑选 10 个例子做定性分析。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|-----------------|-----------------------|
| 编码器 | 输入 RNN | 读取源序列，生成各时间步的隐藏状态和最终的上下文向量。 |
| 解码器 | 输出 RNN | 用上下文向量初始化，逐个生成目标 token。 |
| 上下文向量 | 摘要 | 编码器最后的隐藏状态。大小固定，正是注意力要解决的瓶颈。 |
| 教师强制 | 使用真实 token | 训练时，将上一个位置的真实 token 作为输入，以稳定学习过程。 |
| 曝光偏差 | 训练/测试差异 | 模型只用真实 token 训练，未曾练习如何从自己的错误中恢复。 |
| 束搜索 | 更好的解码 | 每一步保留得分最高的 k 个未完成序列，而不是贪心地只选一条。 |

## 延伸阅读

- [Sutskever, Vinyals, Le (2014). Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215) — 最初的 seq2seq 论文，共四页。
- [Cho et al. (2014). Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation](https://arxiv.org/abs/1406.1078) — 提出了 GRU 和编码器-解码器框架。
- [Bahdanau, Cho, Bengio (2014). Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) — 提出注意力的论文，建议学完本课后立即阅读。
- [PyTorch NLP from Scratch 教程](https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html) — 可实际构建的 seq2seq + 注意力代码。
