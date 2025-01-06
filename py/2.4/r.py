n = int(input())
max_width = 0
for x in range(2):
    line = ""
    level = 1
    counter = 0
    for i in range(1, n + 1):
        if counter != 0:
            line += " "
        line += str(i)
        counter += 1
        if counter == level or i == n:
            if x == 0:
                max_width = max(max_width, len(line))
            else:
                print(f"{line: ^{max_width}}")
            line = ""
            level += 1
            counter = 0
