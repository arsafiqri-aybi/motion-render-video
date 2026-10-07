# M05 — Triangle coverage dan representasi bentuk

## Dari mesh ke pixel

Mesh menyimpan connectivity dan posisi. Projection mengubah silhouette, lalu rasterization menentukan samples yang berada dalam primitives. Triangle adalah unit sederhana untuk opaque surfaces; shape final masih bergantung tessellation, clipping dan sample positions.

Barycentric coordinates lambda0+lambda1+lambda2=1 mengungkap lokasi point terhadap triangle. Point di dalam memiliki weights nonnegative dalam convention yang digunakan. Zero-area triangle tidak mempunyai stable area denominator dan harus ditangani tanpa writes invalid.

## Shared boundaries

Dua triangles pembentuk rectangle berbagi diagonal. Coverage rule harus menjaga tidak ada crack. Renderer CPU menyertakan boundary dengan epsilon; equal-depth tie memakai first writer. Ini subset edukasional, bukan implementasi persis GPU top-left raster rules. Opaque adjacent triangles berwarna sama dapat survive tie tersebut; transparent layers/coplanar faces membutuhkan aturan lebih lengkap.

## Spatial samples

Satu sample pixel-center dapat melewatkan thin shape. Supersampling2×per-axis memakai empat sample centers per output pixel, lalu average linear color. Ini mengaproksimasi coverage box footprint dan tidak menciptakan detail geometry yang tidak ada. Wide reconstruction filters mempunyai trade-off softness/ringing berbeda.

## Topology versus appearance

Surface connected secara mesh dapat terlihat terputus akibat occlusion atau subpixel thickness. Sebaliknya dua components berbeda dapat terlihat menyatu di projection. Geometry validation dan visual validation menguji dua hal berbeda.

## Actual checks

[Renderer](../../runtime/raster3d.py) diuji untuk zero-area triangle dan rectangle dua-triangle tanpa holes pada oracle region. [Tes](../../tests/test_raster3d.py) membandingkan pixel coverage actual; test tidak mengklaim watertight semua arbitrary meshes atau perspective-texture support. Sumber raster stage R39 memberikan konteks pipeline, bukan certification renderer kita.

## Hubungan dan status

Konsep: M05.04, M05.06, M05.07, M05.08. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
