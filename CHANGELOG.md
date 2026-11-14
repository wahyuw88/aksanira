# Changelog AKSANIRA Web App

## v3.7 — Staging & Release Assurance
- Menambahkan `qa_static.py` untuk memeriksa metadata HTML, alt gambar, sitemap, robots.txt, dan referensi gambar lokal.
- Menambahkan `LIVE_RELEASE_RUNBOOK.md` dengan prosedur staging, HTTP smoke test, verifikasi Mayar, Formspree, browser, domain, SEO, dan analytics.
- Menambahkan `RELEASE_STATUS.md` untuk membedakan pekerjaan dalam paket dengan verifikasi yang membutuhkan deployment.
- Mengubah label CTA produk berbayar menjadi “Lihat listing di Mayar” sampai isi listing dan transaksi diverifikasi.
- Menghapus pengulangan status ketersediaan pada halaman Family Command Center.
- Mempertahankan tiga sistem utama dan batasan workbook manual; tidak menambah SKU atau checkout yang belum tersedia.

## Batas validasi
Tidak ada transaksi Mayar, pengiriman email, deployment Vercel, SSL, redirect live, browser QA, Lighthouse, Search Console, atau analytics yang dinyatakan lulus oleh perubahan ini.


## v3.8 — Accuracy & Release Validation
- Corrected Vendor Decision scorecard preview to show all six workbook criteria and a reconciled 100% weighting.
- Recalculated illustrative scores: Vendor A 4.35/5; Vendor B 3.55/5.
- Removed static catalogue prices; Mayar listing remains the source of final checkout price.
- Expanded static QA and added a structured release evidence log.
- Clarified that apex-to-www redirect still requires domain-level verification.
- Reconciled cross-preview Financial Control demo values (budget Rp85m, actual Rp32.5m, commitments Rp28m) and documented all 15 preview assets.


## v3.9 — Automated QA & Documentation Consistency
- Expanded static QA to check canonical host, duplicate IDs, local fragments, empty image alt text, external target blank rel attributes, robots sitemap directive, and Vercel apex-to-www rule.
- Fixed stale catalogue copy that implied the catalogue itself was the current price source.
- Recorded the actually executed local static QA result in the release evidence register.
- Clarified preview inventory: 12 detailed product visuals, one additional catalogue preview, and three unused cover assets.
- Added a Playwright browser smoke-test script for staging desktop/mobile layout, HTTP status, broken images, H1, and JavaScript errors.
- No live checkout, email, deployment, DNS, SSL, Lighthouse, or analytics result is claimed.


## v4.0 — Release Assurance
- Memperbaiki runbook deployment yang sebelumnya masih menyebut folder v3.8; instruksi kini menggunakan isi folder root hasil ekstraksi paket.
- Mengoreksi inventaris preview: 12 visual detail (4 per sistem), 1 preview katalog, 3 cover tambahan, total 16 PNG non-OG.
- Memperluas Playwright smoke test dari 7 halaman terpilih menjadi seluruh file HTML root melalui clean URL; laporan JSON mencatat hasil per route dan melanjutkan setelah kegagalan.
- Menambah pemeriksaan browser desktop/mobile untuk title, H1, overflow, gambar, input tanpa label, tautan kosong, respons same-origin gagal, error JavaScript/console, dan fokus keyboard dasar.
- Menambahkan `package.json` dan perintah `npm run qa:browser`.
- Memperbarui register bukti: static QA lokal PASS; browser QA staging, transaksi, formulir, domain, SSL, dan Lighthouse tetap Pending.


## v4.1 — Functional & SEO Assurance
- Browser smoke test ditingkatkan: lazy-load image check, pemeriksaan nama aksesibel tombol/tautan, input, title/H1 pada desktop dan mobile, serta delapan langkah fokus keyboard.
- Static QA kini memeriksa kecocokan path canonical dengan clean URL halaman, dengan empat canonical alias yang ditinjau secara eksplisit dan pengecualian halaman 404.
- Menambahkan perintah `qa:static`; menyatukan instruksi browser QA ke `npm ci` dan `npm run qa:browser`.
- Runbook menambah checklist functional test, validasi formulir, sitemap, canonical, Lighthouse, dan audit aksesibilitas manual.
- Pengujian browser staging, formulir, transaksi, domain, dan Lighthouse tetap Pending sampai ada URL staging serta akses layanan terkait.


## v4.1 — Functional & SEO Assurance
- Browser smoke test ditingkatkan: lazy-load image, nama aksesibel tombol/tautan, input, title/H1 desktop dan mobile, serta delapan langkah fokus keyboard.
- Static QA memeriksa path canonical per halaman, dengan empat alias yang ditinjau eksplisit dan pengecualian halaman 404.
- Menambahkan perintah qa:static dan menyeragamkan browser QA melalui npm ci dan npm run qa:browser.
- Runbook menambah checklist functional test, formulir, sitemap, canonical, Lighthouse, dan aksesibilitas manual.
- Browser staging, formulir, transaksi, domain, dan Lighthouse tetap Pending.
