# Решение задач из хэндбука Яндекс «Основы Python», глава 3

## Параграф 3.4. Встроенные возможности по работе с коллекциями

A. Автоматизация списка
```python
for index, value in enumerate(input().split(), 1):
    print(f"{index}. {value}")
```

B. Сборы на прогулку
```python
for a, b in zip(input().split(", "), input().split(", ")):
    print(f"{a} - {b}")
```

C. Рациональная считалочка
```python
from itertools import count

start, finish, step = (float(x) for x in input().split())
for value in count(start, step):
    if value <= finish:
        print(f"{value:.2f}")
    else:
        break
```

D. Словарная ёлка
```python
from itertools import accumulate

words = [x + " " for x in input().split()]
for value in accumulate(words):
    print(value)
```

E. Список покупок
```python
from itertools import chain

goods = list(chain.from_iterable(input().split(", ") for _ in range(3)))
for index, value in enumerate(sorted(goods), 1):
    print(f"{index}. {value}")
```

F. Колода карт
```python
from itertools import product

nominals = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
suits = ["пик", "треф", "бубен", "червей"]
suits.remove(input())
for n, s in product(nominals, suits):
    print(n, s)
```

G. Игровая сетка
```python
from itertools import combinations

players = [input() for _ in range(int(input()))]
for a, b in combinations(players, 2):
    print(f"{a} - {b}")
```

H. Меню питания 2.0
```python
from itertools import cycle
from itertools import islice

porridges = [input() for _ in range(int(input()))]
for value in islice(cycle(porridges), 0, int(input())):
    print(value)
```

I. Таблица умножения 3.0
```python
from itertools import product

numbers = [x for x in range(1, int(input()) + 1)]
for n in numbers:
    print(" ".join(str(a * b) for a, b in product([n], numbers)))
```

J. Мы делили апельсин 2.0
```python
from itertools import product

count = int(input())
print("А Б В")
for a, b in product(range(1, count - 1), range(1, count - 1)):
    if a + b >= count:
        continue
    print(f"{a} {b} {count - a - b}")
```

K. Числовой прямоугольник 3.0
```python
from itertools import product

rows, cols = int(input()), int(input())
width = len(str(rows * cols))
for n, m in product(range(rows), range(cols)):
    print(f"{n * cols + m + 1: >{width}} ", end="")
    if m == cols - 1:
        print()
```

L. Список покупок 2.0
```python
from itertools import chain

goods_iter = chain.from_iterable(input().split(", ") for _ in range(int(input())))
for index, value in enumerate(sorted(goods_iter), 1):
    print(f"{index}. {value}")
```

M. Расстановка спортсменов
```python
from itertools import permutations

for values in permutations(sorted(input() for _ in range(int(input())))):
    print(", ".join(values))
```

N. Спортивные гадания
```python
from itertools import permutations

for values in permutations(sorted(input() for _ in range(int(input()))), 3):
    print(", ".join(values))
```

O. Список покупок 3.0
```python
from itertools import chain
from itertools import permutations

goods_iter = chain.from_iterable(input().split(", ") for _ in range(int(input())))
for values in permutations(sorted(goods_iter), 3):
    print(" ".join(values))
```

P. Расклад таков...
```python
from itertools import combinations, product

suits = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
nominals = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
necessary_suit = input()
nominals.remove(input())
counter = 0
for combination in combinations(product(sorted(nominals), sorted(suits.keys())), 3):
    if necessary_suit not in (s for _, s in combination):
        continue
    print(", ".join(f"{n} {suits[s]}" for n, s in combination))
    counter += 1
    if counter >= 10:
        break
```

Q. А есть ещё варианты?
```python
from itertools import combinations, product

suits = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
nominals = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
necessary_suit = input()
nominals.remove(input())
last_combination = input()
flag = False
for combination in combinations(product(sorted(nominals), sorted(suits.keys())), 3):
    if necessary_suit not in (s for _, s in combination):
        continue
    current_combination = ", ".join(f"{n} {suits[s]}" for n, s in combination)
    if flag:
        print(current_combination)
        break
    else:
        flag = current_combination == last_combination
```

R. Таблица истинности
```python
from itertools import product

expression = input()
print("a b c f")
for a, b, c in product((False, True), repeat=3):
    print(" ".join(str(int(x)) for x in (a, b, c, eval(expression))))
```

S. Таблица истинности 2
```python
from itertools import product

expression = input()
variables = sorted(set(x for x in expression if x.isupper()))
print(" ".join(variables), "F")
for values in product((False, True), repeat=len(variables)):
    f = eval(expression, None, {x: y for x, y in zip(variables, values)})
    print(" ".join(str(int(x)) for x in values + (f, )))
```

T. Таблица истинности 3
```python
from itertools import product

expression = input()
operators = ["not", "and", "or", "->", "~", "^"]
variables = sorted(set(x for x in expression if x.isupper()))

rpn_expression = []
stack = []
for x in expression.replace("(", "( ").replace(")", " )").split():
    if x in variables:
        rpn_expression.append(x)
    elif x in operators:
        while len(stack) and stack[-1] != "(" and operators.index(stack[-1]) < operators.index(x):
            rpn_expression.append(stack.pop())
        stack.append(x)
    elif x == "(":
        stack.append(x)
    elif x == ")":
        while stack[-1] != "(":
            rpn_expression.append(stack.pop())
        stack.pop()
rpn_expression.extend(reversed(stack))

print(" ".join(variables), "F")
for values in product((False, True), repeat=len(variables)):
    f = []
    for x in rpn_expression:
        if x in variables:
            f.append(values[variables.index(x)])
        elif x == "not":
            f.append(not f.pop())
        else:
            b, a = f.pop(), f.pop()
            if x == "and":
                f.append(a and b)
            elif x == "or":
                f.append(a or b)
            elif x == "->":
                f.append(not a or b)
            elif x == "~":
                f.append(not a and not b or a and b)
            elif x == "^":
                f.append(a and not b or not a and b)
    print(" ".join(str(int(x)) for x in values + (f[0], )))
```