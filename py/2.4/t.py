number = int(input())
max_sum = 0
top_base = 2
for base in range(2, 11):
    x = number
    current_sum = 0
    while x:
        current_sum += x % base
        x //= base
    if current_sum > max_sum:
        max_sum = current_sum
        top_base = base
print(top_base)
