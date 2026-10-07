# Kinetic typography yang tetap terbaca

## Contract

Satu pesan utama, dua baris supporting text, satu CTA; output landscape dan portrait. Tulis apa yang harus diingat penonton dan window membaca yang dibutuhkan. Jangan memilih character stagger sebelum text, font dan layout stabil.

## Persiapan

Resolve font serta license. Shape teks secara utuh, ukur advances dan ink bounds. Tentukan unit reveal: word, grapheme, glyph atau line. Untuk Arabic/complex scripts, memotong codepoints dapat merusak glyph shaping; gunakan text engine dan representation yang sesuai. Segmentasi bukan shaping.

Layout at final aspect. Tentukan wrapping, optical alignment, leading, tracking, safe area dan background contrast. Hindari memaksa layout portrait sebagai crop landscape jika headline menjadi terpotong.

## Motion plan

Buat tiga fase: reveal→stable reading→exit. Reveal dapat bergerak, tetapi reading hold menjaga text stable. Untuk N unit, durasi local d dan stagger s, last completion=(N-1)*s+d jika semuanya berurutan. Tambahkan reading hold setelah completion terakhir, bukan menghitungnya sejak unit pertama muncul. Speed typography tidak boleh dinilai hanya dari timeline total.

Jika teks harus berpindah saat dibaca, kurangi relative motion dan exposure blur; check target size. Gunakan accent satu kata dengan alasan semantik, bukan setiap kata mempunyai effect berbeda. Masukkan musik sebagai struktur pendukung, jangan memotong klausa hanya untuk beat alignment.

## Render dan QA

Render worst-case long text, diacritics, angka dan tanda baca. Periksa font substitution, frame yang masih overlapping dan endpoint holds. Inspect encoded output karena yuv420p dapat merusak thin colored edges. Review muted comprehension dan captions bila diperlukan.

## Kriteria penguasaan

Mampu menghitung last reveal, membedakan shaping/segmentation/layout, menyiapkan portrait version dan menjelaskan mengapa motion membantu pesan. Tes comprehension tetap memerlukan viewers. Domain M01/M03/M06/M11/M12/M20/M22.
