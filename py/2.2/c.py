speed_1 = int(input())
speed_2 = int(input())
speed_3 = int(input())
max_speed = max(speed_1, speed_2, speed_3)
if max_speed == speed_1:
    print("Петя")
elif max_speed == speed_2:
    print("Вася")
else:
    print("Толя")
