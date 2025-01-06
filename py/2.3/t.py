result = -1
h_prev = 0
for i in range(int(input())):
    b = int(input())
    m = b // 256 ** 2
    r = (b - m * 256 ** 2) // 256
    h = b - m * 256 ** 2 - r * 256
    if h >= 100 or h != 37 * (m + r + h_prev) % 256:
        result = i
        break
    h_prev = h
print(result)
