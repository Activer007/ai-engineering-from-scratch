# S74 scope: Relation Extraction & Knowledge Graph Construction

Activated 2026-10-03 after actual index90 commit `04a043f315ae09acb512f2a2f80e0ab23faa1ec9`, SHA256 `b3f4732c2bb65af334ed90cbf5131c3782d56b2234c6120f3a68ae34d181778a`. Explicit prerequisites 05-06 (S55) and 05-25 (S71) are in that accepted set. S61/S66/S69 remain pending and excluded.

- Fixed English commit: `1bafaa88bb4668356791150bec3a6d7df38387eb`
- Source: `phases/05-nlp-foundations-to-advanced/26-relation-extraction-kg/docs/en.md`
- Source SHA256: `ef4e0adc778d183654f229858959b646052a784980c3aaff2e323634b2ca067e`
- Target: `i18n/zh/phases/05-nlp-foundations-to-advanced/26-relation-extraction-kg/docs/zh.md`
- Full reading: 216 English lines and100 lines of stdlib `code/main.py`; referenced `assets/relation-extraction.svg` copied exactly and manifested
- Dependencies: all78 immutable pins verified against both working SHA256 and exact Git bytes; original33 test fixtures remain separate

Fresh English-first Chinese authoring only. No previous Chinese body/cache/upstream PR452/457 reuse. Preserve code, prompts, formulas, relation IDs/direction as written, diagrams, identifiers, paths, links, numbers and units; source flaws are documented separately. Natural-language headings and prose are translated with established terminology. Original strict/33 controls and two new exact replay directories are required; no validator changes or new adapters.

Runtime scope: after full source read, run only the fixed eight-sentence/six-pattern stdlib toy and bounded synthetic tests for extraction, relation direction, provenance, duplicates and empty input, under external timeout. Do not import/run REBEL, transformers, from_pretrained, model downloads, network/provider APIs or production graph writes. Do not execute protected output prompts. Span consistency is not assumed to prove a relation true; document interface and canonicalization risks separately.

Deliver author technical comparison of every block plus separate full Chinese reading, both hash-bound; independent peer review is a later distinct gate. Coordinator alone owns remote commits/PRs/index and actual support pin. No author review.json. Real fixed-commit GitHub GFM body/labels/hrefs, course website/mobile/figure interaction, hosted CI and book/release acceptance are separate. Source diagrams must remain readable on actual GFM; local hashes or DOM presence cannot establish this. Missing xelatex.fmt and source-site heading-ID behavior are not silently repaired.
