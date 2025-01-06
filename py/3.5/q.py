with open("secret.txt", "r", encoding="UTF-8") as file_in:
    print("".join(chr(ord(x) % 256) for x in file_in.read()))
