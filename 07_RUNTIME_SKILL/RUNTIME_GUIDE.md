# Runtime Motion Render Video

Runtime menghubungkan brief/gejala dengan pengetahuan yang tersedia, prasyarat, evidence dan verifier. Index `retrieval.sqlite3` merupakan cache yang dapat dibangun ulang dengan `05_TOOLS/project_runtime.py`; ia bukan otoritas ilmiah atau model terlatih.

Skill pribadi **Motion Render Video** menyediakan alur brief → kemampuan alat → retrieval → produksi/diagnosis → acceptance → penyimpanan/handoff. Snapshot sumber di skill memiliki manifest dan batas cakupan. Untuk proyek hidup, baca versi terbaru; jangan menimpa proyek dengan snapshot skill yang lebih tua.

Penggunaan:

- “Gunakan Motion Render Video untuk membuat bumper 2 detik …”
- “Periksa video ini; geraknya terasa tersendat dan aku ingin diagnosis berbukti.”
- “Analisis referensi audio ini dan tandai kandidat event untuk edit.”
- “Periksa inventaris aset ini, font yang hilang dan referensi glTF sebelum produksi.”
- “Periksa asumsi viewport, HDR, sound-off dan autoplay dari konteks platform ini.”
- “Lanjutkan Motion Render Video dari CURRENT_STATE dan next packet.”

Kemampuan aktual saat checkpoint: render 2D nyata, inspeksi stream/frame PTS/reference, pemeriksaan teknis video/audio decode, pengukuran sinyal audio, inventaris aset/dependency yang terukur, profil konteks platform yang diberikan dan retrieval berbukti. Inventaris glTF adalah inspeksi metadata, bukan eksekusi 3D. Jalur 3D/generative/ASR/music inference/true peak/LUFS membutuhkan alat serta acceptance tambahan yang tersedia dan terverifikasi. Runtime harus mempertahankan tujuan pengguna dan status yang belum selesai.

Skill tidak mengubah status seluruh proyek menjadi COMPLETE. Definisi penerimaan tetap berasal dari EXECUTION_CONTRACT, quality gate, registry dan ledger. Tidak ada promosi otomatis karena jumlah file, judul, source atau hasil render bertambah.

Untuk konteks lingkungan, baca `ENVIRONMENT_CONTRACT.md` dan canonical L02.05. `environment_runtime.py` membaca manifest dan menjaga provenance/UNKNOWN. Ia tidak mengeksekusi browser atau mendeteksi penonton; PROFILED bukan sertifikasi target delivery.

Data spasial yang diberikan memakai SPATIAL_CONTRACT.md dan canonical L02.06; kalkulasi subset bukan capture/import native/calibration. Rencana perhatian memakai ATTENTION_CONTRACT.md dan L03.01;53 plan cases tidak membuktikan saliency/gaze. L03.02 menambah motion_perception routing dan motion_diagnostics.py untuk interval derivative, periodic correspondence dan collision ideal bersyarat.30 analytic/media cases memverifikasi properti yang dinyatakan, bukan persepsi manusia atau massa fisik. Teori priority-map dan mass inference tetap OPEN. Baca manifest snapshot skill dan SKILL_INSTALLATION.json untuk versi yang benar-benar terpasang; Main kini67 module; snapshot skill yang benar-benar terpasang43 module telah diverifikasi pada revisionac96cafd3d8a86f93ca06d225d6d7aebbb638ca7. Status instalasi dicatat terpisah.

Executionpriority: functional breadth-first FAST_RELEASE_COMPLETE→DEEPENING_IN_PROGRESS, sesuaiEXECUTION_CONTRACT/FAST_RELEASE_FLOOR. Architecture-onlyretrieval bukan canonicalcoverage. Primarysourcefit tetap diperlukan untuk keputusanworking; optionalexhaustivedepth masukstructuredbacklog. BatchlocalQA danbroaderaffectedregression/persistence diamortisasi tanpa mengklaimcriticalgate yang belumdijalankan.


Adapter memori: `05_TOOLS/memory_runtime.py`, kontrak `MEMORY_CONTRACT.md`, actual92 cases plus3 Main CLI cases. Eligibility memakai scope/version/expiry yang dideklarasikan dan model byte pins; tidak ada learned-memory, autentikasi atau persistence/deletion operation.

Adapter 3D: `05_TOOLS/blender_runtime.py` dengan sibling fixed driver dan explicit Blender4.5.14LTS. Baca `BLENDER_CONTRACT.md`; contoh `05_TOOL_ADAPTERS/BLENDER_EXAMPLES`. Actual52 Main cases memeriksa primitive scene, keyframe midpoint, lighting control, decode/timestamps dan rejection. Arbitrary imports/GPU/HDR/generative/human/full-release requirements tetap terbuka.