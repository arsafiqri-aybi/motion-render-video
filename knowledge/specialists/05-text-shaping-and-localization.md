# Text shaping, localization dan glyph animation

## Representation chain

Unicode text→segmentation→script/language/font shaping→glyph positions→layout→animated representation→rasterized output. Urutan serta boundaries perlu sesuai engine. Grapheme, codepoint dan glyph bukan unit yang sama; satu glyph dapat mewakili beberapa characters dan sebaliknya.

[R12](../../evidence/sources.md#r12) mendukung distinction grapheme/glyph; [R13](../../evidence/sources.md#r13) diperiksa untuk definition shaping. Mengetahui istilah ini tidak membuktikan seluruh script telah didukung.

## Animation choices

Per-letter reveal berdasarkan Python string slices dapat memisahkan combining marks atau emoji sequence. Per-glyph animation pada complex scripts juga bisa mengubah hubungan visual; choose grouping yang menjaga script readability. Word/line reveal dengan masks atas shaped text dapat lebih aman untuk beberapa kebutuhan.

Bidi/RTL memerlukan layout direction serta mixed numeral treatment. Localization mengubah text length dan wrapping. Jangan flip semua image sebagai substitute RTL. Font fallback perlu documented; fallback glyph metrics dapat mengubah bounds dan timing.

## Test corpus

Latin with diacritics, combining sequences, emoji ZWJ, Arabic joining, Indic clusters, mixed-direction strings, punctuation/numerals, long headlines dan missing glyph cases. Uji reference shaping engine, visual render dan animation grouping. Text language expertise diperlukan untuk acceptance pada script tertentu.

## Delivery

Captions mempunyai own time intervals dan line breaks; tidak sekadar overlay seluruh transcript. Motion text dan captions jangan overlap area penting. Encoded chroma/subsample dapat merusak colored thin glyph edges; review final sizes.

## Batas

Demo memakai Indonesian Latin text dan DejaVu Sans; complex scripts tidak diuji. Domain M03/M06/M11/M20/M22.
