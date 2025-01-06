def enter_results(*numbers):
    results.extend(numbers)


def get_sum():
    total_sum = sum(results[::2]), sum(results[1::2])
    return tuple(map(lambda x: round(x, 2), total_sum))


def get_average():
    average = map(lambda x: x * 2 / len(results), get_sum())
    return tuple(map(lambda x: round(x, 2), average))


results = []
