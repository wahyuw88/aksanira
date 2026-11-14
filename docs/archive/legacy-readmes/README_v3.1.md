# AKSANIRA Web App v3.1 — Price Consistency & Product Proof Upgrade

## Status paket
Paket ini adalah pembaruan file website statis berbasis v3.0. Paket belum membuktikan website sudah dideploy, checkout berjalan, formulir terkirim, domain/SSL/redirect aktif, atau analytics menerima data.

## Perubahan v3.1
- Menghapus klaim harga coret, harga promo, dan persentase hemat yang belum diverifikasi pada Guest List RSVP dan Checklist & Timeline Planner.
- Menghapus label harga uji awal Rp29.000 pada Wedding Day Rundown Planner. Harga dan ketersediaan diarahkan ke checkout Mayar agar tidak menampilkan nominal yang belum dikonfirmasi.
- Menandai Guest List, Checklist & Timeline, dan Day Rundown sebagai produk pendukung/operasional, bukan pengganti tiga sistem utama.
- Mempertahankan tautan checkout Mayar yang sudah tercantum; tautan tersebut belum diuji end-to-end.
- Mempertahankan preview tabel ilustratif yang sudah diberi label jelas sebagai ilustrasi, bukan screenshot workbook. Tidak ada screenshot palsu atau aset bukti yang direkayasa.
- Mempertahankan event instrumentation lokal dari v3.0; tidak menambahkan ID GA4/GTM.

## Hierarki produk yang harus konsisten
**Tiga produk utama:** Financial Control System, Vendor Decision System, Family & Wedding Command Center.

**Produk pendukung:** planner dan tools operasional spesifik seperti daftar tamu, checklist/timeline, dan rundown hari-H. Produk pendukung membantu aktivitas tertentu, tetapi bukan SKU hero baru.

**Bundle:** AKSANIRA Complete Wedding Planning System. Data antar-workbook tetap dipindahkan manual; tidak ada integrasi otomatis. Checkout Family Command Center dan bundle jangan ditambahkan sebelum listing resmi benar-benar dibuat.

## Aset bukti produk yang masih dibutuhkan pemilik
Ganti/tingkatkan preview ilustratif hanya setelah menyediakan screenshot aktual dari workbook final. Untuk masing-masing dari tiga produk utama, siapkan:
1. Screenshot dashboard/overview.
2. Screenshot sheet input utama dengan data contoh yang sudah dianonimkan.
3. Screenshot output/hasil perhitungan atau ringkasan.
4. Screenshot daftar sheet atau panduan penggunaan PDF.

Jangan gunakan data pelanggan, kontak, nomor rekening, atau informasi pribadi pada screenshot. Beri label jika contoh data dibuat untuk demonstrasi.

## Daftar pemeriksaan sebelum produksi
- [ ] Verifikasi nominal, nama listing, deskripsi, dan file yang dikirim untuk setiap tautan Mayar.
- [ ] Lakukan transaksi uji untuk Financial Control System, Vendor Decision System, serta produk pendukung yang masih dijual; periksa email dan file yang diterima.
- [ ] Pastikan listing Family Command Center dan bundle tersedia sebelum menampilkan CTA beli. Jika belum, tetap Coming Soon/kontak.
- [ ] Kirim formulir kontak uji; periksa inbox, spam, validasi, pesan sukses, dan skenario gagal.
- [ ] Sediakan screenshot aktual untuk tiga sistem utama dan ganti preview ilustratif secara bertahap.
- [ ] Jika memasang GTM/GA4, gunakan ID resmi pemilik situs, atur consent, dan uji event `click_checkout`, `click_contact`, `click_free_tool`, `submit_contact`.
- [ ] Uji desktop dan mobile pada browser utama, keyboard/focus, kontras, aksesibilitas, dan Lighthouse.
- [ ] Setelah deploy, periksa canonical, sitemap, robots, clean URL, SSL, redirect apex ke www, serta halaman 404.

## Batasan analytics
Script hanya memancarkan `CustomEvent` bernama `aksanira:conversion` dan meneruskan payload ke `window.dataLayer` bila GTM/dataLayer sudah tersedia. Script tidak mengirim data ke pihak ketiga dengan sendirinya dan bukan pengganti konfigurasi GA4/GTM. Payload berisi nama event, path halaman, dan teks tautan yang dibatasi 100 karakter. Jangan memasukkan nama, email, isi pesan, atau data sensitif ke analytics.

## Batasan produk
Workbook adalah file Excel yang dikelola manual. Tidak ada kolaborasi real-time, sinkronisasi otomatis antar-workbook, sinkronisasi kalender, notifikasi, atau pemrosesan pembayaran di dalam workbook. Pembayaran dan distribusi file mengikuti penyedia checkout yang digunakan.
