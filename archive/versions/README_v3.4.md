# AKSANIRA Web App v3.4 — Conversion & Production QA

## Isi paket
- Website statis dengan 67+ halaman HTML dan aset pendukung.
- Halaman detail tiga sistem utama: Financial Control System, Vendor Decision System, Family & Wedding Command Center.
- Pratinjau lembar kerja yang dirender dari workbook AKSANIRA v1.4. Pratinjau bukan screenshot aplikasi Excel; formula ditandai sebagai formula otomatis dan tidak memuat data pelanggan.
- `robots.txt` berada di root deployment dan merujuk sitemap canonical www.

## Produk dan checkout
- Financial Control System: `https://aksanira.myr.id/catalog/wedding-budget-planner-79298`
- Vendor Decision System: `https://aksanira.myr.id/catalog/wedding-vendor-comparison-planner`
- Planner pendukung tetap memakai listing Mayar yang tersedia pada halaman masing-masing.
- Family & Wedding Command Center belum memiliki listing checkout terverifikasi; halaman hanya mengarahkan calon pembeli ke kontak untuk menanyakan ketersediaan.
- Bundel tiga sistem belum memiliki listing checkout; jangan menambahkan tombol beli sampai listing resmi dibuat dan diuji.
- Harga, pembayaran, dan pengiriman file harus diverifikasi langsung di Mayar sebelum publikasi. Jangan menyalin harga ke website tanpa pemeriksaan berkala.

## Batasan produk
Workbook adalah file Excel manual. Tidak ada sinkronisasi antar-workbook, kolaborasi real-time, notifikasi otomatis, sinkronisasi kalender, atau pemrosesan pembayaran.

## Deployment
1. Deploy isi folder ini sebagai root proyek Vercel.
2. Pastikan `robots.txt`, `sitemap.xml`, dan `vercel.json` berada di root.
3. Verifikasi domain apex mengarah ke `www` sesuai konfigurasi Vercel; uji status HTTP, SSL, canonical, dan redirect setelah deployment.
4. Periksa sitemap dan robots di Search Console setelah domain aktif.

## Checklist QA wajib sebelum launch
- [ ] Uji setiap listing Mayar, harga, metode pembayaran, receipt, dan pengiriman file dari awal sampai selesai.
- [ ] Uji Formspree/kontak: submit, validasi, pesan sukses/gagal, dan email penerima.
- [ ] Uji desktop dan mobile pada Chrome, Safari, dan Firefox bila tersedia.
- [ ] Uji navigasi keyboard, focus state, kontras, alt image, dan heading.
- [ ] Jalankan Lighthouse/performance dan perbaiki isu prioritas tinggi.
- [ ] Uji apex → www, HTTPS, canonical, redirect lama, 404, robots, dan sitemap di domain live.
- [ ] Putuskan halaman noindex berdasarkan nilai konten; pastikan halaman noindex tidak masuk sitemap.
- [ ] Tambahkan GA4/GTM hanya setelah ID resmi diberikan; lalu uji event CTA dan pembelian.

## Status yang diketahui
Paket ini telah diperbarui dan diperiksa secara statis. Tidak ada klaim bahwa website sudah live, SSL/redirect sudah aktif, transaksi Mayar berhasil, Formspree mengirim email, atau GA4/GTM aktif. Browser QA, Lighthouse, dan Search Console masih harus dilakukan setelah deployment.
