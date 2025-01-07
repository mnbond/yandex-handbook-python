# Решение задач из хэндбука Яндекс «Основы Python», глава 4

## Параграф 4.3. Рекурсия. Декораторы. Генераторы

A. Рекурсивный сумматор
```python
def recursive_sum(*numbers):
    if len(numbers) == 0:
        return 0
    return numbers[-1] + recursive_sum(*numbers[:-1])
```

B. Рекурсивный сумматор цифр
```python
def recursive_digit_sum(number):
    if number == 0:
        return 0
    return number % 10 + recursive_digit_sum(number // 10)
```

C. Многочлен N-ой степени
```python
def make_equation(*coefs):
    if len(coefs) == 1:
        return coefs[0]
    return f"({make_equation(*coefs[:-1])}) * x + {coefs[-1]}"
```

D. Декор результата
```python
def answer(old_func):
    def new_func(*args, **kwargs):
        return f"Результат функции: {old_func(*args, **kwargs)}"
    
    return new_func
```

E. Накопление результата
```python
def result_accumulator(old_func):
    queue = []

    def new_func(*args, method="accumulate"):
        nonlocal queue
        queue.append(old_func(*args))
        if method == "drop":
            result = queue.copy()
            queue.clear()
            return result

    return new_func
```

F. Сортировка слиянием
```python
def merge(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) or j < len(b):
        if j == len(b) or (i < len(a) and j < len(b) and a[i] < b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    return result


def merge_sort(items):
    if len(items) == 1:
        return items
    return merge(merge_sort(items[:len(items) // 2]), 
                 merge_sort(items[len(items) // 2:]))
```

G. Однотипность не порок
```python
def same_type(old_func):
    def new_func(*args):
        if len({type(x) for x in args}) > 1:
            print("Обнаружены различные типы данных")
            return False
        return old_func(*args)
    
    return new_func
```

H. Генератор Фибоначчи
```python
def fibonacci(n):
    prev, curr = 0, 1
    for i in range(n):
        yield prev
        prev, curr = curr, prev + curr
```

I. Циклический генератор
```python
def cycle(items):
    while True:
        for item in items:
            yield item
```

J. «Выпрямление» списка
```python
def make_linear(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(make_linear(item))
        else:
            result.append(item)
    return result
```