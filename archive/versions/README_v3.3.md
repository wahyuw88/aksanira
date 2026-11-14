# AKSANIRA Web App v3.3 — Product Proof & Conversion

## Perubahan utama
- Menambahkan halaman detail khusus untuk tiga sistem utama: Financial Control System, Vendor Decision System, dan Family & Wedding Command Center.
- Konten fitur dirujuk dari panduan PDF produk v1.4; tidak menambahkan klaim integrasi, notifikasi, atau kemampuan yang tidak didukung.
- Setiap halaman memiliki alur penggunaan, batasan, dan FAQ spesifik.
- Menautkan katalog dan halaman produk lama ke halaman sistem utama.
- Menambahkan tiga URL baru ke sitemap dengan canonical domain www.
- Menyeragamkan teks CTA pada tautan checkout Mayar yang sudah tersedia menjadi “Lihat harga & beli di Mayar”.

## Batasan yang sengaja dipertahankan
- Checkout Financial Control dan Vendor Decision memakai tautan Mayar yang sudah ada.
- Family & Wedding Command Center dan bundel lengkap belum diberi tombol checkout karena listing Mayar resminya belum tersedia; CTA diarahkan ke kontak.
- Tidak membuat screenshot workbook palsu. Halaman menjelaskan fungsi berdasarkan panduan v1.4 dan belum mengklaim screenshot UI aktual.
- Workbook bersifat manual; tidak ada real-time collaboration, sinkronisasi antar-workbook, notifikasi, sinkronisasi kalender, atau pemrosesan pembayaran.

## Sebelum peluncuran
1. Ambil screenshot aktual dari workbook v1.4 untuk tiap sistem dan pasang setelah diperiksa.
2. Uji semua tautan Mayar, nominal checkout, proses pembayaran, dan pengiriman file.
3. Uji Formspree/kontak, domain, SSL, redirect apex ke www, serta canonical setelah deployment.
4. Lakukan QA browser desktop/mobile, aksesibilitas, performa, dan Search Console.
5. Putuskan apakah halaman planner pendukung perlu diindeks setelah konten unik dan bukti produknya lengkap.
6. Tambahkan GA4/GTM hanya setelah ID resmi tersedia; saat ini tidak ada ID analitik yang dikonfigurasi.

## Status
Paket statis siap untuk review dan deployment staging. File ini tidak membuktikan website sudah live, SSL/redirect berfungsi, transaksi Mayar berhasil, formulir mengirim email, atau analitik aktif.
