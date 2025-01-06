side_1 = int(input())
side_2 = int(input())
side_3 = int(input())
if max(side_1, side_2, side_3) * 2 < side_1 + side_2 + side_3:
    print("YES")
else:
    print("NO")
