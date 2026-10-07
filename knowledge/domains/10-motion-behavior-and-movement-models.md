# M10 — Motion Behavior and Movement Models

## Manifestasi yang ditampilkan

Objek bergerak dengan character tertentu: decisive, elastic, floating, heavy-looking, mechanical, organic atau continuous. Trajectory adalah manifestation dari chosen motion model.

[Master map](../../architecture/master-map.md) · [Daftar konsep](../../architecture/concepts.json) · [Bukti dan batas verifikasi](../../evidence/README.md)

## Cakupan dan batas

Physical equations, authored easing dan perceived qualities adalah different layers. Visible motion alone does not determine mass; moving target and interruption require explicit state.

## Fondasi yang membentuk tampilan

Position/velocity/acceleration, functions, interpolation, ODEs, springs, noise, numerical integration dan constraints. Choose model by function, then inspect appearance.

## M10.01 — Kinematic quantities

Position determines where; velocity/acceleration/jerk describe changes. Angular quantities need frame/convention.

**Model / mekanisme.** v=xprime, a=vprime, jerk=aprime.

**Implementasi.** Use seconds/radians and derivatives with actual dt.

**Kegagalan tampilan.** Frame-based speeds; inaccurate noisy derivative.

**Pemeriksaan.** Analytic constant velocity/acceleration and unit audit.

## M10.02 — Interpolation

Lerp bridges values in chosen space, extrapolates outside range if allowed.

**Model / mekanisme.** x=a+(b−a)u.

**Implementasi.** Separate value interpolation and u(t) timing.

**Kegagalan tampilan.** Clamp ruins designed overshoot; angle wrap wrong.

**Pemeriksaan.** Endpoints, extrapolation and value-space checks.

## M10.03 — Easing models

Easing maps progress; Bézier x inversion required for CSS-style mapping.

**Model / mekanisme.** Solve x(s)=u, evaluate y(s).

**Implementasi.** Bisection/Newton with robust bounds; pure evaluator.

**Kegagalan tampilan.** y(u) directly used, flat tangent solver fails.

**Pemeriksaan.** Known parametric fixture and endpoint continuity.

## M10.04 — Spring dynamics

Linear spring has state x,v and parameters mass/stiffness/damping.

**Model / mekanisme.** m xdoubleprime+c xprime+k(x−r)=0; ω=√(k/m), ζ=c/(2√km).

**Implementasi.** Analytic propagation for fixed target or stated numerical solver.

**Kegagalan tampilan.** dt instability, wrong damping meaning.

**Pemeriksaan.** Step response, initial conditions and refinement.

## M10.05 — Trajectory geometry

Time law and path define different behavior. Curve shape alone does not define speed.

**Model / mekanisme.** x(t)=p(u(t)); derivative chain rule.

**Implementasi.** Arc-length mapping when distance response required.

**Kegagalan tampilan.** Uneven motion despite smooth path.

**Pemeriksaan.** Distance/time and derivatives along full path.

## M10.06 — Angular motion

Quaternion/orientation interpolation respects rotation geometry.

**Model / mekanisme.** Unit quaternion, q/−q equivalence; shortest-path hemisphere.

**Implementasi.** Slerp/normalized alternatives with convention.

**Kegagalan tampilan.** Gimbal lock, long path, norm drift.

**Pemeriksaan.** Known quarter/half rotations and equivalent quaternion tests.

## M10.07 — Constraints and bounds

Hard bounds must remain respected throughout trajectory. Soft settling may cross boundary.

**Model / mekanisme.** Limit state/target/solver depending intended semantics.

**Implementasi.** Decide contact/clamp/retarget policy explicitly.

**Kegagalan tampilan.** Snap at bound; visually goes through obstacle.

**Pemeriksaan.** High velocity, boundary targeting and residual.

## M10.08 — Retargeting continuity

New goal during motion needs current pose/velocity initialization.

**Model / mekanisme.** C0 preserves position; C1 derivative continuity under parameterization.

**Implementasi.** Snapshot state at change; bridge or spring with velocity.

**Kegagalan tampilan.** Start from old origin, stale completion.

**Pemeriksaan.** Repeated reversals and interruption trace.

## M10.09 — Organic procedural variation

Noise/oscillators add variation with scale/correlation.

**Model / mekanisme.** Signal/time-based variation, reproducible seed.

**Implementasi.** Keep core action distinct from secondary variation.

**Kegagalan tampilan.** Random perframe jitter; variation changes task meaning.

**Pemeriksaan.** Seed/rate sweeps and bounds.

## Penurunan mekanisme dan contoh terhitung

Critical spring y=x−r has solution y(t)=[y0+(v0+ωy0)t]exp(−ωt). Derivative v(t)=[v0−ω(v0+ωy0)t]exp(−ωt). With m1,k100,c20,ω10 and y0=1,v0=0, at t=.5 position6exp(−5)≈.04043. Formula assumes fixed target and constant coefficients. Moving target introduces reference derivatives; do not reuse fixed-target formula blindly. Numerical semi-implicit Euler updates v then x and must be checked against oracle at decreasing h.

## Kasus produksi

Token joins diagram. Use path to determine location, time law to determine progression, and separate small spring settle after arrival only if intended. Text labels remain stable. If direction changes mid-flight, preserve state and pick feasible bridge; high incoming velocity may require overshoot or longer settle.

## Memilih teknik dan trade-offs

Use authored easing for tightly specified duration/trajectory; spring when stateful responsiveness matters; physics when forces/contacts meaningful; procedural variation for controlled texture of motion. No model guarantees perceived premium/weight.

## Alur kerja operasional

Define function/character; choose space/model; set unit/initial state; derive duration/derivative behavior; implement pure evaluator; integrate constraints; test edge/retarget; inspect rendered sequence.

## Verifikasi dan kriteria penguasaan

Dapat explain why trajectory behaves as rendered, derive critical spring and detect numerical/timing errors. Perceived character remains reviewable hypothesis.

## Cabang spesialis dalam cakupan

Geometric integration, constrained motion, coupled oscillators, inertial response, nonuniform easing, manifold interpolation, stochastic motion and trajectory optimization.

## Hubungan antardomain

[M05](../../architecture/master-map.md#m05), [M09](../../architecture/master-map.md#m09), [M11](../../architecture/master-map.md#m11), [M12](../../architecture/master-map.md#m12), [M13](../../architecture/master-map.md#m13), [M14](../../architecture/master-map.md#m14), [M16](../../architecture/master-map.md#m16), [M20](../../architecture/master-map.md#m20), [M21](../../architecture/master-map.md#m21).

## Jalur sumber

[R06](../../evidence/sources.md#r06), [R21](../../evidence/sources.md#r21), [R22](../../evidence/sources.md#r22).

Setiap sumber memiliki scope/status sendiri. Technical synthesis dan authored design choices tidak otomatis menjadi empirical human findings. Contoh hitungan memiliki assumptions yang dinyatakan; daftar cabang spesialis bukan klaim seluruh literaturnya telah diaudit.
