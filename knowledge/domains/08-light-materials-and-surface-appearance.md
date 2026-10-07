# M08 — Light Materials and Surface Appearance

## Manifestasi yang ditampilkan

Surfaces terasa matte, glossy, textured, emissive, translucent atau atmospheric karena geometry, light dan material interaction.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

2D illusion can be valid art direction; do not label it measured physical material. PBR does not imply calibrated real scene.

## Fondasi yang membentuk tampilan

Normals, reflectance/BSDF models, coordinates, sampling, exposure and output transforms determine appearance. Light/material changes may communicate state if meaning established.

## M08.01 — Normals orientation

Lighting needs surface direction in correct frame.

**Model / mekanisme.** Nonuniform transform normal uses inverse transpose then normalization.

**Implementasi.** Validate normals before material tuning.

**Kegagalan tampilan.** Highlights wrong under scale.

**Pemeriksaan.** Plane/tangent perpendicularity fixtures.

## M08.02 — Diffuse specular roughness

Reflection lobes and roughness change surface response.

**Model / mekanisme.** Renderer-defined BRDF and parameter ranges.

**Implementasi.** Compare under fixed light/camera/exposure.

**Kegagalan tampilan.** Shiny assumed universally premium; wrong data texture space.

**Pemeriksaan.** View/light sweeps and controlled material comparisons.

## M08.03 — Metal dielectric transmission

Reflective/transmissive models require appropriate assumptions.

**Model / mekanisme.** IOR, thickness, scattering and reflectance contract.

**Implementasi.** Use supported models with known geometry.

**Kegagalan tampilan.** Impossible glass/backfaces or inconsistent metal.

**Pemeriksaan.** Thickness/angle and boundaries.

## M08.04 — Textures UVs

Surface detail must follow chosen coordinate system.

**Model / mekanisme.** UV/object/world mapping with scale/filtering.

**Implementasi.** Classify color versus data textures and sampling.

**Kegagalan tampilan.** Swimming textures/seams/aliasing.

**Pemeriksaan.** Rotate/deform/zoom sequence.

## M08.05 — Lighting placement

Light type/size/falloff affects form and shadows.

**Model / mekanisme.** Directional/point/area/environment with documented intensity units.

**Implementasi.** Start static known scene then animate one variable.

**Kegagalan tampilan.** Scale/exposure mismatch alters brightness.

**Pemeriksaan.** Distance/angle sweeps.

## M08.06 — Shadows contact

Shadows relate surface/object and depth.

**Model / mekanisme.** Shadow algorithm/bias/blur/contact policy.

**Implementasi.** Include effective shadow bounds and sampling.

**Kegagalan tampilan.** Floating object/acne/flicker.

**Pemeriksaan.** Contact/light/camera movement.

## M08.07 — Exposure tone mapping

High dynamic radiance needs output-range treatment.

**Model / mekanisme.** Separate exposure, tone mapping and grading.

**Implementasi.** Lock stages for comparisons.

**Kegagalan tampilan.** Clipped highlight or unexplained brightness jump.

**Pemeriksaan.** Gray/bright patches over sequence.

## M08.08 — Material animation

Property change can express state but parameter-linear isn't necessarily appearance-linear.

**Model / mekanisme.** Time/state→material evaluator.

**Implementasi.** Inspect actual rendered intermediates.

**Kegagalan tampilan.** Uneven appearance transition or opacity pop.

**Pemeriksaan.** Endpoint/intermediate and semantic checks.

## M08.09 — Volumes atmosphere

Density/lighting/transport affect visibility and depth.

**Model / mekanisme.** State volume integration or labeled 2D approximation.

**Implementasi.** Use supported renderer and preserve text visibility.

**Kegagalan tampilan.** Fog hides subject, noisy flicker.

**Pemeriksaan.** Temporal samples/readability and density extremes.

## Penurunan mekanisme dan contoh terhitung

Ideal Lambertian f=ρ/π combines incident radiance with cosine geometry in light transport. A dot(n,l) shaded2D circle mimics form but is not full light transport. Nonuniformly scaled mesh without correct normals gives wrong highlight: more samples cannot correct that. Separate rendering assumptions from art-directed cue.

## Kasus produksi

Object becomes solid when process complete through opacity/roughness/light changes coordinated motion. Silhouette retains identity. A2D illustration may be sufficient; label physical approximation and do not claim calibrated glass/metal appearance.

## Memilih teknik dan trade-offs

Use2D cues for controlled illustration;3D when appearance must survive viewpoint/light changes. Choose realistic/stylized based message. Quality/cost evaluated on sequence, not beauty frame.

## Alur kerja operasional

Define intent; validate geometry/normals; establish light/exposure; choose material; add textures; animate; inspect artifacts/readability; verify color output.

## Verifikasi dan kriteria penguasaan

Dapat separate geometry/material/light/exposure errors and preserve appearance across motion. Hardware rendering and material calibration are separate evidence.

## Cabang spesialis dalam cakupan

BSDFs, subsurface scattering, thin films, participating media, spectral rendering, PBR texture workflows, real-time lighting and stylized shaders.

## Hubungan antardomain

[M02](../../architecture/master-map.md#m02), [M05](../../architecture/master-map.md#m05), [M07](../../architecture/master-map.md#m07), [M09](../../architecture/master-map.md#m09), [M14](../../architecture/master-map.md#m14), [M17](../../architecture/master-map.md#m17), [M18](../../architecture/master-map.md#m18), [M21](../../architecture/master-map.md#m21).

## Jalur sumber

[R11](../../evidence/sources.md#r11), [R18](../../evidence/sources.md#r18), [R19](../../evidence/sources.md#r19).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.

## Pendalaman produksi

[Normals, shading dan material contract](../deep-dives/08-normals-shading-and-material-contract.md) — decision/model/counterexample yang melengkapi chapter ini.
