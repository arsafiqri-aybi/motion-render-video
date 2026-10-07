# M08 — Normals, shading dan material contract

## Normal sebagai directional data

Normal menentukan orientasi permukaan untuk model shading. Tangent t memenuhi n·t=0. Di bawah invertible linear transform A, tangent menjadi At; normal yang menjaga orthogonality adalah proportional A^-T n karena (A^-T n)·(At)=n·t. Normalisasi sesudahnya. Untuk nonuniform scale, An umumnya bukan hasil yang benar.

## Model demonstrasi

Renderer CPU memakai linear color base serta response0.22+0.78*max(0,n·l), dengan l normalized. Angka adalah authored visual controls. Constant ambient bukan hasil solved global illumination; tidak ada cast shadows/specular/transmission. Jangan menginterpretasikan response ini sebagai complete material model atau energy-calibrated lighting setup.

Base color sama dapat tampak berbeda karena normals/camera exposure. Surface identity membutuhkan model serta light context, bukan memilih RGB saja. Material parameters dari engine tertentu tidak diterjemahkan satu-ke-satu ke adjectives rough/premium tanpa review.

## Geometry context

Face winding mengatur normal cross product. Winding terbalik membuat face tampak terlalu gelap pada model yang memakai max dot. Backface culling dan two-sided shading merupakan policy lain; renderer demo opaque melakukan depth visibility tanpa culling yang diklaim universal.

## Contact

Lighting tanpa shadows tidak memberikan contact cues lengkap. Floor dan depth occlusion menyediakan spatial relations tetapi bukan physical contact validation. Product realism perlu cast/contact shadows serta material transport tests tersendiri.

## Actual verification

Tes inverse-transpose mengukur orthogonality terhadap transformed tangent dengan nonuniform scale. Scene video menunjukkan flat face differentiation. Ia tidak menguji all BRDF models, material capture atau PBR convergence. Penjelasan model matematis ini derived; reference reflection intro R18 membatasi apa yang benar-benar dibaca.

## Hubungan dan status

Konsep: M08.01, M08.02, M08.05, M08.06. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
