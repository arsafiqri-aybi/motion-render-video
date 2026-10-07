# M12 — Channel ownership, sequence dan konflik

## Channel ownership

Tiap animated property memiliki owner atau composition rule. Jika clipA dan clipB menulis position bersamaan, hasil last-writer bergantung execution order. Itu sering bug, bukan choreography. Tetapkan replace, additive, weighted blend atau explicit handoff.

Additive translation mempunyai makna jelas dalam frame yang sama: x=base+deltaA+deltaB. Rotation composition noncommutative; opacity additive dapat keluar range. Scale multiplicative berbeda dari additive differences. Blend rules ditentukan per property/space, bukan satu function untuk semua tracks.

## Dependency

NodeA completion mengizinkanB start; event cueC menandai audio/visual accent. Dependency graph membantu scheduling tetapi edge belum menetapkan duration. CycleA-afterB-afterA tanpa trigger awal tidak mempunyai schedule valid. Parallel tracks dapat share milestone dengan role berbeda.

Contoh three-unit reveal: local duration0.4s, stagger0.1s→last completion0.6s. Reading hold0.8s dimulai setelah0.6, exit earliest1.4s. Jika exit dimulai dari first-unit completion0.4, last unit kehilangan sebagian hold. Arithmetic tidak memberi universal reading sufficiency; hold adalah contract yang perlu review.

## Interruption

Pada t_interrupt evaluasi position/velocity dan track status. Pilih finish-to-end, cancel-to-current, blend-to-new-target atau reverse; semuanya mempunyai consequences. Jangan cancel timeline tetapi membiarkan audio effect tail atau particles dari state lama tanpa policy.

## Verification

List writes per property over time, detect overlapping replace owners, validate dependency cycles dan endpoint states. Review actual sequence untuk handoff/speed/meaning. Unit checks timing saja tidak menguji layer visual order. Cue sheet menjadi single source untuk sound/visual; graph memisahkan prerequisites dari temporal edges agar pembaca tidak menganggap semua concepts wajib dieksekusi sequential.

## Hubungan dan status

Konsep: M12.01, M12.02, M12.05, M12.08. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
