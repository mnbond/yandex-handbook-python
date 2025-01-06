def is_palindrome(x):
    if isinstance(x, int):
        x = str(x)
    n = len(x)
    if x[0:n // 2] == x[-1:-1 - n // 2:-1]:
        return True
    return False