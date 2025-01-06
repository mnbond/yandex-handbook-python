toys = set()
uniques = set()
for _ in range(int(input())):
    for toy in set(input().split(": ")[1].split(", ")):
        if toy in toys:
            uniques.discard(toy)
        else:
            toys.add(toy)
            uniques.add(toy)
print("\n".join(sorted(uniques)))
