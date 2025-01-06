import json

with open(input(), "r", encoding="UTF-8") as file_in:
    numbers = [int(x) for x in file_in.read().split()]

statistics = {
    "count": (count := len(numbers)),
    "positive_count": len([x for x in numbers if x > 0]),
    "min": min(numbers),
    "max": max(numbers),
    "sum": (total_sum := sum(numbers)),
    "average": round(total_sum / count, 2)
}

with open(input(), "w", encoding="UTF-8") as file_out:
    json.dump(statistics, file_out, ensure_ascii=False, indent=4)
