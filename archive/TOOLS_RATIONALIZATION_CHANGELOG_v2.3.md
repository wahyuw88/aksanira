# AKSANIRA Web App — Tools Rationalization v2.3

## Perubahan
- Halaman tools gratis sekarang hanya menampilkan tiga alat inti yang selaras dengan tiga sistem unggulan: Financial Control, Vendor Decision, dan Family & Wedding Command Center.
- Vendor Offer Evaluator ditingkatkan menjadi Vendor Comparison Scorecard dengan skor berbobot untuk harga, kualitas, kelengkapan layanan, komunikasi, dan ketentuan.
- Wedding Readiness Check diarahkan ke Family & Wedding Command Center; copy menjelaskan keterbatasan progres numerik dan konteks koordinasi.
- Tools lama yang tumpang tindih diarahkan ke halaman relevan menggunakan redirect sisi klien dan meta refresh dengan fallback tautan.
- Budget Allocation Check dipertahankan sebagai pintu masuk Financial Control System.

## Batasan yang perlu diketahui
- Bobot scorecard vendor merupakan bobot awal yang transparan, bukan rekomendasi universal; pengguna tetap perlu menilai kesetaraan cakupan penawaran dan kontrak.
- Budget Allocation Check masih menggunakan komposisi alokasi bawaan; belum dibuat dinamis berdasarkan pilihan prioritas.
- Wedding Readiness Check masih menggunakan jumlah tugas selesai/total, belum merupakan checklist per tugas dengan PIC dan tingkat kritikalitas.
- Redirect sisi klien/meta refresh bukan pengganti redirect HTTP 301/308 di konfigurasi hosting. Jika URL lama sudah memiliki trafik/tautan, tambahkan redirect permanen di Vercel.
- Belum dilakukan pengujian browser lintas perangkat, uji end-to-end, atau deployment produksi.

## File
Paket ini dibangun dari AKSANIRA_WebApp_Editorial_Upgrade_v2.2.zip.
