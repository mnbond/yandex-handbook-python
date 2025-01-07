# Решение задач из хэндбука Яндекс «Основы Python», глава 5

## Параграф 5.3. Модель исключений Python. Try, except, else, finally. Модули

A. Обработка ошибок
```python
try:
    func()
except Exception as e:
    print(e.__class__.__name__)
else:
    print("No Exceptions")
```

B. Ломать — не строить
```python
try:
    func(None, "None")
except Exception:
    print("Ура! Ошибка!")
```

C. Ломать — не строить 2
```python
class Defective:

    def __repr__(self):
        raise Exception


try:
    func(Defective())
except Exception:
    print("Ура! Ошибка!")
```

D. Контроль параметров
```python
def only_positive_even_sum(a, b):
    if not all(isinstance(x, int) for x in (a, b)):
        raise TypeError
    if not all(x > 0 and x % 2 == 0 for x in (a, b)):
        raise ValueError
    return a + b
```

E. Слияние с проверкой
```python
def is_iterable(x):
    try:
        iter(x)
    except Exception:
        raise StopIteration
    return True


def is_same_type(elements):
    for i in range(len(elements) - 1):
        if not isinstance(elements[i], type(elements[i + 1])):
            raise TypeError
    return True


def is_sorted(elements):
    for i in range(len(elements) - 1):
        if elements[i] > elements[i + 1]:
            raise ValueError
    return True


def merge(a, b):
    if (is_iterable(a) and is_iterable(b) 
        and is_same_type((*a, *b)) 
        and is_sorted(a) and is_sorted(b)):
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
```

F. Корень зла 2
```python
class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError
    d = b ** 2 - 4 * a * c
    if a == 0 and b == 0 and c == 0:
        raise InfiniteSolutionsError
    elif (a == 0 and b == 0) or d < 0:
        raise NoSolutionsError
    elif a == 0:
        roots = [-c / b, -c / b]
    elif d == 0:
        roots = [-b / (2 * a), -b / (2 * a)]
    else:
        roots = [(-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a)]
    return tuple(sorted(roots))
```

G. Валидация имени
```python
class CyrillicError(ValueError):
    pass


class CapitalError(ValueError):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    elif not all(x in "абвгдеёжзийклмнопрстуфхцчшщьыъэюя" for x in name.lower()):
        raise CyrillicError
    elif name != name.capitalize():
        raise CapitalError
    return name
```

H. Валидация имени пользователя
```python
class BadCharacterError(ValueError):
    pass


class StartsWithDigitError(ValueError):
    pass


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError
    elif not all("a" <= x <= "z" or x == "_" or x.isdigit() for x in username.lower()):
        raise BadCharacterError
    elif username[0].isdigit():
        raise StartsWithDigitError
    return username
```

I. Валидация пользователя
```python
class CyrillicError(ValueError):
    pass


class CapitalError(ValueError):
    pass


class BadCharacterError(ValueError):
    pass


class StartsWithDigitError(ValueError):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    elif not all(x in "абвгдеёжзийклмнопрстуфхцчшщьыъэюя" for x in name.lower()):
        raise CyrillicError
    elif name != name.capitalize():
        raise CapitalError
    return name


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError
    elif not all("a" <= x <= "z" or x == "_" or x.isdigit() for x in username.lower()):
        raise BadCharacterError
    elif username[0].isdigit():
        raise StartsWithDigitError
    return username


def user_validation(**kwargs):
    if set(kwargs) != {"last_name", "first_name", "username"}:
        raise KeyError
    kwargs["last_name"] = name_validation(kwargs["last_name"])
    kwargs["first_name"] = name_validation(kwargs["first_name"])
    kwargs["username"] = username_validation(kwargs["username"])
    return kwargs
```

J. Валидация пароля
```python
from hashlib import sha256


class MinLengthError(ValueError):
    pass


class PossibleCharError(ValueError):
    pass


class NeedCharError(ValueError):
    pass


def password_validation(password, min_length=8, 
                        possible_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", 
                        at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    elif len(password) < min_length:
        raise MinLengthError
    elif not all(x in possible_chars for x in password):
        raise PossibleCharError
    elif not any(at_least_one(x) for x in password):
        raise NeedCharError
    return sha256(password.encode("utf-8")).hexdigest()
```