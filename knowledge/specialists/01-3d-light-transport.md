# 3D light transport dan material appearance

## Manifestasi

Highlight mengikuti orientasi, shadows mengikat objek ke ruang, transmission memperlihatkan medium, dan reflections memberi informasi lingkungan. Parameter material tidak langsung menjamin identity; lighting/camera turut membentuk tampilan.

## Mechanism

Untuk model surface rendering, outgoing radiance memadukan emission dan integral incoming radiance dikali scattering serta cosine over directions. Renderer mengaproksimasi transport sesuai teknik. BRDF memodelkan reflection di surface; BSSRDF/volume diperlukan untuk phenomena yang berpindah lokasi di medium. [R18](../../evidence/sources.md#r18) hanya diperiksa pada introduction reflection models, bukan seluruh transport algorithm.

Albedo, metalness dan roughness adalah controls dari model tertentu, bukan direct perceptual adjectives. Periksa workflow material tool; roughness textures adalah data dan tidak diproses seperti sRGB color texture. Normal maps membutuhkan tangent basis convention dan transformed normals yang benar.

## Production test

Gunakan material spheres serta known lighting: diffuse-like, glossy, conductor, dielectric. Render camera fixed lalu ubah satu parameter. Pisahkan noise sampling dari intended microtexture. Compare contact shadow, highlights, roughness effect dan exposure. Untuk animation, denoiser serta moving reflections harus diperiksa sequence, bukan satu still.

## Trade-offs

Raster approximation dapat cocok motion graphic dengan art-directed shadows. Path tracing membantu transport kompleks tetapi noise serta cost naik. Stylization dapat sengaja menyederhanakan light; nyatakan intent agar tidak mendiagnosisnya sebagai physics bug.

## Batas

Repo menyediakan conceptual model serta test plan. Tidak ada actual PBR scene di demo. Penguasaan membutuhkan renderer-specific implementation, reference scenes dan convergence checks. Domain M08/M09/M14/M21.
