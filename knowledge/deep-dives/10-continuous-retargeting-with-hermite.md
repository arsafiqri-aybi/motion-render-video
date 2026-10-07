# M10 — Retargeting kontinu dengan Hermite connector

## Persoalan

Target baru datang saat objek bergerak. Menjalankan easing baru dari current position dengan zero velocity dapat membuat velocity jump. Pertahankan state x0,v0 dan pilih trajectory yang memenuhi endpoint constraints.

## Cubic Hermite

Untuk durasi d dan normalized u∈[0,1], gunakan x(u)=h00*x0+h10*d*v0+h01*x1+h11*d*v1. Basis h00=2u³-3u²+1; h10=u³-2u²+u; h01=-2u³+3u²; h11=u³-u². Faktor d diperlukan karena v mempunyai units distance/second sedangkan derivative basis terhadap u.

Model memenuhi positions serta endpoint velocities. Ia tidak otomatis menjaga acceleration continuity. Untuk C2 connection, gunakan quintic dengan acceleration constraints atau model response continuous-state yang sesuai.

## Example

x0=0,x1=1,d=1,v0=2,v1=0 menghasilkan x=-2u³+3u²+2(u³-2u²+u)=2u-u². Midpoint0.75 dan velocity endpoint0; linear interpolation midpoint0.5. Velocity awal sama, tetapi trajectory orientation/overshoot pada parameter lain perlu pemeriksaan.

## Constraints

Short duration dan large initial velocity dapat memerlukan overshoot atau very high acceleration. Endpoint constraints tidak menjamin bounds/speed limits. Cari extrema dari derivative quadratic dan assess contract; jika trajectory melanggar, extend duration, alter endpoint velocity atau gunakan constrained path solver.

Untuk vectors, gunakan per-component basis namun screen-space bounds masih perlu inspect. Untuk rotations, scalar Hermite angles memerlukan unwrap/path intent; quaternion interpolation bukan menyalin vector formula tanpa normalization/appropriate model.

## Verification

Positions/velocities endpoint dan max range dapat diturunkan; render interruption interval untuk appearance. Guide ini authored derivation, belum dijalankan sebagai runtime connector dalam build. Spring actual tests tidak memberi otomatis PASS Hermite branch.

## Hubungan dan status

Konsep: M10.01, M10.02, M10.08. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
