LETTERS = "abcdefghijklmnopqrstuvwxyz"
shift = int(input())

with open("public.txt", "r", encoding="UTF-8") as file_in:
    public = file_in.read()

private = list(public.lower())
for i in range(len(private)):
    if private[i] in LETTERS:
        private[i] = LETTERS[(LETTERS.index(private[i]) + shift) % len(LETTERS)]
    if public[i].isupper():
        private[i] = private[i].upper()

with open("private.txt", "w", encoding="UTF-8") as file_in:
    file_in.write("".join(private))
