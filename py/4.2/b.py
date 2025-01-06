def make_matrix(size, value=0):
    if isinstance(size, tuple):
        width, height = size
    else:
        width, height = size, size
    return list(map(lambda x: list(map(lambda y: value, range(width))), range(height)))
