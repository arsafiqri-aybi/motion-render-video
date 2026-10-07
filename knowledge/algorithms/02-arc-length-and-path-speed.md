# Arc length dan speed sepanjang path

## Masalah

Marker melambat di satu bagian curve meskipun progress linear. Panjang derivative geometry tidak seragam.

## Penurunan

P(u) adalah cubic Bezier. ds/du=norm(P'(u)); s(u)=integral0..u norm(P'(r))dr. Constant travel speed memakai s(t)=v*t lalu inverse u=s_inverse(s). Secara umum inverse memerlukan approximation.

LUT yang dipakai demo: sample uniform u, hitung chord lengths, cumulative sum, normalize menjadi0–1. Untuk travel fraction f, cari interval s_i<=f<=s_(i+1), interpolasi u di interval itu, lalu evaluasi cubic asli. Evaluasi cubic asli menghindari output sepenuhnya menjadi polyline, tetapi length table tetap approximation.

Kurva kontrol(0,0),(0,1),(1,1),(1,0) memiliki P'=(6u(1-u),3(1-2u)). Norm derivative menyederhana menjadi3(2u²-2u+1), sehingga length tepat2. Oracle ini dipakai untuk memeriksa LUT, bukan membandingkan implementasi dengan salinan kode yang sama.

## Degenerate dan cusp

Jika seluruh control points sama, total length0 dan normalized LUT tidak valid. Reject atau pakai stationary path dengan policy eksplisit. Di cusp norm derivative dapat nol; inverse speed menjadi sensitif. Adaptive subdivision berdasarkan curvature/flatness dapat lebih efisien daripada ribuan samples uniform. Error tolerance sebaiknya terkait pixel displacement pada resolusi target.

## Choreography

Constant path speed bukan selalu intent. Easing travel fraction mengatur start/stop; geometry path menjaga jalurnya. Orientasi dapat memakai tangent tetapi tangent near-zero memerlukan fallback. Untuk closed paths, pastikan position dan tangent seam sesuai.

## Verifikasi

Ukur accumulated length dan equal-distance segments, naikkan samples lalu bandingkan. Inspect slow motion dan full-speed playback. LUT test demo menguji satu kurva dengan exact reference, tidak seluruh bentuk path. [M05](../domains/05-forms-geometry-and-visual-objects.md), [M10](../domains/10-motion-behavior-and-movement-models.md).
