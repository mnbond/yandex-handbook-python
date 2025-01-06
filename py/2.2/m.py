a = int(input())
b = int(input())
c = int(input())
if a % 10 == b % 10 and a % 10 == c % 10:
    print(a % 10)
else:
    print(a // 10)
