import numpy as np


def make_board(n):
    board = np.zeros((n, n), dtype="int8")
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board