# M16 — Physical Procedural and Secondary Motion

## Manifestasi yang ditampilkan

Gerak sekunder memberi respons: rambut mengikuti kepala, kain tertinggal, partikel menyebar, kartu bergetar setelah impact. Simulasi atau prosedur menyediakan dinamika yang kemudian dipilih dan diarahkan untuk kebutuhan video.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Mencakup springs, rigid/soft bodies, cloth, fluids, particles, noise dan agents bila hasilnya menjadi video. Engineering robot atau gameplay bukan tujuan utama. Solver dan field yang tidak terlihat dibahas sejauh menentukan tampilan, stabilitas dan reproducibility.

## Fondasi yang membentuk tampilan

State, force, timestep, constraints, damping, collision geometry, seeded random serta sampling output. Simulation clock dapat berbeda dari video clock. Art direction dapat mengubah parameter fisik dengan asumsi jelas.

## M16.01 — Springs and damped response

Gaya pemulih dan damping membentuk oscillation atau settling.

**Model / mekanisme.** m x''+c x'+k(x-target)=0 dengan damping ratio c/(2 sqrt(mk)).

**Implementasi.** Gunakan analytic solution untuk target tetap; integrator untuk forcing umum.

**Kegagalan tampilan.** Overshoot tidak diinginkan, energi meledak atau response terlalu lambat.

**Pemeriksaan.** Ukur settling, peak overshoot dan perubahan timestep.

## M16.02 — Rigid bodies and contact

Benda padat menampilkan trajectory serta perubahan gerak akibat kontak.

**Model / mekanisme.** Momentum, angular momentum dan contact impulses tergantung mass/inertia.

**Implementasi.** Pilih collision proxy, friction dan restitution yang sesuai shot.

**Kegagalan tampilan.** Penetration, jitter atau benda memantul tanpa berat.

**Pemeriksaan.** Visualize contacts dan cek momentum pada kasus tanpa external force.

## M16.03 — Cloth and flexible surfaces

Permukaan fleksibel dipengaruhi bending, stretch, gravity dan contact.

**Model / mekanisme.** Constraint lengths/angles atau energy gradients mengatur deformation.

**Implementasi.** Gunakan substeps, collision thickness dan attachment constraints.

**Kegagalan tampilan.** Cloth menembus, stretching berlebihan dan high-frequency jitter.

**Pemeriksaan.** Bandingkan mesh resolution/timestep serta inspeksi silhouette.

## M16.04 — Fluids smoke and volume motion

Aliran membentuk coherent transport, vortices dan diffusion.

**Model / mekanisme.** Advection memindahkan quantity mengikuti velocity field; pressure solve mengatur divergence.

**Implementasi.** Pilih grid/particle hybrid serta boundary conditions.

**Kegagalan tampilan.** Volume menghilang, bocor dan detail bergantung grid secara tak terkendali.

**Pemeriksaan.** Periksa mass surrogate, divergence dan convergence scene sederhana.

## M16.05 — Particles emitters and lifetime

Banyak elemen membentuk jejak, ledakan atau atmosfer.

**Model / mekanisme.** Particle identity mempunyai birth time, lifetime dan state.

**Implementasi.** Seed per-id, pisahkan spawn dari frame evaluation dan batasi jumlah.

**Kegagalan tampilan.** Pop, pola berubah tiap render atau partikel hidup tak terhingga.

**Pemeriksaan.** Render frame acak versus sequential dan cek birth/death boundaries.

## M16.06 — Noise fields and procedural oscillation

Variasi terstruktur menghasilkan irregularity dengan skala yang dapat dikontrol.

**Model / mekanisme.** Band-limited fields berbeda dari independent random per frame.

**Implementasi.** Batasi amplitude/frequency dan gunakan continuous time evaluation.

**Kegagalan tampilan.** Flicker, tremor atau drift yang merusak framing.

**Pemeriksaan.** Plot spectrum kasar dan playback pada beberapa frame rates.

## M16.07 — Secondary follow-through

Bagian mengikuti perubahan utama dengan lag dan settling.

**Model / mekanisme.** Filter atau spring driven target membentuk response bergantung history.

**Implementasi.** Cache state simulation atau derive closed form pada segment diketahui.

**Kegagalan tampilan.** Secondary motion menyalip pesan utama atau tidak reproducible saat seeking.

**Pemeriksaan.** Test interruption, seek dan cue hierarchy.

## M16.08 — Constraint and timestep management

Solver menentukan stabilitas visual dan pemenuhan constraint.

**Model / mekanisme.** Integrator error serta solver iterations bergantung h dan stiffness.

**Implementasi.** Jalankan fixed substeps; map output time ke simulation state secara eksplisit.

**Kegagalan tampilan.** Gerak berbeda ketika fps berubah atau constraint gagal di impact.

**Pemeriksaan.** Halve timestep dan bandingkan trajectory serta constraint residual.

## M16.09 — Art direction caching and reproducibility

Hasil fisik menjadi asset yang perlu dapat diulang dan dikoreksi.

**Model / mekanisme.** Cache identity mencakup inputs, solver version, seed dan timestep.

**Implementasi.** Simpan provenance dan pilih shot timing tanpa mengubah cache diam-diam.

**Kegagalan tampilan.** Cache stale, rerender berbeda dan final frame tidak match preview.

**Pemeriksaan.** Hash input/config dan rerender sample frames dari cache.

## Penurunan mekanisme dan contoh terhitung

Untuk oscillator tanpa damping dengan symplectic Euler: v_next=v-h*omega²*x; x_next=x+h*v_next. Trace matriks update adalah 2-(h*omega)² dan determinant 1. Batas linear stability untuk kasus ini adalah 0<h*omega<2, dengan boundary tidak menjamin hasil akurat. Ini bukan aturan universal semua solver.

Jika output 30 fps dan simulation 240 Hz, ada delapan substeps per frame interval. Menurunkan output menjadi 24 fps tidak boleh otomatis mengubah physics timestep. Sampling atau interpolasi state harus didefinisikan agar rendering tidak mengubah dinamika.

## Kasus produksi

Sekumpulan kartu jatuh lalu headline muncul. Simulasikan kartu sampai kontak tenang, cache hasil, retime reveal sesuai cerita. Kurangi secondary motion dekat teks. Jika exact collision tidak penting, gunakan trajectory procedural yang mudah diarahkan; jangan membayar kompleksitas solver tanpa manfaat tampilan.

## Memilih teknik dan trade-offs

Analytic spring baik untuk response sederhana dan seeking. Fixed-step simulation cocok contacts dan forcing kompleks. Noise field cocok variation tanpa physical identity. Cache cocok final production; live simulation cocok exploration tetapi harus dibekukan atau diverifikasi sebelum delivery.

## Alur kerja operasional

1. Pisahkan primary action dan secondary response.
2. Nyatakan parameter, units dan boundaries.
3. Pilih model minimum yang memenuhi tampilan.
4. Uji stability pada timestep lebih kecil.
5. Cache dengan provenance.
6. Render dan nilai apakah secondary membantu pesan.

## Verifikasi dan kriteria penguasaan

Penguasaan: mampu menjelaskan perbedaan model, integrator dan output sampling; mendiagnosis energy growth; menjaga deterministic seeds; serta mengarahkan secondary motion tanpa mengacaukan headline. Contoh numeric stability bukan sertifikasi solver semua scene.

## Cabang spesialis dalam cakupan

XPBD, position-based dynamics, finite elements, material point methods, PIC/FLIP, vorticity confinement, multigrid, continuous collision detection, flocking, turbulence synthesis, differentiable simulation, simulation-to-keyframe baking.

## Hubungan antardomain

[M10](../../architecture/master-map.md#m10), [M11](../../architecture/master-map.md#m11), [M13](../../architecture/master-map.md#m13), [M17](../../architecture/master-map.md#m17), [M21](../../architecture/master-map.md#m21), [M22](../../architecture/master-map.md#m22).

## Jalur sumber

[R22](../../evidence/sources.md#r22), [R26](../../evidence/sources.md#r26), [R30](../../evidence/sources.md#r30).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.

## Pendalaman produksi

[State history, integrator dan cache](../deep-dives/16-history-state-and-simulation-caches.md) — decision/model/counterexample yang melengkapi chapter ini.
