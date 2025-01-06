a = int(input())
b = int(input())
while b:
    tmp = a
    a = b
    b = tmp % b
print(a)
