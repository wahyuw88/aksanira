# Production & Purchase Assurance QA — v3.6

## A. Product-to-listing verification (wajib)
- [ ] Buka listing Mayar Financial Control dan cocokkan nama, file XLSX, PDF panduan, versi, harga, dan deskripsi.
- [ ] Buka listing Mayar Vendor Decision dan cocokkan nama, file XLSX, PDF panduan, versi, harga, dan deskripsi.
- [ ] Pastikan produk yang diterima pembeli sama dengan produk yang dijanjikan di halaman web.
- [ ] Uji transaksi sah dari awal sampai file berhasil diunduh.
- [ ] Periksa receipt, email delivery, nama file, dan instruksi penggunaan.
- [ ] Jangan aktifkan CTA pembelian Family atau bundel sebelum listing resmi diuji.

## B. Product proof
- [ ] Pastikan seluruh gambar berlabel DATA DEMO/ILUSTRASI.
- [ ] Pastikan angka dan contoh tidak disajikan sebagai testimoni atau hasil pelanggan.
- [ ] Cocokkan istilah dan nama sheet dengan workbook v1.4.
- [ ] Ambil screenshot langsung dari workbook setelah formula dihitung ulang di aplikasi target jika ingin mengganti visual demo.

## C. Purchase information
- [ ] Cantumkan isi paket dan format file sesuai listing aktual.
- [ ] Cantumkan cara menerima file berdasarkan alur delivery aktual.
- [ ] Uji Excel versi yang ditargetkan.
- [ ] Uji Google Sheets sebelum menyatakan kompatibel.
- [ ] Publikasikan kebijakan dukungan/pengembalian dana hanya jika benar-benar berlaku.

## D. Live website
- [ ] Uji desktop dan mobile di browser nyata.
- [ ] Uji seluruh CTA, navigasi, gambar, form, dan halaman 404.
- [ ] Uji Formspree hingga email benar-benar diterima.
- [ ] Verifikasi SSL dan redirect apex ke www.
- [ ] Verifikasi robots.txt, sitemap, canonical, dan indexing di Search Console.
- [ ] Jalankan Lighthouse dan perbaiki isu aksesibilitas/performa prioritas.
- [ ] Aktifkan GA4/GTM setelah ID resmi tersedia dan uji event.

## E. Release gate
Jangan menyatakan website siap transaksi sebelum A dan D selesai. Pemeriksaan statis ZIP bukan pengganti pengujian transaksi dan website live.
