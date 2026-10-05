# OCR 与文档理解

> 光学字符识别（OCR）是一条包含三个阶段的管线：先检测文本框，再识别字符，最后整理版面。所有现代 OCR 系统都会调整这些阶段的顺序，或将它们合并。

**Type:** Learn + Use
**Languages:** Python
**Prerequisites:** 阶段 4 第 06 课（目标检测）、阶段 7 第 02 课（自注意力）
**Time:** ~45 分钟

## 学习目标

- 梳理经典 OCR 管线（检测 -> 识别 -> 版面整理），以及现代端到端（end-to-end）替代方案（Donut、Qwen-VL-OCR）
- 实现用于序列到序列 OCR 训练的连接时序分类（Connectionist Temporal Classification，CTC）损失
- 无需训练，使用 PaddleOCR 或 EasyOCR 完成生产环境中的文档解析
- 区分 OCR、版面解析（layout parsing）和文档理解（document understanding），并为各类任务选择合适的工具

## 要解决的问题

充满文字的图像随处可见：收据、发票、身份证件、扫描书籍、表单、白板、标牌、屏幕截图。从这些图像中提取结构化数据，不只是读出字符，还要判断“这是总金额”，是计算机视觉应用中价值最高的问题之一。

这个领域的能力可以分为三个层次：

1. **OCR 本身**：把像素转换成文本。
2. **版面解析**：将 OCR 输出归并为不同区域（标题、正文、表格、页眉）。
3. **文档理解**：从版面中提取结构化字段（"invoice_total = $42.50"）。

每一层都有经典方法和现代方法。而“我想从图像中读出文字”与“我需要这张收据上的总金额”之间的差距，比大多数团队意识到的更大。

## 核心概念

### 经典管线

```mermaid
flowchart LR
    IMG["Image"] --> DET["Text detection<br/>(DB, EAST, CRAFT)"]
    DET --> BOX["Word/line<br/>bounding boxes"]
    BOX --> CROP["Crop each region"]
    CROP --> REC["Recognition<br/>(CRNN + CTC)"]
    REC --> TXT["Text strings"]
    TXT --> LAY["Layout<br/>ordering"]
    LAY --> OUT["Reading-order text"]

    style DET fill:#dbeafe,stroke:#2563eb
    style REC fill:#fef3c7,stroke:#d97706
    style OUT fill:#dcfce7,stroke:#16a34a
```

- **文本检测（text detection）** 为每行或每个单词生成一个四边形框。
- **文本识别（recognition）** 裁出各个区域并处理为固定高度，再通过卷积神经网络（CNN）+ 双向长短期记忆网络（BiLSTM）+ CTC，生成字符序列。
- **版面整理（layout）** 重建阅读顺序（reading order）：拉丁文字按从上到下、从左到右的顺序排列；阿拉伯文和日文则有所不同。

### 一段话理解 CTC

OCR 的识别阶段根据固定长度的特征图生成可变长度的序列。CTC（Graves 等人，2006）让你无需字符级对齐就能训练这样的模型。模型在每个时间步都输出一个覆盖词表及空白 token（blank，即不输出字符的词元）的分布；CTC 损失对所有在合并连续重复项、再移除空白 token 后可还原为目标文本的对齐关系进行边缘化，也就是对这些有效路径的概率求和。

```text
raw output: "h h h _ _ e e l l _ l l o _ _"
after merge repeats and remove blanks: "hello"
```

CTC 让卷积循环神经网络（CRNN）在 2015 年取得成功；到了 2026 年，大多数生产级 OCR 模型仍使用它进行训练。

### 现代端到端模型

- **Donut**（Kim 等人，2022）由视觉 Transformer（ViT）编码器和文本解码器组成；读入图像，直接输出 JSON。不需要文本检测器，也不需要版面模块。
- **TrOCR**：ViT + Transformer 解码器，用于文本行级 OCR。
- **Qwen-VL-OCR / InternVL**：针对 OCR 任务微调（fine-tuning）的完整视觉语言模型（VLM）；在 2026 年的复杂文档任务上准确率最高。
- **PaddleOCR**：将经典的 DB + CRNN 管线封装成成熟的生产级工具包，仍是开源 OCR 的主力。

端到端模型需要更多数据和计算资源，但能避免多阶段管线中的误差累积。

### 版面解析

对于结构化文档，运行版面检测器（LayoutLMv3、DocLayNet），为每个区域标注类别：标题、段落、插图、表格、脚注。这样，确定阅读顺序就变成了“按版面顺序遍历各个区域，再将它们拼接起来”。

对于表单，使用**键值抽取（Key-Value extraction）** 模型：视觉信息丰富的文档使用 Donut，普通扫描件使用 LayoutLMv3。这些模型以图像 + 检测出的文本 + 位置信息为输入，预测结构化的键值对。

### 评估指标

- **字符错误率（Character Error Rate，CER）**：Levenshtein 距离 / 参考文本长度，越低越好。生产目标：在清晰扫描件上 < 2%。
- **词错误率（Word Error Rate，WER）**：同样的计算方式，但以词为单位。
- **结构化字段的 F1**：用于键值任务，衡量 `{invoice_total: 42.50}` 是否被正确输出。
- **JSON 的编辑距离（edit distance）**：用于端到端文档解析；Donut 论文引入了归一化树编辑距离。

```figure
cv3-ctc-collapse
```

## 动手实现

### 步骤 1：CTC 损失 + 贪心解码器（greedy decoder）

```python
import torch
import torch.nn as nn
import torch.nn.functional as F


def ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0):
    """
    log_probs:      (T, N, C) log-softmax over vocab including blank at index 0
    targets:        (N, S) int targets (no blanks)
    input_lengths:  (N,) per-sample time steps used
    target_lengths: (N,) per-sample target length
    """
    return F.ctc_loss(log_probs, targets, input_lengths, target_lengths,
                      blank=blank, reduction="mean", zero_infinity=True)


def greedy_ctc_decode(log_probs, blank=0):
    """
    log_probs: (T, N, C) log-softmax
    returns: list of index sequences (blanks removed, repeats merged)
    """
    preds = log_probs.argmax(dim=-1).transpose(0, 1).cpu().tolist()
    out = []
    for seq in preds:
        decoded = []
        prev = None
        for idx in seq:
            if idx != prev and idx != blank:
                decoded.append(idx)
            prev = idx
        out.append(decoded)
    return out
```

`F.ctc_loss` 会在可用时采用高效的 CuDNN 实现。贪心解码器比束搜索（beam search）简单，其 CER 与束搜索相比通常相差不超过 1%。

### 步骤 2：小型 CRNN 识别器

用于文本行 OCR 的最简 CNN + BiLSTM。

```python
class TinyCRNN(nn.Module):
    def __init__(self, vocab_size=40, hidden=128, feat=32):
        super().__init__()
        self.cnn = nn.Sequential(
            nn.Conv2d(1, feat, 3, 1, 1), nn.BatchNorm2d(feat), nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
            nn.Conv2d(feat, feat * 2, 3, 1, 1), nn.BatchNorm2d(feat * 2), nn.ReLU(inplace=True),
            nn.MaxPool2d(2),
            nn.Conv2d(feat * 2, feat * 4, 3, 1, 1), nn.BatchNorm2d(feat * 4), nn.ReLU(inplace=True),
            nn.MaxPool2d((2, 1)),
            nn.Conv2d(feat * 4, feat * 4, 3, 1, 1), nn.BatchNorm2d(feat * 4), nn.ReLU(inplace=True),
            nn.MaxPool2d((2, 1)),
        )
        self.rnn = nn.LSTM(feat * 4, hidden, bidirectional=True, batch_first=True)
        self.head = nn.Linear(hidden * 2, vocab_size)

    def forward(self, x):
        # x: (N, 1, H, W)
        f = self.cnn(x)                # (N, C, H', W')
        f = f.mean(dim=2).transpose(1, 2)  # (N, W', C)
        h, _ = self.rnn(f)
        return F.log_softmax(self.head(h).transpose(0, 1), dim=-1)  # (W', N, vocab)
```

输入高度固定（CNN 通过最大池化将高度缩减到 1）。宽度就是 CTC 的时间维度。

### 步骤 3：合成 OCR 数据

生成白底黑字的数字字符串，用于端到端冒烟测试。

```python
import numpy as np

def synthetic_line(text, height=32, char_width=16):
    W = char_width * len(text)
    img = np.ones((height, W), dtype=np.float32)
    for i, c in enumerate(text):
        x = i * char_width
        shade = 0.0 if c.isalnum() else 0.5
        img[6:height - 6, x + 2:x + char_width - 2] = shade
    return img


def build_batch(strings, vocab):
    H = 32
    W = 16 * max(len(s) for s in strings)
    imgs = np.ones((len(strings), 1, H, W), dtype=np.float32)
    target_lengths = []
    targets = []
    for i, s in enumerate(strings):
        imgs[i, 0, :, :16 * len(s)] = synthetic_line(s)
        ids = [vocab.index(c) for c in s]
        targets.extend(ids)
        target_lengths.append(len(ids))
    return torch.from_numpy(imgs), torch.tensor(targets), torch.tensor(target_lengths)


vocab = ["_"] + list("0123456789abcdefghijklmnopqrstuvwxyz")
imgs, targets, lengths = build_batch(["hello", "world"], vocab)
print(f"images: {imgs.shape}   targets: {targets.shape}   lengths: {lengths.tolist()}")
```

真实的 OCR 数据集会加入字体、噪声、旋转、模糊和颜色等变化，所用管线与上面相同。

### 步骤 4：训练示例

```python
model = TinyCRNN(vocab_size=len(vocab))
opt = torch.optim.Adam(model.parameters(), lr=1e-3)

for step in range(200):
    strings = ["abc" + str(step % 10)] * 4 + ["xyz" + str((step + 1) % 10)] * 4
    imgs, targets, target_lens = build_batch(strings, vocab)
    log_probs = model(imgs)  # (W', 8, vocab)
    input_lens = torch.full((8,), log_probs.size(0), dtype=torch.long)
    loss = ctc_loss(log_probs, targets, input_lens, target_lens, blank=0)
    opt.zero_grad(); loss.backward(); opt.step()
```

在这份简单的合成数据上，经过 200 步训练，损失应从 ~3 降至 ~0.2。

## 实际使用

有三条生产应用路线：

- **PaddleOCR**：成熟、快速，支持多种语言。一行即可使用：`paddleocr.PaddleOCR(lang="en").ocr(image_path)`。
- **EasyOCR**：基于 Python 原生实现，支持多种语言，以 PyTorch 构建主干网络。
- **Tesseract**：经典工具；当模型难以处理老旧文档扫描件时，它仍然有用。

端到端文档解析可以使用 Donut 或 VLM：

```python
from transformers import DonutProcessor, VisionEncoderDecoderModel

processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base-finetuned-cord-v2")
model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base-finetuned-cord-v2")
```

对于具有重复结构的收据、发票和表单，微调 Donut。对于任意文档，或需要推理的 OCR 任务，Qwen-VL-OCR 这类 VLM 是当前的默认选择。

## 交付成果

本课产出：

- `outputs/prompt-ocr-stack-picker.md`：一份提示词（prompt），根据文档类型、语言和结构，在 Tesseract / PaddleOCR / Donut / VLM-OCR 中选择合适的方案。
- `outputs/skill-ctc-decoder.md`：一份技能文件，用于从零编写贪心和束搜索 CTC 解码器，包括长度归一化（length normalisation）。

## 练习

1. **（简单）** 使用随机的 5 位数字字符串训练 TinyCRNN，共训练 500 步。报告在留出集（held-out set）上的 CER。
2. **（中等）** 用束搜索替换贪心解码（beam_width=5）。报告 CER 的变化量。在哪些输入上束搜索更有优势？
3. **（困难）** 对一组 20 张收据使用 PaddleOCR，提取明细条目，再以人工标注的真实值为参照，计算 {item_name, price} 对的 F1。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|------|----------------|----------------------|
| OCR | “从像素中读出文字” | 将图像区域转换为字符序列 |
| CTC | “无需对齐的损失” | 无需逐时间步标签即可训练序列模型的损失；对所有对齐关系进行边缘化 |
| CRNN | “经典 OCR 模型” | 卷积特征提取器 + BiLSTM + CTC；这一 2015 年的基线至今仍用于生产环境 |
| Donut | “端到端 OCR” | ViT 编码器 + 文本解码器；直接从图像输出 JSON |
| 版面解析 | “找出区域” | 检测并标注文档中的标题/表格/插图/段落区域 |
| 阅读顺序 | “文本顺序” | 将识别出的区域排序并组织成句子；对拉丁文字很简单，对混合版面则不简单 |
| CER / WER | “错误率” | 按字符或词的粒度计算 Levenshtein 距离 / 参考文本长度 |
| VLM-OCR | “能阅读的大语言模型（LLM）” | 为 OCR 任务训练或通过提示词引导的视觉语言模型；在复杂文档上达到当前最优水平（SOTA） |

## 延伸阅读

- [CRNN (Shi et al., 2015)](https://arxiv.org/abs/1507.05717)：最初的 CNN+RNN+CTC 架构
- [CTC (Graves et al., 2006)](https://www.cs.toronto.edu/~graves/icml_2006.pdf)：最初的 CTC 论文，包含大量算法思想
- [Donut (Kim et al., 2022)](https://arxiv.org/abs/2111.15664)：无需 OCR 的文档理解 Transformer
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)：开源的生产级 OCR 技术栈
