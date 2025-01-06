a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif (a == 0 and b == 0) or d < 0:
    print("No solution")
elif a == 0:
    root = -c / b
    print(f"{root:.2f}")
elif d == 0:
    root = -b / (2 * a)
    print(f"{root:.2f}")
else:
    root_1 = (-b - d ** 0.5) / (2 * a)
    root_2 = (-b + d ** 0.5) / (2 * a)
    print(f"{min(root_1, root_2):.2f}", f"{max(root_1, root_2):.2f}")
