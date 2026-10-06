# S152-neural-audio-codecs source-only scope candidate

Fixed source: `1bafaa88bb4668356791150bec3a6d7df38387eb`. Source: [phases/06-speech-and-audio/13-neural-audio-codecs/docs/en.md](https://github.com/Activer007/ai-engineering-from-scratch/blob/1bafaa88bb4668356791150bec3a6d7df38387eb/phases/06-speech-and-audio/13-neural-audio-codecs/docs/en.md). SHA-256 `4fc76820d2dc2bafeda60c77018b05b52b4ee1febbdbe2a32b2ac76bcd4f3feb`; Git blob `541fcfeac0e4f0bd6ad0085572bcd251aea7cd30`.

Status: COMPLETE LOCAL OWN3 CANDIDATE, pending independent review, remote publication/readback and installation. Common155 now binds final accepted S146/S147/S148 chains at verified formal163; previous common152 remains exactly unchanged. Expected final author input is147 terminology+8 immutable controls+own3=158 support files. No Chinese lesson body, author role or first-write chronology exists.

## English-first inputs and boundaries

- Complete target package (5 files) and direct English prerequisites 06-02, 10-11, 05-19 with all main implementations were statically read. No whole transitive DAG is claimed.
- Fresh source-only tree contains5411 fixed English/non-i18n files; byte/blob/mode checked. No common support, own3, old Chinese body/record/review, original33 fixture, runtime install or author exists.
- Existing parent-approved target-only bare→text normalizations: b47 source lines56–58, b83 source lines132–134. Source and fence payload remain exact. Future author records each delta before initial capture/selfcheck. Immutable scanner d89de5eec36e10edcc391330d973632e3ceedb33fe679de3503dab52a7f6ece8 lines128–130 and existing rollout line86; no new exception.
- Preserve all code/math/identifiers/paths/URLs/numbers/units/metadata/table structure/Mermaid/figure/SVG. No source repair or fact modernization in translation.
- Source scanner and English identity assembly pass; this is not Chinese strict/review, GFM/site/mobile/PDF or course runtime verification.
- Mandatory canonical i18n documentation includes unrelated historical Chinese sample; source preparer exposure disclosed, not reused. Fresh authors use only English and finalized lexical supports.

## Source caveats

### CODEC-PACKAGE

Full five-file package. No quiz.json, code/tests, dependency manifest or Learning Objectives section. One stdlib Python demonstration, one SVG, one output skill and one empty notebook placeholder. Preserve package contract deviations; no tests or missing files created.

### CODEC-BITRATE

docs/en.md codec descriptions; outputs/skill-codec-picker.md. Source says EnCodec four codebooks at1.5kbps, but official 24k mapping is2 at1.5,4 at3 and8 at6. Source says Mimi8 books at4.4kbps and all books have1024 codes; official Mimi uses2048 entries and32 available books. Fixed-width arithmetic gives8×12.5×11=1100 bits/s, while32×12.5×11=4400. Keep all original values; these are external caveats, not silent corrections.

### CODEC-RVQ-UNIVERSAL

docs/en.md RVQ and semantic/acoustic split. RVQ/codebook sizes and semantic-acoustic separability are not universal across modern audio models. Source 1024^8=10^24 is an approximate order statement written with equality:1024^8 is2^80. The original arithmetic text remains. Reconstruction quality need not improve linearly with extra codebooks, and a semantic codebook is not guaranteed content-only.

### CODEC-ENCODEC-ARCH

docs/en.md EnCodec; assets/codec-comparison.svg. The source conv+transformer+conv architecture is inconsistent with checked EnCodec SEANet code using convolution and LSTM. An entropy-language model is separate from the waveform encoder. Preserve both original prose and SVG byte payload.

### CODEC-MIMI-API

docs/en.md Step3. loaders.get_mimi() omits the required filename argument in the checked current official implementation. The default loader selects8 codebooks from a32-book model; it requires weights for pretrained behavior. No installation/load/call occurred, and current mutable API evidence is a dated compatibility caveat.

### CODEC-RECONSTRUCTION-DEMO

code/main.py all functions. This is scalar1-D k-means residual quantization on the same1000 training values, not vector latents from a learned neural encoder/decoder. It retrains each residual book for each count and measures in-sample MSE only. No audio files, PESQ, ViSQOL, listening tests, trained semantic teacher, streaming or LM is exercised.50fps bitrate is an assumed display conversion.

### CODEC-EDGE-CASES

code/main.py learn_codebook/rvq_encode/rvq_decode/mse. Empty values yield a zero codebook, but empty MSE divides by zero. Zero codebook size fails for nonempty input; lengths and index validity are unchecked. Zip can truncate pairs; decoder length mismatch can fail. Empty k-means clusters retain old centroids. No claim of correctness on these inputs or runtime validation.

### CODEC-QUALITY-TABLE

docs/en.md reconstruction table and frame-rate claims. PESQ/ViSQOL table lacks dataset, sample-rate preprocessing and evaluation protocol. Unequal bitrate rows do not prove Opus universally wins per bit.75Hz EnCodec-24k is later called50Hz in Pitfalls; preserve inconsistency. DAC/SNAC superlatives, destruction/inaudibility claims and256M generation-in-milliseconds are unvalidated source assertions.

### CODEC-OUTPUT-ARITHMETIC

outputs/skill-codec-picker.md. The refusal example computes86×8×10 as5504; arithmetic is6880. Preserve original5504. LM-only codec-token generation still needs decoding to waveform; decoder options are ambiguous. Blanket codec refusals and voice-cloning prescriptions are source heuristics, not validated operational policy or permission.

### CODEC-DEPENDENCIES

docs/en.md Build It and Exercises. encodec, torchaudio, moshi and model-weight downloads are not the local stdlib example and are outside the AGENTS Python allowlist except torch. compute_deltas is unused. The input is torch.randn noise, not speech. No package install/import, audio playback, external inference, GPU, download, benchmark or exercise run.

### CODEC-FORMAT-ASSET

docs/en.md:56-58,132-134; codec-comparison.svg; rvq-codec-cascade. Both bare fences replay losslessly; only preexisting bare→text target normalization is eligible. SVG was rendered locally with Inkscape at1760×920 and inspected: title and all four columns/bottom text are readable with this renderer. This is not actual GitHub GFM, browser/site or interaction acceptance. The figure widget is a conceptual animation and does not run RVQ.

### CODEC-PREREQUISITES

06-02,10-11,05-19 docs and all main.*. All direct docs and five main implementations read statically.06-02 uses DFT, magnitude-mel and non-integrated chirp phase;10-11 NumPy/Rust arithmetic demos are not actual GPTQ/AWQ, asymmetric constant input loses its nonzero value, Python INT4 is stored int32 rather than packed, GB labels useGiB math, Rust qmin differs from Python;05-19 Python/TypeScript demos use ASCII word extraction and do not provide universal byte fallback, TS ranked scanning is not near-linear. No need to translate prerequisite Chinese first; no transitive DAG or code execution claim.

## Gate and lifecycle

S149 Voice Assistant is an isolated unpublished source-visual hold; it adds zero formal/pending lessons and leaves the historical seven blockers unchanged. Active next trio is S152/S150/S151 only. All shared files/history remain unchanged. Before authoring: final common155 identity closure, independent own3 scope/terms review, serialized fork-only support publication, one independent exact-byte readback, installation proof, then at most three fresh authors. Prerequisite Chinese acceptance is not the gate. Course acceptance still requires original strict, independent complete English/Chinese review, real GFM, remote final-byte readback and separately reported actual cumulative regression. No merge/deployment/CI change.

## Final local common support binding

Common155 SHA-256 `6ff499787041345bd952d34a1dd6b1e87c54ea832cc7624477f51ee69024d0a6`:147 terminology files +8 immutable controls. All155 current local payloads match pinned SHA256/Git blob/size/mode. Only selected lexical supports were semantically read; unrelated supports are identity-only. Verified formal163 commit `3ff9d167b03d0453a9334bb344d72fcbce72cf7f` retains actual162 separately. S148 is outside actual162 and begins the next acceptance-order cohort; S152/S150/S151 membership is not predetermined by author order. Preparation adds zero accepted lessons.
