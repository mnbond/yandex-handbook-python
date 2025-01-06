n = int(input())
if n // 1000 == n % 10 and n // 100 % 10 == n // 10 % 10:
    print("YES")
else:
    print("NO")
