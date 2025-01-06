flag = True
for _ in range(int(input())):
    if not input()[0] in "абв":
        flag = False
if flag:
    print("YES")
else:
    print("NO")
