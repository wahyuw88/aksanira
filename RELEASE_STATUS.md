# Status Rilis AKSANIRA v4.1

**Status: kandidat staging — belum production-ready.**

## Sudah diperiksa secara lokal
- Static QA: 67 HTML pages, 57 sitemap URLs, 0 errors, 0 warnings.
- Canonical path diperiksa terhadap clean URL; empat alias eksplisit dan halaman 404 ditangani sebagai pengecualian terdokumentasi.
- Browser QA script lolos pemeriksaan sintaks JavaScript; ini bukan hasil browser staging.
- Instruksi browser QA diseragamkan: npm install, npx playwright install chromium, dan BASE_URL=... npm run qa:browser.

## Belum diuji / Pending
- Playwright pada URL staging, navigasi/CTA live, mobile browser nyata, Firefox/Safari.
- Formspree sampai email diterima; Mayar sampai transaksi uji dan file delivery berhasil.
- SSL, redirect apex-to-www, sitemap live, Search Console.
- Lighthouse, aksesibilitas manual, GA4/GTM.

Static QA dan pemeriksaan sintaks tidak membuktikan perilaku layanan eksternal atau kelayakan produksi. Ikuti release gate di LIVE_RELEASE_RUNBOOK.md.
