# Решение задач из хэндбука Яндекс «Основы Python», глава 2

## Параграф 2.2. Условный оператор

A. Просто здравствуй, просто как дела
```python
name = input("Как Вас зовут?\n")
print(f"Здравствуйте, {name}!")
answer = input("Как дела?\n")
if answer == "хорошо":
    print("Я за вас рада!")
elif answer == "плохо":
    print("Всё наладится!")
```

B. Кто быстрее?
```python
speed_1 = int(input())
speed_2 = int(input())
if speed_1 > speed_2:
    print("Петя")
else:
    print("Вася")
```

C. Кто быстрее на этот раз?
```python
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
```

D. Список победителей
```python
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
```

E. Яблоки
```python
first_count = 6 + int(input())
second_count = 12 + int(input())
if first_count > second_count:
    print("Петя")
else:
    print("Вася")
```

F. Сила прокрастинации
```python
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("YES")
else:
    print("NO")
```

G. А роза упала на лапу Азора
```python
n = int(input())
if n // 1000 == n % 10 and n // 100 % 10 == n // 10 % 10:
    print("YES")
else:
    print("NO")
```

H. Зайка — 1
```python
phrase = input()
if "зайка" in phrase:
    print("YES")
else:
    print("NO")
```

I. Первому игроку приготовиться
```python
name_1 = input()
name_2 = input()
name_3 = input()
print(min(name_1, name_2, name_3))
```

J. Лучшая защита — шифрование
```python
n = int(input())
sum_1_2 = n // 100 + n // 10 % 10
sum_2_3 = n // 10 % 10 + n % 10
print(max(sum_1_2, sum_2_3), min(sum_1_2, sum_2_3), sep="")
```

K. Красота спасёт мир
```python
n = int(input())
d_1 = n // 100
d_2 = n // 10 % 10
d_3 = n % 10
if (d_1 + d_2 + d_3) * 2 == (max(d_1, d_2, d_3) + min(d_1, d_2, d_3)) * 3:
    print("YES")
else:
    print("NO")
```

L. Музыкальный инструмент
```python
side_1 = int(input())
side_2 = int(input())
side_3 = int(input())
if max(side_1, side_2, side_3) * 2 < side_1 + side_2 + side_3:
    print("YES")
else:
    print("NO")
```

M. Властелин Чисел: Братство общей цифры
```python
a = int(input())
b = int(input())
c = int(input())
if a % 10 == b % 10 and a % 10 == c % 10:
    print(a % 10)
else:
    print(a // 10)
```

N. Властелин Чисел: Две Башни
```python
n = int(input())
d_1 = n % 10
d_2 = n // 10 % 10
d_3 = n // 100
min_d = min(d_1, d_2, d_3)
max_d = max(d_1, d_2, d_3)
mid_d = d_1 + d_2 + d_3 - min_d - max_d
if mid_d == 0:
    a = f"{max_d}{mid_d}"
elif min_d == 0:
    a = f"{mid_d}{min_d}"
else:
    a = f"{min_d}{mid_d}"
print(a, f"{max_d}{mid_d}")
```

O. Властелин Чисел: Возвращение Цезаря
```python
a = int(input())
b = int(input())
d_1 = a // 10
d_2 = a % 10
d_3 = b // 10
d_4 = b % 10
min_d = min(d_1, d_2, d_3, d_4)
max_d = max(d_1, d_2, d_3, d_4)
print(max_d, (d_1 + d_2 + d_3 + d_4 - min_d - max_d) % 10, min_d, sep="")
```

P. Легенды велогонок возвращаются: кто быстрее?
```python
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
print(f"{'': ^8}{first: ^8}{'': ^8}")
print(f"{second: ^8}{'': ^8}{'': ^8}")
print(f"{'': ^8}{'': ^8}{third: ^8}")
print(f"{'II': ^8}{'I': ^8}{'III': ^8}")
```

Q. Корень зла
```python
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
```

R. Территория зла
```python
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
```

S. Автоматизация безопасности
```python
x = float(input())
y = float(input())
if (x ** 2 + y ** 2) ** 0.5 > 10:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
else:
    if (x >= 0 and y >= 0 and (x ** 2 + y ** 2) ** 0.5 <= 5) \
            or (-4 <= x <= 0 and 0 <= y <= 5) \
            or (-7 <= x <= -4 and 0 <= y <= (x * 5 / 3 + 7 * 5 / 3)) \
            or (-7 <= x <= 5 and ((x + 1) ** 2) / 4 - 9 <= y <= 0):
        print("Опасность! Покиньте зону как можно скорее!")
    else:
        print("Зона безопасна. Продолжайте работу.")
```

T. Зайка — 2
```python
line_1 = input()
line_2 = input()
line_3 = input()
query = "зайка"
result = ""
if query in line_1:
    result = line_1
if query in line_2 and (result == "" or line_2 < result):
    result = line_2
if query in line_3 and (result == "" or line_3 < result):
    result = line_3
print(result, len(result))
```