file_in_name, tail = input(), int(input())

with open(file_in_name, "r", encoding="UTF-8") as file_in:
    lines_count = sum(1 for _ in file_in)

with open(file_in_name, "r", encoding="UTF-8") as file_in:
    for i, line in enumerate(file_in):
        if i >= lines_count - tail:
            print(line, end="")
