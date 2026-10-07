# M17 — Fields, effects dan frequency control

## Field-based appearance

Scalar field dapat mengatur density, distance, opacity atau color parameter. Vector field dapat mengatur flow/displacement. Units serta coordinate spaces wajib jelas: pixel offset, normalizedUV dan world meters menghasilkan appearance berbeda saat resize.

## Circle distance example

F(x,y)=sqrt(x²+y²)-r adalah exact signed distance circle dengan boundaryF0. Band widthw memberi approximate coverage transition di sekitar boundary; width harus terkait footprint output. Setelah nonuniform scale, field hasil transform bukan otomatis Euclidean distance di output space. Memakai value lama untuk stroke thickness dapat membuat stroke tidak rata.

## Temporal frequency

Oscillatorx=A*sin(2*pi*f*t) mempunyai speed max2*pi*f*A dan acceleration max(2*pi*f)²*A. A10px,f2Hz→speed≈125.66px/s,acceleration≈1579.14px/s². Frequency changes dapat lebih drastis daripada amplitude changes. Samplingfps tidak mengubah equation; temporal aliasing masih harus diperiksa.

## Trails

Decayexp(-lambda*dt) mempunyai half-life ln2/lambda seconds. History buffer di cut perlu clear/replace policy agar ghost scene lama tidak masuk shot baru. Premultiplied alpha/color convention tetap berlaku saat accumulating trails.

## Stack order

Displacement→blur tidak identik dengan blur→displacement. Threshold→glow dapat berbeda dari glow→threshold. Capture intermediates untuk mengetahui operator mana yang menciptakan clipping/halos. Semantic controls seperti trail half-life atau halo radius lebih reproducible daripada strength tanpa unit.

## Verification

Use checker/grid/impulse tests dan sample-rate/resolution sweep. Compare intentional texture variation dengan random render noise. Demo tidak mengeksekusi procedural fluid/shader effects; explanations bersifat authored models dengan checks yang disebut, tanpa promosi menjadi GPU execution.

## Hubungan dan status

Konsep: M17.01, M17.02, M17.04, M17.09. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
