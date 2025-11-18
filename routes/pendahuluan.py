import streamlit as st


# ================================
# Halaman Pendahuluan
# ================================

st.title("🌱 Virtual Lab - Fotosintesis")
st.markdown("---")

st.header("📘 Selamat Datang")
st.write(
    """
Virtual Lab Fotosintesis ini dirancang untuk membantu mahasiswa memahami proses fotosintesis
melalui pembelajaran interaktif, simulasi sederhana, serta kuis evaluasi.  
Laboratorium virtual ini dapat digunakan kapan saja tanpa memerlukan peralatan laboratorium fisik.
"""
)

# -------------------------------------------------------------------------
st.header("🎯 Tujuan Pembelajaran")
st.write(
    """
Setelah mengikuti Virtual Lab ini, mahasiswa diharapkan mampu:

1. **Menjelaskan konsep dasar fotosintesis**, termasuk reaksi terang dan reaksi gelap.
2. **Mengidentifikasi faktor-faktor yang memengaruhi laju fotosintesis**, seperti intensitas cahaya, CO₂, dan suhu.
3. **Melakukan simulasi interaktif** untuk melihat perubahan laju fotosintesis berdasarkan variabel yang diatur.
4. **Mengevaluasi pemahaman** melalui kuis otomatis.
"""
)

# -------------------------------------------------------------------------
st.header("🧭 Struktur Virtual Lab")
st.write(
    """
Virtual Lab ini terdiri dari beberapa bagian:

- **Pendahuluan** (halaman ini)  
  Penjelasan tujuan, manfaat, serta alur penggunaan aplikasi.

- **Teori Fotosintesis**  
  Ringkasan konsep ilmiah tentang fotosintesis.

- **Simulasi Interaktif**  
  Eksperimen virtual untuk mengamati bagaimana faktor eksternal memengaruhi fotosintesis.

- **Kuis**  
  Soal latihan untuk menguji pemahaman mahasiswa.

"""
)

# -------------------------------------------------------------------------
st.header("💡 Cara Menggunakan Virtual Lab")
st.write(
    """
1. Mulailah dengan membaca **Teori Fotosintesis**.  
2. Lanjutkan ke **Simulasi Interaktif** dan coba ubah variabel seperti intensitas cahaya atau kadar CO₂.  
3. Akhiri dengan mengerjakan **Kuis** untuk mengetahui tingkat pemahaman Anda.  
4. Tidak ada batasan waktu—Anda dapat mengulang kapan pun.

"""
)

# -------------------------------------------------------------------------
st.info(
    "**Catatan:** Virtual Lab ini merupakan bagian dari inovasi pembelajaran "
    "berbasis teknologi untuk mendukung pelaksanaan aktualisasi CPNS pada Prodi Biologi FST UIN Ar-Raniry Banda Aceh."
)

