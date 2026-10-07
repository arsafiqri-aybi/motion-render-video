# M18 — Compositing and Image Processing

## Manifestasi yang ditampilkan

Compositing menyusun gambar menjadi hasil akhir: foreground, background, mask, shadow, glow dan footage. Kesalahan pada alpha, color space, filter atau urutan operasi sering tampak sebagai halo, tepi gelap, double exposure dan detail yang hilang.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Mencakup layer operations, alpha, masks, mattes, blending, image filtering dan color-processing workflow. Pembentukan cahaya M08, color relationships M07, temporal sampling M21 dan output encoding M22 saling terhubung.

## Fondasi yang membentuk tampilan

Straight versus premultiplied alpha, source-over, working-space encoding, convolution, sampling kernels, numerical range, bit depth dan layer order. Data color, coverage, depth, normals dan motion vectors tidak boleh diperlakukan sebagai channel yang identik.

## M18.01 — Straight and premultiplied alpha

Convention alpha menentukan arti RGB pada pixel transparan.

**Model / mekanisme.** Premultiplied color c=alpha*C; RGB straight menyimpan C secara terpisah.

**Implementasi.** Tag input convention dan convert satu kali pada boundaries.

**Kegagalan tampilan.** Dark fringe, bright fringe atau double multiplication.

**Pemeriksaan.** Composite edge di atas hitam, putih dan saturated backgrounds.

## M18.02 — Source over and layer order

Foreground coverage menentukan bagian background yang tersisa.

**Model / mekanisme.** Premultiplied co=cs+cb(1-as); ao=as+ab(1-as).

**Implementasi.** Tetapkan order eksplisit dan handle opaque output dengan benar.

**Kegagalan tampilan.** Objek belakang muncul di depan atau opacity salah.

**Pemeriksaan.** Uji numeric pixel oracle serta swapped order case.

## M18.03 — Masks mattes and keying

Mask mengatur coverage berdasarkan geometry, channel atau selection.

**Model / mekanisme.** Coverage mask berbeda dari RGB luminosity dan key confidence.

**Implementasi.** Refine edge, preserve hair/detail bila relevan, handle spill terpisah.

**Kegagalan tampilan.** Edge chatter, holes atau color contamination.

**Pemeriksaan.** Inspect matte sendiri dan hasil di beberapa backgrounds.

## M18.04 — Blend modes and operation space

Multiply, screen dan add membentuk hubungan tonal yang berbeda.

**Model / mekanisme.** Formula bergantung normalized range dan working space; modes nonlinear.

**Implementasi.** Nyatakan blend mode, channel range dan transfer convention.

**Kegagalan tampilan.** Tampilan berubah antar aplikasi walau angka sama.

**Pemeriksaan.** Compare reference pixels dan intermediate layers.

## M18.05 — Convolution blur and sharpening

Filter menggabungkan spatial samples untuk mengubah bandwidth.

**Model / mekanisme.** Kernel normalized mempertahankan flat-field intensity; boundary modes memengaruhi tepi.

**Implementasi.** Blur premultiplied RGB/alpha bersama; sharpening jangan clip terlalu awal.

**Kegagalan tampilan.** Halo, edge bleeding dan ringing.

**Pemeriksaan.** Uji impulse, constant field dan high-contrast edge.

## M18.06 — Color correction and grading

Correction menjaga kesesuaian; grading mengarahkan hubungan tampilan.

**Model / mekanisme.** Transfer functions, matrices, curves dan LUT mempunyai domain input.

**Implementasi.** Tetapkan scene/display-referred boundary dan transform order.

**Kegagalan tampilan.** Skin/brand color drift, crushed shadows atau clipping.

**Pemeriksaan.** Scope channels dan compare neutral/brand patches.

## M18.07 — Depth motion and auxiliary passes

Data passes memungkinkan efek mengikuti scene relationships.

**Model / mekanisme.** Depth units dan motion-vector direction/timebase harus jelas.

**Implementasi.** Gunakan data types tanpa color transform; simpan validity dan coordinate convention.

**Kegagalan tampilan.** Depth blur terbalik atau vector blur salah arah.

**Pemeriksaan.** Uji scene sederhana dengan known depth serta translation.

## M18.08 — Resolution resampling and crop

Resize membentuk pixel baru dari footprint sumber.

**Model / mekanisme.** Downsampling memerlukan low-pass filtering; crop mengubah framing.

**Implementasi.** Pilih kernel dan aspect policy; recompute safe areas.

**Kegagalan tampilan.** Moire, soft text atau silent stretch.

**Pemeriksaan.** Check grid/circle references dan target-size readability.

## M18.09 — Precision ranges and pipeline checkpoints

Intermediate precision menjaga headroom serta repeatability.

**Model / mekanisme.** Repeated quantization menambah rounding error dan dapat membentuk banding.

**Implementasi.** Gunakan float intermediates bila diperlukan, capture selected passes.

**Kegagalan tampilan.** Banding, NaN, out-of-range channels atau irrecoverable clipping.

**Pemeriksaan.** Scan finite values, extrema dan roundtrip samples.

## Penurunan mekanisme dan contoh terhitung

Foreground straight C=(1,0,0), alpha=0.5 menjadi premultiplied cs=(0.5,0,0). Background opaque blue cb=(0,0,1), ab=1. Source-over memberikan co=(0.5,0,0.5), ao=1. Jika cs keliru dikali alpha lagi, merah menjadi 0.25: penyebab tepi gelap. Formula ini diasumsikan memakai working space yang sama; numeric color mixing pada encoded values tidak otomatis sama dengan mixing radiance.

Dua blur berturut-turut tidak sama dengan alpha mask yang diblur sendiri lalu dipasang ke RGB straight lama. RGB dari wilayah transparan dapat bocor kecuali convention ditangani.

## Kasus produksi

Title transparan di atas footage dikirim ke editor. Buat test tile alpha gradient dan edge anti-alias; ekspor format yang benar-benar mendukung alpha; dokumentasikan straight/premult convention. Render proof composites pada background terang dan gelap. MP4 umum yuv420p tidak dipakai sebagai alpha master.

## Memilih teknik dan trade-offs

Premultiplied workflow nyaman untuk filtering dan compositing. Straight dapat cocok interchange tertentu tetapi boundaries wajib eksplisit. Float intermediates menjaga headroom; 8-bit cukup untuk beberapa flat graphic outputs tetapi banding perlu dinilai. LUT bukan pengganti metadata color space.

## Alur kerja operasional

1. Inventaris layer dan data convention.
2. Tetapkan working space serta precision.
3. Composite dalam order yang terdokumentasi.
4. Tambahkan filter/grade pada domain tepat.
5. Periksa edges, scopes dan intermediate passes.
6. Konversi ke output space sekali pada boundary yang dirancang.

## Verifikasi dan kriteria penguasaan

Penguasaan: mampu menghitung source-over, mendiagnosis alpha fringe, menjelaskan operation order dan memeriksa data passes tanpa color transform. Pixel oracle menguji formula tertentu; ia tidak membuktikan keseluruhan compositing shot.

## Cabang spesialis dalam cakupan

Deep compositing, spectral workflows, cryptomatte, rotoscoping, despill, optical flow, frequency separation, reconstruction filters, bilateral/edge-aware filters, HDR tone mapping, gamut mapping, OCIO configurations.

## Hubungan antardomain

[M07](../../architecture/master-map.md#m07), [M08](../../architecture/master-map.md#m08), [M15](../../architecture/master-map.md#m15), [M17](../../architecture/master-map.md#m17), [M21](../../architecture/master-map.md#m21), [M22](../../architecture/master-map.md#m22).

## Jalur sumber

[R15](../../evidence/sources.md#r15), [R16](../../evidence/sources.md#r16), [R32](../../evidence/sources.md#r32).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.

## Pendalaman produksi

[Depth, alpha dan auxiliary pass conventions](../deep-dives/18-depth-alpha-and-pass-conventions.md) — decision/model/counterexample yang melengkapi chapter ini.
