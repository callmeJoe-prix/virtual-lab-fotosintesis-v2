import streamlit as st

st.set_page_config(layout="wide")

# ---- CSS untuk membuat slider gaya comphot-biotool ----
st.markdown("""
<style>
/* Warna teks slider */
.css-1emrehy edgvbvh3 {
    color: red !important;
}

/* Warna slider */
.stSlider > div[data-baseweb="slider"] > div > div {
    background: #ff4b4b !important;
}

/* Background tema gelap */
.block-container {
    background-color: #111111;
    padding: 2rem;
    border-radius: 12px;
}

/* Tombol */
div.stButton > button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 8px;
    height: 50px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

st.title("🔬 Photosynthesis Virtual Lab – Interactive Simulation")

st.write("Ubah parameter berikut untuk menjalankan simulasi fotosintesis secara virtual.")

# -------------------------------
# Layout 2 kolom seperti comphot
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    AL = st.slider("Light intensity of light phase (AL) in µmol m⁻² s⁻¹",
                   min_value=50, max_value=900, value=100)

    duration = st.slider("Test duration in minutes",
                         min_value=1, max_value=15, value=5)

    CtZ = st.slider("Conversion rate to Zeaxanthin (CtZ) in percent of default",
                    min_value=1, max_value=10000, value=100)

    dark_phase = st.slider("Length of the dark phase in seconds",
                           min_value=0, max_value=300, value=30)

with col2:
    SP_interval = st.slider("Seconds between saturating pulse during light phase",
                            min_value=5, max_value=150, value=85)

    CtV = st.slider("Conversion rate to Violaxanthin (CtV) in percent of default",
                    min_value=1, max_value=10000, value=100)

    SP = st.slider("Light intensity of saturating pulse (SP) in µmol m⁻² s⁻¹",
                   min_value=0, max_value=10000, value=5000)

# -------------------------------
# Tombol simulasi + checkbox
# -------------------------------
start = st.button("🚀 Start the simulation", use_container_width=True)
compare = st.checkbox("Compare with the last simulation")

# -------------------------------
# Placeholder Output
# -------------------------------
output = st.empty()

if start:
    output.info("Simulasi sedang berjalan... (model akan ditambahkan)")
else:
    output.write("📉 Grafik hasil simulasi akan tampil di sini.")
