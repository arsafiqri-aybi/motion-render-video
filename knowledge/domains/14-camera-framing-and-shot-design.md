# M14 — Camera Framing and Shot Design

## Manifestasi yang ditampilkan

Kamera menentukan apa yang terlihat, seberapa besar, dari arah mana, dan bagaimana perhatian berpindah. Dolly, pan, tilt, orbit dan perubahan focal length mempunyai hubungan perspektif berbeda walaupun seluruhnya membuat gambar bergerak.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Mencakup virtual cinematography, framing, lens projection, camera movement, focus dan coverage shot. Komposisi statis ada di M03, gerak objek di M10, edit antars shot di M15. Kamera fisik dan sintetik berbagi beberapa model, tetapi rolling shutter atau distorsi lens harus dimodelkan eksplisit.

## Fondasi yang membentuk tampilan

Gunakan world/view/projection space, arah view, aspect ratio, near/far plane, focal length, sensor/film size, dan fungsi kamera atas waktu. Framing adalah constraint pada projected bounds, bukan hanya posisi kamera.

## M14.01 — Framing and subject scale

Ukuran subjek pada layar memengaruhi informasi dan konteks yang tersedia.

**Model / mekanisme.** Projected bounding box berubah terhadap jarak, focal length dan pose.

**Implementasi.** Definisikan margin dan posisi subjek dalam normalized screen coordinates.

**Kegagalan tampilan.** Subjek keluar frame atau shot kosong saat pose berubah.

**Pemeriksaan.** Sweep pose dan waktu; ukur bounds dengan safe margin.

## M14.02 — Perspective and lens choice

Perspektif berasal dari posisi kamera; focal length mengatur sudut pandang pada posisi itu.

**Model / mekanisme.** Model pinhole memetakan x=fX/Z.

**Implementasi.** Pisahkan perubahan focal length dari perubahan posisi kamera pada tools.

**Kegagalan tampilan.** Dolly dan zoom dianggap identik sehingga kedalaman berperilaku salah.

**Pemeriksaan.** Bandingkan rasio ukuran foreground/background selama gerak.

## M14.03 — Pan tilt roll and orbit

Orientasi kamera mengubah framing dengan karakter gerak berbeda.

**Model / mekanisme.** Orbit mengubah posisi sekaligus orientasi menuju target; pan/tilt dapat menjaga posisi.

**Implementasi.** Tetapkan target, up vector dan singularity handling.

**Kegagalan tampilan.** Horizon flip atau orbit melewati subjek.

**Pemeriksaan.** Uji arah pandang, up vector dan trajectory pada shot penuh.

## M14.04 — Dolly truck pedestal

Translasi kamera menghasilkan parallax sesuai kedalaman.

**Model / mekanisme.** Image velocity tergantung relative transform objek terhadap kamera.

**Implementasi.** Buat path world-space dengan acceleration yang sesuai intent.

**Kegagalan tampilan.** Gerak datar atau terasa seperti seluruh scene digeser.

**Pemeriksaan.** Gunakan foreground/midground/background landmarks untuk mengecek parallax.

## M14.05 — Focus and depth of field

Distribusi ketajaman membantu penekanan tetapi dapat mengurangi informasi.

**Model / mekanisme.** Lens model memetakan point menjadi blur footprint di luar focus plane.

**Implementasi.** Pisahkan focus distance, aperture dan artistic blur; antisipasi focus pull.

**Kegagalan tampilan.** Teks dan produk kabur atau fokus hunting.

**Pemeriksaan.** Periksa target focus pada full-resolution frames.

## M14.06 — Camera easing and stabilization

Gerak kamera mengubah seluruh visual field, sehingga jerk mudah terasa.

**Model / mekanisme.** Continuity velocity dan acceleration menentukan start/stop.

**Implementasi.** Pakai bounded trajectory, look-ahead dan motion smoothing yang tidak menggeser cue tanpa kontrol.

**Kegagalan tampilan.** Overshoot framing, tremor dan tracking terlambat.

**Pemeriksaan.** Plot camera pose dan screen-space velocity target.

## M14.07 — Shot coverage and scale progression

Rangkaian wide-medium-detail memberi struktur pengungkapan.

**Model / mekanisme.** Shot graph menghubungkan fungsi informasi dengan ukuran dan arah view.

**Implementasi.** Tulis shot list dengan tujuan, start/end composition dan continuity data.

**Kegagalan tampilan.** Banyak shot indah tanpa informasi baru.

**Pemeriksaan.** Nilai kontribusi setiap shot terhadap pesan dan orientasi.

## M14.08 — Dolly zoom and coupled parameters

Perubahan jarak dan focal length dapat mempertahankan skala subjek sambil mengubah ruang.

**Model / mekanisme.** Untuk subject tetap, f/Z dijaga konstan.

**Implementasi.** Animasi f dan Z dari satu constraint, bukan dua kurva independen.

**Kegagalan tampilan.** Ukuran subjek ikut berubah atau background effect tidak jelas.

**Pemeriksaan.** Ukur subject bounds dan perubahan rasio objek kedalaman lain.

## M14.09 — Screen direction and axis

Arah layar membentuk orientasi tindakan dan hubungan antar subjek.

**Model / mekanisme.** Projected movement sign dapat berubah ketika camera melintasi axis.

**Implementasi.** Catat action axis dan desain crossing dengan motivasi visual.

**Kegagalan tampilan.** Gerak tampak membalik atau dua objek terlihat menuju arah sama tanpa sengaja.

**Pemeriksaan.** Review consecutive shots pada kecepatan normal dan tanpa audio.

## Penurunan mekanisme dan contoh terhitung

Pinhole: objek tinggi H pada jarak Z menghasilkan tinggi gambar h=fH/Z dalam satuan konsisten. Dengan H=2 m, Z=10 m dan f=50 mm, h=10 mm pada image plane. Jika kamera mundur menjadi 20 m dan f menjadi 100 mm, h tetap 10 mm, tetapi objek lain pada kedalaman berbeda tidak menjaga rasio yang sama. Inilah dasar coupled dolly-zoom.

Jika view direction sejajar world-up, cross product untuk right vector menjadi mendekati nol. Camera look-at perlu fallback up axis atau representasi orientasi yang tidak mengasumsikan cross product selalu valid.

## Kasus produksi

Shot produk dimulai sebagai detail lalu mengungkap bentuk keseluruhan. Tentukan projected product height 70% pada akhir dan margin 10%; solve jarak dari lens/aspect, bukan trial tanpa constraint. Gerakkan kamera melalui path dengan sedikit lateral translation untuk menunjukkan depth. Focus mengikuti label produk, lalu hold cukup untuk membaca.

## Memilih teknik dan trade-offs

Orthographic cocok untuk diagram dan konsistensi skala; perspective cocok untuk spatial cues. Camera path eksplisit cocok shot terarah; procedural target tracking cocok subjek berubah tetapi perlu filtering dan batas framing. Depth of field membantu fokus jika informasi yang kabur memang tidak diperlukan.

## Alur kerja operasional

1. Tulis fungsi shot dan informasi yang harus terlihat.
2. Pilih projection/lens serta framing endpoints.
3. Atur camera path dan target.
4. Periksa occlusion serta screen direction.
5. Atur focus/exposure integration bila digunakan.
6. Render shot penuh termasuk handles untuk editing.

## Verifikasi dan kriteria penguasaan

Penguasaan: mampu menyelesaikan framing dari constraints, membedakan zoom/dolly, memprediksi parallax, menghindari singularity look-at, dan mempertahankan informasi penting sepanjang shot. Kamera cantik pada thumbnail belum membuktikan trajectory nyaman ditonton.

## Cabang spesialis dalam cakupan

Lens distortion, anamorphic projection, panoramic/fisheye, rack focus, handheld noise dengan frequency band terkontrol, crane and gimbal models, camera collision, rolling shutter, lens breathing, multi-camera coverage, virtual production matching.

## Hubungan antardomain

[M03](../../architecture/master-map.md#m03), [M09](../../architecture/master-map.md#m09), [M11](../../architecture/master-map.md#m11), [M15](../../architecture/master-map.md#m15), [M21](../../architecture/master-map.md#m21).

## Jalur sumber

[R11](../../evidence/sources.md#r11), [R20](../../evidence/sources.md#r20), [R27](../../evidence/sources.md#r27).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.
