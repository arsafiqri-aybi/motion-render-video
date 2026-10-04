# Motion Render Video

Sistem pengetahuan dan alur kerja untuk merancang, membuat, merender, memeriksa dan memperbaiki motion/video. Tujuan lengkapnya tetap mencakup 27 lobe, 174 module dan 1.740 neuron beserta graph, bukti, diagnosis, adapter, runtime dan pengembangan yang terkendali.

Checkpoint Work menyediakan proyek yang konsisten dan runtime eksperimental yang benar-benar dapat menjalankan render 2D, inspeksi video, analisis sinyal audio, inventaris aset, konteks platform/data spasial yang diberikan, rencana perhatian dan kalkulasi gerak bersyarat dan retrieval berbukti. Kini tersedia adapter memori deklaratif dan render 3D primitive CPU Cycles dengan pemeriksaan hasil nyata; batas subsetnya dijelaskan dalam kontrak runtime. Bukti3D mengacu pada eksekusi historis yang tercatat; executable perlu dipulihkan dan diperiksa sebelum render3D baru. **Sistem pengetahuan lengkap belum selesai:** 67 module mempunyai review lokal; 107 masih belum dipopulasi. Status ini dibaca dari berkas, bukan percakapan.

Prioritas aktif: **FAST_RELEASE_COMPLETE** melalui coverage seluruh174module, functional completeness, integration, critical verification dan usable release, lalu **DEEPENING_IN_PROGRESS**. Arsitektur/scope tetap; pendalaman non-kritis tercatat di `00_CONTROL/DEEPENING_BACKLOG.json`. Milestone fast release belum tercapai.

Baca `PROJECT_REPORT_ID.md` untuk hasil dan batasnya. Untuk melanjutkan: `00_CONTROL/CURRENT_STATE.md` → `03_MANIFEST.yaml` → `EXECUTION_CONTRACT.json` → `WORK_HANDOFF.yaml` → packet dan scope yang dituju. Riwayat versi lama tetap merupakan riwayat, bukan status terbaru.

## Pemakaian lokal

Butuh Python, NumPy, Pillow, PyYAML dan fontTools untuk inspeksi font dan FFmpeg/FFprobe. Lihat `05_TOOLS/README_TOOLS.md` untuk perintah dan versi yang benar-benar diuji.

```bash
python 05_TOOLS/media_runtime.py doctor
python 05_TOOLS/project_runtime.py . status
python 05_TOOLS/project_runtime.py . query "brief atau gejala" --limit 6
python 05_TOOLS/media_runtime.py render 06_EVALUATION/BENCHMARKS/demo_motion.json hasil.mp4
```

Bila index usang, bangun dari bytes saat ini dengan `python 05_TOOLS/project_runtime.py . build`. Perintah retrieval tidak mengubah status modul atau graph. File sumber dilindungi; gunakan nama output baru untuk iterasi.

## Hasil dan pemeriksaan

- `06_EVALUATION/BENCHMARKS/demo_motion.mp4`: render nyata 6 detik, 960×540, 30 fps, tanpa audio.
- `06_EVALUATION/BENCHMARKS/attention_staged_demo.mp4`: variasi timing nyata dengan rencana perhatian dan laporan teknis; efek penonton belum diuji.
- `06_EVALUATION/`: hasil uji integritas, media, retrieval, numerik/pengukuran, audio, review lokal dan pemakaian skill.
- `01_RESEARCH/`: sumber, klaim, evidence, contradiction dan scope per modul.
- `02_KNOWLEDGE/`: canonical, operational, QA dan neuron cards yang sudah tersedia.
- `03_GRAPH/`: graph aktif dan representasinya; usulan provisional berada terpisah dalam modul.
- `07_RUNTIME_SKILL/`: index yang dapat dibangun ulang dan panduan runtime proyek. Skill yang terpasang dikelola sebagai skill pribadi tersendiri.

PASS berlaku hanya bagi properti yang diperiksa. Decode sukses, metadata benar, jumlah ID lengkap atau output yang menarik tidak menggantikan validasi pengetahuan, kualitas temporal, respons manusia atau penerimaan seluruh proyek.