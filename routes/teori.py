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
""")

# --- Tambahan: Tampilan Persamaan Reaksi Fotosintesis ---
st.subheader("Persamaan Reaksi Fotosintesis")
# Menggunakan st.latex untuk menampilkan persamaan kimia yang diformat dengan baik
st.latex(
    r"""
    \text{6 CO}_2 + \text{6 H}_2\text{O} \xrightarrow[\text{Klorofil}]{\text{Energi Cahaya}} \text{C}_6\text{H}_{12}\text{O}_6 + \text{6 O}_2
    """
)

st.markdown("""
<div style='background-color: #f0f2f6; padding: 10px; border-radius: 5px; margin-bottom: 20px;'>
    **Input:** 6 Karbon Dioksida ($\text{CO}_2$) + 6 Air ($\text{H}_2\text{O}$)
    <br>
    **Output:** Glukosa ($\text{C}_6\text{H}_{12}\text{O}_6$) + 6 Oksigen ($\text{O}_2$)
</div>
""", unsafe_allow_html=True)

# --- 3. Hitung dan Tampilkan Hasil ---

# Hitung hasil simulasi
rate, oxygen, glucose = calculate_photosynthesis_rate(light_intensity, co2_concentration)

# Tentukan Faktor Pembatas
limiting_factor_name = ""
if light_intensity < co2_concentration:
    limiting_factor_name = "Intensitas Cahaya"
    message_type = st.error
    
elif co2_concentration < light_intensity:
    limiting_factor_name = "Konsentrasi CO₂"
    message_type = st.error
    
else:
    limiting_factor_name = "Keseimbangan Optimal"
    message_type = st.info
    
# Tampilkan Hasil Utama
st.subheader("Laju Reaksi dan Produk")

col_rate, col_o2, col_glukosa = st.columns(3)

with col_rate:
    # Laju Reaksi
    st.metric(label="Laju Fotosintesis Total", value=f"{rate:.2f} Unit/Jam", delta=None)

with col_o2:
    # Produksi Oksigen
    st.metric(label="Produksi Oksigen ($\text{O}_2$)", value=f"{oxygen:.2f} Unit", delta=None)

with col_glukosa:
    # Produksi Glukosa
    st.metric(label="Produksi Glukosa ($\text{C}_6\text{H}_{12}\text{O}_6$)", value=f"{glucose:.2f} Unit", delta=None)

st.markdown("---")

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
