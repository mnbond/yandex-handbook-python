import os

UNITS = ["Б", "КБ", "МБ", "ГБ"]
size = os.stat(input()).st_size
p = 0
while size >= 1024 and p < len(UNITS) - 1:
    size = -(-size // 1024)
    p += 1
print(f"{size}{UNITS[p]}")
