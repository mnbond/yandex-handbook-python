n, m = int(input()), int(input())
children = set()
for _ in range(n + m):
    children.add(input())
count = len(children) * 2 - (n + m)
if count > 0:
    print(count)
else:
    print("Таких нет")
