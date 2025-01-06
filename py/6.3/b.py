from requests import get

address = "http://" + input()
total_sum = 0
while (value := int(get(address).text)) != 0:
    total_sum += value
print(total_sum)
