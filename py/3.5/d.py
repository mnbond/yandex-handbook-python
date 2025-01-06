from sys import stdin

lines = stdin.readlines()
query = lines.pop().rstrip("\n").lower()
print("".join(x for x in lines if query in x.lower()), end="")
