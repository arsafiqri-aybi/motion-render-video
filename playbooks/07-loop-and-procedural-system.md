# Procedural loop tanpa seam

## Contract

Loop T detik memiliki periodicity visual dan audio yang disengaja. Tentukan apakah sifat loop benar-benar periodic, hanya approximate ambience, atau sequence yang ditutup dengan transition.

## Periodic model

Oscillator sin(2*pi*k*t/T+phi) periodic jika k integer. Untuk k noninteger, state diT tidak sama awal. Gerak dengan noise arbitrary tidak otomatis loop; gunakan periodic coordinate embedding seperti(cos(2*pi*t/T),sin(2*pi*t/T)) pada field yang sesuai atau crossfade sequence carefully.

Particle loop memerlukan birth/death wrap yang menjaga distribution serta identity. State physics chaotic tidak dapat dibuat perfect periodic hanya dengan modulo time pada state history. Gunakan cache closure yang diperiksa atau pilih procedural model periodic.

## Render interval

Jika T=4s,30fps→120frames di t0..119/30, jangan tambah frame120/30=4. Audio waveform/decay tail harus continuity atau intentional crossfade. Jika audio transition memakai overlap, verify resulting duration dan phase cancellation.

Camera pose dan light parameters juga periodic; hanya object position yang loop belum cukup. Blur shutter di boundary perlu sampling wrapped time agar exposure tidak membekukan stateakhir. Compositing history/trails harus wrap/cache dengan convention yang konsisten.

## Perceptual design

Perfect numeric continuity belum menjamin seam tidak terasa: event timing, accent audio atau repeated announcement dapat tetap menandai restart. Untuk ambient loop, kurangi standout pulse di boundary. Untuk branded loop, boundary accent dapat sengaja dipakai.

## QA

Concatenate tiga putaran, inspect seam frames, velocity serta audio click. Compare value/derivative endpoints dalam scene model. Evaluate encoded playback gap separately karena player behavior berbeda dari file contents. Domain M10/M11/M15/M16/M17/M19/M21.
