# AKSANIRA Web App v2.1 — Perbaikan Strategis

Paket ini adalah hasil penerapan perbaikan file-level pada web app v2.0.

## Perubahan utama
1. Katalog `/produk` kini hanya menampilkan tiga sistem unggulan: Financial Control System, Vendor Decision System, dan Family & Wedding Command Center.
2. Metadata dan isi halaman Tentang diselaraskan dengan fokus tiga sistem.
3. Halaman Financial Control System diperjelas untuk mencakup kontrol keputusan dan simulasi skenario.
4. Halaman Vendor Decision System diperkuat dengan penjelasan kriteria penilaian, audit biaya tersembunyi, dan pemeriksaan kontrak. Penjelasan menegaskan bahwa AKSANIRA tidak memverifikasi vendor atau memberi nasihat hukum.
5. Halaman Family & Wedding Command Center tidak lagi menampilkan harga usulan. CTA diarahkan ke Kontak sampai checkout Mayar resmi tersedia.
6. Canonical, Open Graph URL, sitemap, dan robots diarahkan ke `https://www.aksanira.my.id`.
7. Sitemap hanya memuat halaman HTML yang tersedia dan tidak memuat halaman yang diberi `noindex`.
8. Halaman produk lama dipertahankan untuk mengurangi risiko tautan lama menjadi 404, tetapi diberi `noindex,follow` agar tidak bersaing dengan tiga produk unggulan.

## Sebelum deploy
- Pastikan `www.aksanira.my.id` menjadi domain Production utama di Vercel dan apex diarahkan satu arah ke www. Jangan menambahkan redirect www → apex.
- Pastikan DNS apex A record dan sertifikat SSL telah valid di Vercel.
- Buat listing Mayar resmi untuk Family & Wedding Command Center sebelum mengganti CTA Kontak menjadi checkout.
- Uji checkout Mayar dari awal sampai file diterima, termasuk email pembeli dan file yang benar.
- Uji Formspree di halaman Kontak dari browser nyata.
- Uji enam tools gratis secara manual (input kosong, nol, batas maksimum, angka desimal, hasil, dan tampilan mobile).
- Periksa legalitas dan isi kebijakan privasi agar sesuai konfigurasi Formspree, Mayar, Vercel, analytics, dan cookie yang benar-benar digunakan.

## QA yang dilakukan pada paket
- Arsip ZIP dapat dibuka dan diekstrak.
- HTML utama dan sitemap diperbarui.
- Tidak ada klaim bahwa perubahan sudah dideploy atau bahwa checkout/form sudah teruji secara live.

## Batas validasi
Pemeriksaan ini bersifat statis pada file. Browser rendering, responsive behavior di perangkat nyata, pengiriman Formspree, checkout Mayar, SSL, DNS, dan deployment Vercel belum dapat diverifikasi dari paket ini.
