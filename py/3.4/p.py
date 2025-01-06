from itertools import combinations, product

suits = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
nominals = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
necessary_suit = input()
nominals.remove(input())
counter = 0
for combination in combinations(product(sorted(nominals), sorted(suits.keys())), 3):
    if necessary_suit not in (s for _, s in combination):
        continue
    print(", ".join(f"{n} {suits[s]}" for n, s in combination))
    counter += 1
    if counter >= 10:
        break
