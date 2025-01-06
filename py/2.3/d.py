start = int(input())
finish = int(input())
if start < finish:
    step = 1
else:
    step = -1
for i in range(start, finish + step, step):
    print(i, end=" ")
