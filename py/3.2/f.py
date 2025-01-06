n, m = int(input()), int(input())
children = set()
for _ in range(n + m):
    child = input()
    if child in children:
        children.remove(child)
    else:
        children.add(child)
if len(children) > 0:
    print("\n".join(sorted(children)))
else:
    print("Таких нет")
