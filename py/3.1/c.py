max_length = int(input())
for _ in range(int(input())):
    s = input()
    if len(s) > max_length:
        print(s[:max_length - 3] + "...")
    else:
        print(s)
