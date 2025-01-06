from itertools import permutations

for values in permutations(sorted(input() for _ in range(int(input()))), 3):
    print(", ".join(values))
