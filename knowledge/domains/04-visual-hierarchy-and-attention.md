# M04 — Visual Hierarchy and Attention

## Manifestasi yang ditampilkan

Penekanan dan perpindahan focus membuat penonton tahu bagian apa yang perlu dilihat ketika informasi muncul, bergerak atau berubah.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Attention plan bukan measured gaze. Salience dan attention dipengaruhi task, competing cues serta viewer; tidak ada cue guaranteed always menang.

## Fondasi yang membentuk tampilan

Fondasi mencakup grouping, contrast, temporal priority, motion salience dan information dependencies. Dalam coding, hierarchy menjadi scene roles, visibility, emphasis envelopes dan handoff windows.

## M04.01 — Priority roles

Primary, supporting dan contextual information menentukan what should stand out. Priority bisa berubah antarbeats.

**Model / mekanisme.** Time-dependent priority map authored by message needs.

**Implementasi.** Tag content roles and active focus windows in scene spec.

**Kegagalan tampilan.** Semua elemen diberi intensity sama.

**Pemeriksaan.** Message-role coverage dan actual frame/sequence review.

## M04.02 — Contrast cues

Size, luminance, color, detail dan position can emphasize. Combined cues may conflict.

**Model / mekanisme.** Compare relative contrast locally, with color/transfer assumptions.

**Implementasi.** Bounded emphasis parameters; keep information accessible without color alone.

**Kegagalan tampilan.** Accent bright tapi text unreadable; contrast inverted after grading.

**Pemeriksaan.** Actual output contrast and semantic alternative checks.

## M04.03 — Grouping dan separation

Proximity, similarity, alignment dan shared movement help organize information, context-dependent.

**Model / mekanisme.** Group relations linked to content semantics.

**Implementasi.** Animate group transforms to preserve intended relationship.

**Kegagalan tampilan.** Related items separate during motion; unrelated items appear one group.

**Pemeriksaan.** Before/after grouping interpretation and trajectories.

## M04.04 — Motion onset dan competition

New movement can draw attention but ongoing scene/activity affects response. More motion can distract rather than clarify.

**Model / mekanisme.** Schedule onset and hold of primary/supporting actions.

**Implementasi.** Limit competing cues as authored policy, not universal law.

**Kegagalan tampilan.** Background moves while core diagram changes unnoticed.

**Pemeriksaan.** Compare focus plan to full playback and task outcomes.

## M04.05 — Attention handoff

Viewer needs locate next relevant object before relation lost. Handoff can use movement, continuity, gaze/camera/sound cues.

**Model / mekanisme.** Record source focus, target focus, cue and overlap interval.

**Implementasi.** Cue target before/while source emphasis relaxes.

**Kegagalan tampilan.** Instant jump across frame; explanatory connection unclear.

**Pemeriksaan.** Review eye travel/task comprehension, actual gaze if measured.

## M04.06 — Reveal dan information availability

Information can be present but not yet readable due opacity, crop or unfinished text animation.

**Model / mekanisme.** Availability window differs object lifetime.

**Implementasi.** Track readable state after entry completion and before exit.

**Kegagalan tampilan.** Reading budget counted while letters still hidden.

**Pemeriksaan.** Availability times and actual text layout/playback.

## M04.07 — Clutter dan competing channels

Dense detail, sound and motion can exceed task capacity. Density metrics are diagnostics, not direct cognition measurement.

**Model / mekanisme.** Inventory simultaneous relevant/irrelevant cues by beat.

**Implementasi.** Reduce or stage cues based purpose and review.

**Kegagalan tampilan.** Distraction mistaken engagement.

**Pemeriksaan.** Task errors/time and editorial observation separately.

## M04.08 — Camera dan viewpoint emphasis

Framing/perspective changes can emphasize object while moving entire field. Large camera motion has comfort/legibility implications.

**Model / mekanisme.** Target framing and projected priority regions over time.

**Implementasi.** Keep essential labels stable/readable when camera movement unnecessary.

**Kegagalan tampilan.** Focus target leaves view; camera dominates content.

**Pemeriksaan.** Full camera path and viewing context review.

## M04.09 — Measurement dan interpretation

Technical visibility, AI review, eye-tracking and human comprehension are different evidence types.

**Model / mekanisme.** Predefine task/method/population/device and limitations.

**Implementasi.** Store observations separately from authored attention plan.

**Kegagalan tampilan.** Planned focus reported as measured gaze percentage.

**Pemeriksaan.** Evidence provenance, known competing cue cases, no invented outcomes.

## Penurunan mekanisme dan contoh terhitung

Contoh focus handoff A→B: highlight A while explaining input, reveal connector toward B, establish B, then de-emphasize A. Timing cue can be tested technically, but effective attention shift remains hypothesis. A 150ms overlap is a design example, not universal human threshold. If both areas pulse continuously, the contrast between primary/supporting states disappears.

## Kasus produksi

Kasus black-background explainer: use one accent to mark active relation; background marks static context; sound accent corresponds meaningful state change. Avoid equating black background with premium outcome automatically. Full playback should show whether emphasis helps story or competes with captions.

## Memilih teknik dan trade-offs

Use spatial focus when relationship location matters; use temporal staging when many facts need sequencing; use redundant cue when color alone insufficient. Do not apply maximum luminance/scale to every focal item.

## Alur kerja operasional

Define priority by beat; map relations/groups; choose cue envelopes; plan handoffs; preview competing cues; verify visibility; review comprehension/gaze only with appropriate actual evidence.

## Verifikasi dan kriteria penguasaan

Dapat membedakan planned attention dari observed attention, membuat handoff yang dapat dijelaskan, dan menemukan conflicting cues tanpa invented saliency scores.

## Cabang spesialis dalam cakupan

Eye movement research; task-driven attention; visual search; saliency models with limits; crossmodal cueing; change blindness; attention-aware annotation systems.

## Hubungan antardomain

[M01](../../architecture/master-map.md#m01), [M03](../../architecture/master-map.md#m03), [M06](../../architecture/master-map.md#m06), [M07](../../architecture/master-map.md#m07), [M10](../../architecture/master-map.md#m10), [M11](../../architecture/master-map.md#m11), [M12](../../architecture/master-map.md#m12), [M19](../../architecture/master-map.md#m19), [M20](../../architecture/master-map.md#m20).

## Jalur sumber

[R03](../../evidence/sources.md#r03), [R09](../../evidence/sources.md#r09), [R10](../../evidence/sources.md#r10).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.
