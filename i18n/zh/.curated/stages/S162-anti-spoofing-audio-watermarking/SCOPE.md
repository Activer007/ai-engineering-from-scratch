# S162 anti-spoofing and audio watermarking source-only scope

Fixed English `1bafaa88bb4668356791150bec3a6d7df38387eb`; lesson 06-16. Target source `phases/06-speech-and-audio/16-anti-spoofing-audio-watermarking/docs/en.md`, Git blob `e1aadece22ba5fc103ae9ac75d02cd1ed2de4fd3`, SHA-256 `312eab13609b920ae76f6c7e413cfc8abfdbf761b87328fcd7af4edd9a7b944a`.

Status: local own3 proposal only. No Chinese lesson prose, translation record, capture, strict pass, independent review or publication is claimed. Author lane is assigned for support preparation; first Chinese lesson write is blocked until coordinator confirms all167 supports published, independently read back and installed, plus terminology calibration acceptance.

## Source coverage

Fresh author tree was made by git archive at the fixed source, excluding all i18n. All5411 non-i18n baseline files were hash-verified; all12 baseline i18n files excluded. Full target five-file package (docs, code, SVG, output and empty placeholder) read statically. Direct prerequisite06-06 and06-08 full five-file packages read, including docs, code, SVG and outputs; no quiz/tests present. AGENTS fully read. Relevant English glossary content-provenance/data-provenance ranges and site audioWatermark function/registry read; broad shared files only fingerprinted outside listed ranges. No transitive DAG or full-repository semantic review claimed.

Target source has196 lines, five language-tagged fences (one figure, four python), two tables and one linked SVG. Dossier regex inventory is not original strict acceptance. No bare fence normalization is needed. Source bytes, code/comments, math, numeric quantities, model/API identifiers, links, SVG and figure payload are protected. Do not repair source or add checker exceptions.

## Source caveats

- Fixed historical source contains 2026 production mandates and SOTA/performance statements. No external fact verification was requested or performed; translate as source claims, not verified current advice.
- AudioSeal speed differs inside en.md: 485x realtime and 1000x faster than WavMark in concept; key terms says 485x faster than WavMark. Code repeats the latter. Preserve and escalate, do not harmonize silently.
- 0.42% ASVspoof 2019 LA EER is attributed to NeXt-TDNN + SSL in en.md, while code also attributes it to AASIST. ASVspoof benchmark scores are not demonstrated by the toy program.
- Toy detector score is high-band energy and synthetic clips explicitly add a 6 kHz component, but FAR/FRR sweep treats high scores as acceptance of real speech. The standalone en.md EER function leaves score polarity implicit. No execution or correctness certification.
- Toy watermark adds +/-0.0005 at selected samples; detector simply checks sample sign without a clean reference. This does not establish payload recovery or real AudioSeal robustness.
- 16-bit payload cannot directly hold arbitrary user ID, model ID, and timestamp jointly without an unspecified encoding/allocation. Both prose and shipped skill imply these identifiers.
- SVG checklist says 30-day retention; output skill says 7+ years and example 7 years. No jurisdictional or legal verification. These are conflicting fixed-source claims, not user instructions.
- AudioSeal example depends on external audioseal and undefined load_wav; production integration has undefined helpers and identifiers. Do not install or execute. audioseal is outside AGENTS dependency allowlist.
- No quiz.json and no code/tests directory in this fixed lesson. Toy code imports math/random only. Do not invent compliance with repository lesson contract.
- Source has categorical universal pitch-shift/removal and C2PA-stripping claims; retain caveats and do not upgrade these to universal verified guarantees.
- AudioSeal attribution and dates, AASIST/RawNet2 architecture and SOTA claims, ASVspoof population/attack counts, WaveVerify July2025 and AudioMarkBench universal-removal claims are fixed historical claims, not externally verified facts. No external references were fetched in this support-only task.
- The detector probability return comment and exact AudioSeal API behavior have not been checked against a versioned installed package. Preserve code instead of turning the example into an executable guarantee.
- The discrete EER sweep checks observed thresholds only, returns an average at the smallest FAR/FRR gap, and has no empty-list guard or interpolation. It is not a proof of a continuous crossover. High-band score polarity mismatch is separate.
- magnitude_spectrum excludes the final exact-length frame via range endpoint and produces an all-zero spectrum for a single n_fft-sized clip; this is static inspection, not an executed result. The main header lacks the prescribed explicit source path.
- The linked site figure is illustrative fixed animation, not measured watermark recovery. It depicts payload surviving MP3/crop/resampling and must not be promoted to an experiment.
- Prerequisite06-06 doc EER initializes equal FA/FR and updates only on strictly smaller difference, so its best tuple can never update; main.py differs. Its cosine-normalization warning is not generally valid for exact cosine; do not repair the prerequisite or carry its claim into a new guarantee.
- Prerequisite06-08 has legal requirements, licensing, model availability, quality-threshold and retention claims not independently verified here; its toy mixes vectors and uses a clean-reference watermark detector, not production cloning. Its prose WER versus code CER table differs. These are context caveats, not target-source repairs.

## Visual and release boundaries

Existing fixed-source SVG pixel preflight may be reused only at identical source and screenshot hashes. The prior actual browser inspection found all31 labels readable; the last checklist baseline is tight to the bottom border. This is inherited spacing, not established content loss. English SVG labels remain unlocalized. No new capture was taken. The site-specific figure is not native GFM interactivity. Actual complete immutable target GitHub GFM, independent bilingual review and separate Chinese read, original strict, link/structure checks, CJK-bold diagnostic with manual adjudication, and raw-angle review remain future gates. Website, PDF, mobile and CI are not passed.

## Support and history

Common164 =156 terminology files +8 immutable controls, with exact inherited pin metadata/order. Own SCOPE.md, TERMINOLOGY.md and DEPENDENCIES.json add3, for167 supports. Source/context/assets and original33 test fixtures are separate, not extra support files. The common manifest preserves39 missing historical original receipt limitations; recovered public bindings do not reconstruct those originals. Historical pending rows, old source/visual holds and earlier validation facts are unchanged.

Clean172 is confirmed at `61a301b1d2f5321f8bd03e25fda3ed76946d099a`: formal172, actual cumulative171. S159/04-28 is not thereby covered by actual171. No future regression, formal increment, support publication/readback/installation, calibration pass or first-write timestamp is fabricated. Frozen publication nulls are to remain in this support snapshot; future events belong in separate receipts rather than circular self-hashes.

No remote writes, source repairs, model imports, demos, tests, GPU/API/network model calls, installs, training or audio generation occurred. Future coordinator publication is fork-only, serial, draft-only, no merge/deploy or CI enablement; rollout-plan v1.3 and original controls remain in force.
