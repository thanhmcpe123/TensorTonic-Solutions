import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    matrix = np.asarray(matrix, dtype=float)
    if norm_type == 'l1':
        norm = np.sum(abs(matrix), axis=axis, keepdims = True)
        matrix = np.where(norm==0, 0, matrix / norm)
    elif norm_type == 'l2':
        norm = np.sqrt(np.sum(matrix**2, axis=axis, keepdims = True))
        matrix = np.where(norm==0, 0, matrix / norm)
    else:
        norm = np.max(abs(matrix), axis=axis, keepdims = True)
        matrix = np.where(norm==0, 0, matrix / norm)
    
    return matrix