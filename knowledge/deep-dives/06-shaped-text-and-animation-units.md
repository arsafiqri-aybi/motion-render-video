# M06 — Shaped text dan unit animasi

## Representation boundary

Input string mempunyai codepoints; segmentation menyediakan grapheme-like units; shaper menghasilkan glyphs/positions sesuai font/script. Animation grouping perlu menjaga hubungan hasil shaping. Memilih “huruf” tanpa menyatakan unit dapat merusak marks, ligatures atau scripts dengan joining.

HarfBuzz clusters menghubungkan input dan output shaping. Final cluster values dapat berubah saat composition/substitution; tidak boleh diasumsikan selalu one-codepoint-one-glyph. [R40](../../evidence/sources.md#r40) dibaca untuk distinction ini. Implementation-specific flags serta script behavior perlu periksa dokumentasi/engine versi aktual.

## Production choices

Whole-word/line reveal via mask atas text yang sudah shaped menjaga geometry teks asal. Per-glyph transforms memberi kontrol lokal tetapi bisa memisahkan glyph grouping yang penting. Shape-before-mask bukan solusi otomatis jika mask memotong glyph/marks secara visual; pilih timing/granularity sesuai readability.

Contoh text memakai combining acute: representation dapat memakai base+mark atau precomposed codepoint. Memotong berdasarkan byte count jelas tidak sama dengan visual letter count. Default Python slicing memakai codepoints; ia belum menjadi grapheme reveal algorithm. Emoji ZWJ juga memerlukan grouping yang sesuai.

## Metrics

Advance width mengatur progression pen glyph; ink bounds mengatur actual pixels. Italics dapat keluar advance box. Baseline, ascender/descender dan font fallback memengaruhi alignment. Character spacing uniform setelah shaping dapat merusak spacing yang dirancang engine; lakukan adjustment dengan model yang benar.

## Verification

Gunakan corpus Latin accents, mixed scripts, RTL, punctuation, emoji dan long localized strings. Render reference layout melalui engine yang dipilih, kemudian animate grouping dan review dengan language competence. Demo repo hanya menguji Indonesian Latin font yang disebut; tidak menandai seluruh typography engine support dari keberhasilan satu title.

## Hubungan dan status

Konsep: M06.01, M06.02, M06.05, M06.08. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
