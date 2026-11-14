# AKSANIRA Web App v3.0 — Sales Readiness & QA

## Diterapkan
- Menegaskan hierarki katalog: tiga sistem unggulan dan planner pendukung.
- Menambahkan FAQ pembelian, keterbatasan workbook manual, ketersediaan checkout, dan arahan verifikasi harga di checkout.
- Memperjelas label pratinjau tabel sebagai ilustrasi, bukan screenshot workbook aktual.
- Menambahkan instrumentasi event lokal untuk klik checkout, kontak, tools gratis, dan submit formulir.
- Instrumentasi meneruskan event ke `dataLayer` hanya jika tersedia; tidak menanam ID GA4/GTM atau mengirim data sendiri.
- Memperjelas peringatan agar pengguna tidak mengirimkan informasi sensitif melalui formulir kontak.
- Menambahkan checklist wajib sebelum produksi.

## Belum dapat diselesaikan tanpa akses/bahan pemilik
- Screenshot workbook aktual.
- Verifikasi listing, harga, transaksi, dan pengiriman Mayar.
- Verifikasi inbox dan endpoint Formspree.
- GTM/GA4 ID dan konfigurasi consent.
- Pengujian deployment, SSL, redirect, browser, Lighthouse, dan aksesibilitas.

## Prinsip
Tidak membuat checkout, testimoni, screenshot, analytics ID, atau klaim operasional yang belum diverifikasi.
