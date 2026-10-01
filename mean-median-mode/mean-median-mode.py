from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x)

    counts = Counter(x.tolist())
    highest_frequency = max(counts.values())
    mode = min(value for value, count in counts.items() if count == highest_frequency)
    dict = {"mean": float(np.mean(x)), "median": float(np.median(x)), "mode": float(mode)}
    return dict