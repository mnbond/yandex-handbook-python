items = ("Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая")
for i in range(int(input())):
    print(items[i % len(items)])
