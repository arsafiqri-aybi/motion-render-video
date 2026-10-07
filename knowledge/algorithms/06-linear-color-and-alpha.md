# Transfer functions dan alpha compositing

## Dua persoalan berbeda

Transfer function menghubungkan code values dengan linear-light coordinates. Alpha convention menghubungkan coverage dengan color values. Memperbaiki satu tidak otomatis memperbaiki yang lain.

## sRGB example

Inverse transfer: L=C/12.92 bila C<=0.04045; selain itu L=((C+0.055)/1.055)^2.4. Forward memakai12.92L bila L<=0.0031308; selain itu1.055L^(1/2.4)-0.055. Black/white equal linear mix mempunyai L=0.5 dan encoded C≈0.735357, bukan0.5. Angka ini berlaku pada convention tersebut; metadata BT709 tidak membuat file otomatis memakai transfer sRGB.

## Alpha

Straight RGB menyimpan color C; premultiplied menyimpan c=alpha*C. Dengan shared space, source-over: co=cs+cb*(1-as), ao=as+ab*(1-as). RGB hasil straight diperoleh co/ao bila ao>0; alpha0 perlu policy agar tidak divide-by-zero. Urutan layers tidak commute.

Filtering RGBA premultiplied membantu mencegah arbitrary RGB pixel transparan mencemari edge. Ketika melakukan nonlinear color conversion pada premultiplied RGB, sering diperlukan unpremultiply→convert→premultiply, dengan handling alpha kecil. Color transform tidak boleh dianggap linear kecuali memang matriks linear pada space yang sesuai.

## Batas demo

Pillow source colors ditetapkan sebagai sRGB code values. Temporal samples di-linearize untuk averaging, lalu re-encode. zscale melakukan sRGB→BT709 transfer/matrix/range pada delivery. Spatial raster antialias/downsample sebelumnya masih approximate; bukan exact radiance renderer.

## Pemeriksaan

Gunakan known color patches, black/white midpoint, transparent edges di banyak backgrounds, float finite checks dan output tags. Aritmetika oracle tidak mengukur calibrated screen appearance. [M07](../domains/07-color-and-color-relationships.md), [M18](../domains/18-compositing-and-image-processing.md).
