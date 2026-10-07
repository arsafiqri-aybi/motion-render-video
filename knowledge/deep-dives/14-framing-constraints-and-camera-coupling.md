# M14 — Framing constraints dan coupled camera

## Subject framing

Untuk subject heightH pada perpendicular plane distanceZ, projected heighth=fH/Z dalam consistent image-plane units. Jika focalf didefinisikan pixels, h menjadi pixels. Extent objek3D tidak cukup dihitung dari satu depth saat depth span/rotation signifikan; project relevant geometry/bounds.

## Dolly dan zoom

Zoom mengubah focal pada posisi sama; dolly mengubah posisi dan perspective relationships. Subject plane size dapat dijaga dengan f/Z konstan. Example: H2,Z10,f50→h10; Z20,f100→h10. Background berbeda depth tidak menjaga ratios yang sama.

Tes demo memeriksa subject scale invariant tersebut. Ini geometric identity, bukan lens breathing, physical calibration atau camera comfort test. Finite cube distance/orientation memerlukan projected bounds actual.

## Orbit framing

Camera eye mengikuti orbit dan target look-at. Ketika up sejajar direction, basis tidak valid; gunakan fallback/better pose parameterization. Target yang baik secara world-space tidak menjamin subject centered secara image bounds jika subject asymmetric; framing solve dapat memakai projected center/anchors.

Path camera menyebabkan seluruh field bergerak. Stabilkan reading text atau pakai screen-space overlay sesuai purpose. Text overlay demo intentionally bukan label world-attached; tidak mengklaim surface tracking.

## Shot checks

Check margin sepanjang path, occlusion of key features, near-plane crossings, screen direction dan scale progression. Debug camera position/target curves serta projected bounds. Periksa maximum speed dan acceleration bila comfort constraints ditetapkan; threshold kontekstual perlu evidence yang sesuai.

## Production trade-off

Solve framing terlebih dahulu, lalu choose lens/path yang memberi depth/information. Jangan mengatasi cropped subject dengan random lens changes yang membuat intended perspective berubah. Focus/DOF tetap specialist branch belum dieksekusi pada CPU renderer ini.

## Hubungan dan status

Konsep: M14.01, M14.02, M14.04, M14.08. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
