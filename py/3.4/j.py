from itertools import product

count = int(input())
print("А Б В")
for a, b in product(range(1, count - 1), range(1, count - 1)):
    if a + b >= count:
        continue
    print(f"{a} {b} {count - a - b}")
