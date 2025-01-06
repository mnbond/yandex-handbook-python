from itertools import chain

goods_iter = chain.from_iterable(input().split(", ") for _ in range(int(input())))
for index, value in enumerate(sorted(goods_iter), 1):
    print(f"{index}. {value}")
