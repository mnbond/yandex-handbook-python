import json

with open(users_file_name := input(), "r", encoding="UTF-8") as file_in:
    users = json.load(file_in)

with open(input(), "r", encoding="UTF-8") as file_in:
    updates = json.load(file_in)

result = dict()
for user in users:
    result[user["name"]] = {key: value for key, value in user.items() if key != "name"}
for user in updates:
    for key, value in user.items():
        if key != "name" and value > result[user["name"]].get(key, ""):
            result[user["name"]][key] = value

with open(users_file_name, "w", encoding="UTF-8") as file_out:
    json.dump(result, file_out, ensure_ascii=False, indent=4)
