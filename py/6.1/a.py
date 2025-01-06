import math

x = float(input())
f = math.log(math.pow(x, 3 / 16), 32)
f += math.pow(x, math.cos(math.pi * x / (2 * math.e)))
f -= math.pow(math.sin(x / math.pi), 2)
print(f)