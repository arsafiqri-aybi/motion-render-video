# M13 — Transformation and Deformation

## Manifestasi yang ditampilkan

Objek dapat berubah ukuran, orientasi, siluet, volume yang terasa, atau identitas bentuk. Transformasi adalah perubahan pemetaan; deformasi mengubah hubungan internal titik. Penonton menilai kesinambungan bentuk, berat, serta apakah perubahan terasa seperti benda yang sama.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Mencakup transformasi affine, morphing, warp, deformasi mesh, rig dan skinning. Pemilihan kamera di M14, simulasi deformasi akibat gaya di M16, dan sampling hasil di M21. Transform tidak selalu mempertahankan luas atau volume.

## Fondasi yang membentuk tampilan

Gunakan representasi lokal sebelum world transform, korespondensi titik, parameter kurva, Jacobian untuk skala lokal, serta interpolasi rotasi yang sesuai. Matriks memungkinkan komposisi tetapi urutan perkalian memengaruhi hasil.

## M13.01 — Pivot and affine transformation

Pivot mengatur titik yang tampak menetap ketika objek berputar atau membesar.

**Model / mekanisme.** Pemetaan p'=T(c) R S T(-c)p; nonuniform scale dapat mengubah sudut.

**Implementasi.** Simpan pivot sebagai data lokal, lalu susun parent transform secara eksplisit.

**Kegagalan tampilan.** Logo mengorbit tanpa sengaja atau skala merusak stroke.

**Pemeriksaan.** Periksa bahwa titik pivot tetap pada lokasi yang diinginkan di beberapa waktu.

## M13.02 — Shape correspondence

Morph terlihat kontinu jika fitur semantik mempunyai pasangan yang konsisten.

**Model / mekanisme.** Dua kontur perlu orientasi, titik awal, jumlah titik, dan urutan korespondensi yang sesuai.

**Implementasi.** Resample sepanjang arc length, sejajarkan landmark, lalu interpolasi koordinat.

**Kegagalan tampilan.** Kontur menyilang, twist mendadak, lubang berubah secara tidak terkendali.

**Pemeriksaan.** Uji signed area, self-intersection dan landmark pada fase tengah.

## M13.03 — Path morphing

Kurva berubah melalui control points dan struktur segmen.

**Model / mekanisme.** P(u,t) memakai basis kurva tetap dengan control points yang bergantung t.

**Implementasi.** Samakan jenis segmen dan parameterisasi sebelum mengubah titik; pisahkan perubahan topology.

**Kegagalan tampilan.** Speed kontur tidak rata dan bagian penting meleleh.

**Pemeriksaan.** Overlay beberapa kontur intermediate dan plot kecepatan landmark.

## M13.04 — Squash and stretch

Perubahan proporsi menampilkan elastisitas, impact dan berat.

**Model / mekanisme.** Dalam pendekatan 2D luas konstan, sx*sy=1; dalam 3D volume memakai sx*sy*sz=1.

**Implementasi.** Pilih axis impact, pivot kontak dan amplitudo deformasi berdasarkan aksi.

**Kegagalan tampilan.** Benda mengembang seperti balon saat seharusnya padat.

**Pemeriksaan.** Bandingkan luas atau volume bila preservation memang menjadi tujuan artistik.

## M13.05 — Mesh and lattice deformation

Medan perpindahan mengubah banyak titik secara koheren.

**Model / mekanisme.** x'=x+d(x,t); determinant Jacobian nol menunjukkan local collapse.

**Implementasi.** Pakai lattice kasar untuk kontrol besar lalu subdivision untuk detail.

**Kegagalan tampilan.** Foldover, stretching tekstur atau pinching.

**Pemeriksaan.** Periksa determinant, edge length dan normals selain tampilan render.

## M13.06 — Rigging and skinning

Gerak kontrol diterjemahkan menjadi pose permukaan.

**Model / mekanisme.** Linear blend skinning menjumlahkan weighted bone transforms; bobot berjumlah satu.

**Implementasi.** Pisahkan rig controls dari deform bones dan simpan bind pose.

**Kegagalan tampilan.** Candy-wrapper twisting dan volume sendi mengempis.

**Pemeriksaan.** Test pose ekstrem, weight normalization dan sambungan deformasi.

## M13.07 — Rotation interpolation

Rotasi interpolasi perlu jalur yang jelas tanpa lompatan representasi.

**Model / mekanisme.** Quaternion q dan -q merepresentasikan orientasi sama; pilih hemisphere sebelum slerp.

**Implementasi.** Normalisasi quaternion, tangani rotasi kecil dan tentukan jalur untuk putaran lebih dari 180 derajat.

**Kegagalan tampilan.** Flip, gimbal lock atau putaran mengambil arah yang salah.

**Pemeriksaan.** Plot orientasi dan bandingkan endpoint serta angular speed.

## M13.08 — Warp and displacement

Gambar berpindah mengikuti medan koordinat, berbeda dari mengganti nilai warna.

**Model / mekanisme.** Sampling output sering memakai inverse mapping agar tidak meninggalkan holes.

**Implementasi.** Bedakan normalized UV, piksel, satuan world dan boundary modes.

**Kegagalan tampilan.** Tepi robek, aliasing dan detail hilang karena magnification.

**Pemeriksaan.** Gunakan checker grid dan impulse image untuk menguji warp.

## M13.09 — Topology change and staged morph

Perubahan jumlah komponen tidak selalu dapat diwakili interpolasi titik sederhana.

**Model / mekanisme.** Birth, split, merge dan hole closure membutuhkan transisi representasi.

**Implementasi.** Gunakan mask reveal, implicit fields atau crossfade terkendali saat topology berubah.

**Kegagalan tampilan.** Shape popping atau transparency yang membocorkan dua identitas.

**Pemeriksaan.** Tinjau frame sebelum, saat dan sesudah topology event.

## Penurunan mekanisme dan contoh terhitung

Contoh squash 2D: tinggi dikurangi menjadi 0.8 kali awal. Jika luas persegi panjang ingin dijaga, lebar perlu dikali 1/0.8=1.25. Ini syarat geometris untuk model tersebut, bukan bukti bahwa semua karakter harus menjaga luas. Untuk pivot c=(10,20), transform p'=c+s(p-c) mempertahankan p=c untuk setiap s. Menguji invariant pivot lebih kuat daripada sekadar melihat satu frame.

Morph dua lingkaran ke persegi dapat memakai sampling radial dengan titik awal sama. Namun korespondensi radial tidak cocok untuk semua bentuk concave; bentuk yang tidak star-shaped dapat memiliki beberapa intersection sepanjang satu ray.

## Kasus produksi

Logo lingkaran berubah menjadi kartu dengan sudut bulat. Pertahankan center dan empat landmark arah utama; resample kontur dengan jumlah sama; batasi distorsi di sisi yang berisi teks; masukkan teks setelah area aman cukup besar. Render intermediate pada 25%, 50%, 75%. Jika topology tidak cocok, ubah rancangan transisi daripada memaksa interpolation.

## Memilih teknik dan trade-offs

Affine cocok untuk posisi/orientasi tanpa perubahan bentuk internal. Path morph cocok untuk siluet dengan korespondensi jelas. Mesh cocok untuk permukaan dengan kebutuhan deformation lokal. Rig lebih mahal saat setup tetapi memberi kontrol ulang yang konsisten. Implicit morph dapat mengatasi topology dengan biaya surface extraction dan kontrol identitas yang berbeda.

## Alur kerja operasional

1. Nyatakan bagian yang harus tetap: center, anchor, contact atau volume.
2. Pilih representasi dan korespondensi.
3. Tentukan parameter perubahan dan timing.
4. Uji midpoint sebelum menghaluskan easing.
5. Periksa distortion, topology dan shading.
6. Render sequence pada ukuran delivery.

## Verifikasi dan kriteria penguasaan

Penguasaan: mampu menjelaskan transform order, memperbaiki crossing contour, memilih rotasi quaternion dengan jalur tepat, dan membedakan kegagalan geometri dari kegagalan rasterisasi. Test numerik membantu invariant; kualitas identitas morph tetap memerlukan penilaian visual.

## Cabang spesialis dalam cakupan

Dual quaternion skinning, blend shapes, pose-space deformation, free-form deformation, differential coordinates, ARAP, signed distance morphing, remeshing, corrective shapes, texture-space warps. Metode ini memerlukan model dan evaluasi tersendiri.

## Hubungan antardomain

[M05](../../architecture/master-map.md#m05), [M09](../../architecture/master-map.md#m09), [M10](../../architecture/master-map.md#m10), [M16](../../architecture/master-map.md#m16), [M21](../../architecture/master-map.md#m21).

## Jalur sumber

[R06](../../evidence/sources.md#r06), [R07](../../evidence/sources.md#r07), [R11](../../evidence/sources.md#r11), [R26](../../evidence/sources.md#r26).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.

## Pendalaman produksi

[Deformation, correspondence dan local distortion](../deep-dives/13-deformation-correspondence-and-jacobian.md) — decision/model/counterexample yang melengkapi chapter ini.
