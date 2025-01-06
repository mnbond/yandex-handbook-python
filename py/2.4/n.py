rows = int(input())
cols = int(input())
width = len(str(rows * cols))
for row in range(rows):
    for col in range(cols):
        if row % 2 == 0:
            n = row * cols + col + 1
        else:
            n = (row + 1) * cols - col
        print(f"{n: >{width}}", end=" ")
    print()
