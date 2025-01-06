from itertools import product

expression = input()
print("a b c f")
for a, b, c in product((False, True), repeat=3):
    print(" ".join(str(int(x)) for x in (a, b, c, eval(expression))))
