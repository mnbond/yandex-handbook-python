def make_linear(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(make_linear(item))
        else:
            result.append(item)
    return result