from requests import get

response = get("http://" + input())
key = input()
print(response.json().get(key, "No data"))
