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
    return result


def merge_sort(items):
    if len(items) == 1:
        return items
    return merge(merge_sort(items[:len(items) // 2]), 
                 merge_sort(items[len(items) // 2:]))