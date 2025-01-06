rows = int(input())
cols = int(input())
width = len(str(rows * cols))
for row in range(rows):
    for col in range(cols):
        if col % 2 == 0:
            n = col * rows + row + 1
        else:
            n = (col + 1) * rows - row
        print(f"{n: >{width}}", end=" ")
    print()
