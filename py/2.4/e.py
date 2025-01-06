counter = 0
for _ in range(int(input())):
    flag = False
    while (animal := input()) != "ВСЁ":
        if animal == "зайка":
            flag = True
    if flag:
        counter += 1
print(counter)
