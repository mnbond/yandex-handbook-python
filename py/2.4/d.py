digit_sum = 0
for _ in range(int(input())):
    number = int(input())
    while number:
        digit_sum += number % 10
        number //= 10
print(digit_sum)
