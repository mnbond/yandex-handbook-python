total_sum = 0
while (price := float(input())) != 0:
    if price < 500:
        total_sum += price
    else:
        total_sum += price * 0.9
print(total_sum)
