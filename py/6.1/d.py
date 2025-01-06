import math

numbers = list(map(float, input().split()))
result = math.pow(math.prod(numbers), 1 / len(numbers))
print(result)