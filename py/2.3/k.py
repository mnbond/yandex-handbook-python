number = int(input())
digit_sum = 0
while number:
    digit_sum += number % 10
    number //= 10
print(digit_sum)
