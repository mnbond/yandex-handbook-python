from requests import get

response = get("http://" + input())
total_sum = sum(x for x in response.json() if isinstance(x, int))
print(total_sum)
