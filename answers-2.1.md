# Решение задач из хэндбука Яндекс «Основы Python»

## Глава 2.1. Ввод и вывод данных. Операции с числами, строками. Форматирование

A. Привет, Яндекс!
```
print("Привет, Яндекс!")
```

B. Привет, всем!
```
print("Как Вас зовут?")
name = input()
print(f"Привет, {name}")
```

C. Излишняя автоматизация
```
phrase = input()
print((phrase + "\n") * 3)
```

D. Сдача
```
payment = int(input())
print(int(payment - 2.5 * 38))
```

E. Магазин
```
price = int(input())
weight = int(input())
payment = int(input())
print(payment - weight * price)
```

F. Чек
```
item = input()
price = int(input())
weight = int(input())
payment = int(input())
print("Чек")
print(f"{item} - {weight}кг - {price}руб/кг")
print(f"Итого: {price * weight}руб")
print(f"Внесено: {payment}руб")
print(f"Сдача: {payment - price * weight}руб")
```

G. Делу — время, потехе — час
```
count = int(input())
phrase = "Купи слона!"
print((phrase + "\n") * count)
```

H. Наказание
```
count = int(input())
phrase = input()
print(f'Я больше никогда не буду писать "{phrase}"!\n' * count)
```

I. Деловая колбаса
```
minutes = int(input())
children = int(input())
print(children * minutes // 2)
```

J. Детский сад — штаны на лямках
```
name = input()
box = int(input())
print(f"Группа №{box // 100}.")
print(f"{box % 10}. {name}.")
print(f"Шкафчик: {box}.")
print(f"Кроватка: {box // 10 % 10}.")
```

K. Автоматизация игры
```
n = int(input())
print(n // 100 % 10, n // 1000, n % 10, n // 10 % 10, sep="")
```

L. Интересное сложение
```
a = int(input())
b = int(input())
result = (a % 10 + b % 10) % 10 \
         + (a // 10 % 10 + b // 10 % 10) % 10 * 10 \
         + (a // 100 % 10 + b // 100 % 10) % 10 * 100
print(result)
```

M. Дед Мороз и кофеты
```
children = int(input())
candies = int(input())
print(candies // children)
print(candies % children)
```

N. Шарики и ручки
```
red = int(input())
green = int(input())
blue = int(input())
print(red + blue + 1)
```

O. В ожидании доставки
```
hours = int(input())
minutes = int(input())
duration = int(input())
delivery_hours = (hours + (minutes + duration) // 60) % 24
delivery_minutes = (minutes + duration) % 60
print(f"{str(delivery_hours):0>2}:{str(delivery_minutes):0>2}")
```

P. Доставка
```
warehouse = int(input())
store = int(input())
speed = int(input())
print(f"{(store - warehouse) / speed:.2f}")
```

Q. Ошибка кассового аппарата
```
total = int(input())
last_order = int(input(), 2)
print(total + last_order)
```

R. Сдача 10
```
price = int(input(), 2)
payment = int(input())
print(payment - price)
```

S. Украшение чека
```
product = input()
price = int(input())
weight = int(input())
payment = int(input())
print(f"{'Чек':=^35}")
print("Товар:", f"{product: >28}")
print("Цена:", f"{f'{weight}кг * {price}руб/кг': >29}")
print("Итого:", f"{weight * price: >25}руб")
print("Внесено:", f"{payment: >23}руб")
print("Сдача:", f"{payment - weight * price: >25}руб")
print("=" * 35)
```

T. Мухи отдельно, котлеты отдельно
```
weight = int(input())
price = int(input())
first_price = int(input())
second_price = int(input())
first_weight = (price - second_price) * weight // (first_price - second_price)
second_weight = weight - first_weight
print(first_weight, second_weight)
```