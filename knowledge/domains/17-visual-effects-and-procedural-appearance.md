# M17 — Visual Effects and Procedural Appearance

## Manifestasi yang ditampilkan

Efek membentuk hal yang terlihat: glow, sparks, smoke, trails, texture flow, glitch atau stylized energy. Tujuannya bukan menumpuk filter, melainkan mengatur bentuk, lokasi, intensitas dan timing supaya mendukung identitas serta informasi.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Mencakup procedural textures, field-based shapes, stylization dan effect systems. Transport fisik di M16, light/material di M08, image operations/compositing di M18. Efek screen-space mempunyai batas visibility dan resolusi yang berbeda dari scene-space.

## Fondasi yang membentuk tampilan

Field skalar/vektor, sampling, noise coherence, signed distance, threshold, convolution, frequency dan deterministic parameterization. Effect intensity perlu dipisahkan dari exposure serta alpha agar kontrol tidak tercampur.

## M17.01 — Signed distance shapes

Field jarak memberi batas bentuk yang dapat dimodulasi secara kontinu.

**Model / mekanisme.** f(x)<0 berada di dalam bentuk; coverage memakai filter di sekitar zero crossing.

**Implementasi.** Gunakan analytic distance sesuai geometry dan smoothing sesuai pixel footprint.

**Kegagalan tampilan.** Edge terlalu keras, stroke tidak rata atau distance tidak lagi benar setelah warp.

**Pemeriksaan.** Uji contour dan gradient pada simple shapes.

## M17.02 — Noise textures and flow

Coherent noise menghubungkan detail antar ruang dan waktu.

**Model / mekanisme.** Spatial frequency dan temporal frequency menentukan scale serta speed.

**Implementasi.** Gunakan seeded continuous fields dan advect koordinat secara terkendali.

**Kegagalan tampilan.** Flicker, texture swimming dan detail tenggelam saat encode.

**Pemeriksaan.** Bandingkan frame berdekatan serta downscaled delivery.

## M17.03 — Glow bloom and halos

Cahaya terang tampak menyebar di sekitar sumber.

**Model / mekanisme.** Thresholded radiance atau mask dikonvolusi, lalu ditambahkan menurut working space.

**Implementasi.** Pisahkan core, halo radius dan intensity; blur premultiplied data bila alpha.

**Kegagalan tampilan.** Semua menjadi kabut, text kehilangan contrast dan highlight clipped.

**Pemeriksaan.** Ukur area terang dan cek readability sebelum/sesudah glow.

## M17.04 — Trails echoes and motion marks

Jejak menyimpan informasi posisi lampau.

**Model / mekanisme.** Trail dapat berupa sampled trajectory atau temporal accumulation.

**Implementasi.** Tetapkan decay dalam detik dan clear behavior saat scene cut.

**Kegagalan tampilan.** Ghosts menembus scene berikutnya atau length bergantung fps.

**Pemeriksaan.** Uji fps berbeda, cue cuts dan alpha accumulation.

## M17.05 — Displacement distortion and refraction

Koordinat sampling membelok sehingga image memberi kesan medium lain.

**Model / mekanisme.** UV'=UV+d(UV,t), dengan offset units dan edge handling eksplisit.

**Implementasi.** Pakai low-frequency displacement untuk mass dan detail kecil terpisah.

**Kegagalan tampilan.** Pixel stretching, holes dan pattern shimmer.

**Pemeriksaan.** Render checker test dan inspect border behavior.

## M17.06 — Glitch and digital stylization

Gangguan sengaja memakai discontinuity spasial/temporal yang terarah.

**Model / mekanisme.** Block offset, channel offsets dan hold frames adalah operators berbeda.

**Implementasi.** Kaitkan glitch pada cue, batasi wilayah serta durasi.

**Kegagalan tampilan.** Efek tampak seperti error delivery atau menyulitkan pembacaan.

**Pemeriksaan.** Bandingkan dengan versi bersih dan tinjau viewing comfort.

## M17.07 — Particle appearance and sprite shading

Partikel memperoleh identitas dari shape, size, opacity, color dan depth.

**Model / mekanisme.** Life-normalized curves mengatur appearance selain trajectory.

**Implementasi.** Precompute atlas atau procedural sprite, tentukan blend/order.

**Kegagalan tampilan.** Kartu sprite terlihat, popping opacity dan sorting salah.

**Pemeriksaan.** Inspect isolated particles, overlap dan lifespan extremes.

## M17.08 — Volumetric effects and atmospheric depth

Volume mengubah visibility melalui absorption dan scattering.

**Model / mekanisme.** Beer-Lambert transmittance T=exp(-integral sigma_t ds) dalam model yang sesuai.

**Implementasi.** Pilih density, phase function, sample count dan light coupling.

**Kegagalan tampilan.** Banding, noise, volume datar atau terlalu pekat.

**Pemeriksaan.** Sweep step size dan compare transmittance kasus homogen.

## M17.09 — Effect stacks and parameter exposure

Beberapa efek membutuhkan urutan serta shared controls yang dapat dijelaskan.

**Model / mekanisme.** Nonlinear operators biasanya tidak commute.

**Implementasi.** Dokumentasikan stack dan expose semantic controls, bukan ratusan angka tanpa unit.

**Kegagalan tampilan.** Efek saling memperkuat hingga clipping atau tidak dapat diperbaiki lokal.

**Pemeriksaan.** Toggle per-layer dan simpan reference intermediate.

## Penurunan mekanisme dan contoh terhitung

Untuk volume homogen dengan extinction sigma=0.5 per meter dan panjang lintasan 2 m, T=exp(-1)≈0.3679. Alpha coverage geometris tidak identik dengan extinction volume; memakai opacity konstan per langkah tanpa koreksi step size membuat volume berubah ketika sample count berubah.

Trail decay a(t+dt)=a(t)*exp(-lambda*dt) menjaga half-life ln(2)/lambda dalam detik. Faktor tetap 0.9 per frame pada 24 dan 60 fps menghasilkan decay berbeda. Jika half-life 0.2 s, lambda≈3.4657 per detik.

## Kasus produksi

Energi mengikuti kontur logo. Gunakan path-space coordinates agar flow melekat pada bentuk; core tipis dan halo lembut; sparks hanya di cue utama. Batasi brightness saat headline muncul. Render versi tanpa bloom untuk mengecek apakah desain dasarnya masih dapat dibaca.

## Memilih teknik dan trade-offs

Procedural fields cocok resolusi fleksibel dan parameterization. Sprite assets cocok tampilan khusus dengan biaya asset management. Screen-space effect lebih sederhana tetapi tidak mengetahui geometry tersembunyi. Volume memberi spatial interaction dengan biaya sampling serta noise.

## Alur kerja operasional

1. Nyatakan fungsi efek dan visual anchor.
2. Bangun core silhouette dulu.
3. Tambahkan detail dan temporal variation.
4. Uji sampling serta alpha conventions.
5. Integrasikan stack dengan compositing.
6. Periksa encoded output, bukan hanya preview.

## Verifikasi dan kriteria penguasaan

Penguasaan: dapat menjaga effect scale terhadap resolution, menjelaskan decay berbasis waktu, mengisolasi halo/core, serta memilih space yang tepat. Keindahan efek dan keberhasilan komunikasi perlu dinilai bersama.

## Cabang spesialis dalam cakupan

Reaction-diffusion, curl noise, domain warping, fractals, ray marching, participating media, procedural fire, stylized lightning, chromatic aberration, lens flares, bokeh synthesis, temporal accumulation, effect baking.

## Hubungan antardomain

[M05](../../architecture/master-map.md#m05), [M07](../../architecture/master-map.md#m07), [M08](../../architecture/master-map.md#m08), [M16](../../architecture/master-map.md#m16), [M18](../../architecture/master-map.md#m18), [M21](../../architecture/master-map.md#m21).

## Jalur sumber

[R11](../../evidence/sources.md#r11), [R18](../../evidence/sources.md#r18), [R31](../../evidence/sources.md#r31).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.

## Pendalaman produksi

[Fields, effects dan frequency control](../deep-dives/17-fields-effects-and-frequency-control.md) — decision/model/counterexample yang melengkapi chapter ini.
