AKSANIRA — MAYAR CHECKOUT INTEGRATION PATCH v1

File yang diperbarui:
- produk.html
- wedding-budget-planner.html
- wedding-checklist-timeline-planner.html
- wedding-guest-list-rsvp-planner.html
- wedding-vendor-comparison-planner.html
- wedding-day-rundown-planner.html

Perubahan:
1. Tombol pembelian di halaman detail diarahkan ke tautan checkout Mayar yang diberikan.
2. Katalog produk menampilkan harga jual, harga coret, badge hemat, dan tombol checkout langsung.
3. Catatan lama yang menyatakan checkout belum aktif diperbarui pada bagian yang ditargetkan.
4. Tombol checkout membuka tab baru dengan rel=noopener noreferrer.

Cara menerapkan:
1. Backup repository website saat ini.
2. Ekstrak ZIP patch.
3. Salin keenam file HTML ke root website, timpa file dengan nama yang sama.
4. Commit dan deploy ke Vercel.
5. Uji semua lima tombol dari katalog dan halaman detail, pada desktop dan ponsel.

Penting:
- Tautan checkout disalin persis dari informasi yang diberikan pemilik.
- Patch ini tidak mengubah pengaturan Mayar, metode pembayaran, atau mekanisme pengiriman file.
- Pastikan harga dan diskon di Mayar memang sama dengan yang ditampilkan website sebelum deploy.
- Patch tidak melakukan deploy otomatis.
