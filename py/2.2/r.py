a = int(input()) ** 2
b = int(input()) ** 2
c = int(input()) ** 2
g = max(a, b, c)
if 2 * g < a + b + c:
    print("крайне мала")
elif 2 * g > a + b + c:
    print("велика")
else:
    print("100%")
