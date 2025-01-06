items = set()
for _ in range(int(input())):
    items = items | set(input().split())
print("\n".join(items))
