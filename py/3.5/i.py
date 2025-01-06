lines = []
with open(input(), "r", encoding="UTF-8") as file_in:
    for line in file_in:
        line = " ".join(line.replace("\t", "").split())
        if line != "":
            lines.append(line + "\n")

with open(input(), "w", encoding="UTF-8") as file_out:
    file_out.writelines(lines)
