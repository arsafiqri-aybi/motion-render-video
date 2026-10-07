# M20 — Viewing contract dan kelas bukti

## Conditions

Ukuran encoded frame, physical display size, viewport/letterbox serta viewing distance memberi pengalaman berbeda. Motionpx/s berguna bagi renderer tetapi bukan langsung angular speed mata. Video di mobile dapat ditonton muted, cropped atau dengan captions; contract harus menyatakan intended contexts.

## Case

Movement120px/s pada canvas1200px berarti0.1 frame-width/s. Downsample600px memberi60px/s dengan normalized speed sama. Display600px pada layar fisik besar tidak otomatis sama dengan600px pada ponsel. Jangan menetapkan comfort threshold hanya dari pixels/s.

## Readability

Stable text hold dimulai setelah glyph/line terakhir readable, bukan first onset. Background contrast berubah sepanjang footage. Check worst-case encoded frames dan reading interval. Cropping caption/CTA menyebabkan information loss walau scene geometry serta media timestamps valid.

## Evidence classes

Engineering check membuktikan property terdefinisi, misalnya decoded framecount. AI sample review mencatat terlihat/tidak pada samples yang dipilih. Expert review memberi evaluasi professional dengan limits. Human task study memberi observations population/conditions tertentu. Flash analysis atau accessibility conformance membutuhkan method/scope tersendiri.

Menggabungkan kelas ini tanpa label membuat confidence berlebihan. “No decode errors” tidak berarti “comfortable”. “Looks good” tidak berarti “all users understand”. Derived equation tidak otomatis empirical human finding.

## Practical acceptance

Tulis viewer question, intended task, conditions dan criteria sebelum melihat responses. Pisahkan preference dari correct comprehension. Jika tidak ada study, simpan design hypothesis sebagai hypothesis. Buat calmer motion variant jika brief/audience membutuhkannya dan verifyvariant sendiri.

Build ini mempunyai numeric/media evidence dan sampled image review. Tidak ada human study, flash certification atau accessibility audit seluruhvideo.

## Hubungan dan status

Konsep: M20.01, M20.04, M20.07, M20.09. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
