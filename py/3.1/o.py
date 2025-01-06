numbers = input().split()
a = int(numbers[0])
for b in numbers[1:]:
    b = int(b)
    while b:
        a, b = b, a % b
print(a)
