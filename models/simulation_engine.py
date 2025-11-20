import numpy as np
import pandas as pd
from .light_response import non_rectangular_hyperbola
from .co2_response import co2_response
from .oxygen_production import oxygen_from_assimilation

def run_simulation(AL, SP, duration_min, SP_interval_s, CtZ_percent=100, CtV_percent=100, temp=25):
    """
    Run a combined simulation.
    Parameters:
      AL: light intensity of light phase (µmol m-2 s-1)
      SP: saturating pulse intensity (µmol m-2 s-1)
      duration_min: total test duration in minutes
      SP_interval_s: seconds between saturating pulses
      CtZ_percent, CtV_percent: not yet used deeply (placeholders for xanthophyll dynamics)
      temp: temperature (°C)
    Returns:
      dict with:
         - light_curve_df: DataFrame with light intensities vs Pn
         - co2_curve_df: dummy CO2 vs Pn
         - time_series_df: time series of O2 over seconds (or minutes)
    """
    # Light-response curve (0..max_light)
    max_light = max(AL, SP, 1000)
    x = np.linspace(0, max_light, 200)
    # we adjust phi (quantum yield) slightly by CtZ/CtV (simple effect)
    phi = 0.04 * (1.0 + (CtZ_percent - 100)/10000.0 - (CtV_percent - 100)/10000.0)
    Amax = 20.0
    theta = 0.7
    Rd = 1.0

    Pn_light = non_rectangular_hyperbola(x, phi=phi, Amax=Amax, theta=theta, Rd=Rd)

    light_curve_df = pd.DataFrame({"Light": x, "Pn": Pn_light})

    # CO2-response curve (use range 0..1000 ppm)
    co2_x = np.linspace(0, 1000, 200)
    Pn_co2 = co2_response(co2_x, Vcmax=60.0, Kc=300.0, gamma_star=42.0, Rd=Rd)
    co2_curve_df = pd.DataFrame({"CO2": co2_x, "Pn": Pn_co2})

    # Time series: simulate seconds over duration minutes
    total_seconds = int(duration_min * 60)
    times = np.arange(0, total_seconds + 1)  # seconds
    # For each second, light exposure is AL, but every SP_interval_s a saturating pulse happens for 1s
    Pn_time = []
    temp_opt = 28.0
    temp_factor = np.exp(-((temp - temp_opt)**2) / 50.0)
    for t in times:
        current_light = AL
        # if saturating pulse moment:
        if SP_interval_s > 0 and (t % SP_interval_s == 0):
            current_light = SP
        # compute instantaneous Pn as product of light-limited and temp factor
        pn_inst = non_rectangular_hyperbola(np.array([current_light]), phi=phi, Amax=Amax, theta=theta, Rd=Rd)[0]
        pn_inst = pn_inst * temp_factor
        Pn_time.append(pn_inst)
    time_series_df = pd.DataFrame({"time_s": times, "Pn": Pn_time})
    # O2 production estimate
    time_series_df["O2"] = oxygen_from_assimilation(time_series_df["Pn"])

    return {
        "light_curve_df": light_curve_df,
        "co2_curve_df": co2_curve_df,
        "time_series_df": time_series_df
    }
