# Logo morph dan reveal yang menjaga identitas

## Contract

Logo terlihat jelas pada akhir, tidak memperoleh proporsi/warna/stroke yang melanggar brief, dan animation membawa satu gagasan perubahan. Simpan logo source geometry; jangan mengandalkan screenshot rendah resolusi.

## Analisis bentuk

Inventaris components, holes, winding dan landmarks. Tentukan apakah morph topology cocok. Untuk lettermarks, counter spaces adalah fitur identitas; correspondence yang membuat counter tertutup di tengah perlu keputusan artistik, bukan kebetulan algoritma.

Jika logo berubah dari shape abstrak, pilih intermediate yang menjaga visual relation. Path morph membutuhkan same segment representation atau resampling. Mesh warp cocok permukaan internal tetapi dapat mendistorsi strokes. Mask reveal mempertahankan geometry asli dan sering lebih terkontrol saat correspondence buruk.

## Motion plan

Tetapkan anchor/pivot; tentukan trajectory, overshoot jika relevan, settle dan hold. Jangan menambahkan spring hanya karena library tersedia. Jika logo stroke tipis, motion blur serta downsample dapat membuat stroke hilang; render target-size test lebih awal.

Audio accent ditautkan pada reveal milestone, bukan otomatis frame pertama. Cue dapat berada saat logo recognizability mencapai titik yang dirancang, lalu diuji pada hasil render.

## Compositing

Gunakan alpha convention eksplisit. Blur/glow mempunyai extents di luar bounds logo sehingga crop harus lebih besar. Untuk transparent master, pilih format yang benar-benar membawa alpha dan proof composite di beberapa backgrounds. MP4 review opaque terpisah dari alpha master.

## QA

Inspect contours25/50/75%, self-intersections, brand geometry final, color transform, margin, loop closure bila loop. Bandingkan logo still final dengan approved geometry, tetapi nilai movement dalam sequence. Domain M02/M05/M07/M10/M13/M15/M18/M22.
