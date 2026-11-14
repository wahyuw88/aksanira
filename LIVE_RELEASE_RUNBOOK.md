# AKSANIRA — Live Release Runbook (v4.1)

Dokumen ini memisahkan pemeriksaan yang dapat dilakukan dari ZIP dan pemeriksaan yang hanya dapat dinyatakan lulus setelah deployment. Tidak ada status live yang diasumsikan.

## 1. Pemeriksaan lokal sebelum upload

Dari folder root situs, jalankan:

```bash
python3 qa_static.py
```

Jika ada `ERROR`, jangan lanjutkan deployment sampai diperbaiki. Peringatan clean URL perlu diverifikasi pada konfigurasi Vercel; script tidak menganggap file slug tanpa ekstensi sebagai file rusak.

## 2. Browser smoke test otomatis (setelah staging tersedia)

Persyaratan: Node.js dan Playwright. Dari folder root situs:

```bash
npm install
npx playwright install chromium
BASE_URL="https://your-preview.vercel.app" npm run qa:browser
```

Script memetakan seluruh file HTML root ke clean URL, lalu memeriksa HTTP, title/H1, overflow, gambar lazy-load, input tanpa label, nama aksesibel tautan/tombol, tautan kosong, respons same-origin 4xx/5xx, error JavaScript/console, dan progres fokus keyboard pada desktop serta mobile Chromium. Script juga memeriksa robots.txt dan sitemap.xml. Script tidak mengirim formulir, tidak melakukan checkout, tidak menguji Firefox/Safari, dan bukan audit aksesibilitas penuh. Pemeriksaan canonical statis memvalidasi path per halaman; empat halaman alias memiliki allowlist eksplisit yang harus ditinjau jika struktur URL berubah. Simpan `browser-smoke-report.json` sebagai bukti rilis; kegagalan satu halaman tetap dicatat dan tidak menghentikan pemeriksaan halaman berikutnya.

## 3. Deployment staging

1. Buat deployment Preview/Staging di Vercel, bukan langsung mengganti production.
2. Ekstrak ZIP v4.1, lalu upload **isi folder root hasil ekstraksi** (folder yang berisi `index.html`, `vercel.json`, dan `sitemap.xml`), bukan folder ZIP induk atau folder versi lama.
3. Catat URL preview dan commit/deployment ID.
4. Jalankan pemeriksaan HTTP di bawah pada URL staging.

## 4. HTTP smoke test setelah staging tersedia

Ganti `STAGING_URL` dengan URL preview Vercel:

```bash
STAGING_URL="https://your-preview.vercel.app"
for path in / /robots.txt /sitemap.xml /produk /financial-control-system /vendor-decision-system /family-wedding-command-center /kontak /404; do
  printf '%-38s' "$path"
  curl -sS -o /dev/null -w '%{http_code} %{content_type}\n' "$STAGING_URL$path"
done
```

Kriteria: halaman penting mengembalikan 200, robots dan sitemap dapat dibaca, gambar tidak 404, halaman tidak dikenal diarahkan/ditampilkan sebagai 404 yang benar. Periksa redirect apex ke www secara terpisah setelah domain terpasang.

## 5. Mayar — uji manual wajib

URL yang ditautkan website (belum berarti listing sudah diverifikasi):

- Financial Control: https://aksanira.myr.id/catalog/wedding-budget-planner-79298
- Vendor Decision: https://aksanira.myr.id/catalog/wedding-vendor-comparison-planner

Untuk masing-masing listing, cocokkan nama produk, workbook XLSX, panduan PDF, versi 1.4, harga, deskripsi, receipt, dan file delivery. Lakukan transaksi uji yang sah sesuai mekanisme akun Mayar, lalu pastikan pembeli menerima file yang dijanjikan. Jangan mengandalkan HTTP 200 sebagai bukti checkout berhasil.

Family Command Center dan bundel tetap tanpa checkout sampai listing resminya dibuat dan diuji.

## 6. Form kontak

Kirim satu pesan uji melalui halaman Kontak. Verifikasi pesan masuk di tujuan email/Formspree, cek balasan/error yang ditampilkan di halaman, dan pastikan data tidak hilang. Jangan menandai lulus hanya karena tombol submit dapat diklik.

## 7. Browser, aksesibilitas, dan performa

- Uji Chrome/Firefox/Safari atau browser target di desktop dan ponsel.
- Uji navigasi keyboard, focus-visible, label formulir, alt gambar, kontras, zoom 200%, dan reduced motion.
- Jalankan Lighthouse pada homepage dan tiga halaman produk; catat skor serta isu nyata, jangan hanya menyimpan skor.
- Periksa gambar, font, clean URLs, 404, dan seluruh CTA.

## 8. Domain, SEO, analytics

- Pastikan SSL valid pada apex dan www.
- Verifikasi apex → www (308 sesuai konfigurasi) dan canonical www.
- Buka `/robots.txt` dan `/sitemap.xml`; daftarkan sitemap di Search Console dan periksa indexing.
- GA4/GTM hanya boleh diaktifkan setelah ID resmi diberikan. Setelah aktif, uji event CTA dan pembelian; jangan menganggap dataLayer lokal sebagai analytics aktif.

## 9. Bukti pengujian yang wajib disimpan

Gunakan `RELEASE_EVIDENCE_LOG.csv` sebagai register pengujian. Untuk setiap baris, isi tanggal, pemeriksa, hasil aktual, status, dan lokasi bukti (screenshot, output terminal, receipt, atau deployment ID). Status `PASS` hanya boleh diberikan setelah hasil benar-benar diamati; `Pending` bukan lulus.

Tambahan pemeriksaan sebelum rilis:
- Cocokkan seluruh enam kriteria Vendor Decision, bobot 100%, dan rumus risiko terbalik dengan workbook v1.4. Preview demo menampilkan Vendor A 4,35 dan Vendor B 3,55.
- Cocokkan 12 visual detail pada galeri produk serta satu preview katalog tambahan dengan lembar workbook yang disebutkan pada caption. Preview visual bukan bukti formula telah diuji di Excel atau aplikasi lain.
- Harga katalog tidak ditampilkan statis; teks katalog tidak boleh menyatakan katalog sebagai sumber harga terkini. Harga final harus diperiksa pada listing Mayar saat transaksi.
- Pastikan nama produk, versi XLSX, panduan PDF, harga, receipt, dan file delivery cocok pada kedua listing Mayar.
- `vercel.json` berisi aturan host-specific apex → www. Setelah deploy, uji status 308, path, query string, HTTPS, dan tidak ada redirect loop. Jika Vercel Dashboard memiliki redirect domain yang sama, pastikan tidak terjadi konflik.

## 10. Release gate

Rilis produksi hanya jika: (a) dua listing Mayar cocok dengan deliverable dan transaksi/delivery berhasil, bukti dicatat dalam `RELEASE_EVIDENCE_LOG.csv`, (b) formulir kontak terbukti masuk, (c) staging/browser QA lulus, (d) domain/SSL/redirect benar, dan (e) tidak ada error prioritas tinggi dari Lighthouse/aksesibilitas. Simpan tanggal, URL, bukti, dan nama pemeriksa.


## 11. Interpretasi hasil browser QA

- `browser_smoke.mjs` menguji seluruh file `.html` yang ada di root paket melalui clean URL karena `vercel.json` mengaktifkan `cleanUrls`. Jumlah halaman dapat berubah jika file HTML ditambah/dihapus; laporan mencatat jumlah aktual.
- PASS hanya berlaku untuk URL staging, waktu, versi, dan browser yang tercatat di laporan. Uji ulang setelah perubahan deployment.
- Fokus keyboard dasar dan pemeriksaan label input bukan pengganti audit WCAG. Tetap lakukan pemeriksaan manual keyboard, screen reader, kontras, zoom 200%, dan reduced motion.
- Script tidak mengklik CTA eksternal, tidak submit form, dan tidak melakukan transaksi. Validasi Mayar/Formspree tetap merupakan release gate manual.


## 12. Functional test manual dan SEO integrity

- Pada staging, buka homepage, katalog, tiga halaman sistem, dan kontak. Klik setiap navigasi internal utama dan CTA; pastikan tujuan sesuai label dan tidak ada tautan kosong. Jangan otomatis mengirim formulir atau melakukan pembayaran.
- Untuk formulir, uji validasi field wajib, email tidak valid, status loading, status sukses, dan status gagal. Setelah itu lakukan satu pengiriman uji yang disetujui dan verifikasi inbox Formspree.
- Untuk canonical, bandingkan URL canonical tiap halaman dengan clean URL yang dimaksud. Empat canonical alias yang disengaja dicatat dalam `qa_static.py`; perubahan alias harus disertai tinjauan manusia. Halaman 404 dikecualikan dari kecocokan path canonical.
- Pastikan URL sitemap dapat diakses, mengembalikan halaman yang benar, dan bukan redirect/404 yang tidak diharapkan. Cocokkan URL sitemap dengan daftar halaman indexable yang memang hendak dipublikasikan.
- Jalankan Lighthouse pada homepage dan tiga halaman produk. Catat skor dan isu, lalu audit keyboard, kontras, zoom 200%, reduced motion, dan screen reader secara manual.


## 12. Functional test manual dan SEO integrity

- Pada staging, buka homepage, katalog, tiga halaman sistem, dan kontak. Klik navigasi internal utama dan CTA; pastikan tujuan sesuai label dan tidak ada tautan kosong. Jangan otomatis mengirim formulir atau melakukan pembayaran.
- Untuk formulir, uji validasi field wajib, email tidak valid, status loading, sukses, dan gagal. Lakukan satu pengiriman uji yang disetujui dan verifikasi inbox Formspree.
- Cocokkan canonical tiap halaman dengan clean URL yang dimaksud. Empat canonical alias yang disengaja dicatat dalam qa_static.py; perubahan alias perlu tinjauan manusia. Halaman 404 dikecualikan dari kecocokan path canonical.
- Pastikan URL sitemap mengembalikan halaman yang benar, bukan redirect/404 yang tidak diharapkan. Cocokkan sitemap dengan daftar halaman indexable.
- Jalankan Lighthouse pada homepage dan tiga halaman produk. Catat skor dan isu; audit keyboard, kontras, zoom 200%, reduced motion, dan screen reader secara manual.
