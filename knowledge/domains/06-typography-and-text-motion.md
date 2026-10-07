# M06 — Typography and Text Motion

## Manifestasi yang ditampilkan

Titles, captions, labels, counters dan kinetic typography menyampaikan informasi melalui bentuk huruf, grouping dan perubahan sepanjang waktu.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Text tidak aman diperlakukan sebagai independent code points. Shaping, segmentation, direction, font coverage dan line breaks menjadi constraints nyata.

## Fondasi yang membentuk tampilan

Semantic string, Unicode graphemes, glyph shaping, metrics, layout, rasterization dan information availability terpisah. Coding menjaga text meaning sebelum expressive transforms.

## M06.01 — Characters clusters glyphs

Satu grapheme dapat berisi beberapa code points, satu glyph dapat mewakili ligature.

**Model / mekanisme.** Preserve string/language/direction; use relevant segmentation/shaping engine.

**Implementasi.** Animate runs/words atau shaped groups bila didukung.

**Kegagalan tampilan.** Arabic joining/accents/emoji broken.

**Pemeriksaan.** Combining marks, RTL, multiple scripts actual output.

## M06.02 — Fonts metrics fallback

Font metrics dan glyph coverage menentukan layout. Name availability bukan full glyph coverage.

**Model / mekanisme.** Font path/hash, metrics, coverage and fallback policy.

**Implementasi.** Load exact font, measure/render actual glyphs.

**Kegagalan tampilan.** Silent fallback changes identity/wrapping.

**Pemeriksaan.** Long strings, missing glyphs and loading failures.

## M06.03 — Hierarchy readability

Text size/weight/contrast/placement define roles. Availability begins ketika informasi readable.

**Model / mekanisme.** Title/caption/label role and readable window.

**Implementasi.** Measure actual bounds; allocate completed hold.

**Kegagalan tampilan.** Tiny text or effect hides meaning.

**Pemeriksaan.** Native-size playback dan task review.

## M06.04 — Wrapping alignment

Line break dan baseline grouping affect meaning/geometry.

**Model / mekanisme.** Width constraint, break opportunities, direction and anchor.

**Implementasi.** Layout before animation; reflow deliberately for new format.

**Kegagalan tampilan.** Mid-motion wrap jump, crop outside frame.

**Pemeriksaan.** Long content, aspect variants and baseline checks.

## M06.05 — Reveal granularity

Per-letter/word/line affects rhythm and total duration.

**Model / mekanisme.** Completion=(n−1)stagger+unit_duration from first start.

**Implementasi.** Compute availability and adjust grouping/timing.

**Kegagalan tampilan.** Text exits before fully revealed.

**Pemeriksaan.** Full string completion, order, hold and exit.

## M06.06 — Kinetic transforms

Expressive transforms must retain intended letter identity. Layout and deformation separate.

**Model / mekanisme.** Group/pivot/path model with allowed changes.

**Implementasi.** Preserve shaping then animate valid groups.

**Kegagalan tampilan.** Stretched/distorted words unreadable.

**Pemeriksaan.** Endpoint identity and full-sequence legibility.

## M06.07 — Counters and numerical text

Formatting precision/units/localization determine truthful data presentation.

**Model / mekanisme.** Value evaluator→formatter→layout.

**Implementasi.** Reserve width, align decimals, use tabular digits if supported.

**Kegagalan tampilan.** False precision, jittering width, wrong final value.

**Pemeriksaan.** Negative/large/localized known examples.

## M06.08 — Captions and spoken cues

Caption content and timing must match actual intended speech/context.

**Model / mekanisme.** Cue intervals/text/accuracy with safe region.

**Implementasi.** Keep overlays separate from focal motion.

**Kegagalan tampilan.** Cropped captions, late cue, diagram hidden.

**Pemeriksaan.** Content accuracy and start/middle/end alignment.

## M06.09 — Sampling and encoding

Thin moving strokes can shimmer or soften under output compression.

**Model / mekanisme.** Spatial/temporal sampling, color/chroma and codec contract.

**Implementasi.** Inspect decoded output at native size.

**Kegagalan tampilan.** Colored glyph edges blur, shimmer on slow motion.

**Pemeriksaan.** Small text/fast move/gradient examples.

## Penurunan mekanisme dan contoh terhitung

Six-word reveal: unit duration.35s and stagger.08s gives completion.75s. A2s beat leaves1.25s fully completed hold if no overlapping exit. Twenty-four units need2.19s, so same preset fails. Arithmetic establishes availability, not universal human reading threshold. Complex scripts may require grouping shaped runs rather than independent glyphs.

## Kasus produksi

Indonesian title and diagram labels keep exact semantic text. Measure DejaVu Sans for simple Latin demo; multilingual adaptation must reshape/re-layout. Word reveal then group hold/exit preserves sentence. Repo demo does not claim complex-script validation.

## Memilih teknik dan trade-offs

Prefer groups when shaping support limited. Per-glyph motion adds expression but increases segmentation/reading risk. Font fidelity/content accuracy outrank decorative complexity.

## Alur kerja operasional

Validate text/language/font; shape/layout; choose grouping; derive completed hold; assign hierarchy; render native formats; inspect final encoded cues.

## Verifikasi dan kriteria penguasaan

Dapat membedakan code points/graphemes/glyphs dan menghitung availability. Actual reading outcome needs appropriate viewers/task.

## Cabang spesialis dalam cakupan

OpenType shaping, variable fonts, bidirectional text, complex scripts, animated font axes, glyph-outline morphing, motion-aware typesetting and captions.

## Hubungan antardomain

[M01](../../architecture/master-map.md#m01), [M03](../../architecture/master-map.md#m03), [M04](../../architecture/master-map.md#m04), [M07](../../architecture/master-map.md#m07), [M10](../../architecture/master-map.md#m10), [M11](../../architecture/master-map.md#m11), [M12](../../architecture/master-map.md#m12), [M18](../../architecture/master-map.md#m18), [M20](../../architecture/master-map.md#m20).

## Jalur sumber

[R12](../../evidence/sources.md#r12), [R13](../../evidence/sources.md#r13), [R14](../../evidence/sources.md#r14).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.

## Pendalaman produksi

[Shaped text dan unit animasi](../deep-dives/06-shaped-text-and-animation-units.md) — decision/model/counterexample yang melengkapi chapter ini.
