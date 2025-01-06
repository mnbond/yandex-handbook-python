import json

with open("scoring.json", "r", encoding="UTF-8") as file_in:
    scoring = json.load(file_in)

points = 0
for group in scoring:
    counter = sum(1 for test in group["tests"] if test["pattern"] == input())
    points += counter * group["points"] // len(group["tests"])
print(points)
