# S79：马尔可夫决策过程、状态、动作与奖励

Author activated 2026-10-03 UTC by coordinator. This is a local, English-first draft authoring scope, not independent acceptance, release, or a change to formal course counts.

## Fixed inputs and deliverables

- Source commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`.
- Source: `phases/09-reinforcement-learning/01-mdps-states-actions-rewards/docs/en.md` (192 lines; SHA256 `f6054bf219d82d9195bbfc01f132528a7727733157a0188d948725f9f3fd5f97`).
- Full implementation read: `phases/09-reinforcement-learning/01-mdps-states-actions-rewards/code/main.py` (113 lines; SHA256 `dc612127f115ea9b702c784cfd94da81d5b3e5d259e5ae740dca2c366a4e2da5`); its only import is Python stdlib `random`, with no local imports.
- Target: `i18n/zh/phases/09-reinforcement-learning/01-mdps-states-actions-rewards/docs/zh.md`.
- Draft record: `i18n/zh/.curated/lessons/09-01/translation.json`.
- Only referenced relative asset: `phases/09-reinforcement-learning/01-mdps-states-actions-rewards/assets/mdp.svg`, copied unchanged to the parallel `i18n/zh/` path and bound in the record (SHA256 `f0062f08f574e0f5bee5ad1e273b4af6f0a4cad3817134f9e7a535b8ac83dfb8`).
- Author evidence stays under `stage79_evidence/`; shared final report is `stage79_author_report.json` at the shared workspace root.

## Prerequisites and immutable support

The assigned source requires 01-06 Probability & Distributions and 02-01 ML Taxonomy. The coordinator verified both in the actual accepted set before this wave; no same-wave or pending lesson is used. Relevant accepted terminology: S09 Probability and S22 ML overview. Core glossary, addendum, and all 83 exact support path/commit/SHA256 tuples in `DEPENDENCIES.json` were checked against working bytes and immutable Git objects at author start. The dependency manifest SHA256 is `8f10bcbaa0f7e26109e074bade03da8474e7584c00e815af549714a136a5bea7`. Pending S61/S66/S73 are excluded. The three fixed 00-04 production fixtures are for the unchanged original 33 tests only, never translation memory or new dependencies.

## Translation and source-risk boundaries

Translate the complete English lesson afresh; do not consult old Chinese prose, caches, upstream PR452/457, another author draft, or a translation service. Preserve source code/comments/prompts, formulas, figure payload, paths, numbers, links and metadata keys/immutable values. Only an originally unlabelled fence may gain `text`. Use canonical headings and the stage terminology. Preserve source flaws in translation; record them separately, especially the distinction between undiscounted capped rollout return and discounted value, boundary self-loops in the stochastic down/right policy, and implementation/domain caveats in the source.

## Authorized bounded runtime

Only the offline stdlib 4×4 GridWorld, fixed seeds and external 30-second timeout. After complete source read, the unchanged main entry may run two policies × 5000 rollouts, each capped 200 steps, plus four evaluations capped 2000 iterations. Small tests use 2–20 rollouts capped 60 steps and deterministic terminal/reward/Bellman/distribution/gamma/tolerance/cap checks. No Gymnasium install, network, environment API, real trades/actions, credentials, datasets, models, GPU or RL training. Do not run the 10,000-episode exercise or the unbounded documentation loop.

## Gates and ownership

Original strict and unchanged original33 tests, two new out-of-repository exact-byte replays, asset identity, final 83-pin verification, complete block-bound author technical comparison, then a separate complete Chinese reading are author gates. They do not stand in for another person's complete independent review or actual exact-commit GitHub GFM screenshots and visible diagram/link inspection. Course-site anchors/mobile/figure interactivity, hosted CI, translated-book build and user release approval remain separate. Only the coordinator may commit/publish/update PRs or the formal index; no support_commit is claimed before a real read-back value is supplied. No author-created independent review.json.
