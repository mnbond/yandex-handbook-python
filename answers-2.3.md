# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 2.3

### 2.3. Циклы

A. Раз, два, три! Ёлочка, гори!
```python
while input() != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")
```

B. Зайка — 3
```python
counter = 0
while (line := input()) != "Приехали!":
    if "зайка" in line:
        counter += 1
print(counter)
```

C. Считалочка
```python
start = int(input())
finish = int(input())
for i in range(start, finish + 1):
    print(i, end=" ")
```

D. Считалочка 2.0
```python
start = int(input())
finish = int(input())
if start < finish:
    step = 1
else:
    step = -1
for i in range(start, finish + step, step):
    print(i, end=" ")
```

E. Внимание! Акция!
```python
total_sum = 0
while (price := float(input())) != 0:
    if price < 500:
        total_sum += price
    else:
        total_sum += price * 0.9
print(total_sum)
```

F. НОД
```python
a = int(input())
b = int(input())
while b:
    tmp = a
    a = b
    b = tmp % b
print(a)
```

G. НОК
```python
a = c = int(input())
b = d = int(input())
while b:
    tmp = a
    a = b
    b = tmp % b
print(c * d // a)
```

H. Излишняя автоматизация 2.0
```python
phrase = input()
count = int(input())
for _ in range(count):
    print(phrase)
```

I. Факториал
```python
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)
```

J. Маршрут построен
```python
x = y = 0
while (direction := input()) != "СТОП":
    step = int(input())
    match direction:
        case "СЕВЕР":
            y += step
        case "ВОСТОК":
            x += step
        case "ЮГ":
            y -= step
        case "ЗАПАД":
            x -= step
print(y, x, sep="\n")
```

K. Цифровая сумма
```python
number = int(input())
digit_sum = 0
while number:
    digit_sum += number % 10
    number //= 10
print(digit_sum)
```

L. Сильная цифра
```python
number = int(input())
max_digit = 0
while number:
    max_digit = max(max_digit, number % 10)
    number //= 10
print(max_digit)
```

M. Первому игроку приготовиться 2.0
```python
count = int(input())
first_player = input()
for _ in range(count - 1):
    first_player = min(first_player, input())
print(first_player)
```

N. Простая задача
```python
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
    print("YES")
else:
    print("NO")
```

O. Зайка — 4
```python
counter = 0
for _ in range(int(input())):
    if "зайка" in input():
        counter += 1
print(counter)
```

P. А роза упала на лапу Азора 2.0
```python
number = int(input())
direct_number = str(number)
reversed_number = ""
while number:
    reversed_number += str(number % 10)
    number //= 10
if direct_number == reversed_number:
    print("YES")
else:
    print("NO")
```

Q. Чётная чистота
```python
number = int(input())
clean_number = ""
while number:
    if number % 10 % 2 != 0:
        clean_number = str(number % 10) + clean_number
    number //= 10
print(clean_number)
```

R. Простая задача 2.0
```python
number = int(input())
result = ""
for i in range(2, number):
    while number % i == 0:
        if len(result) > 0:
            result += " * " + str(i)
        else:
            result = str(i)
        number = number // i
print(result)
```

S. Игра в «Угадайку»
```python
left = 1
right = 1000
while left <= right:
    middle = (left + right) // 2
    print(middle)
    answer = input()
    if answer == "Меньше":
        right = middle - 1
    elif answer == "Больше":
        left = middle + 1
    else:
        break
```

T. Хайпанём немножечко!
```python
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
```