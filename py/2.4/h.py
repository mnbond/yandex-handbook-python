winner = ""
max_sum = 0
for _ in range(int(input())):
    name = input()
    number = int(input())
    current_sum = 0
    while number:
        current_sum += number % 10
        number //= 10
    if current_sum >= max_sum:
        winner = name
        max_sum = current_sum
print(winner)
