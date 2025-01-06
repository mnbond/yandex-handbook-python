line_1 = input()
line_2 = input()
line_3 = input()
query = "зайка"
result = ""
if query in line_1:
    result = line_1
if query in line_2 and (result == "" or line_2 < result):
    result = line_2
if query in line_3 and (result == "" or line_3 < result):
    result = line_3
print(result, len(result))
