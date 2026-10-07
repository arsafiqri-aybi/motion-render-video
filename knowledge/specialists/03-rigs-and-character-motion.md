# Rigs, skeletal motion dan expressive deformation

## Manifestasi

Karakter membawa pose, gesture, weight, contact, gaze dan facial cues. Motion identity terbentuk dari timing, silhouette dan coordination; bukan hanya joint angles yang valid.

## Representations

Skeleton mempunyai hierarchy dan bind pose. FK memetakan joint transforms ke world pose; IK mencari joint parameters yang mendekati target/constraints. IK dapat memiliki banyak solusi atau tidak ada; pilih preferred pose serta limits sesuai character. Skin weights menghubungkan mesh dengan bones; weights normalized tidak otomatis menghindari volume loss.

Blend shapes memberi deformation targets; pose-space corrective dapat memperbaiki sendi tertentu. Rotation interpolation harus menjaga intended path. Root motion berbeda dari local pose tracks; combining clips dapat membuat foot sliding jika world displacement tidak sesuai contact phase.

## Motion design

Mulai key poses dan silhouette; tentukan anticipation, action, follow-through serta holds. Jangan menambahkan overlap yang membuat gesture semantik terlambat. Untuk hand contact, gunakan explicit target/constraint interval dan transition yang kontinu. Facial timing serta speech cues dapat membutuhkan data/audio analysis tetapi viseme mapping bukan full expression model.

## Test plan

Extreme poses, skin weight sums, bind reconstruction, contact intervals dan trajectory comparisons. Review feet/hands, shoulder volume, gaze and silhouette in rendered sequence. Cek rest pose normal/tangent transforms. Retargeting antar proportions memerlukan adaptation; copying joint angles tidak menjaga world contacts.

## Batas

Ini authored specialist guide, tidak ada rig scene dieksekusi. [R25/R26](../../evidence/sources.md#r26) masih candidate implementation routes. Domain M10/M12/M13/M16/M20.
