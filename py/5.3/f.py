class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError
    d = b ** 2 - 4 * a * c
    if a == 0 and b == 0 and c == 0:
        raise InfiniteSolutionsError
    elif (a == 0 and b == 0) or d < 0:
        raise NoSolutionsError
    elif a == 0:
        roots = [-c / b, -c / b]
    elif d == 0:
        roots = [-b / (2 * a), -b / (2 * a)]
    else:
        roots = [(-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a)]
    return tuple(sorted(roots))