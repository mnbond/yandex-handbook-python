import math

x, y = map(float, input().split())
ro, phi = map(float, input().split())
result = math.dist((x, y), (math.cos(phi) * ro, math.sin(phi) * ro))
print(result)