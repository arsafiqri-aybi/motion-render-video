# M19 — Sound Design Music and Audiovisual Synchronization

## Manifestasi yang ditampilkan

Audio memberi aksen, tekstur, emosi, spatial cue dan temporal struktur. Whoosh, impact, musik, voice-over dan keheningan dapat memperjelas gerak; hubungan audiovisual ditentukan oleh onset, envelope, frequency content serta fungsi pesan.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Mencakup audio untuk motion video, synthesis/asset selection, music timing, mixing dan sync. Haptics atau interactive audio masuk hanya jika mendukung output audiovisual terkait. Hak penggunaan asset dan provenance merupakan bagian production M22.

## Fondasi yang membentuk tampilan

Sample clock, amplitude, frequency, phase, envelopes, transient, spectral content, dBFS, channel mapping dan sample-rate conversion. Onset matematis, onset terdengar dan puncak visual bukan selalu waktu yang sama.

## M19.01 — Audio timebase and event alignment

Audio dan video memakai grid waktu berbeda.

**Model / mekanisme.** Audio sample n pada t=n/Fs; video frame m pada t=m/fps dengan timestamps.

**Implementasi.** Definisikan cue time dalam seconds/rational units dan map ke keduanya.

**Kegagalan tampilan.** Drift panjang, offset cue atau sync hanya tepat di awal.

**Pemeriksaan.** Ukur cue awal/tengah/akhir pada decoded output.

## M19.02 — Transient and envelope design

Envelope membentuk attack, sustain dan decay yang terasa mengikuti aksi.

**Model / mekanisme.** a(t) mengalikan oscillator/noise; smooth endpoints menghindari discontinuity.

**Implementasi.** Sesuaikan attack dengan impact atau acceleration, fade ending to zero.

**Kegagalan tampilan.** Click, tail berlebihan atau aksen terasa terlambat.

**Pemeriksaan.** Inspect waveform/onset dan listen dengan gambar.

## M19.03 — Whoosh impact and texture

Spectral evolution membantu menampilkan speed, material dan skala.

**Model / mekanisme.** Filtered noise, pitched components dan transients membentuk kelas suara.

**Implementasi.** Layer sedikit komponen dengan fungsi berbeda dan controlled bandwidth.

**Kegagalan tampilan.** Semua aksi berbunyi sama atau suara mendominasi pesan.

**Pemeriksaan.** Solo layers lalu compare full mix pada playback target.

## M19.04 — Music pulse meter and phrasing

Beat menyediakan struktur tetapi frasa musikal lebih panjang dari beat tunggal.

**Model / mekanisme.** Beat interval 60/BPM; bar length tergantung meter.

**Implementasi.** Buat beat grid serta phrase markers; pilih cue penting.

**Kegagalan tampilan.** Semua objek selalu bergerak pada beat tanpa hierarchy.

**Pemeriksaan.** Review frase utuh dan versi tanpa beat accents.

## M19.05 — Voiceover and information space

Ucapan membawa informasi yang bersaing dengan teks serta effects.

**Model / mekanisme.** Speech intervals dan pauses membentuk windows untuk visual emphasis.

**Implementasi.** Lock script lalu tempatkan key phrases, subtitle dan effect ducking.

**Kegagalan tampilan.** Kata tertutup musik atau gambar mendahului konteks terlalu jauh.

**Pemeriksaan.** Check intelligibility dan subtitle alignment.

## M19.06 — Mixing gain and headroom

Penjumlahan sinyal dapat clip walau masing-masing layer aman.

**Model / mekanisme.** Linear gain g=10^(dB/20); peaks dan loudness mengukur hal berbeda.

**Implementasi.** Gunakan meters, deliberate gain staging dan limiter bila sesuai target.

**Kegagalan tampilan.** Distortion, pumping atau silent clipped peaks.

**Pemeriksaan.** Measure sample/true peak dengan alat sesuai scope, lalu listen.

## M19.07 — Stereo spatial placement and mono

Posisi suara dapat membantu arah tetapi harus survive channel reduction.

**Model / mekanisme.** Pan law dan phase relationships memengaruhi perceived level.

**Implementasi.** Pilih panning yang mendukung scene; cek mono sum.

**Kegagalan tampilan.** Suara penting hilang karena phase cancellation.

**Pemeriksaan.** Compare stereo/mono dan channel balance.

## M19.08 — Audio reactive visuals

Visual dapat mengikuti envelope, band energy atau beat estimates.

**Model / mekanisme.** FFT magnitude memberi spectral representation bergantung window/hop.

**Implementasi.** Normalize, smooth attack/release dan pilih feature sesuai pesan.

**Kegagalan tampilan.** Visual jitter, gain-dependent behavior dan latency salah.

**Pemeriksaan.** Uji sinyal known-frequency, silence dan level changes.

## M19.09 — Silence accessibility and licensed assets

Keheningan dan captions memberi struktur serta akses informasi.

**Model / mekanisme.** Visual-only path harus tetap membawa pesan utama bila audio tidak tersedia.

**Implementasi.** Simpan license provenance, transcript/captions dan mix variants bila perlu.

**Kegagalan tampilan.** Pesan hanya tersimpan dalam sound effect atau hak asset tidak jelas.

**Pemeriksaan.** Review muted playback dan inventory asset rights.

## Penurunan mekanisme dan contoh terhitung

Pada 48 kHz, cue t=0.5 s jatuh di sample 24000. Pada 30 fps, frame 15 dimulai pada 0.5 s. Ini alignment grid yang tepat, tetapi bukan jaminan persepsi onset sama karena visual exposure, fade attack dan playback latency. Pada 29.97 fps (30000/1001), waktu frame n=n*1001/30000; jangan memakai 29.97 sebagai exact fraction ketika sync panjang penting.

Musik 120 BPM mempunyai interval beat 0.5 s. Pada 30 fps itu 15 frame intervals. Pada 24 fps itu 12. Amplitude layer 0.7+0.7 dapat menghasilkan 1.4 jika peaks sefase, melebihi normalized full scale. Headroom perlu dinilai dari mix, bukan volume slider terpisah.

## Kasus produksi

Demo shape landing memakai tone pendek pada impact. Cue disimpan sekali sebagai seconds lalu dipakai renderer dan synthesizer. Attack/decay smooth menghindari click. Final encoded video didecode untuk mengukur signal around cues; hasil listening tetap dibutuhkan karena peak alignment bukan evaluasi kualitas sound design.

## Memilih teknik dan trade-offs

Synthesis cocok accent terkontrol dan reproducible. Recorded asset cocok material specificity tetapi perlu rights serta editing. Music-driven timing cocok phrase-led storytelling; narasi-driven timing dapat memakai musik sebagai layer penopang. Auto beat detection harus diverifikasi, terutama musik syncopated.

## Alur kerja operasional

1. Susun cue sheet dengan fungsi, waktu dan prioritas.
2. Pilih sumber suara serta rights.
3. Bentuk envelope dan spectral role.
4. Mix dengan voice serta headroom.
5. Encode lalu decode dan ukur offset/duration.
6. Listen stereo, mono, muted dan device target.

## Verifikasi dan kriteria penguasaan

Penguasaan: mampu menghitung sample/frame alignment, membedakan peak dari loudness, menghindari click serta clipping, dan menjelaskan audio-reactive feature/latency. Demo tone bukan mastering musik atau compliance semua platform.

## Cabang spesialis dalam cakupan

Spectral flux onset detection, phase vocoders, time stretch, resampling, sidechain compression, loudness normalization, true-peak measurement, spatial audio, ambisonics, subtitle timing, audio description, sample-accurate automation.

## Hubungan antardomain

[M01](../../architecture/master-map.md#m01), [M11](../../architecture/master-map.md#m11), [M12](../../architecture/master-map.md#m12), [M15](../../architecture/master-map.md#m15), [M20](../../architecture/master-map.md#m20), [M22](../../architecture/master-map.md#m22).

## Jalur sumber

[R24](../../evidence/sources.md#r24), [R33](../../evidence/sources.md#r33), [R34](../../evidence/sources.md#r34).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.

## Pendalaman produksi

[Feature windows dan audio-reactive timing](../deep-dives/19-features-time-windows-and-audio-reactivity.md) — decision/model/counterexample yang melengkapi chapter ini.
