# Tools & Data Utilities - SpeedGuard

Folder ini berisi skrip bantu dan utilitas data yang digunakan untuk memproses, memvalidasi, dan mengonversi data riwayat pelanggaran ke dalam aplikasi SpeedGuard.

## Berkas yang Tersedia:
- **`parse_126.py`**: Skrip Python untuk mengekstrak dan mem-parsing data mentah dari 126 kasus riwayat pelanggaran kecepatan awal Puninar Nagrak.
- **`apply_126.py`**: Skrip injeksi untuk memformat dan memperbarui dataset awal ke berkas aplikasi.
- **`sync_rn_data.py`**: Skrip sinkronisasi data antar modul aplikasi.
- **`initial_data_126.js`**: Ekspor data JavaScript dari 126 catatan riwayat awal (nama, tanggal, kecepatan, area, plat, NIK, jenis kendaraan, dan status).

> **Catatan**: Seluruh 126 data riwayat awal tersebut sudah secara otomatis terintegrasi langsung di dalam `index.html` dan disimpan ke `localStorage` peramban (browser), sehingga aplikasi utama dapat langsung digunakan tanpa memerlukan eksekusi ulang skrip pada folder ini.
