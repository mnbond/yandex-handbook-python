# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 6.3

### 6.3. Модуль requests

A. Проверка системы
```python
from requests import get

response = get("http://127.0.0.1:5000")
print(response.text)
```

B. Суммирование ответов
```python
from requests import get

address = "http://" + input()
total_sum = 0
while (value := int(get(address).text)) != 0:
    total_sum += value
print(total_sum)
```

C. Суммирование ответов 2
```python
from requests import get

response = get("http://" + input())
total_sum = sum(x for x in response.json() if isinstance(x, int))
print(total_sum)
```

D. Конкретное значение
```python
from requests import get

response = get("http://" + input())
key = input()
print(response.json().get(key, "No data"))
```

E. Суммирование ответов 3
```python
from sys import stdin
from requests import get

total_sum = 0
address = "http://" + input()
pathes = [x.strip() for x in stdin.readlines()]
total_sum = sum(sum(get(address + x).json()) for x in pathes)
print(total_sum)
```

F. Список пользователей
```python
from requests import get

response = get("http://" + input() + "/users")
users = [f'{x["last_name"]} {x["first_name"]}' for x in response.json()]
print(*sorted(users), sep="\n")
```

G. Рассылка сообщений
```python
from sys import stdin
from requests import get

address = "http://" + input() + "/users/" + input()
template = stdin.read()
try:
    user = get(address).json()
except Exception:
    print("Пользователь не найден")
else:
    for key in user:
        template = template.replace("{" + key + "}", str(user[key]))
    print(template)
```

H. Регистрация нового пользователя
```python
from requests import post
from json import dumps

address = "http://" + input() + "/users"
new_user = {x: input() for x in ["username", "last_name", "first_name", "email"]}
post(address, data=dumps(new_user))
```

I. Изменение данных
```python
from sys import stdin
from requests import put
from json import dumps

address = "http://" + input() + "/users/" + input()
updates = {x[0]: x[1] for x in [line.strip().split("=") for line in stdin.readlines()]}
put(address, data=dumps(updates))
```

J. Удаление данных
```python
from requests import delete

address = "http://" + input() + "/users/" + input()
delete(address)
```