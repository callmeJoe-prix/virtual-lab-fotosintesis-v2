import streamlit as st

def show_survey_page():
    st.title("📋 Survey Pengalaman Belajar")
    st.markdown("""
    Selamat datang di halaman **Survey Pengalaman Belajar Virtual Lab Fotosintesis**.  
    Mohon luangkan waktu sekitar **2–3 menit** untuk mengisi survey ini.

    Survey ini bertujuan untuk:
    - Mengukur pemahaman mahasiswa  
    - Menilai kemudahan penggunaan Virtual Lab  
    - Mengetahui pengalaman belajar sebelum & sesudah simulasi  
    - Mengumpulkan masukan untuk pengembangan lab virtual selanjutnya  

    Terima kasih atas partisipasinya 🙏
    """)
    
    st.divider()
    
    st.subheader("📝 Akses Form Survey")
    st.markdown("""
    Klik tombol di bawah untuk membuka form survey resmi:

    👉 **[BUKA FORM SURVEY](https://docs.google.com/forms/d/e/FORM_ID/viewform)**  
    *(Ganti link di atas setelah kamu membuat Google Form finalnya)*  
    """)

    st.info("Pastikan Anda mengisi survey sampai selesai agar data tersimpan.")

    st.divider()

    st.subheader("📊 Mengapa Survey Ini Penting?")
    st.markdown("""
    Data dari survey akan digunakan untuk:
    - Menilai efektivitas Virtual Lab  
    - Melakukan perbaikan konten teori  
    - Menambah fitur baru pada simulasi  
    - Meningkatkan pengalaman belajar mahasiswa  

    Semua data bersifat **anonim** dan hanya digunakan untuk keperluan akademik.
    """)

    st.success("Halaman survey siap digunakan ✔")
