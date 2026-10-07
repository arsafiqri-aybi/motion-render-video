# Fondasi yang bekerja di balik tampilan

## Representasi dan unit

Tentukan apakah posisi berada dalam world units, pixels atau normalized coordinates. Jangan menjumlahkan seconds dengan frames, radians dengan degrees, atau straight RGB dengan premultiplied RGB. Variable harus membawa arti dan unit walaupun bahasa pemrograman tidak mempunyai unit type. Pilihan convention bukan masalah kosmetik; ia menentukan arti setiap operasi.

Untuk aspect adaptation, normalized layout dapat dipakai sebagai awal. Ukuran glyph, stroke dan safe margins tetap perlu constraints pada output pixels. Scaling semua koordinat secara identik dapat membuat label terlalu kecil atau perspective berubah bila aspect ikut berubah.

## Fungsi terhadap waktu

Scene evaluator murni `state(t, config)` memungkinkan frame di-render acak dan reproducible. Animation phase `u=clamp((t-start)/duration,0,1)` memisahkan clock dari motion model. Timing curve mengubah phase; geometry curve mengubah posisi. State-history models seperti collision simulation membutuhkan integrasi/cache, bukan sekadar evaluasi titik waktu tanpa state.

Untuk output fps=p/q, sample time frame n adalah n*q/p. Timestep simulation, shutter exposure dan frame interval memiliki fungsi berbeda. Setiap kali berpindah antar clock, dokumentasikan mapping serta rounding.

## Kalkulus yang terlihat

Position x(t) mempunyai velocity x'(t), acceleration x''(t), dan jerk d³x/dt³. Endpoint yang sama tidak membuat response sama. Curve dengan velocity endpoint nonzero akan membentur hold statis dengan discontinuity velocity. Quintic smootherstep dapat memberi zero velocity serta acceleration pada endpoints untuk scalar interpolation, tetapi tidak menentukan choreography yang baik dengan sendirinya.

Untuk path P(u(t)), velocity dP/dt=P'(u)*u'(t). Jika P'(u) berubah panjang, linear u tidak berarti constant speed. Arc-length mapping membantu memisahkan geometry dari travel speed.

## Algebra dan transforms

Homogeneous matrices menggabungkan translation, rotation, scale dan projection dengan conventions yang dinyatakan. Di column-vector convention, operasi paling kanan terjadi dahulu. Parent-child transform menghasilkan world=M_parent*M_local. Nonuniform scale sebelum rotation tidak identik dengan setelah rotation. Uji invariant pivot dan landmarks untuk mendeteksi urutan salah.

Quaternion menghindari sebagian masalah representasi Euler tetapi tidak memilih seluruh artistic path otomatis. q dan -q memiliki orientasi sama; hemisphere selection membantu shortest interpolation. Putaran sengaja lebih dari180° perlu informasi tambahan.

## Probabilitas dan prosedur

Random state per frame membuat seeking dan rerender bergantung urutan. Gunakan seeded identity per event/particle, atau sample field kontinu. Deterministic seed tidak berarti seluruh arithmetic bitwise-identical across machines. Nyatakan policy: exact structural state, numeric tolerance, image perceptual tolerance atau byte hash.

Noise visual yang dirancang berbeda dari Monte Carlo render noise. Menambah samples dapat mengurangi yang kedua tetapi tidak seharusnya menghapus texture intentional yang pertama.

## Numerik dan stability

Persamaan differential memerlukan solver. Explicit Euler dapat meningkatkan energy untuk oscillator meskipun output terlihat benar beberapa frame. Integrator stability, accuracy dan constraint satisfaction adalah pertanyaan berbeda. Uji timestep lebih kecil dan known analytic cases; simpan residual/energy jika relevan. Jangan menyimpulkan stabil dari render satu shot pendek.

## Sampling dan image formation

Pixel serta frame adalah samples dengan footprint. Antialiasing mengaproksimasi spatial coverage, shutter sampling mengaproksimasi perubahan selama exposure. Averaging colors dalam nonlinear encoding tidak sama dengan averaging radiance. Pilih explicit linear working space untuk light integration, lalu convert ke output encoding.

## Sistem dan graph

Bentuk scene graph, timeline/track graph, compositing graph dan dependency graph tidak harus satu struktur yang sama. Scene graph menjelaskan spatial parenting; timeline menjelaskan waktu; compositor menjelaskan image dependency. Memisahkan responsibilities membantu diagnosis. Shared cue sheet mengikat audio dan visual tanpa menduplikasi waktu yang mudah drift.

## Fondasi menjadi hasil

Setiap foundation dinilai melalui konsekuensi output. Contohnya: transform order → pivot salah; timestep → cloth jitter; color transfer → dark blend; timestamp rounding → audio drift; glyph segmentation → karakter rusak. Jika foundation tidak memberi hubungan yang relevan pada video, ia bukan prioritas induk repo ini.
