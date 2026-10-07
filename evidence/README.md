# Evidence dan batas klaim

## Jenis status

- **AUTHORED:** penjelasan ditulis; bukan otomatis audit literatur.
- **DERIVED:** contoh diturunkan dari assumptions yang disebut.
- **PASS untuk pemeriksaan bernama:** kode atau media aktual diuji dalam run tertentu.
- **VISUALLY_REVIEWED_SAMPLE:** sampled frames ditinjau; bukan full perceptual study.
- **PASSAGE_INSPECTED:** bagian sumber dibaca untuk scope tertentu; bukan seluruh buku.
- **CANDIDATE:** jalur primary source yang disarankan; belum menjadi bukti klaim spesifik.

[Source registry](sources.md) memisahkan dua status sumber terakhir. [Claim ledger](claims.json) menyimpan contoh kaitan claim/metode/batas. [Render report](render-report.json), [media report](media-report.json), [numeric report](numeric-report.json) dan [structure report](structure-report.json) adalah actual outputs dari pemeriksaan build.

Repo tidak menyebut semua 198 konsep telah dieksekusi. Demo flat graphic membuktikan sebagian timing/path/morph/color/audio/render/encode pipeline. GPU shaders, path tracing, cloth/fluid solvers, complex-script shaping, HDR, human comfort dan universal accessibility tidak memperoleh status PASS dari demo tersebut.

## Pembaruan bukti

Jika code/config/output berubah, rerun checks lalu update report hashes. Catatan source passage perlu membatasi klaim yang didukungnya. Human finding perlu metode, kondisi, population dan limitations; jangan memperlakukan design preference sebagai hukum psikologi.

## Pendalaman 3D yang dieksekusi

[Render 3D](spatial-render-report.json), [numeric](spatial-numeric-report.json), [media](spatial-media-report.json) dan [sample review](spatial-visual-review.md) menambah actual subset geometry/camera/clipping/opaque visibility. [Coverage](execution-coverage.json) menghubungkan checks ke concepts dengan scope explicit. Tidak mempromosikan seluruh domain menjadiPASS.
