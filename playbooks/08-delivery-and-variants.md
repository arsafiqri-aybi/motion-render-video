# Delivery, variant dan bukti hasil

## Contract

Buat spesifikasi output per variant: aspect, resolution, frame rate, duration, codec/container, alpha, color, audio channels, captions dan message acceptance. “Video final” tanpa contract membuat banyak failures terlambat diketahui.

## Re-layout

Landscape→portrait dapat memakai fit, crop atau recompose. Fit memberi bars/space; crop menghilangkan informasi; recompose mengubah layout. Pilih berdasarkan information importance, bukan hanya command resize. Text size serta safe margin dihitung ulang. Camera FOV/aspect dapat mengubah framing walau object geometry sama.

## Build

Resolve required assets/fonts lalu render. Scene evaluator, simulation/cache dan temporal sampling memakai time conventions explicit. Simpan versions, configuration, seed dan hashes. Run report selalu terkait current inputs, bukan hasil build lama.

## Encode

Codec/container/pixel format dipilih sesuai target. Metadata color harus cocok actual conversion; menulis BT709 tag bukan transform dari sRGB. Alpha master perlu format yang mendukung alpha. Audio sample rate/channel mapping serta priming/padding diperiksa setelah decode.

## Gates

Engineering: dimensions, framecount, timestamps, stream durations, decode errors, tags, audio properties. Visual: missing layers, edges, banding, typography, safe areas dan continuity. Audio: intelligibility, cue relation, clicks, mix. Semantic: pesan dan factual integrity. Accessibility/comfort checks memakai method applicable; tidak otomatis PASS karena ffmpeg sukses.

## Packaging

Sertakan final media, cue/config source, asset provenance, reports dan limitations. Jangan menyebut all domains executed dari single flat demo. Jika upload/distribute ditujukan ke platform tertentu, verify current requirement sebelum final export.

## Penguasaan

Mampu menjelaskan setiap failed gate dan memperbaikinya pada mechanism yang benar. Video besar atau bitrate tinggi bukan substitute quality evidence. Domain M01/M06/M07/M19/M20/M21/M22.
