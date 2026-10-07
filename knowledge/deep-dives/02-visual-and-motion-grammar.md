# M02 — Visual grammar dan motion grammar

## Sistem identity

Definisikan vocabulary: shape family, corner treatment, stroke behavior, typography hierarchy, palette roles dan material cues. Motion grammar menjelaskan cara elemen muncul, berubah, bergabung dan berhenti. Sistem yang konsisten tidak membutuhkan semua elemen bergerak identik; variasi ditentukan role.

Contoh authored grammar untuk explainer teknis: objects memakai corners kecil; relationships memakai thin connectors; state change memakai accent orange; camera bergerak hanya ketika spatial context berubah; labels masuk dengan short translation lalu hold statis. Angka durasi/amplitude dicatat per brief, bukan dijadikan hukum visual universal.

## Constraint dan variation

Pisahkan invariants dan variables. Invariants dapat berupa logo proportions, font family, channel colors dan hierarchy. Variables dapat berupa arrangement, object count, shot angle dan local timing. Variasi yang melanggar invariant memerlukan alasan atau versi identity baru.

Atur parameter dengan unit: radius pixels atau normalized local geometry; travel sebagai fraction viewport; spring settling seconds; opacity0–1. Nama seperti premium/smooth tidak cukup untuk reproduce system. Berikan example serta counterexample: overshoot besar dilarang pada numeric labels karena membuat value ambiguity.

## Cross-format identity

Landscape dan portrait dapat mempunyai layout berbeda sambil mempertahankan roles. Jangan mempertahankan semua positions atas nama consistency. Teks, spacing, motion amplitude dan framing disesuaikan agar informasi sama tetap tampil. Identitas dinilai pada hubungan serta behavior, bukan identik pixel.

## Review

Buat contact set lintas shots dan formats, plus playback sequences untuk motion grammar. Cari accidental exceptions: CTA mempunyai easing berbeda tanpa role, radius berubah setelah scale, warna accent dipakai untuk background lalu kehilangan fungsi. Pilih satu correction pada sistem terlebih dahulu sebelum memperbaiki banyak shot secara manual.

Tidak ada klaim bahwa grammar tersebut menjamin audience emotion; tone adalah design intent yang perlu review sesuai konteks.

## Hubungan dan status

Konsep: M02.03, M02.04, M02.06, M02.08. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
