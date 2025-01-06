n = int(input())
d_1 = n % 10
d_2 = n // 10 % 10
d_3 = n // 100
min_d = min(d_1, d_2, d_3)
max_d = max(d_1, d_2, d_3)
mid_d = d_1 + d_2 + d_3 - min_d - max_d
if mid_d == 0:
    a = f"{max_d}{mid_d}"
elif min_d == 0:
    a = f"{mid_d}{min_d}"
else:
    a = f"{min_d}{mid_d}"
print(a, f"{max_d}{mid_d}")
