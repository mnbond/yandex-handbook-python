import numpy as np
import pandas as pd


def values(func, start, end, step):
    index = np.arange(start, end + step, step)
    result = pd.Series(map(func, index), index)
    return result


def min_extremum(data):
    return data[data == data.min()].index[0]


def max_extremum(data):
    return data[data == data.max()].index[0]
