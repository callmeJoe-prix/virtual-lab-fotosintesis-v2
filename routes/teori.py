import streamlit as st
import pandas as pd

st.title("Teori Fotosintesis")
st.write("""
Kehidupan di Bumi secara fundamental bergantung pada energi yang berasal dari matahari. Fotosintesis merupakan satu-satunya
proses yang memiliki signifikansi biologis yang mampu memanen energi tersebut. Sebagian besar sumber daya energi planet ini,
baik yang baru (biomassa) maupun yang purba (bahan bakar fosil), merupakan hasil dari aktivitas fotosintetik. Secara harfiah,
istilah fotosintesis berarti "sintesis menggunakan cahaya." Organisme fotosintetik memanfaatkan energi surya untuk menyintesis 
senyawa karbon kompleks. Lebih spesifik, energi cahaya menggerakkan sintesis karbohidrat dan menghasilkan oksigen dari karbon
dioksida dan air, sesuai dengan persamaan stoikiometri berikut:

🌬️ **CO₂** + 💧 **H₂O** + ☀️ **Cahaya**  
➡️ 🍬 **Glukosa** + 🌫️ **Oksigen (O₂)**


Energi yang tersimpan dalam molekul karbohidrat ini kemudian dapat dimanfaatkan untuk mendukung berbagai proses seluler pada
tumbuhan dan berfungsi sebagai sumber energi utama bagi semua bentuk kehidupan.
""")

# --- Video Penjelasan ---
st.subheader("🎥 Penjelasan Singkat Fotosintesis")
video_file = "assets/video/fotosintesis_intro.mp4"
st.video(video_file)

# --- Struktur Kloroplas ---
st.header("Struktur Kloroplas")
st.image("assets/images/kloroplas_diagram.png", caption="Diagram Kloroplas")
st.write("""
Penjelasan bagian kloroplas:
- Grana  
- Tilakoid  
- Stroma  
""")

# --- Reaksi Terang ---
st.header("Reaksi Terang")
st.image("assets/images/light_reaction.png", caption="Diagram Reaksi Terang")
st.write("""
Penjelasan aliran elektron, fotolisis, ATP, NADPH, O₂.
""")

# --- Grafik Respon Cahaya ---
st.subheader("Grafik Laju Fotosintesis vs Intensitas Cahaya")
df_light = pd.read_csv("assets/graphs/kurva_cahaya.csv")
st.line_chart(df_light, x="Light", y="Rate")

# --- Reaksi Gelap (Siklus Calvin) ---
st.header("Siklus Calvin (Reaksi Gelap)")
st.image("assets/images/calvin_cycle.png", caption="Siklus Calvin")
st.write("""
Detail tahapan:
1. Karboksilasi  
2. Reduksi  
3. Regenerasi  
""")

# --- Faktor-Faktor yang Mempengaruhi ---
st.header("Faktor-Faktor Pembatas Fotosintesis")
st.image("assets/images/faktor_fotosintesis.png", caption="Faktor-faktor Fotosintesis")
st.write("""
Deskripsi masing-masing faktor:
- Intensitas cahaya  
- CO₂  
- Suhu  
- Pigmen  
""")

# --- Pigmen Fotosintetik ---
st.header("Pigmen Fotosintetik")
st.image("assets/images/pigment_spectrum.png", caption="Spektrum Pigmen")
st.write("""
- Klorofil a  
- Klorofil b  
- Karotenoid  
""")

# --- Ringkasan & Kesimpulan ---
st.markdown("---")
st.subheader("Kesimpulan")
st.write("""
Fotosintesis adalah proses kompleks tetapi sangat penting...  
(ditambah kesimpulan ringkas)
""")

df_light = pd.read_csv("assets/graphs/kurva_cahaya.csv")
st.line_chart(df_light, x="Light", y="Rate")

df_co2 = pd.read_csv("assets/graphs/grafik_co2.csv")
st.line_chart(df_co2, x="CO2", y="Rate")
