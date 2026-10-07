# Menambah atau memperbaiki pengetahuan

Pilih existing concept/domain bila scope cocok. Tambahkan model dengan units/assumptions, implementation yang dapat diikuti, visible failure dan verification method. Beri source status sesuai tindakan actual; jangan mengubah candidate menjadi inspected hanya karena URL ada.

Untuk runnable work, simpan configuration dan checks yang menguji expected behavior melalui oracle atau meaningful invariant. Rerun related reports bila runtime/config/output berubah. Jangan mengklaim human effectiveness hanya dari numeric/render checks.

Jalankan `python3 tools/validate_knowledge.py`; untuk runtime changes jalankan numeric tests dan actual render/media verification. Hindari duplicated chapters serta empty placeholder files. Stable concept IDs dijaga; rename paths harus update indexes/links.
