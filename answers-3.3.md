# Решение задач из хэндбука Яндекс «Основы Python», глава 3

## Параграф 3.3. Списочные выражения. Модель памяти для типов языка Python

A. Список квадратов
```python
[x ** 2 for x in range(a, b + 1)]
```

B. Таблица умножения 2.0
```python
[[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
```

C. Длины всех слов
```python
[len(x) for x in sentence.split()]
```

D. Множество нечетных чисел
```python
{x for x in numbers if x % 2 != 0}
```

E. Множество всех полных квадратов
```python
{x for x in numbers if (x ** 0.5).is_integer()}
```

F. Буквенная статистика
```python
{x: text.lower().count(x) for x in text.lower() if x.isalpha()}
```

G. Делители
```python
{i: [j for j in range(1, i + 1) if i % j == 0] for i in numbers}
```

H. Аббревиатура
```python
"".join([x[0].upper() for x in string.split()])
```

I. Преобразование в строку
```python
" - ".join([str(x) for x in sorted(set(numbers))])
```

J. RLE наоборот
```python
"".join([i * j for i, j in rle])
```