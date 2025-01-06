from itertools import combinations

players = [input() for _ in range(int(input()))]
for a, b in combinations(players, 2):
    print(f"{a} - {b}")
