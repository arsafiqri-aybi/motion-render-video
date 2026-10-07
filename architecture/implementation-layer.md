# Technology sebagai implementation layer

| Kebutuhan output | Contoh lapisan implementasi | Hal yang tetap perlu diputuskan |
|---|---|---|
| Timeline/2D motion graphic | Remotion, Manim, custom Python, browser animation capture | Absolute time, font/layout, rendering/capture fidelity |
| Vector graphic animation | SVG, Canvas, custom rasterizer | Path representation, compositing, edge sampling |
| 3D scene | Blender, Three.js, renderer khusus | Units, camera, material/light, samples, deterministic clock |
| GPU fields/effects | WebGL/GLSL, WebGPU/WGSL, Vulkan pipelines | Resources, precision, coordinate convention, readback/time mapping |
| Editing/timeline interchange | FFmpeg filtergraphs, OpenTimelineIO, editing tools | Overlap, source/output time, handles, audio alignment |
| Color/compositing | OCIO workflows, image-processing tools, compositor | Alpha convention, working/output space, precision |
| Encoding/probing | FFmpeg, ffprobe | Codec/container/pixel format, metadata, cadence, decode verification |

Daftar adalah mapping pilihan, bukan recommendation/version matrix. Spesifikasi serta API diperiksa pada versi aktual saat implementation. Build ini hanya mengeksekusi Python/Pillow/NumPy dan FFmpeg/ffprobe. Library easing/timeline tidak menggantikan keputusan motion model atau komunikasi; knowledge taxonomy tetap berpusat pada manifestasi.
