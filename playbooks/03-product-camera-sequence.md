# Product sequence dengan camera dan lighting

## Contract

Penonton harus memahami bentuk produk, fitur utama serta label penting. Tulis shot functions: orientasi keseluruhan, feature detail, demonstration, final hero. Lens dan lighting dipilih berdasarkan informasi ini.

## Scene preparation

Check units, mesh normals, scale, UV, material roles serta texture color/data spaces. Normal maps tidak diberi color transform sebagai color photograph. Tentukan contact/shadow agar produk mempunyai spatial anchor. Roughness dan environment reflections memberi bentuk; brightness saja tidak menyelesaikan material.

## Camera design

Tetapkan focal length/sensor/aspect dan projected bounds. Wide/detail progression memberi context, bukan sekadar orbit360°. Camera path memiliki start/end framing, target dan safe margin. Gunakan foreground/parallax hanya jika membantu bentuk. Jika label perlu dibaca, stabilkan camera atau hold pada shot relevan.

Focal length dan distance dapat dikopel untuk framing. Depth of field perlu menjaga informasi yang dimaksud sharp; terlalu sempit dapat menutupi label. Periksa camera near plane serta collision/occlusion saat path bergerak.

## Light and render

Bangun key/fill/rim dengan fungsi form separation. Reflection cards dapat memberi highlight yang diarahkan tanpa mengubah product material. Uji gray material untuk shape, lalu final material. Atur temporal samples dan render samples berdasarkan visible failure; jangan menaikkan semuanya serentak tanpa diagnosis.

## Editing/audio

Cut pada informasi baru atau action phase yang sesuai. Match screen direction dan scale cues. Sound design dapat menunjukkan material atau movement tetapi rights/provenance dicatat. Final hero hold memberi waktu membaca label dan CTA.

## QA

Check full-resolution label, moire, material noise/denoiser flicker, camera continuity, output color dan audio. Flat demo repo tidak menjalankan workflow3D ini; jika digunakan, simpan scene/renderer-specific reports. Domain M03/M08/M09/M14/M15/M19/M21/M22.
