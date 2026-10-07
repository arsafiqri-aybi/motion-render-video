# M21 — Rendering and Temporal Image Formation

## Manifestasi yang ditampilkan

Video terbentuk dari sequence images yang masing-masing mewakili hasil sampling ruang dan waktu. Sharpness, blur, aliasing, noise, detail, exposure dan artifacts adalah konsekuensi pilihan renderer serta sampling; bukan sekadar pilihan ekspor.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Mencakup raster/vector/ray-based image generation, spatial/temporal sampling, shutter, antialiasing, passes, rendering precision dan compute strategy yang menentukan video. Encoding serta playback timestamps dikelola M22. Real-time GPU digunakan sejauh mendukung output video, bukan seluruh computer systems engineering.

## Fondasi yang membentuk tampilan

Pixel footprint, reconstruction, sample distribution, visibility, radiance, exposure interval, temporal frequency dan deterministic evaluation. Scene state pada satu waktu berbeda dari image yang mengintegrasikan interval shutter.

## M21.01 — Raster vector and ray-based rendering

Renderer memakai representasi dan visibility algorithms berbeda.

**Model / mekanisme.** Raster projects primitives; vector rasterizes paths; ray tracing samples visibility/light transport.

**Implementasi.** Pilih output-driven renderer dan maintain world/screen conventions.

**Kegagalan tampilan.** Layer order, missing shadows atau edges berbeda dari intent.

**Pemeriksaan.** Gunakan reference scene sederhana untuk representation chosen.

## M21.02 — Spatial sampling and antialiasing

Pixel mewakili footprint, bukan titik geometry dengan ukuran nol.

**Model / mekanisme.** Supersampling dan filtering memperkirakan coverage/integral.

**Implementasi.** Pilih sample count/kernel dan ukur target-resolution edges.

**Kegagalan tampilan.** Jagged edges, moire atau excessive softness.

**Pemeriksaan.** Sweep resolution/sample count dan inspect moving edges.

## M21.03 — Temporal sampling and shutter

Blur terbentuk dari integrasi scene berubah selama exposure.

**Model / mekanisme.** I_n≈sum w_k R(scene(t_n+offset_k)); weights berjumlah satu.

**Implementasi.** Nyatakan shutter duration, alignment dan samples; jangan blur seluruh frame tanpa motion model.

**Kegagalan tampilan.** Trails salah arah, endpoint smear dan blur terlalu berat.

**Pemeriksaan.** Bandingkan known constant-velocity segment dengan expected displacement.

## M21.04 — Frame rate cadence and time evaluation

Output fps menentukan sample cadence, bukan otomatis animation speed.

**Model / mekanisme.** t_n=n*q/p untuk fps=p/q; sequence interval biasanya half-open.

**Implementasi.** Evaluate state dari absolute time atau fixed-step cache.

**Kegagalan tampilan.** Gerak lebih cepat di60fps atau endpoint duplicated.

**Pemeriksaan.** Render rates berbeda lalu compare same-time states.

## M21.05 — Motion vectors and temporal reprojection

History pixels dapat digunakan untuk temporal filtering dengan mapping gerak.

**Model / mekanisme.** Vectors memetakan previous/current positions dengan direction convention.

**Implementasi.** Reject history saat disocclusion dan gunakan validity/anti-ghosting.

**Kegagalan tampilan.** Ghosts, smearing dan stale pixels.

**Pemeriksaan.** Test moving occluder, camera cuts dan vector direction.

## M21.06 — Noise convergence and denoising

Monte Carlo noise berbeda dari deterministic texture.

**Model / mekanisme.** Ideal independent sample averaging menurunkan variance sekitar 1/N.

**Implementasi.** Simpan sample count/seeds; evaluate denoiser detail stability.

**Kegagalan tampilan.** Temporal crawling, lost highlights dan flickering detail.

**Pemeriksaan.** Compare temporal sequences dan higher-sample references.

## M21.07 — Render passes and dependency scheduling

Passes menyediakan intermediate data untuk compositing atau diagnostics.

**Model / mekanisme.** Dependency graph menentukan valid execution order serta resource lifetime.

**Implementasi.** Document pass format, units, color/data role dan cache dependencies.

**Kegagalan tampilan.** Stale pass, mismatched times dan nondeterministic render.

**Pemeriksaan.** Hash config serta compare selected frames from clean runs.

## M21.08 — Precision color and accumulation

Arithmetic/encoding menentukan apakah averaging mencerminkan light atau code values.

**Model / mekanisme.** Linear-light accumulation berbeda dari averaging nonlinear encoded channels.

**Implementasi.** Convert to defined linear space when approximating radiance integration.

**Kegagalan tampilan.** Dark blur edges, clipped highlights atau banding.

**Pemeriksaan.** Use numeric color oracle plus rendered patches.

## M21.09 — CPU GPU resource and deterministic execution

Hardware/pipeline menentukan feasibility dan repeatability.

**Model / mekanisme.** Parallel reduction order dan floating precision dapat menghasilkan small differences.

**Implementasi.** Define tolerance; control seeds, libraries, versions and resource budgets.

**Kegagalan tampilan.** OOM, missing frames atau bitwise differences dianggap semuanya error.

**Pemeriksaan.** Track complete frame set, finite pixels dan reproducibility policy.

## Penurunan mekanisme dan contoh terhitung

Shutter angle theta pada frame rate f memberi exposure T=theta/(360*f) jika model memakai angle relatif frame interval. Pada 30 fps dan180°, T=1/60 s. Objek constant speed120 px/s bergerak2 px selama exposure. Render midpoint tunggal tidak menghasilkan blur2px; beberapa samples atau analytic integration diperlukan.

Nyquist membantu sinyal band-limited: frekuensi di atas f/2 tidak dapat direkonstruksi unik dari sampling seragam f. Kontur bergerak dan visibility changes bukan selalu band-limited. Motion blur dapat mengurangi beberapa temporal high frequencies, tetapi tidak menjamin semua aliasing hilang.

RGBA compositing dan temporal accumulation membutuhkan convention space yang eksplisit. Demo repo menyatakan approximation yang dipakai; ia bukan physically based path tracer.

## Kasus produksi

Flat motion graphic merender180frames pada30fps. State dihitung dari n/30 agar seeking konsisten. Empat temporal samples dipakai untuk moving graphic; color accumulation dilakukan setelah inverse transfer sesuai convention demo. Frames diekspor lalu di-encode dengan metadata yang dinyatakan. Diperiksa frame count, cadence, dimensions, stream duration dan full decode.

## Memilih teknik dan trade-offs

Single sample murah dan tajam tetapi dapat strobe. Temporal supersampling lebih mahal dan tidak selalu cocok teks yang perlu stabil. Ray tracing cocok light interactions; raster/vector cocok graphic precision. Denoiser mempercepat practical convergence tetapi wajib dicek temporal stability. Jangan membeli kompleksitas GPU jika CPU cukup untuk tujuan.

## Alur kerja operasional

1. Tetapkan scene evaluator dan exact output clock.
2. Pilih rendering/sampling representation.
3. Nyatakan shutter serta color accumulation.
4. Render tests dengan known geometry/motion.
5. Run full sequence dengan resource/provenance log.
6. Verify frame set dan inspect encoded playback.

## Verifikasi dan kriteria penguasaan

Penguasaan: mampu memprediksi shutter footprint, membedakan frame cadence/simulation steps/exposure, menjelaskan aliasing, dan mendiagnosis render noise versus compression artifacts. Tes demo membuktikan pipeline kecil, bukan semua teknik GPU/3D.

## Cabang spesialis dalam cakupan

Path tracing, MIS, bidirectional transport, spectral rendering, differentiable rendering, adaptive sampling, temporal antialiasing, blue-noise distributions, rolling-shutter sampling, distributed rendering, render farms, compute shaders, tiled memory pipelines.

## Hubungan antardomain

[M07](../../architecture/master-map.md#m07), [M08](../../architecture/master-map.md#m08), [M10](../../architecture/master-map.md#m10), [M11](../../architecture/master-map.md#m11), [M18](../../architecture/master-map.md#m18), [M22](../../architecture/master-map.md#m22).

## Jalur sumber

[R11](../../evidence/sources.md#r11), [R19](../../evidence/sources.md#r19), [R20](../../evidence/sources.md#r20), [R23](../../evidence/sources.md#r23), [R31](../../evidence/sources.md#r31).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.
