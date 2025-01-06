expression = input().split()
result = []
for char in expression:
    if char.isdigit():
        result.append(int(char))
    else:
        if char in "~!#":
            a = result.pop()
            if char == "~":
                result.append(-a)
            elif char == "!":
                fact = 1
                for i in range(1, a + 1):
                    fact *= i
                result.append(fact)
            elif char == "#":
                result.extend([a, a])
        elif char in "+-*/":
            b, a = result.pop(), result.pop()
            if char == "+":
                result.append(a + b)
            elif char == "-":
                result.append(a - b)
            elif char == "*":
                result.append(a * b)
            elif char == "/":
                result.append(a // b)
        elif char == "@":
            c, b, a = result.pop(), result.pop(), result.pop()
            result.extend([b, c, a])
print(result[0])
