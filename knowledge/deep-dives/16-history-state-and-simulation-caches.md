# M16 — State history, integrator dan cache

## State identity

Simulation state mencakup positions/velocities/constraints/history yang dipakai model. Mengevaluasi frame 100 membutuhkan integrasi dari initial condition atau cache yang sesuai. Rendering random frame order tidak boleh mengonsumsi random state berbeda jika reproducibility diharapkan.

## Fixed clock

Pilih step h berdasarkan solver/model requirements; outputfps hanya sampling schedule. Pada24 fps, h1/240s memberi10steps per interval. Fractional cadence dapat memerlukan interpolation state. Interpolating position tanpa velocity/contact context dapat menghasilkan penetrasi walau cached endpoints valid.

## Cache key

Isi key: input geometry/config hashes, units, solver/version, timestep/substeps, seed, collisions, constraints dan relevant force settings. Code atau geometry berubah memerlukan invalidation sesuai dependency. Cache filename yang tetap bukan evidence matching inputs.

Hash mencatat identity bytes; ia tidak membuktikan physical accuracy. Solver-specific convergence/residual tests dibutuhkan untuk quality. Menyalin reportPASS lama ke cache baru menutup missing evidence secara palsu.

## Render versus resimulation

Retiming cache mengubah mapping action-time. Gerak terlihat lebih cepat, acceleration berubah, tetapi model forces tidak disimulasikan ulang. Untuk stylized shot itu dapat diterima; jika claim mekanisme fisik penting, tentukan apakah resim diperlukan.

## Actual branch

Critical spring memiliki analytic solution dengan fixed target, sehingga seeking tidak membutuhkan step-by-step replay. Tes residualODE memeriksa model terbatas tersebut. Cube scene memakai absolute-time transforms dan bukan dynamics simulation. Jadi ia tidak membuktikan collision/cloth/fluid caching.

## Verification

Render sampled state sequential dan random order; compare same-time state within stated tolerance. Halve timestep untuk convergence, inspect constraints/collisions serta visible jitter. Simpan evidence model, cache identity dan render output sebagai tiga concerns berbeda.

## Hubungan dan status

Konsep: M16.01, M16.05, M16.08, M16.09. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
