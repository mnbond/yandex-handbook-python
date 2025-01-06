n = int(input())
width = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j: ^{width}}", end="")
        if j < n:
            print("|", end="")
        else:
            print()
    if i < n:
        print("-" * (n * (width + 1) - 1))
