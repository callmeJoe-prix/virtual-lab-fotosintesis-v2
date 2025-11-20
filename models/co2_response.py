import numpy as np

def co2_response(Ci, Vcmax=60.0, Kc=300.0, gamma_star=42.0, Rd=1.0):
    """
    Simplified Rubisco-limited assimilation (very simplified)
    An = Vcmax * (Ci - gamma*) / (Ci + Kc) - Rd
    """
    Ci = np.array(Ci, dtype=float)
    An = Vcmax * (Ci - gamma_star) / (Ci + Kc) - Rd
    # Clip negative to zero (simplified)
    An = np.maximum(An, 0.0)
    return An
