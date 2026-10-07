# M09 — Camera space, frustum dan clipping

## Convention

World memakai3D coordinates; camera evaluator menghasilkan right, up, forward basis. Demo menganggap camera depthZ positif dan imageY turun. Camera-positive-Z tidak boleh disamakan dengan seluruh convention graphics API lain; dokumentasikan tanda dan multiplication order.

Pinhole projection x_screen=cx+fX/Z, y_screen=cy-fY/Z. NonpositiveZ harus ditangani sebelum divide. Near plane mencegah projection singular/huge, tetapi reject seluruh triangle hanya karena satu vertex terlalu dekat akan membuat visible part mendadak hilang.

## Halfspace clipping

Untuk plane n·p+d>=0, vertex inside jika expression nonnegative. Edge a→b yang menyeberang mempunyai intersection a+u(b-a), u=da/(da-db). Ini diperoleh dengan menyelesaikan da+u(db-da)=0. Simpan portion inside dan lanjut pada semua frustum planes.

Positive-Z symmetric frustum mempunyai right constraintX<=Z*w/(2f), left sebaliknya; vertical memakaih/(2f); nearZ>=near, farZ<=far. Clip polygon dapat mempunyai lebih dari tiga vertices lalu ditriangulate sebagai fan. Ini cocok polygon convex hasil clipping triangle.

## Failure modes

Divide dahulu sebelum clipping dapat menghasilkan infinities. Clip interpolating only positions tidak cukup untuk textured/smooth-shaded mesh: attributes harus ikut sesuai representation. View basis singular ketika up hampir sejajar forward perlu fallback; eye=target tetap invalid.

## Actual checks

Tes target camera centered, up fallback, near-crossing polygon, all-behind/all-far rejection dan post-clipping projected bounds. Perhitungan proyeksi offset50px padaZ2 menjadi25px padaZ4 diuji numeric. Ini geometric proof dalam declared model, bukan camera calibration fisik. [CPU code](../../runtime/raster3d.py).

## Hubungan dan status

Konsep: M09.01, M09.03, M09.07, M09.09. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
