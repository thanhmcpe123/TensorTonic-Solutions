import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    if not np.any(a) or not np.any(b):
        return 0.0
    denominator = np.linalg.norm(a) * np.linalg.norm(b)
    numerator = np.dot(a, b)
    return float(numerator/denominator)