# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 3.1

### 3.1. Строки, кортежи, списки

A. Азбука
```python
flag = True
for _ in range(int(input())):
    if not input()[0] in "абв":
        flag = False
if flag:
    print("YES")
else:
    print("NO")
```

B. Кручу-верчу
```python
for char in input():
    print(char)
```

C. Анонс новости
```python
max_length = int(input())
for _ in range(int(input())):
    s = input()
    if len(s) > max_length:
        print(s[:max_length - 3] + "...")
    else:
        print(s)
```

D. Очистка данных
```python
while (s := input()) != "":
    if s.endswith("@@@"):
        continue
    if s.startswith("##"):
        s = s[2:]
    print(s)
```

E. А роза упала на лапу Азора 4.0
```python
s = input()
n = len(s)
if s[:n // 2] == s[:(n - 1) // 2:-1]:
    print("YES")
else:
    print("NO")
```

F. Зайка — 6
```python
counter = 0
for _ in range(int(input())):
    counter += input().count("зайка")
print(counter)
```

G. А и Б сидели на трубе
```python
numbers = input().split()
print(int(numbers[0]) + int(numbers[1]))
```

H. Зайка — 7
```python
for _ in range(int(input())):
    pos = input().find("зайка")
    if pos != -1:
        print(pos + 1)
    else:
        print("Заек нет =(")
```

I. Без комментариев
```python
while (s := input()) != "":
    pos = s.find("#")
    if pos == -1:
        print(s)
    elif pos > 0:
        print(s[:pos])
```

J. Частотный анализ на минималках
```python
text = ""
while (s := input()) != "ФИНИШ":
    text += s.lower()
top_char = ""    
max_count = 0
for char in text:
    if char == " ":
        continue
    count = text.count(char)
    if count > max_count or (count == max_count and char < top_char):
        top_char = char
        max_count = count
print(top_char)
```

K. Найдётся всё
```python
titles = []
for _ in range(int(input())):
    titles.append(input())
query = input().lower()
for title in titles:
    if query in title.lower():
        print(title)
```

L. Меню питания
```python
items = ("Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая")
for i in range(int(input())):
    print(items[i % len(items)])
```

M. Массовое возведение в степень
```python
numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
power = int(input())
for n in numbers:
    print(n ** power)
```

N. Массовое возведение в степень 2.0
```python
numbers = input().split()
power = int(input())
result = []
for n in numbers:
    result.append(str(int(n) ** power))
print(" ".join(result))
```

O. НОД 3.0
```python
numbers = input().split()
a = int(numbers[0])
for b in numbers[1:]:
    b = int(b)
    while b:
        a, b = b, a % b
print(a)
```

P. Анонс новости 2.0
```python
limit = int(input())
lines = []
for _ in range(int(input())):
    lines.append(input())
if len("".join(lines)) <= limit:
    print("\n".join(lines))
else:
    limit -= 3
    for line in lines:
        if len(line) < limit:
            print(line)
            limit -= len(line)
        else:
            print(line[:limit] + "...")
            break
```

Q. А роза упала на лапу Азора 5.0
```python
s = "".join(input().lower().split())
n = len(s)
if s[:n // 2] == s[:(n - 1) // 2:-1]:
    print("YES")
else:
    print("NO")
```

R. RLE
```python
s = input()
n = len(s)
counter = 1
for i in range(n):
    if i == n - 1 or s[i] != s[i + 1]:
        print(s[i], counter)
        counter = 1
    else:
        counter += 1
```

S. Польский калькулятор
```python
expression = input().split()
result = []
for char in expression:
    if char.isdigit():
        result.append(int(char))
    else:
        b, a = result.pop(), result.pop()
        if char == "+":
            result.append(a + b)
        elif char == "-":
            result.append(a - b)
        elif char == "*":
            result.append(a * b)
print(result[0])
```

T. Польский калькулятор — 2
```python
expression = input().split()
result = []
for char in expression:
    if char.isdigit():
        result.append(int(char))
    else:
        if char in "~!#":
            a = result.pop()
            if char == "~":
                result.append(-a)
            elif char == "!":
                fact = 1
                for i in range(1, a + 1):
                    fact *= i
                result.append(fact)
            elif char == "#":
                result.extend([a, a])
        elif char in "+-*/":
            b, a = result.pop(), result.pop()
            if char == "+":
                result.append(a + b)
            elif char == "-":
                result.append(a - b)
            elif char == "*":
                result.append(a * b)
            elif char == "/":
                result.append(a // b)
        elif char == "@":
            c, b, a = result.pop(), result.pop(), result.pop()
            result.extend([b, c, a])
print(result[0])
```