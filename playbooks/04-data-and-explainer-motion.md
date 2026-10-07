# Explainer dan data motion

## Contract

Nyatakan konsep yang harus dipahami serta fakta/nilai data yang tidak boleh berubah. Animation tidak boleh membuat audience menyimpulkan jumlah, urutan atau hubungan yang salah.

## Representation

Pilih encoding yang cocok: position, length, area, angle, color atau topology. Jika lingkaran menunjukkan nilai v lewat area, radius proportional sqrt(v), bukan v. Interpolating radius linear tidak sama dengan interpolating area/value linear. Tetapkan representation dan uncertainty sebelum motion.

Layout labels dengan constraints; prioritaskan overlaps, units dan scale. Diagram graph perlu node/edge semantics serta direction. Gesture/camera movement bukan pengganti penjelasan relationships.

## Sequence

Mulai dari baseline/context, ungkap satu transformation, highlight relationship, lalu summary state. Progressive disclosure mengurangi competing information tetapi jangan menyembunyikan denominator atau axis ketika comparison berlangsung. Stable holds untuk labels penting. Perubahan skala axis perlu jelas agar bars tidak terlihat tumbuh padahal hanya rescale.

Untuk node movement, pertahankan correspondence lewat consistent color/label/trajectory. Crossing dapat dikurangi dengan staged transitions atau routing. Banyak lines moving serentak sulit dilacak; buat cue hierarchy.

## Mathematical integrity

Value interpolation harus mempertahankan totals bila total tetap. Normalized shares w_i(v)=v_i/sum(v) berubah secara terkopel; interpolating setiap displayed percentage independently dapat sementara tidak berjumlah100%. Discrete counts tidak otomatis masuk akal ditampilkan sebagai fractional people tanpa penjelasan.

## QA

Compare source data, displayed values dan final endpoints. Check labels at delivery-size serta compressed thin lines. Uji viewer question yang tepat: apa yang berubah, apa penyebabnya, apa yang tetap? No fake statistic about understanding. Domain M01/M03/M04/M05/M10/M12/M20/M22.
