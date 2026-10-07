# M07 — Color and Color Relationships

## Manifestasi yang ditampilkan

Palette, contrast, gradients dan color transitions memperlihatkan roles, relationships dan continuity sepanjang video.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Numeric RGB without color-space context is ambiguous. Emotional interpretation varies; tags alone do not convert pixels.

## Fondasi yang membentuk tampilan

Colorimetry, transfer curves, primaries, white point, gamut, interpolation, contrast dan display conditions form foundations. Separate role tokens from processing/output representation.

## M07.01 — Representations

Same triples can mean different colors under different spaces.

**Model / mekanisme.** Declare primaries/white point/transfer/range.

**Implementasi.** Version source→working→output conversions.

**Kegagalan tampilan.** Hue shifts/desaturation despite same numbers.

**Pemeriksaan.** Known patches and managed display review.

## M07.02 — Linear versus encoded

sRGB encoding is nonlinear; physical light arithmetic differs from encoded-value arithmetic.

**Model / mekanisme.** Decode low c as c/12.92, otherwise((c+.055)/1.055)^2.4.

**Implementasi.** Convert once per boundary with adequate precision.

**Kegagalan tampilan.** Double gamma or dark blends.

**Pemeriksaan.** Gray ramps, endpoints and round trips.

## M07.03 — Palette roles

Color can denote category/state/emphasis, with stable meanings.

**Model / mekanisme.** Role→token→color/material value.

**Implementasi.** Preserve map across shots and alternative cues.

**Kegagalan tampilan.** Same category changes color unexpectedly.

**Pemeriksaan.** Semantic audit and color-independent interpretation.

## M07.04 — Contrast legibility

Foreground/background variation can change text visibility during motion.

**Model / mekanisme.** Evaluate actual composited pixels with stated space/context.

**Implementasi.** Keep text/effects separate when necessary.

**Kegagalan tampilan.** Readable title disappears over bright shape.

**Pemeriksaan.** Worst frames and native output readability.

## M07.05 — Gradients

Stop/interpolation/gamut choices affect midpoint and banding.

**Model / mekanisme.** Spatial interpolation in chosen space.

**Implementasi.** Generate precision/dither as appropriate; record method.

**Kegagalan tampilan.** Muddy midpoint, bands or seams.

**Pemeriksaan.** Encode/playback moving ramps.

## M07.06 — Temporal interpolation

A color transition is path through color space, not always linear-energy mixing.

**Model / mekanisme.** Define endpoint space and route.

**Implementasi.** Pure evaluator; explicit clipping/gamut policy.

**Kegagalan tampilan.** Unexpected hue route or saturation flash.

**Pemeriksaan.** Endpoints and intermediate samples.

## M07.07 — Gamut mapping

Destination may not reproduce all source colors.

**Model / mekanisme.** Detect out-of-gamut; choose clamp/compression/mapping intentionally.

**Implementasi.** Record mapping and compare retained detail.

**Kegagalan tampilan.** Bright colors collapse same tone.

**Pemeriksaan.** Saturated patches and boundary gradients.

## M07.08 — Grading

Technical normalization and creative look have distinct purposes.

**Model / mekanisme.** Separate correction, look and output transform.

**Implementasi.** Version settings and inspect common subjects across shots.

**Kegagalan tampilan.** Exposure/white-balance jump at cut.

**Pemeriksaan.** Shared object/reference patches and transitions.

## M07.09 — Delivery perception

Player/display interpretation affects appearance.

**Model / mekanisme.** Record actual decode metadata and viewing setup.

**Implementasi.** Test known output target, preserve limits.

**Kegagalan tampilan.** SDR tagged HDR; unmanaged preview treated proof.

**Pemeriksaan.** Pixel/metadata comparison plus target playback.

## Penurunan mekanisme dan contoh terhitung

Halfway black/white encoded-value sRGB is.5. Halfway linear light.5 encodes≈.735sRGB. These are different goals, not interchangeable operations. Neither alone proves perceptual uniformity. Alpha filtering must also track premultiplication; averaging encoded RGB samples is an illustrative approximation unless intentionally correct for chosen model.

## Kasus produksi

Accent object crosses dark/light fields. Role remains fixed but legibility may need panel, outline or layout change. Final completion uses text/shape too. When exporting, convert pixels and tag output consistently rather than changing metadata only.

## Memilih teknik dan trade-offs

Choose linear-light for radiometric operations, perceptual spaces for intended appearance progression, authored path for style. Fit palette to destination gamut and actual viewing conditions.

## Alur kerja operasional

Inventory spaces; define role palette; implement conversions; check contrast/gamut; evaluate transitions; grade; encode and inspect target.

## Verifikasi dan kriteria penguasaan

Dapat compute transfer round-trip and distinguish interpolation goals. Emotion claims remain contextual hypothesis absent actual evidence.

## Cabang spesialis dalam cakupan

Spectral color, chromatic adaptation, gamut mapping, perceptual spaces, HDR tone mapping, appearance models, display calibration and temporal color artifacts.

## Hubungan antardomain

[M02](../../architecture/master-map.md#m02), [M04](../../architecture/master-map.md#m04), [M08](../../architecture/master-map.md#m08), [M17](../../architecture/master-map.md#m17), [M18](../../architecture/master-map.md#m18), [M20](../../architecture/master-map.md#m20), [M21](../../architecture/master-map.md#m21), [M22](../../architecture/master-map.md#m22).

## Jalur sumber

[R15](../../evidence/sources.md#r15), [R16](../../evidence/sources.md#r16), [R17](../../evidence/sources.md#r17).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.

## Pendalaman produksi

[Color sebagai data sepanjang pipeline](../deep-dives/07-color-as-data-through-pipeline.md) — decision/model/counterexample yang melengkapi chapter ini.
