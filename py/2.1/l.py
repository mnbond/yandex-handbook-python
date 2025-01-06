a = int(input())
b = int(input())
result = (a % 10 + b % 10) % 10 \
         + (a // 10 % 10 + b // 10 % 10) % 10 * 10 \
         + (a // 100 % 10 + b // 100 % 10) % 10 * 100
print(result)
