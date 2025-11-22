import streamlit as st

# ===========================
#   HALAMAN SURVEY
# ===========================

st.set_page_config(page_title="Survey Pengalaman Belajar", layout="wide")

st.title("📋 Survey Pengalaman Belajar – Virtual Lab Fotosintesis")

st.markdown("""
Selamat datang di halaman **Survey Pengalaman Belajar Virtual Lab Fotosintesis** 👋

Mohon luangkan waktu sekitar **2–3 menit** untuk mengisi survey ini.

Survey ini bertujuan untuk:
- Mengukur pemahaman mahasiswa  
- Menilai kemudahan penggunaan Virtual Lab  
- Mengetahui pengalaman belajar sebelum & sesudah simulasi  
- Mengumpulkan masukan untuk pengembangan lab virtual selanjutnya  

Terima kasih atas partisipasinya 🙏
""")

st.divider()


# ===========================
#   GOOGLE FORM LINK
# ===========================

st.subheader("📝 Isi Form Survey")

st.markdown("""
Klik tombol di bawah untuk membuka form survey resmi:

👉 **[BUKA FORM SURVEY](https://docs.google.com/forms/d/1ftYfPiMdNJsLxIsXLJGioXMEu9_A2fKxwKIJu7NzZLU)**  
*(Ganti link ini setelah Google Form final dibuat)*  
""")

st.info("Pastikan Anda mengisi survey sampai selesai agar data tersimpan dengan benar.")


st.divider()


# ===========================
#   INFO MENGAPA SURVEY PENTING
# ===========================

st.subheader("📊 Mengapa Survey Ini Penting?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Data survey digunakan untuk:**
    - Mengukur efektivitas Virtual Lab  
    - Meningkatkan kualitas konten teori  
    - Memperbaiki UX simulasi interaktif  
    - Menentukan fitur tambahan untuk pengembangan berikutnya  
    """)

with col2:
    st.markdown("""
    **Manfaat bagi mahasiswa:**
    - Pengalaman belajar lebih interaktif  
    - Penjelasan materi yang lebih mudah dipahami  
    - Simulasi lebih realistis  
    - Mendukung pembelajaran mandiri dan praktikum digital  
    """)

st.success("Halaman survey siap digunakan ✔")
