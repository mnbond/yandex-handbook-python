n = int(input())
is_prime = True
if n == 1 or (n > 2 and n % 2 == 0):
    is_prime = False
else:
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print("YES")
else:
    print("NO")
