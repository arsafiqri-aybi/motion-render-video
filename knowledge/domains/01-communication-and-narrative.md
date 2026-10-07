# M01 — Communication and Narrative

## Manifestasi yang ditampilkan

Urutan visual dan suara membuat penonton mengetahui apa yang berubah, mengapa perubahan penting, dan apa hubungan antarbagian. Manifestasinya adalah cerita, penjelasan, demonstrasi, atau argumen yang dapat diikuti.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Fokus pada komunikasi audiovisual. Video dapat abstrak/nonverbal; narasi tetap bisa berupa progression visual. Konversi/emosi tidak diasumsikan hanya dari struktur cerita.

## Fondasi yang membentuk tampilan

Pengetahuan fondasi: semantic relationships, information architecture, temporal sequencing, causal representation dan audience/task context. Coding perlu menyimpan maksud scene, bukan hanya koordinat objek. Pisahkan fakta, ilustrasi dan editorial interpretation.

## M01.01 — Purpose dan audience

Purpose menyatakan apa yang ingin diketahui/dirasakan/dilakukan penonton dalam konteks tertentu. Audience menentukan prior knowledge dan vocabulary, bukan stereotipe taste.

**Model / mekanisme.** Brief: audience, context, claim, desired understanding, constraints.

**Implementasi.** Representasikan tujuan dan key message sebagai scene metadata yang bisa ditinjau.

**Kegagalan tampilan.** Efek indah tetapi penonton tidak tahu topik; jargon tanpa konteks.

**Pemeriksaan.** Ringkas pesan tanpa melihat script; bandingkan dengan tujuan yang dideklarasikan.

## M01.02 — Message hierarchy

Satu video dapat membawa beberapa informasi dengan priority berbeda. Memilah primary/supporting facts membantu menentukan durasi dan focal point.

**Model / mekanisme.** Message graph memuat claim, evidence, example, implication dan dependencies.

**Implementasi.** Link beats ke message IDs; track fakta mana sudah ditampilkan.

**Kegagalan tampilan.** Informasi baru ditumpuk saat penonton masih membaca poin lama.

**Pemeriksaan.** Coverage map message→shot; periksa omissions dan repeated content tanpa fungsi.

## M01.03 — Narrative progression

Setup, development dan resolution adalah pola kerja, bukan formula wajib semua video. Explain, compare, transform atau reveal dapat menjadi organizing logic.

**Model / mekanisme.** Susun perubahan state/information yang bisa diamati antarbeats.

**Implementasi.** Scene sequence mempunyai before/after semantic states.

**Kegagalan tampilan.** Transisi scene baru tanpa alasan; climax visual tidak terkait pesan.

**Pemeriksaan.** Baca sequence sebagai storyboard dan evaluasi hubungan setiap perubahan.

## M01.04 — Causality dan explanation

Diagram bergerak dapat menunjukkan relation; spatial proximity/temporal succession tidak membuktikan causality ilmiah.

**Model / mekanisme.** Bedakan causal claim, association dan illustrative metaphor.

**Implementasi.** Annotate arrows/events sesuai jenis hubungan; source-map factual claims.

**Kegagalan tampilan.** Animasi menyiratkan sebab-akibat yang tidak didukung data.

**Pemeriksaan.** Audit meaning arrows, direction, timing dan claim source.

## M01.05 — Story beats dan pacing

Beat adalah unit perubahan informasi/aksi. Durasi bergantung content/readability dan distribution platform.

**Model / mekanisme.** Budget entry, action, hold, exit tiapbeat; overlaps sengaja.

**Implementasi.** Timeline beat objects punya start/end, focal content dan dependencies.

**Kegagalan tampilan.** Semua beat sama panjang; informasi penting hanya flash singkat.

**Pemeriksaan.** Playback real-time dan task comprehension, bukan hanya frame count.

## M01.06 — Voiceover dan script

Spoken language memiliki tempo, breaths, emphasis dan silence. Visual tidak perlu menggambarkan setiap kata literal.

**Model / mekanisme.** Script alignment map phrase→visual cue; editorial flexibility eksplisit.

**Implementasi.** Simpan text, cue time, speaker/track dan confidence alignment.

**Kegagalan tampilan.** Visual tertinggal message; subtitle menutup diagram.

**Pemeriksaan.** Cue checks, pronunciation/content review dan readability.

## M01.07 — Evidence dan examples

Contoh membuat abstraksi konkret; examples harus sesuai claim dan tidak menyamar sebagai data real jika illustrative.

**Model / mekanisme.** Classify measured, simulated, synthetic, fictional, explanatory.

**Implementasi.** Tampilkan labeling yang membantu interpretasi bila relevan.

**Kegagalan tampilan.** Dummy result tampak actual measurement; cherry-picked success.

**Pemeriksaan.** Provenance review dan counterexample yang meaningful.

## M01.08 — Semantic continuity

Orientation penonton mencakup subject, scale, time dan relationship. Cut dapat melompat, tetapi kebutuhan konteks harus dipenuhi.

**Model / mekanisme.** Track what persists/changes between scenes.

**Implementasi.** Carry identifiers/colors/labels untuk concepts yang sama.

**Kegagalan tampilan.** Same color denotes different category unexpectedly.

**Pemeriksaan.** Before/after comprehension dan state consistency checks.

## M01.09 — Narrative evaluation

Story quality diukur terhadap intended communication. Editorial review berbeda dari actual audience results.

**Model / mekanisme.** Define comprehension questions atau task sebelum testing.

**Implementasi.** Capture reviewer notes by beat/time; user study status terpisah.

**Kegagalan tampilan.** AI review disebut human evidence; invented comprehension rate.

**Pemeriksaan.** Actual protocol/data jika tersedia; otherwise label editorial hypothesis.

## Penurunan mekanisme dan contoh terhitung

Contoh explainer 12 detik tentang progress: 0–2s establish system, 2–5s show input, 5–8s show transformation, 8–10s show result, 10–12s hold key conclusion. Jika title masuk 0.4s, durasi available membaca bukan otomatis 2s; subtract period ketika text belum lengkap. Budget ini authored example, tidak universal reading threshold. Model narrative graph lebih bermakna daripada 12 detik efek tanpa message mapping.

## Kasus produksi

Kasus diagram tiga tahap: setiap stage mempunyai satu noun/verb utama. Gerakkan token dari INPUT menuju PROCESS lalu OUTPUT; voice cue menandai perpindahan. Data explanatory dilabeli bila dapat dikira actual measurement. Setelah draft, hide animations dan inspect static keyframes: apakah relationship tetap dapat dijelaskan? Lalu playback untuk memastikan timing memperjelas perubahan, bukan menghilangkan informasi.

## Memilih teknik dan trade-offs

Pilih chronological structure untuk process, juxtaposition untuk comparison, transformation untuk identity/state change. Hindari memilih pola hanya karena familiar. More cuts dapat mempercepat perceived pace tetapi mengurangi time untuk relation; more words meningkatkan detail tetapi dapat menutupi diagram. Trade-off diputuskan melalui tujuan.

## Alur kerja operasional

Tulis brief dan message graph; buat beat sheet; map beats ke visual/audio; allocate timing; preview sequence; inspect factual meaning; lakukan comprehension review; revisi content sebelum polishing effects.

## Verifikasi dan kriteria penguasaan

Dapat menjelaskan fungsi setiap shot, mempertahankan actual facts, dan membuat message-to-shot coverage. Numerical duration validation tidak membuktikan comprehension; actual viewers/task diperlukan untuk claim audience outcomes.

## Cabang spesialis dalam cakupan

Visual rhetoric; documentary logic; argumentation; nonverbal storytelling; scientific visualization narratives; educational multimedia; nonlinear narrative untuk source footage; culturally specific storytelling.

## Hubungan antardomain

[M02](../../architecture/master-map.md#m02), [M04](../../architecture/master-map.md#m04), [M11](../../architecture/master-map.md#m11), [M12](../../architecture/master-map.md#m12), [M15](../../architecture/master-map.md#m15), [M19](../../architecture/master-map.md#m19), [M20](../../architecture/master-map.md#m20).

## Jalur sumber

[R01](../../evidence/sources.md#r01), [R02](../../evidence/sources.md#r02), [R03](../../evidence/sources.md#r03).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.
