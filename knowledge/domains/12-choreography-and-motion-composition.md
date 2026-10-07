# M12 — Choreography and Motion Composition

## Manifestasi yang ditampilkan

Gerakan beberapa objek, teks, kamera dan suara menjadi satu rangkaian yang terarah, dengan hierarchy, overlap, contrast dan continuity.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Composition is choreography/evaluation semantics, bukan sekadar banyak effects. Timeline/clip systems must preserve ownership, target identity and intended information sequence.

## Fondasi yang membentuk tampilan

Tracks, clips, layers, dependencies, sequencing, masks, additive poses, blending dan reactive orchestration. Choreography connects purpose to quantitative time/space controls.

## M12.01 — Tracks clips channels

Track updates property; clip groups tracks/time domain. Missing channels need base/default semantics.

**Model / mekanisme.** Value evaluator per channel with defined interpolation.

**Implementasi.** Schema validation and independent local times.

**Kegagalan tampilan.** Zero default wipes pose, units mismatched.

**Pemeriksaan.** Missing keys, duplicate time, endpoints.

## M12.02 — Sequencing dependencies

Relative starts and overlaps express relations. Depends-on meaning must explicit.

**Model / mekanisme.** Timeline graph with interval/dependency types.

**Implementasi.** Derive starts from rules; detect invalid cycles.

**Kegagalan tampilan.** Accidental deadlock, offsets stale after edits.

**Pemeriksaan.** Known chain/parallel fixtures and total duration.

## M12.03 — Staggering

Stagger based index, position, relation or data yields different pattern.

**Model / mekanisme.** start_i=start0+offset(i).

**Implementasi.** Preserve semantic order, adapt total reveal duration.

**Kegagalan tampilan.** Array reorder changes story, late items never finish.

**Pemeriksaan.** Reordered/long-content fixtures.

## M12.04 — Layering masks

Multiple layers affect channels/regions. Order and influence determine result.

**Model / mekanisme.** Base pose then explicit replace/additive/mask operations.

**Implementasi.** One composition owner combines contributions.

**Kegagalan tampilan.** Hover/physics/camera effects fight same property.

**Pemeriksaan.** Isolated then combined layers and zero/full weights.

## M12.05 — Blending spaces

Translation/color/rotation require appropriate space semantics.

**Model / mekanisme.** Weighted sums only when representation supports; quaternion-aware rotation.

**Implementasi.** Normalize weights under declared model.

**Kegagalan tampilan.** Shear from matrix averaging; incorrect color path.

**Pemeriksaan.** Identity/endpoints and intermediate constraints.

## M12.06 — Anticipation follow-through

Prepare/overlap/settle can make action legible, but context governs usefulness.

**Model / mekanisme.** Primary/secondary phases and delayed response.

**Implementasi.** Distinct envelopes with constraints.

**Kegagalan tampilan.** Decoration delays message; secondary hides labels.

**Pemeriksaan.** Playback clarity and response timing.

## M12.07 — Attention handoff

Group motion changes focal location/information.

**Model / mekanisme.** Source/target focus and handoff cue timeline.

**Implementasi.** Align connector/subject/text/audio roles.

**Kegagalan tampilan.** Unrelated simultaneous emphasis.

**Pemeriksaan.** Sequence versus focus plan review.

## M12.08 — Interruption and final state

Even offline authors can seek/change parameters; preview/live controls need cancellation ownership.

**Model / mekanisme.** Desired state separate evaluated presentation.

**Implementasi.** Version/generation guards for async completions.

**Kegagalan tampilan.** Wrong final state after repeat preview.

**Pemeriksaan.** Seek/reverse/restart and callback history.

## M12.09 — Orchestration and readability

Coordinating channels must leave content available. Busy complexity isn't evidence sophistication.

**Model / mekanisme.** Beat-level resource/information schedule.

**Implementasi.** Review maximum simultaneous relevant cues and quality/cost.

**Kegagalan tampilan.** All elements move continuously.

**Pemeriksaan.** Task/message review and bounded renderer workload.

## Penurunan mekanisme dan contoh terhitung

For n items, stagger s and unit duration d, sequence coverage is d+(n−1)s when starts aligned. Eight tokens atd=.4,s=.07 finish.89s. If scene allocates.6s, later tokens unfinished. Weighted simultaneous layers also need defined property-space composition: additive rotation is relative rotation, not component addition. A timeline that can render frames but has conflicting writers is not deterministic choreography.

## Kasus produksi

Flow diagram: title enters then holds; connectors establish relation; token moves; destination changes surface; audio accent marks state; closing label appears. Overlap is chosen to retain causal relation, not maximize activity. Code scene metadata includes primary/supporting purpose and interval boundaries.

## Memilih teknik dan trade-offs

Sequential staging for new information, parallel motion for meaningful shared change, stagger for ordered distribution. Choose replacement/additive layers by semantic intent. Avoid blanket same timing for different functions.

## Alur kerja operasional

Create beat/channel map; define ownership/base; implement clips/evaluation; derive intervals; add layers; inspect conflicts/readability; evaluate seek/history; revise choreography before polish.

## Verifikasi dan kriteria penguasaan

Dapat compose deterministic channels and explain each overlap/stagger. Human narrative/attention outcomes need appropriate evaluation.

## Cabang spesialis dalam cakupan

Nonlinear animation, blend trees, pose graphs, hierarchical timelines, additive motion, multi-agent choreography, procedural sequencing and rhythm systems.

## Hubungan antardomain

[M01](../../architecture/master-map.md#m01), [M03](../../architecture/master-map.md#m03), [M04](../../architecture/master-map.md#m04), [M06](../../architecture/master-map.md#m06), [M10](../../architecture/master-map.md#m10), [M11](../../architecture/master-map.md#m11), [M14](../../architecture/master-map.md#m14), [M15](../../architecture/master-map.md#m15), [M19](../../architecture/master-map.md#m19).

## Jalur sumber

[R02](../../evidence/sources.md#r02), [R21](../../evidence/sources.md#r21), [R25](../../evidence/sources.md#r25).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.

## Pendalaman produksi

[Channel ownership, sequence dan konflik](../deep-dives/12-channel-ownership-and-sequencing.md) — decision/model/counterexample yang melengkapi chapter ini.
