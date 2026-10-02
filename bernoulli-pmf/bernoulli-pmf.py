import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    pmf = (1 - x) + (-1)**(1 - x) * p
    mean = float(p)
    var = float(p*(1-p))
    return {"pmf": pmf, "mean": mean, "variance": var}