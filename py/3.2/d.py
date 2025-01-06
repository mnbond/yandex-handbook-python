n, m = int(input()), int(input())
children_1, children_2 = set(), set()
for _ in range(n):
    children_1.add(input())
for _ in range(m):
    children_2.add(input())
count = len(children_1 & children_2)
if count > 0:
    print(count)
else:
    print("Таких нет")
