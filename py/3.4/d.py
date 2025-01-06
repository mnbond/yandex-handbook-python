from itertools import accumulate

words = [x + " " for x in input().split()]
for value in accumulate(words):
    print(value)
