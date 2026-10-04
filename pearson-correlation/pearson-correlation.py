import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    X_c = X - np.mean(X, axis = 0)
    co_matrix = X_c.T@X_c/(X.shape[0] - 1)
    std = np.sqrt(np.diag(co_matrix))
    return co_matrix/ np.outer(std, std)
    