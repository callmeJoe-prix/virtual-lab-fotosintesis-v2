import streamlit as st

# DEBUG
st.write("DEBUG: simulasi.py loaded")
try:
    from models.simulation_engine import run_simulation
    st.write("DEBUG: import simulation_engine OK")
except Exception as e:
    st.error(f"DEBUG: import error → {e}")

# -----------------------------------------
# TITLE
# -----------------------------------------
st.title("🔬 Virtual Lab Fotosintesis – Simulasi Interaktif")


# -----------------------------------------
# CSS (AMAN, TIDAK BREAK LAYOUT)
# -----------------------------------------
st.markdown("""
<style>
div.stButton > button {
    background-color:#ff4b4b;
    color:white;
    height:50px;
    border-radius:8px;
    font-size:18px;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------------------
# SLIDER LAYOUT (SELALU TAMPIL)
# -----------------------------------------
col1, col2 = st.columns(2)

with col1:
    AL = st.slider("Light intensity (AL)", 10, 1000, 200)
    duration = st.slider("Test duration (minutes)", 1, 15, 5)
    dark_phase = st.slider("Dark phase length (seconds)", 0, 300, 30)

with col2:
    SP = st.slider("Saturating Pulse (SP)", 0, 10000, 5000)
    CtZ = st.slider("Conversion rate to Zeaxanthin (CtZ %)", 1, 10000, 100)
    CtV = st.slider("Conversion rate to Violaxanthin (CtV %)", 1, 10000, 100)

compare = st.checkbox("Compare with last simulation")

# TOMBOL
start = st.button("🚀 Start Simulation", use_container_width=True)

# -----------------------------------------
# OUTPUT PLACEHOLDER
# -----------------------------------------
out = st.empty()


# -----------------------------------------
# SIMULASI BERJALAN NORMAL
# -----------------------------------------
if start:
    st.write("DEBUG: mulai simulasi")

    params = {
        "AL": AL,
        "duration": duration,
        "CtZ": CtZ,
        "CtV": CtV,
        "SP": SP,
        "dark_phase": dark_phase,
    }

    # JALANKAN MODEL
    result = run_simulation(params)

    # Simpan sebagai last simulation
    if "last_simulation" not in st.session_state:
        st.session_state.last_simulation = None

    last = st.session_state.last_simulation
    st.session_state.last_simulation = result

    # -----------------------------------------
    # TAMPILKAN HASIL
    # -----------------------------------------
    st.subheader("📊 Grafik Hasil Simulasi")

    import plotly.express as px

    # contoh grafik: kurva cahaya
    df_light = result["light_curve"]

    fig = px.line(df_light, x="Light", y="Anet", title="Light Response Curve (Current Simulation)")
    fig.update_traces(line=dict(color="red"))

    st.plotly_chart(fig, use_container_width=True)

    # BANDINKAN
    if compare and last is not None:
        st.subheader("📌 Perbandingan dengan Simulasi Sebelumnya")

        df_last = last["light_curve"]
        fig2 = px.line(df_last, x="Light", y="Anet", title="Last Simulation")
        fig2.update_traces(line=dict(color="blue"))

        st.plotly_chart(fig2, use_container_width=True)

else:
    st.info("Tekan tombol **Start Simulation** untuk menjalankan simulasi.")
