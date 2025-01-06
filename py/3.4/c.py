from itertools import count

start, finish, step = (float(x) for x in input().split())
for value in count(start, step):
    if value <= finish:
        print(f"{value:.2f}")
    else:
        break
