def gcd(*numbers):
    a = 0
    for b in numbers:
        while b:
            a, b = b, a % b
    return a