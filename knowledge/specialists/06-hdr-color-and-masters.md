# HDR, wide gamut dan master color workflow

## Manifestasi

HDR/wide gamut dapat memberi highlight range serta colors yang berbeda dari SDR, tetapi tampilannya bergantung mastering/display interpretation. Menambah brightness atau bit depth tidak otomatis menghasilkan HDR yang benar.

## Contract

Nyatakan reference pipeline, primaries, transfer, luminance assumptions, signal range, precision, container/codec serta target display. Scene-referred values dan display-referred encoding mempunyai fungsi berbeda. [R16/R17](../../evidence/sources.md#r17) merupakan candidate color management routes; tidak dijalankan build.

## Pipeline

Assets mempunyai input interpretation; shaders/compositing memakai working space; output transform/tone mapping/gamut mapping menghasilkan distribution format. LUT mempunyai input domain dan expected transform order. Metadata yang benar perlu cocok actual transform; tag-only change dapat memberikan wrong interpretation.

Data passes normals/depth/motion vectors tetap data, bukan HDR color. Alpha interchange memerlukan convention yang jelas; nonlinear transform terhadap premultiplied data perlu handling khusus. Clipping highlight sebelum output transform menghilangkan detail yang tidak dapat dikembalikan metadata.

## Test plan

Known patches, neutral ramps, bright highlights, saturated colors serta transparent edges. Periksa numeric values/ranges, format precision dan actual display/viewing path dengan tools yang sesuai. Compare SDR variant sebagai independent deliverable, bukan sekadar crop intensity. Banding/noise/codec artifacts diperiksa encoded media.

## Batas

Demo secara eksplisit SDR sRGB source ke BT709 delivery8bit. Ia tidak menguji PQ/HLG, HDRmetadata, reference display, ACES/OCIO atau color calibration. Domain M07/M08/M18/M21/M22.
