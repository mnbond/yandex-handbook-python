from sys import stdin

count, difference = 0, 0
for line in stdin:
    info = line.split()
    difference += int(info[2]) - int(info[1])
    count += 1
print(round(difference / count))
