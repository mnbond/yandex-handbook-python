counters = dict()
for _ in range(int(input())):
    x, y = input().split()
    group = x[:-1] + " " + y[:-1]
    counters[group] = counters.get(group, 0) + 1
print(max(counters.values()))
