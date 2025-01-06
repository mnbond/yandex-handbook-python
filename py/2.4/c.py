n = int(input())
level = 1
counter = 0
for i in range(1, n + 1):
    print(i, end=" ")
    counter += 1
    if counter == level:
        print()
        level += 1
        counter = 0
