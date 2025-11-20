import numpy as np

def non_rectangular_hyperbola(I, phi=0.04, Amax=20, theta=0.7, Rd=1.0):
    """
    Returns An (photosynthetic rate) for given light intensity I (scalar or array).
    Formula: An = (phi*I + Amax - sqrt((phi*I + Amax)^2 - 4*theta*phi*I*Amax)) / (2*theta) - Rd
    """
    I = np.array(I, dtype=float)
    a = phi * I + Amax
    discr = a**2 - 4 * theta * phi * I * Amax
    # Numerical safety
    discr = np.maximum(discr, 0)
    An = (a - np.sqrt(discr)) / (2 * theta) - Rd
    # ensure non-negative
    An = np.maximum(An, 0.0)
    return An
