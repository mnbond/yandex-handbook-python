s = input()
n = len(s)
if s[:n // 2] == s[:(n - 1) // 2:-1]:
    print("YES")
else:
    print("NO")
