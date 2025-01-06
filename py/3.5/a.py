from sys import stdin

total_sum = 0
for line in stdin:
    for n in line.split():
        total_sum += int(n)
print(total_sum)
