# M22 — Mengikat inputs, outputs dan laporan

## Evidence identity

Report harus menjelaskan input config, relevant code dependencies, tools/runtime, output hash, methods dan observed results. Hash output mengikat report ke file, tetapi tidak menjelaskan apakah method memeriksa property yang tepat. Simpan keduanya.

## Two independent examples

Demo2D6s30 fps mempunyai audio dan flatgraphic motion; demo 3D4s24 fps intentionally silent. Jangan memakai one-size checker yang memaksa audio pada silent contract atau menganggap3D output sama dengan2D expected frame count. Config masing-masing menyatakan expected dimensions, clock, streams dan scope.

## Validation order

Resolve dependencies→render→encode→probe/decode→property checks→sample visual review→link/index/report integrity→publish. Property failures diperbaiki pada mechanism relevan; jangan menaikkan tolerance setelah melihat failure hanya agarPASS. Missing shader runtime tetap explicit limitation, bukan forcedpass.

## Freshness

Jika renderer dependency berubah, reports/output perlu rerun sesuai effect. Mengubah doc saja tidak selalu perlu rerender; internal links/indexes perlu revalidate. Input changes yang mengubah semantic contract memerlukan visual/message review walau binary mungkin tidak berubah. Report dari code lama tetap dapat valid untuk historical output yang sama, tetapi tidak untuk newrun code tanpa matching inputs.

## Repo operations

Knowledge files stableIDs serta typed graph links membantu navigation. Source registry membatasi statusinspected/candidate; latestURL dapat berubah. Commit atomic dengan expectedhead menghindari silentoverwriteconcurrentchanges; filehashverification sesudahpublish menguji persistence actual.

## Acceptance

Numeric tests, full media decode, content samples serta human evaluation merupakan gates berbeda. Build ini menyimpan actual 24 numeric tests dan dua media outputs, dengan scope terpisah. Tidak menyatakan semua198concepts atau semua specialistbranches telah dieksekusi hanya karena test suite green.

## Hubungan dan status

Konsep: M22.01, M22.03, M22.04, M22.07, M22.09. [Master map](../../architecture/master-map.md), [bukti](../../evidence/README.md). Status penjelasan: AUTHORED. Hanya metode yang ditautkan dalam coverage record mendapatkan status EXECUTED_SCOPED; tidak ada blanket PASS seluruh induk.
