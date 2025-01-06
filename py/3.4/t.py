from itertools import product

expression = input()
operators = ["not", "and", "or", "->", "~", "^"]
variables = sorted(set(x for x in expression if x.isupper()))

rpn_expression = []
stack = []
for x in expression.replace("(", "( ").replace(")", " )").split():
    if x in variables:
        rpn_expression.append(x)
    elif x in operators:
        while len(stack) and stack[-1] != "(" and operators.index(stack[-1]) < operators.index(x):
            rpn_expression.append(stack.pop())
        stack.append(x)
    elif x == "(":
        stack.append(x)
    elif x == ")":
        while stack[-1] != "(":
            rpn_expression.append(stack.pop())
        stack.pop()
rpn_expression.extend(reversed(stack))

print(" ".join(variables), "F")
for values in product((False, True), repeat=len(variables)):
    f = []
    for x in rpn_expression:
        if x in variables:
            f.append(values[variables.index(x)])
        elif x == "not":
            f.append(not f.pop())
        else:
            b, a = f.pop(), f.pop()
            if x == "and":
                f.append(a and b)
            elif x == "or":
                f.append(a or b)
            elif x == "->":
                f.append(not a or b)
            elif x == "~":
                f.append(not a and not b or a and b)
            elif x == "^":
                f.append(a and not b or not a and b)
    print(" ".join(str(int(x)) for x in values + (f[0], )))
