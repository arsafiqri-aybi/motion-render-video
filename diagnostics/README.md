# Diagnosis dari kegagalan yang terlihat

Jangan langsung menaikkan quality settings. Pisahkan representation, motion model, temporal sampling, compositing dan encoding dengan controlled tests.

| Gejala | Kemungkinan mechanism | Tes pemisah | Perbaikan yang relevan |
|---|---|---|---|
| Speed curve tidak rata | Geometry parameterization | Plot equal-time/length markers | Arc-length map; kemudian pilih travel easing |
| Gerak membentur hold | Velocity discontinuity | Finite difference endpoint | Endpoint derivatives atau connector trajectory |
| Spring eksplosif | Integrator/timestep/stiffness | Halve timestep; compare energy | Solver/model sesuai; analytic solution untuk kasus terbatas |
| Gerak berubah dengan fps | Per-frame increments/decay | Compare same-time state24/60fps | Absolute time atau fixed simulation step |
| Text kabur saat reveal | Relative motion/shutter/filter | Single-sample render vs blurred | Stable reading window; tune shutter/trajectory |
| Morph crossing | Point correspondence/topology | Intermediate contour overlay | Landmark alignment/resampling/alternate representation |
| Pivot bergeser | Transform order/space | Check pivot invariant | Correct local/world composition |
| Camera flip | Degenerate look-at up vector | Plot dot(view,up) | Fallback orientation/quaternion path |
| Depth terasa datar | No parallax/occlusion/form shading | Diagnostic landmarks | Camera/space/light design sesuai tujuan |
| Edge hitam transparan | Double premultiply/filter convention | Composite black/white patches | Correct alpha boundary handling |
| Midpoint blend gelap | Encoded-space averaging | Linear-light pixel oracle | Defined transfer conversion |
| Volume berubah dengan steps | Step-dependent opacity | Half step size compare | Extinction-based integration |
| Trail length berubah fps | Fixed per-frame decay | Check decay at same seconds | exp(-lambda*dt) |
| Noise berubah saat seeking | Order-dependent PRNG | Random frame order | Seeded identity atau deterministic replay/cache |
| Cloth jitter | Solver/contact/substeps | Contact/residual inspection | Specific solver tuning; not render denoise |
| Pattern shimmer | Spatial/temporal aliasing | Sample count/resolution sweep | Frequency control/filter/sampling |
| Bright pixels flicker | Render sample noise/denoiser | High-sample reference | Sampling/denoiser temporal review |
| Sound terlambat | Duplicate cue values/encode/onset definition | Decoded cue measurement | Shared clock; correct evidenced offset |
| Sync drift | Wrong rate mapping | Check early/middle/late | Exact rational timestamps/resample/conform |
| Color washed out | Range/transfer/tag mismatch | Probe + controlled patches | Actual conversion with matching metadata |
| Output no alpha | Pixel format/container | Probe channels + proof composite | Alpha-supporting master |
| Final extra hold | Duplicate loop endpoint | Framecount and boundary check | Half-open sampling |
| Portrait CTA terpotong | Blind crop/layout | Target-aspect bounds | Recompose with content priority |
| MP4 decode succeeds but pesan gagal | Semantic/reading issue | Target-viewer task | Revise narrative/hierarchy/dwell |

## Iterasi

1. Simpan gejala dengan timecode/frame index serta output spec.
2. Nyatakan dua hipotesis paling masuk akal.
3. Buat test yang memberi hasil berbeda untuk kedua hipotesis.
4. Ubah satu mechanism relevan dan rerender rentang masalah.
5. Periksa adjacent frames serta full sequence untuk regressions.
6. Catat evidence sesuai scope; jangan mengubah uncertain hypothesis menjadi fakta tanpa pemeriksaan.

Materi rinci ada di [master map](../architecture/master-map.md) dan [algoritma](../knowledge/algorithms/README.md).
