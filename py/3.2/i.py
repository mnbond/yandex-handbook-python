animals = dict()
while (line := input()) != "":
    for item in line.split():
        animals[item] = animals.get(item, 0) + 1
for animal, count in animals.items():
    print(animal, count)
