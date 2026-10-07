# Solver stability, accuracy dan visual convergence

## Tiga pertanyaan

Stability: error tidak tumbuh tanpa batas untuk model/timestep tertentu. Accuracy: trajectory mendekati solusi yang diinginkan. Constraint satisfaction: pembatas geometry/contact dipenuhi. Solver dapat stabil tetapi tidak cukup akurat, atau posisi tampak baik tetapi velocity/energy salah.

## Explicit Euler oscillator

x'=v, v'=-omega²x. Explicit Euler update x_next=x+h*v;v_next=v-h*omega²*x. Eigenvalues update1±i*h*omega memiliki magnitude sqrt(1+(h*omega)²)>1 untuk h>0. Untuk oscillator ideal tanpa damping, amplitude numerical tumbuh. Ini counterexample penting terhadap asumsi “timestep kecil pasti stable”.

Symplectic Euler mengupdate v dahulu lalu x memakai v baru. Matrix mempunyai determinant1 dan trace2-(h*omega)²; stability linear membutuhkan h*omega<2 dengan caveat boundaries. Energy tidak identik exact setiap step, walaupun behavior jangka panjang dapat lebih baik pada kasus ini.

## Convergence workflow

Jalankan timestep h,h/2,h/4 dengan inputs sama. Compare positions pada times sama, energy atau constraint residual sesuai model, dan actual output frames. Bila results berubah besar, jangan hanya menaikkan fps render; naikkan simulation quality atau ubah model.

Collision impulses, friction, stiff constraints dan nonlinear forces mempunyai restrictions sendiri. RK4 bukan otomatis terbaik; lebih banyak evaluations tidak menyelesaikan discontinuous contacts atau implicit stiffness secara universal.

## Production

Fix solver timestep independen output rate; cache state with config/version. Jangan retime physics dengan mengubah timestep diam-diam. Time remapping atas cache mempunyai consequence acceleration yang berbeda dari resimulating forces.

## Pemeriksaan

Known analytical cases memberi oracle sebelum complex scenes. Stability chapter ini adalah penurunan model oscillator linear; cloth/fluid tetap membutuhkan solver-specific tests. [M16](../domains/16-physical-procedural-and-secondary-motion.md).
