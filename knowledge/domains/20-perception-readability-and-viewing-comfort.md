# M20 — Perception Readability and Viewing Comfort

## Manifestasi yang ditampilkan

Video berhasil ketika informasi dapat dilihat, diikuti, dipahami dan ditonton dalam kondisi nyata. Ukuran layar, compression, visual complexity, motion amplitude, dwell time dan sensitivitas penonton mengubah pengalaman.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Mencakup perceptual legibility, attention, contrast, temporal comfort dan akses informasi. Prinsip tidak menggantikan penelitian pengguna; tidak ada satu durasi atau easing yang menjamin semua orang nyaman. Standards memiliki applicability dan scope sendiri.

## Fondasi yang membentuk tampilan

Pisahkan physical signal, measured screen properties, subjective judgment dan empirical human findings. Gunakan hypotheses yang dapat diuji: pesan, kondisi viewing, ukuran, durasi, target audience dan indikator keberhasilan.

## M20.01 — Text legibility during motion

Teks yang bergerak atau kabur dapat sulit dibaca walau ukurannya cukup.

**Model / mekanisme.** Relative motion, exposure blur, contrast dan glyph shape berinteraksi.

**Implementasi.** Beri stable reading window dan ukur pada output resolution.

**Kegagalan tampilan.** Headline settle setelah hold sudah berakhir.

**Pemeriksaan.** Playback target-size serta uji recall/pemahaman yang relevan.

## M20.02 — Attention load and competing motion

Beberapa perubahan simultan dapat menimbulkan competing signals.

**Model / mekanisme.** Priority graph menentukan perubahan mana yang diharapkan menjadi focus.

**Implementasi.** Kurangi motion tidak penting saat pesan utama hadir.

**Kegagalan tampilan.** Eye-catching effect menarik dari CTA atau diagram.

**Pemeriksaan.** Compare variants; catat observations tanpa mengklaim gaze measurement.

## M20.03 — Contrast and background variation

Readability berubah sepanjang footage bergerak, bukan hanya satu warna statis.

**Model / mekanisme.** Luminance relationship bergantung transfer conversion dan patch sampling.

**Implementasi.** Gunakan scrim/backplate atau adaptive placement jika diperlukan.

**Kegagalan tampilan.** Teks hilang di sebagian frame.

**Pemeriksaan.** Sweep sequence dan cek low-contrast segments; standards test memakai definisi resmi.

## M20.04 — Motion amplitude and visual field

Gerak besar pada seluruh layar mempunyai pengalaman berbeda dari ikon kecil.

**Model / mekanisme.** Screen-space displacement, angular size dan covered area adalah parameter berbeda.

**Implementasi.** Sediakan calmer variant sesuai kebutuhan distribusi dan audience.

**Kegagalan tampilan.** Parallax besar atau camera shake mengganggu penonton.

**Pemeriksaan.** Review full playback pada beberapa display sizes dan feedback nyata.

## M20.05 — Flashes repetitive patterns and thresholds

Flash serta pattern berulang memerlukan pemeriksaan khusus.

**Model / mekanisme.** Definisi flash/red flash dan threshold bukan sekadar jumlah cut per detik.

**Implementasi.** Hindari efek intens tanpa fungsi; gunakan analisis yang mengikuti applicable standard.

**Kegagalan tampilan.** Video berisiko/menyakitkan ditonton walau thumbnail tenang.

**Pemeriksaan.** Dokumentasikan screening; jangan menyebut PASS dari framecount saja.

## M20.06 — Occlusion continuity and object identity

Penonton menghubungkan objek sebelum dan sesudah tersembunyi melalui cues.

**Model / mekanisme.** Position, appearance dan timing menjaga correspondence.

**Implementasi.** Pertahankan anchor atau desain reveal yang memperjelas perubahan.

**Kegagalan tampilan.** Objek terasa berganti tanpa alasan atau informasi tertutup.

**Pemeriksaan.** Review occlusion boundaries dan continuity hypotheses.

## M20.07 — Viewing size compression and environment

Detail yang terlihat di workstation dapat hilang di ponsel atau encoded output.

**Model / mekanisme.** Spatial/temporal compression mengubah fine detail serta gradients.

**Implementasi.** Uji actual encode pada ukuran/aspect dan ambient conditions relevan.

**Kegagalan tampilan.** Thin strokes, texture dan subtitles rusak.

**Pemeriksaan.** Bandingkan source/decoded crops serta practical playback.

## M20.08 — Multimodal access and comprehension

Informasi dapat disampaikan melalui visual, audio dan teks pendukung.

**Model / mekanisme.** Redundant routes membantu ketika salah satu channel tidak tersedia.

**Implementasi.** Sediakan captions/transcript dan visual-only understanding sesuai konteks.

**Kegagalan tampilan.** Key claim hanya dalam suara atau captions menutup aksi.

**Pemeriksaan.** Review muted, audio-only bila relevan, serta caption readability.

## M20.09 — Evaluation uncertainty and audience testing

Klaim pengalaman membutuhkan evidence yang sesuai klaim.

**Model / mekanisme.** Checklist engineering, expert review dan user study mengukur hal berbeda.

**Implementasi.** Tetapkan pertanyaan, peserta, kondisi dan limitations sebelum tes.

**Kegagalan tampilan.** Desainer menyebut intuitif atau accessible tanpa evidence.

**Pemeriksaan.** Laporkan actual method, observations dan uncertainty.

## Penurunan mekanisme dan contoh terhitung

Motion speed 120 pixels/s pada layar preview 1200 px lebar setara 10% lebar per detik. Jika preview dikecilkan menjadi 600 px dengan resampling, displacement menjadi 60 px/s tetapi normalized speed tetap 10%. Angular speed pada mata tetap bergantung physical display size dan viewing distance. Oleh karena itu pixel-speed tunggal tidak cukup menjelaskan comfort.

Kontras untuk warna teks statis tidak menyelesaikan readability ketika teks sedang bergerak atau background terus berubah. Verifikasi perlu mencakup waktu paling buruk dan fase membaca yang direncanakan, bukan hanya hero frame.

## Kasus produksi

Explainer menampilkan diagram kompleks. Gunakan progressive disclosure; highlight satu jalur; hentikan node motion selama label dibaca. Buat calmer version dengan camera movement lebih kecil. Uji pesan utama pada viewers yang belum mengenal diagram dan catat apa yang mereka salah pahami; revisi berdasarkan masalah yang terlihat.

## Memilih teknik dan trade-offs

Expert review murah untuk menemukan obvious failures tetapi bukan representasi seluruh audience. Automated scans cocok properti yang terdefinisi; comfort dan comprehension membutuhkan metode tambahan. Reduced-motion variant pada video biasanya file/edisi alternatif, bukan runtime preference yang otomatis mengubah encoded video.

## Alur kerja operasional

1. Tetapkan informasi dan audience.
2. Tentukan reading windows serta motion budget secara kontekstual.
3. Uji target-size encode.
4. Screening flashes/patterns menggunakan metode yang tepat.
5. Sediakan akses informasi lintas channel.
6. Laporkan evidence serta batas klaim.

## Verifikasi dan kriteria penguasaan

Penguasaan: dapat membedakan angka engineering dari human evidence, menemukan worst-case readability, membuat quieter motion variant, dan memakai standar sesuai scope. Repo ini tidak mengklaim certification accessibility atau photosensitivity dari demo render.

## Cabang spesialis dalam cakupan

Eye tracking, psychophysics, motion sensitivity, visual crowding, apparent motion, temporal masking, reading studies, caption usability, audio description, photosensitive flash analysis, task-based comprehension studies, inclusive audience sampling.

## Hubungan antardomain

[M01](../../architecture/master-map.md#m01), [M04](../../architecture/master-map.md#m04), [M06](../../architecture/master-map.md#m06), [M07](../../architecture/master-map.md#m07), [M11](../../architecture/master-map.md#m11), [M19](../../architecture/master-map.md#m19), [M22](../../architecture/master-map.md#m22).

## Jalur sumber

[R03](../../evidence/sources.md#r03), [R09](../../evidence/sources.md#r09), [R10](../../evidence/sources.md#r10), [R35](../../evidence/sources.md#r35).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.
