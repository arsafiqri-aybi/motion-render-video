# Critical spring dengan target tetap

## Persamaan

m*x''+c*x'+k*(x-target)=0. Dengan y=x-target dan omega=sqrt(k/m), critical damping c=2m*omega. Solusi y(t)=(A+B*t)exp(-omega*t). Initial conditions memberi A=y0 dan B=v0+omega*y0. Velocity=(v0-omega*B*t)exp(-omega*t).

Model ini memberi absolute-time evaluation tanpa integrasi per frame untuk target tetap. Ia dapat di-seek atau dirender acak. Parameter stiffness, damping dan mass tidak boleh dicampur dengan duration easing tanpa definisi.

## Contoh

m=1,k=100,c=20,y0=1,v0=0: omega=10 dan y=(1+10t)exp(-10t). Pada0.5s y≈0.0404277. Settling adalah kondisi error di bawah tolerance, bukan waktu ketika exponential menjadi nol. Tentukan tolerance absolut/relatif serta velocity tolerance jika ingin menghentikan residual motion.

## Target berubah

Jika target berubah pada t_a, evaluasi posisi/velocity tepat sebelum perubahan lalu jadikan initial conditions segmen baru terhadap target baru. Menyetel velocity ke0 setiap perubahan menyebabkan discontinuity. Target kontinu yang berubah arbitrer membutuhkan forcing model, piecewise analytic solution atau numerical integration.

Critical damping tidak berarti tidak mungkin melintasi target untuk semua velocity awal. Velocity awal yang cukup besar menuju target dapat mengubah sign y. Klaim “tidak overshoot” perlu assumptions initial conditions, bukan label spring saja.

## Pemeriksaan

Tes memeriksa initial values dan residual differential equation melalui finite difference velocity, sebagai jalur yang berbeda dari closed form. Tambahkan scenario target interruption jika model dipakai produksi. Visual review menilai apakah response mendukung material/identitas. [M16](../domains/16-physical-procedural-and-secondary-motion.md).
