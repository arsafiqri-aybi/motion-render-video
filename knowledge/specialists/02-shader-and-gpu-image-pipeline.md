# Shaders dan GPU sebagai lapisan image generation

## Manifestasi

Shader dapat membentuk gradient, displacement, lighting, particle appearance dan post-process images. GPU dipilih untuk kebutuhan komputasi, bukan dianggap induk motion-video terpisah dari hasilnya.

## Architecture

Vertex processing mengatur geometry attributes serta projected positions; fragment processing membentuk pixel-related outputs; compute dapat membentuk fields, particles atau image buffers. Resource bindings, texture formats, buffer layout dan pipeline state harus sesuai API/language. [R37](../../evidence/sources.md#r37) adalah jalur WGSL; document/index dibuka, detail normative layouts perlu section inspection saat implementasi.

Screen-space normalized UV, texel coordinates, clip/NDC dan world positions jangan dicampur. Aspect correction diperlukan ketika circle dihitung dari UV tetapi target bukan square. Derivative-based edge width perlu memperhatikan shader execution context dan sampling footprint.

## Offline video

GPU render target/readback menghasilkan frames yang diberi timestamps dari offline clock. Wall-clock refresh tidak boleh menentukan final motion speed. Schedule resources agar frames tidak hilang saat readback tertunda. Workgroups/parallel writes perlu algorithm yang tidak race; seed tidak menyelesaikan race-condition determinism.

## Test plan

Mulai known gradient, checkerboard, transformed triangle dan circle yang tetap bulat di dua aspects. Validate buffer layout dengan known values; compare CPU reference untuk simple equations. Periksa output finite/range, alpha/color conventions, frame count dan readback order. Gunakan tolerances yang mempertimbangkan precision, bukan force pixel hashes lintas semua GPU.

## Batas

Tidak ada shader/GPU execution claim pada build ini. Implementasi demo CPU flat2D dan opaque3D adalah technology layers yang benar-benar dijalankan; belum ada GPU execution. Domain M05/M08/M17/M18/M21/M22.
