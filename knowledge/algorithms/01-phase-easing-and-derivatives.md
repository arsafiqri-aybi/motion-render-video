# Phase, easing dan derivatives

## Masalah yang terlihat

Objek bergerak dari A ke B tetapi start/stop membentur hold, atau gerak menjadi cepat ketika durasi diubah. Pisahkan progress, geometry dan waktu agar penyebabnya jelas.

## Model

Untuk start s, durasi d>0: u=clamp((t-s)/d,0,1). Posisi x(t)=A+(B-A)e(u). Di bagian interior, velocity=(B-A)e'(u)/d dan acceleration=(B-A)e''(u)/d². Menggandakan durasi membuat speed menjadi separuh dan acceleration seperempat, walaupun bentuk easing sama. Ini alasan durasi tidak dapat dipilih terpisah dari amplitude bila ingin mempertahankan karakter.

Quintic e(u)=6u⁵-15u⁴+10u³ mempunyai e(0)=0, e(1)=1, e'(0)=e'(1)=0 serta e''(0)=e''(1)=0. Ia dapat disambung dengan holds tanpa discontinuity velocity/acceleration. Jerk endpoint tidak nol; jangan menyebut semua derivative kontinu.

## Implementasi

Simpan timestamps dalam satu convention. Clamp phase sebelum easing dan pertahankan posisi endpoint di luar interval. Jika transisi dibatalkan saat bergerak, restart easing dengan zero velocity akan mengubah gerak; gunakan model yang menerima velocity awal atau trajectory connector. Untuk opacity, overshoot easing dapat keluar0–1; keputusan clamp harus disebut.

Cubic Bezier easing memakai x sebagai input waktu dan y sebagai output. Evaluasi y(u) langsung biasanya salah karena perlu mencari parameter r sehingga x(r)=u. Bisection robust untuk x monotonic; Newton lebih cepat tetapi membutuhkan fallback ketika derivative kecil. Path Bezier adalah problem geometry berbeda meskipun namanya sama.

## Pemeriksaan

Uji endpoints, interior midpoint, range dan finite values. Periksa velocity numerik dekat sambungan. Compare same absolute time ketika output fps berubah. Di demo, smootherstep dipakai sebagai pilihan authored; tidak diklaim paling baik untuk semua gerak. [Kode](../../runtime/motion.py) dan [tes](../../tests/test_motion.py).
