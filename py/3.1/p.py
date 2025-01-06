limit = int(input())
lines = []
for _ in range(int(input())):
    lines.append(input())
if len("".join(lines)) <= limit:
    print("\n".join(lines))
else:
    limit -= 3
    for line in lines:
        if len(line) < limit:
            print(line)
            limit -= len(line)
        else:
            print(line[:limit] + "...")
            break
