# M18 — Depth, alpha dan auxiliary pass conventions

## Berbeda jenis data

Beauty RGB dapat encoded/linear; alpha coverage tidak sama dengan density; depth menyimpan jarak menurut convention; normals arah; motion vectors displacement antara times. Applying color grade ke semua channels merusak data yang dipakai compositor.

## Perspective depth

Barycentric weights pada projected triangle tidak menghasilkan linear cameraZ. Untuk camera-depth z_i dan screen-space weights lambda_i, reciprocal depth interpolates: 1/z=sum(lambda_i/z_i) dalam pinhole model. Renderer memakai hubungan ini untuk depth comparison.

Tes independent menggunakan plane z-x=3 dan ray melalui pixel center. Ray directionx/z=0.5/32 memberi intersection depth3/(1-0.5/32)≈3.047619. Ini oracle geometry berbeda dari formula barycentric yang sedang diuji.

## Opaque versus transparent

Zbuffer memilih nearest opaque surface per sample. Transparent compositing membutuhkan remaining layers/order atau methods khusus; mempertahankan nearest RGB saja menghilangkan informasi belakang. CPU renderer tidak mengklaim alpha geometry support. Source-over formula di runtime 2D membutuhkan correct premultiplied inputs serta shared space.

## Pass interchange

Nyatakan depth units/direction, invalid/background sentinel, camera space, vector direction/timebase, alpha convention dan encoding. DepthInf background valid sebagai sentinel dalam internal buffer tetapi format output mungkin memerlukan mask/encoding lain. Jangan scan depthallfinite lalu menganggap sentinel valid sebagai corruption.

## Verification

Known near/far triangles, draw order swap, flat-plane oracle dan normal/tangent checks. Tes order independence berlaku untuk unequal-depth opaque surfaces; coplanar ties memakai renderer policyfirst writer. Color/alpha passes memiliki checks tersendiri. Shadow/DOF operations berbasis depth perlu additional implementation/testing sebelum memperolehPASS.

## Hubungan dan status

Konsep: M18.01, M18.02, M18.07, M18.09. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
