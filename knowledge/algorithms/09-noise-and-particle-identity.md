# Seeded identity dan continuous variation

## Masalah

Render frame70 lalu frame10 menghasilkan pola berbeda dari render sequential. Penyebab lazim adalah global PRNG yang dikonsumsi sesuai call order.

## Identity-first model

Tiap particle mempunyai stable id, birth time, lifetime serta parameter random yang diturunkan dari seed+id. Scene evaluation menghitung age=t-birth; particles aktif jika0<=age<lifetime. Parameter velocity/color/size tidak diacak ulang saat draw. Output frame order tidak mengubah identity.

Untuk generator particle births konstan, derive id range dari time atau precompute manifest. Bila collision/interactions membuat history matters, identity saja belum cukup; simulation state perlu cache atau deterministic replay dengan timestep tetap.

## Continuous variation

Independent random per frame memberi temporal white-noise-like behavior dan flicker. Smooth noise/oscillators mempunyai correlation serta frequency scale. Gerak y=A*sin(2*pi*f*t+phi) mempunyai max speed2*pi*f*A dan acceleration(2*pi*f)²*A; menaikkan f sedikit dapat menambah acceleration besar. Jangan memilih amplitude/frequency hanya lewat static noise preview.

Noise displacement pada shape dapat menambah spatial high frequencies. Batasi band berdasarkan target resolution dan temporal cadence. Animating noise coordinates tidak otomatis band-limited; test encoded playback.

## Reproducibility policy

Record seed, generator algorithm, particle id rule dan timestep. Same seed across different PRNG implementations tidak menjamin same values. Pixel hash equivalence dapat terlalu ketat lintas hardware untuk floating pipelines; gunakan scope tolerance yang dinyatakan.

## Pemeriksaan

Render random-order frames lalu compare same-time state. Uji birth/death boundaries dan scene cuts agar trails tidak leak. Inspect pattern distribution serta art direction; deterministic bukan berarti visual sudah bagus. [M16](../domains/16-physical-procedural-and-secondary-motion.md), [M17](../domains/17-visual-effects-and-procedural-appearance.md).
