# M09 — Space Depth and Perspective

## Manifestasi yang ditampilkan

Objek terasa berlapis, dekat/jauh, besar/kecil atau berada dalam ruang tertentu melalui projection, occlusion, parallax dan transformations.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Depth cues dapat berupa illustration2D atau spatial scene3D. Perspective perception bukan proof physical dimensions; frame/unit/projection assumptions must clear.

## Fondasi yang membentuk tampilan

Linear algebra, affine/projective geometry, local/world/view/clip/screen frames dan camera conventions. Geometry creation M05, shot decisions M14, rendered image M21.

## M09.01 — Reference frames

Same vector meaningful only in declared basis/unit.

**Model / mekanisme.** p_world=T_world_local p_local.

**Implementasi.** Tag transforms; compose in renderer convention.

**Kegagalan tampilan.** Mixed y-up/y-down, wrong handedness.

**Pemeriksaan.** Origin/basis vectors and round-trip inverse.

## M09.02 — Transform order

Translation/rotation/scale do not generally commute. Parent transforms alter child motion.

**Model / mekanisme.** Column convention composition applied right-to-left.

**Implementasi.** Keep hierarchy explicit and avoid duplicate transforms.

**Kegagalan tampilan.** Pivot drift, scaled translation unexpected.

**Pemeriksaan.** Known parent/child scenarios.

## M09.03 — Projection

Orthographic/perspective map space differently. Near/far, aspect and FOV determine appearance.

**Model / mekanisme.** Perspective divide by w after clip transform.

**Implementasi.** Use documented camera matrices and guard invalid w.

**Kegagalan tampilan.** Object disappears at near plane, distorted aspect.

**Pemeriksaan.** Known projected geometry and resizing.

## M09.04 — Depth cues

Occlusion, scale, shadows and parallax can reinforce/invalidate spatial relation.

**Model / mekanisme.** Planned cues should agree or deliberate ambiguity.

**Implementasi.** Coordinate scene layers/material/camera.

**Kegagalan tampilan.** Shadow says floating while overlap says touching.

**Pemeriksaan.** Full-sequence cue consistency review.

## M09.05 — Parallax

Different depths show different projected displacement under camera translation.

**Model / mekanisme.** For simplified pinhole x_screen=fX/Z; translation changes X/Z.

**Implementasi.** Animate actual camera/planes or labeled2D approximation.

**Kegagalan tampilan.** Fake parallax reversed or camera-independent.

**Pemeriksaan.** Known depth planes and motion direction.

## M09.06 — Scale perception

Physical size, projection size and authoring scale separate.

**Model / mekanisme.** Screen extent depends geometry/camera depth/projection.

**Implementasi.** Preserve units and label data-derived size encodings.

**Kegagalan tampilan.** Perspective size misread as data magnitude.

**Pemeriksaan.** Reference objects, projection checks, meaning review.

## M09.07 — Normals and directions

Directions don't translate; normals need inverse transpose under nonuniform scale.

**Model / mekanisme.** Homogeneous point w=1, direction w=0.

**Implementasi.** Transform attributes by proper rule.

**Kegagalan tampilan.** Lighting or paths shift wrongly.

**Pemeriksaan.** Perpendicularity and known directions.

## M09.08 — Spatial continuity

Cross-shot orientation can persist through anchors, axes or identifiers.

**Model / mekanisme.** Map world/scene changes explicitly.

**Implementasi.** Align transitions using chosen common reference.

**Kegagalan tampilan.** Viewer loses direction/subject relation.

**Pemeriksaan.** Before/after relationship and trajectory review.

## M09.09 — Spatial constraints

Distance/attachment/occlusion limits keep scene meaningful.

**Model / mekanisme.** Constraints C(state)=0 or inequalities with residual.

**Implementasi.** Evaluate bounded solve/query; report infeasible geometry.

**Kegagalan tampilan.** Deformation stretched to hide impossible layout.

**Pemeriksaan.** Residual, crop and crossing fixtures.

## Penurunan mekanisme dan contoh terhitung

Simplified pinhole with focal scale f=500px: object X=.2m at Z=2m projects50px from center. Same X atZ=4m projects25px. Translating camera changes relative X and can create parallax. This relation assumes camera-aligned coordinates and no distortion; output screen origin/aspect must also specified. It does not identify real distance from a single image without calibration/scale.

## Kasus produksi

Layered diagram: foreground token, middle diagram and background grid. Choose orthographic if data sizes must remain comparable; use perspective for intentional spatial storytelling. Parent camera movement requires rechecking labels/occlusions throughout path.

## Memilih teknik dan trade-offs

Use2D depth cues for illustration when coherent;3D representation when view changes require persistent geometry. Orthographic simplifies size comparison; perspective adds view-dependent scale and requires explanatory context.

## Alur kerja operasional

Define frames/unit/projection; verify basis; build hierarchy; plan depth cues; evaluate camera path; check projected bounds/continuity; render native output.

## Verifikasi dan kriteria penguasaan

Dapat audit transforms/projection and distinguish world geometry from screen appearance. Perceived depth requires actual context review.

## Cabang spesialis dalam cakupan

Quaternions, Lie groups, camera calibration, projective geometry, stereo, SDF scenes, camera-aware constraints and motion-aware spatial layouts.

## Hubungan antardomain

[M03](../../architecture/master-map.md#m03), [M05](../../architecture/master-map.md#m05), [M08](../../architecture/master-map.md#m08), [M10](../../architecture/master-map.md#m10), [M13](../../architecture/master-map.md#m13), [M14](../../architecture/master-map.md#m14), [M18](../../architecture/master-map.md#m18), [M21](../../architecture/master-map.md#m21).

## Jalur sumber

[R06](../../evidence/sources.md#r06), [R11](../../evidence/sources.md#r11), [R20](../../evidence/sources.md#r20).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.

## Pendalaman produksi

[Camera space, frustum dan clipping](../deep-dives/09-camera-space-frustum-and-clipping.md) — decision/model/counterexample yang melengkapi chapter ini.
