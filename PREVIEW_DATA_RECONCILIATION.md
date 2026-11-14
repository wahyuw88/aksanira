# Preview Data Reconciliation — v4.0

Dokumen ini memisahkan aset visual yang benar-benar ditampilkan pada halaman dari aset cover tambahan. Pemeriksaan visual dan aritmetika yang tampak bukan pengujian ulang seluruh formula workbook di Excel/LibreOffice.

## Inventaris aset PNG non-OG

Folder berisi **16 PNG non-OG** dengan pembagian berikut:

### 12 visual detail yang digunakan pada halaman sistem

- **Financial Control System (4):** `financial-control-budget.png`, `financial-control-contracts.png`, `financial-control-scenarios.png`, `financial-control-summary.png`.
- **Vendor Decision System (4):** `vendor-decision-audit.png`, `vendor-decision-comparison.png`, `vendor-decision-dashboard.png`, `vendor-decision-scorecard.png`.
- **Family & Wedding Command Center (4):** `family-command-dashboard.png`, `family-command-decisions.png`, `family-command-risks.png`, `family-command-tasks.png`.

### 1 preview katalog yang digunakan

- `wedding-budget-planner-preview.png` — digunakan pada halaman katalog `produk.html`.

### 3 cover tambahan yang tersedia tetapi tidak direferensikan langsung oleh HTML

- `financial-control-preview.png`
- `vendor-decision-preview.png`
- `family-command-center-preview.png`

**Rekonsiliasi jumlah:** 12 visual detail + 1 preview katalog + 3 cover tambahan = **16 PNG non-OG**. Dari total tersebut, 13 direferensikan oleh HTML dan 3 merupakan aset cover tambahan.

## Konsistensi lintas preview Financial Control

Data ilustrasi menggunakan satu set angka utama:

- Anggaran: Rp85.000.000.
- Realisasi: Rp32.500.000.
- Komitmen/sisa termin: Rp28.000.000.
- Sisa setelah realisasi dan komitmen: Rp24.500.000.
- Dana cadangan: dicatat terpisah dalam Ringkasan Keuangan.

Rekonsiliasi:

- `financial-control-budget.png`: estimasi Rp25 jt + Rp22 jt + Rp10 jt + Rp15 jt + Rp13 jt = Rp85 jt; realisasi Rp18 jt + Rp8 jt + Rp0 + Rp4 jt + Rp2,5 jt = Rp32,5 jt.
- `financial-control-contracts.png`: nilai kontrak Rp18 jt + Rp22 jt + Rp8 jt = Rp48 jt; dibayar Rp20 jt; sisa termin Rp28 jt.
- `financial-control-summary.png`: Rp85 jt − Rp32,5 jt − Rp28 jt = Rp24,5 jt.

## Vendor Decision scorecard

Workbook v1.4 memakai enam kriteria dan bobot: 15%, 20%, 20%, 15%, 15%, 15% (total 100%). Risiko biaya tambahan dibalik dengan `(6 − skor risiko)`.

- Vendor A: skor 5, 4, 5, 4, 4, risiko 2 → 4,35/5.
- Vendor B: skor 4, 4, 4, 3, 4, risiko 4 → 3,55/5.

Semua visual adalah ilustrasi/preview struktur workbook. Bukan data pelanggan, screenshot aplikasi Excel, bukti formula tervalidasi penuh, atau rekomendasi vendor.
