from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x)

    count = {}
    max_key = x[0]
    max_value = 1
    for xi in x:
        if xi in count:
            count[xi] += 1
            if max_value < count[xi]:
                max_key = xi
                max_value = count[xi]
        else:
            count[xi] = 1
    dict = {"mean": float(np.mean(x)), "median": float(np.median(x)), "mode": float(max_key)}
    return dict