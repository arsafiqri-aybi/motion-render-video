# M13 — Deformation, correspondence dan local distortion

## Deformation field

Mapping x'=F(x,t) mengubah hubungan titik. Jacobian J=∂F/∂x menjelaskan local linear effect. Determinant magnitude memberi area/volume scale pada local model; zero menandai collapse. Sign change dapat menandai orientation inversion tetapi acceptance bergantung representation/intent.

Squash affine2D diag(sx,sy) mempunyai determinant sx*sy. Jika sy0.8 dan ingin area preserved, sx1.25. Dalam3D, mempertahankan luas penampang tidak sama dengan volume; sx*sy*sz perlu didefinisikan. Cartoon deformation tidak wajib physically conservative, tetapi jangan salah menamai invariant.

## Correspondence

Morph vertex arrays membutuhkan topology/landmark relationship. Equal pointcount tidak menjamin identity; swapped starting index dapat memutar kontur. Resample dan align features; review intermediate, bukan endpoints saja.

For mesh, skinning weights normalized mempertahankan weighted combination consistency, tetapi volume loss tetap dapat terjadi. Corrective shapes dan alternate skinning models mengatasi problem tertentu; tidak otomatis menyelesaikan all poses.

## Topology changes

Split/merge/holes tidak selalu dapat diwakili continuous fixed-connectivity mesh tanpa intermediate artifacts. Implicit fields, remeshing atau staged mask transition menawarkan choices. Intermediate blended field belum tentu signed distance; derivative-based normals dan stroke thickness perlu diperiksa.

## Failure probes

Checkerboard deformation mengungkap stretch/foldovers. Landmark overlay mengungkap correspondence. Signed area/triangle orientation checks mengungkap inversion. Normals/tangent transform checks mengungkap shading mismatch yang dapat keliru dianggap geometry distortion.

## Scope

Actual CPU3D demo memakai rigid rotations, tidak melakukan cloth/skinning deformation. Inverse-transpose test hanya directional behavior pada invertible affine mapping. Morph circle/superellipse pada demo 2D mempunyai fixed radial correspondence; hasil itu tidak menjadi proof arbitrary contour morph.

## Hubungan dan status

Konsep: M13.02, M13.04, M13.05, M13.09. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
