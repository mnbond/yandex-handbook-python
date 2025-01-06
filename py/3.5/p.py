from sys import stdin

query = input().lower()
flag = False
for file_name in stdin.read().split():
    with open(file_name, "r", encoding="UTF-8") as file_in:
        if query in " ".join(file_in.read().replace("&nbsp;", " ").lower().split()):
            print(file_name)
            flag = True
if not flag:
    print("404. Not Found")
