import numpy as np


def snake(width, height, direction="H"):
    if direction == "V":
        width, height = height, width
    matrix = np.arange(1, width * height + 1, dtype="int16").reshape(height, width)
    matrix[1::2, :] = matrix[1::2, ::-1]
    if direction == "V":
        matrix = matrix.transpose()
    return matrix