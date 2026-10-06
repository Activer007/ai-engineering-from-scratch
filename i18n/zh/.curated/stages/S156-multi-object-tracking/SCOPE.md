# S156-multi-object-tracking source-only scope candidate

Fixed English `1bafaa88bb4668356791150bec3a6d7df38387eb`; source [phases/04-computer-vision/27-multi-object-tracking/docs/en.md](https://github.com/Activer007/ai-engineering-from-scratch/blob/1bafaa88bb4668356791150bec3a6d7df38387eb/phases/04-computer-vision/27-multi-object-tracking/docs/en.md). Git blob `bc6530301ed8db6012ddea7578a77eb19d604fea`, SHA-256 `c94305127796ce8683c9625ebc1897373e86de8c1da82580815f656988c09e7c`.

Status: COMPLETE LOCAL OWN3 CANDIDATE, pending independent review, serial remote support publication/readback and installation. Common158 = 150 terminology files + 8 immutable controls; own3 gives161 prospective supports. No author assignment, Chinese lesson prose, course execution or formal/pending count increment.

## English-first coverage

Complete target package: 5 files. Direct prerequisites: 04-06, 04-08, 04-24, with 6 English docs/main files fully read. Detailed fixed pins and semantic line ranges are in DEPENDENCIES.json. Only direct prerequisite closure is claimed; preceding Chinese acceptance is not an author gate.

Fresh author tree has exactly5411 fixed non-i18n files from the Git archive, with all bytes, Git blobs, Git modes and POSIX modes verified. All12 baseline i18n files excluded. No supports, Chinese bodies, records, reviews or original33 fixtures installed. Common lexical identity verification does not claim semantic rereading of all158 supports.

Source scanner join and identity assembly are lossless. English self-comparison is not Chinese strict acceptance. Bare-fence eligibility: none. The only eligible later label normalization is the unchanged original bare-to-text rule; record it before first capture and protect payload bytes.

Preserve every code/math/number/metadata/API/model/identifier/path/URL/Mermaid/figure/SVG surface. Source caveats remain outside Chinese prose; do not modernize or silently repair them.

## Source caveats

### MOT-PACKAGE

complete five-file package. No code/tests, dependency manifest, code header/source citation or SVG asset. Quiz has5 questions (2pre+3post), no check stage, lesson/title keys absent and conspicuously long correct options. Existing course contract gaps remain. The only diagrams are Mermaid and cv3-track-assoc figure fallback.

### MOT-NOT-FROM-SCRATCH

Learning Objectives and code/main.py. IoU is implemented directly but assignment calls scipy.optimize.linear_sum_assignment, not a from-scratch Hungarian algorithm. scipy is outside the AGENTS Python allowlist. Only NumPy geometry/synthetic trajectories are present: no detector, Kalman filter, appearance model, neural tracker or real video evaluation. No imports/tests/run/install occurred.

### MOT-FAMILY-HISTORY

Concept tracker families and Kalman paragraph. StrongSORT improves DeepSORT and OC-SORT modifies SORT; calling both ByteTrack descendants is inaccurate. SAM2 was released July29,2024, not introduced in2026. Claims that every tracker follows the depicted loop or every classical tracker uses Kalman are overbroad. Quoted1–5frame recovery and ~1000object speed are workload-dependent, not validated guarantees.

### MOT-ASSIGNMENT

Hungarian section; docs Step2; main SimpleTracker.step. SciPy current implementation is modified Jonker-Volgenant, although it solves the intended rectangular linear assignment. Main builds one IoU matrix, replaces below-threshold costs by1e6, rejects cost>=1, creates unmatched tracks and prunes after matching. Expired tracks can therefore be revived before pruning; unmatched surviving tracks are returned with stale boxes. No min-hit confirmation, motion prediction, class filtering or ReID. matched_track is unused. Nonmonotonic frame values, malformed/NaN/reversed boxes and threshold bounds lack validation.

### MOT-BYTETRACK

ByteTrack key idea. Official implementation performs low-confidence second association, but its second-stage IoU-distance threshold0.5 is not a universal looser threshold than first stage; first pass also fuses detection scores and uses configurable match_thresh. The0.5detector cutoff and claimed best/default status are contextual, not universal.

### MOT-SAM-API-MEMORY

SAM2, Object Multiplex and Use It. SAM2 native prompts are points/boxes/masks, not native arbitrary text; open-vocabulary use requires another model/prompt path. Current Meta uses init_state/add_new_points_or_box/propagate_in_video; Transformers uses inference sessions and model.propagate_in_video_iterator, not processor.track(). Object Multiplex releaseMarch27,2026 is verified but official mechanism groups instances in fixed-capacity buckets, not literally a single unlimited bank. Reported~7x at128objects/H100 and mixed benchmark scores do not establish universal sublinear complexity or deployment default. Attention memory is bounded/configurable; source grows-unbounded framing is simplified.

### MOT-METRICS

Three metrics; main count_id_switches. MOTA formula counts FN,FP,ID switches with equal unit weights; wording weighted-by-type may mislead. IDF1 requires global identity matching; the helper is only greedy per-GT argmax IoU>0.5 switch counting, can reuse one prediction for multiple GT, ignores unmatched objects/FP/FN, retains assignments across gaps and zip truncates unequal videos. It computes neither IDF1 nor MOTA nor HOTA. HOTA balances detection/association/localization across thresholds; domain advice and community-standard claims are not guarantees.

### MOT-SYNTHETIC

docs Step3 versus main synthetic_frames/main. Docs use20frames and velocities[-5,5]; main defaults25frames and[-4,4], adds ground truth/dropouts and clipping. H/W unused in docs, but main clips only some endpoints and can generate reversed boxes after objects leave the image. No real camera motion, appearance, detector noise or measured performance. Zero ID switches and short-occlusion recovery are exercises, not established results.

### MOT-PRODUCTION-CLAIMS

Use It and prompt-tracker-picker. Official Ultralytics still supports explicit tracker=bytetrack.yaml but fetched current docs list TrackTrack as default and ReID off by default for BoT-SORT. Source default, production superiority, named package availability and performance prescriptions remain dated claims. No model download, video access, external detector or package validation occurred.

### MOT-OUTPUT-PICKER

outputs/prompt-tracker-picker.md. num_objects is a category yet rules use numeric-style >=many/>=crowd. First-match rule6 at>=30fps can shadow rule7>=60fps for general-purpose scenes. particles appears in rules but not inputs. High occlusion does not make appearance universally essential. Recommendations need measured workload suitability; outputs are unexecuted instructional artifacts, not permission to conduct surveillance.

### MOT-OUTPUT-EVALUATOR

outputs/skill-mot-evaluator.md. Text output is MOT-like but benchmark loaders also need dataset layout, seqinfo, class/visibility/ignore-region conventions and configuration; generic prediction-style ground-truth columns are not sufficient for every TrackEval MOTChallenge loader. Source provides only py-motmetrics sketch and no actual TrackEval invocation or saved results. Formats/zero-versus-one coordinate conventions and metric units require version-specific checking. Current py-motmetrics also documents HOTA, so the source strict library split is dated.

### MOT-PREREQUISITES

full06/08/24 English docs and main implementations. 06-YOLO docs encode offsets without logit while main fixes inversion; docs NMS complexity ignores repeated pair comparisons; main NMS is class-agnostic and grid-anchor collisions overwrite.08-MaskRCNN source says four losses but equation has five, one-sample RoIAlign test is not all torchvision modes/borders, main can download pretrained weights and catches exceptions; not run.24-SAM3 main is deterministic geometry stub, split/RLE differ from prose, instance IDs restart per concept and custom RLE is not standard COCO encoding; source API and benchmark caveats retained. Only direct docs/main semantic closure is claimed, no whole transitive DAG.

### MOT-FORMAT-FIGURE

Mermaid; figure cv3-track-assoc; table. All target body fences tagged; all scanned body table rows have header-compatible columns. Raw<br/> stays within immutable Mermaid payload. Manual prose angle-tag review and readonly CJK-bold diagnostic are mandatory for future Chinese; original strict and actual GitHub GFM remain mandatory. Figure provider animates three predetermined correspondences and a diagonal illustrative cost matrix; it does not compute IoU/Hungarian. No source SVG exists, so no SVG pixel pass is claimed.

## Required later gates

- Read-only CJK-bold adjacency risk diagnostic using unchanged prior packaging/check_bold_adjacency.py, followed by manual context review, before any future body publication. Risk scan never replaces original strict or GFM.
- Manual raw angle-tag Markdown review outside protected code, especially literal model/control tags and comparisons; no automatic global replacement, no new checker exception.
- Original local strict and source-target protected payload/structure checks, independent complete EN-to-ZH semantic review and separate full Chinese read.
- Actual fixed-target GitHub GFM inspection of every table, code, math, long line, Mermaid/figure and exact SVG; source local PNG is not GFM/site/mobile/PDF acceptance.
- One independent final remote byte/readback gate and separately scoped actual cumulative regression after accepted lessons.

Only the coordinator may write remotely, fork-only, with at least60seconds between publication groups. No support installation before independent immutable byte/tree/ref readback. Fresh author then supplies own actual terminology proposal/calibration and first-write chronology. Frozen support pending/null states are historical snapshots, not fabricated future commits.

## Baseline and held sources

Verified formal166 at `34efa23be08970d25291d057b108949ddceef7e2`; actual165 PASS remains separately scoped. S151/04-25 is the first member of future actual168. The next two accepted active courses complete that cohort in acceptance order; the remaining new course starts a later cohort. Preparation cannot infer future acceptance or actual168 execution. S149/06-12 remains held. S155/04-26 remains reserved and held for source-table content loss incompatible with original strict; approved active replacement is S156/04-27. Neither hold changes historical seven blocker rows. Source-only S155 files prepared before hold are retained inactive.

Common158 SHA-256 `a4ed394c03650b70a6e48172186d37c5bc255dc887753c058be7a73bc5a78875` retains exact prior155 objects/metadata/order and appends only accepted S150/S152/S151 terminology, including format-repair descendant proofs. Required repository i18n documentation exposed an unrelated old Chinese sample; it is not translation memory.
