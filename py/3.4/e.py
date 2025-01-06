from itertools import chain

goods = list(chain.from_iterable(input().split(", ") for _ in range(3)))
for index, value in enumerate(sorted(goods), 1):
    print(f"{index}. {value}")
