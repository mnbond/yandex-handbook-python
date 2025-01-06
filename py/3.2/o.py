numbers = input().split()
result = []
for n in numbers:
    b = bin(int(n))[2:]
    result.append({
        "digits": len(b),
        "units": b.count("1"),
        "zeros": b.count("0")
    })
print(result)
