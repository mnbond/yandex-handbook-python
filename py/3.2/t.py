numbers = []
for n in set(input().split("; ")):
    numbers.append(int(n))
numbers.sort()
primes = dict()
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        a, b = numbers[i], numbers[j]
        while b:
            a, b = b, a % b
        if a == 1:
            primes[numbers[i]] = primes.get(numbers[i], []) + [str(numbers[j])]
            primes[numbers[j]] = primes.get(numbers[j], []) + [str(numbers[i])]
    if numbers[i] in primes:
        print(f"{numbers[i]} - {', '.join(primes[numbers[i]])}")
