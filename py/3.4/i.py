from itertools import product

numbers = [x for x in range(1, int(input()) + 1)]
for n in numbers:
    print(" ".join(str(a * b) for a, b in product([n], numbers)))
