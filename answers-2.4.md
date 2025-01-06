# Решение задач из хэндбука Яндекс «Основы Python», глава 2

## Параграф 2.4. Вложенные циклы

A. Таблица умножения
```python
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j} ", end="")
    print()
```

B. Не таблица умножения
```python
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{j} * {i} = {i * j}")
```

C. Новогоднее настроение
```python
n = int(input())
level = 1
counter = 0
for i in range(1, n + 1):
    print(i, end=" ")
    counter += 1
    if counter == level:
        print()
        level += 1
        counter = 0
```

D. Суммарная сумма
```python
digit_sum = 0
for _ in range(int(input())):
    number = int(input())
    while number:
        digit_sum += number % 10
        number //= 10
print(digit_sum)
```

E. Зайка — 5
```python
counter = 0
for _ in range(int(input())):
    flag = False
    while (animal := input()) != "ВСЁ":
        if animal == "зайка":
            flag = True
    if flag:
        counter += 1
print(counter)
```

F. НОД 2.0
```python
n = int(input())
a = int(input())
for _ in range(n - 1):
    b = int(input())
    while b:
        tmp = a
        a = b
        b = tmp % b
print(a)
```

G. На старт! Внимание! Марш!
```python
for i in range(int(input())):
    for j in range(3 + i, 0, -1):
        print(f"До старта {j} секунд(ы)")
    print(f"Старт {i + 1}!!!")
```

H. Максимальная сумма
```python
winner = ""
max_sum = 0
for _ in range(int(input())):
    name = input()
    number = int(input())
    current_sum = 0
    while number:
        current_sum += number % 10
        number //= 10
    if current_sum >= max_sum:
        winner = name
        max_sum = current_sum
print(winner)
```

I. Большое число
```python
result = ""
for _ in range(int(input())):
    number = int(input())
    max_digit = 0
    while number:
        max_digit = max(max_digit, number % 10)
        number //= 10
    result += str(max_digit)
print(result)
```

J. Мы делили апельсин
```python
n = int(input())
print("А Б В")
for i in range(1, n - 1):
    for j in range(1, n - i):
        print(i, j, n - i - j)
```

K. Простая задача 3.0
```python
counter = 0
for _ in range(int(input())):
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
        counter += 1
print(counter)
```

L. Числовой прямоугольник
```python
rows = int(input())
cols = int(input())
width = len(str(rows * cols))
for row in range(rows):
    for col in range(cols):
        print(f"{row * cols + col + 1: >{width}}", end=" ")
    print()
```

M. Числовой прямоугольник 2.0
```python
rows = int(input())
cols = int(input())
width = len(str(rows * cols))
for row in range(rows):
    for col in range(cols):
        print(f"{col * rows + row + 1: >{width}}", end=" ")
    print()
```

N. Числовая змейка
```python
rows = int(input())
cols = int(input())
width = len(str(rows * cols))
for row in range(rows):
    for col in range(cols):
        if row % 2 == 0:
            n = row * cols + col + 1
        else:
            n = (row + 1) * cols - col
        print(f"{n: >{width}}", end=" ")
    print()
```

O. Числовая змейка 2.0
```python
rows = int(input())
cols = int(input())
width = len(str(rows * cols))
for row in range(rows):
    for col in range(cols):
        if col % 2 == 0:
            n = col * rows + row + 1
        else:
            n = (col + 1) * rows - row
        print(f"{n: >{width}}", end=" ")
    print()
```

P. Редизайн таблицы умножения
```python
n = int(input())
width = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j: ^{width}}", end="")
        if j < n:
            print("|", end="")
        else:
            print()
    if i < n:
        print("-" * (n * (width + 1) - 1))
```

Q. А роза упала на лапу Азора 3.0
```python
counter = 0
for _ in range(int(input())):
    number = int(input())
    direct_number = str(number)
    reversed_number = ""
    while number:
        reversed_number += str(number % 10)
        number //= 10
    if direct_number == reversed_number:
        counter += 1
print(counter)
```

R. Новогоднее настроение 2.0
```python
n = int(input())
max_width = 0
for x in range(2):
    line = ""
    level = 1
    counter = 0
    for i in range(1, n + 1):
        if counter != 0:
            line += " "
        line += str(i)
        counter += 1
        if counter == level or i == n:
            if x == 0:
                max_width = max(max_width, len(line))
            else:
                print(f"{line: ^{max_width}}")
            line = ""
            level += 1
            counter = 0
```

S. Числовой квадрат
```python
n = int(input())
width = len(str((n + 1) // 2)) + 1
for i in range(n):
    for j in range(n):
        val = min(i + 1, j + 1, n - i, n - j)
        print(f"{val: ^{width}}", end="")
    print()
```

T. Математическая выгода
```python
number = int(input())
max_sum = 0
top_base = 2
for base in range(2, 11):
    x = number
    current_sum = 0
    while x:
        current_sum += x % base
        x //= base
    if current_sum > max_sum:
        max_sum = current_sum
        top_base = base
print(top_base)
```