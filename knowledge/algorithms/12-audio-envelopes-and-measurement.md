# Audio envelopes dan pengukuran cue

## Sintesis

Signal s(t)=A*a(t)*sin(2*pi*f*t+phi). Envelope mengatur attack serta decay. Jika signal berakhir saat amplitude nonzero, abrupt discontinuity dapat menimbulkan click. Pilih a(t) dengan smooth endpoints atau fade. Envelope demo memakai sin²(pi*n/L)*exp(-18t), dimulai0 dan mengecil mendekati akhir.

Frekuensi330,440,550,660Hz dipakai untuk empat cues. Ini authored design untuk onderscheid cue, bukan aturan material sound universal. Sample rate48kHz dan bandwidth tone jauh di bawah Nyquist; synthesis noise atau chirps membutuhkan perhatian aliasing tersendiri.

## Level

Amplitude gain dB=20log10(A). dBFS terkait digital full scale; loudness integrated bukan amplitude peak. Penjumlahan tracks dapat clip. Limit normalized sample peak saja tidak mengukur intersample true peaks. Jangan mengklaim broadcast loudness compliance dari satu peak check.

## Onset detector scoped

Decode AAC ke mono float PCM. Bagi menjadi windows5ms, hitung RMS=sqrt(mean(samples²)), cari window pertama>0.001 di sekitar cue. Window start memberikan observed onset menurut method; attack envelope dapat membuat threshold crossing lebih lambat dari mathematical start. Codec pre-echo/noise dapat memajukan crossing. Karena itu tolerance dinyatakan dan bukan zero-error claim.

## Duration

Source samples288000 untuk6s48kHz. Decoder dapat menghasilkan padding samples. Compare duration dengan tolerance yang sesuai encode; jangan truncate arbitrary lalu menganggap output original tepat. Visual PTS dan audio onset menguji properties berbeda.

## Pemeriksaan

Check silence, finite samples, headroom, all cues dan full decode. Listen dengan gambar untuk sound function; peak/rms cannot evaluate emotional fit. Demo tidak menjadi mastering/music composition benchmark. [M19](../domains/19-sound-design-music-and-audiovisual-synchronization.md), [pemeriksa](../../tools/verify_media.py).
