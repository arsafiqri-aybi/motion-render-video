# Rational clocks, duration dan audiovisual sync

## Clock convention

Frame n pada rate p/q memiliki t=nq/p. N frame intervals mencakup Nq/p seconds, sedangkan timestamp terakhir(N-1)q/p. Menyamakan last timestamp dengan duration menyebabkan ekspor atau audio dipotong satu frame.

Audio sample i pada Fs memiliki waktu i/Fs. Cue seconds tau dipetakan ke sample round(tau*Fs); quantization error maksimal sekitar half sample bila rounding nearest. Mapping ke frame nearest menghasilkan error sampai half frame. Visual cue dapat berada pada subframe selama shutter integration; pixel manifestation dan mathematical event perlu dibedakan.

## Fractional rates

30000/1001≈29.97002997. Decimal29.97 berbeda sedikit. Pada workflow panjang, drift serta timecode conventions perlu exact rational values. Drop-frame timecode adalah penomoran yang mengompensasi clock display; ia bukan instruksi menghapus image frames.

## Codec delay

AAC dapat membawa priming dan padding. Encoded packet timing, declared stream duration dan decoded sample count dapat berbeda dengan source PCM length. Gunakan decoded measurement dan container timing yang relevan; jangan menambahkan manual offset tanpa bukti.

## Cue sheet

Satu file menyimpan cue time, function, visual event dan audio event. Jangan copy magic number ke dua scripts. Jika retiming, gunakan mapping yang sama atau sengaja dokumentasikan audio treatment. Longer clips perlu cek awal/tengah/akhir untuk membedakan fixed offset dari drift.

## Pemeriksaan

Tes demo memeriksa rational sample time, decoded PTS cadence dan threshold-defined audio onsets. RMS threshold/window adalah operational definition, bukan precise perceptual onset. Tolerance[-15ms,+35ms] hanya untuk synthetic demo envelope. [M11](../domains/11-time-timing-and-rhythm.md), [M19](../domains/19-sound-design-music-and-audiovisual-synchronization.md).
