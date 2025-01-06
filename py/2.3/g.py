a = c = int(input())
b = d = int(input())
while b:
    tmp = a
    a = b
    b = tmp % b
print(c * d // a)
