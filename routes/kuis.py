import streamlit as st

st.title("🧪 Kuis Virtual Lab Fotosintesis")
st.write("Uji kemampuan Anda setelah melakukan simulasi Virtual Lab.")

# ============================
# KUNCI JAWABAN
# ============================
kunci_pg = {
    "q1": "C",
    "q2": "B",
    "q3": "B",
    "q4": "B",
    "q5": "B",
    "q6": "B",
    "q7": "C",
    "q8": "A",
    "q9": "B",
    "q10": "C"
}

# ============================
# FORM KUIS
# ============================
with st.form("quiz_form"):

    st.header("📘 Bagian A – Pilihan Ganda")

    q1 = st.radio("1. Faktor pembatas fotosintesis pada intensitas cahaya rendah adalah ...",
                  ["A. Suhu", "B. Rubisco", "C. Cahaya", "D. CO₂"])
    q2 = st.radio("2. Penurunan laju fotosintesis pada cahaya tinggi disebabkan oleh ...",
                  ["A. Rubisco jenuh", "B. Fotoinhibisi", "C. Suhu rendah", "D. Karotenoid turun"])
    q3 = st.radio("3. Fungsi saturating pulse (SP) adalah ...",
                  ["A. Mengukur respirasi", "B. Mengukur kapasitas ET", "C. Menurunkan suhu", "D. Menambah CO₂"])
    q4 = st.radio("4. CtZ dan CtV menggambarkan ...",
                  ["A. CO₂", "B. Xanthophyll cycle", "C. Stomata", "D. Kloroplas"])

    st.header("📗 Bagian B – Analisis Grafik")
    q5 = st.radio("5. Jika Pn tidak meningkat pada cahaya tinggi, artinya ...",
                  ["A. Cahaya membatasi", "B. Reaksi gelap jenuh", "C. CO₂ berlebih", "D. Fotosintesis berhenti"])
    q6 = st.radio("6. Osilasi O₂ pada grafik terjadi karena ...",
                  ["A. Suhu berubah", "B. Saturating pulse berkala", "C. Kesalahan model", "D. Rubisco turun"])
    q7 = st.radio("7. Kurva CO₂ datar pada kadar tinggi karena ...",
                  ["A. CO₂ toksik", "B. Cahaya rendah", "C. Rubisco jenuh", "D. Stomata menutup"])

    st.header("📙 Bagian C – Studi Kasus")
    q8 = st.radio("8. Cahaya naik 200 → 1500 tetapi O₂ hampir tidak naik. Apa yang perlu diubah?",
                  ["A. Tambah CO₂", "B. Turunkan suhu", "C. Suhu tetap", "D. Simulasi pendek"])
    q9 = st.radio("9. Suhu 45°C menurunkan O₂. Mengapa?",
                  ["A. Suhu ekstrem optimal", "B. Enzim rusak", "C. Cahaya terbatas", "D. CO₂ rendah"])
    q10 = st.radio("10. Pulse terlalu sering menyebabkan grafik ...",
                   ["A. Stabil", "B. O₂ naik terus", "C. Banyak puncak tajam", "D. O₂ nol"])

    st.header("📕 Bagian D – Bonus (Esai Singkat)")
    q11 = st.text_area("11. Mengapa CtZ meningkat pada cahaya tinggi?")
    q12 = st.text_area("12. Berdasarkan simulasi Anda, kapan fotosintesis optimum?")

    submitted = st.form_submit_button("📤 Kumpulkan Jawaban")

# ============================
# PROSES PENILAIAN
# ============================
if submitted:
    st.subheader("📊 Hasil Kuis")

    # Mengambil jawaban user → huruf saja
    jawaban_user = {
        "q1": q1[0],
        "q2": q2[0],
        "q3": q3[0],
        "q4": q4[0],
        "q5": q5[0],
        "q6": q6[0],
        "q7": q7[0],
        "q8": q8[0],
        "q9": q9[0],
        "q10": q10[0],
    }

    # Hitung skor
    benar = sum(jawaban_user[q] == kunci_pg[q] for q in kunci_pg)
    total_pg = len(kunci_pg)
    skor = round((benar / total_pg) * 100, 2)

    st.write(f"### 🎯 Skor Anda: **{skor} / 100**")
    st.write(f"Jawaban benar: **{benar} dari {total_pg} soal**")

    # Feedback otomatis
    if skor >= 85:
        st.success("🌟 Sangat baik! Pemahaman Anda sangat kuat.")
    elif skor >= 70:
        st.info("👍 Baik! Masih ada ruang untuk perbaikan.")
    else:
        st.warning("📘 Perlu belajar lagi. Coba ulangi simulasi dan baca grafik dengan teliti.")

    # ============================
    # Pembahasan
    # ============================
    with st.expander("📖 Lihat Pembahasan Lengkap"):
        st.write("""
        **Pembahasan Singkat Pilihan Ganda:**

        1. **C** – Intensitas cahaya rendah → cahaya pembatas.  
        2. **B** – Cahaya tinggi → fotoinhibisi pada PSII.  
        3. **B** – Saturating pulse mengecek kapasitas ET maksimum.  
        4. **B** – CtZ/CtV adalah bagian dari xanthophyll cycle.  
        5. **B** – Reaksi gelap jenuh meski cahaya tinggi.  
        6. **B** – Pulse berkala → puncak O₂ muncul periodik.  
        7. **C** – Rubisco jenuh pada CO₂ tinggi.  
        8. **A** – CO₂ menjadi pembatas.  
        9. **B** – Temperatur 45°C merusak enzim.  
        10. **C** – Pulse sering → grafik bergerigi/puncak intens.
        """)

        st.write("**11. CtZ meningkat karena zeaxanthin menyerap energi berlebih untuk mencegah fotoinhibisi (NPQ).**")
        st.write("**12. Jawaban bervariasi—berdasarkan grafik simulasi masing-masing mahasiswa.**")

