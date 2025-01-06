expression = input().split()
result = []
for char in expression:
    if char.isdigit():
        result.append(int(char))
    else:
        b, a = result.pop(), result.pop()
        if char == "+":
            result.append(a + b)
        elif char == "-":
            result.append(a - b)
        elif char == "*":
            result.append(a * b)
print(result[0])
