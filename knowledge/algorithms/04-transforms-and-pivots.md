# Transforms, pivot dan urutan operasi

## Model dan convention

Column vector convention: p_world=M_parent*M_local*p_local. Untuk rotate/scale sekitar pivot c, local transform=T(c)*R*S*T(-c). Operasi kanan terjadi dahulu. Row-vector systems memakai order berbeda; jangan menyalin formula tanpa memeriksa convention tool.

Pivot adalah invariant: memasukkan p=c harus menghasilkan c sebelum parent transform. Ini tes yang kuat untuk diagram, logo, contact squash dan product rotation. Bila parent bergerak, world pivot ikut parent; bukan berarti local invariant gagal.

## Noncommutativity

Ambil p=(1,0), scale S=(2,1), rotasi90°. R*S*p=(0,2), tetapi S*R*p=(0,1). Urutan berbeda menghasilkan geometry berbeda. Jika child diwarisi nonuniform scale lalu rotated, shear effective dapat muncul dalam world space. Decompose matrix menjadi scale/rotation tidak selalu memberi satu jawaban yang diinginkan.

## Normals dan bounds

Untuk surface normals dengan linear transform A, gunakan inverse-transpose A^-T lalu normalisasi jika A invertible. Mengubah normals memakai A langsung salah untuk nonuniform scale. Bounding box axis-aligned world perlu transform semua corners atau compute bounds geometry aktual; transform min/max saja dapat salah setelah rotation.

## Production

Simpan local/world/screen coordinates terpisah. UI control dapat mengekspos pivot sebagai normalized local point tetapi renderer menghitung unit nyata. Hindari mengubah geometry asli hanya untuk menyembunyikan transform-order bug.

## Pemeriksaan

Uji pivot, known90° rotation, parent composition dan finite matrix. Visualize axes serta bounding corners. Singular scale0 memerlukan policy: object hidden, inverse unavailable, normals invalid. [M09](../domains/09-space-depth-and-perspective.md), [M13](../domains/13-transformation-and-deformation.md).
