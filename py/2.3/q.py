number = int(input())
clean_number = ""
while number:
    if number % 10 % 2 != 0:
        clean_number = str(number % 10) + clean_number
    number //= 10
print(clean_number)
