# Compositing motion di atas footage

## Contract

Grafis mengikuti konteks footage, tetap terbaca dan tidak merusak spatial continuity. Tentukan apakah overlay screen-space, attached-to-surface, depth-aware atau image-processing effect.

## Ingest

Probe footage fps/timebase, dimensions, rotation tags, color characteristics dan audio. Variable frame rate tidak boleh diperlakukan seolah every index equal time tanpa mapping. Resolve plate interpretation sebelum grading. Jangan memperbaiki wrong color tags lewat artistic grade tanpa memahami conversion.

## Placement/tracking

Screen-space overlay mengikuti layout, sedangkan attached graphic perlu track transform sesuai surface/camera. Planar tracking dapat cocok bidang datar; parallax/3D geometry dapat membutuhkancamera solve. Lens distortion perlu considered; undistort→composite→redistort adalah satu workflow tetapi precision serta edge handling harus dinilai.

## Integration

Match occlusion, blur, light/shadow dan grain sesuai function. Grafik informasional tidak harus menjadi photoreal jika clarity lebih penting; keputusan ini dibuat explicit. Depth matte dan rotoscope membantu foreground menutup attached graphic, namun matte chatter perlu dicek sepanjang waktu.

Alpha input convention dicatat. Color corrections/filters terjadi dalam space yang tepat. Transparent edges proof-tested di background asli plus diagnostic black/white. Grain ditambahkan dengan scale sesuai output dan tidak dianggap render noise yang perlu di-denoise.

## Text and audio

Footage background berubah; text contrast diperiksa sepanjang hold. Scrim/backplate dapat memberi stability. Audio original, voice dan effects dipisahkan role serta levels; edit cues mengikuti source/output time mapping.

## QA

Review track slip, matte edges, color shifts, resampling softness, fonts dan encoded text. Periksa full decode/duration lalu semantic continuity. Domain M06/M07/M09/M15/M18/M19/M20/M22.
