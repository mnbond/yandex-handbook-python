from itertools import product

expression = input()
variables = sorted(set(x for x in expression if x.isupper()))
print(" ".join(variables), "F")
for values in product((False, True), repeat=len(variables)):
    f = eval(expression, None, {x: y for x, y in zip(variables, values)})
    print(" ".join(str(int(x)) for x in values + (f, )))
