from itertools import cycle
from itertools import islice

porridges = [input() for _ in range(int(input()))]
for value in islice(cycle(porridges), 0, int(input())):
    print(value)
