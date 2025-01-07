# Решение задач из хэндбука Яндекс «Основы Python», глава 6

## Параграф 6.1. Модули math и numpy

A. Математика — круто, но это не точно
```python
import math

x = float(input())
f = math.log(math.pow(x, 3 / 16), 32)
f += math.pow(x, math.cos(math.pi * x / (2 * math.e)))
f -= math.pow(math.sin(x / math.pi), 2)
print(f)
```

B. Потоковый НОД
```python
from math import gcd
from sys import stdin

for line in stdin:
    print(gcd(*map(int, line.split())))
```

C. Есть варианты?
```python
from math import comb

n, m = map(int, input().split())
print(m * comb(n, m) // n, comb(n, m))
```

D. Среднее не арифметическое
```python
import math

numbers = list(map(float, input().split()))
result = math.pow(math.prod(numbers), 1 / len(numbers))
print(result)
```

E. Шаг навстречу
```python
import math

x, y = map(float, input().split())
ro, phi = map(float, input().split())
result = math.dist((x, y), (math.cos(phi) * ro, math.sin(phi) * ro))
print(result)
```

F. Матрица умножения
```python
import numpy as np


def multiplication_matrix(n):
    return np.arange(1, n + 1) * np.arange(1, n + 1).reshape(n, 1)
```

G. Шахматная подготовка
```python
import numpy as np


def make_board(n):
    board = np.zeros((n, n), dtype="int8")
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board
```

H. Числовая змейка 3.0
```python
import numpy as np


def snake(width, height, direction="H"):
    if direction == "V":
        width, height = height, width
    matrix = np.arange(1, width * height + 1, dtype="int16").reshape(height, width)
    matrix[1::2, :] = matrix[1::2, ::-1]
    if direction == "V":
        matrix = matrix.transpose()
    return matrix
```

I. Вращение
```python
import numpy as np


def rotate(matrix, degrees):
    return np.rot90(matrix, -degrees // 90)
```

J. Лесенка
```python
import numpy as np


def stairs(vector):
    n = len(vector)
    matrix = np.zeros((n, n), dtype=vector.dtype)
    for i in np.arange(n):
        matrix[i] = np.roll(vector, i)
    return matrix
```