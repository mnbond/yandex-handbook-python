from math import gcd
from sys import stdin

for line in stdin:
    print(gcd(*map(int, line.split())))