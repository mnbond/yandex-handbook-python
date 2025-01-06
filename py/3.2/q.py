persons = dict()
while (line := input()) != "":
    x, y = line.split()
    persons[x] = persons.get(x, set()) | {y}
    persons[y] = persons.get(y, set()) | {x}
for x in sorted(persons.keys()):
    level_1 = persons[x]
    level_2 = set()
    for y in level_1:
        level_2 = level_2 | persons[y]
    level_2 = level_2 - level_1 - {x}
    print(f"{x}: {', '.join(sorted(level_2))}")
