# M15 — Transitions Editing and Continuity

## Manifestasi yang ditampilkan

Editing mengatur hubungan antar waktu dan shot. Cut, dissolve, wipe, match move dan reveal dapat menyambung informasi, mengubah konteks, atau menandai lompatan. Efek transisi harus dibaca bersama gambar sebelum dan sesudahnya.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Mencakup edit decisions, continuity, transition geometry, sequencing dan temporal retiming. Timeline data M11/M12 menyediakan waktu, compositing M18 membentuk image blend, delivery M22 memastikan sequence benar.

## Fondasi yang membentuk tampilan

Gunakan shot intervals, editorial handles, action phase, directional continuity, landmark matching dan mapping source-time ke output-time. Duration transisi adalah interval nyata yang mengambil bagian dari dua shot.

## M15.01 — Cut and information change

Cut mengubah image state secara diskrit dan dapat langsung mengubah pusat perhatian.

**Model / mekanisme.** Cut boundary terletak di antara dua output frames; tidak perlu intermediate.

**Implementasi.** Pilih cut pada cue aksi, pesan atau perubahan konteks.

**Kegagalan tampilan.** Jump terasa tidak termotivasi atau informasi hilang.

**Pemeriksaan.** Review frame sebelum/sesudah dan first impression penonton.

## M15.02 — Match action and motion continuity

Gerak dapat menjembatani shot bila phase dan arah terasa berlanjut.

**Model / mekanisme.** Cocokkan pose, screen direction serta action time pada overlap coverage.

**Implementasi.** Gunakan shot handles untuk memilih phase cut.

**Kegagalan tampilan.** Aksi diulang atau melompat terlalu jauh.

**Pemeriksaan.** Compare pose serta displacement pada sekitar cut.

## M15.03 — Graphic and shape matching

Kesamaan bentuk/lokasi membimbing mata saat konteks berubah.

**Model / mekanisme.** Landmark layar sebelum/sesudah berada dalam jarak dan skala yang dirancang.

**Implementasi.** Buat guide overlay dan transform alignment.

**Kegagalan tampilan.** Match hanya mirip di satu frame tetapi runtuh saat bergerak.

**Pemeriksaan.** Periksa landmark trajectory di beberapa frame sekitar cut.

## M15.04 — Dissolve and alpha blending

Dissolve menampilkan dua image layers bersamaan selama interval.

**Model / mekanisme.** C=(1-u)A+uB dalam working space yang didefinisikan.

**Implementasi.** Linearize bila target adalah light mixing; tetapkan alpha convention.

**Kegagalan tampilan.** Midpoint kusam, double subject atau ghost text.

**Pemeriksaan.** Inspect midpoint serta readable overlap, bukan endpoint saja.

## M15.05 — Wipe mask and occlusion

Batas spasial menentukan wilayah yang menjadi shot baru.

**Model / mekanisme.** Mask m(x,t) mengatur coverage dengan edge antialiasing.

**Implementasi.** Hubungkan wipe direction dengan geometry scene bila bermakna.

**Kegagalan tampilan.** Tepi jagged, mask bocor dan objek terlihat terpotong tanpa alasan.

**Pemeriksaan.** Uji first/last coverage dan edge pada full scale.

## M15.06 — Object-mediated transitions

Objek atau kamera menutup frame sehingga perpindahan memiliki motivasi.

**Model / mekanisme.** Occlusion interval menyembunyikan perubahan scene state.

**Implementasi.** Cocokkan warna, skala dan trajectory occluder di dua shot.

**Kegagalan tampilan.** Cut terlihat di sela celah atau occluder mengubah identitas.

**Pemeriksaan.** Tinjau frame minimum coverage dan continuous velocity.

## M15.07 — Retiming speed ramps and freeze

Mapping waktu mengubah speed peristiwa sumber.

**Model / mekanisme.** t_source=g(t_output); derivative g' adalah speed ratio.

**Implementasi.** Rancang g kontinu; untuk interpolasi frame tentukan optical flow atau duplicated frames.

**Kegagalan tampilan.** Stutter, temporal hallucination atau audio pitch tak diinginkan.

**Pemeriksaan.** Plot source time, cek monotonicity dan inspect occlusion artefacts.

## M15.08 — Editorial pacing and holds

Ritme editorial mengatur waktu pengungkapan dan integrasi pesan.

**Model / mekanisme.** Shot duration dan information density adalah variabel berbeda.

**Implementasi.** Buat versi timing dengan hold lebih panjang/pendek dan bandingkan fungsi.

**Kegagalan tampilan.** Tempo seragam atau shot berakhir sebelum pesan terbaca.

**Pemeriksaan.** View sequence utuh pada kondisi target dan uji pemahaman.

## M15.09 — Loop closure and temporal seams

Loop memerlukan hubungan akhir-awal dalam tampilan dan gerak.

**Model / mekanisme.** Periodic function menjaga value; derivative continuity menjaga velocity.

**Implementasi.** Render interval half-open tanpa duplicate endpoint; cek audio seam.

**Kegagalan tampilan.** Frame hold ganda, klik audio atau jump phase.

**Pemeriksaan.** Gabungkan tiga putaran dan ukur boundary value serta motion.

## Penurunan mekanisme dan contoh terhitung

Dua shot masing-masing 3 detik dengan dissolve overlap 0.5 detik menghasilkan sequence 3+3-0.5=5.5 detik, bukan 6.5. Pada 30 fps constant-frame-rate, 0.5 detik adalah 15 frame intervals. Harus jelas apakah durasi shot yang dilaporkan termasuk handles dan overlap.

Speed ramp g(t)=a t² memberi speed g'=2at. Ia tidak cocok dipasang langsung setelah segmen speed konstan v bila 2at pada boundary tidak sama v. Blend duration perlu memenuhi derivative continuity untuk menghindari perubahan speed mendadak.

## Kasus produksi

Video tiga informasi produk menggunakan cut untuk perubahan pesan dan satu object-mediated transition untuk memperlihatkan hubungan. Simpan minimal 0.5 s handles pada shot penghubung, align screen direction, biarkan headline settle sebelum cut, dan hindari dissolve antar dua headline karena keduanya sulit dibaca saat overlap.

## Memilih teknik dan trade-offs

Cut biasanya paling langsung untuk informasi baru. Dissolve cocok perubahan gradual bila superposition tidak membingungkan. Wipe mengarahkan attention tetapi membawa edge motion. Optical-flow retiming dapat halus namun memerlukan inspeksi frame occlusion. Tidak ada default transition yang selalu superior.

## Alur kerja operasional

1. Tetapkan fungsi setiap edit.
2. Buat sequence tanpa effects dan nilai ritme.
3. Cocokkan action/graphic continuity.
4. Tambahkan transition sesuai hubungan yang hendak dibangun.
5. Hitung ulang duration dan audio cue.
6. Periksa boundary frames serta full playback.

## Verifikasi dan kriteria penguasaan

Penguasaan: dapat menjelaskan alasan cut, menghitung overlap, menghindari repeated action, membuat loop tanpa endpoint ganda, dan mengenali artefak retiming. Kepatuhan hitungan duration belum membuktikan editorial pacing berhasil.

## Cabang spesialis dalam cakupan

J/L cuts, montage, parallel action, split screen, match dissolves, motion vector transitions, optical flow, interpolation uncertainty, inverse time mapping, variable frame rate conforming, EDL/OTIO interoperability.

## Hubungan antardomain

[M01](../../architecture/master-map.md#m01), [M11](../../architecture/master-map.md#m11), [M12](../../architecture/master-map.md#m12), [M14](../../architecture/master-map.md#m14), [M18](../../architecture/master-map.md#m18), [M19](../../architecture/master-map.md#m19).

## Jalur sumber

[R23](../../evidence/sources.md#r23), [R28](../../evidence/sources.md#r28), [R29](../../evidence/sources.md#r29).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.

## Pendalaman produksi

[Batas edit, meaning dan match continuity](../deep-dives/15-edit-boundaries-meaning-and-matching.md) — decision/model/counterexample yang melengkapi chapter ini.
