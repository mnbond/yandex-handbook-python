words = []
for _ in range(2):
    with open(input(), "r", encoding="UTF-8") as file_in:
        words.append(set(file_in.read().split()))

with open(input(), "w", encoding="UTF-8") as file_out:
    file_out.write("\n".join(sorted(words[0] ^ words[1])))
