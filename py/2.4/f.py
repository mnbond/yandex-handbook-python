n = int(input())
a = int(input())
for _ in range(n - 1):
    b = int(input())
    while b:
        tmp = a
        a = b
        b = tmp % b
print(a)