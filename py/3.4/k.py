from itertools import product

rows, cols = int(input()), int(input())
width = len(str(rows * cols))
for n, m in product(range(rows), range(cols)):
    print(f"{n * cols + m + 1: >{width}} ", end="")
    if m == cols - 1:
        print()
