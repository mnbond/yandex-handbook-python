with open(input(), "r", encoding="UTF-8") as file_in:
    numbers = [int(x) for x in file_in.read().split()]
print(count := len(numbers))
print(len([x for x in numbers if x > 0]))
print(min(numbers))
print(max(numbers))
print(total_sum := sum(numbers))
print(round(total_sum / count, 2))
