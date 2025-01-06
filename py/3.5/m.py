import json
from sys import stdin

with open(file_name := input(), "r", encoding="UTF-8") as file_in:
    content = json.load(file_in)

for line in stdin:
    variable, value = line.rstrip("\n").split(" == ")
    content[variable] = value

with open(file_name, "w", encoding="UTF-8") as file_out:
    json.dump(content, file_out, ensure_ascii=False, indent=4)
