def is_iterable(x):
    try:
        iter(x)
    except Exception:
        raise StopIteration
    return True


def is_same_type(elements):
    for i in range(len(elements) - 1):
        if not isinstance(elements[i], type(elements[i + 1])):
            raise TypeError
    return True


def is_sorted(elements):
    for i in range(len(elements) - 1):
        if elements[i] > elements[i + 1]:
            raise ValueError
    return True


def merge(a, b):
    if (is_iterable(a) and is_iterable(b) 
            and is_same_type((*a, *b)) 
            and is_sorted(a) and is_sorted(b)):
        result = []
        i, j = 0, 0
        while i < len(a) or j < len(b):
            if j == len(b) or (i < len(a) and j < len(b) and a[i] < b[j]):
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        return result