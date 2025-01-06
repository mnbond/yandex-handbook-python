from itertools import chain
from itertools import permutations

goods_iter = chain.from_iterable(input().split(", ") for _ in range(int(input())))
for values in permutations(sorted(goods_iter), 3):
    print(" ".join(values))
