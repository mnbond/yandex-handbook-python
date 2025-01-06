from sys import stdin
from requests import get

total_sum = 0
address = "http://" + input()
pathes = [x.strip() for x in stdin.readlines()]
total_sum = sum(sum(get(address + x).json()) for x in pathes)
print(total_sum)
