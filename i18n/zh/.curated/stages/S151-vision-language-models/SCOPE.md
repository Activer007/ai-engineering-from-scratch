# S151-vision-language-models source-only scope candidate

Fixed source: `1bafaa88bb4668356791150bec3a6d7df38387eb`. Source: [phases/04-computer-vision/25-vision-language-models/docs/en.md](https://github.com/Activer007/ai-engineering-from-scratch/blob/1bafaa88bb4668356791150bec3a6d7df38387eb/phases/04-computer-vision/25-vision-language-models/docs/en.md). SHA-256 `8998f05f5d863f11139112ef6d845dce76cd3efc7756d6ea040ccb3bad018578`; Git blob `7779b8d1e4d8196b3f34ee02a8aaa5873db7e619`.

Status: COMPLETE LOCAL OWN3 CANDIDATE, pending independent review, remote publication/readback and installation. Common155 now binds final accepted S146/S147/S148 chains at verified formal163; previous common152 remains exactly unchanged. Expected final author input is147 terminology+8 immutable controls+own3=158 support files. No Chinese lesson body, author role or first-write chronology exists.

## English-first inputs and boundaries

- Complete target package (5 files) and direct English prerequisites 04-14, 04-18, 07-02 with all main implementations were statically read. No whole transitive DAG is claimed.
- Fresh source-only tree contains5411 fixed English/non-i18n files; byte/blob/mode checked. No common support, own3, old Chinese body/record/review, original33 fixture, runtime install or author exists.
- Existing parent-approved target-only bare→text normalizations: b59 source lines94–96. Source and fence payload remain exact. Future author records each delta before initial capture/selfcheck. Immutable scanner d89de5eec36e10edcc391330d973632e3ceedb33fe679de3503dab52a7f6ece8 lines128–130 and existing rollout line86; no new exception.
- Preserve all code/math/identifiers/paths/URLs/numbers/units/metadata/table structure/Mermaid/figure/SVG. No source repair or fact modernization in translation.
- Source scanner and English identity assembly pass; this is not Chinese strict/review, GFM/site/mobile/PDF or course runtime verification.
- Mandatory canonical i18n documentation includes unrelated historical Chinese sample; source preparer exposure disclosed, not reused. Fresh authors use only English and finalized lexical supports.

## Source caveats

### VLM-UNIVERSAL-ARCHITECTURE

phases/04-computer-vision/25-vision-language-models/docs/en.md:3,21-23,47-51,57-65,269; site/figures-visaudio4.js:159-160. Universal assertions (every production VLM, mechanical swapping, projector being where most fine-tuning occurs, three standard stages) exceed the source implementation. The diagram itself allows a Q-former, which is not simply a 2-4-layer MLP. Model-specific mergers, token compression, cross-layer routing, tokenization, training stages and masks require integration work.

### VLM-MODEL-TABLE

phases/04-computer-vision/25-vision-language-models/docs/en.md:67-78. Multiple owner-source conflicts and variant ambiguities are recorded in official_claim_checks. The table is explicitly early 2026, not a verified live catalog. Model names, parameter/context values, active-parameter qualifiers, benchmark labels, and table structure are protected source evidence.

### VLM-CMER-EVIDENCE

phases/04-computer-vision/25-vision-language-models/docs/en.md:88-98; phases/04-computer-vision/25-vision-language-models/quiz.json questions 3 and 4; phases/04-computer-vision/25-vision-language-models/outputs/skill-cmer-monitor.md:12,55-81. The lesson supplies no linked primary study for Skywork introducing CMER, the 12% dataset figure, the 35% reduction, or the universal deployment requirement. The bounded official-domain searches found no matching primary evidence; this is absence in the checked sources, not proof no evidence exists. Quiz question 3 further recasts the 12% image-caption mismatch statistic as a typical CMER output rate, mixing different denominators.

### VLM-CMER-DENOMINATOR

phases/04-computer-vision/25-vision-language-models/docs/en.md:188-203; phases/04-computer-vision/25-vision-language-models/code/main.py:31-37; phases/04-computer-vision/25-vision-language-models/outputs/skill-cmer-monitor.md:47-51. The implementation computes mean((confidence > 0.8) & (similarity < 0.25)) over all requests. The docs return comment can be read as fraction among high-confidence outputs, which is a different denominator. Operators are strict > and <; equality is not flagged. Human-scored hallucination fraction in exercise 1 is described only as CMER-like.

### VLM-CMER-CONFIDENCE

phases/04-computer-vision/25-vision-language-models/outputs/skill-cmer-monitor.md:23. The source calls confidence mean per-token probability but specifies exp(mean(log_probs)), the geometric mean rather than arithmetic mean. The lesson does not extract or calibrate probabilities from a real VLM. These scores and global cosine similarity do not establish truth of every object, count, relation or OCR detail.

### VLM-CMER-CHECKER

phases/04-computer-vision/25-vision-language-models/outputs/skill-cmer-monitor.md:24-43,78-81; phases/04-computer-vision/25-vision-language-models/code/main.py:31-37. Monitor artifact assumes two 1-D torch.float32 vectors from a compatible independently aligned image-text encoder; it checks equal shape but does not enforce dimension, rank, finite values or score calibration. The main function normalizes on the last dimension and lacks equal-shape/confidence validation, so unintended broadcasting and non-finite inputs remain possible. DINOv3 requires an explicitly text-aligned setup, not an arbitrary image backbone.

### VLM-SYNTHETIC-NOT-END-TO-END

phases/04-computer-vision/25-vision-language-models/code/main.py:6-28,48-87; phases/04-computer-vision/25-vision-language-models/docs/en.md:207-219. ToyVLM trains a 2-linear-layer GELU projector and mean-pool linear classification head over synthetic tokens. It has no real image encoder, language decoder, tokenizer or generation. deepstack_features only torch.cat(..., dim=-1) and does not execute projection despite its docstring. Synthetic data are class-major; the 85% split leaves all 30 validation items in class 4, while training has 40 examples each of classes 0-3 and only 10 of class 4.

### VLM-SYNTHETIC-CMER

phases/04-computer-vision/25-vision-language-models/code/main.py:89-98. The CMER demo creates random vectors and fixed high confidence. Four random low-similarity candidates are labeled hallucinations in comments, but similarity threshold crossing is stochastic; the printed expected ~0.5 is not a test assertion or real hallucination measurement.

### VLM-MERGE-SKELETON

phases/04-computer-vision/25-vision-language-models/docs/en.md:140-178. MinimalVLM exists in the markdown only, not main.py. It requires a matching number of image placeholders per batch sample, clones text embeddings and replaces positions without changing sequence length. No general processor, variable-image packing, positional/RoPE policy or mask expansion is implemented. The vision encoder is assumed to return a tensor in the expected shape.

### VLM-PRODUCTION-DEPENDENCIES

phases/04-computer-vision/25-vision-language-models/docs/en.md:222-250; AGENTS.md:Dependencies. Use It imports transformers and PIL (Pillow), outside the Python allowlist; device_map auto may require Accelerate. It loads large external weights, expects plot.png, chooses bfloat16 and sends inputs to CUDA. The source neither pins package/model revisions nor provides an installation environment. Owner example uses Qwen3VLForConditionalGeneration; source uses AutoModelForVision2Seq whose availability/compatibility is version-sensitive and not tested here.

### VLM-COST-AND-DEPLOYMENT

phases/04-computer-vision/25-vision-language-models/docs/en.md:102,106; phases/04-computer-vision/25-vision-language-models/outputs/prompt-vlm-selector.md:22-28,44-56. Single-A100/H100 LoRA/QLoRA fit, 2-10 hour training, $100-$5,000 cost, sub-$0.002 serving recommendation, GPU thresholds and 50-60% spatial accuracy are workload/model/hardware/benchmark-dependent estimates without full assumptions. Active MoE parameter counts are compute counts, not total weight-memory sizes. Model-selector rules can conflict (GUI choice vs memory/edge/context constraints) and are heuristics, not a solver.

### VLM-PACKAGE-CONTRACT

phases/04-computer-vision/25-vision-language-models/quiz.json; phases/04-computer-vision/25-vision-language-models/code/main.py:1-3; phases/04-computer-vision/25-vision-language-models/docs/en.md:5. Target package has five quiz questions (2 pre, 0 check, 3 post), lacks top-level lesson/title fields, has no code/tests files and main.py starts directly with imports rather than required header. Type is Learn + Use, outside AGENTS listed enum. These are existing fixed-source deviations; no audit or tests were executed.

### VLM-UNTAGGED-FENCES

phases/04-computer-vision/25-vision-language-models/docs/en.md:94-96; phases/04-computer-vision/25-vision-language-models/outputs/skill-cmer-monitor.md:49-51; phases/04-computer-vision/25-vision-language-models/outputs/prompt-vlm-selector.md:32-48. AGENTS requires language tags, but these source fences are untagged. This is a source style-contract caveat, not evidence of loss or parser failure.

### DEPENDENCY-04-14

phases/04-computer-vision/14-vision-transformers/docs/en.md:7,128-130,Use It; phases/04-computer-vision/14-vision-transformers/code/main.py:1-85. ViT dependency implements patch Conv2d, CLS/position parameters, nn.MultiheadAttention pre-LN blocks and classifier. It is torch-based, not a manual attention kernel. Learned positional shape assumes constructor image size; arbitrary inference image size is not handled. Its figure ID is batchnorm-inference despite ViT content. Use It needs timm and downloads pretrained weights. Broader 2026 dominance and every-modern-model assertions were read but not comprehensively fact-checked.

### DEPENDENCY-04-18

phases/04-computer-vision/18-open-vocab-clip/docs/en.md:41,167,Use It; phases/04-computer-vision/18-open-vocab-clip/code/main.py:1-88. CLIP prerequisite is a two-MLP synthetic feature demo with normalized outputs and symmetric contrastive loss; it is not training a real ViT/text encoder. A finite random batch with learned logit scale need not equal log(N). Repeated synthetic class labels can be treated as in-batch negatives. Production example needs OpenCLIP/Pillow/model weights and exercise mentions FAISS, outside the allowlist. Source generalizations and stated CLIP-L/14 embedding dimension were not validated in this limited audit.

### DEPENDENCY-07-02

phases/07-transformers-deep-dive/02-self-attention-from-scratch/docs/en.md:6,129; phases/07-transformers-deep-dive/02-self-attention-from-scratch/code/main.rs; phases/07-transformers-deep-dive/02-self-attention-from-scratch/code/main.jl; phases/07-transformers-deep-dive/02-self-attention-from-scratch/code/self_attention.py. docs declares Python but the main.* files are Rust and Julia; Python lives at self_attention.py. All three implementations were read. Rust is single-head; Julia and Python also include multi-head output projection. None implements the optional causal mask exercise. Example weights at docs line 129 sum to 0.90, not approximately 1.00. Rust next_u32 shifts u64 state by 33 and uniform divides by full u32 range, yielding only roughly (0,0.5], so the claimed Box-Muller Gaussian is suspect by static derivation. Untagged/ASCII illustrations are source AGENTS caveats.

## Gate and lifecycle

S149 Voice Assistant is an isolated unpublished source-visual hold; it adds zero formal/pending lessons and leaves the historical seven blockers unchanged. Active next trio is S152/S150/S151 only. All shared files/history remain unchanged. Before authoring: final common155 identity closure, independent own3 scope/terms review, serialized fork-only support publication, one independent exact-byte readback, installation proof, then at most three fresh authors. Prerequisite Chinese acceptance is not the gate. Course acceptance still requires original strict, independent complete English/Chinese review, real GFM, remote final-byte readback and separately reported actual cumulative regression. No merge/deployment/CI change.

## Final local common support binding

Common155 SHA-256 `6ff499787041345bd952d34a1dd6b1e87c54ea832cc7624477f51ee69024d0a6`:147 terminology files +8 immutable controls. All155 current local payloads match pinned SHA256/Git blob/size/mode. Only selected lexical supports were semantically read; unrelated supports are identity-only. Verified formal163 commit `3ff9d167b03d0453a9334bb344d72fcbce72cf7f` retains actual162 separately. S148 is outside actual162 and begins the next acceptance-order cohort; S152/S150/S151 membership is not predetermined by author order. Preparation adds zero accepted lessons.
