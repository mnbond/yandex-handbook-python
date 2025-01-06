persons = set()
uniques = set()
for _ in range(count := int(input())):
    name = input()
    if name in persons:
        uniques.discard(name)
    else:
        persons.add(name)
        uniques.add(name)
print(count - len(uniques))
