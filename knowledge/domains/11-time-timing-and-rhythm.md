# M11 — Time Timing and Rhythm

## Manifestasi yang ditampilkan

Entry, action, pause, hold, repetition dan exit membentuk pace video. Timing membuat perubahan terlihat pada saat yang meaningful terhadap scene dan audio.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Clock, timeline evaluation, rendered sample cadence dan exposure different. FPS alone does not establish perceived smoothness or narrative pacing.

## Fondasi yang membentuk tampilan

Monotonic time, rational frame rates, phase, local/global timelines, time remapping, sampling dan signal rhythm. Pure time evaluation allows seek and offline reproducibility.

## M11.01 — Clock and origin

Time requires clock origin/unit; audio/video/scene clocks may differ.

**Model / mekanisme.** Local=(global−start)rate under simple single-clip assumptions.

**Implementasi.** Store clock IDs and convert at boundaries.

**Kegagalan tampilan.** Subtract timestamps from different clocks.

**Pemeriksaan.** Known offsets/rates and seek tests.

## M11.02 — Duration phase iteration

Delay/active/hold/exit regions need exact boundary semantics.

**Model / mekanisme.** Progress definition includes loops/direction/fill policy.

**Implementasi.** Pure evaluator handles before/after/inactive/zero duration.

**Kegagalan tampilan.** Last frame jumps, repeat event duplicates.

**Pemeriksaan.** Boundary times and reverse/loop cases.

## M11.03 — Cadence rational sampling

Frame timestamps should derive from index, not repeated addition.

**Model / mekanisme.** t_n=n q/p for fps=p/q.

**Implementasi.** Rational arithmetic or bounded conversions; retain PTS.

**Kegagalan tampilan.** Drift from rounded rate or cumulative additions.

**Pemeriksaan.** Frame count/first-last/spacing.

## M11.04 — Spacing and rhythm

Timing controls event positions; spacing controls displacement samples. Repeats and rests create rhythm.

**Model / mekanisme.** Beat map with accents, holds and contrast.

**Implementasi.** Record visual cue times and intended rhythmic function.

**Kegagalan tampilan.** All equal intervals or perpetual activity.

**Pemeriksaan.** Full playback and narrative/audio relation.

## M11.05 — Readable holds

Information may appear gradually; completed-readable interval differs total beat.

**Model / mekanisme.** Available hold=end_readable−start_readable.

**Implementasi.** Derive actual reveal/exit windows for content.

**Kegagalan tampilan.** Hold includes hidden/blurred text.

**Pemeriksaan.** Content completeness and native readability.

## M11.06 — Time remapping

u(t) changes velocity/acceleration through chain rule.

**Model / mekanisme.** xprime=pprime uprime; xdoubleprime=pdoubleprime uprime²+pprime udoubleprime.

**Implementasi.** Store warp function and continuity requirements.

**Kegagalan tampilan.** Continuous position with velocity jump.

**Pemeriksaan.** Derivatives at segment/rate boundaries.

## M11.07 — Seeking stateful simulations

Stateless animation can evaluate arbitrary t; simulation needs replay/checkpoint/analytic propagation.

**Model / mekanisme.** evaluate(t) distinct advance(dt).

**Implementasi.** Seed/state checkpoint includes model/version/time.

**Kegagalan tampilan.** Seek advances old state twice.

**Pemeriksaan.** Same t from multiple histories.

## M11.08 — Synchronization cues

Audio accents, subtitles and visual events need time mapping.

**Model / mekanisme.** Marker/clock alignment and output delay policy.

**Implementasi.** Schedule cues explicitly; verify decoded markers.

**Kegagalan tampilan.** Start sync good but drift by end.

**Pemeriksaan.** Beginning/middle/end technical markers.

## M11.09 — Cadence versus exposure

Exposure integrates scene interval; frame interval schedules outputs.

**Model / mekanisme.** Blur distance≈speed×exposure for ideal translation.

**Implementasi.** Define shutter placement/sample method.

**Kegagalan tampilan.** Exposure mistaken duration, blur hides wrong timing.

**Pemeriksaan.** Known moving geometry and decoded timing.

## Penurunan mekanisme dan contoh terhitung

At60fps with120frames: timestamps n/60 for n0…119; last sample1.9833s, nominal coverage2s. Endpointt2 is not sampled. If final exact pose should visible, design hold or evaluation policy intentionally. For30000/1001fps, use rational timestamps, not29.97rounding. Tempo120beats/min gives.5s per beat, but onset detection does not automatically equal musical beat.

## Kasus produksi

Scene timing maps voice phrase, token travel, text availability and settle. Changing fps does not change durations; renderer samples same evaluator. If short format requires faster video, content and readable windows are reevaluated, not globally accelerated without review.

## Memilih teknik dan trade-offs

Clock-driven for offline sequence; authored cue timeline for precise story; simulation state for physical systems. Higher cadence increases rendering cost; exposure and antialias need separate choices.

## Alur kerja operasional

Specify clocks/fps; define beats/intervals; evaluate boundary semantics; allocate holds; align cues; support seek/replay; sample index grid; verify final PTS/duration.

## Verifikasi dan kriteria penguasaan

Dapat distinguish sample time/coverage/exposure and reproduce exact cue timeline. Perceived rhythm/smoothness not proved by arithmetic alone.

## Cabang spesialis dalam cakupan

Timecode/drop-frame notation, multirate systems, phase synchronization, continuous-time evaluation, event-driven simulation, temporal cognition and frame-rate conversion.

## Hubungan antardomain

[M01](../../architecture/master-map.md#m01), [M06](../../architecture/master-map.md#m06), [M10](../../architecture/master-map.md#m10), [M12](../../architecture/master-map.md#m12), [M15](../../architecture/master-map.md#m15), [M19](../../architecture/master-map.md#m19), [M20](../../architecture/master-map.md#m20), [M21](../../architecture/master-map.md#m21), [M22](../../architecture/master-map.md#m22).

## Jalur sumber

[R21](../../evidence/sources.md#r21), [R23](../../evidence/sources.md#r23), [R24](../../evidence/sources.md#r24).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.
