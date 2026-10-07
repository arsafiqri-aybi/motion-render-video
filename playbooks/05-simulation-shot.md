# Shot simulasi yang dapat diarahkan dan diulang

## Contract

Tetapkan primary event, material feel, contact locations serta informasi yang harus tetap terlihat. Simulation adalah mechanism; shot function menentukan bentuk yang dibutuhkan.

## Minimal model

Spring cocok response satu parameter. Procedural trajectory cocok controlled flight. Rigid bodies cocok contacts. Cloth/softbody cocok flexible surface, volume solver cocok smoke/fluid. Jangan menggunakan fluid simulation untuk effect yang dapat dibentuk texture flow tanpa kehilangan kebutuhan visual.

Nyatakan units, gravity, mass/inertia, material/constraint values dan boundary conditions. Collision proxies dapat berbeda dari mesh render; perbedaan ini perlu dipertimbangkan agar tidak ada visible gaps atau intersections.

## Numerical exploration

Uji kasus sederhana sebelum complex scene. Halve timestep, compare motion/energy/residual, serta test impacts ekstrem. Solver iterations bukan sinonim substeps. Timestep output video tidak langsung menjadi simulation timestep.

Seed emitter/agents secara stable. Kalau animation hanya dievaluasi dalam frame-order, test seeking untuk mengetahui kebutuhan cache. Bake/cache setelah scene parameters disetujui dan simpan hash/config/solver version. Mengubah parameter perlu invalidasi cache.

## Art direction

Sediakan semantic controls: impact strength, spread, settling, silhouette envelope. Hindari mengatur ratusan numeric knobs tanpa fungsi. Sekunder motion dekat teks dikurangi atau ditunda. Retiming cache dapat mengubah apparent acceleration; pertimbangkan resimulation bila hubungan gaya harus dijaga.

## QA

Review collisions, silhouette, jitter, temporal sampling dan render noise sebagai masalah terpisah. Cek cache against inputs, frame completeness dan same-time rerender. Repo memberikan model/derivation tetapi tidak mengklaim cloth/fluid engine sudah dijalankan. Domain M10/M13/M16/M17/M21/M22.
