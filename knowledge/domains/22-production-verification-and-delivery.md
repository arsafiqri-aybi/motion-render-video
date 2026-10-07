# M22 — Production Verification and Delivery

## Manifestasi yang ditampilkan

Penonton menerima file, stream atau image sequence. Produksi mengubah scene dan aset menjadi keluaran dengan durasi, resolusi, aspect ratio, color, audio, metadata dan kualitas yang sesuai. Error produksi dapat merusak karya walau scene tampak benar di preview.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Mencakup brief/specification, asset inventory, pipeline configuration, reproducibility, build verification, codec/container, captions, delivery variants dan quality gates. Tidak mencakup semua hukum/media broadcast; kebutuhan spesifik harus ditetapkan dan diverifikasi dari sumber yang berlaku.

## Fondasi yang membentuk tampilan

Source of truth, input hashes, versioned parameters, rational timestamps, codec/container distinction, dimensions, pixel format, metadata, decode checks dan review criteria. Status AUTHORED, EXECUTED dan HUMAN_REVIEWED tidak saling menggantikan.

## M22.01 — Brief output contract and acceptance

Target output perlu dinyatakan sebelum produksi.

**Model / mekanisme.** Contract berisi duration/aspect/fps/color/audio/caption/content constraints.

**Implementasi.** Buat machine-readable spec serta human acceptance questions.

**Kegagalan tampilan.** Final terasa benar tetapi salah ukuran atau pesan.

**Pemeriksaan.** Validate spec dan confirm content against brief.

## M22.02 — Asset font and rights inventory

Asset dependency menentukan tampilan serta portability.

**Model / mekanisme.** Inventory mencatat file/hash/license/version/fallback dan usage.

**Implementasi.** Resolve fonts/assets sebelum render; fail jika required asset hilang.

**Kegagalan tampilan.** Font substitution, missing texture atau asset rights tak diketahui.

**Pemeriksaan.** Run clean dependency check dan inspect critical typography.

## M22.03 — Determinism versions and provenance

Reproducing output memerlukan inputs serta environment yang cukup.

**Model / mekanisme.** Provenance mencakup code/config/seeds/tool versions/hashes.

**Implementasi.** Simpan report scoped per run; jangan menyalin PASS lama.

**Kegagalan tampilan.** Render berbeda atau laporan tidak cocok file saat ini.

**Pemeriksaan.** Compare input hashes dan output characteristics across runs.

## M22.04 — Sequence completeness and timestamps

File sequence harus lengkap dan timestamps sesuai clock.

**Model / mekanisme.** N frames at fps p/q cover N*q/p seconds for CFR intervals.

**Implementasi.** Check missing/duplicate frames, PTS monotonicity and spacing.

**Kegagalan tampilan.** Black gap, freeze, cadence error atau wrong endpoint.

**Pemeriksaan.** Probe and decode every output frame.

## M22.05 — Codec container and pixel format

Codec mengompresi streams; container menyimpan timing dan metadata.

**Model / mekanisme.** H264 dalam MP4 berbeda dari lossless master; yuv420p tidak membawa alpha.

**Implementasi.** Pilih supported codec/pixel format untuk target; declare bit depth/chroma.

**Kegagalan tampilan.** Playback gagal, alpha hilang atau text color edges rusak.

**Pemeriksaan.** ffprobe actual streams plus target playback and pixel review.

## M22.06 — Color audio and metadata integrity

Tags, levels dan channels memengaruhi interpretation output.

**Model / mekanisme.** Correct metadata perlu cocok conversion yang benar-benar dilakukan.

**Implementasi.** State primaries/transfer/matrix/range; verify sample rate/channels/duration.

**Kegagalan tampilan.** Washed colors, crushed blacks atau channel mapping salah.

**Pemeriksaan.** Probe tags dan compare controlled patches/audio cues.

## M22.07 — Visual audio and semantic quality gates

Engineering success tidak sama dengan content success.

**Model / mekanisme.** Gates berbeda mengukur decode integrity, visual artifacts, sync dan message.

**Implementasi.** Maintain separate reports, contact sheets and listening notes.

**Kegagalan tampilan.** PASS teknis dipakai untuk menutupi unreadable text atau wrong claim.

**Pemeriksaan.** Report executed scope and inspect actual deliverable.

## M22.08 — Variants adaptation and accessibility

Different aspect/resolution/caption needs require intentional re-layout.

**Model / mekanisme.** Crop, fit dan recompose have different information costs.

**Implementasi.** Define variant specs, safe areas and calmer/clean audio editions where needed.

**Kegagalan tampilan.** Portrait crop cuts headline atau subtitles clash.

**Pemeriksaan.** Validate each variant independently at viewing size.

## M22.09 — Packaging indexing and maintenance

Repo perlu dapat dicari, digunakan dan diperluas tanpa drift.

**Model / mekanisme.** Stable IDs, local links, structured indexes and source status form a knowledge graph.

**Implementasi.** Run link/coverage validator and version docs with relevant changes.

**Kegagalan tampilan.** Broken links, duplicated concepts or unsupported completeness claims.

**Pemeriksaan.** Check all paths and distinguish reference candidate from inspected evidence.

## Penurunan mekanisme dan contoh terhitung

180 frames pada30fps mencakup6detik. Frame terakhir bertimestamp179/30≈5.966667s; timestamp terakhir bukan durasi sequence. Untuk fractional rate30000/1001,180frames mencakup6.006s. Audio48kHz sepanjang6s memiliki288000samples per channel sebelum codec padding. Encoded audio dapat membawa priming/padding; ukur decoded behavior dan declared stream durations.

Bitrate tinggi tidak membuktikan kualitas, dan resolusi besar tidak membuktikan readability. Delivery contract perlu memasangkan property checks dengan criteria manusia yang terkait pesan.

## Kasus produksi

Pipeline demo dibangun dari config/cue sheet satu sumber, menghasilkan MP4 dan contact sheet serta reports. Unit checks mengevaluasi numeric motion; media checks menguji actual encode; visual review memakai sampled frames. Semua status disimpan terpisah agar reviewer mengetahui apa yang telah diuji. Footage/3D assets tidak diam-diam dianggap teruji oleh demo flat graphic.

## Memilih teknik dan trade-offs

MP4 H264 umum praktis untuk review/delivery bila target mendukungnya. Image sequences memberi frame-level control dan dapat lossless tetapi besar. Alpha master perlu format yang mendukung alpha. Manual review cocok semantic quality; automated validation cocok properties yang repeatable. Pilih target terlebih dahulu, baru settings.

## Alur kerja operasional

1. Lock output contract serta content acceptance.
2. Resolve assets/fonts dan record provenance.
3. Build render dengan explicit settings.
4. Encode serta decode full file.
5. Run engineering checks, visual review dan listening sesuai scope.
6. Package outputs/reports and state remaining limitations.

## Verifikasi dan kriteria penguasaan

Penguasaan: dapat membedakan codec/container, menghitung sequence duration, menghindari fake metadata conversion, mengaitkan reports dengan actual hashes, dan menjelaskan mana yang sudah dieksekusi. Tidak ada blanket claim 100% dunia motion atau semua delivery platforms.

## Cabang spesialis dalam cakupan

HDR masters, IMF/DCP/broadcast workflows, loudness specifications, codec benchmarking, perceptual quality metrics, render orchestration, signed manifests, supply-chain integrity, subtitle formats, localization, archival policies sesuai kebutuhan pengguna.

## Hubungan antardomain

[M01](../../architecture/master-map.md#m01), [M06](../../architecture/master-map.md#m06), [M07](../../architecture/master-map.md#m07), [M19](../../architecture/master-map.md#m19), [M20](../../architecture/master-map.md#m20), [M21](../../architecture/master-map.md#m21).

## Jalur sumber

[R23](../../evidence/sources.md#r23), [R16](../../evidence/sources.md#r16), [R34](../../evidence/sources.md#r34), [R35](../../evidence/sources.md#r35), [R36](../../evidence/sources.md#r36).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.
