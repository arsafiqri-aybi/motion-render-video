# Cloth, fluids dan volumes: representasi ke tampilan

## Representasi berbeda

Cloth surface mengutamakan stretching/bending/contact; fluid flow membutuhkan transport/pressure/boundaries; smoke/fire volume juga mempunyai density/temperature/emission appearance. Mesh yang bergerak seperti kain tidak otomatis hasil material physics yang benar.

## Simulation concern

Cloth constraint stiffness, timestep dan solver iterations dapat berinteraksi. Contact thickness membantu mencegah penetrasi tetapi dapat menghasilkan visible gaps. Fluids memakai representations grid, particles atau hybrid; boundary conditions menentukan leakage/solid interaction. A volume renderer membaca fields yang mungkin memerlukan interpolation antar simulation frames.

## Coupling

Pisahkan simulation resolution dari render detail. Subdivision menambah visual smoothness tetapi tidak menambah detail dynamics yang tidak ada di simulation. Noise detail tambahan boleh menjadi art direction asalkan tidak disamakan dengan solved turbulence. Surface extraction dapat menimbulkan popping jika topology/threshold berubah.

Untuk homogeneous extinction sigma, transmittance sepanjang ds mengikuti exp(-sigma*ds). Jika step size berubah, opacity per step perlu mengikuti ds; fixed opacity membuat appearance bergantung sample count. Smoke density field dan shaded image adalah tahap berbeda sehingga diagnosis harus memeriksa keduanya.

## Test plan

Hanging cloth under known load, freefall patch, contact drape; fluid box/boundary, mass surrogate/divergence; homogeneous volume transmittance. Halve timestep/grid step/render step secara terpisah untuk menentukan penyebab artifact. Cache version, units, seeds dan field conventions.

## Batas

Tidak ada solver fluid/cloth di demo. Physics manuals/project R26/R30 adalah candidate routes. Penguasaan memerlukan specific solver tests dan rendered cases. Domain M13/M16/M17/M21.
