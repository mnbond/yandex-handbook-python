from math import comb

n, m = map(int, input().split())
print(m * comb(n, m) // n, comb(n, m))