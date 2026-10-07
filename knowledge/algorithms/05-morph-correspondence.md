# Morph dan korespondensi siluet

## Persoalan

Dua bentuk dengan jumlah vertex sama masih dapat twist jika vertex pertama, winding atau landmark correspondence berbeda. Morph bukan sekadar lerp setiap array index.

## Prosedur

1. Tentukan apakah topology cocok: jumlah components/holes.
2. Normalize winding dan pilih landmark semantik sebagai start.
3. Resample contour berdasarkan arc length untuk density konsisten.
4. Align landmark positions dengan mapping monotonic jika possible.
5. Interpolate points dan render intermediate.
6. Cek self-intersection, area, feature preservation serta edge sampling.

Untuk linear correspondence p_i(t)=(1-u)a_i+u*b_i, topology intermediate tidak otomatis dijamin walaupun endpoints sederhana. Test segment intersections dan signed area dapat mengungkap crossing; artistic identity tetap perlu review.

## Radial demonstration

Demo memakai family superellipse pada center sama: x=r*sign(cos a)*abs(cos a)^(2/n), y=r*sign(sin a)*abs(sin a)^(2/n). n=2 memberi circle, n>2 memberi silhouette square-like. Angle a menjaga correspondence. Ini cocok untuk family star-shaped tersebut; tidak menunjukkan general morph arbitrary paths.

Rounded square dari superellipse tidak identik dengan rounded rectangle yang memakai circular corner arcs. Pilih representasi sesuai silhouette yang dimaksud, bukan menganggap semua rounded shapes interchangeable.

## Alternatif

Mesh morph mempertahankan connectivity namun perlu mesh kualitas baik. SDF blending dapat split/merge topology tetapi interpolated field belum tentu signed distance; normals/contour thickness perlu diperiksa. Mask transition dapat lebih jelas untuk identity change dibanding forced morph.

## Pemeriksaan

Render quarter phases, overlay contour landmarks dan inspect slow/full playback. Jika feature hilang di tengah, mengubah easing hanya menyembunyikan sebentar; perbaiki correspondence atau transisi representation. [M13](../domains/13-transformation-and-deformation.md).
