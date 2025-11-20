def oxygen_from_assimilation(An, stoich_factor=0.25):
    """
    Convert net assimilation (An) to O2 evolution estimate.
    This is a simplified relation: O2 ≈ stoich_factor * ETR ~ stoich_factor * (some function of An)
    For simplicity we scale An linearly to O2 units.
    """
    return An * stoich_factor
