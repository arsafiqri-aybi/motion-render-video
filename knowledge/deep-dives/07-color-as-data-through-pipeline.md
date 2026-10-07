# M07 — Color sebagai data sepanjang pipeline

## Input interpretation

Tiga channel RGB tidak menyatakan primaries, transfer atau range sendiri. File dapat membawa metadata atau membutuhkan declaration dari source. Value0.5 dalam sRGB code berbeda dari0.5 linear light. Alpha coverage dan normals/depth bukan color channels yang boleh dikonversi seragam.

## Color arithmetic

Contoh intermediate: black dan white linear weights0.5 menghasilkan linear0.5, encoded sRGB≈0.735357. Formula transfer serta tes numeric berada di guide algoritma. Jika averaging dilakukan pada0/1 encoded lalu hasil0.5 ditag sebagai linear, tampilan berbeda; metadata tidak mengubah arithmetic yang sudah terjadi.

Color interpolation untuk palette dapat mengikuti purpose lain, misalnya encoded-space blend atau perceptual-space path. Pilihan artistik boleh berbeda dari physical light mix, tetapi dokumentasikan model dan inspect gamut. Tidak semua line segment pada suatu representation tetap berada dalam output gamut setelah transform.

## Output transform

Demo3D mempertahankan primitive/shading samples linear sebelum spatial/temporal averaging, lalu encode sRGB source images. Encoder zscale mengubah transfer/matrix/range ke BT709 delivery. Probe tags membuktikan tags tersimpan; actual transform didukung command yang dijalankan, bukan tags saja.

Text overlay2D diterapkan setelah source encoding sebagai display graphic; ia tidak menjadi light source di scene. Hal ini membantu menjelaskan batas pipeline dan menghindari klaim PBR.

## Quality checks

Float finite/range checks, neutral/brand patches, gradients, transparent edges dan final decoded crops. 8-bit/chroma subsample memberi quantization serta chroma edge losses yang perlu inspect. Calibrated display appearance membutuhkan viewing setup tambahan; numerical oracle tidak mengukur warna layar penonton.

Nyatakan scene-referred/display-referred boundaries dan jangan mengubah grade untuk menyembunyikan wrong source interpretation.

## Hubungan dan status

Konsep: M07.01, M07.02, M07.06, M07.09. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
