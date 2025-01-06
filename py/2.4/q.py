counter = 0
for _ in range(int(input())):
    number = int(input())
    direct_number = str(number)
    reversed_number = ""
    while number:
        reversed_number += str(number % 10)
        number //= 10
    if direct_number == reversed_number:
        counter += 1
print(counter)
