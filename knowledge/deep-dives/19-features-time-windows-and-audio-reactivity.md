# M19 — Feature windows dan audio-reactive timing

## Feature bukan sound understanding

RMS mengukur energy-like amplitude per window; spectrum menunjukkan frequency components dalam window; onset candidate menunjukkan perubahan menurut method. RMS peak bukan beat terverifikasi dan tone onset threshold bukan perceptual synchronization study.

Untuk samplesx_i, RMS=sqrt(sum x_i²/N). WindowN padaFs mempunyai coverageN/Fsseconds. JikaN240danFs48000→5ms. Window start, center atau end sebagai feature timestamp memberikan offsets berbeda. Dokumentasikan convention sebelum mengikat visual state.

## Smoothing

Filter first-order envelope dapat memakai a=exp(-dt/tau), y_next=a*y+(1-a)*input. Tau dalam seconds berbeda dari blendfactor per-frame. Attack/release asymmetric memberi respons accents serta tails tetapi menambah model-dependent lag. Compare expected response terhadap step/tone signals.

## FFT scope

Frequency-bin spacingFs/N; zero-padding menambah interpolation bins tetapi tidak membuat observation window lebih panjang. Window/hop, channel mixing dan level normalization memengaruhi feature. Harmonic content dapat mengubah dominant frequency tanpa beat baru; voice can dominate music band features.

## Offline motion video

Offline feature analysis dapat menghitung future context; realtime causal analysis tidak mempunyai future samples. Jika feature windowcentered, cue dapat bergeser dari live causal version. Sync audio/video actual encode needs mapping source analysis clock→output clock, including edits/retiming.

## Actual evidence

Demo2D menggunakan cue sheet dan tone synthesis, bukan automatic beat/ASR/music analysis. Decoder checks first 5 ms RMS window above0.001 around known cues; observed offsets+5ms memenuhi declared demo tolerance. Tidak ditafsirkan sebagai universal acceptable lip-sync threshold atau mastered soundtrack quality.

## Hubungan dan status

Konsep: M19.01, M19.02, M19.08. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
