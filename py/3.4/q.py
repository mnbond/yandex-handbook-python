from itertools import combinations, product

suits = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
nominals = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
necessary_suit = input()
nominals.remove(input())
last_combination = input()
flag = False
for combination in combinations(product(sorted(nominals), sorted(suits.keys())), 3):
    if necessary_suit not in (s for _, s in combination):
        continue
    current_combination = ", ".join(f"{n} {suits[s]}" for n, s in combination)
    if flag:
        print(current_combination)
        break
    else:
        flag = current_combination == last_combination
