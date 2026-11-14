# AKSANIRA Web App v3.2 — Production & Trust Readiness

## Status
Pembaruan paket file statis. Ini bukan bukti bahwa website telah dideploy atau layanan eksternal telah diuji.

## Perubahan v3.2
- Menyamakan nama direktori rilis menjadi `AKSANIRA_WebApp_v3.2`.
- Mengganti README utama yang usang (planner seserahan sebagai fitur utama dan klaim 100 artikel) dengan dokumentasi operasional yang konsisten dengan tiga sistem utama AKSANIRA.
- Menambahkan ringkasan positioning, hirarki produk, batasan workbook, dan urutan deployment/QA.
- Menyamakan CTA tiga halaman produk pendukung menjadi “Lihat harga & beli di Mayar”.
- Menghapus styling harga promo yang tidak lagi digunakan dari tiga halaman pendukung.
- Memperjelas copy halaman rundown agar tidak menjanjikan pengiriman file sebelum pengaturan Mayar diuji.
- Mempertahankan `noindex,follow` pada tiga halaman produk pendukung sampai screenshot aktual, konten pembelian unik, dan QA checkout tersedia. Ini keputusan sementara, bukan kebijakan SEO permanen.

## Belum dapat diterapkan tanpa akses/aset pemilik
- Screenshot aktual harus berasal dari workbook final; tidak dibuat atau direkayasa dalam paket ini.
- Harga/listing/transaksi dan pengiriman file Mayar belum diverifikasi.
- Formspree/email, GA4/GTM, consent, Search Console, SSL, redirect, dan deployment belum diuji.
- Belum ada browser QA, Lighthouse, uji aksesibilitas, atau pengujian pengguna.

## Checklist sebelum produksi
- [ ] Uji transaksi dan file delivery setiap listing Mayar yang aktif.
- [ ] Konfirmasi Family Command Center dan bundle hanya ditawarkan setelah listing resmi ada.
- [ ] Uji formulir kontak termasuk inbox, spam, validasi, dan kegagalan.
- [ ] Sediakan empat screenshot aktual per produk utama: dashboard, input, output, daftar sheet/panduan.
- [ ] Putuskan index/noindex setelah halaman memiliki konten unik dan bukti memadai; perbarui sitemap sesuai keputusan.
- [ ] Uji desktop/mobile, keyboard, focus, kontras, aksesibilitas, dan Lighthouse.
- [ ] Setelah deploy, cek canonical, sitemap, robots, clean URL, SSL, redirect apex ke www, dan 404.
- [ ] Pasang analytics hanya dengan ID resmi dan consent yang disetujui pemilik.

## Batasan
Workbook tetap manual. Tidak ada sinkronisasi otomatis, kolaborasi real-time, kalender, notifikasi, atau pemrosesan pembayaran di dalam workbook. Event instrumentation lokal bukan pengganti GA4/GTM.
