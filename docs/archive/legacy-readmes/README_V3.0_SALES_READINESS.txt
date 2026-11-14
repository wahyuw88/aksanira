AKSANIRA WEB APP v3.0 — SALES READINESS & QA
================================================

Isi paket
- 64 halaman HTML dan aset website dari v2.9.
- Klasifikasi katalog: tiga sistem utama vs planner pendukung.
- FAQ pembelian dan penjelasan batasan workbook.
- Instrumentasi event konversi lokal yang siap diteruskan ke dataLayer bila GTM dipasang.

PENTING — BATASAN YANG TIDAK BOLEH DIANGGAP SUDAH SELESAI
1. Event tracking hanya memancarkan CustomEvent "aksanira:conversion" dan meneruskan event ke window.dataLayer JIKA dataLayer sudah tersedia. Tidak ada Google Analytics/GTM ID yang dibuat atau dikonfigurasi, dan tidak ada data yang dikirim sendiri.
2. Tidak ada screenshot workbook baru yang dibuat. Semua tabel contoh tetap merupakan ilustrasi dan diberi label bukan screenshot workbook. Ganti dengan screenshot aktual setelah aset asli tersedia.
3. Tidak ada checkout Mayar, Formspree, email, SSL, redirect, atau deployment yang diuji dari paket statis ini.
4. Harga website adalah nilai konten yang ditampilkan; harga akhir wajib diverifikasi di Mayar sebelum transaksi.
5. Family & Wedding Command Center dan bundel tidak diberi checkout palsu.

LANGKAH WAJIB SEBELUM PRODUKSI
[ ] Verifikasi harga dan listing Financial Control System di Mayar.
[ ] Verifikasi harga dan listing Vendor Decision System di Mayar.
[ ] Lakukan transaksi uji dan periksa email/unduhan/file yang diterima.
[ ] Kirim formulir kontak uji; periksa inbox, spam, dan skenario error.
[ ] Ganti preview ilustratif dengan screenshot aktual dari workbook final (dashboard, input, output, panduan).
[ ] Putuskan apakah Family Command Center dan bundel akan dijual sekarang atau tetap Coming Soon.
[ ] Jika memasang GTM/GA4, masukkan ID resmi milik pemilik situs, atur consent dan uji event click_checkout, click_contact, click_free_tool, submit_contact.
[ ] Deploy sebagai Vercel Preview terlebih dahulu.
[ ] Uji mobile, desktop, keyboard, kontras, Lighthouse, canonical, sitemap, SSL, dan redirect.
[ ] Setelah semua lulus, promosikan deployment produksi.

CATATAN TRACKING
Event yang dipancarkan:
- click_checkout
- click_contact
- click_free_tool
- submit_contact

Payload hanya memuat event, path halaman, dan teks tautan yang dibatasi 100 karakter. Jangan mengirim nama, email, isi pesan, atau data sensitif ke analytics.

Kebenaran status
Paket ini merupakan pembaruan file website. Paket tidak membuktikan layanan pihak ketiga, pembayaran, email, hosting, domain, maupun pengiriman produk berfungsi.
