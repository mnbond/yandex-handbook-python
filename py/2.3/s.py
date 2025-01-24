left = 1
right = 1000
while left <= right:
    middle = (left + right) // 2
    print(middle)
    answer = input()
    if answer == "Меньше":
        right = middle - 1
    elif answer == "Больше":
        left = middle + 1
    else:
        break
