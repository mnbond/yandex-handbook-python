result = set()
while (line := input()) != "":
    items = line.split()
    for i in range(len(items)):
        if items[i] == "зайка":
            if i > 0:
                result.add(items[i - 1])
            if i < len(items) - 1:
                result.add(items[i + 1])
print("\n".join(result))
