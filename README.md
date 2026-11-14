# AKSANIRA Web App v4.1 — Release Assurance

## Status
Kandidat staging. Paket ini belum dinyatakan live, production-ready, atau siap transaksi sebelum release gate selesai.

## Produk
Tiga sistem utama: Financial Control System, Vendor Decision System, dan Family & Wedding Command Center. Produk pendukung tetap terpisah. Tidak ada SKU baru.

## Bukti produk
Halaman produk memakai 12 visual detail demo (empat per sistem). Katalog memakai satu preview tambahan. Folder juga menyimpan tiga aset cover tambahan yang belum direferensikan oleh HTML. Total: 16 PNG non-OG, 13 direferensikan oleh halaman HTML. Rincian nama file tersedia di `PREVIEW_DATA_RECONCILIATION.md`. Data, nominal, nama, skor, PIC, dan tanggal pada visual bersifat ilustratif, bukan data pelanggan, bukan hasil transaksi, dan bukan bukti pengujian formula lintas aplikasi.

## Checkout
- Financial Control System → https://aksanira.myr.id/catalog/wedding-budget-planner-79298
- Vendor Decision System → https://aksanira.myr.id/catalog/wedding-vendor-comparison-planner
- Family Command Center → belum ada listing checkout terverifikasi.
- Bundel → belum ada listing checkout terverifikasi.

URL di atas adalah tautan yang dipakai situs, bukan pernyataan bahwa nama, isi, harga, delivery, atau transaksi listing sudah diverifikasi. Cocokkan workbook XLSX, panduan PDF, versi, harga, receipt, dan file yang diterima pembeli.

## Batasan
Workbook merupakan file manual. Tidak ada sinkronisasi real-time, kolaborasi otomatis, kalender, notifikasi, atau pemrosesan pembayaran. Kompatibilitas formula di luar aplikasi Excel target belum dijamin.

## Prosedur
1. Jalankan `python3 qa_static.py` atau `npm run qa:static`.
2. Untuk browser QA staging, jalankan `npm install` lalu `npx playwright install chromium`; setelah staging tersedia jalankan `BASE_URL=https://URL-STAGING npm run qa:browser`. Script memeriksa semua file HTML root melalui clean URL pada desktop/mobile Chromium, termasuk gambar lazy-load, nama aksesibel kontrol, fokus keyboard bertahap, dan menghasilkan `browser-smoke-report.json`. Pemeriksaan browser belum dijalankan sampai URL staging tersedia.
3. Ikuti `LIVE_RELEASE_RUNBOOK.md` pada deployment staging.
4. Periksa `RELEASE_STATUS.md` sebelum memberi status rilis.

## Deployment
Ekstrak ZIP v4.1 dan upload isi folder root hasil ekstraksi (folder yang berisi `index.html`, `vercel.json`, dan `sitemap.xml`) ke Vercel. Verifikasi www, redirect apex, SSL, robots.txt, sitemap, clean URLs, 404, semua gambar, dan formulir setelah deployment. Jangan menganggap pemeriksaan ZIP sebagai live test.


## Pembaruan v3.8 — Accuracy & Release Validation
- Memperbaiki preview Scorecard Vendor: enam kriteria, bobot 100%, dan contoh skor yang dapat direkonsiliasi dengan formula workbook v1.4 (Vendor A 4,35; Vendor B 3,55). Risiko biaya tambahan dibalik dengan rumus (6 − skor risiko).
- Menghapus angka harga statis dari katalog; calon pembeli diarahkan memeriksa harga final pada listing Mayar agar katalog tidak menjadi sumber harga yang usang.
- Memperluas QA statis untuk tautan lokal, canonical, noindex/sitemap, aset gambar, dan URL checkout yang diharapkan.
- Menambahkan template release evidence log dan checklist konsistensi harga, listing, versi, serta file delivery.
- Aturan redirect apex → www dicatat sebagai pemeriksaan dashboard/domain; tidak diklaim selesai hanya dari konfigurasi file.

- `PREVIEW_DATA_RECONCILIATION.md` mendokumentasikan rekonsiliasi angka demo pada preview Financial Control dan Vendor Decision.


## Pembaruan v3.9 — Automated QA & Documentation Consistency
- Static QA kini memeriksa canonical host, alt kosong, ID duplikat, fragment lokal, rel keamanan tautan eksternal, URL sitemap, robots Sitemap directive, dan aturan apex-to-www.
- Pernyataan katalog yang sebelumnya menyiratkan katalog adalah sumber harga saat ini telah diperbaiki; harga final tetap mengacu listing Mayar.
- Register bukti mencatat STATIC-01 PASS berdasarkan eksekusi lokal aktual pada 2026-11-12. Pemeriksaan eksternal tetap Pending.
- Inventaris preview diperjelas: 12 visual detail, satu preview katalog tambahan, dan tiga aset cover yang belum dipakai.
- Ditambahkan `browser_smoke.mjs` untuk uji staging desktop/mobile, HTTP, gambar, H1, dan error JavaScript menggunakan Playwright.


## Pembaruan v4.0 — Release Assurance
- Runbook diperbaiki agar tidak mengarahkan deployment ke folder versi lama.
- Inventaris visual dipisahkan menjadi 12 detail, 1 katalog, dan 3 cover tambahan.
- Browser QA diperluas ke semua file HTML root melalui clean URL dengan laporan JSON, pemeriksaan desktop/mobile, error resource same-origin, label input, tautan kosong, dan fokus keyboard dasar.
- Static QA lokal tetap terpisah dari browser QA staging dan pengujian transaksi live.
