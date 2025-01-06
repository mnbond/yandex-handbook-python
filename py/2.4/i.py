result = ""
for _ in range(int(input())):
    number = int(input())
    max_digit = 0
    while number:
        max_digit = max(max_digit, number % 10)
        number //= 10
    result += str(max_digit)
print(result)
