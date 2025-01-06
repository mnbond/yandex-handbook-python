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
