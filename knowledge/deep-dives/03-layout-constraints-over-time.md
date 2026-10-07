# M03 — Layout constraints sepanjang waktu

## Layout bergerak

Final frame rapi belum menjamin sequence rapi. Bounds berubah karena translation, scale, rotation, morph, camera projection, shadows dan glow. Bedakan geometry bounds, painted bounds dan information bounds. Teks boleh tidak mempunyai painted overflow tetapi counter/label penting tetap bisa tertutup objek lain.

## Constraint example

Canvas640×360 dengan safe margin24 memberi region[24,616]×[24,336]. Rectangle lokal120×40 diputar30° mempunyai axis-aligned width=120*cos30°+40*sin30°≈123.923 dan height=120*sin30°+40*cos30°≈94.641. Memeriksa120×40 saja akan meloloskan clipping yang tampak saat rotasi.

Untuk rectangle center(x,y), require x±width/2 dan y±height/2 di safe region pada critical intervals. Glow radius12 menambah painted bound, tetapi cropped glow dan cropped glyph memiliki biaya informasi berbeda. Document acceptance masing-masing.

## Swept bounds

Evaluate endpoints saja tidak cukup jika easing overshoot atau path melengkung. Sample trajectory plus extrema yang dapat diturunkan; pilih sample density berdasarkan possible motion dan margin. Sampling dapat melewatkan transient event di antara samples. Jika exact continuous guarantee penting, gunakan conservative bounding atau analytic extrema.

## Adaptation

Normalized anchor membantu placement tetapi fonts membutuhkan min/max pixel-size dan wrapping. Fit/crop/recompose adalah policies berbeda. Portrait variant dapat menyusun vertical sequence dengan timing yang sama, tetapi informasi yang sebelumnya simultan mungkin menjadi sequential; update choreography/message checks.

## Diagnosis

Pisahkan overlap yang disengaja, occlusion yang menghilangkan informasi, dan proximity yang mengurangi readability. Debug overlay menunjukkan local bounds, world/screen transformed bounds serta safe regions. Periksa render pada entry, maximum overshoot, reading hold dan exit, kemudian final encode. Bounds arithmetic adalah engineering evidence, bukan audience comprehension.

## Hubungan dan status

Konsep: M03.01, M03.06, M03.07, M03.09. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
