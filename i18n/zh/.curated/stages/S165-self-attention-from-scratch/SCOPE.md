# S165-self-attention-from-scratch source-only support candidate

Fixed English: `1bafaa88bb4668356791150bec3a6d7df38387eb`.
Lesson: `07-02`, `phases/07-transformers-deep-dive/02-self-attention-from-scratch/docs/en.md`.
Source Git blob: `fdd602ab55cc270fff890327f07715327bee6129`.
Source SHA-256: `54a8d6da2e4f1ea0b0b43a1bf09be1b3c41e2d5b974cef459b0ab8ea0af18177`.

## Current boundary

Local support-only own3 preparation after clean172, not permission to author lesson prose. Common164 contains 156 terminology files plus eight immutable controls; this stage adds three supports for a future installed total of 167. Publication, independent readback, author-tree installation, separate terminology calibration and coordinator prose clearance remain pending. No lesson translation, translation.json, review record, capture, new completion or regression result exists here. The frozen support file does not self-reference its eventual publication commit; subsequent receipts remain external.

Clean172 is commit `61a301b1d2f5321f8bd03e25fda3ed76946d099a`, formally reviewed 172 with actual cumulative 171. Those numbers and 39 missing historical original receipts remain unchanged. No missing receipt is reconstructed. 07-01 (S164) remains source-held; the other existing holds 06-12, 04-26, 14-09 and 14-10 remain.

## Source coverage

The complete six-file 07-02 package was read: English, Python, Rust, Julia, output prompt and quiz. The full 05-09 and 05-10 English lessons and Phase 3 overview were read as context. No full Phase 3 or transitive prerequisite-package review is claimed. Relevant Attention, Self-Attention and Cross-Attention glossary entries and the two lesson figure implementations were read; unrelated glossary and figure entries were only fingerprinted. Output prompt instructions were inspected as curriculum content, not executed.

Fresh author tree was extracted using local git archive at the fixed English commit, excluding every i18n file. All remaining source file bytes were verified against fixed Git blobs. Source context and the original33 test-only fixtures are outside the 167-support count. Common candidates were read externally for lexical reconciliation; they are not yet installed in the author tree.

## Source caveats, preserved without corrections or exceptions

- Explicit prerequisite says Phase 5 Lesson 10 (Sequence-to-Sequence), but fixed tree has Sequence-to-Sequence at 05-09 and Attention Mechanism at 05-10. Preserve wording and flag mismatch; no source correction.
- Printed softmax weights [0.52,0.09,0.07,0.14,0.08] sum to 0.90, despite sums-to-approximately-1.0 label; repeated weighted-sum example uses them. Do not silently normalize.
- Model projections are trainable in principle, but demonstrations randomly initialize weights and embeddings with no training; resulting heatmaps are not evidence of learned syntax/coreference.
- Learning objectives include multi-head implementation and causal masking. Prose build steps implement single-head attention; multi-head and masking are exercises. Python and Julia files add multi-head; Rust file is single-head. None of these files implements causal masking.
- Languages metadata says Python despite main.rs and main.jl being present; Python entry point is self_attention.py, not main.py. No code/tests directory. Quiz has five questions, no lesson/title keys, and stages 2 pre + 3 post.
- Documentation example uses d_model=8, dk=dv=4; shipped Python/Rust/Julia demos use 16,8,8. Seeds and generators differ across languages, so no byte/numeric equivalence should be inferred.
- K.T implementation is two-dimensional only; do not imply batched attention support. Softmax subtract-max improves stability but does not define all-masked -infinity rows.
- Scaling explanation omits independence/unit-variance assumptions; dot-product standard deviation grows as sqrt(dk), not deterministic magnitude. Preserve source nuance without introducing a guarantee.
- ASCII diagrams and output prompt request conflict with current AGENTS Mermaid/SVG-only diagram rule. Existing source must remain intact; do not replace figures or waive controls.
- Rust next_u32 shifts u64 right by 33, giving at most 31 random bits, then uniform divides by u32::MAX; Box-Muller inputs cover only about half the unit interval. Static source concern, not runtime-tested.

- The attention-matrix site figure uses hard-coded synthetic affinities, including an it-to-cat relationship. It does not demonstrate learned coreference. The scaling figure uses fixed illustrative logits; its claims do not prove stability for every input dimension or distribution.
- Quiz statements about equal single-head/multi-head computation and quadratic memory are source assertions, not measured implementation results. No benchmark or runtime verification was performed.

## Protected payload and later rendering work

Eight bare fence openings occur at English lines 31, 50, 70, 85, 114, 124, 138 and 162. Adding only a `text` language tag later is the permitted GFM change; payloads, source math, numeric examples, comments, identifiers and diagrams remain exact. One Mermaid block and two figure blocks remain unchanged. No diagram replacement, numeric normalization, English repair or generic checker exception is allowed. Figure IDs are attention-matrix and softmax-attention-scaling; no lesson-local assets directory exists.

No lesson code, compiler, model, GPU, package installer or API was run. No source-control replay, target strict check, independent semantic review, GFM browser inspection, website/mobile/PDF acceptance, remote publication or CI pass is claimed. Actions remain disabled and zero checks would mean unrun. Authoring can begin only after the coordinator verifies all 167 published/readback supports installed and separately approves terminology calibration.
