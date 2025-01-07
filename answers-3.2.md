# Решение задач из хэндбука Яндекс «Основы Python», глава 3

## Параграф 3.2. Множества, словари


A. Символическая выжималка
```python
print("".join(set(input())))
```

B. Символическая разница
```python
string_1 = input()
string_2 = input()
print("".join(set(string_1) & set(string_2)))
```

C. Зайка — 8
```python
items = set()
for _ in range(int(input())):
    items = items | set(input().split())
print("\n".join(items))
```

D. Кашееды
```python
n, m = int(input()), int(input())
children_1, children_2 = set(), set()
for _ in range(n):
    children_1.add(input())
for _ in range(m):
    children_2.add(input())
count = len(children_1 & children_2)
if count > 0:
    print(count)
else:
    print("Таких нет")
```

E. Кашееды — 2
```python
n, m = int(input()), int(input())
children = set()
for _ in range(n + m):
    children.add(input())
count = len(children) * 2 - (n + m)
if count > 0:
    print(count)
else:
    print("Таких нет")
```

F. Кашееды — 3
```python
n, m = int(input()), int(input())
children = set()
for _ in range(n + m):
    child = input()
    if child in children:
        children.remove(child)
    else:
        children.add(child)
if len(children) > 0:
    print("\n".join(sorted(children)))
else:
    print("Таких нет")
```

G. Азбука Морзе
```python
MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.",
    "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..",
    "9": "----."
}
for word in input().upper().split():
    encoded_word = []
    for char in word:
        encoded_word.append(MORSE[char])
    print(" ".join(encoded_word))
```

H. Кашееды — 4
```python
porridges = dict()
for _ in range(int(input())):
    line = input().split()
    for porridge in line[1:]:
        porridges[porridge] = porridges.get(porridge, []) + [line[0]]
result = porridges.get(input(), ["Таких нет"])
print("\n".join(sorted(result)))
```

I. Зайка — 9
```python
animals = dict()
while (line := input()) != "":
    for item in line.split():
        animals[item] = animals.get(item, 0) + 1
for animal, count in animals.items():
    print(animal, count)
```

J. Транслитерация
```python
RULES = {
    "А": "A", "Б": "B", "В": "V", "Г": "G",
    "Д": "D", "Е": "E", "Ё": "E", "Ж": "Zh",
    "З": "Z", "И": "I", "Й": "I", "К": "K",
    "Л": "L", "М": "M", "Н": "N", "О": "O",
    "П": "P", "Р": "R", "С": "S", "Т": "T",
    "У": "U", "Ф": "F", "Х": "Kh", "Ц": "Tc",
    "Ч": "Ch", "Ш": "Sh", "Щ": "Shch", "Ъ": "",
    "Ы": "Y", "Ь": "", "Э": "E", "Ю": "Iu", 
    "Я": "Ia"
}
result = ""
for char in input():
    new_char = RULES.get(char.upper(), char)
    if char.islower():
        new_char = new_char.lower()
    result += new_char
print(result)
```

K. Однофамильцы
```python
persons = set()
uniques = set()
for _ in range(count := int(input())):
    name = input()
    if name in persons:
        uniques.discard(name)
    else:
        persons.add(name)
        uniques.add(name)
print(count - len(uniques))
```

L. Однофамильцы — 2
```python
persons = set()
repeats = dict()
for _ in range(int(input())):
    name = input()
    if name in persons:
        if name in repeats:
            repeats[name] += 1
        else:
            repeats[name] = 2
    else:
        persons.add(name)
if len(repeats):
    for name in sorted(repeats.keys()):
        print(f"{name} - {repeats[name]}")
else:
    print("Однофамильцев нет")
```

M. Дайте чего-нибудь новенького!
```python
dishes = set()
for _ in range(int(input())):
    dishes.add(input())
for _ in range(int(input())):
    for _ in range(int(input())):
        dishes.discard(input()) 
if len(dishes) > 0:
    print("\n".join(sorted(dishes)))
else:
    print("Готовить нечего")
```

N. Это будет шедевр!
```python
result = set()    
in_stock = set()
for _ in range(int(input())):
    in_stock.add(input())
for _ in range(int(input())):
    recipe = input()
    items = set()
    for _ in range(int(input())):
        items.add(input())
    if len(items - in_stock) == 0:
        result.add(recipe)
if len(result) > 0:
    print("\n".join(sorted(result)))
else:
    print("Готовить нечего")
```

O. Двоичная статистика!
```python
numbers = input().split()
result = []
for n in numbers:
    b = bin(int(n))[2:]
    result.append({
        "digits": len(b),
        "units": b.count("1"),
        "zeros": b.count("0")
    })
print(result)
```

P. Зайка — 10
```python
result = set()
while (line := input()) != "":
    items = line.split()
    for i in range(len(items)):
        if items[i] == "зайка":
            if i > 0:
                result.add(items[i - 1])
            if i < len(items) - 1:
                result.add(items[i + 1])
print("\n".join(result))
```

Q. Друзья друзей
```python
persons = dict()
while (line := input()) != "":
    x, y = line.split()
    persons[x] = persons.get(x, set()) | {y}
    persons[y] = persons.get(y, set()) | {x}
for x in sorted(persons.keys()):
    level_1 = persons[x]
    level_2 = set()
    for y in level_1:
        level_2 = level_2 | persons[y]
    level_2 = level_2 - level_1 - {x}
    print(f"{x}: {', '.join(sorted(level_2))}")
```

R. Карта сокровищ
```python
counters = dict()
for _ in range(int(input())):
    x, y = input().split()
    group = x[:-1] + " " + y[:-1]
    counters[group] = counters.get(group, 0) + 1
print(max(counters.values()))
```

S. Частная собственность
```python
toys = set()
uniques = set()
for _ in range(int(input())):
    for toy in set(input().split(": ")[1].split(", ")):
        if toy in toys:
            uniques.discard(toy)
        else:
            toys.add(toy)
            uniques.add(toy)
print("\n".join(sorted(uniques)))
```

T. Простая задача 4.0
```python
numbers = []
for n in set(input().split("; ")):
    numbers.append(int(n))
numbers.sort()
primes = dict()
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        a, b = numbers[i], numbers[j]
        while b:
            a, b = b, a % b
        if a == 1:
            primes[numbers[i]] = primes.get(numbers[i], []) + [str(numbers[j])]
            primes[numbers[j]] = primes.get(numbers[j], []) + [str(numbers[i])]
    if numbers[i] in primes:
        print(f"{numbers[i]} - {', '.join(primes[numbers[i]])}")
```