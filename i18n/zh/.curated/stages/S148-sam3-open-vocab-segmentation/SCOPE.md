# S148 SAM 3 and open-vocabulary segmentation source-only scope candidate

Fixed English: `1bafaa88bb4668356791150bec3a6d7df38387eb`. Lesson `04-24`: `phases/04-computer-vision/24-sam3-open-vocab-segmentation`. Local preparation adds **0 reviewed drafts**. The coordinator owns DEPENDENCIES.json, common152/formal160 bindings, support publication, installation and author assignment. No Chinese lesson body, record or review is written here.

## Translation scope and complete package inventory

Future target: `i18n/zh/phases/04-computer-vision/24-sam3-open-vocab-segmentation/docs/zh.md`. Only eligible prose in the fixed `docs/en.md` is the future translation target. The complete five-file package was read statically: English doc, implementation, quiz and both output templates. There are no same-lesson tests, assets, notebook placeholders or dependency manifests. The outputs are contextual source material, not instructions to run models or log user data and not additional translation targets.

| Package file | Bytes | Git blob | SHA-256 | Read coverage |
|---|---:|---|---|---|
| `phases/04-computer-vision/24-sam3-open-vocab-segmentation/code/main.py` | 3854 | `6ecb44cf24124e792bd6f4076a27e32a12dcc175` | `6cc9481d21e6e14111d6319a649c61c1085d7ab03faac512daeea6ee80b66b7b` | {"kind": "full"} |
| `phases/04-computer-vision/24-sam3-open-vocab-segmentation/docs/en.md` | 13789 | `357c72837176273755348be861422ab36ed7c0fa` | `56e317c037a7b9fb92c05d8738f795c30b11e5cc3e082127984a1ca25a2bd040` | {"kind": "full"} |
| `phases/04-computer-vision/24-sam3-open-vocab-segmentation/outputs/prompt-open-vocab-stack-picker.md` | 2270 | `8ab7fd052ef28d09821720b60a5052c0904a2318` | `08eca5ed262ed3e00e90f7b955d49f22f14a3c4d4e7ceba0fdc6fa32de2901a4` | {"kind": "full"} |
| `phases/04-computer-vision/24-sam3-open-vocab-segmentation/outputs/skill-concept-prompt-designer.md` | 3733 | `1934d4513969dfe6d253651e5be350a2f151a15d` | `04a9f53abd00de9d4f8015d56e4bbcc3016d473cc3c858cadf45b3db26965e43` | {"kind": "full"} |
| `phases/04-computer-vision/24-sam3-open-vocab-segmentation/quiz.json` | 4277 | `5cadfdcc9fc729b510379db5d3e890b5389a9723` | `2b1bb30724d527d328dc821b96ec978a04e557154aaf7029b5947247f34d130f` | {"kind": "full"} |

## Direct prerequisite inventory

Full English docs and full main implementations of 04-07 U-Net, 04-08 Mask R-CNN and 04-18 CLIP were read. Those are the actual declared prerequisites. Their output/quiz files and transitive dependencies were not fully read. No full DAG claim is made. The existing S97/04-07 Dice table blocker remains unchanged and does not gate English prerequisite understanding or unrelated drafting.

| Prerequisite file | Bytes | Git blob | SHA-256 | Read coverage |
|---|---:|---|---|---|
| `phases/04-computer-vision/07-semantic-segmentation-unet/docs/en.md` | 18557 | `6739f33a49e8a26e66f6dd8311c403e06fad9309` | `7c1b00723a204bfc263ea5c3c3219b04b1549a7d2fc7e3297a4a6611609e54f1` | {"kind": "full"} |
| `phases/04-computer-vision/07-semantic-segmentation-unet/code/main.py` | 6231 | `5e8c1c53b131ba5fe2ea306ceb59c3271173a993` | `e0a359a17a0028a1c682fcc0fbc8ad1dfbfe1f9f979527e781178958f4e129ce` | {"kind": "full"} |
| `phases/04-computer-vision/08-instance-segmentation-mask-rcnn/docs/en.md` | 14358 | `2516968ed3638bf89924cdf5a5ac842307cfae9c` | `b7ced123dcc47406affd5cc13916ffb6954f8417a29d8b99526c61ec97a4168b` | {"kind": "full"} |
| `phases/04-computer-vision/08-instance-segmentation-mask-rcnn/code/main.py` | 3912 | `a5cfbeb322856b346b08dd6fa703678afda8fca9` | `481de1fd2bbb9443d5dc936eac44193b55a4d0b097cb26b4e198260825b6393f` | {"kind": "full"} |
| `phases/04-computer-vision/18-open-vocab-clip/docs/en.md` | 10019 | `9157c0b5304a40983b117011863e860ea782cf6d` | `7c62736dc19a39acdbec6499254e943c83a8c14023a1ed0979462fc8a3fbebe1` | {"kind": "full"} |
| `phases/04-computer-vision/18-open-vocab-clip/code/main.py` | 3063 | `601eab462fb95089d1967d015c1a507991bf4c78` | `0db17b4067ed0c3daa83e9e32548892bbf075ef5b44e6956467ca352b3ecb450` | {"kind": "full"} |

## Repository, figure and cross-file context

| Context file | Bytes | Git blob | SHA-256 | Read coverage |
|---|---:|---|---|---|
| `AGENTS.md` | 13617 | `3be7cf810ba6879a068d6da4756a399eab129740` | `24a1cb3e111107b1a3d922f550776e7573396bc9d0b651b33b1e2cc1d7e1bcc2` | {"kind": "full"} |
| `CONTRIBUTING.md` | 4933 | `3a561b62567ad298277adcebfbd65853e3e7ccf0` | `fd1d4f0b904f6ec83b2ad1c0290fe537dcc4ebfd3f1bf1d88148dd383059c166` | {"kind": "full"} |
| `docs/i18n.md` | 14861 | `5eea45dea0c125705ed158db3f0c731b4ef68ace` | `5d0e89958e6c90c3f4f65d8f0369800d350b4a3ceaf51275e2c41f23c6f4aa56` | {"kind": "full"} |
| `README.md` | 110543 | `fa3bdfe6f7161c0e8176a288443c7e528b0fb9be` | `e65435a0190b0d5d88019b92838a387c1e142699178c3d8881c86de2283804d7` | {"kind": "selected_ranges", "line_ranges": [[560, 598]]} |
| `ROADMAP.md` | 53970 | `2bfe92922350584f648109bd35997676bc059574` | `715bc5177f4eb6e0671a1497eff871a2048aab3f6706d732d3fc3ab53c29a419` | {"kind": "selected_ranges", "line_ranges": [[96, 129]]} |
| `site/figures-cv3.js` | 23622 | `8d3cafd99ef58660d02eabc2ccd2283dde7d1bb3` | `ac0ba50f88ff721c28f528e8d21f48d48d84c1a138dda0c754199a7e57023740` | {"kind": "selected_ranges", "line_ranges": [[1, 44], [257, 300], [331, 343]]} |
| `site/lesson.html` | 249289 | `e0dab75fa0746e01a6618ff5b507975a70967334` | `03a79431a160d84c30793da3433d565b236db586ba53083b45b07e304d15757e` | {"kind": "selected_ranges", "line_ranges": [[2772, 2781], [4298, 4335]]} |
| `phases/04-computer-vision/16-vision-pipeline-capstone/docs/en.md` | 15362 | `6d955080ee09edddd304d381bedb931551347b10` | `8f658578957bb2c27e48dd1926960ebc448d5030d5c21e3dd8398443689f9b73` | {"kind": "selected_ranges", "line_ranges": [[48, 69], [98, 127]]} |
| `phases/04-computer-vision/16-vision-pipeline-capstone/code/main.py` | 6966 | `f5ccce255b32cd33a38f7154e9252bfadeb995be` | `e13cb6033c4db5c6d6f0d41514b66633d45901102d1a8f63cd5065e1db7c6c99` | {"kind": "selected_ranges", "line_ranges": [[1, 33]]} |

AGENTS.md and CONTRIBUTING.md were read completely. Local ROLLOUT-PLAN.md was read completely, SHA-256 `8aa60a30dd31a7ae579a064a28bedeb324727d8f4d0fa2b26c111fac9b6fb397`, 12613 bytes; v1.3 operative gates supersede its historical scheduling examples. docs/i18n.md was read as repository guidance and incidentally exposed its unrelated Chinese quality sample, which was not used as translation memory. No old Chinese lesson body, translation record, review, old cache or original33 fixture was read or used. Generic run/install/push directions in repository guidance are not authorized execution in this task.

04-16 is only an explicit contract cross-reference: selected doc ranges and the implementation's data types were read. It is not added as a declared prerequisite. Its field names differ from this lesson's dataclass and must not be silently normalized.

## Source structure and figures

The fixed body has 296 lines, 141 lossless blocks, 64 nonempty prose blocks, 1435 approximate English whitespace units outside protected fences/math/inline code, 9 H2 and 14 H3 headings. This is a planning measurement, not tokenizer or effort telemetry.

- Seven tagged fences: one Mermaid, one `figure`, five Python. No bare body fence or display-math block. All payloads remain exact; no new text tag is needed in the translation body. The output templates have three bare fences, but are read-only contextual files.
- One three-column key-term table has eight body rows. The immutable lossless scanner found no source table/fence content-loss blocker here; this is not a strict translation pass or actual GitHub rendering acceptance.
- Preserve the figure payload `cv3-open-vocab`, the entire Mermaid, code, inline identifiers, model/paper names, numbers/units, paths, URLs and source comparisons. Do not add absent headings or repair source claims.
- The complete `openVocab` widget function was read at provider lines 257-298, along with helpers and registration. It uses a hard-coded scene and SMIL animation, not segmentation inference. No generated manifest was read or treated as evidence; no static lesson asset exists, so future_support_assets is empty.
- GitHub GFM, original-site interaction, mobile and PDF acceptance remain pending/unverified; static inspection cannot decide diagram label visibility.

## Source correctness and runtime caveats

The following are fixed-source caveats for faithful translation and independent review. They are not authority to edit English, code, outputs, quiz, controls or assets, and are not new generic checker exceptions.

### R01: Hugging Face API mismatch

Location: `docs/en.md:207-231`.

The fixed snippet calls Sam3Processor.set_text_prompt, post_process_masks and outputs.masks/boxes/scores. Current official Transformers examples instead provide text in processor(...), then post_process_instance_segmentation(outputs, threshold, mask_threshold, target_sizes); raw masks use pred_masks. Meta native Sam3Processor has a different set_text_prompt(state=..., prompt=...) interface. The lesson mixes these surfaces and leaves pil_image undefined. Preserve all code; no API/runtime success is claimed.

References: [https://huggingface.co/docs/transformers/model_doc/sam3](https://huggingface.co/docs/transformers/model_doc/sam3), [https://github.com/facebookresearch/sam3](https://github.com/facebookresearch/sam3)

### R02: Ultralytics text interface mismatch

Location: `docs/en.md:252-261`.

Current official Ultralytics documentation requires SAM3SemanticPredictor for text/exemplar PCS. The basic SAM("sam3.pt") interface is for visual point/box/mask prompts, so the source prompts= text call is not the documented text path. Preserve the fixed snippet and treat it as unverified reference code. The reviewed page also separates SAM 3.1 image support from unavailable Object Multiplex video support in that wrapper.

References: [https://docs.ultralytics.com/models/sam-3/](https://docs.ultralytics.com/models/sam-3/)

### R03: prompt splitting differs across surfaces

Location: `docs/en.md:117-130; code/main.py:17-24; outputs/skill-concept-prompt-designer.md`.

The doc helper notices comma/semicolon/and/or/& but only replaces "and " and splits commas, returning early. Semicolon/or/& can remain unsplit; substring matching can damage words. The main implementation replaces several literal separators first, but is case-sensitive and quote-unaware and returns [""] for empty/whitespace-only input. It does not implement concrete-noun extraction, filler removal, context disambiguation, max_concepts or quoted-string preservation from the skill. No function was run; these are static code distinctions.

### R04: stub behavior and instance identities

Location: `docs/en.md:177-205; code/main.py:66-105`.

The real SAM3OpenVocabSeg subclass is proposed, not shipped. StubOpenVocabSeg returns the same two rectangular instances with scores 0.89/0.74 for every concept and image content, without presence decisions, learned recognition, tracking, NMS or cross-concept deduplication. IDs 0 and 1 restart for every concept; run_multi_concept concatenates them, so IDs are not globally unique across the merged output. Doc stub RLE strings describe 350 and 340 flattened pixels irrespective of image dimensions, whereas main.py constructs full-size rectangle masks.

### R05: RLE format and validation limits

Location: `docs/en.md:145-165; code/main.py:27-57`.

This is a custom semicolon-separated value-by-count string in NumPy default flatten order, not a demonstrated COCO RLE adapter. The doc encoder indexes flat[0] before checking emptiness; main.py handles empty masks. Neither enforces binary input. The decoder does not validate values, positive counts or total length; short runs leave zeros and excessive slices can truncate rather than establish a valid shape contract. RLE size depends on spatial run structure and can expand alternating masks. No roundtrip test or compression measurement ran.

### R06: unified output and pipeline-contract overstatement

Location: `docs/en.md:86-105,134-136,167-170; 04-16 docs/en.md:48-69,98-127 and code/main.py:1-33`.

The source says YOLO-World supplies boxes only, then claims all three models return boxes+labels+scores+masks+IDs without an explicit three-model list at that point. Do not strengthen this ambiguous antecedent into universal native-schema equality: detection-only output lacks masks and temporal tracking identity. An adapter can normalize a chosen representation. ConceptDetection also substitutes concept/instance_id for the Phase 4 Lesson 16 Detection.class_id field and is a plain dataclass rather than that Pydantic contract. They share geometry/score/RLE ideas, not exact drop-in field equality. 04-16 was read only at its contract passages, not as a new full prerequisite.

### R07: SAM-MI method and metrics scope

Location: `docs/en.md:93-101,287; outputs/prompt-open-vocab-stack-picker.md`.

The SAM-MI paper describes SAM-mask guidance for a pixel-text cost map with low/high-frequency branches, which is more specific than the lesson description of a decoder receiving precomputed masks. Its 96.0% is reduction in point prompts on ADE20K-150, not a universal measured decoder-call reduction. The 1.6x comparison is a particular Grounded-SAM/MESS efficiency setup. These do not establish edge real-time performance. Preserve the lesson claims without silently repairing them.

References: [https://arxiv.org/html/2511.20027v1](https://arxiv.org/html/2511.20027v1)

### R08: Object Multiplex simplification

Location: `docs/en.md:73-75; quiz.json`.

The official March 27, 2026 release describes fixed-capacity object buckets processed jointly. The lesson simplifies this to one shared memory with per-instance queries. Release notes report mixed video benchmark changes, despite the headline faster without sacrificing accuracy. Preserve source dates/numbers/qualifiers and do not turn the simplification into an exact implementation description or a guarantee for every object count/hardware.

References: [https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md](https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md)

### R09: concept and generation boundaries

Location: `docs/en.md:12,21-23,52-67,131; 04-18 docs/en.md`.

SAM 2 itself must remain distinct from Grounded SAM 2, which chains a detector and a segmenter. PCS operates on concept prompts; all matches is the task objective, not perfect recall. Anything describable in natural language and the universal production replacement wording are stronger than short noun-phrase concept segmentation. SAM3-I addresses richer instruction semantics. One forward pass concerns the stated prompt/image path; video tracking spans frames and multiple concept queries need looping/batching. The prerequisite CLIP source also has broad SAM text-prompt claims; do not import them as a contradiction repair.

References: [https://arxiv.org/abs/2511.16719](https://arxiv.org/abs/2511.16719), [https://arxiv.org/abs/2512.04585](https://arxiv.org/abs/2512.04585)

### R10: benchmarks and broad dated recommendations

Location: `docs/en.md:69-71,77-91,233-251; quiz.json`.

The official SAM 3 summary reports 4M concepts, 270K SA-Co concepts, 75-80% of human performance and gains on its defined tasks. These are reported benchmark claims, not local measurements or universal object recognition accuracy. Source statements about 2026 defaults, equal common-concept accuracy, usually net-neutral latency, 30-60 fps on modest GPUs, CVAT integration, medical suitability and fine-tuning gains were not broadly validated. Preserve them as source claims, without endorsing hardware-independent latency or deployment safety.

References: [https://arxiv.org/abs/2511.16719](https://arxiv.org/abs/2511.16719), [https://github.com/facebookresearch/sam3](https://github.com/facebookresearch/sam3)

### R11: license access and output selector scope

Location: `docs/en.md:79-83,241,250; outputs/prompt-open-vocab-stack-picker.md`.

The public SAM 3 model page shows a gated contact-information sharing/access flow. A gate is distinct from a license restriction and does not establish commercial suitability or healthcare readiness. The selector labels other detectors Apache/permissive and proposes precision/browser/edge choices without verified version-specific compatibility or legal review. Top-down first-match policy and its later domain-specific preference can point to different choices. No agreement was accepted, identity/contact data sent, model accessed or legal clearance concluded.

References: [https://huggingface.co/facebook/sam3](https://huggingface.co/facebook/sam3)

### R12: shipped prompt-design recommendations are not implemented

Location: `outputs/skill-concept-prompt-designer.md`.

Lowercase benefit, plural hint, an absolute eight-word limit and preserved quoted conjunctions are source recommendations, not measured or implemented behavior here. The example changing "thing near the door" to "door" changes which entity is selected. The logging rule may capture personal utterances and is read-only source content, not authorization to collect or transmit logs. No downstream prompt-design evaluator or noun parser is shipped.

### R13: quiz and repository contract

Location: `quiz.json; code/main.py; AGENTS.md`.

There are five quiz questions: two pre and three post, with no check items and no lesson/title top-level fields. Root guidance calls for six, 1 pre+3 check+2 post, and those fields. No tests directory, dependency manifest, notebook or lesson asset is present in the fixed five-file package. main.py has no required 4-6-line source/spec header. These are source contract caveats; nothing is deleted, relabeled, generated or silently repaired, and no repository audit pass is claimed.

### R14: prerequisite English context and known blocker

Location: `04-07 docs/en.md and code/main.py; 04-08 docs/en.md and code/main.py; 04-18 docs/en.md and code/main.py`.

All three declared prerequisite docs and full main implementations were read. U-Net doc synthetic colors vary independently of class while main.py fixes circle/square colors; missing-class IoU handling and divisibility wording are also simplified. Mask R-CNN prose says four losses while its formula has five; its main may download pretrained weights. CLIP main is a synthetic shared-prototype two-tower demo, not real image/text tokenization. These programs were never imported or run. S97/04-07 raw-pipe Dice-table translation blocker remains unchanged and does not prevent English prerequisite reading; no full transitive DAG or prerequisite Chinese acceptance is claimed.

### R15: figure and protected source-format surface

Location: `docs/en.md:29-50,107-109,276-287; site/figures-cv3.js:257-298`.

The original body has one Mermaid diagram, one figure fence and five Python fences, all tagged. The key-term table has eight rows with three columns; a lossless static scan found no content-loss table/fence blocker in this lesson. This is not actual GFM acceptance. The site widget draws fixed oranges/apple/box with animated rings and IDs, without inference, and the figure fence is not itself a GitHub live widget. No static lesson asset is present or needs copying. Website, mobile, PDF and diagram rendering remain untested.

### R16: runtime and release gates

Location: `this local source preparation; ROLLOUT-PLAN.md v1.3`.

Local source readiness is not authoring, own3 publication/readback/installation, strict acceptance, independent language review, actual GFM inspection, final remote readback or cumulative regression. No lesson command/import/test, NumPy or torch runtime, model/GPU/provider API, checkpoint/data download, installation, remote mutation, merge, deployment or count increment occurred. Original controls and seven historical blockers stay unchanged.

## Narrow external checks

Public primary sources were read only at the stated passages on 2026-10-06 UTC. These checks distinguish fixed lesson assertions from current documentation; they do not update the lesson or constitute a full literature/API/license audit. No model, test, GPU, account, agreement, download or installation was used.

- [https://arxiv.org/abs/2511.16719](https://arxiv.org/abs/2511.16719): abstract and version metadata only. Confirms PCS, 4M labels and detector/tracker shared backbone with presence head; no full paper reproduction.
- [https://github.com/facebookresearch/sam3](https://github.com/facebookresearch/sam3): README summary, release announcement and basic native image/video usage passages. Reported 270K/75-80% benchmark context, 2026-03-27 release and native set_text_prompt interface. No install/auth/download performed.
- [https://huggingface.co/docs/transformers/model_doc/sam3](https://huggingface.co/docs/transformers/model_doc/sam3): text/batched/multi-prompt usage and output examples; set_text_prompt/post_process_masks exact-name searches. Documents processor(text=...) and post_process_instance_segmentation; returned raw mask name differs from fixed lesson.
- [https://docs.ultralytics.com/models/sam-3/](https://docs.ultralytics.com/models/sam-3/): text/image/video predictor examples and 3.1 support notice. SAM3SemanticPredictor for text PCS; basic SAM is visual-prompt interface. Object Multiplex video not supported in reviewed wrapper notice.
- [https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md](https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md): release introduction, Object Multiplex description and benchmark summary/table only. Fixed-capacity buckets and mixed benchmark changes qualify simplified one-memory/no-accuracy-loss source wording.
- [https://arxiv.org/html/2511.20027v1](https://arxiv.org/html/2511.20027v1): abstract; introduction metric/method passages; method overview; targeted 96.0%, low-frequency and 1.6 searches including Table 11. 96.0% concerns point prompts on ADE20K-150; 1.6x is specific Grounded-SAM efficiency comparison; mask guidance enters pixel-text maps.
- [https://arxiv.org/abs/2512.04585](https://arxiv.org/abs/2512.04585): title, abstract and version metadata only. SAM3-I is an instruction-following extension; richer instruction reasoning differs from noun-phrase concepts. Fixed source link title is retained.
- [https://huggingface.co/facebook/sam3](https://huggingface.co/facebook/sam3): public gate, license label, native example and Transformers text example. Contact-information sharing gate is visible; terms/access approval and legal suitability were not assessed or accepted.

## Terminology calibration

Full semantic reads: core TERMINOLOGY.md; S94/S97/S100/S118/S121/S124/S130/S139; appended S143/S144/S145. ADDENDUM lines 1-42 and S122 open/closed-vocabulary row at line 13 targeted. All 144 TERM payload identities verified and all searched for named relevant terms; other historical glossaries not fully reread. Historical lifecycle prose is not current acceptance evidence.

Common152 identity: SHA-256 `adb98cb4c54c97f8485605d3d90e10fbe80209705ffcae1545170c1c10c39beb`. Receipt identity: `4d8b3ece2ce2abb6455304075636495184be45bad78d9da5844955b666e8e447`. The complete common149 prefix is preserved in order and metadata; appended terms are accepted S143/S144/S145, read from independent-readback payloads. Common152 consists of 144 TERM files and eight unchanged controls. Prospective own3 yields 155 support items. The parent prepares DEPENDENCIES.json. This worker has not installed any support into the fresh author tree and has not created an author proposal/calibration receipt.

## Preserved seven historical blockers

Only index160 active_stages support/provenance metadata was read, SHA-256 `c7ed29d1c863b93fac3bcd985258709aac971f20b15be5f02738c230edbf690e`. No underlying Chinese bodies, records or review reports were read. All seven remain uncounted and untouched:

- S61-scaling-distributed / 10-05: Third protected 3D Mermaid has three overlapping/obscured nested explanation labels in both English and Chinese; no payload repair authorized
- S66-instruction-tuning-sft / 10-06: Protected source Mermaid group subtitles (pre-trained) and (after SFT) are covered by first nodes in both English and Chinese after refresh/expanded/zoom/pan; no payload repair authorized
- S79-mdps-states-actions-rewards / 09-01: Complete content Draft PR and language review verified; full actual GFM and final acceptance gates pending; uncounted
- S95-machine-translation / 05-11: Source mt-pipeline.svg later target-ids rectangle paints over tail of beam search. Source asset byte-identical; no repair applied; original protection remains and no new checker exception.
- S97-semantic-segmentation-unet / 04-07: Fixed English Dice table has six unescaped pipes; actual GFM drops formula/description. Original strict protects table signature; no repair applied and no extra exception or math/source rewrite.
- S107-multilingual-nlp / 05-18: Source multilingual.svg black dots cover parts of cat(en),gato(es),dog(en) labels. Body/code/table/end visually pass, whole-figure text gate fails. Authorized native zoom call executed but no visible zoom; not pending permission. No repair applied; original asset protection remains, no new checker exception.
- S119-long-context-evaluation / 05-28: Protected original long-context-eval.svg paints first-column opaque rectangles over depth0.1/0.3/0.5/0.7/0.9 suffixes. Three real screenshots plus source coordinates show loss of row depth values. Source/targetSVG byte-identical; no repair or checker exception. Later body not visually inspected.

## Counts and next gates

Coordinator baseline: formal160 at `5c848f294ac8437ee3186e4aab3c9b969691698a`, latest actually validated cumulative set actual159. This source-only worker does not claim fresh remote verification. Next actual162 comprises S145 plus the next two accepted lessons; this third new lane joins later unless acceptance order changes. Source readiness contributes no accepted lesson and no batch-regression pass.

Own3 publication, independent exact-byte readback and installation remain pending. A fresh author's proposal/calibration, first-write/capture, target/record, original strict, independent full English-Chinese technical comparison and Chinese read-through, real GitHub GFM inspection, final changed-byte readback and cumulative regression all remain separate gates. Existing S07/S19 exact exceptions are not broadened. No course runtime/import/tests, model/GPU/provider API, download/install, remote write, merge, deploy or CI change occurred. Preserve every prior artifact.
