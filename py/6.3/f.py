from requests import get

response = get("http://" + input() + "/users")
users = [f'{x["last_name"]} {x["first_name"]}' for x in response.json()]
print(*sorted(users), sep="\n")
