Virtual Lab Fotosintesis – Interaktif untuk Pembelajaran Biologi

Bagian dari Proyek Aktualisasi Latsar CPNS Dosen UIN Ar-Raniry

Virtual Lab Fotosintesis ini dikembangkan sebagai media pembelajaran interaktif untuk membantu mahasiswa memahami konsep fotosintesis melalui teori, simulasi, kuis, dan survei pengalaman belajar.
Project ini merupakan bagian dari Aktualisasi Latsar CPNS Golongan III/b dan dirancang untuk meningkatkan kualitas pembelajaran berbasis teknologi di lingkungan perguruan tinggi.

📘 Deskripsi Singkat

Proyek ini menghadirkan sebuah dashboard pembelajaran interaktif berbasis Streamlit yang berfungsi sebagai:

Media pengayaan teori fotosintesis

Simulasi real-time hubungan intensitas cahaya, laju fotosintesis, dan produksi oksigen

Kuis otomatis

Survei pengalaman belajar mahasiswa

Tampilan sederhana, responsif, dan mudah digunakan

Tujuan utamanya adalah membangun Virtual Lab ringan yang dapat mendukung pembelajaran mandiri mahasiswa, terutama di mata kuliah Fisiologi Tumbuhan.

🎯 Tujuan Proyek

Proyek ini dibuat untuk memenuhi beberapa tujuan utama:

Tujuan Pembelajaran

Memberikan pemahaman konseptual dan visual mengenai proses fotosintesis

Menyediakan simulasi interaktif sebagai pengganti atau pendamping praktikum

Mempermudah mahasiswa melakukan eksperimen virtual tanpa peralatan laboratorium

Tujuan Aktualisasi CPNS

Sebagai bagian dari aktualisasi, proyek ini merefleksikan nilai:

Berorientasi Pelayanan → menyediakan sarana belajar baru bagi mahasiswa

Akuntabel → sistem transparan, dapat diakses, dan mudah dievaluasi

Kompeten → meningkatkan kemampuan pedagogik dan digital dosen

Harmonis & Adaptif → mendukung pembelajaran modern berbasis teknologi

Loyal & Kolaboratif → selaras dengan visi UIN Ar-Raniry dan kebutuhan mahasiswa

⚙️ Instalasi & Menjalankan Aplikasi

Pastikan menggunakan Python 3.11+.

1. Buat dan aktifkan virtual environment
conda create -n virtuallab python==3.11 pip
conda activate virtuallab

2. Install seluruh dependensi
pip install -r requirements.txt

3. Jalankan aplikasi Streamlit
streamlit run Start.py

📁 Struktur Proyek
virtual-lab-fotosintesis/
│
├── Start.py                 # Halaman utama Streamlit
├── routes/                  # Folder halaman-halaman modul
│   ├── teori.py
│   ├── simulasi.py
│   ├── kuis.py
│   ├── survey.py
│
├── assets/                  # Gambar, ikon, desain
├── utils/                   # Fungsi pendukung
├── requirements.txt
└── README.md

🧪 Fitur Utama
1. Teori Fotosintesis

Disajikan dalam bentuk ringkas, runtut, dan dilengkapi gambar.

2. Simulasi Fotosintesis

Slider intensitas cahaya

Grafik laju fotosintesis real-time

Indikator produksi oksigen

Animasi interaktif

3. Kuis Otomatis

Kuis pilihan ganda

Penilaian otomatis

Feedback instan untuk mahasiswa

4. Survei Pengalaman Belajar

Dibuat otomatis via Google Form melalui Apps Script

Mengumpulkan data kepuasan, pemahaman, dan pengalaman mahasiswa

🌐 Teknologi yang Digunakan

Streamlit – framework web interaktif berbasis Python

Matplotlib / Plotly – grafik simulasi

Pandas / NumPy – pengolahan data

Google Apps Script – pembuatan formulir survei otomatis

GitHub – version control dan dokumentasi

🏫 Kontribusi Terhadap Lembaga

Proyek ini berkontribusi langsung terhadap:

Peningkatan kualitas pembelajaran digital

Pengayaan materi praktikum Fisiologi Tumbuhan

Inovasi pembelajaran untuk mahasiswa UIN Ar-Raniry

Pengembangan kompetensi pedagogik dosen pemula

👨‍🏫 Pengembang

Dibuat oleh:
[Nama Anda] – Dosen CPNS, Program Studi [Isi]
UIN Ar-Raniry Banda Aceh

Sebagai bagian dari:
Aktualisasi Pelatihan Dasar CPNS 2025

🔖 Lisensi

Proyek ini bebas digunakan untuk kebutuhan pembelajaran dan penelitian.
