# M21 — Pipeline 3D CPU dari geometry ke frame

## Actual stages

[Renderer 3D](../../runtime/render_spatial.py) mengevaluasi world geometry/camera pada absolute time, mengubah vertices ke camera space, clip pada enam planes, project ke sample raster, depth-test opaque triangles, membentuk flat linear shading, lalu meng-average spatial/temporal samples. Encoded source dihasilkan sesudah accumulation; overlay text2D diterapkan terpisah.

## Sample count

Output640×360; spatial2×per-axis menghasilkan1280×720sample raster, empat spatial samples per output pixel. Dua temporal samples per frame berarti delapan primitive image samples per pixel secara nominal. Tidak ada adaptive sampling atau physically complete lighttransport.

96 frames 24 fps,shutter180°forward memberi4ssequence serta exposure1/48s. Sample positions ditetapkan midpoint; duplicate final endpoint tidak disertakan. Static label overlay tidak mempunyai blur3D karena purpose screen-space annotation.

## Visibility

Reciprocal-depth interpolation menjaga perspective plane depth untuk model tersebut. Depth buffer menyimpan nearestopaque surface. Coplanar ties serta shared edges mempunyai simple renderer policy; bukan GPU conformance. Texture attributes, alpha geometry, specular materials, shadows, GI serta denoising belum diimplementasikan.

## Encoded output

H264/yuv420p8bit,limitedrangeBT709 dengan actual zscale transform dari source sRGB. Silent output disengaja; audio_required=false. Full decode menghasilkan96RGBframes dengan expected size; PTS error terhadapidealgrid berada dalam declared floating tolerance.

## Quality interpretation

Frame count/cadence serta geometry unit oracles membuktikan subsets yang disebut. First-last pixel difference hanya membuktikan perubahan terlihat secara numeric, bukan smoothness/comfort. Sample contact sheet memberi visual inspection terhadap framing/occlusion; tidak mewakili full human perception. Lebih besar sample count dapat memperbaiki aliasing tetapi tidak menambah missing material/shadow physics.

## Hubungan dan status

Konsep: M21.01, M21.02, M21.03, M21.08, M21.09. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
