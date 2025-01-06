porridges = dict()
for _ in range(int(input())):
    line = input().split()
    for porridge in line[1:]:
        porridges[porridge] = porridges.get(porridge, []) + [line[0]]
result = porridges.get(input(), ["Таких нет"])
print("\n".join(sorted(result)))