import numpy as np


def stairs(vector):
    n = len(vector)
    matrix = np.zeros((n, n), dtype=vector.dtype)
    for i in np.arange(n):
        matrix[i] = np.roll(vector, i)
    return matrix
