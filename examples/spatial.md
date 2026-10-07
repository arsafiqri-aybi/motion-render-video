# Executed 3D CPU example

[Video4detik](rendered/spatial.mp4) · [Decoded contact sheet](rendered/spatial-decoded-contact-sheet.png) · [Source contact sheet](rendered/spatial-contact-sheet.png) · [Config](spatial.json)

Tiga cubes berada dalam scene3D dengan finite floor/grid geometry. Camera orbit dan object rotation mengubah projected silhouettes serta occlusion. Camera/transforms, clipping dan depth buffer dievaluasi dari geometry 3D; ini bukan sequence of pasted cube sprites.

## Run

```bash
python3 runtime/render_spatial.py --out .local-output/spatial
python3 tools/verify_spatial.py .local-output/spatial
python3 -m unittest discover -s tests -v
```

Output640×360,24 fps,96 frames,4s,intentionallysilent. Layout overlay dirancang untuk contract640×360; outputaspect lain perlu recomposition/layoutupdate. Primitive shadinglinear memakai constant ambient plus diffuse response, tanpa cast shadows/PBR/GI. Sampling2×per-axis dan2temporal samples/forward shutter180°. Actual zscale transform menghasilkanBT709limited8bitH264/yuv420p.

## Evidence

[Render report](../evidence/spatial-render-report.json), [numeric report](../evidence/spatial-numeric-report.json), [media report](../evidence/spatial-media-report.json) dan [coverage](../evidence/execution-coverage.json). Source/decode images reviewed pada frames 0,19,38,57,76,95: label dalam frame; subject utama terlihat; bentuk wajah serta floor perspective berubah; cube belakang terocclude selamacamera bergerak. ReviewAI sampel, bukan human study atau full playback comfort test.

## Batas

Rasterizer edukasional: opaque flat triangles; no textureattributes/alpha/PBR/shadows/Blender/GPU. Equaldepthfirst writer/simpleedgeepsilon bukan GPU raster-rule conformance. Silent output adalah contract, bukan missing audio failure. Cube/floor belum menjadi physical collision simulation. Hash/PTS/decode checks tidak membuktikan material realism.
