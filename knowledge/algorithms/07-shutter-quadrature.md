# Shutter dan temporal quadrature

## Model

Frame image adalah weighted integration render R(t) sepanjang exposure [a,b]. Normalized box shutter I=(1/(b-a))*integral R(t)dt. Midpoint quadrature dengan K samples memperkirakan I≈sum R(a+(k+0.5)*(b-a)/K)/K. Renderer sampling stochastic memakai sample distribution berbeda.

Pada frame interval1/f, shutter angle theta memberi exposure theta/(360f) dalam angle model. Ini tidak menentukan alignment: forward [t,t+T], centered [t-T/2,t+T/2], atau trailing [t-T,t] memberi images yang berbeda di cue boundaries. Demo memakai forward shutter dan melaporkannya.

## Constant motion

Speed120px/s,30fps,180°→T1/60s→displacement2px. Empat samples memberikan posisi sub-exposure, bukan perfect continuous blur. Occlusion, changing opacity dan acceleration dapat membuat analytic uniform line blur tidak cukup.

## Endpoint dan cue

Exposure dapat melewati animation end. Scene evaluator perlu defined behavior outside action intervals. Pada final frame demo179/30, forward exposure masih sebelum6s. Centered shutter pada frame0 membutuhkan state negative time. Pilih clamp/pre-roll policy, jangan membiarkan missing state menjadi black sample.

Text moving cepat dengan exposure besar dapat sulit dibaca. Sediakan stable hold atau pilih shutter per-element jika artistic intent mengizinkan; jangan mengubah global shutter untuk memperbaiki hierarchy yang salah tanpa menilai seluruh scene.

## Pemeriksaan

Compare sample counts1,4,16 untuk convergence visual. Uji moving rectangle known speed dan edge coverage. Average linear values bila target light integration. Motion vectors hanya approximate beberapa gerak dan tidak otomatis menyelesaikan disocclusion. [M21](../domains/21-rendering-and-temporal-image-formation.md).
