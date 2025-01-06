groups = ([], [], [])
with open(input(), "r", encoding="UTF-8") as file_in:
    for line in file_in:
        line_groups = ([], [], [])
        for number in line.split():
            even = sum(1 for x in number if int(x) % 2 == 0)
            if even * 2 > (length := len(number)):
                ind = 0
            elif even * 2 < length:
                ind = 1
            else:
                ind = 2
            line_groups[ind].append(number)
        for ind in range(3):
            groups[ind].append(" ".join(line_groups[ind]) + "\n")

for group in groups:
    with open(input(), "w", encoding="UTF-8") as file_out:
        file_out.writelines(group)
