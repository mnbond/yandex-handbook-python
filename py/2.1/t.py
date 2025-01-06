weight = int(input())
price = int(input())
first_price = int(input())
second_price = int(input())
first_weight = (price - second_price) * weight // (first_price - second_price)
second_weight = weight - first_weight
print(first_weight, second_weight)
