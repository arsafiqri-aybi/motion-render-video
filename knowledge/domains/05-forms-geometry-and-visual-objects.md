# M05 — Forms Geometry and Visual Objects

## Manifestasi yang ditampilkan

Garis, shapes, icons, diagrams dan objek3D memberi tubuh pada motion. Geometry menentukan silhouette, paths, deformation dan relation yang dapat dilihat.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Geometry dibahas melalui manifestation video. Vector/raster/mesh memiliki roles berbeda; representation dipilih menurut fidelity, editing dan renderer.

## Fondasi yang membentuk tampilan

Coordinates, curves, topology, transforms, correspondence dan projected bounds menjadi foundations. Point/direction/normal tidak mempunyai transform semantics identik. Identity objek stabil sepanjang timeline.

## M05.01 — Primitives dan visual vocabulary

Primitive choice membantu recognition dan meaning. Geometry parameters harus konsisten unit dan origin.

**Model / mekanisme.** Circle/rect/line/polygon/mesh ditentukan size, orientation, stroke dan ID.

**Implementasi.** Generate dari named role parameters, bukan magic coordinates.

**Kegagalan tampilan.** Shape berubah style tanpa alasan, dimensions invalid.

**Pemeriksaan.** Known bounds/silhouette dan semantic role review.

## M05.02 — Paths dan curves

Curve parameter berbeda dari jarak. Smooth curve juga dapat mempunyai cusp atau derivative nol.

**Model / mekanisme.** Cubic Bézier B(u)=(1−u)³P0+3(1−u)²uP1+3(1−u)u²P2+u³P3.

**Implementasi.** Pure evaluator; arc-length LUT untuk constant-speed approximation.

**Kegagalan tampilan.** Speed uneven, camera flip near zero tangent.

**Pemeriksaan.** Endpoints/derivatives dan equal-distance samples.

## M05.03 — Strokes fills outlines

Caps/joins/width/fill rules alter apparent shape. Stroke extends geometry bounds.

**Model / mekanisme.** Define line join/cap, winding rule dan alpha.

**Implementasi.** Use renderer semantics and effect-aware bounds.

**Kegagalan tampilan.** Miter spikes, fill holes wrong, crop cuts stroke.

**Pemeriksaan.** Sharp corners/open paths/transformed edge fixtures.

## M05.04 — Topology connectivity

Connectivity menentukan deformasi dan morph possibilities. Positions dan topology merupakan data terpisah.

**Model / mekanisme.** Vertex/edge/face IDs and correspondence.

**Implementasi.** Validate indices, winding, degeneracy and intended manifold assumptions.

**Kegagalan tampilan.** Twisted morph, zero-area faces, cracks.

**Pemeriksaan.** Adjacency, endpoint reconstruction dan seam checks.

## M05.05 — Parametric objects

Generators expose meaningful state while retaining object identity. Ranges dan relationships need validation.

**Model / mekanisme.** Object=f(parameters), invariants define allowed family.

**Implementasi.** Version generator; invalidate caches on changed dependencies.

**Kegagalan tampilan.** Topology pops when parameter crosses boundary.

**Pemeriksaan.** Extremes, continuity and invalid combinations.

## M05.06 — Representation choice

Vector is geometric, raster sampled appearance, mesh spatial surface. All can animate.

**Model / mekanisme.** Content→representation→renderer/cost contract.

**Implementasi.** Preserve source assets and derived outputs separately.

**Kegagalan tampilan.** Raster detail lost on scale, unsupported vector effect.

**Pemeriksaan.** Native resolution and import/export subset.

## M05.07 — Silhouette projection

Recognition depends projected shape and context, not mesh detail alone.

**Model / mekanisme.** Projected outline/size over camera path.

**Implementasi.** Inspect flat silhouette before materials.

**Kegagalan tampilan.** Important features hidden, blur removes identity.

**Pemeriksaan.** Full-sequence silhouette and task review.

## M05.08 — Geometric queries

Distance/intersection/bounds help diagnose scene collisions and crop.

**Model / mekanisme.** Broad-phase candidates then appropriate exact test.

**Implementasi.** Recompute/refit after motion/deformation.

**Kegagalan tampilan.** Stale bounds; missed high-speed crossing.

**Pemeriksaan.** Small brute-force oracle and swept fixture.

## M05.09 — Persistence correspondence

Same appearance does not guarantee same object across scene.

**Model / mekanisme.** Stable semantic IDs, anchors and explicit split/merge.

**Implementasi.** Keep matching separate array order.

**Kegagalan tampilan.** Objects swap identity on sort.

**Pemeriksaan.** Reordering and transition endpoint tests.

## Penurunan mekanisme dan contoh terhitung

For cubic ((0,0),(0,1),(1,1),(1,0)), derivative is (6u(1−u),3(1−2u)). Speed simplifies to3(2u²−2u+1), integral length2. Equal u increments create unequal distance. Invert cumulative-length table for distance-driven motion; error depends subdivision. Curve at u=.5 is(.5,.75) regardless chosen time law. Edited control points invalidate lookup.

## Kasus produksi

Diagram: circles retain IDs, connectors reveal along paths and labels anchor by role. Connector start direction must reflect intended relation. For ring-to-square morph, match path orientation/start anchor and sample correspondence before blending. Similar vertex counts alone do not establish correct mapping.

## Memilih teknik dan trade-offs

Use primitives for relationship clarity, detailed assets for identity. More subdivisions do not always improve projected output. Solve correspondence before morph; texture warp is alternative with different artifacts.

## Alur kerja operasional

Define roles/units; choose representation; validate topology; assign IDs; build bounds/path tables; connect time/deformation; inspect silhouette and final render.

## Verifikasi dan kriteria penguasaan

Dapat membedakan path parameter/distance, menjaga identity dan menguji geometry terhadap known cases. Numeric validity tidak membuktikan recognition manusia.

## Cabang spesialis dalam cakupan

SDFs, implicit surfaces, subdivision, NURBS, tessellation, mesh repair, topology-changing effects, correspondence and procedural illustration.

## Hubungan antardomain

[M03](../../architecture/master-map.md#m03), [M09](../../architecture/master-map.md#m09), [M10](../../architecture/master-map.md#m10), [M13](../../architecture/master-map.md#m13), [M16](../../architecture/master-map.md#m16), [M17](../../architecture/master-map.md#m17), [M18](../../architecture/master-map.md#m18), [M21](../../architecture/master-map.md#m21).

## Jalur sumber

[R06](../../evidence/sources.md#r06), [R07](../../evidence/sources.md#r07), [R11](../../evidence/sources.md#r11).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.

## Pendalaman produksi

[Triangle coverage dan representasi bentuk](../deep-dives/05-triangles-coverage-and-topology.md) — decision/model/counterexample yang melengkapi chapter ini.
