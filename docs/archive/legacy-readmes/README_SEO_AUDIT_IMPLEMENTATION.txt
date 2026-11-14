AKSANIRA — IMPLEMENTASI SEO AUDIT
Versi: 1.0
Acuan: Aksanira SEO Audit, 8 November 2026

PAKET INI
Paket ini adalah salinan lengkap website berdasarkan ZIP sumber yang diunggah, dengan pembaruan SEO dan konten sesuai audit. Unggah isi folder ini sebagai pengganti versi website saat ini setelah membuat backup repository.

PERBAIKAN YANG DITERAPKAN
1. Routing dan status halaman
   - Menambahkan 404.html untuk halaman yang tidak ditemukan.
   - Menghapus redirect lama yang mengarahkan URL mati ke /artikel.
   - Menambahkan redirect permanen (301) untuk URL tools lama ke enam tools baru.
   - Menambahkan redirect host www ke https://aksanira.my.id.
   - Tidak menambahkan catch-all rewrite; URL yang tidak memiliki halaman atau redirect akan ditangani sebagai 404 oleh Vercel.

2. SEO enam tools gratis
   - Enam halaman tools baru: Budget Allocation Check, Wedding Readiness Check, Guest & Capacity Estimator, Vendor Offer Evaluator, Vendor Payment Calculator, dan Wedding Day Timeline Builder.
   - Setiap halaman memiliki title, meta description, canonical self-referencing, og:title, og:description, og:url, dan social image sendiri.
   - tools-gratis.html menjadi hub utama enam tools.

3. Tautan internal
   - Menghapus CTA lama ke /#app / Seserahan Planner.
   - Mengarahkan CTA tools lama ke hub tools baru.
   - Memperbaiki tautan artikel yang mengarah ke URL artikel yang tidak tersedia.
   - Mengarahkan artikel yang sebelumnya memakai checklist gratis lama ke hub tools.

4. Social previews
   - Menambahkan PNG Open Graph lokal untuk homepage, tools, dan kategori konten utama.
   - Mengganti ilustrasi artikel dokumen KUA yang sebelumnya memakai timeline-checklist.svg dengan PNG khusus.
   - Tidak lagi memakai SVG/Unsplash sebagai og:image pada halaman HTML yang diproses.

5. Trust pages
   - Memperbarui Tentang agar menjelaskan cakupan delapan planner digital dan cara penggunaan panduan.
   - Memperbaiki handler formulir Kontak: menghapus handler mailto placeholder yang konflik dan menyelaraskan field honeypot dengan script Formspree yang sudah ada.
   - Memperbarui Kebijakan Privasi dengan penjelasan tools browser, Formspree, checkout Mayar, cookies/layanan pihak ketiga, serta analitik/iklan.

6. Artikel
   - Mengubah lead, catatan konteks, checklist, dan meta description artikel agar tidak memakai blok template yang sama persis.
   - Menambahkan tiga artikel baru dalam klaster Seserahan & Hantaran:
     * Cara Menentukan Isi Seserahan Berdasarkan Kebutuhan
     * Checklist Seserahan Pernikahan untuk Pasangan yang Baru Mulai
     * Biaya Seserahan: Komponen yang Perlu Dihitung
   - Tautan terkait pada artikel disesuaikan dengan artikel yang tersedia.

7. Sitemap
   - Mengganti file sitemap.xml yang sebelumnya berisi HTML dengan XML sitemap yang valid.
   - Menggunakan canonical URL extensionless pada host non-www.
   - Memperbarui robots.txt agar menunjuk ke sitemap XML.

HAL YANG PERLU DIKONFIRMASI PEMILIK SEBELUM/SESUDAH LIVE
- Tentang: audit meminta nama orang/pengelola dan latar belakang/credentials. Data ini tidak tersedia di materi yang diberikan, jadi tidak dibuat-buat. Tambahkan nama dan profil nyata jika ingin menampilkan identitas pengelola.
- Kontak: formulir menggunakan endpoint Formspree yang sudah tercantum dalam sumber website (https://formspree.io/f/mjyyawyd). Uji pengiriman langsung setelah deployment dan pastikan endpoint tersebut milik AKSANIRA.
- Mayar: periksa kebijakan privasi Mayar dan alur transaksi aktual. Detail pemrosesan pembayaran mengikuti ketentuan Mayar dan penyedia pembayaran.
- Cookies/analytics/iklan: kode HTML yang diperiksa tidak memuat Google Analytics, Meta Pixel, atau AdSense secara langsung. Periksa dashboard Vercel dan layanan pihak ketiga untuk memastikan tidak ada integrasi lain yang aktif. Jika AdSense/pixel/analytics diaktifkan, revisi kebijakan privasi dan persetujuan cookies sesuai kebutuhan.
- Verifikasi status domain www dan apex di Vercel; konfigurasi redirect perlu diuji setelah deploy.
- Jalankan PageSpeed Insights pada homepage dan satu artikel. Audit sebelumnya belum memiliki data PageSpeed.
- Periksa JSON-LD dan robots/sitemap secara live melalui Search Console setelah deployment.

CARA DEPLOY
1. Backup repository website saat ini.
2. Ekstrak ZIP ini.
3. Salin seluruh isi folder ke root repository GitHub (sejajar index.html).
4. Commit dan push.
5. Tunggu deployment Vercel selesai.
6. Uji halaman berikut:
   - https://aksanira.my.id/
   - https://aksanira.my.id/tools-gratis
   - https://aksanira.my.id/tool-budget-check
   - https://aksanira.my.id/tool-readiness-checklist
   - https://aksanira.my.id/tool-guest-capacity
   - https://aksanira.my.id/tool-vendor-evaluator
   - https://aksanira.my.id/tool-payment-schedule
   - https://aksanira.my.id/tool-wedding-timeline
   - https://aksanira.my.id/sitemap.xml
   - https://aksanira.my.id/halaman-yang-tidak-ada (harus menampilkan 404)
7. Uji redirect 301 dari tiga URL legacy:
   - /kalkulator-budget-pernikahan
   - /guest-list-rsvp-mini
   - /vendor-comparison-mini

CATATAN
- File ini belum di-deploy ke Vercel. Tidak ada akses langsung ke GitHub/Vercel dalam proses ini.
- Konfigurasi Formspree, Mayar, domain, dan dashboard hosting belum diuji secara live.
