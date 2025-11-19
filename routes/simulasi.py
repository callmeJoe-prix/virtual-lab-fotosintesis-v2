import streamlit as st
import numpy as np
import pandas as pd

st.title("🧪 Simulasi Interaktif Fotosintesis")
st.write("Pada halaman ini, Anda dapat mensimulasikan pengaruh faktor lingkungan terhadap laju fotosintesis.")

st.write("---")

# ================================
# 1. Panel Pengaturan Variabel
# ================================
st.sidebar.header("🔧 Pengaturan Eksperimen")

light = st.sidebar.slider("Intensitas Cahaya (µmol m⁻² s⁻¹)", 0, 2000, 500)
co2 = st.sidebar.slider("Konsentrasi CO₂ (ppm)", 0, 2000, 400)
temp = st.sidebar.slider("Suhu (°C)", 0, 50, 25)
chlorophyll = st.sidebar.selectbox(
    "Jenis Daun (Jumlah Klorofil)",
    ["Rendah", "Sedang", "Tinggi"]
)

st.sidebar.write("---")
st.sidebar.write("Tekan tombol di bawah untuk menjalankan simulasi.")

run_simulation = st.sidebar.button("▶️ Jalankan Simulasi")


# ================================
# 2. Model Simulasi (Sementara)
# ================================
def photosynthesis_model(light, co2, temp, chlorophyll):

    # Faktor cahaya (kurva asimptotik sederhana)
    light_factor = (light / (light + 300))

    # Faktor CO₂ (penjenuhan)
    co2_factor = (co2 / (co2 + 400))

    # Faktor suhu (kurva optimum)
    temp_factor = np.exp(-((temp - 28) ** 2) / 50)

    # Faktor klorofil
    chl_map = {
        "Rendah": 0.7,
        "Sedang": 1.0,
        "Tinggi": 1.3
    }
    chl_factor = chl_map[chlorophyll]

    # Hasil akhir (model kombinasi)
    rate = 50 * light_factor * co2_factor * temp_factor * chl_factor
    return rate


# ================================
# 3. Ketika Simulasi Dijalankan
# ================================
if run_simulation:
    st.subheader("📊 Hasil Simulasi")

    rate = photosynthesis_model(light, co2, temp, chlorophyll)

    st.metric(label="Estimasi Laju Fotosintesis (unit arbitrary)", value=f"{rate:.2f}")

    # Buat grafik kecil untuk menunjukkan efek perubahan
    df = pd.DataFrame({
        "Variabel": ["Cahaya", "CO₂", "Suhu", "Klorofil"],
        "Nilai Normalisasi": [
            light / 2000,
            co2 / 2000,
            temp / 50,
            {"Rendah": 0.3, "Sedang": 0.6, "Tinggi": 1.0}[chlorophyll]
        ]
    })
    st.bar_chart(df, x="Variabel", y="Nilai Normalisasi")

    st.success("Simulasi selesai dijalankan!")
else:
    st.info("Atur variabel di panel samping dan jalankan simulasi.")
