speed_1 = int(input())
speed_2 = int(input())
speed_3 = int(input())
min_speed = min(speed_1, speed_2, speed_3)
max_speed = max(speed_1, speed_2, speed_3)
if speed_1 == max_speed:
    first = "Петя"
elif speed_1 == min_speed:
    third = "Петя"
else:
    second = "Петя"
if speed_2 == max_speed:
    first = "Вася"
elif speed_2 == min_speed:
    third = "Вася"
else:
    second = "Вася"
if speed_3 == max_speed:
    first = "Толя"
elif speed_3 == min_speed:
    third = "Толя"
else:
    second = "Толя"
print(f"1. {first}\n2. {second}\n3. {third}")
