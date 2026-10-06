# S136-image-retrieval-metric English-first support scope

Support-only revision prepared 2026-10-05T08:40:00.217783+00:00; original preparation 2026-10-05T03:09:30.052444+00:00 is retained unchanged. PREAUTHOR CANDIDATE: not published or installed as own3. Stage identifier is not a PR number. Lesson 04-20: Image Retrieval & Metric Learning.

Only planned body target: i18n/zh/phases/04-computer-vision/20-image-retrieval-metric/docs/zh.md from phases/04-computer-vision/20-image-retrieval-metric/docs/en.md at fixed English 1bafaa88bb4668356791150bec3a6d7df38387eb. The full 5-file lesson package was read statically. Exact prerequisite English identities and fresh-read/prior-read-reuse status are recorded in DEPENDENCIES.json. Source prerequisite line: **Prerequisites:** Phase 4 Lesson 14 (ViT), Phase 4 Lesson 18 (CLIP). No prerequisite Chinese-acceptance gate.

Common142 =134 TERM +8 immutable controls, plus own3 =145 prospective support files. Existing common141 identity, ordering, roles and bytes are unchanged. S132 TERM is appended from its existing independent fixed-commit readback; its publication commit is ef718422ae608d453b890b35044d08e50e11a9dd. Original S130/S131/S133/S134/S135 pins remain unchanged. No upstream Chinese acceptance gate. Support set SHA256: e2ec32fb648670673320348a78367c722646dfd43eafa00c4e865ebdd1913ffc.

All author/composition/first-write/capture/record/revision/strict/full bilingual comparison/separate Chinese-read facts are pending. Times and hashes are null and revision lists empty. This is a support candidate, not a fabricated author calibration or review. Public support contains no local worktree or internal evidence path.

## Fixed English source risks

- docs/en.md Triplet loss; code/main.py: The formal formula uses squared L2 distances, while both implementation functions use unsquared pairwise distances. The displayed semi-hard mining snippet omits the upper margin bound that main.py includes; do not reconcile these through translation.
- docs/en.md/code/main.py semi_hard_negatives: Random batches need not contain another same-class example or a different class. All-masked argmax/argmin can select invalid positive/negative indices; neither implementation validates these cases. No runtime claims are established.
- outputs/skill-recall-at-k-runner.md: Self-match masking uses -inf but still admits masked entries when k exhausts available gallery items; evaluate() does not forward IDs. Filtering queries with labels absent from gallery changes the evaluation population. Empty encode_all inputs and invalid k have incomplete guards. scikit-learn is outside the repository allowlist; no install or run.
- docs/en.md metrics/indices; quiz.json; package: This lesson defines recall@K as any-correct-hit fraction, not multi-relevant-item recall. Cosine itself can be computed on non-unit vectors if divided by norms; raw dot product is the constrained shortcut. HNSW memory descriptions conflict, historical/date/ranking guarantees are unverified, quiz has five questions and no lesson/title, and tests are absent.
- docs/en.md figure; site/figures-cv2.js: metric-embedding is registered and depicts scripted class clusters, not measured learned embeddings or general instance retrieval. Mermaid/figure payload unchanged. No actual GFM/site visual acceptance; any future figure problem is scoped to this lesson.

Source risks remain distinct from translation defects. Preserve original code, numbers, math, URLs, model names and protected figures; do not silently rewrite the canonical lesson. Any source-figure blocker is local to this lesson and does not block the other two lanes.

No course code/import/tests, model, GPU/CPU training, API, network, downloads, installation, audio capture/cloning, GFM/browser, site, PDF or cumulative regression was run. Original strict controls are unchanged; no strict pass is claimed without a body. Formal144 and actual144 are historical verified snapshots, with this wave increment0. Actual publication commit/time and later author chronology must be recorded only when they happen.
