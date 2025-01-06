number = int(input())
result = ""
for i in range(2, number):
    while number % i == 0:
        if len(result) > 0:
            result += " * " + str(i)
        else:
            result = str(i)
        number = number // i
print(result)
