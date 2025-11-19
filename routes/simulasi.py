import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run():
    st.title("🧪 Simulasi Interaktif Fotosintesis")
    st.write("""
    Ubah parameter di bawah untuk melihat bagaimana **laju fotosintesis (Pn)** berubah 
    secara real-time berdasarkan intensitas cahaya, CO₂, dan suhu.
    """)

    st.subheader("⚙️ Parameter Simulasi")

    # Sliders
    cahaya = st.slider("Intensitas Cahaya (µmol m⁻² s⁻¹)", 0, 2000, 500)
    co2 = st.slider("Konsentrasi CO₂ (ppm)", 0, 1200, 400)
    suhu = st.slider("Suhu (°C)", 0, 45, 28)

    # Konstanta simulasi
    Amax = 20
    K = 300
    Kc = 400
    Topt = 28

    # Model matematis
    Pn_light = (Amax * cahaya) / (cahaya + K + 1e-9)
    Pn_co2 = (Amax * co2) / (co2 + Kc + 1e-9)
    T_factor = np.exp(-((suhu - Topt)**2) / 20)

    Pn = Pn_light * Pn_co2 * T_factor / Amax

    st.write(f"### 🌱 Laju Fotosintesis (Pn): **{Pn:.2f} µmol CO₂ m⁻² s⁻¹**")

    # Grafik Real-Time
    st.subheader("📈 Grafik Respon Fotosintesis")

    x = np.linspace(0, 2000, 200)
    y = ((Amax * x) / (x + K)) * (Pn_co2 / Amax) * T_factor

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("Intensitas Cahaya (µmol m⁻² s⁻¹)")
    ax.set_ylabel("Laju Fotosintesis (Pn)")
    ax.set_title("Kurva Respon Fotosintesis Terhadap Cahaya")
    st.pyplot(fig)

