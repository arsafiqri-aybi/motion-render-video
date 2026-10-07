# M11 — Contract clock, cadence dan exposure

## Empat waktu

Story time menjelaskan progress cerita. Scene time mengatur states. Simulation time mengintegrasikan dynamics. Exposure time mengintegrasikan gambar. Output PTS mengatur presentation cadence. Mapping di antaranya harus eksplisit, bukan memakai wall-clock render duration.

## Actual3D example

96 frame pada24 fps mencakup4s; frame terakhir95/24≈3.958333s. Shutter180° memberi exposure1/48s. Dua midpoint samples forward berada di95/24+1/192 dan95/24+3/192, keduanya sebelum4s. Itulah alasan scene evaluator memiliki meaningful state untuk semua samples.

Preview render yang membutuhkan lebih dari4s tetap menghasilkan video4s. Performance wall clock tidak mengubah animation speed. Seek frame 40 mengevaluasi t40/24, bukan meneruskan frame counter dari render sebelumnya.

## Stateful mapping

Simulations membutuhkan state history/cache; arbitrary seek tidak dapat hanya mengevaluasi differential forces tanpa integration. Bila output24 fps dan physics240Hz, ada10substeps per frame interval. Jika fractional rates tidak memberi integer ratio, interpolate/cache dengan declared policy. Jangan mengganti physics timestep diam-diam ketika ekspor fps berubah.

## Cadence checks

Probe decoded PTS bukan hanya nominal tag fps. Require count, monotonically increasing timestamps, spacing serta duration yang sesuai. Variable frame rate mempunyai timestamp grid berbeda; avg_frame_rate saja tidak membuktikan per-frame cadence.

## Exposure checks

Cadence tetap tetapi exposure berbeda dapat memberi sharp/strobing versus blurred motion. Inspect moving edge dan reading windows; shutter merupakan image formation choice, bukan duration timeline. Demo3D actual checks memverifikasi CFR/cadence; tidak menyatakan universal comfort pada24 fps.

Simpan rational p/q bila fractional rate digunakan dan bedakan timeline intervals dari last sample timestamp.

## Hubungan dan status

Konsep: M11.01, M11.03, M11.07, M11.09. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
