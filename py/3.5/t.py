with open("numbers.num", "rb") as file_in:
    data = file_in.read()
print(sum(data[i] * 256 + data[i + 1] for i in range(0, len(data), 2)) % 65536)
