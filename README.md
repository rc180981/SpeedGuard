# 🚨 SpeedGuard – Sistem Monitoring Pelanggaran Kecepatan

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PWA Ready](https://img.shields.io/badge/PWA-Ready-orange.svg)](manifest.json)
[![Pure Vanilla JS](https://img.shields.io/badge/Vanilla-JS-F7DF1E.svg?logo=javascript&logoColor=black)](index.html)
[![Chart.js v4](https://img.shields.io/badge/Chart.js-v4.4.2-FF6384.svg?logo=chartdotjs&logoColor=white)](chart.umd.min.js)

**SpeedGuard** adalah aplikasi web monitoring, perekaman, dan pelaporan pelanggaran batas kecepatan kendaraan (> 20 KM/JAM) untuk area operasional logistik **PT Puninar Jaya – Area Puninar Nagrak**.

Aplikasi ini dibangun menggunakan arsitektur **Zero-Dependency Backend / Client-Side Architecture** dengan penyimpanan lokal (*LocalStorage*), offline support, dan kemampuan **Progressive Web App (PWA)** sehingga dapat langsung dideploy ke **GitHub Pages** tanpa perlu konfigurasi server backend maupun database eksternal.

---

## 🌟 Fitur Utama

### 1. 📊 Dashboard Analitik Real-Time & KPI
- **KPI Summary Grid**: Total Pelanggaran, Kasus Kecepatan Ekstrem (≥40 KM/J), Kasus Belum Ditindak, dan Rekor Kecepatan Tertinggi.
- **Grafik Tren Pelanggaran**:
  - Pilihan tampilan **📈 Grafik Garis Area** atau **📊 Diagram Batang**.
  - Deteksi puncak kasus otomatis dengan penanda bintang (⭐).
  - Chip analisis cepat: **🏆 Puncak Kasus**, **📊 Rata-Rata per Bulan**, dan **📅 Kasus Bulan Terakhir**.
- **⚠️ Pelanggar Berulang (Repeat Violators)**:
  - Ditempatkan di bagian atas sebelum daftar terbaru untuk prioritas pengawasan.
  - Menampilkan jumlah pengulangan (contoh: `4x`, `3x`) dan dapat diklik untuk memfilter langsung riwayat nama bersangkutan.
- **🕐 Daftar Pelanggaran Terbaru**: Pilihan fleksibel menampilkan **5, 10, atau 15** data terbaru.

### 2. 🔐 Autentikasi & Role-Based Access Control (RBAC) 3-Tingkat
- **Mode Pengunjung (`view`)**:
  - Dapat diakses siapa saja **tanpa login**.
  - Hanya menampilkan **Dashboard** untuk transparansi monitoring K3.
  - Menu navigasi **Data, Statistik, dan Export disembunyikan secara otomatis** dari bilah navigasi bawah, dan tombol penambahan (FAB `➕`) dinonaktifkan.
- **Mode Petugas (`petugas`)**:
  - Login dengan akun petugas patroli.
  - Seluruh modul terbuka: Input Data, Edit Data, Perubahan Status Tindakan, Lihat Foto Bukti, dan Cetak STPK.
- **Mode Administrator (`admin`)**:
  - Memiliki semua hak akses petugas.
  - Memiliki modul khusus **Manajemen Akun Petugas** (Tambah, Edit, Hapus Akun Petugas).
- **Profil & Kontrol Terpadu**:
  - Tombol aksi akun, menu manajemen, logout, dan penggantian tema gelap/terang disatukan dalam satu menu dropdown elegan di kanan atas.

### 3. 📷 Foto Bukti Pelanggaran Interaktif & Kompresi Canvas
- **Pilihan Sumber Foto saat Diklik**:
  - Mengetuk kolom foto memunculkan jendela pop-up untuk memilih **📸 Kamera Langsung (Live Camera)** atau **🖼️ Pilih dari Galeri / File**.
- **Kompresi Otomatis di Browser**:
  - Foto dikompresi otomatis via HTML5 Canvas (resolusi maksimum 1000px, kualitas JPEG 0.75).
  - Ukuran foto tereduksi menjadi ~60KB - 100KB sehingga aman dan hemat kapasitas penyimpanan di *LocalStorage*.
- **Pratinjau & Lightbox**:
  - Kolom preview foto dilengkapi tombol **`🔄 Ganti`** dan **`🗑️ Hapus`**.
  - Kartu data menampilkan tombol **`📷 Lihat Foto Bukti`** untuk membuka foto beresolusi penuh (*lightbox*) berlatar gelap beserta tombol unduh.
  - Foto bukti otomatis tersemat pada lembar cetak Surat Teguran.

### 4. ✨ Rekomendasi Otomatis (Autocomplete & Auto-Fill)
- Saat mengetik nama di formulir pelanggaran, sistem mencocokkan kata kunci terhadap seluruh riwayat pengemudi yang pernah terdata.
- Memilih saran nama akan **mengisi kolom secara otomatis**:
  - 🏢 Bagian / Karyawan
  - 🪪 Nomor NIK / SIM
  - 🚘 Nomor Polisi
  - 🏍️ Jenis Kendaraan (Motor, Mobil, Truck, Forklift, Sepeda)

### 5. 📑 Surat Teguran Pelanggaran Kecepatan (STPK) & Ekspor Lengkap
- Generator otomatis nomor surat resmi: `STPK-[Nomor]/PUN/[Bulan Romawi]/[Tahun]`.
- Cetak langsung (*Print View*) atau simpan sebagai dokumen PDF.
- Menu **Export** mendukung:
  - 📗 **Microsoft Excel** (`.xlsx`) via SheetJS
  - 📕 **Dokumen PDF** (`.pdf`) via jsPDF AutoTable
  - 📘 **Berkas CSV** (`.csv`)
  - 🖨️ **Cetak Laporan Rekapitulasi**

---

## 🔑 Akun Demo Bawaan

| Role | Username | Password | Keterangan |
| :--- | :--- | :--- | :--- |
| **👑 Admin** | `admin` | `admin123` | Akses penuh & Kelola Petugas |
| **👮 Petugas** | `petugas` | `petugas123` | Akses seluruh modul data & input |
| **👁️ View** | *(Tanpa login)* | *(Tanpa login)* | Hanya melihat tampilan Dashboard |

*(Admin dapat menambah, mengedit nama/kata sandi, atau menghapus akun petugas kapan saja melalui menu akun di pojok kanan atas).*

---

## 🚀 Panduan Deploy ke GitHub Pages (1-Klik Gratis)

Aplikasi ini 100% siap dijalankan di GitHub Pages:

1. Buat repositori baru di akun GitHub Anda (misal: `speedguard-app`).
2. Jalankan perintah berikut di folder ini:
   ```bash
   git remote add origin https://github.com/<USERNAME-ANDA>/speedguard-app.git
   git branch -M main
   git push -u origin main
   ```
3. Buka tab **Settings** di repositori GitHub Anda.
4. Pada bilah navigasi kiri, pilih **Pages**.
5. Pada bagian **Build and deployment**:
   - **Source**: Pilih `Deploy from a branch`
   - **Branch**: Pilih `main` dan folder `/(root)`
   - Klik tombol **Save**.
6. Tunggu sekitar 1 menit, aplikasi Anda akan langsung online di URL:
   `https://<USERNAME-ANDA>.github.io/speedguard-app/`

---

## 💻 Menjalankan Secara Lokal (Local Development)

Anda dapat menjalankan aplikasi di komputer lokal menggunakan salah satu metode di bawah ini:

### Menggunakan Python (Tanpa Install Apapun)
```bash
# Python 3
python -m http.server 5000
```
Buka browser di `http://localhost:5000`.

### Menggunakan Node.js
```bash
npx serve . -l 5000
```

### Menggunakan VS Code
- Pasang ekstensi **Live Server**.
- Klik kanan file `index.html` dan pilih **Open with Live Server**.

---

## 📱 Panduan PWA (Instalasi di Ponsel / HP)

Aplikasi ini dilengkapi berkas `manifest.json`. Anda dapat menginstalnya ke layar utama (*Home Screen*) HP:
1. Buka tautan aplikasi di Google Chrome (Android) atau Safari (iOS).
2. **Android**: Tekan menu titik tiga (⋮) di pojok kanan atas -> pilih **Tambahkan ke Layar Utama** (*Install App*).
3. **iPhone/iPad**: Tekan tombol Bagikan (*Share*) -> pilih **Add to Home Screen**.
4. Aplikasi akan tampil layaknya aplikasi native tanpa bilah alamat browser.

---

## 📁 Struktur Direktori

```
D:\FAJAR Apps\GitHub\
├── .gitignore               # Berkas pengabaian git (OS & temp files)
├── LICENSE                  # Lisensi MIT
├── README.md                # Dokumentasi proyek
├── favicon.svg              # Ikon SVG kecepatan 20 km/jam
├── favicon.ico              # Ikon ICO kompatibilitas browser
├── manifest.json            # Web App Manifest PWA
├── chart.umd.min.js         # Pustaka Chart.js lokal (offline support)
├── index.html               # File aplikasi lengkap (HTML, CSS, JS, database awal)
└── tools/                   # Skrip utilitas pengolahan data riwayat
    ├── README.md            # Dokumentasi modul utilitas
    ├── parse_126.py         # Parser data mentah 126 kasus awal
    ├── apply_126.py         # Skrip injeksi data ke aplikasi
    ├── sync_rn_data.py      # Skrip sinkronisasi dataset
    └── initial_data_126.js  # Ekspor JavaScript data awal
```

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah lisensi [MIT](LICENSE) - bebas digunakan dan dikembangkan untuk operasional keselamatan kerja (K3).
