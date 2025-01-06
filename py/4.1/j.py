def merge(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) or j < len(b):
        if j == len(b) or (i < len(a) and j < len(b) and a[i] < b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    return tuple(result)