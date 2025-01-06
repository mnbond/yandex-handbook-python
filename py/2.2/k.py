n = int(input())
d_1 = n // 100
d_2 = n // 10 % 10
d_3 = n % 10
if (d_1 + d_2 + d_3) * 2 == (max(d_1, d_2, d_3) + min(d_1, d_2, d_3)) * 3:
    print("YES")
else:
    print("NO")
