# M15 — Batas edit, meaning dan match continuity

## Boundary sebagai perubahan state

Cut mengubah image secara diskrit; bukan berarti harus discontinuous meaning. Cocokkan action phase, subject identity, screen direction dan information role. Graphic match dapat memakai lokasi/shape sementara action match memakai temporal progression.

## Handle arithmetic

Shot sourcesA/B mempunyai additional handles. Output overlap0.5s mengambil bagian dari dua shot, sehingga3s+3s-0.5s=5.5s jika durations yang diberikan inclusive output portions. Jika3s adalah trimmed non-overlap duration dan handles ditambahkan, hitungan berbeda. Nyatakan definition sebelum menghitung.

## Retiming derivative

Source time g(t) menentukan speed ratio g'(t). Jika action positionP(sourceTime), velocity outputP'(g(t))*g'(t). Acceleration memuat P''(g)*(g')²+P'(g)*g''. Ramp yang membuat g' jump membuat speed jump meski source motion smooth. Audio traitement harus mengikuti intent: remap waveform, preserve voice timing, atau replace sound cues.

## Match constraints

Untuk dua shots dengan landmark layar L_A danL_B pada cut, distance small membantu planned visual match. Namun small distance tidak membuktikan seamless perception. Match scale, direction dan action phase bisa lebih penting; pilihan berdasarkan fungsi edit.

Jika camera passes occluder untuk hidden cut, evaluate minimum coverage. Celah satu frame dapat membocorkan scene replacement. Motion blur exposure juga dapat mencampur before/after states di cue boundary; scene evaluator needs declared cut policy.

## Verification

Inspect frames±2aroundcut, plus full sequence. Optical flow interpolation perlu review occlusion/disocclusion dan changing shapes. Codec artifacts di cut dapat berbeda dari wrong continuity. Numeric overlap/PTS checks membuktikan duration/cadence; meaning/pace acceptance memerlukan sequence review dan audience question.

## Hubungan dan status

Konsep: M15.01, M15.02, M15.03, M15.07. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
