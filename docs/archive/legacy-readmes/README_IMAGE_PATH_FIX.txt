AKSANIRA — IMAGE PATH FIX

Penyebab:
Halaman memanggil gambar melalui /images/nama-file, sedangkan aset SVG/PNG di arsip website tersimpan di root proyek. Akibatnya browser mencari lokasi yang tidak ada.

Perbaikan:
Referensi gambar yang mengarah ke /images/ telah disesuaikan menjadi /nama-file sesuai lokasi aset yang benar di root.
Tidak ada aset gambar yang dihapus atau dipindahkan.

Penerapan:
1. Backup repository.
2. Ekstrak ZIP ini ke root repository dan timpa file yang sama.
3. Commit dan deploy.
4. Uji halaman artikel di desktop dan ponsel; periksa Network/Console bila gambar masih gagal dimuat.

Patch dibuat berdasarkan AKSANIRA_10_Artikel_FAQ_CTA_Mobile_Optimized_v1.zip.
