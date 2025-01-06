dishes = set()
for _ in range(int(input())):
    dishes.add(input())
for _ in range(int(input())):
    for _ in range(int(input())):
        dishes.discard(input()) 
if len(dishes) > 0:
    print("\n".join(sorted(dishes)))
else:
    print("Готовить нечего")
