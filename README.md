# Motion Render Video

Knowledge base berbahasa Indonesia tentang pengetahuan yang membentuk **manifestasi motion dalam video**: bentuk, teks, ruang, gerak, waktu, kamera, editing, efek, suara, dan gambar hasil render.

Titik masuknya adalah apa yang ditampilkan dan dialami penonton. Matematika, kode, simulasi, GPU, state dan pipeline dibahas ketika menjelaskan atau menghasilkan tampilan tersebut. Library/software menjadi lapisan implementasi, bukan induk pengetahuan.

## Mulai membaca

- [Master map: 22 induk](architecture/master-map.md)
- [Navigasi berdasarkan tampilan dan masalah](architecture/manifestations.md)
- [198 konsep terstruktur](architecture/concepts.json)
- [Fondasi lintas domain](knowledge/foundations.md)
- [Penurunan dan algoritma](knowledge/algorithms/README.md)
- [22 pendalaman produksi](knowledge/deep-dives/README.md)
- [Graph hubungan 198 konsep](architecture/concept-graph.md)
- [Delapan cabang spesialis](knowledge/specialists/README.md)
- [Playbooks produksi](playbooks/README.md)
- [Diagnosis kegagalan](diagnostics/README.md)
- [Sumber, scope, dan bukti](evidence/README.md)
- [Jalur belajar dan penguasaan](learning/README.md)
- [Contoh video yang benar-benar dirender](examples/README.md)

## Cara materi disusun

Setiap induk memuat manifestasi, batas, fondasi, sembilan konsep utama, prinsip/model, implementasi, failure mode, metode pemeriksaan, contoh terhitung, kasus produksi, trade-offs, workflow, kriteria penguasaan dan cabang spesialis. Indeks konsep dapat dipakai software tanpa perlu menebak judul folder.

Hubungan antardomain bersifat many-to-many. Typography yang bergerak, misalnya, menghubungkan text shaping, layout, temporal choreography, compositing dan readability. Tidak setiap efek perlu dibuat menjadi induk baru.

## Menjalankan contoh

Python 3.10+; FFmpeg/ffprobe dengan libx264 dan zscale; Fontconfig dan DejaVu Sans. Dependencies Python berada di [requirements.txt](requirements.txt).

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v
python3 runtime/render_demo.py --out .local-output
python3 tools/verify_media.py .local-output
python3 tools/validate_knowledge.py
```

Render contoh menghasilkan 640×360, 30 fps, 180 frame, enam detik dan audio mono 48 kHz. Kode melakukan sampling temporal, transform color yang dinyatakan dan encoding nyata.

[Contoh 3D CPU](examples/spatial.md) menambah 96 frame/24 fps/4s dengan geometry, camera, clipping, depth buffer dan sampling actual. Jalankan `python3 runtime/render_spatial.py --out .local-output/spatial` lalu `python3 tools/verify_spatial.py .local-output/spatial`. Suite numeric sekarang 24 tests; scope 2D/3D disimpan terpisah. [Laporan run yang disertakan](evidence/render-report.json) dan [pemeriksaan media](evidence/media-report.json) mengacu pada binary demo yang disertakan.

## Kedalaman dan status

Seluruh 22 induk memiliki materi yang tertulis; ini bukan folder kosong atau daftar link saja. Keberadaan cabang spesialis tidak berarti seluruh literaturnya sudah dijabarkan atau diaudit. Klaim universal “seluruh ilmu motion sudah selesai 100%” tidak dipakai.

**AUTHORED** berarti penjelasan tersedia. **PASS untuk masing-masing demo** hanya berarti pemeriksaan yang disebut dalam laporan sudah dijalankan. Sumber yang baru menjadi jalur riset diberi **CANDIDATE**; passage yang dibaca diberi scope tersendiri. [Batas cakupan](architecture/scope.md) menjaga perbedaan ini.

Struktur ini adalah isi baru repository. Materi lama tidak disalin sebagai backup, archive atau release mirror.
