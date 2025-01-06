s = input()
n = len(s)
counter = 1
for i in range(n):
    if i == n - 1 or s[i] != s[i + 1]:
        print(s[i], counter)
        counter = 1
    else:
        counter += 1
