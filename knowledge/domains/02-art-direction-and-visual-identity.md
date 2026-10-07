# M02 — Art Direction and Visual Identity

## Manifestasi yang ditampilkan

Video dikenali melalui coherent shapes, typography, color, materials, camera dan motion vocabulary. Identitas muncul sepanjang sequence, bukan hanya logo pada frame awal.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Art direction adalah keputusan desain berdasarkan purpose/context. Gaya seperti premium, warm, futuristic atau minimal harus diterjemahkan ke properties konkret; tidak menjadi universal psychological claim.

## Fondasi yang membentuk tampilan

Fondasinya adalah abstraction, visual semantics, reference analysis, consistency, constraint systems dan expressive choices. Coding menyimpan style tokens, valid ranges dan exceptions, sementara author tetap meninjau effect nyata.

## M02.01 — Concept dan organizing idea

Identitas kuat memiliki organizing idea terkait subject. Memilih palette saja belum membentuk konsep.

**Model / mekanisme.** Concept→visual rules→motion rules→exceptions.

**Implementasi.** Record rationale dan concrete properties dalam art-direction specification.

**Kegagalan tampilan.** Generic neon/glass dipakai tanpa hubungan topik.

**Pemeriksaan.** Apakah subject masih dikenali setelah logo/title disembunyikan?

## M02.02 — Reference analysis

Referensi dibaca untuk prinsip: hierarchy, material, rhythm, composition. Mengambil protected assets/susunan mentah membutuhkan rights yang sesuai.

**Model / mekanisme.** Distinguish inspiration, licensed asset, original creation and factual reference.

**Implementasi.** Reference ledger mencatat role dan keputusan yang diturunkan.

**Kegagalan tampilan.** Replica karya lain dianggap original; surface styling copied.

**Pemeriksaan.** Source/provenance review dan comparison of structural choices.

## M02.03 — Visual vocabulary

Shape families, line weights, corners, textures dan icon construction menentukan language yang konsisten.

**Model / mekanisme.** Define primitives, scale relationships dan allowed deformation.

**Implementasi.** Parameterized geometry/style components with named intent.

**Kegagalan tampilan.** Semua objek punya styles berbeda; object meaning ambigu.

**Pemeriksaan.** Review vocabulary on several subjects, not one beauty frame.

## M02.04 — Motion vocabulary

Cara masuk, bergerak, berubah dan berhenti dapat menjadi signature. Signature tetap harus cocok fungsi shot.

**Model / mekanisme.** Define response families, trajectory rules, duration ranges and exceptions.

**Implementasi.** Tokens refer to model/easing/time unit, bukan adjective alone.

**Kegagalan tampilan.** Semua motion menggunakan bounce meski serious message.

**Pemeriksaan.** Compare recurring actions dan justified deviations.

## M02.05 — Color material typography system

Colors, surfaces dan text families saling berinteraksi. Surface/specular changes dapat alter perceived palette.

**Model / mekanisme.** Link role tokens to color/material/font values and fallbacks.

**Implementasi.** Scene reads versioned tokens; export records actual fonts/render settings.

**Kegagalan tampilan.** Font substitute merusak identity; lighting changes color roles.

**Pemeriksaan.** Cross-shot appearance, actual assets, target display/context.

## M02.06 — Constraints dan variation

Constraints menjaga family resemblance; variation mencegah monotony. Consistency bukan identical frames.

**Model / mekanisme.** Define invariants versus variable properties per scene role.

**Implementasi.** Enforce invariants through schema, allow explicit overrides.

**Kegagalan tampilan.** Rigid template menghapus subject differences.

**Pemeriksaan.** Evaluate diverse scenes and extreme content lengths.

## M02.07 — Tone dan emotional intent

Intended mood berasal kombinasi content, pacing, contrast, sound dan context. Tidak ada palette yang menjamin emotion sama pada semua audience.

**Model / mekanisme.** State hypothesis dan intended tone; preserve uncertainty.

**Implementasi.** Annotate cues and review with relevant context.

**Kegagalan tampilan.** Color psychology oversold; sound contradicts visual intent.

**Pemeriksaan.** Editorial review plus actual audience evidence when required.

## M02.08 — Identity across formats

Landscape/portrait, captions dan thumbnails memberi constraints berbeda. Cropping automatic dapat menghilangkan signature atau message.

**Model / mekanisme.** Preserve priority and identity while recompose format.

**Implementasi.** Layout presets share tokens but adapt spatial arrangement.

**Kegagalan tampilan.** Center-crop clips focal subject; tiny text.

**Pemeriksaan.** Native-format inspection including platform overlays.

## M02.09 — Direction review dan iteration

Art direction diputuskan dari full sequence, assets dan deviations. Revising root concept berbeda dari adding decoration.

**Model / mekanisme.** Review intent→rule→manifestation→issue→change.

**Implementasi.** Version specification and representative frames.

**Kegagalan tampilan.** Endless polish tanpa tujuan; changes inconsistent across shots.

**Pemeriksaan.** Compare revised sequences against brief and known constraints.

## Penurunan mekanisme dan contoh terhitung

Contoh konsep "state becomes form": shape berubah dari wire outline menjadi solid object ketika informasi lengkap. Identity rules: limited accent, precise alignment, material change as evidence of state, restrained camera. Outline-to-solid transition harus mempunyai semantic role; jika semua elements selalu glow, cue loses distinction. Token duration range adalah production rule yang nanti disesuaikan content.

## Kasus produksi

Kasus product explanation memakai line-based geometry, short decisive motion dan warm matte surface. Title, diagram dan closing shot berbagi vocabulary tetapi tidak layout identical. Coding assets expose stroke, corner, accent, material dan timing families. Missing font menghasilkan flagged fallback, bukan quietly claiming identity preserved.

## Memilih teknik dan trade-offs

Compare 2–3 organizing ideas sebelum pilih. Pilih yang paling cocok subject dan production capability, bukan paling kompleks. Texture richness dapat menambah identity tetapi juga aliasing/encode cost; distinct rhythm bisa membangun signature dengan geometry sederhana.

## Alur kerja operasional

Extract subject/context; analyze references; choose organizing idea; define tokens/invariants; build representative shots; inspect variation; revise system; lock version for production.

## Verifikasi dan kriteria penguasaan

Dapat menerjemahkan style adjectives menjadi measurable/renderable properties, membuat purposeful exceptions dan menjelaskan original choices. Identity fit tetap judgment/context, bukan automated certainty score.

## Cabang spesialis dalam cakupan

Visual semiotics; brand motion systems; motion language grammars; procedural styling; art direction untuk scientific data; culturally grounded visual identity; material storytelling.

## Hubungan antardomain

[M01](../../architecture/master-map.md#m01), [M03](../../architecture/master-map.md#m03), [M05](../../architecture/master-map.md#m05), [M06](../../architecture/master-map.md#m06), [M07](../../architecture/master-map.md#m07), [M08](../../architecture/master-map.md#m08), [M10](../../architecture/master-map.md#m10), [M12](../../architecture/master-map.md#m12), [M19](../../architecture/master-map.md#m19).

## Jalur sumber

[R02](../../evidence/sources.md#r02), [R04](../../evidence/sources.md#r04), [R05](../../evidence/sources.md#r05).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.
