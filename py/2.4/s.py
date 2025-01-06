n = int(input())
width = len(str((n + 1) // 2)) + 1
for i in range(n):
    for j in range(n):
        val = min(i + 1, j + 1, n - i, n - j)
        print(f"{val: ^{width}}", end="")
    print()
