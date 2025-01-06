from itertools import product

nominals = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
suits = ["пик", "треф", "бубен", "червей"]
suits.remove(input())
for n, s in product(nominals, suits):
    print(n, s)
