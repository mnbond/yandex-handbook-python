import numpy as np


def rotate(matrix, degrees):
    return np.rot90(matrix, -degrees // 90)
