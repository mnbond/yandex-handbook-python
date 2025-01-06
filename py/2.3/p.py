number = int(input())
direct_number = str(number)
reversed_number = ""
while number:
    reversed_number += str(number % 10)
    number //= 10
if direct_number == reversed_number:
    print("YES")
else:
    print("NO")
