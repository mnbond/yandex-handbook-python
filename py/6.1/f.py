import numpy as np


def multiplication_matrix(n):
    return np.arange(1, n + 1) * np.arange(1, n + 1).reshape(n, 1)