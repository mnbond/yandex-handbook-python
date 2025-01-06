rows = int(input())
cols = int(input())
width = len(str(rows * cols))
for row in range(rows):
    for col in range(cols):
        print(f"{row * cols + col + 1: >{width}}", end=" ")
    print()
