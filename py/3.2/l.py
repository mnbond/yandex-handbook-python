persons = set()
repeats = dict()
for _ in range(int(input())):
    name = input()
    if name in persons:
        if name in repeats:
            repeats[name] += 1
        else:
            repeats[name] = 2
    else:
        persons.add(name)
if len(repeats):
    for name in sorted(repeats.keys()):
        print(f"{name} - {repeats[name]}")
else:
    print("Однофамильцев нет")
