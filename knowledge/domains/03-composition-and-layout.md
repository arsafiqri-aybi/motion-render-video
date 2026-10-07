# M03 — Composition and Layout

## Manifestasi yang ditampilkan

Posisi, ukuran, alignment dan empty space membentuk susunan frame yang terasa terarah selama objek, teks dan kamera bergerak.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Composition dievaluasi sepanjang waktu dan aspect ratios; static balance tidak otomatis menjaga moving frame. Human preference harus dipisah dari geometric checks.

## Fondasi yang membentuk tampilan

Geometry, coordinate systems, projected bounds, grouping dan constraints memberikan dasar. Layout menyediakan reference pose; motion mengubah pose/presentation. Unit normalized, pixels dan world coordinates harus dijelaskan.

## M03.01 — Frame coordinates dan safe regions

Frame, action-safe/title-safe/project-specific overlays berbeda. Safe margin adalah production constraint sesuai target, bukan satu persentase universal.

**Model / mekanisme.** Bounds normalized or pixels; declare origin/y direction and crop.

**Implementasi.** Keep layout regions per target format, inspect actual projection.

**Kegagalan tampilan.** Essential text outside output crop; coordinate convention inverted.

**Pemeriksaan.** Corner/reference points and platform overlay inspection.

## M03.02 — Alignment grids dan rhythm

Alignment menciptakan hubungan yang dapat dilihat. Grid membantu consistency tetapi optical alignment dapat membutuhkan offsets.

**Model / mekanisme.** Baselines, columns, spacing units and anchor constraints.

**Implementasi.** Solve reference layout first; store meaningful anchors.

**Kegagalan tampilan.** Objects aligned numerical center but visually uneven.

**Pemeriksaan.** Compare geometric bounds and optical/editorial review.

## M03.03 — Balance weight dan negative space

Visual weight depends size/contrast/detail/motion, bukan mass fisik. Empty space memberi separation dan room for path.

**Model / mekanisme.** Define focal area and surrounding clearance; measure occupancy descriptively.

**Implementasi.** Compute bounding/occupied regions as diagnostics, not preference score.

**Kegagalan tampilan.** Frame overload; path crosses title.

**Pemeriksaan.** Keyframes plus trajectories for collisions/overlaps.

## M03.04 — Scale proportion dan relationships

Relative size can express category or importance. Data-driven sizes perlu truthful mappings.

**Model / mekanisme.** Explicit scale ratios/normalization and data encoding.

**Implementasi.** Separate display scale from physical/dataset units.

**Kegagalan tampilan.** Decorative scaling distorts data interpretation.

**Pemeriksaan.** Mapping checks and meaning review.

## M03.05 — Anchors pivots dan transforms

Pivot determines perceived attachment saat rotating/scaling. Translation/rotation/scale order changes result.

**Model / mekanisme.** p_world=T_parent T_local p; store pivot in local space.

**Implementasi.** Offset to/from pivot explicitly or use renderer contract.

**Kegagalan tampilan.** Object drifts during scale; parent transform double applied.

**Pemeriksaan.** Known basis/pivot fixture and reversal endpoints.

## M03.06 — Moving bounds dan occupancy

Layout valid at endpoints dapat collide di tengah animation. Effect bounds include glow/shadow beyond object geometry.

**Model / mekanisme.** Swept/projected bounds over relevant intervals.

**Implementasi.** Sample adaptively around changes; analytical bound when feasible.

**Kegagalan tampilan.** Mask clips blur; transition covers critical caption.

**Pemeriksaan.** Full trajectory overlaps and effect extent checks.

## M03.07 — Recomposition across aspect ratios

Portrait needs reordered relationships, not only crop. Preserve semantic priority with alternative layout.

**Model / mekanisme.** Constraint-based layout with format-specific groups/anchors.

**Implementasi.** Render target-native variants and shared style tokens.

**Kegagalan tampilan.** Text tiny, diagram cut, focus lost.

**Pemeriksaan.** Native-resolution review and long-content fixtures.

## M03.08 — Depth layering dan occlusion

Foreground/background ordering can group or hide content. Transparency and perspective affect projected readability.

**Model / mekanisme.** Z-order/visibility rules and depth cue policy.

**Implementasi.** Scene layers explicit; labels may use separate readable overlay.

**Kegagalan tampilan.** Subject occluded during camera movement.

**Pemeriksaan.** Camera-path occlusion and silhouette checks.

## M03.09 — Layout transitions

Before/after layouts require coherent handoff. Layout motion can use rect transforms but typography wrapping changes semantics.

**Model / mekanisme.** Map source/target anchors/bounds; distinguish scale image from reflow text.

**Implementasi.** Evaluate layout snapshots, animate with stable identity.

**Kegagalan tampilan.** Letter stretching, sudden wrap, wrong correspondence.

**Pemeriksaan.** Dynamic content, interruption, endpoint and mid-transition readability.

## Penurunan mekanisme dan contoh terhitung

Contoh 720×405 frame: title box x=48…672 and y=32…96; diagram occupies y=135…335. A shape with radius 36 and shadow blur 18 has visual footprint larger than radius alone. If its path crosses title baseline, endpoint layout checks miss conflict. Enumerate effective bounds at sampled times and inspect full sequence. When output becomes 405×720, rearrange diagram vertically instead of blindly center-cropping.

## Kasus produksi

Kasus three-node flow uses shared baseline in landscape; portrait stacks nodes but preserves input→process→output order. Labels sit outside node motion path and stay readable. Reference layout stores anchors by role, not magic positions scattered code. After camera scale/rotation, inspect projected bounds again.

## Memilih teknik dan trade-offs

Use fixed pixel layout for controlled single output; normalized/constraints for multiple formats. Constraints improve adaptation but need infeasibility reporting for overly long text. Automated overlap detection flags geometry; it cannot judge whether overlap is intentional/beautiful.

## Alur kerja operasional

Define formats/regions; build hierarchy/groups; compute reference layout; assign anchors; plan paths/effect extents; render representative time samples; adapt variants; validate projection/readability.

## Verifikasi dan kriteria penguasaan

Dapat membuat moving layout tanpa accidental crop/overlap, mengaudit pivots dan native-format recomposition. Optical balance remains editorial/human review.

## Cabang spesialis dalam cakupan

Constraint solvers; responsive scene layout; geometric packing; optical alignment; composition in perspective; camera-aware annotations; motion-aware layout optimization.

## Hubungan antardomain

[M04](../../architecture/master-map.md#m04), [M05](../../architecture/master-map.md#m05), [M06](../../architecture/master-map.md#m06), [M09](../../architecture/master-map.md#m09), [M12](../../architecture/master-map.md#m12), [M14](../../architecture/master-map.md#m14), [M15](../../architecture/master-map.md#m15), [M20](../../architecture/master-map.md#m20).

## Jalur sumber

[R06](../../evidence/sources.md#r06), [R07](../../evidence/sources.md#r07), [R08](../../evidence/sources.md#r08).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.

## Pendalaman produksi

[Layout constraints sepanjang waktu](../deep-dives/03-layout-constraints-over-time.md) — decision/model/counterexample yang melengkapi chapter ini.
