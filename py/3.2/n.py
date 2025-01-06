result = set()    
in_stock = set()
for _ in range(int(input())):
    in_stock.add(input())
for _ in range(int(input())):
    recipe = input()
    items = set()
    for _ in range(int(input())):
        items.add(input())
    if len(items - in_stock) == 0:
        result.add(recipe)
if len(result) > 0:
    print("\n".join(sorted(result)))
else:
    print("Готовить нечего")
