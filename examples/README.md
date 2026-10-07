# Executed example

[Video enam detik](rendered/demo.mp4) · [Contact sheet](rendered/contact-sheet.png) · [Config/cue sheet](demo.json)

Graphic original ini memakai kertas hangat, tinta hijau gelap, satu bentuk merah, path yang terlihat dan tiga kata: BENTUK, WAKTU, SUARA. Motion menunjukkan perjalanan, perubahan siluet dan cue audiovisual tanpa menumpuk efek. Purpose adalah demonstrasi mekanisme yang dapat diperiksa, bukan showcase seluruh 22 induk.

## Pipeline

1. State dari absolute time; path di-map melalui arc-length LUT dan smootherstep.
2. Circle menuju superellipse dengan korespondensi radial yang tetap.
3. Spatial render2×, downsample Lanczos, empat temporal samples dengan forward shutter180°.
4. Temporal colors di-average dalam linear sRGB; source RGB kemudian ditransform ke BT.709 oleh zscale.
5. PCM mono48kHz synthesized dari cue sheet sama; encoded AAC dengan H264 dalam MP4.
6. Probe timestamps/framecount/stream properties; full decode; onset detection pada decoded audio dengan declared threshold.

## Limitations

Supersampling/filtering mengaproksimasi coverage. Pillow menggambar primitive/antialiasing dalam encoded source values sebelum linear temporal accumulation; demo bukan exact linear-light spatial renderer. Tidak ada PBR, GPU, cloth, flow, HDR atau complex-script test. Contact sheet berisi sampled frames; belum menjadi evaluasi semua motion comfort. Synthetic tones bukan mastered music soundtrack.

## Reproduction

Lihat command di [README](../README.md). Output lokal dapat memiliki binary encoder differences across environments; verify scene/frame properties serta hashes dari run sendiri. Tidak mengklaim bitwise reproducibility lintas setiap library/hardware version.

## Contoh kedua:3D CPU

[Spatial demo](spatial.md) memakai geometry 3D, camera, clipping, depth buffer dan opaque flat shading. Scope/outputcontract/report terpisah dari demo 2Dberaudio di halaman ini.
