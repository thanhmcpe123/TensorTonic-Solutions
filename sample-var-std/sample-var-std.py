import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    centered = x - np.mean(x)
    var = float(np.sum(1/(x.size-1) * centered**2))
    dev = float(np.sqrt(var))

    return {"variance": var, "standard_deviation": dev}