numbers = input().split()
power = int(input())
result = []
for n in numbers:
    result.append(str(int(n) ** power))
print(" ".join(result))
