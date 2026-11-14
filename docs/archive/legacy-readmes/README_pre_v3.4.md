# AKSANIRA Web App v3.2 — Production & Trust Readiness

## Identitas rilis
Paket website statis multi-halaman untuk AKSANIRA. Versi ini memperjelas tiga sistem utama, produk pendukung, bukti produk, dan batas kesiapan operasional.

## Positioning dan hirarki produk
**Wedding Planning System for Indonesian Couples.**

Tiga produk utama:
1. Financial Control System — anggaran, realisasi, kewajiban pembayaran, dan simulasi skenario.
2. Vendor Decision System — scorecard berbobot, audit biaya tersembunyi, dan pemeriksaan kontrak.
3. Family & Wedding Command Center — pembagian peran/PIC, matriks keputusan, notulen, dan eskalasi.

Produk seperti Guest List & RSVP, Checklist & Timeline, dan Wedding Day Rundown adalah produk pendukung untuk kebutuhan operasional spesifik, bukan pengganti sistem utama. Bundle lengkap belum memiliki checkout mandiri sampai listing resmi tersedia.

## Struktur proyek
- `index.html` — beranda.
- `produk.html` — katalog dan hirarki produk.
- `kontak.html` — kanal kontak.
- `*.html` — halaman produk, tools, dan artikel.
- `assets/` — aset statis jika tersedia.
- `sitemap.xml`, `robots.txt` — petunjuk perayapan mesin pencari.
- `README.md` — dokumen operasional rilis ini.
- `README_v3.2.md` — ringkasan perubahan dan checklist pra-produksi.

## Menjalankan secara lokal
Buka `index.html` untuk pemeriksaan sederhana, atau jalankan server statis dari direktori ini agar perilaku clean URL dan path relatif dapat diuji.

## Batasan yang wajib dipahami
- Workbook dijalankan secara manual; tidak ada sinkronisasi otomatis antar-workbook, kolaborasi real-time, sinkronisasi kalender, notifikasi, atau pemrosesan pembayaran di workbook.
- Tautan Mayar yang tertanam belum berarti checkout, harga, dan pengiriman file sudah diuji.
- Formulir kontak, analytics, SSL, redirect domain, dan deployment harus diuji pada lingkungan produksi.
- Preview ilustratif bukan screenshot workbook aktual. Jangan menyebutnya bukti produk atau screenshot asli.
- Jangan menampilkan checkout untuk Family Command Center atau bundle sebelum listing resminya tersedia.

## Urutan rilis yang disarankan
1. Validasi harga, listing, file digital, dan transaksi uji Mayar.
2. Uji formulir kontak sampai email diterima; cek spam dan skenario gagal.
3. Ambil screenshot aktual dari workbook final dan panduan PDF, dengan data demonstrasi anonim.
4. Lakukan QA desktop/mobile, keyboard, kontras, aksesibilitas, dan Lighthouse.
5. Setelah deploy, periksa canonical, sitemap, robots, clean URL, SSL, redirect apex ke www, dan 404.
6. Pasang GA4/GTM hanya dengan ID resmi pemilik situs dan konfigurasi consent yang sesuai.
