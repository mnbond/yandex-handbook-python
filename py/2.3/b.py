counter = 0
while (line := input()) != "Приехали!":
    if "зайка" in line:
        counter += 1
print(counter)
