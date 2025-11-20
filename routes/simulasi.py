import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from models.simulation_engine import run_simulation

st.write("DEBUG: simulasi.py loaded")

# Test impor model
try:
    from models.simulation_engine import run_simulation
    st.write("DEBUG: import simulation_engine OK")
except Exception as e:
    st.error(f"DEBUG: import error → {e}")


def run():
    st.title("🔬 Simulasi In Silico Fotosintesis")
    st.write("Atur parameter di panel kiri lalu tekan **Start the simulation**.")

    # Sidebar controls
    st.sidebar.header("Kontrol Simulasi")
    AL = st.sidebar.slider("Light intensity of light phase (AL) µmol m⁻² s⁻¹", 50, 900, 100)
    duration_min = st.sidebar.slider("Test duration in minutes", 1, 15, 5)
    SP_interval = st.sidebar.slider("Seconds between saturating pulse during light phase", 5, 150, 85)
    CtZ = st.sidebar.slider("Conversion rate to Zeaxanthin (CtZ) (%)", 1, 10000, 100)
    CtV = st.sidebar.slider("Conversion rate to Violaxanthin (CtV) (%)", 1, 10000, 100)
    dark_phase = st.sidebar.slider("Length of the dark phase (s)", 0, 300, 30)
    SP = st.sidebar.slider("Light intensity of saturating pulse (SP) µmol m⁻² s⁻¹", 0, 10000, 5000)

    start = st.sidebar.button("▶️ Start the simulation")
    st.sidebar.checkbox("Compare with the last simulation", key="compare_mode")

    # Initialize session_state storage
    if "last_simulation" not in st.session_state:
        st.session_state["last_simulation"] = None

    placeholder_info = st.empty()

    if start:
        placeholder_info.info("Simulasi berjalan... tunggu sebentar.")
        result = run_simulation(AL=AL, SP=SP, duration_min=duration_min, SP_interval_s=SP_interval,
                                CtZ_percent=CtZ, CtV_percent=CtV, temp=25)
        st.session_state["current_simulation"] = result

        # Compare
        if st.session_state.get("compare_mode", False) and st.session_state["last_simulation"] is not None:
            st.session_state["compare_active"] = True
        else:
            st.session_state["compare_active"] = False

        # Save current to last for next run (so user can compare next time)
        st.session_state["last_simulation"] = result
        placeholder_info.success("Simulasi selesai.")

    # If no simulation run yet, inform user
    if "current_simulation" not in st.session_state:
        st.info("Belum ada simulasi. Atur parameter di panel kiri dan tekan Start the simulation.")
        return

    res = st.session_state["current_simulation"]
    light_curve_df = res["light_curve_df"]
    co2_curve_df = res["co2_curve_df"]
    ts = res["time_series_df"]

    # Plot 1: Light response curve
    st.subheader("📈 Kurva Respon Cahaya (Pn vs Light)")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=light_curve_df["Light"], y=light_curve_df["Pn"],
                              mode="lines", name="Current simulation", line=dict(color="crimson")))
    # overlay last simulation if compare active and available
    if st.session_state.get("compare_active") and st.session_state.get("last_simulation") is not None:
        last = st.session_state["last_simulation"]["light_curve_df"]
        fig1.add_trace(go.Scatter(x=last["Light"], y=last["Pn"], mode="lines", name="Last simulation", line=dict(color="royalblue", dash="dash")))
    fig1.update_layout(xaxis_title="Light (µmol m⁻² s⁻¹)", yaxis_title="Pn", template="plotly_dark", height=400)
    st.plotly_chart(fig1, use_container_width=True)

    # Plot 2: CO2 response curve
    st.subheader("📈 Kurva Respon CO₂ (Pn vs CO₂)")
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=co2_curve_df["CO2"], y=co2_curve_df["Pn"],
                              mode="lines", name="Current simulation", line=dict(color="crimson")))
    if st.session_state.get("compare_active") and st.session_state.get("last_simulation") is not None:
        last = st.session_state["last_simulation"]["co2_curve_df"]
        fig2.add_trace(go.Scatter(x=last["CO2"], y=last["Pn"], mode="lines", name="Last simulation", line=dict(color="royalblue", dash="dash")))
    fig2.update_layout(xaxis_title="CO₂ (ppm)", yaxis_title="Pn", template="plotly_dark", height=400)
    st.plotly_chart(fig2, use_container_width=True)

    # Plot 3: Time series O2
    st.subheader("⏱️ Produksi O₂ (time series)")
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=ts["time_s"]/60.0, y=ts["O2"], mode="lines", name="Current simulation", line=dict(color="crimson")))
    if st.session_state.get("compare_active") and st.session_state.get("last_simulation") is not None:
        last_ts = st.session_state["last_simulation"]["time_series_df"]
        fig3.add_trace(go.Scatter(x=last_ts["time_s"]/60.0, y=last_ts["O2"], mode="lines", name="Last simulation", line=dict(color="royalblue", dash="dash")))
    fig3.update_layout(xaxis_title="Time (minutes)", yaxis_title="O₂ (arb. units)", template="plotly_dark", height=400)
    st.plotly_chart(fig3, use_container_width=True)

    # Controls for comparison reset
    cols = st.columns([1,1,1])
    if cols[0].button("Reset comparison"):
        st.session_state["last_simulation"] = None
        st.session_state["compare_active"] = False
        st.success("Comparison cleared.")

    # Export current simulation data
    st.download_button("Download current simulation (CSV)", ts.to_csv(index=False).encode('utf-8'), "current_simulation.csv")
