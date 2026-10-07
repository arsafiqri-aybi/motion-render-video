# Interval algebra untuk transisi dan loop

## Interval convention

Gunakan half-open[a,b): state aktif pada a dan tidak aktif pada b. Adjacent intervals[a,b),[b,c) tidak overlap atau double-own endpoint. Ini memudahkan event ordering dan frame count, tetapi continuous interpolation tetap perlu endpoint value policy.

## Overlap

Shot A durasi Da, B durasi Db, transition overlap O menghasilkan Da+Db-O jika keduanya dimanfaatkan penuh dan overlap menggantikan bagian masing-masing. Handles tambahan berada di source media; tidak harus menjadi output duration. Hitung output intervals setelah transitions, bukan menjumlahkan label shot yang ambiguous.

Opacity weights crossfade wA=1-u,wB=u berjumlah1. Itu belum memastikan luminance perceived constancy, readable overlap atau appropriate editorial transition. Color blending space harus dinyatakan.

## Loop

Period T, phase=(t mod T)/T. Untuk position seam, x(0)=x(T); velocity seam membutuhkan x'(0)=x'(T). Render N samples t=nT/N untuk n0..N-1. Jangan memasukkan frame t=T lagi karena identik dengan awal dan dapat memberi extra hold. Audio loop juga membutuhkan waveform continuity atau crossfade yang disengaja.

## Retiming

Source time g(t) monotonic untuk playback maju. Freeze memiliki derivative0; reverse memiliki derivative negatif. A transition saat reverse bukan otomatis reuse cue order forward. Optical flow hanya mengestimasi intermediate frames dan harus dicek pada occlusion atau shape changes.

## Pemeriksaan

Validate duration arithmetic, frameownership dan boundary values. Loop tiga kali untuk melihat seam, bukan hanya compare first/last thumbnails. Review cut function serta message timing. [M15](../domains/15-transitions-editing-and-continuity.md).
